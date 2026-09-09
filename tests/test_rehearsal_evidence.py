"""Check that rehearsal records cannot pass by omitting live requirements."""

import json
from pathlib import Path

import pytest
import yaml

from rehearsal import evidence


@pytest.fixture
def ledger(monkeypatch: pytest.MonkeyPatch) -> dict:
    """Create a synthetic record without depending on the current Git revision."""
    monkeypatch.setattr(evidence, "git_state", lambda: {"commit": "a" * 40, "dirty": False})
    return evidence.initialize("synthetic/rehearsal")


def test_manifest_covers_all_labs_in_workshop_order() -> None:
    """Keep every guide, check selector, and core lab discoverable."""
    labs = evidence.manifest()
    assert [lab["id"] for lab in labs] == ["00", "01", "02", "08", "05", "03", "04", "07", "06"]
    for lab in labs:
        assert Path(lab["guide"]).is_file()
        assert lab["checks"]
        assert all(Path(path).is_file() for path in lab["tests"])


def test_every_live_condition_starts_pending(ledger: dict) -> None:
    """An initialized checklist is not a completed workshop."""
    assert all(evidence.lab_status(ledger, lab) == "pending" for lab in evidence.manifest())
    assert "pending" in evidence.render_summary(ledger)


def test_passing_requires_observation_and_evidence(ledger: dict) -> None:
    """A green unit suite must not automatically pass the browser journey."""
    with pytest.raises(ValueError, match="Passing requires"):
        evidence.record(ledger, "01", "browser", "passed", [], "Tests passed")
    with pytest.raises(ValueError, match="Passing requires"):
        evidence.record(ledger, "01", "browser", "passed",
                        ["https://github.com/synthetic/rehearsal/issues/1"], "Tests passed")


def test_missing_entries_never_pass(ledger: dict) -> None:
    """Removing a blocked check from JSON must not improve completion status."""
    lab = evidence.manifest()[0]
    ledger["labs"][lab["id"]] = {}
    assert evidence.lab_status(ledger, lab) == "pending"


def test_blocked_and_passed_are_distinct(ledger: dict) -> None:
    """Keep a concrete access blocker visible without requiring a fake proof link."""
    evidence.record(ledger, "00", "access", "blocked", [], "Copilot sign-in required")
    assert evidence.lab_status(ledger, evidence.manifest()[0]) == "blocked"
    for key in ledger["labs"]["00"]:
        evidence.record(ledger, "00", key, "passed",
                        ["https://github.com/synthetic/rehearsal/actions/runs/1"],
                        "Synthetic observation for this test", observed=True)
    assert evidence.lab_status(ledger, evidence.manifest()[0]) == "passed"


@pytest.mark.parametrize("reference", [
    "https://user:secret@example.invalid/run", "https://example.invalid/run?token=secret",
    "http://example.invalid/run", "missing-evidence.json", ".facilitator/README.md",
])
def test_references_reject_unsafe_or_missing_evidence(reference: str) -> None:
    """Do not preserve private files, signed tokens, or nonexistent attachments."""
    with pytest.raises(ValueError):
        evidence.validate_reference(reference)


def test_prompt_is_discoverable_and_has_every_lab() -> None:
    """The comprehensive prompt must run as an agent and cover all nine exercises."""
    text = Path(".github/prompts/rehearse-workshop.prompt.md").read_text(encoding="utf-8")
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["name"] == "rehearse-workshop"
    assert metadata["agent"] == "agent"
    assert metadata["description"]
    for lab in evidence.manifest():
        assert lab["guide"] in text
    assert "az login" in text
    assert "Do not run" in text
    assert "built-in browser tools" in text
    assert json.loads(Path("rehearsal/labs.json").read_text(encoding="utf-8"))["schema_version"] == 1


def test_agent_host_has_a_skill_entrypoint() -> None:
    """Prompt files alone are insufficient in Agent Host sessions."""
    text = Path(".github/skills/workshop-rehearsal/SKILL.md").read_text(encoding="utf-8")
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["name"] == "workshop-rehearsal"
    assert metadata["description"]
    assert "../../prompts/rehearse-workshop.prompt.md" in text