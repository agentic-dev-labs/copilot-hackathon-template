# Week: Overview and Timings

**Always look in this folder.** It is the one place for the workshop's overview and timings, and
it holds nothing else:

| File | Open it for |
| ---- | ----------- |
| **WEEK.md** (this file) | The overview and every slot's timings: David's slot, what Ali shows and when, what attendees do (with Ali or after) and where. Share it with David and the helpers. |
| [DELIVERY.md](DELIVERY.md) | Delivering it: the minute-by-minute run sheet, the words for every show and cut, what to drop when late, what goes wrong, and the preparation lists. |
| [1.png](../1.png) to [5.png](../5.png) | David's final slides, one per day. The times and slot wording here are his, unchanged. |

Private and git-ignored with this folder: never commit it, or every attendee copy gets it.
Checked against the slides and the repository on 22 October 2026: every lab's time-box fits its
slot, and the agenda, the Day 2 guide and the facilitator notes now include Bill Leeson's 11:45
talk from slide 2.

## How to Read the Day Tables

- **Time:** David's slot. Days 1-2 are clock times (the slides write the afternoon as 1:00-3:00),
  in rooms MKC 1D412 and 1D413. Days 3-5 count from the session start, as on the slides: confirm
  each start time with the organizers.
- **David's slot:** his slide wording, unchanged.
- **Ali shows:** each short demonstration on Ali's screen, with the minute it starts.
- **Attendees do:** **Listen** or **Watch** (hands off), **With Ali** (click along at the same
  time), or **After** (repeat it on their own repository straight after the show, from the minute
  given).
- **Open:** the page and section where attendees repeat it. It is also where anyone lost rejoins.

Every lab block runs the same way: **show** (2-5 minutes, eyes up), then **do** (5-15 minutes,
after Ali), then **check** (one visible result), then **cut**: everyone moves on, finished or not,
and a helper catches up whoever is behind. The attendee guides say the same in one line: **Lost?**
Find the row the room is on, open its link, start there, and raise your hand.

## The Week at a Glance

| Day | David's title | Who presents | Attendees build, on their own repository | Outcome |
| --- | ------------- | ------------ | ---------------------------------------- | ------- |
| Mon 26 Oct | GitHub and your first app | Sponsor welcome and HZRW, then Ali all day | Their private copy, a first website, one own idea, a chart or chat, all pushed | Their own website with a feature they checked, saved on GitHub |
| Tue 27 Oct | Your own business idea | David, Jackie and Bill Leeson; Ali at the tables | Their own idea, with fictional data | A first version of their idea, one checked journey, questions for IT, **Next** wishes |
| Wed 28 Oct | VS Code and a Requirements agent | MUKQ, then Ali from 00:20 | Tickets on a board, their own skill and User Requirements agent, criteria, one ticket built and tested | A User Requirements agent, a validated brief and a tested feature |
| Thu 29 Oct | GitHub Copilot cloud agents | Ali | A protected `main`, a version on the live site, the cloud agent building the next ticket, their own Code Review agent | A Code Review agent, a findings report and a reviewed cloud-agent change |
| Fri 30 Oct | CI/CD with GitHub Actions | Ali | Required checks with a UI test and screenshots, Copilot's ticket tried in a feature slot, an approved release to production, a rollback, a demo, a handoff | A tested CI/CD workflow with a sandbox deployment and rollback practice |

**One website all week.** Monday's website and own idea become Tuesday's prototype; Tuesday's
**Next** wishes become Wednesday's tickets. Copilot builds the first ticket in the Codespace on
Wednesday, the cloud agent builds the next one on Thursday and the pipeline deploys it with a
version number, and on Friday GitHub checks every change in a browser, shows each pull request in
a feature slot (the sandbox), and releases to production only after approval.
**Days 3-5** are the same people, continuing: those from Days 1-2 who want to take their idea
further (Ali's call, 21 October), probably fewer than on Monday. Days 4 and 5 open with a short
catch-up for anyone who skipped a day.

## Why It Fits Novo US

- **Their ideas are trackers.** 13 of the 14 real ideas on the roster are trackers, to-do lists or
  dashboards, and Day 3's tickets and board are the same pattern.
- **Their lifecycle, in miniature.** Ticket, acceptance criteria, test, reviewed pull request,
  required checks, approved release and rollback mirror requirements, test evidence, change control
  and release approval. Day 3 says out loud that "validate" means checkable, not GxP validation:
  the Quality & GxP team (3) and Global Security (5) are in the room.
- **David's asks.** Agents that fire against repositories: the Day 4 opening demo. User requirement
  docs: the tickets and the brief's **Requirements** list (his "validated brief"). Code reviews:
  their own Code Review agent. CI/CD in GitHub Enterprise: Day 5, and the handoff routes the work
  into Novo's own GitHub.
- **Safe for a security-sensitive estate.** No tokens, secrets or laptop installs; OIDC publishing
  with no secret, `contents: read` checks, rulesets, approvals, and agents that ask before they act.
  Copilot code review stays off, as decided on 21 October.
- **US English** on the pages they see: color, center, favorite, watercolor.

## Day 1, Monday 26 October: GitHub and Your First App ([slide](../1.png))

Rooms MKC 1D412 and 1D413, 09:00-15:00. Until 10:30 attendees follow only their repository's
README; from 10:45 the route is `docs/START-HERE.md`.

| Time | David's slot | Ali shows | Attendees do | Open |
| ---- | ------------ | --------- | ------------ | ---- |
| 09:00–09:30 | Sponsor welcome (SEFR video), ASTER Overview teaser (HZRW), glossary and GitHub basics (concepts only) | 09:00 nothing: the sponsor's SEFR video and HZRW's ASTER teaser. 09:15 GitHub on the template: a repository, its files and README, **Commits**, a file's **History**, search, **Issues**; the five words; save, review, commit, push | **Listen**, then **Watch**: look along on the template in the browser, changing nothing | README › This Is GitHub |
| 09:30–10:00 | **Lab:** Find files and Copilot Chat, ask and refine a question | 09:30 **Use this template**: owner agentic-dev-labs, name = GitHub username, **Private**. 09:37 the new copy; **Code > Codespaces > Create codespace on main**; **Trust Folder & Continue**; the README's **Open Preview**. 09:42 Chat in **Ask**: everyone asks for a fun table name and compares (same question, different answers). 09:48 a question, then a better one | **With Ali** 09:30-09:42: one private copy, its Codespace, the README preview. **After** 09:44: their table name, compared with a neighbour's, then hands up. **After** 09:50: their own question and its refinement | README › Find Your Files and Copilot Chat |
| 10:00–10:30 | Create an idea note, save, review, commit, push and verify | 10:00 Chat in **Agent**, `/create-website`, the Project Planner beside Chat, then **Keep**. 10:15 `site/brief.md` is the idea note; **Save All**, Source Control, commit, push, found on GitHub | **After** 10:05: their first website, kept. **After** 10:19: pushed and found on GitHub | README › Your First Website |
| 10:30–10:45 | Break | Switches to the warm demo Codespace | Anyone without a pushed page finishes it with a helper | - |
| 10:45–11:45 | **Lab:** Create a website with /create-website and preview it | 10:45 prepared websites, said to be prepared: Weather in 3D, Princeton Map, Photo Studio, Lab Chase. 10:55 five lines explained by Chat; the `<h1>` headline changed by hand. 11:10 `/create-website` again: a tracker built live from one sentence, in its own folder. 11:30 save and push | **Watch** until 11:00. **After** 11:00: their headline changed by hand. **After** 11:14: one own idea in its own folder. **After** 11:32: pushed and shown to a neighbor | Lab 01, sections 1-4 |
| 11:45–12:15 | Trust but verify: check a button and a figure, fix and recheck | 11:45 "hide finished tasks": say what you expect, click twice, compare. 11:55 count it: with the morning's extra task, **1 of 5** becomes **2 of 5**. 12:05 written in `brief.md`, pushed. "Copilot can be wrong; you are the checker." | **After** 11:49: one button checked. **After** 11:57: one number counted. **After** 12:07: written down and pushed | Lab 01 › Coached Verification Block |
| 12:15–13:00 | Lunch | | | |
| 13:00–14:00 | **Lab:** Add a useful interaction, personalize and check | 13:00 chart, chat or picture: pick one. 13:05 `/add-chart` (3D too); `/add-chat` and a picture mentioned. 13:20 tick a task, the chart follows; count it. 13:35 "a sky blue look", kept; then a wild one undone with **Undo** (it takes back everything not kept) | 13:00 they pick. **After** 13:09: their feature added. **After** 13:23: checked against their own count. **After** 13:39: one look change and one **Undo**. 13:50: written in the brief | Lab 02, sections 1-5 |
| 14:00–14:45 | **Lab:** Save, share and keep building (publication optional) | 14:00 the sparkle commit message. 14:10 **Commits** and a file's **History** on GitHub. 14:20 the challenge card; optional `/publish-website`, and at 14:35 the room opens Ali's page on their phones | **After** 14:03: pushed. **After** 14:13: their history found. **After** 14:22: one challenge level, optional publishing with a helper. 14:35: shown to a neighbor | Lab 08, sections 1-4 |
| 14:45–15:00 | Pair sharing and selected volunteer demonstrations | 14:50 hosts two or three volunteers. 14:58 "Push, then stop your Codespace." | 14:45 pairs share one feature and how they checked it, then watch | START-HERE › Today's Route |

**Finish:** their own website with a chart or chat they checked, one own idea in its own folder,
a headline changed by hand, one change undone, and all of it on GitHub with its history found.

## Day 2, Tuesday 27 October: Your Own Business Idea ([slide](../2.png))

Rooms MKC 1D412 and 1D413, 09:00-15:00. Ali does not present today: he is table support with the
other helpers. Still to confirm with David: who restarts the room at 10:45 and who hosts 14:45.

| Time | David's slot | Ali shows | Attendees do | Open |
| ---- | ------------ | --------- | ------------ | ---- |
| 09:00–09:30 | David: Business/IT roles, approved tools and AI marketplace | - David presents | **Listen** | - |
| 09:30–10:30 | Jackie: Power Platform, Dataverse and connector examples | - Jackie presents | **Listen** | - |
| 10:30–10:45 | Break | At the tables | Reopen Monday's Codespace, never a second one; open the Day 2 guide | Day 2 guide › Today's Route |
| 10:45–11:45 | Supported own-idea build with fictional local data | - At the tables: steers each idea towards a tracker or a dashboard | 10:45 four answers agreed with a helper. 10:55 one page built or continued. 11:30 saved and pushed before Bill's talk | Day 2 guide › Morning Build |
| 11:45–12:15 | Bill Leeson: Building a Project Brain | - Bill presents | **Listen** | - |
| 12:15–13:00 | Lunch | | | |
| 13:00–14:00 | Open build: improve an interaction, check behaviour and get help | - At the tables | One useful thing added, then one improvement at a time, each checked | Day 2 guide › Improve One Interaction |
| 14:00–14:45 | Supported building, fixes and optional assisted publication | - At the tables; helps with `/publish-website` | Fixes made and pushed; optional publishing | Day 2 guide › Fixes and Optional Publishing |
| 14:45–15:00 | Volunteer demonstrations and next step with the technical owner | - At the tables: every brief gets its **Next** wishes | Volunteers show; questions for IT; two or three **Next** wishes in their brief, pushed: Wednesday's tickets | Day 2 guide › Show and Plan the Next Step |

**Finish:** a first version of their own idea with one checked journey, saved on GitHub, questions
for IT, and **Next** wishes in the brief.

## Day 3, Wednesday 28 October: VS Code and a Requirements Agent ([slide](../3.png))

MUKQ opening session, then Ali Farahnak (Microsoft). Four hours, elapsed time. In every block Ali
shows the step on the demo website, then attendees do the same on their own idea.

| Time | David's slot | Ali shows (demo website) | Attendees do (own idea) | Open |
| ---- | ------------ | ------------------------ | ----------------------- | ---- |
| 00:00–00:20 | MUKQ: Global and Microsoft perspectives on AI development | - MUKQ presents | **Listen** | - |
| 00:20–00:50 | Ali: workspace setup, repo walkthrough and agent roles/tools | 00:20 a board: **Projects > New project > Board**, `<username> website`, **Import items from repository** with their own repository chosen, then **Workflows > Item added to project > Off**. 00:31 a ticket: **Issues > New issue > Requirement**, "Mark urgent tasks", landing under **No Status**. 00:39 the Codespace terminal, `copilot`, `/login`, "Use the GitHub tools to list the open issues" (that is MCP); agent roles in one sentence each | **After** 00:24: their board, workflow Off. **After** 00:34: two or three tickets from their **Next** wishes. **After** 00:42: Copilot CLI signed in, tickets listed by a GitHub tool | Day 3 guide, section 1 |
| 00:50–01:30 | Build a User Requirements agent: instructions and output format | 00:50 the four building blocks in the Explorer, starting with Monday's `/create-website` skill, and `/agent`. 00:56 the skill prompt: the output format. 01:09 the agent prompt: role and rules. 01:22 `/exit`, `copilot`, `/agent` lists it | **After** 00:59: their `user-stories` skill, one step in their words. **After** 01:12: their User Requirements agent, one rule in their words. **After** 01:24: the agent listed | Day 3 guide, section 2 |
| 01:30–01:45 | Break | | A helper adds the skill and agent with anyone missing them | - |
| 01:45–02:30 | Agent lab: draft user stories and acceptance criteria, then validate | 01:45 the agent on demo ticket #1: the draft, one criterion rewritten so it can be counted ("validate means checkable, not GxP validation"), "Yes, update issue #1". 02:20 one card dragged into **Todo** for today, one for tomorrow | **After** 01:52: criteria on their first ticket. **After** 02:10: on the others. **After** 02:23: two tickets approved in **Todo** | Day 3 guide, section 3 |
| 02:30–03:15 | Build lab: implement an approved story, debug and verify the fix | 02:30 card to **In Progress**; "Read issue #1 with the GitHub tools and build it"; each criterion checked in the preview; "I expected ..., I saw ..." | **After** 02:37: their ticket built, every criterion checked by hand, one fix if needed. 03:05 hands up | Day 3 guide, section 4 |
| 03:15–03:45 | Team build: add tests and document build and run commands | 03:15 `checks/test_issue1.py`: `pytest checks` green, red on purpose, green again. 03:32 the brief's "How to build and run" and **Requirements** list: the validated brief | **After** 03:20, helping each other at the table: green tests. **After** 03:35: their validated brief | Day 3 guide, section 5 |
| 03:45–04:00 | Checkpoint: show the agent, requirements and working feature | 03:45 a commit ending `Closes #1`, pushed: the card moves to **Done** by itself | **After** 03:48: their ticket **Done**. 03:54: agent, skill, board and feature shown to a neighbor | Day 3 guide, section 6 |

**Outcome (slide):** a User Requirements agent, a validated brief and a tested feature.

## Day 4, Thursday 29 October: GitHub Copilot Cloud Agents ([slide](../4.png))

Ali Farahnak (Microsoft). Four hours including the break, elapsed time.

| Time | David's slot | Ali shows | Attendees do | Open |
| ---- | ------------ | --------- | ------------ | ---- |
| 00:00–00:20 | Cloud-agent overview: delegation, safeguards and human review | 00:02 the road of a change: feature branch, pull request, review, merge, pipeline, live with a version. 00:05 a new Requirement ticket on the demo repository that nobody assigns. 00:07 delegation and safeguards. 00:12 human review. 00:15 back to the ticket: an automation added its criteria by itself | **Listen**; at 00:18 two volunteers say the road back. Newcomers do the catch-up with a helper | Day 4 guide › Joining today?, section 1 |
| 00:20–00:50 | GitHub lab: practice branches and pull requests with a small change | 00:20 `/publish-website` first if a website has no address. 00:25 the `Protect main` ruleset. 00:32 branch `feature/version-number`, the `#` and its space removed before `version:`, the footer prompt on the first page. 00:42 pull request, **Files changed**, merge, **Version 1.0.N** live | **After** 00:22: an address, if missing. **After** 00:28: their ruleset. **After** 00:36: their version change. **After** 00:44: merged; the live version checked now or at the break | Day 4 guide, section 2 |
| 00:50–01:30 | Delegation lab: assign an approved requirement to Copilot | 00:50 a **Todo** ticket read once more. 01:05 **Assign to Agent** (base branch `main`, agent Copilot, **Assign**); the board moves the card to **In Progress** by itself. 01:10 the demo ticket assigned last evening: its session log and draft pull request | **After** 00:53: a ticket picked and checked. **After** 01:07: assigned to the cloud agent. **After** 01:14: its log and draft pull request followed | Lab 03, sections 1-4 |
| 01:30–01:45 | Break | | Copilot keeps working | - |
| 01:45–02:30 | Build a Code Review agent: review rules and report format | 01:45 `review.instructions.md` and its `applyTo`. 02:00 `code-review.agent.md`; `/agent` lists it. 02:20 branch `review-tools`, pull request, merge | **After** 01:49: their review rules. **After** 02:04: their Code Review agent, one rule in their words. **After** 02:22: both merged | Day 4 guide, section 4 |
| 02:30–03:15 | Report lab: run the agent on a diff and verify its findings | 02:30 Copilot's pull request under **Files changed**; "Review pull request #5" writes `reviews/pr-5.md`; one finding **Confirmed**, one **Not a problem**. 03:00 the change tried in the preview, `pytest checks` | **After** 02:38: their report, every finding marked by hand. **After** 03:03: the change tried themselves | Day 4 guide, section 5 |
| 03:15–03:45 | Iteration lab: request fixes with @copilot, retest and peer-review | 03:15 `@copilot Fix finding 1 ...` on the pull request. 03:32 pull, retest, and the review agent again | **After** 03:18: their `@copilot` comment. 03:22 peer review in pairs while Copilot works. **After** 03:35: retested and reviewed again | Day 4 guide, section 6 |
| 03:45–04:00 | Checkpoint: review the report and decide whether to merge | 03:45 merge: the pipeline deploys the feature with the next version, and the ticket moves to **Done** | **After** 03:49: merged and live, or closed with a reason; the report saved by pull request | Day 4 guide, section 7 |

**Outcome (slide):** a Code Review agent, a findings report and a reviewed cloud-agent change.

## Day 5, Friday 30 October: CI/CD with GitHub Actions ([slide](../5.png))

Ali Farahnak (Microsoft). Four hours including the break, elapsed time.

| Time | David's slot | Ali shows | Attendees do | Open |
| ---- | ------------ | --------- | ------------ | ---- |
| 00:00–00:20 | CI/CD concepts: continuous integration, delivery and deployment | 00:02 CI and CD in plain words, on their own week. 00:10 `publish-website.yml`: `on:`, `permissions:`, `version:`. 00:18 the Agentic Workflows demo (preview), only if on time | **Listen**. **After** 00:14: the three lines found in their own file. Newcomers do the catch-up with a helper | Day 5 guide › Joining today?, section 1 |
| 00:20–00:50 | Workflow lab: edit a starter YAML file, triggers and permissions | 00:20 branch `ci-checks`: the check starter copied and explained, `pull_request` added, `write` changed to `read`. 00:37 the pull request runs both checks; merged. 00:44 both made **required** in the ruleset | **After** 00:25: their starter edited. **After** 00:40: green and merged. **After** 00:46: both checks required | Day 5 guide, section 2 |
| 00:50–01:30 | CI lab: build and test a pull request, inspect logs and fix failures | 00:50 a 900-pixel banner above the header: the **UI check** turns red and blocks the merge; the log table; `home-phone.png`; Copilot explains; fixed, green, merged. 01:20 the next approved ticket assigned to Copilot for the break | **After** 01:00: their red check read from its log and screenshot, fixed, merged on green. **After** 01:22: their next ticket with Copilot. 01:26 hands up | Day 5 guide, section 3 |
| 01:30–01:45 | Break | | Copilot keeps working | - |
| 01:45–02:30 | CD lab: approve and deploy a build to a training environment | 01:45 both slot starters through a pull request; **Settings > Environments > production** with yourself as required reviewer. 01:57 Copilot's pull request: **Approve workflows to run**, then **Actions > Deploy feature slot > Approve and run**; **View deployment** opens the feature slot with its strip. 02:14 **Approve**, merge, **Review deployments > Approve and deploy**: production shows the same content number | **After** 01:50: slots merged, production protected. **After** 02:03: Copilot's build in their feature slot, its criteria checked. **After** 02:17: released to production. 02:27 hands up | Day 5 guide, section 4 |
| 02:30–03:15 | Recovery lab: smoke-test the app and redeploy a known-good build | 02:30 `scripts/smoke_test.py`: all PASS. 02:38 "Oops, wrong words": the feature slot shows it first, then shipped: FAIL. 02:55 **Revert** and approve: PASS, same content, higher version | **After** 02:33: PASS noted. **After** 02:42: their bad release and its FAIL. **After** 02:58: rolled back, PASS | Day 5 guide, section 5 |
| 03:15–03:45 | Team demos: show requirements, review report and CI/CD evidence | Hosts and keeps time: about three minutes per table | Each table: the board and one ticket's criteria, a confirmed and a rejected finding, red then green with a screenshot, the feature slot with its strip, an approval, the version, a rollback | Day 5 guide, section 6 |
| 03:45–04:00 | Handoff: share agent profiles, pipeline steps and release ownership | 03:45 Copilot writes HANDOFF.md, one sentence corrected, merged by pull request; the "To make it real" routes | **After** 03:48: their HANDOFF.md merged. 03:57 Codespaces stopped | Day 5 guide, section 7 |

**Outcome (slide):** a tested CI/CD workflow with a sandbox deployment and rollback practice.
