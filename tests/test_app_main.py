"""Exercise the starter page without credentials, Azure, or a live server."""

from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from app import main
from src.vendor_assurance.dataverse import DataverseError


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    """Use a fictional attendee without editing the repository's config file."""
    monkeypatch.setattr(main, "load", lambda: {"displayName": "Synthetic Builder", "appName": "synthetic-builder"})
    monkeypatch.delenv("DATAVERSE_URL", raising=False)
    return TestClient(main.app)


def test_sample_page_and_health(client: TestClient) -> None:
    """Day one runs with local synthetic data and no service access."""
    response = client.get("/")

    assert response.status_code == 200
    assert "Synthetic Builder" in response.text
    assert "local synthetic samples" in response.text
    assert response.text.count("class='score'") == 3
    assert client.get("/healthz").json() == {"status": "ok"}


def test_config_failure_is_readable(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    """The unedited placeholder gives instructions instead of a server error."""
    monkeypatch.setattr(main, "load", Mock(side_effect=ValueError("Edit config.json")))

    response = client.get("/")

    assert response.status_code == 400
    assert "Edit config.json" in response.text


def test_empty_dataverse_does_not_masquerade_as_samples(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    """An empty query result differs from unavailable Dataverse."""
    monkeypatch.setenv("DATAVERSE_URL", "https://synthetic.example")
    monkeypatch.setattr(main, "_from_dataverse", lambda attendee: [])

    response = client.get("/")

    assert "no rows tagged" in response.text
    assert "local synthetic samples" not in response.text


def test_dataverse_failure_is_labelled(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    """Fallback must not look like a successful Dataverse connection."""
    monkeypatch.setenv("DATAVERSE_URL", "https://synthetic.example")
    monkeypatch.setattr(main, "_from_dataverse", Mock(side_effect=DataverseError("HTTP 403")))

    response = client.get("/")

    assert response.status_code == 200
    assert "Dataverse unavailable: HTTP 403" in response.text
    assert "local synthetic samples" in response.text


def test_unscored_dataverse_row_is_not_shown_as_a_result(
    client: TestClient, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A manually added vendor has no score until the evaluator runs."""
    monkeypatch.setenv("DATAVERSE_URL", "https://synthetic.example")
    monkeypatch.setattr(main, "_from_dataverse", lambda attendee: [
        {"vendor": "Synthetic Pending Vendor", "score": None, "sensitivity": ""},
    ])

    response = client.get("/")

    assert response.status_code == 200
    assert "Not assessed" in response.text
    assert "None/10" not in response.text


def test_names_are_escaped_for_odata_and_html(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    """A fictional apostrophe must not break a filter or inject page markup."""
    transport = Mock()
    transport.rows.return_value = [{"cr522_vendor": "<Synthetic>", "cr522_score": 8}]
    monkeypatch.setattr(main.DataverseClient, "from_environment", lambda: transport)

    assert main._from_dataverse("Synthetic O'Brien")[0]["vendor"] == "<Synthetic>"
    assert transport.rows.call_args.kwargs["$filter"] == "cr522_attendee eq 'Synthetic O''Brien'"
    monkeypatch.setenv("DATAVERSE_URL", "https://synthetic.example")
    assert "&lt;Synthetic&gt;" in client.get("/").text