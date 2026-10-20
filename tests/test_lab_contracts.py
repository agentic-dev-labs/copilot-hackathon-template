"""Keep executable examples and timetable claims aligned with the labs."""

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


SIGNPOST_LABS = {"00-setup", "05-dataverse-app", "07-automations-hooks"}


def active_lab_guides() -> list[Path]:
    """Exclude the Lab 00, Lab 05 and Lab 07 signposts from attendee exercise requirements."""
    return [path for path in Path("labs").glob("*/README.md") if path.parent.name not in SIGNPOST_LABS]


def test_lab_timeboxes_match_the_agenda() -> None:
    """Optional exercises must not silently extend the published core blocks."""
    agenda = Path("docs/AGENDA.md").read_text(encoding="utf-8")
    rows = re.findall(r"\| (\d\d):(\d\d)-(\d\d):(\d\d) \| Lab (\d\d):", agenda)
    assert {row[-1] for row in rows} == {"01", "02", "08", "03"}
    assert len(rows) == 4
    for start_hour, start_minute, end_hour, end_minute, number in rows:
        minutes = (int(end_hour) - int(start_hour)) * 60 + int(end_minute) - int(start_minute)
        lab = next(Path("labs").glob(f"{number}-*/README.md"))
        assert f"**Time-box:** {minutes} minutes" in lab.read_text(encoding="utf-8")
    # Monday morning's lab lives in the README, which attendees see first on GitHub.
    assert "| 09:30-10:00 | Lab, from the README:" in agenda_day(1)


def test_first_lab_requires_chat_not_terminal_setup() -> None:
    """The beginner entry path must not silently reintroduce diagnostic commands."""
    readme = Path("README.md").read_text(encoding="utf-8")
    morning = readme.split("## Monday Morning: Follow Along", 1)[1].split("\n## ", 1)[0]
    assert "```" not in morning
    assert "copilot --version" not in morning
    assert "gh auth status" not in morning
    for heading in ("### This Is GitHub", "### Find Your Files and Copilot Chat",
                    "### Your First Note", "### Next: Your First Website"):
        assert heading in morning
    flat = " ".join(morning.split())
    assert "Concepts only: no commands." in flat
    assert "Use this template > Create a new repository" in flat
    assert "choose **agentic-dev-labs**" in flat and "choose **Private**" in flat
    assert "Make only one." in flat
    assert "save -> review -> commit -> push" in flat
    assert "presenter shows `/create-website`" in flat
    signpost = Path("labs/00-setup/README.md").read_text(encoding="utf-8")
    assert "README.md#monday-morning-follow-along" in signpost
    assert "**Time-box:**" not in signpost and "```" not in signpost
    guide = Path("docs/START-HERE.md").read_text(encoding="utf-8")
    assert "README.md#monday-morning-follow-along" in guide
    assert "## Your First Note" not in guide, "the note steps live only in the README"
    assert "save -> review -> commit -> push" in guide
    assert "official documentation screenshots" in guide
    assert "Expect -> try -> compare -> improve -> repeat" in guide


def test_monday_build_checks_are_manual_and_extensions_are_optional() -> None:
    """Tool configuration, persistence and publication must not gate a first website."""
    first_page = Path("labs/01-first-website/README.md").read_text(encoding="utf-8")
    interaction = Path("labs/02-make-it-useful/README.md").read_text(encoding="utf-8")
    sharing = Path("labs/08-save-and-share/README.md").read_text(encoding="utf-8")
    assert "python3 scripts/website_preview.py status" in first_page
    assert "appear by itself" in first_page
    assert "MCP: Add Server" not in first_page
    assert "1 of 4 done" in first_page
    assert "localStorage" not in interaction.split("## Optional extras")[0]
    assert "not a requirement" in interaction
    assert "A deployment or saved browser state is not required" in sharing
    assert "## Optional extras" in sharing


def test_personalisation_lab_follows_the_chosen_category() -> None:
    """Learners improve their own page, with visual and feature changes kept small."""
    text = Path("labs/02-make-it-useful/README.md").read_text(encoding="utf-8")
    for category in ("Project Planner", "Calendar", "Ideas Wall", "Weather", "Princeton Map", "Photo Studio"):
        assert f"| {category} |" in text
    assert "**one appearance change** and **one feature change**" in text
    assert "not a new creation interview" in text
    assert "If a feature already works" in text
    assert "Keep the design unchanged" in text
    assert "own-idea extension in a separate folder" in text
    blocks = re.findall(r"^### \d\. .*\((\d+) minutes\)", text, re.MULTILINE)
    assert sum(map(int, blocks)) == 60
    assert "2 of 4" in text and "3 notes planned" in text


def test_day_one_teaches_reading_code_undo_and_history() -> None:
    """First-timers peek at code, undo a change, and find their history, within the same times."""
    first_page = Path("labs/01-first-website/README.md").read_text(encoding="utf-8")
    blocks = re.findall(r"^## \d\. .*\((\d+) minutes\)", first_page, re.MULTILINE)
    assert sum(map(int, blocks)) == 60
    assert "## 3. Peek Inside the Code" in first_page
    assert "Explain the lines I selected" in first_page and "`<h1>`" in first_page
    # The example headline in the lab must be the Project Planner starter's real headline.
    example = re.search(r"for example \*(.+?)\*", first_page).group(1)
    planner = Path(".github/skills/create-website/assets/blueprints/project/index.html")
    assert f"<h1>{example}</h1>" in planner.read_text(encoding="utf-8")

    interaction = Path("labs/02-make-it-useful/README.md").read_text(encoding="utf-8")
    assert "select **Undo**" in interaction and "**Keep** and **Undo**" in interaction
    sketch = Path("docs/images/sketch-example.png")
    assert "](../../docs/images/sketch-example.png)" in interaction
    assert sketch.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n" and sketch.stat().st_size < 100 * 1024
    assert "never a picture with real work information" in interaction

    sharing = Path("labs/08-save-and-share/README.md").read_text(encoding="utf-8")
    blocks = re.findall(r"^### \d\. .*\((\d+) minutes\)", sharing, re.MULTILINE)
    assert sum(map(int, blocks)) == 45
    assert "**sparkle icon**" in sharing and "**Commits**" in sharing and "**History**" in sharing
    for level in ("**Bronze**", "**Silver**", "**Gold**"):
        assert level in sharing
    quick_reference = Path("docs/QUICK-REFERENCE.md").read_text(encoding="utf-8")
    assert "Undo Copilot's change" in quick_reference and "Show Copilot a picture" in quick_reference


def test_daily_schedule_has_no_gaps_or_overlaps() -> None:
    """The published blocks must fill the stated days without adding hidden time."""
    agenda = Path("docs/AGENDA.md").read_text(encoding="utf-8")
    sections = re.split(r"## Day \d[^\n]*\n", agenda)[1:]
    assert len(sections) == 5
    for section, expected in zip(sections, [360, 360, 240, 240, 240], strict=True):
        blocks = re.findall(r"\| (\d\d):(\d\d)-(\d\d):(\d\d) \|", section)
        intervals = [
            (int(start_hour) * 60 + int(start_minute), int(end_hour) * 60 + int(end_minute))
            for start_hour, start_minute, end_hour, end_minute in blocks
        ]
        assert all(end > start for start, end in intervals)
        assert sum(end - start for start, end in intervals) == expected
        assert all(
            previous[1] == following[0] for previous, following in zip(intervals, intervals[1:])
        )


def test_private_run_sheet_matches_when_present() -> None:
    """Only active presenter notes claim to match the current timetable."""
    private_path = Path(".facilitator/RUN-OF-SHOW.md")
    if not private_path.exists():
        return
    private = private_path.read_text(encoding="utf-8")
    if "**Superseded delivery script" in private:
        assert "../docs/AGENDA.md" in private
        assert "../docs/FACILITATOR.md" in private
        return
    pattern = r"\| (\d\d:\d\d)[-\u2013](\d\d:\d\d) \|"
    public = re.findall(pattern, Path("docs/AGENDA.md").read_text(encoding="utf-8"))
    assert public == re.findall(pattern, private)


def test_customization_examples_parse() -> None:
    """Broken frontmatter can silently prevent a customization from loading."""
    for lab in Path("labs").glob("*/README.md"):
        text = lab.read_text(encoding="utf-8")
        for language, body in re.findall(
            r"```(json|yaml|markdown)\n(.*?)\n[ \t]*```", text, re.DOTALL
        ):
            body = "\n".join(
                line[3:] if line.startswith("   ") else line for line in body.splitlines()
            )
            if language == "json":
                json.loads(body)
            elif language == "yaml":
                yaml.safe_load(body)
            elif body.startswith("---\n"):
                metadata = yaml.safe_load(body.split("---", 2)[1])
                assert isinstance(metadata, dict)
                assert metadata.get("description")


def test_guided_website_skill_is_explicit_and_preserves_learner_work() -> None:
    """A provided workflow must wait for choices and never count invented checks as success."""
    path = Path(".github/skills/create-website/SKILL.md")
    text = path.read_text(encoding="utf-8")
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["name"] == path.parent.name
    assert metadata["user-invocable"] is True
    assert metadata["disable-model-invocation"] is True
    assert "Stop after the question and wait" in text
    assert "Choosing a category is the approval to build it" in text
    assert "not yet checked" in text
    assert "Never overwrite the first page" in text
    assert "No deployment or public port" in text
    assert "python3 scripts/website_preview.py start" in text
    assert "paid reference service" in text
    assert "No logo-generation API" in text
    assert 'git remote get-url origin' in text
    assert "Describe your idea in one sentence." in text
    assert "moves on to the next lab" in text
    assert "or build\n  your own idea in its own folder?" in text
    for name in ("project", "calendar", "ideas", "weather", "map", "photo"):
        assert f"./assets/blueprints/{name}/index.html" in text
    assert "Workshop.store" in text and "Workshop.loadJSON" in text
    assert "Workshop.enableBoard" in text and "Workshop.addButton" in text
    assert "./assets/art/" in text
    assert "Vue" not in text and "Vite" not in text
    assert "100 KiB" in text
    assert "../start-website/SKILL.md" in text
    assert "../stop-website/SKILL.md" in text
    assert "category-specific ideas" in text


def test_preview_lifecycle_skills_reuse_the_helper_and_preserve_files() -> None:
    """Recovery must not recreate pages, bypass editor tool restrictions, or kill by port."""
    texts = {}
    for name in ("start-website", "stop-website"):
        path = Path(".github/skills") / name / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        metadata = yaml.safe_load(text.split("---", 2)[1])
        assert metadata["name"] == name
        assert metadata["description"]
        assert metadata["user-invocable"] is True
        assert metadata["disable-model-invocation"] is True
        texts[name] = text
    start = texts["start-website"]
    assert "python3 scripts/website_preview.py start" in start
    assert "relative to site/" in start
    assert "Do not create a placeholder" in start
    assert "Can you see your page beside Chat?" in " ".join(start.split())
    assert "no server, no port, no sign-in" in start
    stop = texts["stop-website"]
    assert "python3 scripts/website_preview.py stop" in stop
    assert "Do not edit, delete, reset" in stop
    assert "Do not use `pkill`, `killall`" in stop
    assert "previewOpen: false" in stop


def test_facilitator_reset_skill_harvests_before_clearing() -> None:
    """A reset tool must keep the evidence, the owner's work, and its own safety rules."""
    path = Path(".github/skills/workshop-reset/SKILL.md")
    text = path.read_text(encoding="utf-8")
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["name"] == path.parent.name
    assert metadata["description"]
    assert metadata["user-invocable"] is True
    # Clearing the run's output must never be something a model decides to do by itself.
    assert metadata["disable-model-invocation"] is True
    body = " ".join(text.split())
    assert "harvest what the run proved, then clear what it generated" in body
    assert "Never start at section 5." in body
    # The destructive commands cannot tell leftovers from the facilitator's own work.
    for command in ("git reset --hard", "git checkout .", "git clean -fdx"):
        assert command in text
    assert "Delete named paths only." in text
    assert "python3 scripts/website_preview.py stop" in text
    assert "site/README.md" in text
    # The preview socket is prepared machinery; clearing it breaks the next run.
    assert "`.workshop-preview/`: the preview extension and its live `site.sock`" in text
    assert "never that this run created it" in text
    assert "16 KiB" in text
    assert "synthetic" in text
    assert "Never invent one" in text
    assert "not a learning" in text
    assert "did not exercise" in body
    assert "uv run pytest" in text and "uv run ruff check ." in text
    assert "never commit, push, or deploy" in body


def test_hand_over_offers_ideas_for_every_category() -> None:
    """A beginner who does not know what to ask for must be shown concrete options."""
    assets = Path(".github/skills/create-website/assets")
    data = json.loads((assets / "starters.json").read_text(encoding="utf-8"))
    shared = data["any_page_ideas"]
    assert len(shared) >= 4
    assert any("color theme" in idea for idea in shared)
    assert any("tabs" in idea for idea in shared)
    seen: set[str] = set()
    for starter in data["starters"]:
        ideas = starter["later_ideas"]
        assert all(idea.strip() and idea[0].isupper() for idea in ideas)
        assert len(set(ideas)) == len(ideas)
        # Each category needs its own wording, not one list repeated four times.
        assert not seen & set(ideas)
        seen |= set(ideas)
        assert not set(ideas) & set(shared)
    skill = Path(".github/skills/create-website/SKILL.md").read_text(encoding="utf-8")
    assert "any_page_ideas" in skill and "later_ideas" in skill
    assert "Suggest, never build" in skill


def test_guided_starter_figures_and_shared_assets() -> None:
    """Every starter has a tested blueprint, matching sample data, a checkable count, and local art."""
    assets = Path(".github/skills/create-website/assets")
    data = json.loads((assets / "starters.json").read_text(encoding="utf-8"))
    assert data["source_mode"] == "synthetic_workshop"
    assert [starter["id"] for starter in data["starters"]] == ["project", "calendar", "ideas", "weather", "map", "photo"]
    assert data["default"] == "project"
    allowed_urls = {"http://www.w3.org/2000/svg", "https://api.open-meteo.com/v1/forecast",
                    "https://geocoding-api.open-meteo.com/v1/search",
                    "https://archive-api.open-meteo.com/v1/archive"}
    for starter in data["starters"]:
        assert starter["summary"] and starter["manual_check"]
        assert len(starter["later_ideas"]) >= 4
        blueprint = assets / "blueprints" / starter["id"]
        sample = json.loads((blueprint / starter["data_file"]).read_text(encoding="utf-8"))
        key = "cities" if starter["id"] == "weather" else "items"
        assert len(sample[key]) == starter["expected"]["item_count"]
        if "done_count" in starter["expected"]:
            assert sum(item["done"] for item in sample["items"]) == starter["expected"]["done_count"]
        page = (blueprint / "index.html").read_text(encoding="utf-8")
        assert f"store('{starter['storage_key']}')" in page
        assert f"'{starter['data_file']}'" in page
        assert '<script src="js/workshop.js"></script>' in page
        assert '<link rel="stylesheet" href="css/workshop.css">' in page
        assert "<title>My " in page and "logo-mark" in page
        assert "innerHTML" not in page
        # Places name the page that supports their description: a link to read, never a request.
        sources = {item["source"] for item in sample[key] if isinstance(item, dict) and item.get("source")}
        assert set(re.findall(r"https?://[^`'\"?$\s]+", page)) <= allowed_urls | sources
        for art in re.findall(r'src="(art/[^"]+)"', page):
            assert (assets / art).is_file(), art
    kit = (assets / "js/workshop.js").read_text(encoding="utf-8")
    assert "innerHTML" not in kit and "eval(" not in kit and not re.search(r"https?://", kit)
    for art in (assets / "art").glob("*.svg"):
        root = ET.parse(art).getroot()
        assert root.tag == "{http://www.w3.org/2000/svg}svg", art
        assert not any(element.tag.endswith("script") for element in root.iter()), art
        text = art.read_text(encoding="utf-8")
        assert "http" not in text.replace("http://www.w3.org/2000/svg", ""), art
        assert "prefers-reduced-motion: reduce" in text, art
    weekdays = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
    assert weekdays <= {art.stem for art in (assets / "art").glob("*.svg")}
    assert sum(art.stat().st_size for art in (assets / "art").glob("*.svg")) < 24 * 1024
    css = (assets / "css/workshop.css").read_text(encoding="utf-8")
    for resource in re.findall(r'url\("([^"]+)"\)', css):
        assert not urlsplit(resource).scheme
        assert (assets / "css" / resource).is_file()
    assert "prefers-reduced-motion" in css
    assert ":focus-visible" in css
    assert "color-scheme: light" in css
    # The Website preview's VS Code webview styles body with the editor's colors, font and padding.
    body_rule = re.search(r"^body \{([^}]*)\}", css, re.MULTILINE).group(1)
    for setting in ("color: var(--ink)", "padding: 0", "font: inherit", "background: var(--canvas)"):
        assert setting in body_rule
    assert len(css.encode("utf-8")) < 16 * 1024
    assert "@import" not in css
    assert "prefers-color-scheme: dark" not in css
    assert "letter-spacing: 0" in css
    assert "SIL OPEN FONT LICENSE" in (assets / "fonts/OFL.txt").read_text(encoding="utf-8")
    font = (assets / "fonts/source-sans-3-latin.woff2").read_bytes()
    assert font[:4] == b"wOF2"
    assert len(font) < 40 * 1024


def test_own_idea_patterns_are_tested_and_stay_out_of_the_first_question() -> None:
    """The Request Tracker and Team Dashboard back up common business ideas without lengthening Monday's menu."""
    assets = Path(".github/skills/create-website/assets")
    data = json.loads((assets / "starters.json").read_text(encoding="utf-8"))
    patterns = {pattern["id"]: pattern for pattern in data["idea_patterns"]}
    assert list(patterns) == ["tracker", "dashboard", "game"]
    starter_ideas = {idea for starter in data["starters"] for idea in starter["later_ideas"]}
    for pattern in patterns.values():
        assert pattern["summary"] and pattern["suits"] and pattern["try_it"].startswith("Try it:")
        assert pattern["manual_check"] and len(pattern["later_ideas"]) >= 4
        assert len(set(pattern["later_ideas"])) == len(pattern["later_ideas"])
        assert not set(pattern["later_ideas"]) & (starter_ideas | set(data["any_page_ideas"]))
        blueprint = assets / "blueprints" / pattern["id"]
        page = (blueprint / "index.html").read_text(encoding="utf-8")
        assert f"store('{pattern['storage_key']}')" in page and f"'{pattern['data_file']}'" in page
        assert '<script src="js/workshop.js"></script>' in page
        assert '<link rel="stylesheet" href="css/workshop.css">' in page
        assert "<title>My " in page and "logo-mark" in page and "innerHTML" not in page
        assert not re.search(r"https?://", page), "own-idea patterns stay offline"
        for art in re.findall(r'src="(art/[^"]+)"', page):
            assert (assets / art).is_file(), art

    tracker = json.loads((assets / "blueprints/tracker/data/requests.json").read_text(encoding="utf-8"))
    expected = patterns["tracker"]["expected"]
    last = tracker["columns"][-1]
    assert len(tracker["items"]) == expected["item_count"]
    assert sum(item["status"] == last for item in tracker["items"]) == expected["done_count"]
    late = [item for item in tracker["items"] if item["status"] != last and item["dueInDays"] < 0]
    assert len(late) == expected["overdue_count"]
    assert {item["status"] for item in tracker["items"]} <= set(tracker["columns"])
    assert {item["type"] for item in tracker["items"]} <= set(tracker["types"])

    metrics = json.loads((assets / "blueprints/dashboard/data/metrics.json").read_text(encoding="utf-8"))
    expected = patterns["dashboard"]["expected"]
    groups = metrics["groups"]
    assert len(metrics["items"]) == expected["item_count"]
    assert all(len(item["values"]) == len(groups) for item in metrics["items"])
    totals = {group: sum(item["values"][index] for item in metrics["items"]) for index, group in enumerate(groups)}
    assert sum(totals.values()) == expected["total"]
    assert max(totals, key=totals.get) == expected["top_group"] and totals["Northeast"] == expected["top_total"]
    assert "2,778" in patterns["dashboard"]["manual_check"] and f"{totals['South']}" in patterns["dashboard"]["manual_check"]
    dashboard = (assets / "blueprints/dashboard/index.html").read_text(encoding="utf-8")
    assert '<script src="js/vendor/echarts.min.js"></script>' in dashboard
    assert '<script src="js/workshop-charts.js"></script>' in dashboard and "chart('#trend-chart'" in dashboard

    skill = Path(".github/skills/create-website/SKILL.md").read_text(encoding="utf-8")
    first_question = skill.split("## 2. Build It Straight Away")[0]
    assert "Tracker" not in first_question and "Dashboard" not in first_question
    for name in ("tracker", "dashboard"):
        assert f"./assets/blueprints/{name}/index.html" in skill
    assert "idea_patterns" in skill and "question for IT" in skill


def test_lab_chase_game_is_playable_original_and_licensed() -> None:
    """The game pattern's maze works, its library is the approved unchanged three.js, and nothing is borrowed."""
    assets = Path(".github/skills/create-website/assets")
    data = json.loads((assets / "starters.json").read_text(encoding="utf-8"))
    pattern = next(item for item in data["idea_patterns"] if item["id"] == "game")
    game = json.loads((assets / "blueprints/game/data/game.json").read_text(encoding="utf-8"))
    maze = game["maze"]
    assert len({len(row) for row in maze}) == 1 and set("".join(maze)) <= set("#.oSMI")
    assert all(ch == "#" for ch in maze[0] + maze[-1]) and all(row[0] == row[-1] == "#" for row in maze)
    cells = {(c, r): ch for r, row in enumerate(maze) for c, ch in enumerate(row)}
    starts = [cell for cell, ch in cells.items() if ch == "S"]
    assert len(starts) == 1
    reachable, queue = {starts[0]}, [starts[0]]
    while queue:
        c, r = queue.pop()
        for step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            near = (c + step[0], r + step[1])
            if cells.get(near, "#") not in "#I" and near not in reachable:
                reachable.add(near)
                queue.append(near)
    walkable = {cell for cell, ch in cells.items() if ch not in "#I"}
    assert reachable == walkable, "every data point, coffee and molecule start can be reached"
    expected = pattern["expected"]
    assert sum(ch == "." for ch in cells.values()) == expected["dots"]
    assert sum(ch == "o" for ch in cells.values()) == expected["coffee"]
    assert sum(ch == "M" for ch in cells.values()) >= 2 and sum(ch == "I" for ch in cells.values()) == 3
    assert len(game["items"]) == expected["item_count"]
    assert f"{expected['dots']} data points" in pattern["manual_check"]
    assert all(game["lines"][key] for key in ("start", "molecule", "caught", "coffee", "declined", "level", "over"))

    page = (assets / "blueprints/game/index.html").read_text(encoding="utf-8")
    assert "import * as THREE from './js/vendor/three.module.js'" in page
    # The scientist runs only while a direction is held, and stops when it is let go.
    assert "if (steering()) advance(scientist, dt)" in page
    assert "window.addEventListener('keyup'" in page and "window.addEventListener('blur', releaseAll)" in page
    assert "'pointerup', 'pointercancel', 'lostpointercapture'" in page
    assert "let go to stop" in page and "let go" in pattern["manual_check"]
    assert "lives: 3" in page and "prefers-reduced-motion" in page
    assert "cannot draw 3D" in page, "a browser without 3D gets a plain message"
    text = (page + json.dumps(game)).lower()
    for borrowed in ("pac-man", "pacman", "pac man", "namco", "blinky", "inky", "clyde"):
        assert borrowed not in text, borrowed

    readme = (assets / "README.md").read_text(encoding="utf-8")
    for name in ("three.module.js", "three.core.js"):
        library = (assets / "game" / name).read_bytes()
        assert hashlib.sha256(library).hexdigest() in readme, name
        source = library.decode("utf-8")
        assert "eval(" not in source and "new Function" not in source, name
    assert "from './three.core.js'" in (assets / "game/three.module.js").read_text(encoding="utf-8")
    licence = (assets / "game/THREE-LICENSE.md").read_text(encoding="utf-8")
    assert "The MIT License" in licence and "three@0.186.1" in licence
    assert "assets/game/*.js -text -diff" in Path(".gitattributes").read_text(encoding="utf-8")
    skill = Path(".github/skills/create-website/SKILL.md").read_text(encoding="utf-8")
    assert "./assets/game/three.module.js" in skill and "site/THREE-LICENSE.md" in skill
    assert "never use a real game's name" in skill


def test_agent_frontmatter_and_handoff_targets() -> None:
    """Every checked-in agent should be discoverable and reference an existing role."""
    agents = {}
    for path in Path(".github/agents").glob("*.agent.md"):
        text = path.read_text(encoding="utf-8")
        assert text.startswith("---\n"), path
        metadata = yaml.safe_load(text.split("---", 2)[1])
        assert metadata["name"] == path.name.removesuffix(".agent.md")
        assert metadata.get("description")
        assert isinstance(metadata.get("tools"), list)
        agents[metadata["name"]] = metadata
    assert agents
    for metadata in agents.values():
        for handoff in metadata.get("handoffs", []):
            assert handoff["agent"] in agents
            assert handoff.get("label") and handoff.get("prompt")


def test_authoring_labs_do_not_embed_finished_customizations() -> None:
    """Give learners requirements rather than complete agent, skill, or hook files."""
    for number in ("01", "06"):
        path = next(Path("labs").glob(f"{number}-*/README.md"))
        text = path.read_text(encoding="utf-8")
        for body in re.findall(r"```markdown\n(.*?)\n[ \t]*```", text, re.DOTALL):
            parts = body.strip().split("---", 2)
            assert len(parts) != 3 or not parts[2].strip(), path
        for body in re.findall(r"```json\n(.*?)\n[ \t]*```", text, re.DOTALL):
            assert "hooks" not in json.loads(body), path


def test_labs_have_completion_checks_and_optional_work() -> None:
    """Attendees need an observable finish and a separate early-finisher path."""
    for path in active_lab_guides():
        text = path.read_text(encoding="utf-8")
        assert "**Done when:**" in text, path
        assert "## Optional extras" in text, path


def test_labs_link_official_references_and_coverage_guide() -> None:
    """Each lab needs usable lookup links alongside its required and optional tasks."""
    official_hosts = {"docs.github.com", "code.visualstudio.com", "learn.microsoft.com"}
    guide = Path("docs/REFERENCES.md").resolve()
    for path in active_lab_guides():
        text = path.read_text(encoding="utf-8")
        assert "## Official References\n" in text, path
        section = text.split("## Official References\n", 1)[1]
        links = [urlsplit(target) for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", section)]
        assert any(link.scheme == "https" and link.hostname in official_hosts for link in links), (
            path
        )
        assert any(
            not link.scheme and (path.parent / unquote(link.path)).resolve() == guide
            for link in links
        ), path


def heading_anchors(document: Path) -> set[str]:
    """Return the GitHub-style anchors generated by a Markdown file's headings."""
    anchors = set()
    for heading in re.findall(r"^#{1,6}\s+(.*)$", document.read_text(encoding="utf-8"), re.M):
        text = re.sub(r"[`*_]", "", heading).strip()
        anchors.add(re.sub(r"[^\w\s-]", "", text.lower()).strip().replace(" ", "-"))
    return anchors


def test_local_document_links_resolve() -> None:
    """Check the simple relative links used by the workshop documentation."""
    files = [Path("README.md"), Path("AGENTS.md")]
    for directory in (
        "docs",
        "labs",
        ".github",
        "src",
        ".facilitator",
        "rehearsal",
        "travel",
        "post-workshop",
    ):
        files.extend(
            path
            for path in Path(directory).rglob("*.md")
            if not {"results", "output"}.intersection(path.parts)
        )
    for path in files:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            link = urlsplit(target)
            if link.scheme or link.netloc or not link.path:
                continue
            document = path.parent / unquote(link.path)
            assert document.exists(), f"{path}: {target}"
            if link.fragment and document.suffix == ".md":
                assert link.fragment.lower() in heading_anchors(document), f"{path}: {target}"


def test_post_workshop_reference_preserves_the_technical_path() -> None:
    """Removing a beginner lab must not discard the maintained implementation or its safeguards."""
    guide = Path("post-workshop/dataverse/README.md").read_text(encoding="utf-8")
    prompts = Path("post-workshop/dataverse/PROMPTS.md").read_text(encoding="utf-8")
    assert "not an attendee lab or a production-ready" in guide
    assert "WORKSHOP_ALLOW_WRITES" in guide
    assert "not authentication" in guide
    assert "not tenant isolation or authorization" in guide
    assert "Do not create a second fork" in guide
    assert "Do not edit files, call live services" in prompts
    assert "Do not delete personal accounts" in prompts
    assert "/post-workshop/" in Path(".dockerignore").read_text(encoding="utf-8").splitlines()
    for path in (
        "app/main.py",
        "src/vendor_assurance/dataverse.py",
        "scripts/dataverse_provision.py",
        "scripts/dataverse_app_user.py",
        "scripts/dataverse_seed.py",
        ".github/workflows/deploy.yml",
    ):
        assert Path(path).is_file()


def test_tuesday_protects_own_idea_building() -> None:
    """The meeting refit removes required integration and tooling tasks from beginner Day 2."""
    agenda = Path("docs/AGENDA.md").read_text(encoding="utf-8")
    tuesday = agenda.split("## Day 2", 1)[1].split("## Day 3", 1)[0]
    assert "09:00-09:30 | David:" in tuesday
    assert "09:30-10:30 | Jackie:" in tuesday
    assert "Lab 05:" not in tuesday
    assert "Guided tools:" not in tuesday
    assert "DAY-2-BUILD.md" in tuesday
    guide = Path("docs/DAY-2-BUILD.md").read_text(encoding="utf-8")
    assert "No database, login, API keys" in guide
    assert guide.count("Run `/create-website`") == 1
    assert "not completion gates" in guide
    assert "helpers work with you at the tables" in guide
    assert "site/ideas/" in guide and "prepared repository" not in guide
    assert "The presenter" not in guide
    quick_reference = Path("docs/QUICK-REFERENCE.md").read_text(encoding="utf-8")
    assert "Open Preview" in quick_reference
    assert "Do not delete accounts" in quick_reference


def test_lab_guides_have_one_current_title() -> None:
    """Catch accidentally retained old introductions alongside replacement instructions."""
    for path in Path("labs").glob("*/README.md"):
        assert len(re.findall(r"^# ", path.read_text(encoding="utf-8"), re.MULTILINE)) == 1, path
    retired = Path("labs/05-dataverse-app/README.md").read_text(encoding="utf-8")
    assert "Status: retired" in retired
    assert "post-workshop/dataverse/README.md" in retired
    assert "docs/DAY-2-BUILD.md" in retired
    assert "**Time-box:**" not in retired
    assert "DATAVERSE_CLIENT_SECRET" not in retired
    automation = Path("labs/07-automations-hooks/README.md").read_text(encoding="utf-8")
    assert "Status: retired" in automation
    assert "post-workshop/advanced/automations-hooks-readiness.md" in automation
    assert "docs/DAY-4-BUILD.md" in automation
    assert "**Time-box:**" not in automation and "```" not in automation


def agenda_day(number: int) -> str:
    """Return one day's section of the published agenda."""
    agenda = Path("docs/AGENDA.md").read_text(encoding="utf-8")
    section = agenda.split(f"## Day {number} ", 1)[1]
    return section.split("\n## ", 1)[0]


def day_route(guide: str) -> list[str]:
    """Return the elapsed or clock times in a day guide's route table."""
    text = Path("docs", guide).read_text(encoding="utf-8")
    route = text.split("## Today's Route", 1)[1].split("\n## ", 1)[0]
    return re.findall(r"\| (\d\d:\d\d-\d\d:\d\d) +\|", route)


def test_day_three_guide_follows_the_slides_on_the_learners_own_page() -> None:
    """Wednesday: the learner describes a requirements agent, builds one story, and tests it."""
    guide = Path("docs/TOOLS-PRACTICE.md").read_text(encoding="utf-8")
    assert guide.startswith("# Day 3: VS Code and a Requirements Agent")
    assert day_route("TOOLS-PRACTICE.md") == re.findall(r"\| (\d\d:\d\d-\d\d:\d\d) \|", agenda_day(3))
    flat = " ".join(guide.replace("\n>", "\n").split())
    assert "/login" in guide and "Never paste a password or token" in guide
    assert ".github/agents/user-requirements.agent.md" in flat and "`name: user-requirements`" in flat
    assert "Given ..., when ..., then ..." in flat and "Approved: yes" in flat
    assert "type `/exit`, then `copilot`" in flat, "the CLI loads new agents when it starts"
    assert "pytest checks" in guide and "from website import Page" in guide
    assert "**Break it on purpose:**" in guide and "How to build and run" in guide
    for target in ("../labs/04-mcp/README.md", "../labs/06-teach-copilot/README.md", "DAY-4-BUILD.md"):
        assert target in guide
    # The template ships the test helper and prompts, never the finished agent or tests.
    assert not Path(".github/agents/user-requirements.agent.md").exists()
    assert not list(Path("checks").glob("test_*.py"))
    assert Path("checks/website.py").is_file() and Path("checks/README.md").is_file()
    # Attendees read only their own steps; the technical helper notes live in the facilitator guide.
    facilitator = Path("docs/FACILITATOR.md").read_text(encoding="utf-8")
    helpers = facilitator.split("## Day 3 Helper Preparation", 1)[1].split("\n## ", 1)[0]
    assert "Helper Preparation" not in guide
    assert "setup.sh browser" not in guide and "uvicorn" not in guide and "seccomp" not in guide
    assert "presenter demonstration" in helpers and "Never add\n  `--no-sandbox`" in helpers
    assert "uv run uvicorn app.site:app --port 8000" in helpers and "never make the\n  port public" in helpers
    assert "No Dataverse connection, vendor app, or research download" in helpers
    assert "workflow-file pushes" in helpers
    old_link = Path("docs/DAY-2-TOOLS.md").read_text(encoding="utf-8")
    assert "TOOLS-PRACTICE.md" in old_link and "DAY-2-BUILD.md" in old_link
    assert "**Time-box:**" not in old_link


def test_days_three_to_five_follow_the_final_slides() -> None:
    """Owner-approved 20 October: requirements agent, cloud agents, and CI/CD, four hours each."""
    titles = {3: "VS Code and a Requirements Agent", 4: "GitHub Copilot Cloud Agents",
              5: "CI/CD with GitHub Actions"}
    guides = {3: "TOOLS-PRACTICE.md", 4: "DAY-4-BUILD.md", 5: "DAY-5-SHOWCASE.md"}
    for number, guide in guides.items():
        section = agenda_day(number)
        assert guide in section and titles[number] in section.splitlines()[0]
        assert "| 01:30-01:45 | Break" in section and "03:45-04:00" in section
        assert day_route(guide) == re.findall(r"\| (\d\d:\d\d-\d\d:\d\d) \|", section), guide
        lowered = section.lower()
        for topic in ("hook", "automation", "vendor", "evaluation", "lab 07"):
            assert topic not in lowered, (number, topic)
        text = Path("docs", guide).read_text(encoding="utf-8")
        assert text.startswith(f"# Day {number}: {titles[number]}")
        assert "**Done when:**" in text and "## Optional extras" in text, guide
        assert "## Official References\n" in text and "(REFERENCES.md)" in text, guide
        assert "made up" in text, guide
    day4 = " ".join(Path("docs/DAY-4-BUILD.md").read_text(encoding="utf-8").replace("\n>", "\n").split())
    assert "**User story for Copilot**" in day4 and "../labs/03-cloud-agent/README.md" in day4
    assert ".github/agents/code-review.agent.md" in day4 and "reviews/pr-NUMBER.md" in day4
    assert "**Confirmed** or **Not a problem**" in day4 and "@copilot" in day4
    assert "It never changes other files, comments on GitHub, or merges." in day4
    day5 = " ".join(Path("docs/DAY-5-SHOWCASE.md").read_text(encoding="utf-8").split())
    for starter in ("check-my-website.yml", "publish-website-with-approval.yml"):
        assert f".github/workflow-starters/{starter}" in day5
        assert Path(".github/workflow-starters", starter).is_file()
    assert "change `contents: write` to `contents: read`" in day5
    assert "**Required reviewers**" in day5 and "**Approve and deploy**" in day5
    assert "python3 scripts/smoke_test.py" in day5 and "Revert my last commit" in day5
    assert "No password, key, or Azure sign-in" in day5 and "HANDOFF.md" in day5
    assert not Path(".github/workflows/check-my-website.yml").exists()


def test_cloud_agent_lab_delegates_an_approved_story() -> None:
    """Lab 03 is Day 4's delegation block, using the story template and keeping human review."""
    cloud = " ".join(Path("labs/03-cloud-agent/README.md").read_text(encoding="utf-8").split())
    assert "**Time-box:** 40 minutes" in cloud and "Day 4's **delegation lab**" in cloud
    assert "**User story for Copilot**" in cloud and "Nothing changes until you merge" in cloud
    assert "Website change for Copilot" in cloud and "Never wait idle for it" in cloud
    story = Path(".github/ISSUE_TEMPLATE/user-story.md").read_text(encoding="utf-8")
    metadata = yaml.safe_load(story.split("---", 2)[1])
    assert metadata["name"] == "User story for Copilot"
    assert "## Acceptance criteria" in story and "site/index.html" in story and "fictional" in story
    template = Path(".github/ISSUE_TEMPLATE/website-change.md").read_text(encoding="utf-8")
    metadata = yaml.safe_load(template.split("---", 2)[1])
    assert metadata["name"] == "Website change for Copilot"
    assert "site/index.html" in template and "fictional" in template


def test_optional_day_three_labs_use_simple_reviewed_tools() -> None:
    """MCP is read-only, the browser check uses the learner's page, and the picture skill is learner-written."""
    mcp = Path("labs/04-mcp/README.md").read_text(encoding="utf-8")
    assert "https://api.githubcopilot.com/mcp/readonly" in mcp and "**optional extra**" in mcp
    assert "open the **.vscode** folder and select **mcp.json**" in mcp and "Select **Start**" in mcp
    assert "## 2. Watch Copilot Use a Browser" in mcp and "nothing to set up" in mcp
    assert "setup.sh browser" not in mcp and "uvicorn" not in mcp and "Playwright" not in mcp
    customization = Path("labs/06-teach-copilot/README.md").read_text(encoding="utf-8")
    assert "**optional extra**" in customization
    assert ".github/instructions/my-website.instructions.md" in customization
    assert ".github/skills/make-image/SKILL.md" in customization
    assert "python3 scripts/workshop_ai.py image" in customization and "no real people" in customization
    assert "`/add-chat`" in customization and "it can be wrong, so you check" in customization
    assert Path(".github/skills/add-chat/SKILL.md").is_file(), "the chat skill is prepared; the picture skill is not"


def test_advanced_material_is_preserved_outside_the_schedule() -> None:
    """Dropped labs remain available as clearly labelled post-workshop reference."""
    index = Path("post-workshop/advanced/README.md").read_text(encoding="utf-8")
    assert "**Not part of the workshop.**" in index
    pages = re.findall(r"\]\(([a-z-]+\.md)\)", index)
    assert len(pages) == 6
    for page in pages:
        text = (Path("post-workshop/advanced") / page).read_text(encoding="utf-8")
        assert text.startswith("# Advanced Reference: "), page
        assert "**Post-workshop reference, not a workshop lab.**" in text, page
        assert "**Time-box:**" not in text, page
    assert Path("scripts/audit_hook.py").is_file() and Path(".github/agents/vendor-analyst.agent.md").is_file()


def test_attendee_pages_stand_alone_for_first_time_users() -> None:
    """Beginners never need the facilitator agenda, and presenter-only pages are labelled."""
    days = [Path(f"docs/{name}.md") for name in
            ("START-HERE", "DAY-2-BUILD", "TOOLS-PRACTICE", "DAY-4-BUILD", "DAY-5-SHOWCASE")]
    for path in days + [Path("docs/QUICK-REFERENCE.md"), *active_lab_guides()]:
        text = path.read_text(encoding="utf-8")
        assert "AGENDA.md" not in text, path
        for label in re.findall(r"\[([^\]]*)\]\([^)]*REFERENCES\.md\)", text):
            assert label == "Topic map (for presenters)", (path, label)
    for path in days:
        route = path.read_text(encoding="utf-8").split("## Today's Route", 1)[1].split("\n## ", 1)[0]
        # Days 1-2 use clock times; Days 3-5 use elapsed times, as on the final slides.
        assert "| 10:30-10:45 | Break" in route or "| 01:30-01:45 | Break" in route, path
    words = Path("docs/START-HERE.md").read_text(encoding="utf-8")
    assert "| Ask          | In Chat: Copilot only answers." in words
    assert "| Agent        | In Chat: Copilot can change your files." in words
    for lab in ("01-first-website", "02-make-it-useful", "06-teach-copilot", "08-save-and-share"):
        assert Path("labs", lab, "README.md").is_file(), "folder names say what the lab does"


def test_active_routes_do_not_send_learners_to_retired_guides() -> None:
    """Compatibility signposts must not stay on the active learning path."""
    paths = active_lab_guides() + [
        Path("README.md"),
        Path("AGENTS.md"),
        Path("docs/AGENDA.md"),
        Path("docs/START-HERE.md"),
        Path("docs/FACILITATOR.md"),
        Path("docs/REFERENCES.md"),
        Path("docs/PREREQS.md"),
        Path("rehearsal/README.md"),
        Path(".github/prompts/rehearse-workshop.prompt.md"),
        Path("docs/DAY-2-BUILD.md"),
        Path("docs/TOOLS-PRACTICE.md"),
        Path("docs/DAY-4-BUILD.md"),
        Path("docs/DAY-5-SHOWCASE.md"),
        Path("docs/QUICK-REFERENCE.md"),
    ]
    for path in paths:
        text = path.read_text(encoding="utf-8")
        assert "DAY-2-TOOLS.md" not in text, path
        assert "labs/05-dataverse-app/README.md" not in text, path
        assert "07-automations-hooks/README.md" not in text, path
    prerequisites = Path("docs/PREREQS.md").read_text(encoding="utf-8")
    assert "DATAVERSE_CLIENT_SECRET" not in prerequisites


def test_research_links_use_completed_reporting_years() -> None:
    """Pin the teaching window without confusing a publication year with a report year."""
    text = Path("docs/RESEARCH.md").read_text(encoding="utf-8")
    links = [urlsplit(target) for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)]
    reports = [link for link in links if link.path.endswith(".pdf")]
    assert len(reports) == 5
    for year, link in zip(range(2021, 2026), reports, strict=True):
        assert link.scheme == "https" and link.hostname == "www.novonordisk.com"
        assert link.path.endswith(f"annual_report/{year + 1}/novo-nordisk-annual-report-{year}.pdf")


def test_travel_output_is_not_published() -> None:
    """Keep collected research out of source control and the vendor app image."""
    assert "/travel/output/" in Path(".gitignore").read_text(encoding="utf-8").splitlines()
    assert "/travel/" in Path(".dockerignore").read_text(encoding="utf-8").splitlines()


def test_prepared_research_has_explicit_provenance() -> None:
    """A small public fallback is not a fabricated learner observation or vendor fixture."""
    facts = json.loads(Path("docs/annual-report-facts.json").read_text(encoding="utf-8"))
    assert facts["source_mode"] == "prepared_public"
    assert facts["currency"] == "DKK" and facts["unit"] == "million"
    assert urlsplit(facts["source_url"]).hostname == "annualreport.novonordisk.com"
    assert "Net sales" in facts["source_location"]
    assert [row["year"] for row in facts["rows"]] == list(range(2021, 2026))
    assert len(facts["limitations"]) >= 3
    skill = Path(".github/skills/visual-brief/SKILL.md").read_text(encoding="utf-8")
    metadata = yaml.safe_load(skill.split("---", 2)[1])
    assert metadata["name"] == "visual-brief"
    assert metadata["description"]
