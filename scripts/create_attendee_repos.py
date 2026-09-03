"""Create attendee repositories from the template and grant the attendee team access.

`AZURE_CREDENTIALS` and `DATAVERSE_CLIENT_SECRET` are organization secrets visible to all
repositories, so nothing needs to be copied per repository. Organization base permission is
`none`, so each repository still needs an explicit team grant.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys

ORG = "agentic-dev-labs"
TEMPLATE = f"{ORG}/copilot-hackathon-template"
TEAM = "hackathon-attendees"

GH = shutil.which("gh") or "gh"


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    """Run a command and capture its output."""
    return subprocess.run(command, capture_output=True, text=True, check=False)


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


def grant_team(name: str) -> None:
    """Give the attendee team write access to the repository."""
    result = run([
        GH, "api", "-X", "PUT",
        f"/orgs/{ORG}/teams/{TEAM}/repos/{ORG}/{name}",
        "-f", "permission=push",
    ])
    print(f"  team access: {'ok' if result.returncode == 0 else result.stderr.strip()[:160]}")


def main() -> None:
    """Create every requested repository and grant the attendee team access."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="+", help="repository names, for example nn-na-2026-10-team-01")
    args = parser.parse_args()

    for name in args.names:
        if create_repo(name):
            grant_team(name)

    print("\nOrganization secrets apply automatically; nothing is copied per repository.")


if __name__ == "__main__":
    sys.exit(main())
