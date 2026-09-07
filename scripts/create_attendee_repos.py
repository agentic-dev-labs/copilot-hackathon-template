"""Create attendee repositories from the template and grant the attendee team access.

The facilitator must configure organization secret access separately. Each repository needs
an explicit team grant when organization base permission is `none`.
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
    return subprocess.run(command, capture_output=True, text=True, check=False, timeout=120)


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


def grant_team(name: str) -> bool:
    """Give the attendee team write access to the repository."""
    result = run([
        GH, "api", "-X", "PUT",
        f"/orgs/{ORG}/teams/{TEAM}/repos/{ORG}/{name}",
        "-f", "permission=push",
    ])
    print(f"  team access: {'ok' if result.returncode == 0 else result.stderr.strip()[:160]}")
    return result.returncode == 0


def main() -> int:
    """Create every requested repository and grant the attendee team access."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="+", help="repository names, for example nn-na-2026-10-team-01")
    args = parser.parse_args()

    failures = 0
    for name in args.names:
        if not create_repo(name) or not grant_team(name):
            failures += 1

    print("\nCheck Actions and Codespaces secret access separately for each repository.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
