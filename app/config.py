"""Read the attendee configuration and derive Azure-safe names from it."""

from __future__ import annotations

import json
import re
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"
MAX_APP_NAME = 32
PLACEHOLDER = "your name"


def slugify(display_name: str) -> str:
    """Turn a display name into a valid Container App name.

    Container App names are lowercase, alphanumeric with hyphens, must start with a letter,
    must end alphanumerically, and are capped at 32 characters.
    """
    slug = re.sub(r"[^a-z0-9]+", "-", display_name.strip().lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)[:MAX_APP_NAME].rstrip("-")
    if not slug:
        raise ValueError("displayName must contain at least one letter or digit")
    if not slug[0].isalpha():
        slug = f"a-{slug}"[:MAX_APP_NAME].rstrip("-")
    return slug


def load(path: Path | None = None) -> dict[str, str]:
    """Load config.json and return the display name with its derived app name."""
    config_path = path or CONFIG_PATH
    data = json.loads(config_path.read_text(encoding="utf-8"))
    display_name = str(data.get("displayName", "")).strip()
    if not display_name:
        raise ValueError("config.json is missing displayName")
    if display_name.lower() == PLACEHOLDER:
        raise ValueError("Edit config.json and replace 'Your Name' with your own name")
    return {"displayName": display_name, "appName": slugify(display_name)}


if __name__ == "__main__":
    settings = load()
    print(f"displayName={settings['displayName']}")
    print(f"appName={settings['appName']}")
