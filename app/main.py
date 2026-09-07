"""Minimal vendor review web app.

Reads vendor reviews from Dataverse when configured, and falls back to evaluating the
local synthetic samples so the app runs in a Codespace with no credentials at all.
"""

from __future__ import annotations

import html
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.config import load
from src.vendor_assurance.dataverse import DataverseClient, DataverseError

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = ROOT / "src" / "vendor_assurance" / "samples"

PREFIX = os.environ.get("DATAVERSE_PREFIX", "cr522")

app = FastAPI()


def _from_dataverse(attendee: str) -> list[dict]:
    """Load this attendee's display rows; the filter is not an access boundary."""
    escaped = attendee.replace("'", "''")
    rows = DataverseClient.from_environment().rows(
        f"{PREFIX}_vendorreviews",
        **{
            "$select": f"{PREFIX}_vendor,{PREFIX}_score,{PREFIX}_sensitivity,{PREFIX}_attendee",
            "$filter": f"{PREFIX}_attendee eq '{escaped}'",
        },
    )
    return [
        {
            "vendor": row.get(f"{PREFIX}_vendor", ""),
            "score": row.get(f"{PREFIX}_score"),
            "sensitivity": row.get(f"{PREFIX}_sensitivity", ""),
        }
        for row in rows
    ]


def _from_samples() -> list[dict]:
    """Evaluate the checked-in synthetic samples for the no-credentials path."""
    from src.vendor_assurance.chunker import chunk_document
    from src.vendor_assurance.evaluator import evaluate_document

    results = []
    for sample in sorted(SAMPLES.glob("*.md")):
        evaluation = evaluate_document(chunk_document(sample.read_text(encoding="utf-8"), 220, 30))
        results.append(
            {
                "vendor": evaluation.vendor,
                "score": evaluation.score,
                "sensitivity": evaluation.sensitivity,
            }
        )
    return results


@app.get("/healthz")
def healthz() -> dict[str, str]:
    """Liveness probe for the container platform."""
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def index() -> HTMLResponse:
    """Render the attendee's vendor review list."""
    try:
        settings = load()
    except (OSError, ValueError) as error:
        return HTMLResponse(
            f"<h1>Configuration needed</h1><p>{html.escape(str(error))}</p>", status_code=400,
        )
    if not os.environ.get("DATAVERSE_URL"):
        reviews = _from_samples()
        source = "local synthetic samples (Dataverse is not configured)"
    else:
        try:
            reviews = _from_dataverse(settings["displayName"])
            source = "Dataverse" if reviews else f"Dataverse - no rows tagged '{settings['displayName']}' yet"
        except (DataverseError, ValueError) as error:
            reviews = _from_samples()
            source = f"local synthetic samples (Dataverse unavailable: {error})"

    rows = "\n".join(
        f"<tr><td>{html.escape(str(item['vendor']))}</td>"
        f"<td class='score'>{html.escape(str(item['score']) + '/10') if item['score'] is not None else 'Not assessed'}</td>"
        f"<td>{html.escape(str(item['sensitivity']))}</td></tr>"
        for item in reviews
    ) or "<tr><td colspan='3'>No reviews yet.</td></tr>"

    name = html.escape(settings["displayName"])
    return HTMLResponse(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} - Vendor Reviews</title>
<style>
 body {{ font-family: Segoe UI, system-ui, sans-serif; margin: 3rem auto; padding: 0 1rem; max-width: 46rem; overflow-wrap: anywhere; }}
 h1 {{ margin-bottom: 0.2rem; }}
 p.source {{ color: #555; margin-top: 0; }}
 table {{ border-collapse: collapse; width: 100%; margin-top: 1.5rem; }}
 th, td {{ border-bottom: 1px solid #ddd; padding: 0.6rem; text-align: left; }}
 .score {{ font-variant-numeric: tabular-nums; }}
 footer {{ margin-top: 2rem; color: #777; font-size: 0.85rem; }}
</style>
</head>
<body>
 <h1>{name} - Vendor Reviews</h1>
 <p class="source">Source: {html.escape(source)}</p>
 <table>
  <thead><tr><th>Vendor</th><th>Score</th><th>Sensitivity</th></tr></thead>
  <tbody>{rows}</tbody>
 </table>
 <footer>Synthetic training data only.</footer>
</body>
</html>""")
