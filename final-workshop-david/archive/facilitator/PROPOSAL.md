# Proposal: what is left before the Novo Nordisk Copilot week

**Superseded on 22 October 2026.** For the overview and timings, always look in
`final-workshop-david/`: `WEEK.md` and `DELIVERY.md`. This note keeps only its decisions and
live-test evidence.

Prepared 19 October 2026 for Ali Farahnak. Private facilitator note (git-ignored). Workshop days:
Monday 26 to Friday 30 October 2026. Sources: this repository, David's five agenda slides
(now `final-workshop-david/1.png`-`5.png`), and live tests run today.

## 1. Where we are

| Area | Status | Evidence |
| --- | --- | --- |
| Day 1 starters (Planner, Calendar, Ideas Wall, Weather 3D, Princeton Map, Photo Studio, own idea), `/add-chat`, `/add-chart` | Done, tested in a real Codespace | Builds take 46-53 s; own idea 1 min 43 s; chat answer 2.7 s; photo edit 25 s |
| Fast Codespaces (prebuilt public image) | Done | Editor ready in about 14 s |
| **Automatic website publishing** | **Done today, tested live** | Push to live in about 2 minutes, with no secret anywhere |
| Day 2 | Needs Bill Leeson's slot | See section 3 |
| Days 3-5 | Repository follows the old plan; David's slides differ completely | See section 3 |

### The new publishing, in one paragraph

An attendee types `/publish-website`, accepts a name such as `ali-planner`, and pushes. GitHub
Actions then puts `site/` on `https://ali-planner.thankfulrock-bf005377.eastus.azurecontainerapps.io`,
checks that exact commit is live, and shows the link under **Deployments** on the repository page.
Every later push updates it. Azure trusts only the template's own publisher on `main`, through
GitHub's signed token (OIDC) and a flexible federated credential. There is no
`AZURE_CREDENTIALS` secret, no attendee Azure login, and an attendee cannot overwrite another
attendee's website (each site is tagged with its repository ID). Details: `infra/README.md`.

Live tests, 19 October, in two private test repositories (all passed):

| Test | Result |
| --- | --- |
| First publish of the Day 1 Planner | Live and verified; link shown under **Deployments** |
| Update an existing website | Push to verified live in about 1.5-2 minutes |
| Another repository claims a used name | Refused before upload: "already used by another repository" |
| Rename the website | New address live; the old one removed automatically |
| Re-run a failed run | Re-published from the stored site files |
| Push with no name yet (every Day 1 push) | Green run, "Not published yet", nothing deployed |
| The template itself | Skipped |
| Signed-in identity | Subject `repo:agentic-dev-labs@323143564/<repo>@<id>:ref:refs/heads/main`, from the template's publisher only |

Typical publish job: check 5 s, build and check the image 7-14 s, OIDC sign-in 3 s, upload 7 s,
create or update 16-19 s, verify the exact commit live 30-40 s.

**Cold start:** a sleeping website took 33 s to answer the first visit; warm visits take 0.6 s.
Almost all of it is Azure finding a node (the 45 MB image pulls in 3 s), so a smaller image would
not help. One line (`MIN_REPLICAS: 1` in the publisher) keeps websites awake; see decision 5.

**Attendee flow in a real Codespace (19 October, 19:26-20:18):** Codespace ready and trusted in
about 1 minute. `/publish-website` asked one question, changed one line of `config.json`, and
handed over the three lines. Source Control **+**, sparkle message, Commit, **... > Push** worked
as Lab 08 says. Push to verified live took 1 min 49 s, and the published Planner showed its example
entries, 3D chart and **Ask** button. "Is my website live yet?" ran `curl /healthz` and
`git rev-parse HEAD` and answered correctly. Two fixes came out of it and are pushed: the skill now
says **... > Push** like every guide (it said Sync Changes), and it suggests a name from
`$GITHUB_USER` (re-tested: `alfarahn-planner`) because `gh api user` fails in a Codespace, and keeps
an existing name instead of silently moving the site. Things attendees will meet:

- One **Allow** prompt when Copilot checks whether the site is live (it fetches `/healthz`).
- The sparkle button did nothing until Copilot finished signing in, about a minute after start.
- Ruff's "No Python environment extension" notification on start (known extension-install race).
- The chat's "1 workspace customization needs an update" migrations banner.
- Credits: `/publish-website` used 9.8 credits and the follow-up 6.5 on GPT-6.1 Sol (the model in
  Ali's synced settings). Each request carried about 45k input tokens, mostly the always-loaded
  `AGENTS.md` and `.github/copilot-instructions.md`, which both load. See decision 9.

All test websites, images and the test Codespace were deleted afterwards; only the shared hosting
remains.

Azure resources (subscription `ME-MngEnvMCAP566671-alfarahn-2`, `rg-nn-hackathon-2026-10`, East US):
Container Apps environment `cae-hackathon`, registry `acrnnhackathon2026` (Basic, no admin user),
log workspace capped at 1 GB/day, deploy identity `nn-hackathon-deploy` (AcrPush, Container Apps
Contributor, Reader, Managed Identity Operator on the pull identity only), pull identity
`nn-hackathon-pull` (AcrPull only).

## 2. Decisions needed

| # | Decision | Recommendation | Who |
| --- | --- | --- | --- |
| 1 | Who attends Days 3-5? David's mail says business users (LoB) attend Days 1-2. The repository assumes the same beginners all week. | Ask David. If Days 3-5 are a more technical team, David's agent/CI/CD content fits as is. If beginners stay, keep each lab to one guided build. | David |
| 2 | Days 3-5 length: David's slides say 4 hours; the published agenda says 09:00-12:30 (3.5 h). | Approve 09:00-13:00 explicitly, then I update the agenda, guides and the schedule test together. | David, Ali |
| 3 | Publishing on Day 1: optional finale in Lab 08, or automatic for everyone? | Teach `/publish-website` as the Lab 08 finale. Optionally preset a name per repository (Actions variable `WEBSITE_NAME`) so the first push publishes with zero steps. | Ali |
| 4 | Published pages are public to anyone with the link. | Keep public (phones on any network work). Fictional content only, as today. | Ali, David |
| 5 | Cold start: sleeping websites take about 30 s to answer the first visit. | Set `MIN_REPLICAS: 1` from Monday 26 to Friday 30 October (about USD 0.19 per website per day idle, about USD 9/day for 45), then back to 0. Two steps in `infra/README.md`. | Ali |
| 6 | Teardown date for the websites and registry. | Delete the resource group on Friday 6 November (one command in `infra/README.md`). | Ali, David |
| 7 | Day 3-4 issues: turning approved requirements into issues needs write access; the repository's MCP server is read-only by design. | Attendees create issues in the GitHub web page (copy the agent's story), which also teaches issues. No write-capable MCP. | Ali |
| 8 | Cloud agent for attendee repositories (Day 4 delegation lab). | Enable for the training organisation; budget premium requests for one cloud-agent session per attendee plus follow-ups (check current billing). | Owner, David |
| 9 | Credits per chat request are driven by always-loaded instructions (about 45k input tokens per request; `AGENTS.md` and `.github/copilot-instructions.md` both load) and the model. | Keep one short always-on file for attendee copies and move facilitator rules to a path-scoped or facilitator-only file; confirm the default model (Auto) for attendee accounts. Re-measure one `/create-website` afterwards. | Ali |

**Status on 22 October 2026:** 1 decided (the same people continue, 21 October); 2 decided (four
hours each in elapsed time, 20 October; start times still to confirm); 3 decided (optional
`/publish-website` in Lab 08); 4 as recommended (pages stay public, made-up content only); 7
superseded (tickets from the Requirement template, which the attendee's own agent updates with
`gh issue edit` after a yes); 5, 8 and 9 are in `final-workshop-david/DELIVERY.md` under Before the
Week, and 6 under After the Week.

## 3. Day by day

Moved on 22 October 2026. The final plan, with every timing, lives only in
`final-workshop-david/WEEK.md` (overview and timings) and `final-workshop-david/DELIVERY.md`
(minute-by-minute script and preparation). The Day 1 items that were still open moved into
DELIVERY.md's Before the Week list; the rest were done in the repository.

## 4. Housekeeping

- The two test repositories (`day1-final-check`, `add-chat-check`) were deleted on 19 October,
  together with their websites, images and Codespaces. The organisation holds only the template
  and `.github-private`.
- `ubuntu-latest` moves to Ubuntu 26 from 19 October, during workshop week. The publisher is now
  pinned to `ubuntu-24.04` with Node 24 actions; `ci.yml`, `codespace-image.yml` and
  `copilot-setup-steps.yml` still use `ubuntu-latest` and Node 20 actions (`checkout@v4`), which
  show a deprecation warning on attendee CI runs. Pin and upgrade them the same way (small).
- The Foundry client secret used by `FOUNDRY_*` expires on Sunday 1 November, two days after the
  workshop. Rotate it if anything should keep working afterwards.
- Keep push access to the template's `main` limited to you and jmkelly6: Azure trusts the
  publisher on that branch.
- Keep the organisation's OIDC subject claim on GitHub's default; a custom subject template would
  stop publishing (the fix would be one change in `infra/website-hosting.bicep`).
- **Deploy my app** (`deploy.yml`) still expects an `AZURE_CREDENTIALS` secret that does not exist.
  It is only for the post-workshop vendor app; move it to the same OIDC pattern later, or leave it.

## 5. Suggested order of work

| Order | Item | Effort |
| --- | --- | --- |
| 1 | Decisions 1, 2, 3 and 8 with David (one short call) | 30 min |
| 2 | Day 2 agenda update (Bill) | Small |
| 3 | Day 5 CI/CD lab: `website-ci.yml`, approval gate, recovery check | Half a day |
| 4 | Day 3 requirements-agent lab with the four building blocks | One day |
| 5 | Day 4 branches, delegation and code-review-agent labs | One day |
| 6 | Day 1 fixes and the attendee-like dry run | Half a day |
| 7 | Full rehearsal in fresh Codespaces, then the printed card | Half a day |
