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
- [ ] Test branch rules with the cloud agent; configure only the bypass access it needs.
- [ ] Confirm package/container endpoints are reachable from Codespaces, including public PyPI artifact hosts. Do not disable TLS checks.
- [ ] Confirm `github.com` is reachable from the corporate network.
- [ ] Confirm GitHub Codespaces is reachable and can create a container from the template.
- [ ] Confirm browser authentication flows for GitHub CLI and remote MCP are allowed.
- [ ] Verify Copilot built-in browser tools in the presenter client; attendees can follow the demo if their client does not expose them.
- [ ] Assign team repositories and unique workshop labels/app names: `[Confirm with facilitator]`.
- [ ] Confirm attendees never need an Azure portal login; deployment runs entirely through the workflow.

## Azure training target

These are the prepared training resource names, not a live health check. Verify them during rehearsal.

| | |
|---|---|
| Subscription | `ME-MngEnvMCAP566671-alfarahn-2` |
| Resource group | `rg-nn-hackathon-2026-10` (East US) |
| Container Apps environment | `cae-hackathon` — all attendee apps share it |
| Registry | `acrnnhackathon2026.azurecr.io` |
| Deploy identity | `nn-hackathon-deploy`, Contributor on the resource group |

- [ ] Grant each generated repository access to the organization **Actions** secret `AZURE_CREDENTIALS`. New repositories only receive access when the secret's visibility policy includes them.
- [ ] Verify the deployment identity can build in the registry and create/update apps, and that Container Apps can pull the private image. Do not expose registry credentials to attendees.
- [ ] Use the approved administrator workflow to manage secrets; no credentials are created by `scripts/create_attendee_repos.py`.

## Dataverse training target

| | |
|---|---|
| Environment | Hackathon Dataverse (Developer SKU) |
| `DATAVERSE_URL` value | `https://org0ef69385.crm.dynamics.com` (origin only) |
| Web API | `https://org0ef69385.crm.dynamics.com/api/data/v9.2` |
| Tables | `cr522_vendorreviews`, `cr522_controlfindings` |
| Exercise grouping | `cr522_attendee` filters by label; this is not row-level authorization |
| App identity | `nn-hackathon-dataverse`; verify its application user and approved security role |
| Seed data | Three sample vendor rows per label; `controlfindings` is an unpopulated extension table |

- [ ] Supply `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`, `DATAVERSE_TENANT_ID`, and `DATAVERSE_CLIENT_SECRET` as **Codespaces** secrets for Lab 05. Names alone in a devcontainer do not provision values.
- [ ] Separately configure **Actions variables** `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`, `DATAVERSE_TENANT_ID`, plus the **Actions secret** `DATAVERSE_CLIENT_SECRET`. The deployment workflow does not read Codespaces secrets.
- [ ] Verify the application user and security role permit the required synthetic-table operations. A 403 can mean a missing application user or insufficient permissions.
- [ ] Provision with `python scripts/dataverse_provision.py` as the facilitator. It checks before creation and stops on permission errors; it does not repair arbitrary schema drift or rebuild tables.
- [ ] Set `DATAVERSE_APP_ID` and an explicit approved `DATAVERSE_ROLE` before running `scripts/dataverse_app_user.py`. The helper never assumes an administrator role.
- [ ] Run `python scripts/dataverse_seed.py` using the assigned label, then deploy with **connect_dataverse** enabled and verify the page source.
- [ ] Keep access scoped to the synthetic training environment. A shared application identity and public demo URLs are not the design for real vendor material.
