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
- [ ] Let attendees make their own copy at 09:30: in agentic-dev-labs **Settings > Member
      privileges**, allow members to create **private** repositories; flag the clean template as
      a **template** and make sure attendees can see it. Test **Use this template** with an
      attendee-like account: owner agentic-dev-labs, name = GitHub username, **Private**.
- [ ] Keep repositories private and names unique; a pair has one project (the driver's) and
      rotates the driver. Keep `scripts/create_attendee_repos.py` ready for anyone who cannot create one.
- [ ] Confirm package/container endpoints are reachable from Codespaces, including public PyPI artifact hosts. Do not disable TLS checks.
- [ ] Confirm `github.com` is reachable from the corporate network.
- [ ] Confirm GitHub Codespaces is reachable and can create a container from the template, and
      that the organization pays for Codespaces on its repositories, with a spending limit.
- [ ] Keep the [ready-made Codespace image](../.devcontainer/README.md#ready-made-image) public
      (**Actions > Codespace image** republishes it). In a fresh copy made with **Use this
      template**, check a Codespace is ready in about a minute, choose **Trust Folder & Continue**,
      and confirm the Website preview helper installs. Confirm concurrent capacity for 40-45 starts.
- [ ] Get the SEFR video file and the running times of the welcome and the ASTER Overview teaser
      (HZRW). They share 09:00-09:30 with the GitHub tour; test video playback and sound in the room.
- [ ] Confirm with David whether attendees are split across rooms MKC 1D412 and 1D413. If so,
      agree how the second room sees and hears the presenter, and who leads the helpers there.
- [ ] Complete the **core-only** [.devcontainer setup](../.devcontainer/README.md) in a fresh
      Codespace. CLI, Chromium, and document-conversion downloads must not be Monday startup gates.
- [ ] Rehearse `/create-website` in Agent Chat: it asks only which website (six starters or My own idea), then builds the tested blueprint, names it after the repository, and opens the preview. Check the starter's manual check yourself. Push it, run `/create-website` again, and confirm it builds an own idea in its own folder straight away.
- [ ] Verify the Website preview helper in a fresh Codespace: creation opens the panel beside Chat, edits appear by themselves, added entries survive an edit, stop closes the panel, and start reopens it. Copilot CLI sign-in stays separate before Day 3.
- [ ] Switch on [AI pictures and chat](FACILITATOR.md#ai-pictures-and-chat): the four `FOUNDRY_*`
      organization Codespaces secrets have repository access set to **Private repositories**
      (not selected ones), so copies made on Monday receive them. In a fresh attendee Codespace,
      `python3 scripts/workshop_ai.py status` reports `"ok": true`, one picture appears, and
      **Ask** answers once. Attendees never see a key or sign in to Azure.
- [ ] Confirm review rules and the first UI-based save/commit/push without bypassing protections.
      A website name in `config.json` is set only for optional publication (`/publish-website`).
- [ ] Confirm attendees never need an Azure portal login; deployment runs entirely through the workflow.
- [ ] Rehearse all four categories: add, drag and remove in each, switch the calendar views, add a Weather city on the corporate network, and confirm an emptied page reloads its own examples. Prepare optional **website** publication with `/publish-website` separately;
      no public URL or localStorage extension is needed to finish Monday.
- [ ] Check capacity/cost for expected concurrent Codespace starts and builds; do not assume one
      successful rehearsal proves a 40-45-person start. Confirm the final count, helpers, and a labelled fallback.
- [ ] Run the novice pilot in [FACILITATOR.md](FACILITATOR.md), compare the official orientation
      screenshots with the actual UI, and record time/help needed separately from test results.

## Before Tuesday

- [ ] Confirm David's 09:00-09:30 overview, Jackie's 09:30-10:30 conceptual Power Platform
      session, and Bill Leeson's 11:45-12:15 Building a Project Brain talk. Attendees are not asked
      to configure databases, connectors, or the internal marketplace.
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

Days 3-5 use each attendee's own repository and website. No vendor app, database, hook, or extra
repository is needed; an automation is a Day 4 presenter demo and an optional extra. See [the Day 3 guide](TOOLS-PRACTICE.md),
[the Day 4 guide](DAY-4-BUILD.md), and [the Day 5 guide](DAY-5-SHOWCASE.md).

- [ ] Confirm the training accounts may use Copilot CLI, custom agents, and skills, and preflight
      one attendee sign-in path privately. Never collect passwords or tokens. Installed is not authenticated.
- [ ] Verify CLI sandbox/local-network prerequisites; package downloads alone prove neither.
      Do not bypass policy. Browser and CLI sessions do not share chat, cookies, or saved entries.
- [ ] Enable the cloud agent for **every attendee repository** before Day 4, and rehearse one
      approved **Requirement** ticket assigned to Copilot through to a merged change. Note how long a session takes.
- [ ] Confirm organization members may create projects in agentic-dev-labs (Day 3 boards), and
      that `gh issue edit` in an attendee-style Codespace may update a ticket. Fallback: attendees
      paste the agent's draft into the ticket themselves.
- [ ] Keep **Copilot code review** switched off for attendees (decided 21 October 2026): Day 4
      uses each attendee's own Code Review agent, so nothing needs enabling for it.
- [ ] Set up the Day 4 presenter demo the day before: the criteria automation from Lab 03's
      extras on your demo repository. It runs as you and uses your allowance; switch it off afterwards.
- [ ] Push the publisher's `version` input and the fingerprint change to the template's `main`,
      then publish one practice website with `version:` switched on and check its footer before Day 4.
- [ ] Confirm attendees can push a file under `.github/workflows/` from their Codespace on a
      branch (Days 4-5) and can add themselves as a required reviewer of a `production` environment
      (Day 5). Fallback for the push: GitHub's web editor on a new branch. Never hand out personal tokens.
- [ ] Confirm Actions minutes for about 45 repositories running two checks (tests and the browser
      UI check, a few minutes each) and a feature-slot deploy on every pull request, and a publish
      on every release, on Day 5. Each attendee then has two websites (production and `-feature`),
      both sleeping when idle: about 90 apps, at most about 23 of the environment's 500
      consumption cores even if all are awake (checked 22 October 2026).
- [ ] Confirm the template CI's `ui-check` job is green on `main`: it proves the Day 5 browser
      install and screenshots on a real starter page.
- [ ] Agree Friday's room logistics for team demos: screen sharing, a timer, the running order, and the host.
- [ ] Optional extras only: the presenter's Lab 04 browser demonstration (VS Code Desktop, see
      the [Day 3 helper notes](FACILITATOR.md#day-3-helper-preparation); never use `--no-sandbox`),
      the remote GitHub MCP server in `.vscode/mcp.json` with no write tools, Lab 06 with the
      FOUNDRY_* secrets, the Day 4 automation extra, and the Day 5 Agentic Workflows demo.
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
| Container Apps environment | `cae-hackathon`, shared by all attendee websites          |
| Registry                   | `acrnnhackathon2026.azurecr.io`, no admin user           |
| Deploy identity            | `nn-hackathon-deploy`, least-privilege roles and GitHub OIDC trust |
| Website addresses          | `https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io` |

- [ ] The hosting is defined in [infra/website-hosting.bicep](../infra/website-hosting.bicep) and
      was deployed on 19 October 2026; [infra/README.md](../infra/README.md) explains its trust,
      listing, and teardown. Agree the teardown date with David.
- [ ] Attendee publishing needs **no secret**: in a fresh copy made with **Use this template**,
      run `/publish-website`, push, and check that **Actions > Publish my website** shows a live
      link. Keep push access to the template's `main` limited to the workshop owners, because
      Azure trusts that branch's publisher.
- [ ] Only the separate **Deploy my app** workflow (vendor app, rehearsals) uses the organization
      **Actions** secret `AZURE_CREDENTIALS`; grant it only where that workflow is used. No
      credentials are created by `scripts/create_attendee_repos.py`.

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
