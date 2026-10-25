"""Serve and fingerprint the learner's static website without exposing the repository."""

import argparse
import hashlib
import html
import json
import os
import re
from collections.abc import Mapping
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException

from app.config import load

SITE_DIRECTORY = Path(__file__).resolve().parents[1] / "site"
ALLOWED_EXTENSIONS = {
    ".html", ".css", ".js", ".json", ".png", ".jpg", ".jpeg", ".gif", ".webp",
    ".svg", ".ico", ".woff", ".woff2", ".ttf",
}
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_SITE_BYTES = 20 * 1024 * 1024
MAX_FILES = 100
# The kit folders every page shares, from the first page and from site/ideas/<name>/.
SHARED_KIT_FOLDERS = {"css", "js", "art", "fonts"}
# Build details the publisher writes on each release. They are served but kept out of the content
# fingerprint, so rolling back to a known-good page shows the known-good fingerprint again.
VERSION_FILE = "version.json"
# Day 5: the publisher runs the same files in two slots. The production slot is the website's own
# address; the feature slot is a test copy of a pull request, marked by a strip at the top.
FEATURE_SLOT = "feature"
BODY_TAG = re.compile(rb"<body\b[^>]*>", re.IGNORECASE)


def website_slot(environment: Mapping[str, str] = os.environ) -> str:
    """Return "feature" for a pull request's test copy, otherwise "production"."""
    return FEATURE_SLOT if environment.get("WEBSITE_SLOT") == FEATURE_SLOT else "production"


def slot_banner(environment: Mapping[str, str] = os.environ) -> str:
    """The strip a feature slot shows above every page; the production slot shows none."""
    if website_slot(environment) != FEATURE_SLOT:
        return ""
    parts = ["Feature slot"]
    for label, name in (("Pull request #", "WEBSITE_PULL_REQUEST"), ("Version ", "WEBSITE_VERSION"),
                        ("Build ", "WEBSITE_BUILD")):
        if environment.get(name):
            parts.append(label + environment[name])
    parts.append("Test copy, not your live website")
    text = " &middot; ".join(html.escape(part) for part in parts)
    return ('<div data-workshop-slot="feature" role="note" style="margin:0;padding:8px 12px;'
            'background:#ffd84d;color:#1b1b1b;font:600 15px/1.4 system-ui,sans-serif;'
            f'text-align:center;border-bottom:2px solid #1b1b1b">{text}</div>')


def site_manifest(directory: Path = SITE_DIRECTORY) -> dict:
    """Validate a bounded asset folder and compute a deterministic content fingerprint."""
    root = directory.resolve()
    if not (root / "index.html").is_file():
        raise ValueError("Create site/index.html before previewing or deploying the website")
    files: dict[str, str] = {}
    total = 0
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError("Website assets must not contain symlinks or paths outside site/")
        if any(part.startswith(".") for part in relative.parts):
            raise ValueError("Hidden files and folders must not be placed in site/")
        if path.is_dir():
            continue
        if path.suffix.lower() == ".md":
            continue
        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            raise ValueError("Only HTML, CSS, JS, JSON, images, and fonts belong in site/")
        size = path.stat().st_size
        if not 0 < size <= MAX_FILE_BYTES:
            raise ValueError("Every published asset must be nonempty and at most 2 MiB")
        total += size
        if total > MAX_SITE_BYTES or len(files) >= MAX_FILES:
            raise ValueError("The workshop site is limited to 100 files and 20 MiB total")
        if relative.as_posix() == VERSION_FILE:
            continue
        files[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    index = (root / "index.html").read_text(encoding="utf-8")
    if "<html" not in index.lower() or "<body" not in index.lower():
        raise ValueError("site/index.html must be a complete UTF-8 HTML document")
    digest = hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()
    return {"digest": digest, "index_sha256": files["index.html"], "files": files}


class WebsiteFiles(StaticFiles):
    """Serve intended web assets only, without directory listings or Markdown notes."""

    def __init__(self, *args, banner: str = "", **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.banner = banner.encode("utf-8")

    def file_response(self, full_path, stat_result, scope, status_code: int = 200) -> Response:
        """Put the feature slot's strip at the top of each page; serve everything else unchanged."""
        if not self.banner or not str(full_path).lower().endswith(".html"):
            return super().file_response(full_path, stat_result, scope, status_code)
        page = Path(full_path).read_bytes()
        opening = BODY_TAG.search(page)
        if opening:
            page = page[:opening.end()] + self.banner + page[opening.end():]
        # Never cached, so a new build's strip shows at once.
        return Response(page, status_code=status_code, media_type="text/html; charset=utf-8",
                        headers={"Cache-Control": "no-store"})

    async def get_response(self, path: str, scope: dict):
        """Keep hidden files, research documents, and planning notes off the preview URL."""
        relative = Path(path)
        if any(part.startswith(".") and part != "." for part in relative.parts):
            raise HTTPException(status_code=404)
        if path not in (".", "") and relative.suffix.lower() not in ALLOWED_EXTENSIONS:
            # Only a folder with its own page, such as an idea in site/ideas/, opens by its address.
            if not (Path(self.directory) / relative / "index.html").is_file():
                raise HTTPException(status_code=404)
            if not scope["path"].endswith("/"):
                # A relative address keeps https behind the hosting proxy, and the page's own
                # links (css, data) need the trailing slash to resolve.
                return RedirectResponse(f"{relative.name}/", status_code=307)
        try:
            return await super().get_response(path, scope)
        except HTTPException as missing:
            # A second website in site/ideas/<name>/ shares the kit in site/css, js, art and fonts.
            # A shared file it asks for next to itself (a missed ../../) comes from the kit instead.
            # Its own data/ folder is never redirected.
            parts = relative.parts
            if missing.status_code != 404 or len(parts) < 4 or parts[0] != "ideas" \
                    or parts[2] not in SHARED_KIT_FOLDERS:
                raise
            return await super().get_response(str(Path(*parts[2:])), scope)


def create_app(directory: Path = SITE_DIRECTORY, config_path: Path | None = None) -> FastAPI:
    """Use the same static serving and health contract in Codespaces and Container Apps."""
    application = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
    slot = website_slot()

    @application.get("/healthz")
    def health() -> JSONResponse:
        """Identify the actual target, slot, commit, label, and deployed asset content."""
        try:
            settings = load(config_path)
            manifest = site_manifest(directory)
        except (OSError, ValueError):
            return JSONResponse({"status": "not-ready", "target": "website"}, status_code=503)
        return JSONResponse({
            "status": "ok", "target": "website", "label": settings["displayName"],
            "commit": os.environ.get("WORKSHOP_COMMIT", "unknown"), "slot": slot,
            "site_digest": manifest["digest"], "index_sha256": manifest["index_sha256"],
        })

    application.mount("/", WebsiteFiles(directory=directory, html=True, check_dir=False, banner=slot_banner()))
    return application


app = create_app()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", required=True)
    try:
        parser.parse_args()
        print(json.dumps(site_manifest(), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Website needs attention: {error}\n")