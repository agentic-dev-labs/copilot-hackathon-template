"""Create attendee repositories from the template and give each one its deployment secrets.

Repository secrets are not copied when a repository is created from a template, and setting
organization secrets needs the admin:org scope. Creating the repository and setting its
secrets in one pass avoids both problems.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys

ORG = "agentic-dev-labs"
TEMPLATE = f"{ORG}/copilot-hackathon-template"
RESOURCE_GROUP = "rg-nn-hackathon-2026-10"
SUBSCRIPTION = "4bf7667a-1e78-40f4-b84b-08bed8e94602"
DATAVERSE_APP_ID = "10c9f0ab-08ad-449d-a0e6-5fdcaf3cddaa"

AZ = shutil.which("az") or "az"
GH = shutil.which("gh") or "gh"


def run(command: list[str], stdin: str | None = None) -> subprocess.CompletedProcess[str]:
    """Run a command, capturing output so secret values are never echoed."""
    return subprocess.run(command, input=stdin, capture_output=True, text=True, check=False)


def deploy_credentials() -> str:
    """Create a fresh deployment credential for the shared resource group."""
    scope = f"/subscriptions/{SUBSCRIPTION}/resourceGroups/{RESOURCE_GROUP}"
    result = run([
        AZ, "ad", "sp", "create-for-rbac",
        "--name", "nn-hackathon-deploy",
        "--role", "Contributor",
        "--scopes", scope,
        "--json-auth", "-o", "json",
    ])
    if result.returncode != 0:
        raise SystemExit(f"could not create deployment credential: {result.stderr[:300]}")
    return result.stdout.strip()


def dataverse_secret() -> str:
    """Add a client secret to the Dataverse app registration."""
    result = run([
        AZ, "ad", "app", "credential", "reset",
        "--id", DATAVERSE_APP_ID,
        "--append", "--display-name", "workshop",
        "--query", "password", "-o", "tsv",
    ])
    if result.returncode != 0:
        raise SystemExit(f"could not create Dataverse secret: {result.stderr[:300]}")
    return result.stdout.strip()


def create_repo(name: str) -> bool:
    """Create one private repository from the template."""
    full = f"{ORG}/{name}"
    if run([GH, "repo", "view", full]).returncode == 0:
        print(f"{name}: already exists")
        return True
    result = run([GH, "repo", "create", full, "--template", TEMPLATE, "--private"])
    if result.returncode != 0:
        print(f"{name}: FAILED {result.stderr.strip()[:200]}")
        return False
    print(f"{name}: created")
    return True


def set_secret(repo: str, key: str, value: str) -> None:
    """Set one repository secret without printing its value."""
    result = run([GH, "secret", "set", key, "--repo", f"{ORG}/{repo}"], stdin=value)
    print(f"  {key}: {'ok' if result.returncode == 0 else result.stderr.strip()[:160]}")


def main() -> None:
    """Create every requested repository and apply the shared secrets."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="+", help="repository names, for example nn-na-2026-10-team-01")
    args = parser.parse_args()

    azure = deploy_credentials()
    dataverse = dataverse_secret()
    json.loads(azure)  # fail fast if the credential payload is not valid JSON

    for name in args.names:
        if not create_repo(name):
            continue
        set_secret(name, "AZURE_CREDENTIALS", azure)
        set_secret(name, "DATAVERSE_CLIENT_SECRET", dataverse)

    print("\nDone. Secret values were never printed.")


if __name__ == "__main__":
    sys.exit(main())
