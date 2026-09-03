"""Create the synthetic vendor-assurance tables in the training Dataverse environment.

Safe to re-run: existing tables and columns return an error that is reported and skipped.
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


def label(text: str) -> dict:
    """Build a Dataverse localized label."""
    return {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
            {
                "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
                "Label": text,
                "LanguageCode": 1033,
            }
        ],
    }


def string_column(name: str, display: str, length: int) -> dict:
    """Define a single-line text column."""
    return {
        "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
        "SchemaName": f"{PREFIX}_{name}",
        "MaxLength": length,
        "RequiredLevel": {"Value": "None"},
        "DisplayName": label(display),
    }


def memo_column(name: str, display: str) -> dict:
    """Define a multi-line text column."""
    return {
        "@odata.type": "Microsoft.Dynamics.CRM.MemoAttributeMetadata",
        "SchemaName": f"{PREFIX}_{name}",
        "MaxLength": 4000,
        "RequiredLevel": {"Value": "None"},
        "DisplayName": label(display),
    }


def integer_column(name: str, display: str, minimum: int, maximum: int) -> dict:
    """Define a bounded whole-number column."""
    return {
        "@odata.type": "Microsoft.Dynamics.CRM.IntegerAttributeMetadata",
        "SchemaName": f"{PREFIX}_{name}",
        "MinValue": minimum,
        "MaxValue": maximum,
        "RequiredLevel": {"Value": "None"},
        "DisplayName": label(display),
    }


def date_column(name: str, display: str) -> dict:
    """Define a date-only column."""
    return {
        "@odata.type": "Microsoft.Dynamics.CRM.DateTimeAttributeMetadata",
        "SchemaName": f"{PREFIX}_{name}",
        "Format": "DateOnly",
        "DateTimeBehavior": {"Value": "DateOnly"},
        "RequiredLevel": {"Value": "None"},
        "DisplayName": label(display),
    }


def create_table(name: str, display: str, plural: str, primary: str) -> None:
    """Create a user-owned table with a primary name column."""
    body = {
        "@odata.type": "Microsoft.Dynamics.CRM.EntityMetadata",
        "SchemaName": f"{PREFIX}_{name}",
        "DisplayName": label(display),
        "DisplayCollectionName": label(plural),
        "OwnershipType": "UserOwned",
        "HasActivities": False,
        "HasNotes": False,
        "IsActivity": False,
        "Attributes": [
            {
                "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
                "SchemaName": f"{PREFIX}_{primary}",
                "MaxLength": 200,
                "IsPrimaryName": True,
                "RequiredLevel": {"Value": "ApplicationRequired"},
                "DisplayName": label(primary),
            }
        ],
    }
    status, text = call("POST", "EntityDefinitions", body)
    print(f"table {PREFIX}_{name}: {status} {'ok' if status < 300 else text}")


def add_column(table: str, column: dict) -> None:
    """Add one column to an existing table."""
    status, text = call("POST", f"EntityDefinitions(LogicalName='{PREFIX}_{table}')/Attributes", column)
    print(f"  column {column['SchemaName']}: {status} {'ok' if status < 300 else text}")


def main() -> None:
    """Provision both training tables."""
    create_table("vendorreview", "Vendor Review", "Vendor Reviews", "Vendor")
    for column in (
        string_column("System", "System", 200),
        string_column("DataTypes", "Data types", 200),
        string_column("HostingRegion", "Hosting region", 200),
        string_column("DataResidency", "Data residency", 400),
        string_column("SubProcessors", "Sub-processors", 400),
        string_column("Soc2Type", "SOC 2 type", 50),
        date_column("ReportDate", "Report date"),
        integer_column("Score", "Score", 0, 10),
        string_column("Sensitivity", "Sensitivity", 20),
        memo_column("Gaps", "Gaps"),
    ):
        add_column("vendorreview", column)

    create_table("controlfinding", "Control Finding", "Control Findings", "Control")
    for column in (
        string_column("Status", "Status", 20),
        memo_column("Evidence", "Evidence"),
        string_column("Reasoning", "Reasoning", 500),
    ):
        add_column("controlfinding", column)


if __name__ == "__main__":
    main()
