"""Keep executable examples and timetable claims aligned with the labs."""

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def test_lab_timeboxes_match_the_agenda() -> None:
    """Optional exercises must not silently extend the published core blocks."""
    agenda = Path("docs/AGENDA.md").read_text(encoding="utf-8")
    rows = re.findall(r"\| (\d\d):(\d\d)-(\d\d):(\d\d) \| Lab (\d\d):", agenda)
    assert len(rows) == 9
    for start_hour, start_minute, end_hour, end_minute, number in rows:
        minutes = (int(end_hour) - int(start_hour)) * 60 + int(end_minute) - int(start_minute)
        lab = next(Path("labs").glob(f"{number}-*/README.md"))
        assert f"**Time-box:** {minutes} minutes" in lab.read_text(encoding="utf-8")


def test_daily_schedule_has_no_gaps_or_overlaps() -> None:
    """The published blocks must fill the stated days without adding hidden time."""
    agenda = Path("docs/AGENDA.md").read_text(encoding="utf-8")
    sections = re.split(r"## Day \d[^\n]*\n", agenda)[1:]
    assert len(sections) == 5
    for section, expected in zip(sections, [360, 360, 210, 210, 210], strict=True):
        blocks = re.findall(r"\| (\d\d):(\d\d)-(\d\d):(\d\d) \|", section)
        intervals = [
            (int(start_hour) * 60 + int(start_minute), int(end_hour) * 60 + int(end_minute))
            for start_hour, start_minute, end_hour, end_minute in blocks
        ]
        assert all(end > start for start, end in intervals)
        assert sum(end - start for start, end in intervals) == expected
        assert all(previous[1] == following[0] for previous, following in zip(intervals, intervals[1:]))


def test_private_run_sheet_matches_when_present() -> None:
    """Validate local presenter notes without requiring private files in CI."""
    private_path = Path("RUN-OF-SHOW.private.md")
    if not private_path.exists():
        return
    pattern = r"\| (\d\d:\d\d)[-\u2013](\d\d:\d\d) \|"
    public = re.findall(pattern, Path("docs/AGENDA.md").read_text(encoding="utf-8"))
    private = re.findall(pattern, private_path.read_text(encoding="utf-8"))
    assert public == private


def test_customization_examples_parse() -> None:
    """Broken frontmatter can silently prevent a customization from loading."""
    for lab in Path("labs").glob("*/README.md"):
        text = lab.read_text(encoding="utf-8")
        for language, body in re.findall(r"```(json|yaml|markdown)\n(.*?)\n[ \t]*```", text, re.DOTALL):
            body = "\n".join(line[3:] if line.startswith("   ") else line for line in body.splitlines())
            if language == "json":
                json.loads(body)
            elif language == "yaml":
                yaml.safe_load(body)
            elif body.startswith("---\n"):
                metadata = yaml.safe_load(body.split("---", 2)[1])
                assert isinstance(metadata, dict)
                assert metadata.get("description")


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


def test_labs_have_completion_checks_and_optional_work() -> None:
    """Attendees need an observable finish and a separate early-finisher path."""
    for path in Path("labs").glob("*/README.md"):
        text = path.read_text(encoding="utf-8")
        assert "**Done when:**" in text, path
        assert "## Optional extras" in text, path


def test_local_document_links_resolve() -> None:
    """Check the simple relative links used by the workshop documentation."""
    files = [Path("README.md"), Path("AGENTS.md")]
    for directory in ("docs", "labs", ".github", "src"):
        files.extend(Path(directory).rglob("*.md"))
    for path in files:
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            link = urlsplit(target)
            if link.scheme or link.netloc or not link.path:
                continue
            assert (path.parent / unquote(link.path)).exists(), f"{path}: {target}"