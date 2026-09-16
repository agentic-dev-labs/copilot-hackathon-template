# Everyday AI With GitHub Copilot

Use AI to research, analyse, communicate, organise, automate, and build. This five-day workshop
starts with useful business-user outputs, then adds engineering depth. You do not need to be a
developer. Every activity follows **show -> try -> personalise -> verify -> share**.

**Day 1:** research public annual reports, discover a reusable skill, create a sourced HTML
presentation, and publish your own interactive website with browser storage. **Day 2:** work
with shared Dataverse data in the separately prepared synthetic vendor app. **Days 3-5:**
cloud agents, MCP, automations, hooks, custom agents, and evidence-based evaluations.

All attendee work uses **browser-based GitHub Codespaces and its Linux terminal**. Nothing
needs installing on your laptop. See the [agenda](docs/AGENDA.md) and
[topic map and official references](docs/REFERENCES.md).

## Start here

1. Select **Code > Codespaces > Create codespace on main**.
2. Wait for the container setup to finish.
3. Edit `config.json` and replace `Your Name` with your assigned, unique workshop label.
4. Open [Lab 00](labs/00-setup/README.md).

The label controls the page title, derived Container App name, and Dataverse display filter.
Repositories sharing a deployment environment need different derived app names. The filter is
not an identity or access boundary. The facilitator prepares service access; attendees do not
need to put secrets in code or sign in to the Azure portal.

Python, Node.js, GitHub CLI, Copilot CLI, browser automation, and document conversion all run
inside the Codespace. Open HTML using **Ports > Open in Browser**, not your laptop's localhost.
Private previews work while the Codespace and web server run; they are not deployments.

## What This Repository Provides

- A prepared environment and lab guidance, not a completed learner website.
- Nine labs, official references, tests, and a [rehearsal package](rehearsal/README.md).
- A ready-to-run vendor-review app for the separate Day 2 business case.
- [Optional travel practice](travel/README.md) for later agent/skill exploration.

[Awesome Copilot](https://awesome-copilot.github.com/) is a community collection to inspect,
adapt, and test, not an enterprise approval policy. The facilitator supplies a reviewed shortlist.
An MCP provides tools; a skill guides a task; you decide whether the result is useful and accurate.

## Rehearse the Complete Workshop

In a dedicated Codespaces rehearsal copy, run **`/rehearse-workshop`** in Copilot's local Agent
mode, or **`/workshop-rehearsal`** through the companion skill in Agent Host. The
[rehearsal package](rehearsal/README.md) drives completion of all nine labs, diagnoses fresh
package installs, runs tests, tracks live evidence, and retrieves verified deployment endpoints.
Attendees do not sign into Azure: the existing Actions workflow uses the prepared deployment identity.
Missing access or required human review stays a blocker, not a simulated pass.

## Run the app locally

```shell
uv sync --locked --extra dev --extra web
uv run uvicorn app.main:app --reload
```

With no Dataverse configured the app evaluates the synthetic samples directly, so it works in a
fresh Codespace with no credentials.

The devcontainer uses the checked-in `uv.lock`. Run `uv run pytest` and `uv run ruff check .`
from the repository root to check your work. Prepared headless Playwright MCP and MarkItDown MCP
run privately inside Codespaces. Built-in desktop browser tools are not an attendee prerequisite.

## Deploy it

Run **Deploy my app** from Actions. Select **website** on Day 1 and **vendor** for the separate
business app. The workflow uses the prepared Actions identity; no attendee Azure login is needed.
The run summary prints the verified URL and commit. Follow [Lab 08](labs/08-deploy/README.md)
before publishing. Only the intended site assets are published, not source reports or notes.

`localStorage` belongs to one browser context and origin. Your preview, deployed site, and
Playwright browser have separate data. A fresh URL showing an empty list is expected; repeat
the synthetic add/refresh check there. Browser storage is not a shared team database.

## Labs

Lab numbers group topics; the **Day** column is the order of the week.

| Lab                                       | Topic                                                 | Day |
| ----------------------------------------- | ----------------------------------------------------- | --- |
| [00](labs/00-setup/README.md)             | Codespace and access setup                            | 1   |
| [01](labs/01-vscode-agent/README.md)      | Research, source verification, skills, and visual briefs | 1 |
| [02](labs/02-copilot-cli/README.md)       | Your interactive website, storage, and browser checks    | 1 |
| [08](labs/08-deploy/README.md)            | Publish your own website                                | 1 |
| [05](labs/05-dataverse-app/README.md)     | Dataverse-backed application                          | 2   |
| [03](labs/03-cloud-agent/README.md)       | Copilot cloud agent                                   | 3   |
| [04](labs/04-mcp/README.md)               | Remote GitHub MCP server                              | 3   |
| [07](labs/07-automations-hooks/README.md) | Automations and hooks                                 | 4   |
| [06](labs/06-multi-agent/README.md)       | Deeper agent/skill authoring and evidence handoffs    | 5   |

See the [prerequisites](docs/PREREQS.md), [agenda](docs/AGENDA.md), and [facilitator runbook](docs/FACILITATOR.md).

Every lab ends with official references and optional tasks. Use the
[daily early-finisher list](docs/REFERENCES.md#small-tasks-for-early-finishers) while the group catches up.

## Sample reports

Three synthetic vendor reports are provided so you can compare outcomes from the same
checklist. All are fabricated and describe no real organization.

| Sample                                  | Outcome                                                    |
| --------------------------------------- | ---------------------------------------------------------- |
| `synthetic_soc2_harborline_congress.md` | Strong report, scores 10/10                                |
| `synthetic_soc2_report.md`              | Mixed report, 8/10 with one failure and one unclear result |
| `synthetic_soc2_meridian_outreach.md`   | Weak report, scores 2/10 despite strong encryption         |

They live in `src/vendor_assurance/samples/`. These outcomes use review date **2026-10-26**;
date-sensitive results change as reports age. Use a fixed date for repeatable demonstrations:

```bash
vendor-assurance src/vendor_assurance/samples/synthetic_soc2_report.md --as-of 2026-10-26 --output-directory reports/
```

The CLI writes JSON to stdout and the output path to stderr. Scores come from deterministic
Python, not the model. Evidence remains source text; the report renderer encodes table characters.

## Training scope

The evaluator recognizes ten controls in the supplied UTF-8 Markdown/text format using simple
rules. It is not a general SOC 2 assessor, an OCR pipeline, or a production compliance opinion.
Chunking uses whitespace-delimited words, not a model tokenizer; it helps demonstrate bounded
processing but does not guarantee complete evidence at every chunk size. Use synthetic data only.

The vendor starter reads rows. Attendees add a write form in Lab 05 and author customizations
in Labs 06 and 07. Day 1 public research is an explicit exception to the synthetic-only business
fixtures: download into ignored `research/`, verify facts, and publish original summaries only.
Never mix annual-report content into the vendor evaluator or confidential material into the lab.
Local tests do not prove live Codespaces, MCP, deployment, or Dataverse availability. Rehearse
the actual learner journey and keep prepared results visibly distinct from live observations.

## Official References

- [Copilot features](https://docs.github.com/en/copilot/get-started/features): the overall capability map.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): branch, commit, PR, review, and merge.
- [VS Code agents](https://code.visualstudio.com/docs/agents/overview): how context, models, tools, and sessions work together.
- [Workshop coverage and references](docs/REFERENCES.md): topic-by-topic official links, later-day practice, and optional extensions.
