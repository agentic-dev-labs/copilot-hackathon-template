"""Serve and fingerprint the learner's static website without exposing the repository."""

import argparse
import hashlib
import json
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse
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
        files[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    index = (root / "index.html").read_text(encoding="utf-8")
    if "<html" not in index.lower() or "<body" not in index.lower():
        raise ValueError("site/index.html must be a complete UTF-8 HTML document")
    digest = hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()
    return {"digest": digest, "index_sha256": files["index.html"], "files": files}


class WebsiteFiles(StaticFiles):
    """Serve intended web assets only, without directory listings or Markdown notes."""

    async def get_response(self, path: str, scope: dict):
        """Keep hidden files, research documents, and planning notes off the preview URL."""
        relative = Path(path)
        if any(part.startswith(".") and part != "." for part in relative.parts):
            raise HTTPException(status_code=404)
        if path not in (".", "") and relative.suffix.lower() not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=404)
        return await super().get_response(path, scope)


def create_app(directory: Path = SITE_DIRECTORY, config_path: Path | None = None) -> FastAPI:
    """Use the same static serving and health contract in Codespaces and Container Apps."""
    application = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    @application.get("/healthz")
    def health() -> JSONResponse:
        """Identify the actual target, commit, label, and deployed asset content."""
        try:
            settings = load(config_path)
            manifest = site_manifest(directory)
        except (OSError, ValueError):
            return JSONResponse({"status": "not-ready", "target": "website"}, status_code=503)
        return JSONResponse({
            "status": "ok", "target": "website", "label": settings["displayName"],
            "commit": os.environ.get("WORKSHOP_COMMIT", "unknown"),
            "site_digest": manifest["digest"], "index_sha256": manifest["index_sha256"],
        })

    application.mount("/", WebsiteFiles(directory=directory, html=True, check_dir=False))
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