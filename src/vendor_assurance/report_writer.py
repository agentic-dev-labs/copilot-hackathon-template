"""Render a completed privacy review from an evaluation."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from .evaluator import Evaluation

PLACEHOLDER = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def _safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "_", value).strip("_") or "Vendor"


def render_report(evaluation: Evaluation, template: str) -> str:
    """Fill the report template and reject incomplete output."""
    rows = "\n".join(
        f"| {item.control} | {item.status} | {item.evidence} | {item.reasoning} |"
        for item in evaluation.findings
    )
    values = {
        "VENDOR": evaluation.vendor,
        "SYSTEM": evaluation.system,
        "DATA_TYPES": ", ".join(evaluation.data_types),
        "HOSTING_REGION": evaluation.hosting_region,
        "DATA_RESIDENCY": evaluation.data_residency,
        "SUBPROCESSORS": ", ".join(evaluation.subprocessors),
        "SOC2_TYPE": evaluation.soc2_type,
        "REPORT_DATE": evaluation.report_date,
        "SCORE": str(evaluation.score),
        "SENSITIVITY": evaluation.sensitivity,
        "FINDINGS": rows,
    }
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    remaining = PLACEHOLDER.findall(rendered)
    if remaining:
        raise ValueError(f"Unfilled template placeholders: {', '.join(sorted(set(remaining)))}")
    return rendered


def write_report(
    evaluation: Evaluation,
    template_path: Path,
    output_directory: Path = Path("."),
    review_date: date | None = None,
) -> Path:
    """Write a dated report and return its path."""
    rendered = render_report(evaluation, template_path.read_text(encoding="utf-8"))
    stamp = (review_date or date.today()).strftime("%Y_%m_%d")
    output = output_directory / f"PrivacyReview_{_safe_name(evaluation.vendor)}_{stamp}.md"
    output.write_text(rendered, encoding="utf-8")
    return output
