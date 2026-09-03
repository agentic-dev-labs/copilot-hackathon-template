from datetime import date
from pathlib import Path

import pytest

from src.vendor_assurance.chunker import chunk_document
from src.vendor_assurance.evaluator import evaluate_document
from src.vendor_assurance.report_writer import render_report, write_report

TEMPLATE = Path("src/vendor_assurance/templates/privacy_review_template.md")
SAMPLE = Path("src/vendor_assurance/samples/synthetic_soc2_report.md")


def _evaluation():
    text = SAMPLE.read_text(encoding="utf-8")
    return evaluate_document(chunk_document(text, max_tokens=220, overlap_tokens=30))


def test_writes_into_a_directory_that_does_not_exist_yet(tmp_path: Path) -> None:
    """An automation runs in a fresh clone, where the output directory is absent."""
    output = write_report(
        _evaluation(),
        TEMPLATE,
        tmp_path / "reports",
        review_date=date(2026, 10, 26),
    )

    assert output.exists()
    assert output.name.endswith("_2026_10_26.md")
    assert output.parent.name == "reports"


def test_unfilled_placeholder_is_rejected() -> None:
    with pytest.raises(ValueError, match="MISSING"):
        render_report(_evaluation(), "Vendor {{VENDOR}} and {{MISSING}}")
