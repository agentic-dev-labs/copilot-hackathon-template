from datetime import date

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
