# Customer access checklist

Complete and dry-run these items before Monday 26 October 2026.

All attendee exercises use browser-based Codespaces and its Linux/Bash terminal on all five days.
No local VS Code, PowerShell, Node, Python, Docker, browser extension, or Azure login is required.
The beginner goal is to describe, build, check, and save a small website. Research, presentations,
and additional integrations remain optional extensions, not first-day prerequisites.
The presenter prepares the cloud-agent demonstration separately. Deeper technical topics are
[post-workshop reference](../post-workshop/advanced/README.md), not workshop prerequisites.
Use the [coverage guide](REFERENCES.md) to see required labs versus optional demonstrations.
GitHub Copilot access does not automatically provide Microsoft 365 Copilot or Power Platform access.

The facilitator can run the [automated rehearsal](../rehearsal/README.md) in a dedicated Codespace
before delivery. Its network doctor checks artifact downloads and a fresh locked installation;
its deployment helper uses GitHub Actions, not attendee Azure sign-in.

- [ ] Collect final attendee GitHub usernames and coordinate approved invitations in the week
      before the event. Use a small approved pilot group for earlier testing; no bulk invite is implied here.
- [ ] Confirm those accounts may join an external GitHub organization.
- [ ] Assign a GitHub Copilot seat to every attendee.
- [ ] Grant each learner or pair write access to their assigned, approved note-free repository.
- [ ] Keep repositories private/internal and labels unique; a pair has one project and rotates the driver.
- [ ] Confirm package/container endpoints are reachable from Codespaces, including public PyPI artifact hosts. Do not disable TLS checks.
- [ ] Confirm `github.com` is reachable from the corporate network.
- [ ] Confirm GitHub Codespaces is reachable and can create a container from the template.
- [ ] Enable Codespaces prebuilds for the attendee repositories, or ask attendees to create their
      Codespace before 09:00 on Monday, so 40-45 first creations do not consume Lab 00.
- [ ] Complete the **core-only** [.devcontainer setup](../.devcontainer/README.md) in a fresh
      Codespace. CLI, Chromium, and document-conversion downloads must not be Monday startup gates.
- [ ] Rehearse `/create-website` in Agent Chat: it asks only which of the four websites, then builds the tested blueprint, names it after the repository, and opens the preview. Check the starter's manual check yourself.
- [ ] Verify the Website preview helper in a fresh Codespace: creation opens the panel beside Chat, edits appear by themselves, added entries survive an edit, stop closes the panel, and start reopens it. Copilot CLI sign-in stays separate before Day 3.
- [ ] Assign repositories, working branches, and unique labels in `config.json` before class.
      Confirm review rules and the first UI-based save/commit/push without bypassing protections.
- [ ] Confirm attendees never need an Azure portal login; deployment runs entirely through the workflow.
- [ ] Rehearse all four categories: add, drag and remove in each, switch the calendar views, add a Weather city on the corporate network, and confirm an emptied page reloads its own examples. Prepare optional assisted **website** publication separately;
      no public URL or localStorage extension is needed to finish Monday.
- [ ] Check capacity/cost for expected concurrent Codespace starts and builds; do not assume one
      successful rehearsal proves a 40-45-person start. Confirm the final count, helpers, and a labelled fallback.
- [ ] Run the novice pilot in [FACILITATOR.md](FACILITATOR.md), compare the official orientation
      screenshots with the actual UI, and record time/help needed separately from test results.

## Before Tuesday

- [ ] Confirm David's 09:00-09:30 overview and Jackie's 09:30-10:30 conceptual Power Platform
      session. Attendees are not asked to configure databases, connectors, or the internal marketplace.
- [ ] Collect brief ideas with examples and an explicit "no idea yet" option. Request no real records
      or private spreadsheets. Own ideas use `/create-website` in `site/ideas/` of the same repository.
- [ ] Rehearse [own-idea building](DAY-2-BUILD.md), manual checks, save/push, and handover questions.
      No live Dataverse, mandatory CLI/MCP session, or public deployment is required to finish.
- [ ] Print [the quick reference](QUICK-REFERENCE.md), confirm table power/screen visibility,
      and agree helper coverage. Use selected volunteers rather than a full-room round-robin.
- [ ] Resolve the reported 09:00-16:00 invitation versus this repository's 09:00-15:00 schedule
      with the organisers; do not silently change hours or book meetings.
- [ ] Keep Codespaces-only work. A corporate environment transition requires separate approval,
      verified access, and saved work. Do not remove training membership needed for later sessions.

## Days 3-5 Access

Days 3-5 use each attendee's own repository and website. No vendor app, database, automation,
hook, or extra repository is needed. See [the Day 3 guide](TOOLS-PRACTICE.md).

- [ ] Confirm the training accounts may use Copilot CLI, and preflight one attendee sign-in path
      privately. Never collect passwords or tokens. Installed is not authenticated.
- [ ] Rehearse the presenter's Lab 04 browser demonstration with VS Code's built-in browser tools
      from VS Code Desktop connected to the presenter's Codespace; the integrated browser is a
      desktop feature. Attendees install nothing for it. The Playwright browser
      profile could not start Chromium's sandbox in a default Codespace on 14 October 2026; see
      the [Day 3 helper notes](TOOLS-PRACTICE.md#helper-preparation) and never use `--no-sandbox`.
- [ ] Verify CLI sandbox/local-network prerequisites; package downloads alone prove neither.
      Do not bypass policy. Browser and CLI sessions do not share chat, cookies, or saved entries.
- [ ] Permit the remote GitHub MCP server. Attendee repositories ship it in `.vscode/mcp.json`
      (`https://api.githubcopilot.com/mcp/readonly`) as their only MCP server; test its sign-in and
      that no write tools appear.
- [ ] Enable the cloud agent for the presenter's demonstration repository and rehearse one
      issue-to-merged-change run. Enable it for attendee repositories only if the optional Day 4 try is offered.
- [ ] Rehearse Lab 06: an instructions file applied to `site/` and a small learner-written skill
      discovered through its slash command.
- [ ] Agree Friday's room logistics: screen sharing, a timer, the running order, and the host.
- [ ] Keep all work in Codespaces; corporate handover is planning, not a local-workstation exercise.

## Optional Examples

- [ ] Prepare a Space containing only synthetic training sources, a non-code summary/table/diagram, and a reviewed PR.
- [ ] Prepare a small public-source visual brief and a synthetic interactive site as labelled demonstrations.
- [ ] Review the full community skill folders, licences, dependencies, and permission needs; do not
      promise a dedicated presentation generator was found in Awesome Copilot. Use the prepared skill.
- [ ] Optional later: demonstrate managed AttractionsAgent origin/version and actual invocation;
      missing private-source access is not a workshop blocker. Do not duplicate the specialist locally.
- [ ] Explain that optional Lab 08 publication deploys **site/**. The separate **vendor** reader is a
      post-workshop example; release it only with local samples and **connect_dataverse** unchecked.
- [ ] Inspect the available model/Auto and usage controls. Do not pin the lesson to a particular model or promise identical reasoning options in every client.
- [ ] Test stop/steer/resume and checkpoint restoration on disposable changes. Keep a Git baseline for recovery.
- [ ] Keep specialist SDK/BYOK, other IDEs, integrations, and administration as reference-only unless separately rehearsed and approved.
- [ ] Keep labelled prepared results for blocked tools. Attendees add connections, not heavy runtime installations.
- [ ] Only for the optional research extension, prepare `bash .devcontainer/setup.sh research`,
      verify MarkItDown, inspect the [public archive and prepared facts](RESEARCH.md), and test
      visual-brief without replacing an existing site. No PDF archive or presentation is a Monday gate.
- [ ] Any Power Platform demonstration access belongs to the guest presenter, not attendee setup.
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

## Post-Workshop Dataverse Work

The former training target, configuration knowledge, schema/identity/seed scripts, verification,
and reusable prompts now live in [the preserved technical reference](../post-workshop/dataverse/README.md).
Do not provision them as a prerequisite for this workshop. Any later session needs explicit
technical-owner approval and a separate non-production target before real-work adoption.

## Official References

- [Copilot getting started](https://docs.github.com/en/copilot/get-started), [administration](https://docs.github.com/en/copilot/how-tos/administer-copilot), and [client feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix).
- [Codespaces](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces), [devcontainers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers), and [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces).
- [Built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools), [GitHub MCP setup](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server), and [enterprise-managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).
- [Actions secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) and [Container Apps deployment](https://learn.microsoft.com/azure/container-apps/github-actions).
- [Dataverse Web API](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api) and [Power Automate connectors](https://learn.microsoft.com/power-automate/dataverse/overview).
- [Whole-week coverage and extras](REFERENCES.md).
