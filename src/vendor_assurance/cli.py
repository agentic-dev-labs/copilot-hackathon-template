"""Command-line entry point for the synthetic assurance workflow."""

from __future__ import annotations

import argparse
from pathlib import Path

from .chunker import chunk_document
from .evaluator import evaluate_document
from .report_writer import write_report


def main() -> None:
    """Chunk, evaluate, and render a source report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--output-directory", type=Path, default=Path("."))
    parser.add_argument("--max-tokens", type=int, default=220)
    parser.add_argument("--overlap-tokens", type=int, default=30)
    args = parser.parse_args()

    text = args.report.read_text(encoding="utf-8")
    chunks = chunk_document(text, args.max_tokens, args.overlap_tokens)
    evaluation = evaluate_document(chunks)
    template = Path(__file__).parent / "templates" / "privacy_review_template.md"
    output = write_report(evaluation, template, args.output_directory)
    print(evaluation.to_json())
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
