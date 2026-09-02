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

    assert result.score == 4
    assert result.sensitivity == "Medium"
    assert statuses["Defined retention schedule"] == "Fail"
    assert statuses["MFA on privileged access"] == "Pass"
    assert next(
        finding.evidence
        for finding in result.findings
        if finding.control == "MFA on privileged access"
    ) in text
