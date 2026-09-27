# Customer access checklist

Complete and dry-run these items before Monday 26 October 2026.

All attendee exercises use browser-based Codespaces and its Linux/Bash terminal on all five days.
No local VS Code, PowerShell, Node, Python, Docker, browser extension, or Azure login is required.
The beginner goal is to describe, build, check, and save a small website. Research, presentations,
and additional integrations remain optional extensions, not first-day prerequisites.
The presenter prepares advanced cloud-agent, managed-plugin, and automation examples separately.
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
- [ ] Complete the **core-only** [.devcontainer setup](../.devcontainer/README.md) in a fresh
      Codespace. CLI, Chromium, and document-conversion downloads must not be Monday startup gates.
- [ ] Rehearse `/create-website` in Agent Chat: it asks only which of the four websites, then builds the tested blueprint, names it after the repository, and opens the preview. Check the starter's manual check yourself.
- [ ] Verify the Website preview helper in a fresh Codespace: creation opens the panel beside Chat, edits appear by themselves, added entries survive an edit, stop closes the panel, and start reopens it. Copilot CLI sign-in stays separate before Day 3.
- [ ] Assign repositories, working branches, and unique labels in `config.json` before class.
      Confirm review rules and the first UI-based save/commit/push without bypassing protections.
- [ ] Confirm attendees never need an Azure portal login; deployment runs entirely through the workflow.
- [ ] Rehearse all four categories: add, drag and remove in each, switch the calendar views, add a Weather city on the corporate network, and **Start again with the examples**. Prepare optional assisted **website** publication separately;
      no public URL or localStorage extension is needed to finish Monday.
- [ ] Check capacity/cost for expected concurrent Codespace starts and builds; do not assume one
      successful rehearsal proves a 40-45-person start. Confirm the final count, helpers, and a labelled fallback.
- [ ] Run the novice pilot in [FACILITATOR.md](FACILITATOR.md), compare the official orientation
      screenshots with the actual UI, and record time/help needed separately from test results.

## Before Tuesday

- [ ] Confirm David's 09:00-09:30 overview and Jackie's 09:30-10:30 conceptual Power Platform
      session. Attendees are not asked to configure databases, connectors, or the internal marketplace.
- [ ] Collect brief ideas with examples and an explicit "no idea yet" option. Request no real records
      or private spreadsheets. Prepare suitable approved repositories or reuse the Monday project.
- [ ] Rehearse [own-idea building](DAY-2-BUILD.md), manual checks, save/push, and handover questions.
      No live Dataverse, mandatory CLI/MCP session, or public deployment is required to finish.
- [ ] Print [the quick reference](QUICK-REFERENCE.md), confirm table power/screen visibility,
      and agree helper coverage. Use selected volunteers rather than a full-room round-robin.
- [ ] Resolve the reported 09:00-16:00 invitation versus this repository's 09:00-15:00 schedule
      with the organisers; do not silently change hours or book meetings.
- [ ] Keep Codespaces-only work. A corporate environment transition requires separate approval,
      verified access, and saved work. Do not remove training membership needed for later sessions.

## Days 3-5 Access

- [ ] Complete `bash .devcontainer/setup.sh cli` and `bash .devcontainer/setup.sh browser` in the
      intended Codespaces before Day 3. Do not install research tools just to use Playwright.
- [ ] Preflight Copilot CLI sign-in separately from editor/GitHub CLI sign-in with each learner's
      approved identity. Never collect passwords or tokens. Installed is not authenticated.
- [ ] Prepare the workspace Playwright connection, then test trust/discovery and an actual call
      in VS Code Web. Follow the existing demonstration blocks in [tools practice](TOOLS-PRACTICE.md).
- [ ] Verify CLI sandbox/local-network prerequisites; package downloads alone prove neither.
      Do not bypass policy. Browser and CLI sessions do not share chat, cookies, or saved entries.
- [ ] Enable the cloud agent, review branch requirements, and rehearse one issue-to-PR task.
- [ ] Confirm automations are enabled for private/internal repositories and disable rehearsal triggers afterward.
- [ ] Permit the remote GitHub MCP server and test its read-only tools and browser authentication.
- [ ] Keep all work in Codespaces; corporate handover is planning, not a local-workstation exercise.
- [ ] Prepare the local-sample vendor reader for technical attendees without a personal site.
      Dataverse credentials and a completed former Lab 05 are not required.
- [ ] Verify the selected everyday-work skill's complete files, licence, Linux dependencies, and
      actual invocation before Friday. Presenter-local skills do not transfer to learners.
- [ ] Run a saved browser assertion check and verify release evidence for Day 4. Do not claim a
      browser CI check unless the workflow actually invokes it.

## Optional Examples

- [ ] Prepare a Space containing only synthetic training sources, a non-code summary/table/diagram, a reviewed PR, and a completed automation.
- [ ] Prepare a small public-source visual brief and a synthetic interactive site as labelled demonstrations.
- [ ] Review the full community skill folders, licences, dependencies, and permission needs; do not
      promise a dedicated presentation generator was found in Awesome Copilot. Use the prepared skill.
- [ ] Optional Day 5: demonstrate managed AttractionsAgent origin/version and actual invocation;
      missing private-source access is not a Day 1 blocker. Do not duplicate the specialist locally.
- [ ] Explain that optional Lab 08 publication deploys **site/**. The technical track can instead
      release the separate **vendor** reader with local samples and **connect_dataverse** unchecked.
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
