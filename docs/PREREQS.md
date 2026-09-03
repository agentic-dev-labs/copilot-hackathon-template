# Customer access checklist

Complete and dry-run these items before Monday 26 October 2026.

- [ ] Collect attendee GitHub usernames: `[Confirm with facilitator]`.
- [ ] Confirm those accounts may join an external GitHub organization.
- [ ] Assign a GitHub Copilot seat to every attendee.
- [ ] Grant every attendee **write** access to the team repository; write access is required to trigger the cloud agent.
- [ ] Enable the Copilot cloud agent at organization level; it is off by default for Business and Enterprise organizations.
- [ ] Keep every team repository **private or internal**; Copilot automations are unavailable in public repositories.
- [ ] Confirm the organization allows Copilot automations as well as the cloud agent.
- [ ] Confirm the remote GitHub MCP server is permitted by any enterprise MCP allowlist.
- [ ] Add Copilot as a bypass actor for applicable branch protection or rulesets.
- [ ] Allowlist required corporate/internal package registries through the firewall.
- [ ] Confirm `github.com` is reachable from the corporate network.
- [ ] Confirm GitHub Codespaces is reachable and can create a container from the template.
- [ ] Confirm browser authentication flows for GitHub CLI and remote MCP are allowed.
- [ ] Assign ten team names and memberships: `[Confirm with facilitator]`.
- [ ] Confirm attendees never need an Azure portal login; deployment runs entirely through the workflow.

## Azure (provisioned)

| | |
|---|---|
| Subscription | `ME-MngEnvMCAP566671-alfarahn-2` |
| Resource group | `rg-nn-hackathon-2026-10` (East US) |
| Container Apps environment | `cae-hackathon` — all attendee apps share it |
| Registry | `acrnnhackathon2026.azurecr.io` |
| Deploy identity | `nn-hackathon-deploy`, Contributor on the resource group |

- [ ] Set `AZURE_CREDENTIALS` as an **organization** secret so repositories created from this template inherit it. Repository secrets are not copied by the template.
- [ ] `gh auth refresh -h github.com -s admin:org` is required before organization secrets can be set from the CLI.

## Dataverse (provisioned)

| | |
|---|---|
| Environment | Hackathon Dataverse (Developer SKU) |
| Web API | `https://org0ef69385.crm.dynamics.com/api/data/v9.2` |
| Tables | `cr522_vendorreviews`, `cr522_controlfindings` |
| Ownership | Rows carry `cr522_attendee`; each attendee filters by their own name |
| App identity | `nn-hackathon-dataverse`, added as a Dataverse application user with System Administrator |
| Seeded rows | Three, generated from the synthetic samples (scores 10, 8, 2) |

- [ ] Confirm each attendee identity can reach the Dataverse Web API. A 403 means the identity exists in Entra but is not a user in the Dataverse environment.
- [ ] Re-run `scripts/dataverse_provision.py` only if the tables need rebuilding; it is safe to re-run.
- [ ] Developer environments cap at 2 GB of database capacity, which is far beyond what synthetic data needs.
