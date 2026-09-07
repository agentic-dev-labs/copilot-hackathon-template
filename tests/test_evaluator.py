from datetime import date
from pathlib import Path

import pytest

from src.vendor_assurance.chunker import chunk_document
from src.vendor_assurance.evaluator import evaluate_document


def test_scoring_and_sensitivity() -> None:
    text = """Vendor: Synthetic Example
System: Training Portal
Data types: PII, employee
MFA is required for all privileged administrator accounts.
Connections use TLS 1.2. Data is encrypted with AES-256 at rest.
There is no defined retention schedule.
The incident response plan is tested annually.
"""
    result = evaluate_document(chunk_document(text, max_tokens=18, overlap_tokens=4))
    statuses = {finding.control: finding.status for finding in result.findings}

    assert result.score == 3
    assert result.sensitivity == "High"
    assert statuses["Defined retention schedule"] == "Fail"
    assert statuses["MFA on privileged access"] == "Pass"
    assert statuses["Incident response SLA within 72 hours"] == "Unclear"
    assert next(
        finding.evidence
        for finding in result.findings
        if finding.control == "MFA on privileged access"
    ) in text


def test_metadata_controls_and_gaps() -> None:
    text = """Vendor: Synthetic Example
System: Training Portal
Data types: none
Hosting region: EU West training region
Data residency: Records remain in the EU West training region
Sub-processors: Example Hosting Cooperative
SOC 2 type: Type II
Report date: 2026-06-30
The incident response plan commits to notifying customers within 72 hours.
"""
    result = evaluate_document(
        chunk_document(text, max_tokens=200, overlap_tokens=10), today=date(2026, 10, 26)
    )
    statuses = {finding.control: finding.status for finding in result.findings}

    assert statuses["Sub-processor disclosure"] == "Pass"
    assert statuses["SOC 2 Type II within 12 months"] == "Pass"
    assert statuses["Data residency stated and consistent"] == "Pass"
    assert statuses["Incident response SLA within 72 hours"] == "Pass"
    assert result.sensitivity == "Low"


def test_stale_soc2_report_fails() -> None:
    text = """Vendor: Synthetic Example
SOC 2 type: Type II
Report date: 2024-01-31
"""
    result = evaluate_document(
        chunk_document(text, max_tokens=200, overlap_tokens=10), today=date(2026, 10, 26)
    )
    finding = next(
        item for item in result.findings if item.control == "SOC 2 Type II within 12 months"
    )

    assert finding.status == "Fail"
    assert finding.evidence == "Report date: 2024-01-31"
    assert any("SOC 2 Type II" in gap for gap in result.gaps)


def test_wrapped_evidence_preserves_the_original_quote() -> None:
    """Matching may span whitespace, but evidence must not rewrite it."""
    text = "MFA is  required for all\nprivileged administrator accounts."
    finding = evaluate_document([text]).findings[0]

    assert finding.status == "Pass"
    assert finding.evidence == text


@pytest.mark.parametrize("text", [
    "MFA is mentioned in the policy. Privileged administrator accounts are reviewed.",
    "MFA may be introduced for privileged administrator accounts.",
])
def test_mfa_mentions_do_not_prove_enforcement(text: str) -> None:
    """A plan or an unrelated sentence cannot satisfy an enforcement requirement."""
    assert evaluate_document([text]).findings[0].status == "Unclear"


@pytest.mark.parametrize("text,control", [
    ("The policy requires\nTLS 1.2 for all connections.", "TLS 1.2+ in transit"),
    ("A documented\ndisposal process is in place.", "Documented disposal"),
    ("The provider documents a data subject\nrights process.", "Data subject rights"),
])
def test_wrapped_phrases_keep_the_complete_source_sentence(text: str, control: str) -> None:
    """Format changes must neither hide a control nor shorten its evidence."""
    finding = next(item for item in evaluate_document([text]).findings if item.control == control)

    assert finding.status == "Pass"
    assert finding.evidence == text


def test_capitalized_metadata_continuation() -> None:
    """A region name on a new line remains part of the residency field."""
    text = "Hosting region: EU West\nData residency: Records remain in the\nEU West\n\n"
    result = evaluate_document([text])
    finding = next(item for item in result.findings if item.control == "Data residency stated and consistent")

    assert result.data_residency == "Records remain in the EU West"
    assert finding.status == "Pass"
    assert finding.evidence == "Data residency: Records remain in the\nEU West"


def test_empty_metadata_does_not_consume_the_next_field() -> None:
    """An empty value must not borrow another field's contents."""
    result = evaluate_document(["Vendor:\nSystem: Training Portal\nData types: PII\n"])

    assert result.vendor == "Synthetic Vendor"
    assert result.system == "Training Portal"
    assert result.data_types == ["PII"]


def test_future_soc2_report_needs_clarification() -> None:
    """A future date does not prove that a current report exists."""
    result = evaluate_document(["SOC 2 type: Type II\nReport date: 2027-01-01"], today=date(2026, 10, 26))
    finding = next(item for item in result.findings if item.control == "SOC 2 Type II within 12 months")

    assert finding.status == "Unclear"
    assert finding.evidence == "Report date: 2027-01-01"


@pytest.mark.parametrize("value,status", [("none", "Pass"), ("not stated", "Unclear"), ("", "Unclear")])
def test_subprocessor_disclosure(value: str, status: str) -> None:
    """Explicitly using no sub-processors differs from a missing disclosure."""
    result = evaluate_document([f"Sub-processors: {value}"])
    finding = next(item for item in result.findings if item.control == "Sub-processor disclosure")

    assert finding.status == status


@pytest.mark.parametrize("sample,score,sensitivity", [
    ("synthetic_soc2_harborline_congress.md", 10, "Medium"),
    ("synthetic_soc2_report.md", 8, "High"),
    ("synthetic_soc2_meridian_outreach.md", 2, "High"),
])
def test_documented_samples_at_the_workshop_date(sample: str, score: int, sensitivity: str) -> None:
    """Keep the documented outcomes and literal quotations reproducible."""
    source = (Path("src/vendor_assurance/samples") / sample).read_text(encoding="utf-8")
    evaluation = evaluate_document(chunk_document(source, 220, 30), today=date(2026, 10, 26))

    assert evaluation.score == score
    assert evaluation.sensitivity == sensitivity
    assert len(evaluation.findings) == 10
    assert len(evaluation.gaps) == 10 - score
    for finding in evaluation.findings:
        if finding.status in {"Pass", "Fail"}:
            assert finding.evidence
        if finding.evidence:
            assert finding.evidence in source
