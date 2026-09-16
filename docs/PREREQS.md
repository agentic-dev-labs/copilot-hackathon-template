# Customer access checklist

Complete and dry-run these items before Monday 26 October 2026.

All attendee exercises use browser-based Codespaces and its Linux/Bash terminal on all five days.
No local VS Code, PowerShell, Node, Python, Docker, browser extension, or Azure login is required.
The goal is AI enablement for business work: research, communication, planning, and small tools.
The presenter prepares advanced cloud-agent, managed-plugin, and automation examples separately.
Use the [coverage guide](REFERENCES.md) to see required labs versus optional demonstrations.
GitHub Copilot access does not automatically provide Microsoft 365 Copilot or Power Platform access.

The facilitator can run the [automated rehearsal](../rehearsal/README.md) in a dedicated Codespace
before delivery. Its network doctor checks artifact downloads and a fresh locked installation;
its deployment helper uses GitHub Actions, not attendee Azure sign-in.

- [ ] Collect attendee GitHub usernames: `[Confirm with facilitator]`.
- [ ] Confirm those accounts may join an external GitHub organization.
- [ ] Assign a GitHub Copilot seat to every attendee.
- [ ] Grant each learner or pair write access to their assigned, approved note-free repository.
- [ ] Keep repositories private/internal and labels unique; a pair has one project and rotates the driver.
- [ ] Confirm package/container endpoints are reachable from Codespaces, including public PyPI artifact hosts. Do not disable TLS checks.
- [ ] Confirm `github.com` is reachable from the corporate network.
- [ ] Confirm GitHub Codespaces is reachable and can create a container from the template.
- [ ] Confirm browser authentication flows for GitHub CLI and remote MCP are allowed.
- [ ] Confirm Copilot CLI sign-in separately from GitHub CLI sign-in; a preinstalled command is not an authenticated session.
- [ ] Rehearse the model picker, stop/review/recovery, and a simple CLI turn in browser-based Codespaces.
- [ ] Complete [.devcontainer setup](../.devcontainer/README.md): app lock, isolated document tools,
      locked Playwright MCP/browser, and a real headless launch. No tools are installed on the laptop.
- [ ] Let learners add/trust the two workspace MCP connections using Lab 01. Test actual browser
      navigation/download and MarkItDown conversion in that client, not only package installation.
- [ ] Check the [official report archive and prepared facts](RESEARCH.md). Use public-source
      material only; no login, visitor survey, confidential data, or CAPTCHA bypass.
- [ ] Verify the portable visual-brief skill and one approved community-skill task in Codespaces.
      Presenter-local skills, desktop file paths, and unsupported canvas extensions are not inherited.
- [ ] Verify skill/MCP discovery separately in VS Code Web and CLI; conversation and browser state do not transfer.
- [ ] Check CLI sandbox/local-network prerequisites in the exact Codespace. Successful
      package downloads do not prove agent access to localhost; do not bypass enforced policy.
- [ ] Assign team repositories and unique workshop labels/app names: `[Confirm with facilitator]`.
- [ ] Confirm attendees never need an Azure portal login; deployment runs entirely through the workflow.
- [ ] Rehearse private Ports previews and the **website** target, including localStorage at each
      origin, a fresh deployed commit, and no uploaded PDFs, source extracts, or private notes.
- [ ] Check capacity/cost for expected concurrent Codespace starts and builds; do not assume one
      successful rehearsal proves a 50-person start. Assign floor helpers and a labelled fallback.

## Days 3-5 Access

- [ ] Enable the cloud agent, review branch requirements, and rehearse one issue-to-PR task.
- [ ] Confirm automations are enabled for private/internal repositories and disable rehearsal triggers afterward.
- [ ] Permit the remote GitHub MCP server and test its read-only tools and browser authentication.
- [ ] Keep all work in Codespaces; corporate handover is planning, not a local-workstation exercise.

## Presenter-only capabilities

- [ ] Prepare a Space containing only synthetic training sources, a non-code summary/table/diagram, a reviewed PR, and a completed automation.
- [ ] Prepare a small public-source visual brief and a synthetic interactive site as labelled demonstrations.
- [ ] Review the full community skill folders, licences, dependencies, and permission needs; do not
      promise a dedicated presentation generator was found in Awesome Copilot. Use the prepared skill.
- [ ] Optional Day 5: demonstrate managed AttractionsAgent origin/version and actual invocation;
      missing private-source access is not a Day 1 blocker. Do not duplicate the specialist locally.
- [ ] Explain that Lab 08 deploys **site/**, while Day 2 uses the separate **vendor** target.
- [ ] Inspect the available model/Auto and usage controls. Do not pin the lesson to a particular model or promise identical reasoning options in every client.
- [ ] Test stop/steer/resume and checkpoint restoration on disposable changes. Keep a Git baseline for recovery.
- [ ] Keep specialist SDK/BYOK, other IDEs, integrations, and administration as reference-only unless separately rehearsed and approved.
- [ ] Keep labelled prepared results for blocked tools. Attendees add connections, not heavy runtime installations.
- [ ] Agree Power Platform environment and connector access with the guest presenter before Day 2.
- [ ] Agree work retention and access cleanup before the event; never delete a participant's personal GitHub account.

## Azure training target

These are the prepared training resource names, not a live health check. Verify them during rehearsal.

|                            |                                                          |
| -------------------------- | -------------------------------------------------------- |
| Subscription               | `ME-MngEnvMCAP566671-alfarahn-2`                         |
| Resource group             | `rg-nn-hackathon-2026-10` (East US)                      |
| Container Apps environment | `cae-hackathon` — all attendee apps share it             |
| Registry                   | `acrnnhackathon2026.azurecr.io`                          |
| Deploy identity            | `nn-hackathon-deploy`, Contributor on the resource group |

- [ ] Grant each generated repository access to the organization **Actions** secret `AZURE_CREDENTIALS`. New repositories only receive access when the secret's visibility policy includes them.
- [ ] Verify the deployment identity can build in the registry and create/update apps, and that Container Apps can pull the private image. Do not expose registry credentials to attendees.
- [ ] Use the approved administrator workflow to manage secrets; no credentials are created by `scripts/create_attendee_repos.py`.

## Dataverse training target

|                       |                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------- |
| Environment           | Hackathon Dataverse (Developer SKU)                                                     |
| `DATAVERSE_URL` value | `https://org0ef69385.crm.dynamics.com` (origin only)                                    |
| Web API               | `https://org0ef69385.crm.dynamics.com/api/data/v9.2`                                    |
| Tables                | `cr522_vendorreviews`, `cr522_controlfindings`                                          |
| Exercise grouping     | `cr522_attendee` filters by label; this is not row-level authorization                  |
| App identity          | `nn-hackathon-dataverse`; verify its application user and approved security role        |
| Seed data             | Three sample vendor rows per label; `controlfindings` is an unpopulated extension table |

- [ ] Supply `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`, `DATAVERSE_TENANT_ID`, and `DATAVERSE_CLIENT_SECRET` as **Codespaces** secrets for Lab 05. Names alone in a devcontainer do not provision values.
- [ ] Separately configure **Actions variables** `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`, `DATAVERSE_TENANT_ID`, plus the **Actions secret** `DATAVERSE_CLIENT_SECRET`. The deployment workflow does not read Codespaces secrets.
- [ ] Verify the application user and security role permit the required synthetic-table operations. A 403 can mean a missing application user or insufficient permissions.
- [ ] Provision with `python scripts/dataverse_provision.py` as the facilitator. It checks before creation and stops on permission errors; it does not repair arbitrary schema drift or rebuild tables.
- [ ] Set `DATAVERSE_APP_ID` and an explicit approved `DATAVERSE_ROLE` before running `scripts/dataverse_app_user.py`. The helper never assumes an administrator role.
- [ ] Seed with `python scripts/dataverse_seed.py` using each assigned label, then deploy the
      **vendor** target with **connect_dataverse** enabled and verify the page source before Day 2.
      The website target refuses Dataverse and must not receive these credentials.
- [ ] Keep access scoped to the synthetic training environment. A shared application identity and public demo URLs are not the design for real vendor material.

## Official References

- [Copilot getting started](https://docs.github.com/en/copilot/get-started), [administration](https://docs.github.com/en/copilot/how-tos/administer-copilot), and [client feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).
- [Codespaces](https://docs.github.com/en/codespaces/overview), [devcontainers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers), and [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces).
- [Built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools), [GitHub MCP setup](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server), and [enterprise-managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).
- [Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions) and [Container Apps deployment](https://learn.microsoft.com/azure/container-apps/github-actions).
- [Dataverse Web API](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api) and [Power Automate connectors](https://learn.microsoft.com/power-automate/dataverse/overview).
- [Whole-week coverage and extras](REFERENCES.md).
