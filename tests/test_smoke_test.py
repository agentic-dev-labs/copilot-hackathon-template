"""The Day 5 smoke test reads a published website and reports every check honestly."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import smoke_test  # noqa: E402

SITE = "https://planner.example.test"
PAGE = (b'<!doctype html><html><head><link rel="stylesheet" href="css/workshop.css">'
        b'<script src="https://cdn.example.invalid/x.js"></script></head><body><h1>Plan our week</h1>'
        b'<img src="art/hero.svg"><a href="ideas/lunch/">Lunch</a></body></html>')


def fake_site(pages: dict[str, tuple[int, bytes]]):
    """Return a fetch replacement that serves fixed responses and records requests."""
    requested = []

    def fetch(url: str) -> tuple[int, bytes]:
        requested.append(url)
        return pages.get(url, (404, b""))

    fetch.requested = requested
    return fetch


def healthy_pages() -> dict[str, tuple[int, bytes]]:
    """A website whose page and two local files all load."""
    health = json.dumps({"status": "ok", "commit": "a" * 40, "site_digest": "b" * 64}).encode()
    return {
        f"{SITE}/healthz": (200, health),
        f"{SITE}/": (200, PAGE),
        f"{SITE}/css/workshop.css": (200, b"body{}"),
        f"{SITE}/art/hero.svg": (200, b"<svg/>"),
    }


def test_healthy_site_passes_and_skips_other_websites(monkeypatch: pytest.MonkeyPatch, capsys) -> None:
    """Remote scripts and links to other pages are not fetched; local files are."""
    fetch = fake_site(healthy_pages())
    monkeypatch.setattr(smoke_test, "fetch", fetch)
    assert smoke_test.main([SITE, "--expect-text", "Plan our week"]) == 0
    output = capsys.readouterr().out
    assert "PASS  Website says it is healthy  (commit aaaaaaa, content bbbbbbbbbbbb)" in output
    assert "5 passed, 0 failed." in output
    assert not any("cdn.example.invalid" in url or "ideas/lunch" in url for url in fetch.requested)


def test_missing_words_and_files_fail(monkeypatch: pytest.MonkeyPatch, capsys) -> None:
    """A broken release is reported as failed with a nonzero exit code."""
    pages = healthy_pages()
    del pages[f"{SITE}/art/hero.svg"]
    monkeypatch.setattr(smoke_test, "fetch", fake_site(pages))
    assert smoke_test.main([SITE, "--expect-text", "Something else"]) == 1
    output = capsys.readouterr().out
    assert 'FAIL  Page shows "Something else"' in output and "FAIL  Loads /art/hero.svg" in output


def test_unhealthy_or_plain_http_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    """Only https addresses are tested, and a down website fails the first check."""
    with pytest.raises(SystemExit):
        smoke_test.main(["http://planner.example.test"])
    monkeypatch.setattr(smoke_test, "fetch", fake_site({}))
    rows = smoke_test.smoke_test(SITE)
    assert rows[0][:2] == ("Website says it is healthy", False)
    assert rows[1][1] is False and len(rows) == 2
