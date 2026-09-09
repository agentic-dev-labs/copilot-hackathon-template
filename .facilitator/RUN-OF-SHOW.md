# Run of Show — Facilitator Only

> **Facilitator preparation material.** Temporarily versioned in `.facilitator/` with the
> repository owner's explicit disclosure approval on 2026-09-09. The folder name does not
> restrict access: repository readers can read this file and its history.
> See [README.md](README.md) for the 2026-10-12 cleanup reminder. Keep talk tracks, fallbacks,
> and timing pressure out of the attendee-facing agenda. Repository paths below start at the root.

**Event:** GitHub Copilot Workshop and Hackathon - Novo Nordisk North America
**Where:** Princeton, New Jersey · **When:** Mon 26 – Fri 30 October 2026
**Delivery:** Ali Farahnak (all content) · Jackie Kelly (Day 2, ~1h Power Platform)

---

## 1. The one rule for the week

**Never two demos back to back, and never a demo longer than 30 minutes.**

Every block follows the same four beats:

| Beat | Who | Length | Purpose |
|---|---|---|---|
| **SHOW** | Ali | 30 min | One theme, demonstrated properly. Latest GitHub Enterprise / agentic engineering. No slides. |
| **HAND OVER** | Ali | 2 min | State the goal, the acceptance criteria, and the time-box. Then stop talking. |
| **BUILD** | Attendees | 30-90 min | The lab. Ali and Jackie help people at their tables. |
| **PLAYBACK** | 2–3 teams | 15 min | A team drives their own screen. Ali narrates the lesson, not the fix. |

Handovers are included inside the existing blocks, not added to the timetable.

**Breadth first, depth later.** Monday introduces the main Copilot feature families, including
prepared results from later labs. It does not attempt every setup live. Keep the
[coverage and official references](../docs/REFERENCES.md) open for questions and point to the
appropriate later lab. Specialist topics are explicit reference options, not hidden omissions
or extra mandatory work. The guest's hour is the agreed exception to the 30-minute presenter demo limit.

**Target ratio: ~30% me showing · ~60% them building · ~10% playback.**
A 30-minute demo is enough to show a tool properly. Two in a row is a lecture, and that is the
failure mode to avoid — not the length of any single one.

### Why this shape
David's ask was explicitly hands-on ("not slideware", v3 outcome slide). Demonstrations teach
the features, guided labs establish the fundamentals, and the team build and showcase let
attendees apply them. The wider building population is potential reach, not an attendance count.

---

## 2. Time discipline

Days 1–2 are **6-hour days**; Days 3–5 are **half-days** (Jackie, 28 Aug).

> **Scheduling decision parked:** this working agenda stays at 09:00-15:00 on Days 1-2 and
> 09:00-12:30 on Days 3-5 until the rehearsal informs a decision. The internal blocking invite
> is a crew calendar hold, not evidence of attendee hours. Older notes translated its time
> inconsistently; verify the original time zone before comparing. No invites or times are
> changed as part of this repository cleanup.

### Where this sheet differs from `docs/AGENDA.md`

The attendee agenda shows the same blocks without the talk tracks. Every day below adds to
exactly 360 minutes (Days 1–2) or 210 minutes (Days 3–5), including breaks and lunch, so the
timing is arithmetic rather than optimism.
Lab time-boxes match the agenda. This validates arithmetic, not how long a new attendee needs;
measure the core path during rehearsal. Optional extras are separate from the required work.

| Lab | Time-box | This sheet |
|---|---|---|
| 00 | 30 min | 30 min |
| 01 | 60 min | 60 min |
| 02 | 60 min | 60 min |
| 08 | 45 min | 45 min |
| 05 | 90 min | 90 min |
| 03 | 60 min | 60 min |
| 04 | 60 min | 60 min |
| 07 | 60 min | 60 min |
| 06 | 90 min | 90 min |

> ✅ **Day-mapping conflict resolved (2 Sep).** Engagement brief §11 and `docs/AGENDA.md`
> disagreed about where Lab 06 sat. `docs/AGENDA.md` is now authoritative and matches the brief:
> Day 4 is the governance and production day, Day 5 is multi-agent plus evaluations. Lab 06 and
> the new Lab 07 both run at their full time-box.

---

## 3. Presenter kit — what is on screen

Have these open as tabs **before** each day starts. Switching context live kills the energy.

| # | Tab | Used on |
|---|---|---|
| 1 | Team repo in **Codespaces** (browser only — make the point loudly) | Every day |
| 2 | The repo **Issues** tab, filtered to Copilot-assigned | Days 1, 3, 5 |
| 3 | A prepared cloud-agent issue, session, and **reviewed PR** | Days 1, 3, 4 |
| 4 | Current agent/session list; prepared independent sessions if supported | Days 1, 5 |
| 5 | Customizations editor and the three repository agent files | Days 1, 5 |
| 6 | Actions run history (`ci.yml`, `deploy.yml`) and a completed automation | Days 1, 4 |
| 7 | A terminal with `copilot` ready | Days 1, 2 |
| 8 | The **integrated browser and Copilot built-in browser tools** in the presenter VS Code session, showing the app | Days 1, 3 |
| 9 | GitHub Chat and a prepared Space containing only synthetic training sources | Days 1, 3 |
| 10 | A verified installed plugin, its component list, source, and successful synthetic result | Days 1, 5 |
| 11 | [Official references](../docs/REFERENCES.md) and today's lab | Every day |

**Browser demo pre-flight:** confirm the built-in tools are available in the presenter session
and can reach the app's forwarded or deployed URL. Attendees can follow along if their client
exposes them; otherwise use the presenter demo or inspect the page manually. Do not install a
separate browser MCP server for this workshop.

**Screen hygiene:** 150% zoom, dark theme off (projectors), notifications silenced, no customer
name in any repo/org name that appears on screen.

---

## 4. Day 1 — Monday · 6h · Line of Business

**Theme: "You can build software today."** No local developer installation is a core prerequisite.

| Time | Beat | Content |
|---|---|---|
| 09:00–09:30 | **SHOW** | **Possibilities tour.** Start with the working app and Codespaces/devcontainer. Use GitHub Chat and a prepared Space for a synthetic explanation, table, or diagram. Open a prepared issue, cloud-agent session, reviewed PR, and automation result. Identify the main surfaces and preview later-day depth; do not wait for a new cloud run. |
| 09:30–10:00 | **BUILD** | **Lab 00.** Attendees open their assigned repository, check tools and sign-in, run tests, set a unique label, and inspect the repository-local `vendor-analyst` definition. Its presence does not prove organization sharing; that is a separate demonstration. |
| 10:00–10:30 | **SHOW** | **Everyday assistance through agent work.** Inline and next-edit suggestions, inline chat/smart actions, then Ask/Plan/Agent for one scoped change. Add context, inspect models/Auto, run a test, verify the page with built-in browser tools, and show stop/steer, diffs, and recovery. Open the Customizations editor. Use the presenter client when attendee tools differ. |
| 10:30–10:45 | Break | |
| 10:45–11:45 | **BUILD** | **Lab 01 — VS Code agent mode.** |
| 11:45–12:15 | **SHOW** | **CLI and reusable capabilities.** Interactive plan, bounded `copilot -p` task, tool permissions, context/model/usage, stop/resume, and a prepared delegated task. Invoke an already-installed plugin agent or skill and inspect its source. Point to research/fleet/scheduling as optional CLI capabilities, and SDK/BYOK as specialist follow-ups. No policy changes or installation wait. |
| 12:15–13:00 | Lunch | |
| 13:00–14:00 | **BUILD** | **Lab 02 — Copilot CLI.** |
| 14:00–14:45 | **BUILD** | **Lab 08 - name it and ship it.** Use the assigned unique label in `config.json`, commit/merge, then run **Deploy my app** with **connect_dataverse** off. Tests run before deployment. Read the actual URL from the workflow summary rather than constructing one. One team repository has one app; service credentials are prepared by the facilitator. |
| 14:45–15:00 | **PLAYBACK** | Show each repository's actual deployment URL and hear one builder lesson. Keep a failed deployment visible as unfinished rather than presenting a prepared URL as that team's result. |

### The three 30-minute demo budgets

These are durations within the existing slots, not new timetable blocks. Handovers are included.

| Block | Sequence and minutes | Fallback |
|---|---|---|
| Opening tour | 5 app; 6 Codespaces/devcontainer; 6 GitHub Chat/Space with a synthetic table or diagram; 7 prepared issue/session/PR/automation; 4 capability map; 2 Lab 00 handover | Open the prepared result when a request is slow; name what is recorded versus live |
| VS Code | 4 inline/NES; 3 inline chat/smart action; 5 Ask/Plan/context/models; 8 Agent/test/browser loop; 4 stop/steer/diff/checkpoint; 4 Customizations editor; 2 Lab 01 handover | Use the prepared diff, test, and browser result if generation exceeds the budget |
| CLI | 6 interactive plan/tool request; 4 bounded `-p`; 4 context/model/usage; 4 stop/resume/delegation; 6 prepared plugin invocation; 4 optional capability map; 2 Lab 02 handover | Inspect the verified task/plugin result if the live client does not expose it |

Say explicitly: Codespaces is the environment, GitHub Copilot is the assistant, and Microsoft 365
Copilot is another product. A model is not an agent role; instructions, tools, and execution location
also shape the result. Auto and reasoning controls vary. Compaction can lose detail; a new task may
deserve a new session. Git preserves work beyond temporary chat checkpoints.

In the browser, contrast **Add to Chat** with **Share with Agent**. Agent-opened pages are isolated;
an explicitly shared tab can carry signed-in state. Share only the training page, then revoke access.
Agent edits may already be applied: demonstrate the actual diff and restore flow, not a universal
"accept every edit" dialog. No separately installed browser server belongs in this workshop.

**Day 1 wins to bank:** attendees can name the main capabilities and choose a next step; each team
has an environment, a tested change, a reviewed commit, a CLI task, and its actual deployment result.
Use the [small optional tasks](../docs/REFERENCES.md#small-tasks-for-early-finishers) during lab slack.

---

## 5. Day 2 — Tuesday · 6h · Line of Business

**Theme: "Your Power Platform skills transfer."** This is Jackie's bridge day.

| Time | Beat | Content |
|---|---|---|
| 09:00–10:00 | **GUEST** | **Jackie — Power Platform connectors, Dataverse, Power Automate → code apps.** Hand the room over completely. Ali floats and takes notes for the Day 3–5 audience split. |
| 10:00–10:30 | **SHOW** | **The teaching version of the assurance problem.** Run `vendor-assurance src/vendor_assurance/samples/synthetic_soc2_meridian_outreach.md --as-of 2026-10-26 --output-directory reports/`: ten controls, 2/10, exact evidence, and gaps. Show the same results in Dataverse. Explain that this is a small text-based training evaluator, not a demonstrated 200-page OCR pipeline or a full implementation of the customer's assessment system. |
| 10:30–10:45 | Break | |
| 10:45–12:15 | **BUILD** | **Lab 05 — connect your app to your own Dataverse rows.** 90 minutes; this is the hardest lab of the LOB days. |
| 12:15–13:00 | Lunch | |
| 13:00–14:00 | **BUILD** | Team build on a chosen small improvement using synthetic data. Agree one observable outcome; Ali and Jackie coach at tables. No new production integrations or infrastructure are required. |
| 14:00–15:00 | **PLAYBACK** | **Showcase.** Every team demos. Photograph the board. Invite David and Susan in for this hour. |

**Recruit here:** during the showcase, identify who should come back for Days 3–5. Ask explicitly.

---

## 6. Day 3 — Wednesday · half-day · Low-coders + pro-coders

**Theme: "The agent works without you."**

| Time | Beat | Content |
|---|---|---|
| 09:00–09:30 | **SHOW** | **Issue to pull request.** Write one goal, acceptance criteria, and files in scope; assign the task and inspect the session log. Show model/reasoning choices where supported, then the actual workflow approval and branch-review rules. Scope this exercise to one PR; don't present a historical session limit as universal. A draft PR exposes work for review but is not itself a required-human-approval policy. |
| 09:30–10:30 | **BUILD** | **Lab 03 — cloud agent.** |
| 10:30–10:45 | Break | |
| 10:45–11:15 | **SHOW** | **Remote MCP and built-in browser tools.** Connect remote GitHub MCP at `https://api.githubcopilot.com/mcp/`; show a read-only query and toolsets. Then use **Copilot's built-in browser tools** in the presenter session to open the deployed app, inspect it, and capture the result. Explain the distinction: GitHub MCP is an external integration; the browser tools come from the Copilot client and need no separately installed server. |
| 11:15–12:15 | **BUILD** | **Lab 04 — remote GitHub MCP.** |
| 12:15–12:30 | **PLAYBACK** | Review the morning's agent PR together as the closer. |

---

## 7. Day 4 — Thursday · half-day · Low-coders + pro-coders

**Theme: "Repeat it, test it, and review it."** Show practical engineering habits. The workshop
does not certify the resulting application or its audit trail for a regulated production use.

| Time | Beat | Content |
|---|---|---|
| 09:00–09:30 | **SHOW** | **The agent runs from a trigger.** Revisit Monday's prepared automation, then configure a narrow issue-created task with the tools needed to read, execute, write, and open a PR. Inspect one real generated result. Show a harmless exact-tool denial and metadata-only hook log. Connect the pattern to David's requested workflow without implying a general document-processing system is complete. |
| 09:30–10:30 | **BUILD** | **Lab 07 — automations and hooks.** |
| 10:30–10:45 | Break | |
| 10:45–11:15 | **SHOW** | **Review and deploy.** Reuse yesterday's PR, request Copilot code review, inspect any effort-level selector, and evaluate one finding against code and tests. Approval capability is a policy-dependent preview, off by default; an assessment comment is not a required approval. Finish with the tested Container Apps workflow and its run log. Do not promise that a model catches a deliberately inserted bug every time. |
| 11:15–12:30 | **BUILD** | Production-readiness review: tests, ruff, deploy, audit trail. |

**Message to land:** the issue, diff, tests, reviewer, and run log make the exercise inspectable.
Lab 07 records selected event metadata, not full arguments or results. Logs are mutable and cloud
files are ephemeral. A retained, access-controlled audit system and formal approvals are separate work.

**Content-exclusion questions:** use the current supported-surfaces documentation. The September
release extended support to the app and CLI, but that is not proof of identical enforcement in
every client or every tool path. Never use a real confidential file to demonstrate a restriction.

### Use David's own framing — and credit him out loud

David publishes a series on LinkedIn called *Putting Agents to Work*. His most-engaged post
gives you the exact spine for this day:

> "An agent is not something you talk to. It is something that acts when something happens.
> **You do not summon the agent. The world does.**"
>
> "You are no longer designing a conversation, you are designing a **trigger**, an
> **instruction set**, a **tool surface**, and an **escalation policy**."
>
> "Old automation runs the same path every time. An agentic workflow chooses the path each
> time." … "Do not start with the model. **Start with the trigger.**"

Lab 07 is now built on those four words, deliberately. Say so from the front: *"This is David's
framing, not mine - and those questions help us design the automation and its review controls."* Naming him is the
point; do not let the lab quietly absorb his thinking without attribution.

Two more of his lines worth holding:

- *"The better question is not whether an agent can act on its own, it is whether it should."*
  Use this when someone asks why the agent opens a **draft** PR instead of merging.
- *"Three of every five decisions are not agent food."* This is exactly why the evaluator
  returns **Unclear** instead of guessing: an empty quote for silence, or an exact quote for an explicit gap. Unclear is the agent saying
  *this one is not mine* — his thesis, running in code.

Careful: reference the published framework, not his career history. Flattering, not creepy.

---

## 8. Day 5 — Friday · half-day · Low-coders + pro-coders

**Theme: "Many agents, and how you know they are right."**

| Time | Beat | Content |
|---|---|---|
| 09:00–09:30 | **SHOW** | **Author and distribute what Monday previewed.** Compare instructions, prompts, agents, skills, hooks, MCP, and plugins. Inspect the repository and organization sources, marketplace, and effective `extraKnownMarketplaces`/`enabledPlugins`. Revisit the installed toolkit and its verified tool result; do not change enterprise policy live. Use prepared independent sessions for optional parallel-work, worktree, or Agent Merge discussion. |
| 09:30–11:00 | **BUILD** | **Lab 06 - build your own agent and skill.** Author both under `.github`, test present and missing evidence, generate evaluator JSON plus a separate `reports/baseline/`, then hand off to analyst, writer, and reviewer. Compare artifacts without overwriting the baseline. Dependent handoffs differ from independent parallel sessions. |
| 11:00–11:15 | Break | |
| 11:15–11:45 | **BUILD** | **Evaluate evidence quality.** Compare results with fixed-date sample expectations, inspect exact quotations, and test silence and explicit gaps. Use a second-model check only where available; it is another opinion, not an oracle. Optionally show usage/impact metrics with synthetic assumptions: PR volume and modeled ROI are directional measures, not proof of correctness or productivity. |
| 11:45–12:30 | **PLAYBACK** | Final demonstrations and close. Handoff: what runs Monday without me. |

**Close with the ask, not a thank-you:** name the next step — their own org, their own repos, the
17 Nov Ignite session at Lyngby, and who owns the vendor-assurance PoC internally.

---

## 9. Excitement devices

| Device | When | How |
|---|---|---|
| **Cold open** | Day 1, 09:00 | Build before you introduce yourself. Kills the "another vendor deck" reflex instantly. |
| **The wall of PRs** | All week | Project the repo PR list on a second screen. It fills up visibly. |
| **Compare agent approaches** | Day 5 | Inspect prepared independent results for the same task; compare correctness and effort as well as elapsed time. |
| **Name the problem** | Every SHOW | Use the synthetic assurance work queue as the through-line. The list analogy helps beginners; the short text examples do not demonstrate a 200-page production pipeline. |
| **Team playback** | Daily | They drive their own screen. Their colleague succeeding beats me succeeding. |
| **Sponsor in the room** | Day 2, 14:00 | David and Susan see the showcase, not a status report. |

---

## 10. Fallbacks — decide these in September, not in the room

| If this breaks | Fallback |
|---|---|
| Attendees cannot join the external org | Deliver everything in Novo's own org; David does admin pre-work |
| Codespaces blocked on the network | Use a prepared presenter environment and screenshots; identify an approved attendee environment before promising a hands-on fallback |
| Cloud agent disabled or blocked by a ruleset | Use local CLI work and a pre-run PR. `/delegate` also requires cloud-agent access and is not a bypass |
| Copilot seats missing on Day 1 | Seats funded in `agentic-dev-labs`; verify the week before |
| Preview features changed | **Re-verify Agent HQ, Claude/Codex week of 19 Oct.** Keep a Copilot-only version of every Day 5 demo |
| Jackie unavailable Day 2 | Use an agreed substitute presentation in the same slot; any timing change requires explicit agreement |

Do not depend on retired products. The August 4 announcement stopped new Spark apps;
the existing workbench's export window ended August 31. Recheck current availability before delivery.

---

## 11. Morning pre-flight — 20 minutes before each day

- [ ] Codespace created and warm from the venue network
- [ ] `python -m pytest` green
- [ ] `copilot` authenticated; `gh auth status` clean
- [ ] One issue ready to assign live; one draft PR already open as a backup
- [ ] Reference guide, synthetic Space, and verified plugin result ready for the opening tour
- [ ] Browser tools, model controls, and recovery exercised in the actual presenter client
- [ ] Projector at 150% zoom, notifications off
- [ ] Synthetic sample is the only data on screen
- [ ] Today's fallback identified out loud to Jackie

---

## 12. Cut list — when running late

Cut in this order, protecting core lab completion:

1. Stretch goals
2. Optional live generation; use its prepared result while retaining the core feature introduction
3. Playback down to one team
4. Additional production-hardening discussion (Day 4), not the core test/review exercise

---

## 13. Pre-event dependencies

Blocking items from the engagement brief that gate this run sheet:

1. EMU vs SSO — can attendees join an external org? (before 14 Sep)
2. Attendee count and **GitHub usernames** per track (before 14 Sep)
3. Tools and network access work inside Codespaces for all core labs; no local Node prerequisite
4. Deck v4 — 6h Days 1–2, half-day Days 3–5, Jackie's hour, no Spark, corrected invite hours
5. Control labels and sample expectations were aligned on 2 Sep; this was not full semantic
  validation. The later review reproduced negation, retention, residency, and unstated-SOC-2
  defects. The Northstar sample is 8/10 at the fixed review date, not proof those cases are solved.
6. Dry run with David and one participant on the loaner laptop (late Sep)
7. **New:** confirm team repos stay **private or internal** — Lab 07 automations do not exist in
   public repositories.
8. **New:** ask whether Novo will allow the **GitHub app for Microsoft Teams** (see §14). If yes,
   it is the strongest bridge from their M365 world into GitHub.

---

## 14. Bonus demos — deploy when a block runs short

Half-days are tight, so none of these have a fixed slot. Keep them loaded and use one when a
build block finishes early or the energy dips. Each is under ten minutes.

| Demo | Why it lands at Novo | Watch out |
|---|---|---|
| **GitHub Copilot in Microsoft Teams** — `@GitHub` in a channel starts a cloud agent session everyone can see and steer | They live in Teams, Work IQ and Cowork. This is the bridge: a Teams discussion becomes a pull request without leaving the conversation. Repo admins can require an **extra approval** for PRs from the Teams identity, which is the compliance answer built in | Public preview. Needs the GitHub app for Teams installed and cloud sandboxes enabled. Consumes AI credits; sandbox billed separately |
| **Agent Plugins 1.0** - inspect an installed capability package | Use `copilot plugin install assurance-toolkit@agentic-dev-labs`, inspect the discovered agent, skills and MCP tools, then ask a narrow question about a synthetic document and verify the source quotation | Installation, tool permissions and conversion quality must all be rehearsed. Do not promise a before-install failure or after-install success. The toolkit remains an optional presenter install, not a Lab 00 dependency |
| **Generate synthetic test data** | Ask for a fictional report with a stated residency contradiction, run the deterministic evaluator, then inspect the quoted result together | Silence should produce Unclear, not Fail. Also test explicit negative evidence; do not claim real reports never acknowledge deficiencies |
| **The distribution ladder** — repo → org → enterprise | The answer to David's scale problem. Repo level works today with no admin; org level is one file in `.github-private/agents/`; enterprise is `copilot/managed-settings.json`. Show it as a ladder so nobody hears "you need admin before this is useful" | David is not a GitHub enterprise admin at Novo. The rungs he can act on are repo and org. Enterprise is a conversation for Martin's onboarding workstream and 17 Nov |
| **Enterprise team specialization** — `copilot/teams/*.json` + `team-mappings.json` | The best answer to "central IT will never move fast enough for us." An enterprise marks individual keys `overridable`; a named team then layers its own values on top while every unmarked key stays locked. Novo could give a pilot team a wider model list and looser permissions without weakening the floor for everyone else. And because the source repo is `.github-private` set to **internal**, a team proposes a governance change by opening a **pull request** — policy with a review gate, which is the language a GxP shop already speaks | Enterprise-admin territory, so this is a conversation for Martin, not a click for David. Multi-team users get the *least restrictive* value per key — say that out loud, it surprises people |
| **`strictKnownMarketplaces`** — restrict installs to named marketplaces only | The sharpest answer to "how do we stop people wiring random tools into our estate?" Policy lives in Git, so every change is reviewable through a pull request | **Show it, do not set it.** It is enterprise-wide with no org scope, and locking it to `agentic-dev-labs` would break your own `ali/*` and `work-iq/*` plugins — Joker, observability, presentation, WorkIQ, ATK. An empty array is total lockdown |
| **MCP allowlists in enterprise managed settings** | Inspect supported server restrictions and effective client policy | Show, do not change. User-assigned names are not a strong security boundary; service authorization still matters |
| **Copilot Memory** | Show a possible source of retained repository context, distinct from a curated Space | Availability and controls vary. Remembered information is not guaranteed correct or complete |
| **Actions quarantines suspicious workflows** (28 Jul) | One line on Day 3 or 4 that costs nothing: it is not only that a human must approve a workflow run, GitHub actively holds workflows it judges potentially malicious. Free credibility in a security-conscious room | Do not oversell it as a security product; it is a guardrail, not GHAS |
| **`vulnerability-alerts` permission for `GITHUB_TOKEN`** (3 Sep) | A concrete least-privilege example for Day 4: grant a workflow read access to Dependabot alerts without handing it a broad scope. Pairs with the hooks story — both are about narrowing what an automated actor may touch | Only worth showing if somebody asks about workflow permissions |
| **Media in issues and pull requests from `gh`** (1 Sep) | Small delight: the agent attaches a screenshot to its own pull request | Ten seconds, no more |
| **Spec Kit** | Optional specification-to-task workflow | Rehearse current installation and commands. Do not promise offline model access or regulatory compliance from a template |
| **`/btw`** or other side-question controls | Show the available way to ask without replacing the active task | Client-specific; inspect the current command list before promising it |
| **Token spend, visible** — hover a response in VS Code for per-model token usage; the same indicator now sits in Copilot Chat on github.com | The room will ask what this costs. Showing the number per turn is far more convincing than quoting a price list, and it sets up the ROI dashboard on Day 5 | Do not editorialise about credits. Show the number, move on |
| **Copilot app and integrations** | A prepared view of another surface and its customization/integration options | Separate setup and policies. Preview in Monday's map; use official references for follow-up rather than installing during a lab |
| **Dictation** | Optional short spoken prompt | Verify the actual client's processing and data-handling settings before making on-device or no-audio-upload claims |

---

## 15. Research snapshots and rehearsal checks

The following release notes were collected in early September. Dates refer to announcements,
not proof that each feature is enabled or works in every workshop client. The current labs and
the rehearsal checklist above take precedence over older talk tracks.

- **Copilot automations exist and are the customer's original ask.** David asked in April for
  "an agent that can automatically run … read a SOC 2 report, and populate a vendor output
  report." Automations do exactly that: schedule, issue-created, PR-opened or PR-synchronized
  triggers, with per-automation tool scoping. Now Lab 07. **Private or internal repos only.**
- **Hooks are new to this plan** — `.github/hooks/*.json`, with `preToolUse` able to *approve or
  deny* a tool call. This is the GxP audit story made concrete. Also Lab 07.
- **The cloud agent is no longer just "issue → draft PR."** It can research, plan and iterate on
  a branch *before* a PR exists, from the agents panel. Lab 03 updated.
- **Copilot code review can approve pull requests** (1 Sep 2026) and has effort levels (7 Aug).
- **Browser demo choice updated 7 Sep:** use Copilot's built-in browser tools, with no additional
  browser MCP server. Lab 04 separately teaches remote GitHub MCP; verify built-in tool availability
  in the actual presenter session before delivery.
- **Custom-agent capabilities and sharing vary by client.** The repository agents now require
  evaluator JSON and preserve its calculated results; run the authoring and handoff lab on the target client.
- **Copilot usage metrics API now exposes PR lifecycle data** and the impact dashboard has an ROI
  section — folded into Day 5 evaluations, and useful to Mike directly.
- **Models moved.** Several were deprecated on 31 Aug. Do not pin a model name in any lab; let the
  picker default. Re-check the week of 19 Oct.
- **Spark retirement announced 4 Aug**, with the existing workbench export window ending 31 Aug. Not part of the workshop.

### Second sweep of the changelog (3 Sep 2026)

Four things were shipping while this plan was being written and are now folded into the blocks above:

- **The VS Code integrated browser can take comments on page elements.** Select elements on a
  rendered page, comment on them, and the agent fixes them in one batch; local HTML reloads as it
  edits. This is the strongest single demo for a non-coding audience and it was missing entirely.
  Use it alongside Copilot's built-in browser tools in the Day 1 agent-mode block.
- **`/rubber-duck` asks a second, complementary model to check the first one's work.** Experimental,
  in an Agent Host session. Now the opener for Day 5 evaluations — "a second reviewer" is the exact
  metaphor this audience lives in.
- **Parallel agent sessions are a local feature now, not only Agent HQ.** Chats arrange side by side
  in horizontal or vertical groups, layouts persist, multiple windows can attach to one session via
  Agent Host, and sessions started in other applications appear in the VS Code sessions list. Day 5
  can use prepared independent sessions if the relevant client supports them; no live demo is guaranteed.
- **Content exclusions expanded to the Copilot app and CLI** (2 Sep). Consult the current
  supported-surfaces matrix before describing enforcement. Keep all workshop data synthetic.

Smaller items already absorbed into the blocks: cloud-agent **reasoning level** (3 Aug), code review
**Lite/Balanced effort levels** with an org default and a visible label (7 Aug), **full agentic review
of cloud-agent pull requests** and the removal of the 300-file cap (27 Aug), and the Copilot CLI's
move to a **native Rust runtime** with `defaultMode` / `defaultPermissionMode` and session restore
(24 Aug).

Not required hands-on: other IDEs, SDK/ACP/LSP, BYOK, migrations, Teams/Slack and other integrations,
and advanced administrative APIs. They now appear in the
[optional coverage map](../docs/REFERENCES.md#optional-possibilities-and-specialist-topics), with
official links and setup caveats. Individual model launches remain unsuitable as a fixed syllabus;
show the actual picker. Use the broader Day 1 budgets above instead of treating this historical
release snapshot as the demo script.

## Official References

- [Coverage guide](../docs/REFERENCES.md): official links for the full week, including the bonus topics.
- [Copilot features](https://docs.github.com/en/copilot/get-started/features), [VS Code agents](https://code.visualstudio.com/docs/agents/overview), and [customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).
- [CLI overview](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli), [browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools), and [Spaces](https://docs.github.com/en/copilot/concepts/context/spaces).
- [Copilot changelog](https://github.blog/changelog/label/copilot/) and [VS Code release notes](https://code.visualstudio.com/updates): recheck the week before delivery.
