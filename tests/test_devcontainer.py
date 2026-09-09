"""Check the startup contract without requiring a container runtime."""

import json
from pathlib import Path


def test_machine_requirements_and_notes() -> None:
    """Keep machine minimums explicit and documentation out of schema properties."""
    config = json.loads(Path(".devcontainer/devcontainer.json").read_text(encoding="utf-8"))

    assert config["hostRequirements"] == {"cpus": 4, "memory": "16gb", "storage": "32gb"}
    assert "//" not in config
    assert Path(".devcontainer/README.md").is_file()


def test_terminal_uses_the_installed_virtual_environment() -> None:
    """Bare Python and CLI commands must resolve to the project environment."""
    config = json.loads(Path(".devcontainer/devcontainer.json").read_text(encoding="utf-8"))

    assert config["waitFor"] == "updateContentCommand"
    assert config["updateContentCommand"] == "bash .devcontainer/setup.sh"
    setup = Path(".devcontainer/setup.sh").read_text(encoding="utf-8")
    assert "uv sync --locked --extra dev --extra web" in setup
    assert "npm" not in setup
    assert config["remoteEnv"]["UV_NATIVE_TLS"] == "true"
    assert 'export UV_NATIVE_TLS="${UV_NATIVE_TLS:-true}"' in setup
    assert "python -m rehearsal.network" in setup
    assert "exit 1" in setup
    assert config["remoteEnv"]["VIRTUAL_ENV"] == "${containerWorkspaceFolder}/.venv"
    assert config["remoteEnv"]["PATH"].startswith("${containerWorkspaceFolder}/.venv/bin:")


def test_setup_does_not_hide_failures_or_request_day_two_secrets() -> None:
    """The first lab needs working tools, not Dataverse credentials."""
    config = json.loads(Path(".devcontainer/devcontainer.json").read_text(encoding="utf-8"))

    for command in config["onCreateCommand"].values():
        assert "pipefail" in command
        assert "||" not in command
    assert "secrets" not in config