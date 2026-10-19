"""Exercise the learner website independently of the preserved vendor app."""

import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.config import deployment_name, slugify
from app.site import create_app, site_manifest

HTML = '<!doctype html><html lang="en"><body><h1>Synthetic planner</h1></body></html>'
KIT = Path(".github/skills/create-website/assets/js/workshop.js")
PROJECT_BLUEPRINT = Path(".github/skills/create-website/assets/blueprints/project")


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


def test_own_idea_pages_serve_at_their_full_index_path(website: Path) -> None:
    """A browser opens an own-idea page by its full index.html path, not its folder."""
    idea = website / "ideas" / "team-lunch"
    idea.mkdir(parents=True)
    (idea / "index.html").write_text(HTML, encoding="utf-8")
    client = TestClient(create_app(website))
    assert client.get("/ideas/team-lunch/index.html").status_code == 200
    # Directory URLs are not served, so anyone opening an idea page must give the full path.
    assert client.get("/ideas/team-lunch/").status_code == 404


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


def board_columns(page: Path) -> list[str]:
    """Read the column names a board page renders from, as written in its inline SAMPLE."""
    inline = re.search(r"columns: \[(.+?)\]", page.read_text(encoding="utf-8"))
    assert inline is not None, "the board page must declare SAMPLE.columns"
    return [name.strip().strip("'") for name in inline.group(1).split(",")]


def test_chat_bubble_is_optional_safe_and_holds_no_secret() -> None:
    """The chat kit file talks only to the preview; it never calls a service or renders HTML."""
    chat = (KIT.parent / "workshop-chat.js").read_text(encoding="utf-8")
    assert "innerHTML" not in chat and "eval(" not in chat and not re.search(r"https?://", chat)
    assert "fetch(" not in chat and "XMLHttpRequest" not in chat
    assert "acquireVsCodeApi()" in chat and chat.count("acquireVsCodeApi()") == 1
    assert "'workshop.ask'" in chat and "'workshop.answer'" in chat
    assert "switched off" in chat
    assert "box.checked ? 'Ticked' : 'Not ticked'" in chat, "the assistant can tell which boxes are ticked"
    assert "Picture: ${picture.alt.trim()}" in chat, "the assistant can tell what pictures show"
    assert "window.Workshop = Object.assign(window.Workshop || {}, { addChat })" in chat
    for category in ("project", "calendar", "ideas", "weather"):
        page = (PROJECT_BLUEPRINT.parent / category / "index.html").read_text(encoding="utf-8")
        assert "workshop-chat.js" not in page, "chat is added on request, not shipped in every starter"


def test_board_columns_come_from_the_page_not_older_browser_storage() -> None:
    """A requested column change must reach a learner who already has saved cards."""
    kit = KIT.read_text(encoding="utf-8")
    assert "function useColumns(" in kit
    assert "useColumns" in kit.split("window.Workshop = ")[1]
    page = (PROJECT_BLUEPRINT / "index.html").read_text(encoding="utf-8")
    assert "useColumns(valid(loaded) ? loaded : SAMPLE, SAMPLE.columns)" in page
    columns = board_columns(PROJECT_BLUEPRINT / "index.html")
    data = json.loads((PROJECT_BLUEPRINT / "data/tasks.json").read_text(encoding="utf-8"))
    assert columns == data["columns"]
    assert {item["column"] for item in data["items"]} <= set(columns)


@pytest.mark.parametrize("category", ["project", "calendar", "ideas", "weather"])
def test_examples_reload_themselves_without_a_reset_button(category: str) -> None:
    """Beginners get their examples back by emptying the page, not by finding a button."""
    blueprints = PROJECT_BLUEPRINT.parent
    page = (blueprints / category / "index.html").read_text(encoding="utf-8")
    assert "Start again with the examples" not in page
    assert 'id="reset"' not in page
    assert "saved.clear()" not in page
    # An emptied page counts as nothing saved, so start() falls back to the examples.
    assert re.search(r"const valid = data =>.*?\.length > 0", page, re.DOTALL) is not None


@pytest.mark.skipif(shutil.which("node") is None, reason="Node runs the browser helper kit")
def test_use_columns_keeps_saved_cards_while_following_a_renamed_board() -> None:
    """Renaming columns must not discard the learner's own entries or strand them."""
    stale = {
        "columns": ["Monday", "Friday"],
        "items": [
            {"id": "t1", "text": "Synthetic sample task", "column": "Monday", "done": True},
            {"id": "own", "text": "Synthetic learner task", "column": "Friday", "done": False},
        ],
    }
    renamed = ["To Do", "In Progress", "Done"]
    harness = f"""
        global.window = {{}}
        eval(require('node:fs').readFileSync({str(KIT)!r}, 'utf8'))
        const {{ useColumns }} = window.Workshop
        const once = useColumns({json.dumps(stale)}, {json.dumps(renamed)})
        console.log(JSON.stringify({{
            once,
            unchanged: useColumns(once, {json.dumps(renamed)}),
            noColumns: useColumns({json.dumps(stale)}, []),
        }}))
    """
    result = subprocess.run(
        ["node", "-e", harness], capture_output=True, text=True, check=True, timeout=60
    )
    once = json.loads(result.stdout)["once"]
    repeated = json.loads(result.stdout)["unchanged"]
    assert once["columns"] == renamed
    assert [item["id"] for item in once["items"]] == ["t1", "own"]
    assert [item["column"] for item in once["items"]] == ["To Do", "To Do"]
    assert once["items"][0]["done"] is True
    assert repeated == once
    assert json.loads(result.stdout)["noColumns"] == stale


def run_node(script: str) -> str:
    """Run a short script in Node and return its standard output."""
    result = subprocess.run(["node", "-e", script], capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
    return result.stdout


def inline_block(page: str, start: str) -> str:
    """Return a top-level block of a blueprint's inline script, from its first line to its closing brace."""
    match = re.search(re.escape(start) + r".*?\n        \}\n", page, re.DOTALL)
    assert match is not None, start
    return match.group(0)


@pytest.mark.parametrize("category", ["project", "calendar", "ideas", "weather"])
def test_inline_sample_matches_the_data_file(category: str) -> None:
    """The skill keeps the inline SAMPLE and data/*.json identical, so an offline page looks the same."""
    blueprint = PROJECT_BLUEPRINT.parent / category
    starters = json.loads((blueprint.parent.parent / "starters.json").read_text(encoding="utf-8"))
    starter = next(item for item in starters["starters"] if item["id"] == category)
    page = (blueprint / "index.html").read_text(encoding="utf-8")
    literal = inline_block(page, "const SAMPLE = ").removeprefix("const SAMPLE = ")
    inline = json.loads(run_node(f"console.log(JSON.stringify({literal}))"))
    assert inline == json.loads((blueprint / starter["data_file"]).read_text(encoding="utf-8"))


def test_weather_starter_uses_us_units_and_local_cities() -> None:
    """The US audience sees Fahrenheit and mph, starting with Princeton."""
    blueprint = PROJECT_BLUEPRINT.parent / "weather"
    data = json.loads((blueprint / "data/weather.json").read_text(encoding="utf-8"))
    assert [city["name"] for city in data["cities"]] == ["Princeton", "New York", "Copenhagen"]
    page = (blueprint / "index.html").read_text(encoding="utf-8")
    assert "temperature_unit: 'fahrenheit', wind_speed_unit: 'mph'" in page
    assert "\\u00b0F`" in page and " mph`" in page
    assert "\\u00b0C" not in page and "km/h" not in page


def test_calendar_weeks_start_on_sunday_and_workdays_are_monday_to_friday() -> None:
    """Run the calendar's own date code: Month and Week start on Sunday, Workdays skip the weekend."""
    page = (PROJECT_BLUEPRINT.parent / "calendar" / "index.html").read_text(encoding="utf-8")
    helpers = "\n".join(
        re.search(rf"^\s*const {name} = .*$", page, re.MULTILINE).group(0)
        for name in ("addDays", "startOfWeek")
    )
    script = helpers + "\nlet state = { view: 'month' }\nlet cursor = new Date(2026, 9, 28)\n"
    script += inline_block(page, "function visibleDays() {")
    script += (
        "const out = {}\n"
        "for (const view of ['month', 'week', 'workdays']) {"
        " state.view = view; out[view] = visibleDays().map(day => day.getDay()) }\n"
        "console.log(JSON.stringify(out))"
    )
    days = json.loads(run_node(script))
    assert days["month"][0] == 0 and days["month"][-1] == 6 and len(days["month"]) % 7 == 0
    assert days["week"] == [0, 1, 2, 3, 4, 5, 6]
    assert days["workdays"] == [1, 2, 3, 4, 5]


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
