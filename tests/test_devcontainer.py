"""Check the startup contract without requiring a container runtime."""

import json
from pathlib import Path
import asyncio
from contextlib import asynccontextmanager
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from scripts import check_workshop_mcp


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
    assert "npm ci --prefix .devcontainer/browser --ignore-scripts" in setup
    assert "--requirement .devcontainer/research-requirements.txt" in setup
    assert "install --with-deps chromium" in setup
    assert "bash .devcontainer/mcp.sh check" in setup
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


def test_mcp_examples_are_private_and_use_pinned_tools() -> None:
    """Learners add trusted remote-workspace connections, not a public MCP endpoint."""
    example = json.loads(Path(".devcontainer/mcp.example.json").read_text(encoding="utf-8"))
    assert set(example["servers"]) == {"playwright", "markitdown"}
    for name, server in example["servers"].items():
        assert server == {
            "type": "stdio", "command": "bash",
            "args": ["${workspaceFolder}/.devcontainer/mcp.sh", name],
        }
    launcher = Path(".devcontainer/mcp.sh").read_text(encoding="utf-8")
    assert "--headless --isolated --executable-path" in launcher
    assert "chromiumSandbox: true, executablePath: chromium.executablePath()" in launcher
    assert "--no-sandbox" not in launcher
    assert "--ignore-https-errors" not in launcher
    assert "--port" not in launcher
    package = json.loads(Path(".devcontainer/browser/package.json").read_text(encoding="utf-8"))
    lock = json.loads(Path(".devcontainer/browser/package-lock.json").read_text(encoding="utf-8"))
    assert package["dependencies"]["@playwright/mcp"] == "0.0.81"
    assert lock["packages"]["node_modules/@playwright/mcp"]["version"] == "0.0.81"
    requirements = Path(".devcontainer/research-requirements.txt").read_text(encoding="utf-8")
    assert "markitdown-mcp==0.0.1a7" in requirements
    assert "markitdown==0.1.7" in requirements
    assert "azure-ai-contentunderstanding==1.2.0b1" in requirements


def test_research_stays_out_of_git_and_container_builds() -> None:
    """Public research does not become synthetic fixture data or a deployed document archive."""
    for name in (".gitignore", ".dockerignore"):
        text = Path(name).read_text(encoding="utf-8")
        assert "/research/" in text.splitlines()
        assert ".venv-research" in text


@pytest.mark.parametrize("is_error,text", [(False, "Synthetic check"), (True, "Synthetic check"), (False, "Wrong")])
def test_mcp_smoke_checks_sdk_two_result_fields(monkeypatch, is_error: bool, text: str) -> None:
    """Use SDK 2's Python field names and reject both tool errors and wrong content."""
    client = SimpleNamespace(
        initialize=AsyncMock(),
        list_tools=AsyncMock(return_value=SimpleNamespace(tools=[SimpleNamespace(name="convert_to_markdown")])),
        call_tool=AsyncMock(return_value=SimpleNamespace(is_error=is_error, content=[SimpleNamespace(text=text)])),
    )

    @asynccontextmanager
    async def transport(parameters):
        assert parameters.command == "bash"
        yield None, None

    @asynccontextmanager
    async def session(reader, writer):
        yield client

    modules = {
        "mcp": SimpleNamespace(StdioServerParameters=SimpleNamespace, ClientSession=session),
        "mcp.client.stdio": SimpleNamespace(stdio_client=transport),
    }
    monkeypatch.setattr(check_workshop_mcp, "import_module", modules.__getitem__)
    operation = check_workshop_mcp.invoke("markitdown", "convert_to_markdown", {}, "Synthetic check")
    if is_error or text != "Synthetic check":
        with pytest.raises(RuntimeError, match="expected synthetic content"):
            asyncio.run(operation)
    else:
        asyncio.run(operation)
    client.initialize.assert_awaited_once()
    client.call_tool.assert_awaited_once_with("convert_to_markdown", {})