"""Evaluate the synthetic sample reports and write the results into Dataverse."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.config import load  # noqa: E402
from src.vendor_assurance.chunker import chunk_document  # noqa: E402
from src.vendor_assurance.evaluator import evaluate_document  # noqa: E402

ORG = os.environ.get("DATAVERSE_URL", "https://org0ef69385.crm.dynamics.com").rstrip("/")
API = f"{ORG}/api/data/v9.2"
PREFIX = os.environ.get("DATAVERSE_PREFIX", "cr522")
SAMPLES = ROOT / "src" / "vendor_assurance" / "samples"


def _token() -> str:
    az = shutil.which("az") or "az"
    result = subprocess.run(
        [az, "account", "get-access-token", "--resource", f"{ORG}/", "--query", "accessToken", "-o", "tsv"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


ACCESS = _token()


def call(method: str, path: str, body: dict | None = None) -> tuple[int, str]:
    """Send one Dataverse Web API request and return the status and body."""
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(f"{API}/{path}", data=data, method=method)
    for key, value in {
        "Authorization": f"Bearer {ACCESS}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
    }.items():
        request.add_header(key, value)
    try:
        with urllib.request.urlopen(request) as response:
            return response.status, response.read().decode()
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode()[:500]


def main() -> None:
    """Replace only this attendee's rows, so seeding never touches anyone else's data."""
    attendee = load()["displayName"]
    escaped = attendee.replace("'", "''")
    mine = urllib.parse.urlencode(
        {"$select": f"{PREFIX}_vendorreviewid", "$filter": f"{PREFIX}_attendee eq '{escaped}'"}
    )
    _, existing = call("GET", f"{PREFIX}_vendorreviews?{mine}")
    for row in json.loads(existing).get("value", []):
        call("DELETE", f"{PREFIX}_vendorreviews({row[f'{PREFIX}_vendorreviewid']})")

    for sample in sorted(SAMPLES.glob("*.md")):
        evaluation = evaluate_document(chunk_document(sample.read_text(encoding="utf-8"), 220, 30))
        record = {
            f"{PREFIX}_vendor": evaluation.vendor,
            f"{PREFIX}_system": evaluation.system,
            f"{PREFIX}_datatypes": ", ".join(evaluation.data_types),
            f"{PREFIX}_hostingregion": evaluation.hosting_region,
            f"{PREFIX}_dataresidency": evaluation.data_residency,
            f"{PREFIX}_subprocessors": ", ".join(evaluation.subprocessors),
            f"{PREFIX}_soc2type": evaluation.soc2_type,
            f"{PREFIX}_reportdate": evaluation.report_date,
            f"{PREFIX}_score": evaluation.score,
            f"{PREFIX}_sensitivity": evaluation.sensitivity,
            f"{PREFIX}_gaps": "\n".join(evaluation.gaps) or "No gaps identified.",
            f"{PREFIX}_attendee": attendee,
        }
        status, text = call("POST", f"{PREFIX}_vendorreviews", record)
        print(f"{evaluation.vendor}: {status} score={evaluation.score} {'ok' if status < 300 else text}")

    query = urllib.parse.urlencode(
        {
            "$select": f"{PREFIX}_vendor,{PREFIX}_score,{PREFIX}_sensitivity",
            "$filter": f"{PREFIX}_attendee eq '{escaped}'",
        }
    )
    _, text = call("GET", f"{PREFIX}_vendorreviews?{query}")
    print(f"\nRows in Dataverse for {attendee}:")
    for row in json.loads(text).get("value", []):
        print(f"  {row[f'{PREFIX}_vendor']:<32} {row[f'{PREFIX}_score']}/10  {row[f'{PREFIX}_sensitivity']}")


if __name__ == "__main__":
    main()
