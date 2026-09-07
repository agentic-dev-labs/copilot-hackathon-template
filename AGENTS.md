# AGENTS.md

Portable guidance for coding agents working in this repository. Copilot supports this file in
relevant clients alongside `.github/copilot-instructions.md`. Other agents have their own file
discovery rules; verify the client rather than assuming every agent reads the same files.

## What this is

A training repository for a hands-on GitHub Copilot workshop. It reviews **synthetic** third-party
vendor assurance reports: it chunks a report, scores ten controls, and renders a privacy review with
a direct quotation behind every finding.

## Non-negotiable rules

- **Synthetic data only.** Never write or invent real vendor, patient, customer or employee data.
  Every sample is fictional and must stay that way.
- **Quote, never paraphrase.** Every finding carries an exact sentence from the source document.
  A finding is `Unclear` when the report does not settle the question: with a quotation when the
  report explicitly acknowledges the gap, and with an empty quotation when it is simply silent.
  Never manufacture evidence to fill a gap.
- **The code decides the score, not the model.** Control status is calculated in
  `src/vendor_assurance/evaluator.py`. Explain the result; do not overrule it.
- **No secrets in code.** Read configuration from environment variables.

## Working in this repository

```bash
uv sync --locked --extra dev --extra web
uv run pytest
uv run ruff check .
uv run uvicorn app.main:app --reload
uv run vendor-assurance <report.md> --as-of 2026-10-26 --output-directory reports/
```

Tests and lint must both pass before opening a pull request.

Browser demos use Copilot's built-in browser tools where available. Do not install a separate
browser automation server. Keep private notes and service credentials out of commits and Docker
build contexts. A green offline suite is not a live Codespaces or Dataverse dry run.

## Layout

| Path | Purpose |
|---|---|
| `src/vendor_assurance/` | Chunker, evaluator, report writer, CLI |
| `src/vendor_assurance/samples/` | Synthetic SOC 2 reports |
| `app/` | The web application attendees deploy |
| `labs/` | Workshop instructions |
| `.github/agents/` | Custom agents |

## Style

Prefer clarity over cleverness; people are reading this to learn. Use type hints and short
docstrings. Prefer the standard library and well-known packages over exotic dependencies. Keep
everything runnable in a browser-based Codespace with no local installation.
