"""Exercise CLI output and errors using only synthetic source files."""

import json
from pathlib import Path

import pytest

from src.vendor_assurance.cli import main


def test_cli_stdout_is_json_and_report_is_written(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    """A redirected CLI result can be handed directly to the writer agent."""
    monkeypatch.setattr("sys.argv", [
        "vendor-assurance", "src/vendor_assurance/samples/synthetic_soc2_report.md",
        "--output-directory", str(tmp_path / "reports"), "--as-of", "2026-10-26",
    ])

    main()
    captured = capsys.readouterr()

    assert json.loads(captured.out)["score"] == 8
    assert "Wrote" in captured.err
    assert len(list((tmp_path / "reports").glob("*_2026_10_26.md"))) == 1


@pytest.mark.parametrize("path", ["missing.md", "unsupported.pdf"])
def test_cli_errors_are_actionable(
    path: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    """Unsupported files and missing inputs should not print a traceback."""
    monkeypatch.setattr("sys.argv", ["vendor-assurance", path])

    with pytest.raises(SystemExit) as caught:
        main()

    assert caught.value.code == 2
    assert "Traceback" not in capsys.readouterr().err