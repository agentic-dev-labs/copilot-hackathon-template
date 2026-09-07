# GitHub Copilot Workshop and Hackathon

This template supports five days of demonstrations, guided labs, and team building. Line-of-business
teams, low-coders, and professional developers extend a synthetic vendor review app and learn to
create their own Copilot instructions, prompts, agents, skills, and hooks.

## Start here

1. Select **Code > Codespaces > Create codespace on main**.
2. Wait for the container setup to finish.
3. Edit `config.json` and replace `Your Name` with your assigned, unique workshop label.
4. Open [Lab 00](labs/00-setup/README.md).

The label controls the page title, derived Container App name, and Dataverse display filter.
Repositories sharing a deployment environment need different derived app names. The filter is
not an identity or access boundary. The facilitator prepares service access; attendees do not
need to put secrets in code or sign in to the Azure portal.

Only a browser is required on the attendee laptop. Python, Node.js, Azure CLI, GitHub CLI, and project dependencies run in the Codespace.

## Run the app locally

```shell
uv sync --locked --extra dev --extra web
uv run uvicorn app.main:app --reload
```

With no Dataverse configured the app evaluates the synthetic samples directly, so it works in a
fresh Codespace with no credentials.

The devcontainer uses the checked-in `uv.lock`. Run `uv run pytest` and `uv run ruff check .`
from the repository root to check your work. Browser demonstrations use Copilot's **built-in
browser tools** where the presenter client supports them. No additional browser server is installed.

## Deploy it

Run the **Deploy my app** workflow from the Actions tab. It reads `config.json`, derives a valid
Container App name, builds the image, and deploys to the shared environment. The run summary
prints your public URL. Leave **connect_dataverse** unchecked on Day 1. Lab 05 explains how to
enable it after the facilitator has configured the separate Actions variables and secrets.

## Labs

Lab numbers group topics; the **Day** column is the order of the week.

| Lab | Topic | Day |
|---|---|---|
| [00](labs/00-setup/README.md) | Codespace and access setup | 1 |
| [01](labs/01-vscode-agent/README.md) | VS Code agent mode | 1 |
| [02](labs/02-copilot-cli/README.md) | Copilot CLI and delegation | 1 |
| [08](labs/08-deploy/README.md) | **Name it and ship it** | 1 |
| [05](labs/05-dataverse-app/README.md) | Dataverse-backed application | 2 |
| [03](labs/03-cloud-agent/README.md) | Copilot cloud agent | 3 |
| [04](labs/04-mcp/README.md) | Remote GitHub MCP server | 3 |
| [07](labs/07-automations-hooks/README.md) | Automations and hooks | 4 |
| [06](labs/06-multi-agent/README.md) | Author an agent and a skill, then hand off work | 5 |

See the [prerequisites](docs/PREREQS.md), [agenda](docs/AGENDA.md), and [facilitator runbook](docs/FACILITATOR.md).

## Sample reports

Three synthetic vendor reports are provided so you can compare outcomes from the same
checklist. All are fabricated and describe no real organization.

| Sample | Outcome |
|---|---|
| `synthetic_soc2_harborline_congress.md` | Strong report, scores 10/10 |
| `synthetic_soc2_report.md` | Mixed report, 8/10 with one failure and one unclear result |
| `synthetic_soc2_meridian_outreach.md` | Weak report, scores 2/10 despite strong encryption |

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

The starter app reads rows. Attendees add the write form in Lab 05 and create customization files
in Labs 01, 06, and 07. Local unit tests mock external services; a green run does not prove live
Codespaces, deployment, Dataverse, cloud-agent, or plugin availability. Use the facilitator's
dry-run checklist before delivery.
