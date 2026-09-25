"""Exercise the learner website independently of the preserved vendor app."""

import hashlib
import json
import shutil
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.config import deployment_name, slugify
from app.site import create_app, site_manifest

HTML = '<!doctype html><html lang="en"><body><h1>Synthetic planner</h1></body></html>'


@pytest.fixture
def website(tmp_path: Path) -> Path:
    """Create a tiny synthetic site, not a prebuilt learner solution in the repository."""
    directory = tmp_path / "site"
    directory.mkdir()
    (directory / "index.html").write_text(HTML, encoding="utf-8")
    return directory


def test_website_serves_assets_and_identifies_revision(website: Path, monkeypatch) -> None:
    """Health and asset content must describe the actual requested website revision."""
    config = website.parent / "config.json"
    config.write_text(json.dumps({"displayName": "Synthetic Web Team"}), encoding="utf-8")
    (website / "main.js").write_text('document.title = "Synthetic";', encoding="utf-8")
    (website / "brief.md").write_text("Draft notes", encoding="utf-8")
    monkeypatch.setenv("WORKSHOP_COMMIT", "b" * 40)
    client = TestClient(create_app(website, config))
    assert client.get("/").text == HTML
    assert client.get("/main.js").status_code == 200
    assert client.get("/brief.md").status_code == 404
    assert client.get("/../config.json").status_code == 404
    result = client.get("/healthz").json()
    assert result["target"] == "website"
    assert result["label"] == "Synthetic Web Team"
    assert result["commit"] == "b" * 40
    assert result["index_sha256"] == hashlib.sha256(HTML.encode()).hexdigest()
    assert result["site_digest"] == site_manifest(website)["digest"]


@pytest.mark.parametrize(
    "filename", ["report.pdf", ".env", "server.py", "files.zip", ".private/data.json"]
)
def test_site_rejects_unintended_publication(website: Path, filename: str) -> None:
    """A website build must fail before copying reports, hidden files, or source code."""
    path = website / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("Synthetic content", encoding="utf-8")
    with pytest.raises(ValueError):
        site_manifest(website)


def test_site_digest_changes_with_assets_not_planning_notes(website: Path) -> None:
    """The fingerprint covers shipped bytes but excludes the unserved Markdown brief."""
    initial = site_manifest(website)
    (website / "brief.md").write_text("Synthetic planning", encoding="utf-8")
    assert site_manifest(website) == initial
    (website / "main.css").write_text("body { color: black; }", encoding="utf-8")
    assert site_manifest(website)["digest"] != initial["digest"]


def test_guided_kit_assets_fit_the_website_target(website: Path) -> None:
    """A copied blueprint and kit publish as-is, without skill files or license notes."""
    source = Path(".github/skills/create-website/assets")
    copies = {
        "blueprints/project/index.html": "index.html",
        "blueprints/project/data/tasks.json": "data/tasks.json",
        "css/workshop.css": "css/workshop.css",
        "js/workshop.js": "js/workshop.js",
        "art/hero-project.svg": "art/hero-project.svg",
        "art/monday.svg": "art/monday.svg",
        "fonts/source-sans-3-latin.woff2": "fonts/source-sans-3-latin.woff2",
        "fonts/OFL.txt": "FONT-LICENSE.md",
    }
    for original, relative in copies.items():
        destination = website / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / original, destination)
    manifest = site_manifest(website)
    assert set(manifest["files"]) == set(copies.values()) - {"FONT-LICENSE.md"}
    client = TestClient(create_app(website))
    for relative in manifest["files"]:
        response = client.get("/" + relative)
        assert response.status_code == 200
        assert hashlib.sha256(response.content).hexdigest() == manifest["files"][relative]
    assert client.get("/FONT-LICENSE.md").status_code == 404


def test_missing_site_and_invalid_markup_are_not_ready(tmp_path: Path, website: Path) -> None:
    """A blank template must not pass a website deployment check."""
    with pytest.raises(ValueError, match="index.html"):
        site_manifest(tmp_path)
    (website / "index.html").write_text("not a website", encoding="utf-8")
    with pytest.raises(ValueError, match="HTML"):
        site_manifest(website)
    assert TestClient(create_app(website)).get("/healthz").status_code == 503


def test_oversized_asset_is_rejected(website: Path, monkeypatch) -> None:
    """Bound asset reads and deployment validation responses."""
    monkeypatch.setattr("app.site.MAX_FILE_BYTES", 10)
    with pytest.raises(ValueError, match="2 MiB"):
        site_manifest(website)


@pytest.mark.parametrize("label", ["Synthetic Team", "7 Synthetic", "Synthetic " * 10])
def test_target_names_are_distinct_and_vendor_names_stay_stable(label: str) -> None:
    """Monday must not overwrite Tuesday's app or silently rename an existing vendor app."""
    vendor = deployment_name(label, "vendor")
    website = deployment_name(label, "website")
    assert vendor == slugify(label)
    assert website != vendor and len(website) <= 32
    assert website.endswith("-web")
    assert website == deployment_name(label, "website")
    with pytest.raises(ValueError):
        deployment_name(label, "unknown")
