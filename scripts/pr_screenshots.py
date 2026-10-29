"""Show the UI check's desktop and phone screenshots in a comment on the pull request.

The Screenshots job in check-my-website.yml runs this after the UI check, on the folder it filled:

    python3 scripts/pr_screenshots.py ui-check --pull-request 5 --commit <the pull request's commit>

It keeps the pictures on a branch called ui-screenshots, which holds nothing else, and posts one
comment with the result and the screenshots. It removes the comment from the run before, so the
newest pictures are always at the bottom of the conversation. It needs GITHUB_TOKEN with contents
and pull-requests write access, and uses only Python's standard library.
"""

import argparse
import base64
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote

MARKER = "<!-- ui-check -->"
BRANCH = "ui-screenshots"
SAFE_NAME = re.compile(r"^[A-Za-z0-9._-]+\.png$")
SCREEN_WIDTHS = {"desktop": 520, "phone": 200}
LONGEST_PROBLEM = 300


class ApiError(Exception):
    """GitHub answered with an error status."""

    def __init__(self, status: int, message: str) -> None:
        super().__init__(f"GitHub answered {status}: {message}")
        self.status = status


def api(method: str, path: str, body: object = None) -> object:
    """One GitHub REST call with the job's own token: JSON in, JSON out."""
    url = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/") + "/" + path
    request = urllib.request.Request(
        url, data=None if body is None else json.dumps(body).encode(), method=method,
        headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}", "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "workshop-pr-screenshots"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            text = response.read()
    except urllib.error.HTTPError as error:
        raise ApiError(error.code, error.read().decode("utf-8", errors="replace")[:200]) from None
    return json.loads(text) if text else None


def store_pictures(folder: Path, repository: str, place: str, attempts: int = 5) -> bool:
    """Commit the folder's screenshots to the ui-screenshots branch under place; True when stored."""
    pictures = sorted(path for path in folder.glob("*.png") if SAFE_NAME.match(path.name))
    if not pictures:
        return False
    try:
        tree = []
        for picture in pictures:
            blob = api("POST", f"repos/{repository}/git/blobs",
                       {"content": base64.b64encode(picture.read_bytes()).decode(), "encoding": "base64"})
            tree.append({"path": f"{place}/{picture.name}", "mode": "100644", "type": "blob", "sha": blob["sha"]})
        for attempt in range(attempts):
            try:
                try:
                    parent = api("GET", f"repos/{repository}/git/ref/heads/{BRANCH}")["object"]["sha"]
                except ApiError as missing:
                    if missing.status != 404:
                        raise
                    parent = None
                request = {"tree": tree}
                if parent:
                    request["base_tree"] = api("GET", f"repos/{repository}/git/commits/{parent}")["tree"]["sha"]
                tree_sha = api("POST", f"repos/{repository}/git/trees", request)["sha"]
                commit = api("POST", f"repos/{repository}/git/commits", {
                    "message": f"Screenshots {place}", "tree": tree_sha, "parents": [parent] if parent else []})["sha"]
                if parent:
                    api("PATCH", f"repos/{repository}/git/refs/heads/{BRANCH}", {"sha": commit, "force": False})
                else:
                    api("POST", f"repos/{repository}/git/refs", {"ref": f"refs/heads/{BRANCH}", "sha": commit})
                return True
            except ApiError as error:
                # Another pull request's run moved the branch at the same moment: add on top of it.
                if error.status not in (409, 422) or attempt == attempts - 1:
                    raise
                time.sleep(2 * (attempt + 1))
    except ApiError as error:
        print(f"::warning::The screenshots could not be stored: {error}")
    return False


def _label(page: str) -> str:
    """The plain name of a checked page."""
    return "Your first page" if page == "home" else f"Idea page {page.removeprefix('idea-')}"


def _short(text: str) -> str:
    """One line that cannot break the comment's layout."""
    flat = " ".join(str(text).split()).replace("|", "/").replace("<", "&lt;")
    return flat if len(flat) <= LONGEST_PROBLEM else flat[: LONGEST_PROBLEM - 3] + "..."


def comment_markdown(results: list[dict], images: str, commit: str = "", run_url: str = "") -> str:
    """The comment: how many screens passed, what to look at, and each page on a desktop and a phone."""
    passed = sum(not result["problems"] for result in results)
    intro = "GitHub opened your pages in a browser on a desktop and a phone screen"
    intro += f", for commit `{commit[:7]}`." if commit else "."
    if run_url:
        intro += f" [Open the run]({run_url}) for its log."
    lines = [MARKER, f"### UI check: {passed} of {len(results)} screens passed", "", intro, ""]
    problems = [f"- **{_label(result['page'])}, {result['screen']}:** {_short(problem)}"
                for result in results for problem in result["problems"]]
    if problems:
        lines += ["**What to look at**", "", *problems, ""]
    if not images:
        lines += ["The pictures could not be stored this time: open the run and look under **Artifacts**.", ""]
    for index, page in enumerate(dict.fromkeys(result["page"] for result in results)):
        shots = {result["screen"]: result for result in results if result["page"] == page}
        state = "Pass" if not any(result["problems"] for result in shots.values()) else "Fail"
        cells = []
        for screen, width in SCREEN_WIDTHS.items():
            shot = shots.get(screen, {}).get("screenshot", "")
            if images and SAFE_NAME.match(shot):
                alt = html.escape(f"{_label(page)} on a {screen}")
                cells.append(f'<img src="{images}/{quote(shot)}?raw=true" width="{width}" alt="{alt}">')
            else:
                cells.append("No screenshot")
        table = ["| Desktop | Phone |", "| --- | --- |", f"| {cells[0]} | {cells[1]} |"]
        if index == 0:
            lines += [f"**{_label(page)}: {state}**", "", *table, ""]
        else:
            lines += ["<details>", f"<summary>{_label(page)}: {state}</summary>", "", *table, "", "</details>", ""]
    lines.append("Every new commit runs the check again; the newest screenshots are in the last comment like this.")
    return "\n".join(lines) + "\n"


def post_comment(repository: str, pull_request: int, body: str) -> int:
    """Post the new comment, then remove the ones earlier runs left; return the new comment's id."""
    new = api("POST", f"repos/{repository}/issues/{pull_request}/comments", {"body": body})["id"]
    old = []
    page = 1
    while True:
        comments = api("GET", f"repos/{repository}/issues/{pull_request}/comments?per_page=100&page={page}")
        old += [comment["id"] for comment in comments if comment["id"] != new
                and comment["user"]["login"] == "github-actions[bot]" and comment["body"].startswith(MARKER)]
        if len(comments) < 100:
            break
        page += 1
    for comment in old:
        api("DELETE", f"repos/{repository}/issues/comments/{comment}")
    return new


def main(arguments: list[str] | None = None) -> int:
    """Store the screenshots and comment on the pull request."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("folder", help="The UI check's folder, with results.json and the screenshots")
    parser.add_argument("--pull-request", type=int, required=True, help="The pull request's number")
    parser.add_argument("--commit", default="", help="The pull request's commit")
    options = parser.parse_args(arguments)
    folder = Path(options.folder)
    results = json.loads((folder / "results.json").read_text(encoding="utf-8"))
    repository = os.environ["GITHUB_REPOSITORY"]
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    run = os.environ.get("GITHUB_RUN_ID", "local")
    place = f"pr-{options.pull_request}/run-{run}"
    images = f"{server}/{repository}/blob/{BRANCH}/{place}" if store_pictures(folder, repository, place) else ""
    body = comment_markdown(results, images, options.commit, f"{server}/{repository}/actions/runs/{run}")
    post_comment(repository, options.pull_request, body)
    print(f"Posted the screenshots on pull request #{options.pull_request}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
