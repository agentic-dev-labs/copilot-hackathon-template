"""Validate checked-in workflow contracts; these are not live Azure tests."""

from pathlib import Path
import tomllib
from urllib.parse import urlsplit

import yaml


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