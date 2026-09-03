# GitHub Copilot Vendor Assurance Hackathon

This private template supports a five-day, browser-first GitHub Copilot hackathon. Line-of-business teams, low-coders, and professional developers build a synthetic third-party vendor privacy review workflow without putting customer, patient, or real vendor data in source control.

## Start here

1. Select **Code > Codespaces > Create codespace on main**.
2. Wait for the container setup to finish.
3. Edit `config.json` and replace `Your Name` with your own name.
4. Open [Lab 00](labs/00-setup/README.md).

Your name in `config.json` is the only thing you configure. It becomes the title of your app,
the name of your Container App, and the filter for your rows in Dataverse. You never handle a
secret and never open the Azure portal.

Only a browser is required on the attendee laptop. Python, Node.js, Azure CLI, GitHub CLI, and project dependencies run in the Codespace.

## Run the app locally

```shell
uv sync --extra dev --extra web
uvicorn app.main:app --reload
```

With no Dataverse configured the app evaluates the synthetic samples directly, so it works in a
fresh Codespace with no credentials.

## Deploy it

Run the **Deploy my app** workflow from the Actions tab. It reads `config.json`, derives a valid
Container App name, builds the image, and deploys to the shared environment. The run summary
prints your public URL.

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
| [06](labs/06-multi-agent/README.md) | Multi-agent workflows | 5 |

See the [prerequisites](docs/PREREQS.md), [agenda](docs/AGENDA.md), and [facilitator runbook](docs/FACILITATOR.md).

## Sample reports

Three synthetic vendor reports are provided so you can compare outcomes from the same
checklist. All are fabricated and describe no real organization.

| Sample | Outcome |
|---|---|
| `synthetic_soc2_harborline_congress.md` | Strong report, scores 10/10 |
| `synthetic_soc2_report.md` | Mixed report with one failure and one unclear result |
| `synthetic_soc2_meridian_outreach.md` | Weak report, scores 2/10 despite strong encryption |

They live in `src/vendor_assurance/samples/`.
