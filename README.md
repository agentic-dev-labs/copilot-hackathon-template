# GitHub Copilot Vendor Assurance Hackathon

This private template supports a five-day, browser-first GitHub Copilot hackathon. Line-of-business teams, low-coders, and professional developers build a synthetic third-party vendor privacy review workflow without putting customer, patient, or real vendor data in source control.

## Start here

1. Select **Code > Codespaces > Create codespace on main**.
2. Wait for the container setup to finish.
3. Open [Lab 00](labs/00-setup/README.md).

Only a browser is required on the attendee laptop. Python, Node.js, Azure CLI, GitHub CLI, and project dependencies run in the Codespace.

## Labs

| Lab | Topic |
|---|---|
| [00](labs/00-setup/README.md) | Codespace and access setup |
| [01](labs/01-vscode-agent/README.md) | VS Code agent mode and repository instructions |
| [02](labs/02-copilot-cli/README.md) | Copilot CLI and delegation |
| [03](labs/03-cloud-agent/README.md) | Copilot cloud agent |
| [04](labs/04-mcp/README.md) | Remote GitHub MCP server |
| [05](labs/05-dataverse-app/README.md) | Dataverse-backed application |
| [06](labs/06-multi-agent/README.md) | Multi-agent workflows |
| [07](labs/07-automations-hooks/README.md) | Automations and hooks |

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
