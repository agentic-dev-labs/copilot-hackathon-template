"""Validate checked-in workflow contracts; these are not live Azure tests."""

import json
from pathlib import Path
import subprocess
import tomllib
from unittest.mock import Mock
from urllib.parse import urlsplit

import pytest
import yaml

from scripts import create_attendee_repos


@pytest.mark.parametrize("entries,returncode", [
    ([{"name": ".facilitator"}], 0),
    ([{"name": "RUN-OF-SHOW.private.md"}], 0),
    ([{"name": "NN-NA-Hackathon-2026-10-Engagement-Brief.md"}], 0),
    ({"message": "Not Found"}, 1),
    ({"message": "Unexpected shape"}, 0),
])
def test_attendee_repo_creation_fails_closed(
    entries: object, returncode: int, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Private templates and failed inspections cannot reach repository or team writes."""
    command = Mock(return_value=subprocess.CompletedProcess([], returncode, json.dumps(entries), ""))
    create = Mock()
    grant = Mock()
    monkeypatch.setattr(create_attendee_repos, "run", command)
    monkeypatch.setattr(create_attendee_repos, "create_repo", create)
    monkeypatch.setattr(create_attendee_repos, "grant_team", grant)
    monkeypatch.setattr("sys.argv", ["create_attendee_repos.py", "synthetic-team-01"])

    with pytest.raises(SystemExit):
        create_attendee_repos.main()

    create.assert_not_called()
    grant.assert_not_called()
    assert command.call_count == 1
    assert command.call_args.args[0][1] == "api"


def test_attendee_repos_use_the_explicit_clean_template(monkeypatch: pytest.MonkeyPatch) -> None:
    """An approved clean template is inspected before any copy or team grant."""
    command = Mock(return_value=subprocess.CompletedProcess([], 0, '[{"name":"README.md"}]', ""))
    create = Mock(return_value=True)
    grant = Mock(return_value=True)
    monkeypatch.setattr(create_attendee_repos, "run", command)
    monkeypatch.setattr(create_attendee_repos, "create_repo", create)
    monkeypatch.setattr(create_attendee_repos, "grant_team", grant)
    monkeypatch.setattr("sys.argv", [
        "create_attendee_repos.py", "synthetic-team-01", "--template", "synthetic/clean-template",
    ])

    assert create_attendee_repos.main() == 0
    assert command.call_args.args[0][-1] == "repos/synthetic/clean-template/contents"
    create.assert_called_once_with("synthetic-team-01", template="synthetic/clean-template")
    grant.assert_called_once_with("synthetic-team-01")


def test_python_environments_use_the_lockfile() -> None:
    """Local, cloud-agent, deployment and CI dependencies must agree."""
    for path in Path(".github/workflows").glob("*.yml"):
        workflow = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        assert "jobs" in workflow
        assert "uv sync --locked --extra dev --extra web" in path.read_text(encoding="utf-8")
    assert Path("uv.lock").is_file()


def test_lockfile_does_not_depend_on_a_corporate_mirror() -> None:
    """A clean Codespace must not inherit the presenter's package proxy."""
    lock = tomllib.loads(Path("uv.lock").read_text(encoding="utf-8"))
    for package in lock["package"]:
        if "registry" not in package["source"]:
            continue
        assert package["source"]["registry"] == "https://pypi.org/simple"
        artifacts = package.get("wheels", []) + [package["sdist"]]
        assert all(urlsplit(artifact["url"]).hostname == "files.pythonhosted.org" for artifact in artifacts)


def test_dataverse_deployment_is_opt_in_and_uses_secret_references() -> None:
    """Day one needs no Dataverse; day two must configure the actual server."""
    path = Path(".github/workflows/deploy.yml")
    workflow = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)

    assert workflow["on"]["workflow_dispatch"]["inputs"]["connect_dataverse"]["default"] == "false"
    assert "secretref:dataverse-client-secret" in path.read_text(encoding="utf-8")
    assert "Source: Dataverse" in path.read_text(encoding="utf-8")


def test_docker_context_excludes_private_material() -> None:
    """Git ignore rules alone do not protect a remote Docker build context."""
    patterns = Path(".dockerignore").read_text(encoding="utf-8").splitlines()

    assert "*.private.md" in patterns
    assert "NN-NA-Hackathon-2026-10-Engagement-Brief.md" in patterns
    assert "/.facilitator/" in patterns
    assert ".env*" in patterns
    assert ".git" in patterns


def test_ci_builds_both_deliverables() -> None:
    """Hosted CI must exercise packaging and the image, not only Python unit tests."""
    workflow = yaml.load(Path(".github/workflows/ci.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    commands = [step.get("run", "") for step in workflow["jobs"]["test"]["steps"]]

    assert "uv build --wheel" in commands
    assert "docker build --tag workshop-check ." in commands
    assert "docker build --file Dockerfile.website --tag workshop-website-check ." in commands
    tool_commands = [step.get("run", "") for step in workflow["jobs"]["research-tools"]["steps"]]
    assert workflow["jobs"]["research-tools"]["runs-on"] == "ubuntu-22.04"
    tool_script = "\n".join(tool_commands)
    assert "bash .devcontainer/setup.sh browser" in tool_script
    assert "bash .devcontainer/setup.sh research" in tool_script
    assert ".venv-research/bin/python scripts/check_workshop_mcp.py" in tool_commands


def test_public_deployments_disable_training_writes() -> None:
    """Both creation and redeployment must override any previously enabled training form."""
    workflow = yaml.load(Path(".github/workflows/deploy.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    deploy = next(step for step in workflow["jobs"]["deploy"]["steps"]
                  if step.get("name") == "Deploy to Container Apps")
    assert deploy["run"].count('"WORKSHOP_ALLOW_WRITES=false"') == 2
    assert "WORKSHOP_ALLOW_WRITES=true" not in deploy["run"]


def test_deployment_publishes_exact_revision_evidence_without_attendee_login() -> None:
    """A successful run must yield a verified artifact, not only a printed hostname."""
    text = Path(".github/workflows/deploy.yml").read_text(encoding="utf-8")
    workflow = yaml.load(text, Loader=yaml.BaseLoader)
    inputs = workflow["on"]["workflow_dispatch"]["inputs"]
    assert inputs["expected_sha"]["default"] == ""
    assert inputs["rehearsal_id"]["default"] == ""
    assert "inputs.rehearsal_id" in workflow["run-name"]
    steps = workflow["jobs"]["deploy"]["steps"]
    upload = next(step for step in steps if step.get("uses") == "actions/upload-artifact@v4")
    assert upload["with"]["path"] == "deployment-result.json"
    assert upload["with"]["if-no-files-found"] == "error"
    assert "github.run_id" in upload["with"]["name"]
    assert "github.run_attempt" in upload["with"]["name"]
    assert "--remove-env-vars DATAVERSE_URL" in text
    assert "WORKSHOP_COMMIT=$GITHUB_SHA" in text
    assert "python -m scripts.deployment_result" in text
    assert "az login" not in text


def test_website_target_is_separate_and_validated_before_build() -> None:
    """Only an intentional site folder can enter the Day 1 image."""
    text = Path(".github/workflows/deploy.yml").read_text(encoding="utf-8")
    workflow = yaml.load(text, Loader=yaml.BaseLoader)
    target = workflow["on"]["workflow_dispatch"]["inputs"]["target"]
    assert target["options"] == ["website", "vendor"]
    assert target["default"] == "website"
    assert text.index("python -m app.site --check") < text.index("az acr build")
    dockerfile = Path("Dockerfile.website").read_text(encoding="utf-8")
    assert "COPY site ./site" in dockerfile
    assert "COPY . " not in dockerfile
    assert "app.site:app" in dockerfile
    assert "research" not in dockerfile
    assert "site/**/*.md" in Path(".dockerignore").read_text(encoding="utf-8")
    assert "uv run --no-sync python -m app.site --check" in text
    assert "uv run --no-sync python -m scripts.deployment_result" in text
    assert "uv run --no-sync python -m app.site --check" in Path(".github/workflows/ci.yml").read_text(encoding="utf-8")