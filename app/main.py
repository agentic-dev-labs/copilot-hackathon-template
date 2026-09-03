"""Minimal vendor review web app.

Reads vendor reviews from Dataverse when configured, and falls back to evaluating the
local synthetic samples so the app runs in a Codespace with no credentials at all.
"""

from __future__ import annotations

import html
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.config import load

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = ROOT / "src" / "vendor_assurance" / "samples"

DATAVERSE_URL = os.environ.get("DATAVERSE_URL", "").rstrip("/")
CLIENT_ID = os.environ.get("DATAVERSE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("DATAVERSE_CLIENT_SECRET", "")
TENANT_ID = os.environ.get("DATAVERSE_TENANT_ID", "")
PREFIX = os.environ.get("DATAVERSE_PREFIX", "cr522")

app = FastAPI()


def _dataverse_token() -> str:
    body = urllib.parse.urlencode(
        {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "scope": f"{DATAVERSE_URL}/.default",
            "grant_type": "client_credentials",
        }
    ).encode()
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    with urllib.request.urlopen(urllib.request.Request(url, data=body)) as response:
        return json.loads(response.read())["access_token"]


def _from_dataverse(attendee: str) -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "$select": f"{PREFIX}_vendor,{PREFIX}_score,{PREFIX}_sensitivity,{PREFIX}_attendee",
            "$filter": f"{PREFIX}_attendee eq '{attendee}'",
        }
    )
    request = urllib.request.Request(f"{DATAVERSE_URL}/api/data/v9.2/{PREFIX}_vendorreviews?{params}")
    request.add_header("Authorization", f"Bearer {_dataverse_token()}")
    request.add_header("Accept", "application/json")
    with urllib.request.urlopen(request) as response:
        rows = json.loads(response.read())["value"]
    return [
        {
            "vendor": row.get(f"{PREFIX}_vendor", ""),
            "score": row.get(f"{PREFIX}_score"),
            "sensitivity": row.get(f"{PREFIX}_sensitivity", ""),
        }
        for row in rows
    ]


def _from_samples() -> list[dict]:
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
def index() -> str:
    """Render the attendee's vendor review list."""
    settings = load()
    source = "Dataverse"
    try:
        if not (DATAVERSE_URL and CLIENT_ID and CLIENT_SECRET and TENANT_ID):
            raise RuntimeError("Dataverse is not configured")
        reviews = _from_dataverse(settings["displayName"])
        if not reviews:
            source = "Dataverse (no rows yet for you)"
    except Exception:  # noqa: BLE001 - the fallback must work for any failure
        reviews = _from_samples()
        source = "local synthetic samples"

    rows = "\n".join(
        f"<tr><td>{html.escape(str(item['vendor']))}</td>"
        f"<td class='score'>{html.escape(str(item['score']))}/10</td>"
        f"<td>{html.escape(str(item['sensitivity']))}</td></tr>"
        for item in reviews
    ) or "<tr><td colspan='3'>No reviews yet.</td></tr>"

    name = html.escape(settings["displayName"])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{name} - Vendor Reviews</title>
<style>
 body {{ font-family: Segoe UI, system-ui, sans-serif; margin: 3rem auto; max-width: 46rem; }}
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
</html>"""
