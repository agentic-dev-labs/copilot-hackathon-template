"""Create the Dataverse application user for the deployed app's identity.

Without this, the app registration authenticates to Entra successfully and then receives 403
from every Dataverse call, because it is not a user inside the environment.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import urllib.error
import urllib.parse
import urllib.request

ORG = os.environ.get("DATAVERSE_URL", "https://org0ef69385.crm.dynamics.com").rstrip("/")
API = f"{ORG}/api/data/v9.2"
APP_ID = os.environ.get("DATAVERSE_APP_ID", "10c9f0ab-08ad-449d-a0e6-5fdcaf3cddaa")
ROLE_NAME = os.environ.get("DATAVERSE_ROLE", "System Administrator")


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


def query(path: str, **params: str) -> dict:
    """Run a GET with URL-encoded OData parameters."""
    _, text = call("GET", f"{path}?{urllib.parse.urlencode(params)}")
    return json.loads(text)


def main() -> None:
    """Create the application user if needed and grant it a security role."""
    existing = query("systemusers", **{"$select": "systemuserid,applicationid", "$filter": f"applicationid eq {APP_ID}"})
    if existing.get("value"):
        user_id = existing["value"][0]["systemuserid"]
        print(f"application user exists: {user_id}")
    else:
        unit = query("businessunits", **{"$select": "businessunitid", "$filter": "parentbusinessunitid eq null"})
        unit_id = unit["value"][0]["businessunitid"]
        status, text = call(
            "POST",
            "systemusers",
            {"applicationid": APP_ID, "businessunitid@odata.bind": f"/businessunits({unit_id})"},
        )
        print(f"create application user: {status} {'ok' if status < 300 else text}")
        created = query("systemusers", **{"$select": "systemuserid", "$filter": f"applicationid eq {APP_ID}"})
        if not created.get("value"):
            print("application user was not created; stopping")
            return
        user_id = created["value"][0]["systemuserid"]

    roles = query("roles", **{"$select": "roleid,name", "$filter": f"name eq '{ROLE_NAME}'"})
    if not roles.get("value"):
        print(f"role not found: {ROLE_NAME}")
        return
    role_id = roles["value"][0]["roleid"]

    status, text = call(
        "POST",
        f"systemusers({user_id})/systemuserroles_association/$ref",
        {"@odata.id": f"{API}/roles({role_id})"},
    )
    print(f"assign role {ROLE_NAME}: {status} {'ok' if status < 300 else text}")


if __name__ == "__main__":
    main()
