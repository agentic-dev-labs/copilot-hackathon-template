"""Add the attendee ownership column to the vendor review table.

Each attendee filters the shared table by their own name from config.yml, which avoids
provisioning one table per person.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import urllib.error
import urllib.request

ORG = os.environ.get("DATAVERSE_URL", "https://org0ef69385.crm.dynamics.com").rstrip("/")
API = f"{ORG}/api/data/v9.2"
PREFIX = os.environ.get("DATAVERSE_PREFIX", "cr522")


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
    """Send one Dataverse Web API request and return the status and truncated body."""
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
            return response.status, response.read().decode()[:400]
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode()[:400]


def main() -> None:
    """Add the attendee column, ignoring the error raised when it already exists."""
    column = {
        "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
        "SchemaName": f"{PREFIX}_Attendee",
        "MaxLength": 100,
        "RequiredLevel": {"Value": "None"},
        "DisplayName": {
            "@odata.type": "Microsoft.Dynamics.CRM.Label",
            "LocalizedLabels": [
                {
                    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
                    "Label": "Attendee",
                    "LanguageCode": 1033,
                }
            ],
        },
    }
    status, text = call(
        "POST", f"EntityDefinitions(LogicalName='{PREFIX}_vendorreview')/Attributes", column
    )
    print(f"column {PREFIX}_attendee: {status} {'ok' if status < 300 else text}")


if __name__ == "__main__":
    main()
