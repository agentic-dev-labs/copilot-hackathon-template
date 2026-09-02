"""Deterministic training evaluator for the synthetic report."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from typing import Literal

Status = Literal["Pass", "Fail", "Unclear"]
Sensitivity = Literal["High", "Medium", "Low"]


@dataclass(frozen=True)
class Finding:
    """One checklist result grounded in source evidence."""

    control: str
    status: Status
    evidence: str
    reasoning: str


@dataclass(frozen=True)
class Evaluation:
    """Merged document metadata, findings, score, and sensitivity."""

    vendor: str
    system: str
    data_types: list[str]
    hosting_region: str
    data_residency: str
    subprocessors: list[str]
    soc2_type: str
    report_date: str
    findings: list[Finding]
    score: int
    sensitivity: Sensitivity

    def to_json(self, *, indent: int = 2) -> str:
        """Serialize the evaluation to JSON."""
        return json.dumps(asdict(self), indent=indent)


@dataclass(frozen=True)
class ControlRule:
    name: str
    pass_pattern: str
    fail_pattern: str
    unclear_pattern: str = ""


CONTROL_RULES = (
    ControlRule("MFA on privileged access", r"\bMFA\b.{0,80}\b(privileged|administrator)", r"\bMFA\b.{0,80}\bnot (required|enforced)"),
    ControlRule("TLS 1.2+ in transit", r"\bTLS (1\.[2-9]|[2-9])\b", r"\bTLS 1\.[01]\b"),
    ControlRule("AES-256 at rest", r"\bAES-256\b", r"\b(AES-128|unencrypted at rest)\b"),
    ControlRule("Defined retention schedule", r"\b(retention schedule|retained for \d+ (days|years|months))\b", r"\bno defined retention schedule\b"),
    ControlRule("Documented disposal", r"\b(documented disposal|secure disposal|cryptographic erasure)\b", r"\bdisposal (is )?not documented\b"),
    ControlRule("Incident response", r"\bincident response (plan|program)\b", r"\bno incident response (plan|program)\b"),
    ControlRule("Vulnerability management", r"\bvulnerability (management|scanning|remediation)\b", r"\bno vulnerability management\b"),
    ControlRule("Business continuity", r"\b(business continuity|disaster recovery) (plan|program)\b", r"\bno (business continuity|disaster recovery) (plan|program)\b"),
    ControlRule("Sub-processor oversight", r"\bsub-processors?.{0,100}\b(annual review|due diligence|oversight|assessed)\b", r"\bsub-processors?.{0,100}\bnot (reviewed|assessed)\b"),
    ControlRule(
        "Data subject rights",
        r"\b(data subject rights process|process for access, correction, and deletion requests)\b",
        r"\bno process for data subject rights\b",
        r"\bno direct statement about a process for data subject rights\b",
    ),
)


def _sentence_for_match(text: str, match: re.Match[str]) -> str:
    before = text[: match.start()]
    boundaries = list(re.finditer(r"(?:^|\n+|[.!?]\s+)(?=[A-Z])", before))
    start = boundaries[-1].end() if boundaries else 0
    after = text[match.end() :]
    boundary = re.search(r"[.!?](?=\s+(?:[A-Z#]|\Z))|\n", after)
    end = match.end() + boundary.end() if boundary else len(text)
    return text[start:end].strip(" \n#*-")


def _find(rule: ControlRule, chunks: list[str]) -> Finding:
    for status, pattern in (
        ("Fail", rule.fail_pattern),
        ("Unclear", rule.unclear_pattern),
        ("Pass", rule.pass_pattern),
    ):
        if not pattern:
            continue
        for chunk in chunks:
            match = re.search(pattern, chunk, re.IGNORECASE)
            if match:
                evidence = _sentence_for_match(chunk, match)
                reasons = {
                    "Fail": "The quoted statement contradicts the required control.",
                    "Pass": "The quoted statement directly supports the required control.",
                    "Unclear": "The quoted statement confirms that the report lacks decisive evidence.",
                }
                reason = reasons[status]
                return Finding(rule.name, status, evidence, reason)
    return Finding(
        rule.name,
        "Unclear",
        "",
        "The report does not provide enough evidence to determine implementation.",
    )


def _field(text: str, label: str, default: str = "Not stated") -> str:
    match = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else default


def evaluate_document(chunks: list[str]) -> Evaluation:
    """Evaluate all chunks and merge each control into one evidence-backed result."""
    text = "\n".join(chunks)
    findings = [_find(rule, chunks) for rule in CONTROL_RULES]
    raw_types = _field(text, "Data types", "none")
    data_types = [value.strip() for value in raw_types.split(",") if value.strip()]
    normalized = {value.upper() for value in data_types}
    sensitivity: Sensitivity = (
        "High" if normalized & {"PHI", "PAYMENT"} else "Medium" if normalized & {"PII", "EMPLOYEE"} else "Low"
    )
    return Evaluation(
        vendor=_field(text, "Vendor", "Synthetic Vendor"),
        system=_field(text, "System"),
        data_types=data_types,
        hosting_region=_field(text, "Hosting region"),
        data_residency=_field(text, "Data residency"),
        subprocessors=[value.strip() for value in _field(text, "Sub-processors", "None stated").split(",")],
        soc2_type=_field(text, "SOC 2 type"),
        report_date=_field(text, "Report date"),
        findings=findings,
        score=sum(finding.status == "Pass" for finding in findings),
        sensitivity=sensitivity,
    )
