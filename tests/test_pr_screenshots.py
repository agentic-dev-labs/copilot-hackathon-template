"""The Screenshots job shows the UI check's pictures on the pull request, safely and in plain words."""

import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pr_screenshots  # noqa: E402

RESULTS = [
    {"page": "home", "screen": "desktop", "screenshot": "home-desktop.png", "problems": []},
    {"page": "home", "screen": "phone", "screenshot": "home-phone.png",
     "problems": ["Wider than a phone screen by 45 pixels"]},
    {"page": "idea-team-lunch", "screen": "desktop", "screenshot": "idea-team-lunch-desktop.png", "problems": []},
    {"page": "idea-team-lunch", "screen": "phone", "screenshot": "idea-team-lunch-phone.png", "problems": []},
]
IMAGES = "https://github.com/synthetic-org/synthetic-site/blob/ui-screenshots/pr-5/run-77"


def test_comment_shows_the_result_problems_and_both_screens() -> None:
    """The first page is open; idea pages fold away; every problem is listed once, in words."""
    body = pr_screenshots.comment_markdown(RESULTS, IMAGES, "a" * 40, "https://example.invalid/run")
    assert body.startswith(pr_screenshots.MARKER + "\n")
    assert "### UI check: 3 of 4 screens passed" in body and "for commit `aaaaaaa`" in body
    assert "- **Your first page, phone:** Wider than a phone screen by 45 pixels" in body
    assert "**Your first page: Fail**" in body
    assert "<summary>Idea page team-lunch: Pass</summary>" in body
    assert f'<img src="{IMAGES}/home-desktop.png?raw=true" width="520"' in body
    assert f'<img src="{IMAGES}/home-phone.png?raw=true" width="200"' in body
    assert "[Open the run](https://example.invalid/run)" in body


def test_comment_without_stored_pictures_points_to_the_artifacts() -> None:
    """When the branch could not be written, the comment still says what passed."""
    body = pr_screenshots.comment_markdown(RESULTS[:2], "")
    assert "<img" not in body and "No screenshot" in body and "**Artifacts**" in body


def test_problem_text_cannot_break_the_comment() -> None:
    """Page text reaches the comment as one short line, with no table pipes or raw tags."""
    results = [{"page": "home", "screen": "phone", "screenshot": "../evil.png",
                "problems": ["a | b\n<script>alert(1)</script>" + "x" * 400]}]
    body = pr_screenshots.comment_markdown(results, IMAGES)
    problem = next(line for line in body.splitlines() if line.startswith("- **"))
    assert "|" not in problem and "<script>" not in problem and problem.endswith("...")
    assert "evil.png" not in body, "only plain screenshot names become image links"


def test_pictures_go_to_their_own_branch_and_retry_when_it_moved(tmp_path: Path, monkeypatch) -> None:
    """A first run creates ui-screenshots; a run that meets another one adds on top of it."""
    for name in ("home-desktop.png", "home-phone.png", "notes.txt", "bad name.png"):
        (tmp_path / name).write_bytes(b"\x89PNG")
    calls: list[tuple[str, str, object]] = []
    moved = {"once": False}

    def fake_api(method: str, path: str, body: object = None) -> object:
        calls.append((method, path, body))
        if path.endswith("/git/blobs"):
            return {"sha": f"blob{len(calls)}"}
        if path.endswith("/git/ref/heads/ui-screenshots"):
            return {"object": {"sha": "parent1"}}
        if "/git/commits/" in path:
            return {"tree": {"sha": "basetree"}}
        if path.endswith("/git/trees"):
            return {"sha": "tree1"}
        if path.endswith("/git/commits"):
            return {"sha": "commit1"}
        if method == "PATCH" and not moved["once"]:
            moved["once"] = True
            raise pr_screenshots.ApiError(422, "Update is not a fast forward")
        return {}

    monkeypatch.setattr(pr_screenshots, "api", fake_api)
    monkeypatch.setattr(pr_screenshots.time, "sleep", lambda seconds: None)
    assert pr_screenshots.store_pictures(tmp_path, "synthetic-org/synthetic-site", "pr-5/run-77")
    blobs = [call for call in calls if call[1].endswith("/git/blobs")]
    assert len(blobs) == 2, "only plain .png names are stored"
    tree = next(call[2] for call in calls if call[1].endswith("/git/trees"))
    assert tree["base_tree"] == "basetree"
    assert {entry["path"] for entry in tree["tree"]} == {"pr-5/run-77/home-desktop.png", "pr-5/run-77/home-phone.png"}
    patches = [call for call in calls if call[0] == "PATCH"]
    assert len(patches) == 2 and patches[-1][2] == {"sha": "commit1", "force": False}, "never a force push"


def test_first_run_creates_the_branch_without_history(tmp_path: Path, monkeypatch) -> None:
    """No ui-screenshots branch yet: a commit with no parent, then a new branch."""
    (tmp_path / "home-desktop.png").write_bytes(b"\x89PNG")
    calls: list[tuple[str, str, object]] = []

    def fake_api(method: str, path: str, body: object = None) -> object:
        calls.append((method, path, body))
        if path.endswith("/git/ref/heads/ui-screenshots"):
            raise pr_screenshots.ApiError(404, "Not Found")
        return {"sha": "new"}

    monkeypatch.setattr(pr_screenshots, "api", fake_api)
    assert pr_screenshots.store_pictures(tmp_path, "synthetic-org/synthetic-site", "pr-1/run-1")
    commit = next(call[2] for call in calls if call[1].endswith("/git/commits"))
    assert commit["parents"] == []
    assert calls[-1] == ("POST", "repos/synthetic-org/synthetic-site/git/refs",
                         {"ref": "refs/heads/ui-screenshots", "sha": "new"})


def test_a_refused_write_is_a_warning_not_a_crash(tmp_path: Path, monkeypatch, capsys) -> None:
    """Without permission to write, the comment is still posted, pointing to the artifacts."""
    (tmp_path / "home-desktop.png").write_bytes(b"\x89PNG")

    def refuse(method: str, path: str, body: object = None) -> object:
        raise pr_screenshots.ApiError(403, "Resource not accessible by integration")

    monkeypatch.setattr(pr_screenshots, "api", refuse)
    assert not pr_screenshots.store_pictures(tmp_path, "synthetic-org/synthetic-site", "pr-1/run-1")
    assert "::warning::" in capsys.readouterr().out


def test_new_comment_replaces_only_earlier_check_comments(monkeypatch) -> None:
    """The newest pictures stay at the bottom; people's own comments are never touched."""
    deleted: list[str] = []
    existing = [
        {"id": 1, "user": {"login": "github-actions[bot]"}, "body": pr_screenshots.MARKER + "\nold"},
        {"id": 2, "user": {"login": "synthetic-learner"}, "body": pr_screenshots.MARKER + "\nquoted by a person"},
        {"id": 3, "user": {"login": "github-actions[bot]"}, "body": "another workflow's comment"},
        {"id": 9, "user": {"login": "github-actions[bot]"}, "body": pr_screenshots.MARKER + "\nnew"},
    ]

    def fake_api(method: str, path: str, body: object = None) -> object:
        if method == "POST":
            return {"id": 9}
        if method == "GET":
            return existing
        deleted.append(path)
        return None

    monkeypatch.setattr(pr_screenshots, "api", fake_api)
    assert pr_screenshots.post_comment("synthetic-org/synthetic-site", 5, "body") == 9
    assert deleted == ["repos/synthetic-org/synthetic-site/issues/comments/1"]


def test_main_links_the_pictures_it_stored(tmp_path: Path, monkeypatch) -> None:
    """The comment's picture links point at the folder the pictures were stored in."""
    (tmp_path / "results.json").write_text(json.dumps(RESULTS[:2]), encoding="utf-8")
    posted: dict = {}
    monkeypatch.setenv("GITHUB_REPOSITORY", "synthetic-org/synthetic-site")
    monkeypatch.setenv("GITHUB_RUN_ID", "77")
    monkeypatch.setattr(pr_screenshots, "store_pictures", lambda folder, repository, place: place == "pr-5/run-77")
    monkeypatch.setattr(pr_screenshots, "post_comment",
                        lambda repository, number, body: posted.update(number=number, body=body))
    assert pr_screenshots.main([str(tmp_path), "--pull-request", "5", "--commit", "b" * 40]) == 0
    assert posted["number"] == 5 and f"{IMAGES}/home-phone.png?raw=true" in posted["body"]


@pytest.mark.parametrize("starter", [".github/workflow-starters/check-my-website.yml"])
def test_only_the_screenshots_job_may_write_and_it_runs_mains_helper(starter: str) -> None:
    """The jobs that run the pull request's code only read; the writing job runs main's helper."""
    text = Path(starter).read_text(encoding="utf-8")
    workflow = yaml.load(text, Loader=yaml.BaseLoader)
    jobs = workflow["jobs"]
    assert workflow["permissions"] == {"contents": "read"}
    assert "permissions" not in jobs["check"] and "permissions" not in jobs["ui"]
    shots = jobs["screenshots"]
    assert shots["permissions"] == {"contents": "write", "pull-requests": "write"}
    assert shots["needs"] == "ui" and shots["continue-on-error"] == "true"
    for condition in ("always()", "github.event_name == 'pull_request'",
                      "github.event.pull_request.head.repo.full_name == github.repository",
                      "needs.ui.outputs.results == 'ready'"):
        assert condition in shots["if"]
    checkout = shots["steps"][0]
    assert checkout["with"] == {"ref": "${{ github.event.pull_request.base.sha }}", "persist-credentials": "false"}
    assert shots["steps"][1]["with"] == {"name": "all-screenshots", "path": "ui-check"}
    assert "python3 scripts/pr_screenshots.py ui-check" in shots["steps"][2]["run"]
    for job in jobs.values():
        for step in job["steps"]:
            assert "${{" not in step.get("run", ""), "values reach scripts only through env"
    assert "secrets." not in text and "id-token" not in text
