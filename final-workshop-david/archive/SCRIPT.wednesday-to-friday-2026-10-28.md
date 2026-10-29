# Cue sheet

**Who:** 🎤 **Ali** = you show, they watch · 🤝 **Ali + attendees** = they click along with you ·
👥 **Attendees** = they do it alone · 🗣️ = guest speaker · `grey` = type or paste exactly ·
"quotes" = what you say · 📄 = the file in **docs/** and the section attendees have open; **bold** = a new section starts. Full version with Monday and Tuesday: `archive/SCRIPT.full-2026-10-28.md`.

**Rejoin rule** (every morning): "Lost? Find our row in your guide's route
table, open its link, start there. Hand up and a helper catches you up."

**Every morning, 30 min before:** demo Codespace open and warm · zoom 150% · notifications off ·
your own MCP servers off (**MCP: List Servers** → **Disable**) · today's guide in a tab · 5 min with
helpers (their tables, rejoin rule, today's Watch for) · fixed the template overnight? Tell the
room: open **docs > QUICK-COMMANDS.md** → **Fetch Updates From the Main Workshop Repository** →
paste it in Chat (Agent) → commit and push (from Thursday: the workshop-updates branch prompt,
then merge the PR).

Jump to: [Wednesday](#wednesday) · [Thursday](#thursday) · [Friday](#friday) · [Preparation](#preparation)

## Wednesday

28 Oct · 4 h, times from the start · their guide: **docs/DAY-3.md**, read in the template on GitHub ·
demo repo: `alfarahn-hackaton` · you: Copilot app, GitHub website, then the Codespace
**Screen link:** `github.com/agentic-dev-labs/copilot-hackathon-template/blob/main/docs/DAY-3.md`

🎤 Ali shows · 🤝 Ali and attendees together · 👥 attendees alone · **Where** = the app, page, file
or guide step to look at · **Paste** = the exact text to paste or type (attendees' prompts are in
their guide at the step under **Where**)

**30 min before:**

1. Copilot app signed in as **alfarahn** (not `alfarahn_microsoft`: it gets a 404 on workshop repos).
2. App clean: **Customize > Plugins** shows Awesome Copilot only (no `anthropics/skills`, no
   example-skills, no project-planning). Backup skill: `~/.copilot/skills-backup/travel-planner`.
3. ADO is yours only (attendees have no access; they watch 00:27-00:33). **Project Meridian** is filled ✓ (42 items: 6 epics, 12 features, 24 stories, 4 sprints).
   Do not rehearse 00:29-00:32 on it: those prompts change priorities and states live.
4. Demo repo `alfarahn-hackaton`: planner on `main`, no board, no automations, no tickets (yours start at **#1**).
5. Meridian backup: `github.com/agentic-dev-labs/meridian-demo` (9 epic issues) and
   `final-workshop-david/demo/meridian/ROADMAP.md`. The live run takes about 6 minutes.
6. Codespace open and warm, Chat signed in, **Agent** chosen. Tabs: screen link,
   dev.azure.com/alfarahn-demo-org › Project Meridian › Boards, your repo, meridian-demo,
   skyscanner.com, trivago.com, visitcopenhagen.com. Backup art: `final-workshop-david/demo/wish-to-live/index.html`.
7. Helpers know: workshop account in the app · quit the app fully after installing a plugin ·
   three ticket routes (agent, helper connects GitHub's issue tools, paste by hand) · `Duplicate of #1` fallback.

### 00:00 MUKQ

Global and Microsoft perspectives on AI. You: app, tabs, Codespace ready.

### 00:20-00:50 Setup and tools · attendees: DAY-3.md §1

| Time | Who | Where | Do | Paste |
| --- | --- | --- | --- | --- |
| 00:20 | 🎤 Ali | Screen link: `docs/DAY-3.md` | Rejoin rule. **Say:** "Today: a fun skill, your own skill, your own agent, your backlog, a tested feature. Ask answers, Agent changes files, a custom agent has one job, a skill is a recipe, a plugin is a package. Tomorrow: the cloud agent." | |
| 00:22 | 🎤 Ali | Copilot app | Click through: **Sessions** · **My work** · **Automations** · **Customize**. Under the message box: **Interactive** / **Plan** / **Autopilot**; tool permission **Ask every time**. **Say:** "Today you approve every step." | |
| 00:25 | 👥 Attendees | Copilot app · `DAY-3.md` §1 steps 1-2 | Open the app → **Sign in to GitHub** (workshop account). No app: pair with a neighbour. | |
| 00:27 | 🎤 Ali | dev.azure.com/alfarahn-demo-org › **Project Meridian** › **Boards > Backlogs**, then **Sprints** | **MCP, you only: attendees have no ADO access, they just watch.** Show what AI planned before they arrived: 6 epics → 12 features → 24 stories in 4 sprints. Open one story → **Acceptance Criteria**. **Say:** "AI planned this launch. Every story has criteria someone can check." | |
| 00:28 | 🎤 Ali | Copilot app › new session | Paste → **Allow** → three projects. **Say:** "MCP is a standard plug. This one connects Copilot to Azure DevOps." | `Using the azure-devops MCP server, list the projects in my Azure DevOps organization, one per line. Read only: change nothing.` |
| 00:29 | 🎤 Ali | Copilot app, same session | **Prioritise.** Paste → it reads all 24 stories and shows a table; nothing changes yet. **Say:** "It thinks like a product owner: safety and regulatory first, and whatever others wait for." | `In Project Meridian, act as the product owner. Read every User Story with its Epic, sprint, links and acceptance criteria. Give each one a Priority from 1 (must have) to 4 (nice to have) and Story Points (1, 2, 3, 5 or 8): safety reporting, regulatory work, and stories that other stories wait for come first. Show me one table sorted by priority with ID, title, sprint, priority, points and a reason of at most 8 words. Change nothing yet: wait for my yes.` |
| 00:30 | 🎤 Ali | Copilot app → ADO **Boards > Backlogs** (refresh) | Paste → it writes. ADO: **Story Points** filled in → open a Priority 1 story → **Discussion** has its reason, **History** shows the change. **Say:** "It asked before it changed anything, and every change is traceable." | `Yes, apply them: set Priority and Story Points on every story, and add a one-line comment with the reason on each Priority 1 story. Then tell me how many items you changed.` |
| 00:31 | 🎤 Ali | Copilot app → ADO **Boards > Boards** (refresh) | **Stand-up.** Paste → cards move to **Active** and **Closed**, one card tagged **Blocked**. **Say:** "Your Monday stand-up, in one sentence." | `Run a made-up stand-up for Sprint 1 Prepare in Project Meridian: set its 2 highest-priority stories to Closed and the next 3 to Active, then tag one Active story Blocked and add a comment that it waits for a made-up packaging supplier. Then tell me in 4 lines what is done, what is in progress, what is blocked, and which Sprint 2 stories can start now.` |
| 00:32 | 🎤 Ali | Copilot app | **Steering report.** Paste → read three lines aloud. **Say:** "From backlog to steering committee in one sentence. GitHub has the same plug: you use it in an hour." | `Write a 10-line status report on Project Meridian for a steering committee: progress per Epic (closed, active, new), what is blocked and why, the top 3 risks, and a go or no-go for Sprint 2 with one reason. Read only: change nothing.` |
| (if ahead) | 🎤 Ali | Copilot app | **Triage.** Paste → read its triage aloud. | `In Project Meridian a tester reports: "The adverse-event form loses the reporter's phone number when it is saved." Triage it like a team lead: search the backlog for a related story or a duplicate, decide whether it is a Bug or a User Story, suggest a priority from 1 to 4 and the sprint, and show me the work item you would create with its title, repro steps and the story it relates to. Create nothing yet: wait for my yes.` |
| (if ahead) | 🎤 Ali | Copilot app → ADO: the new Bug | Paste → open the new item: tag, link, comment. | `Yes, create it tagged Meridian, link it as Related to that story, and add a one-line comment saying why you chose that priority.` |
| 00:33 | 🤝 Both | Copilot app › **Customize > Plugins** · `DAY-3.md` §1 steps 3-4 | Scroll **Awesome Copilot** 1 min (**Say:** "a community shop window") → add marketplace → open **example-skills** → read its skills and the Apache licence aloud (**Say:** "A plugin runs on your laptop: read before you install.") → **Install**. | `anthropics/skills` |
| 00:37 | 🤝 Both | Copilot app · `DAY-3.md` §1 step 5 | Quit the app completely (also the icon near the clock) → reopen → new session → type → **algorithmic-art** is listed. | `/skills` |
| 00:39 | 🎤 Ali | Copilot app, same session | Type → it lists its art skills. | `Do you have art skills?` |
| 00:39 | 🎤 Ali | Copilot app · `DAY-3.md` §1 step 6 | Paste → **Allow** reading the skill and writing files (about 2 min; **Say:** "skill = recipe, plugin = package, marketplace = shop") → open the page → move the sliders → **Regenerate**. | `Use the algorithmic-art skill. Title it "Induced Fit". Made-up drug-like molecules, little ball-and-stick shapes with blue, teal and white atoms, drift through calm water around a made-up protein with a curved pocket in the centre. When a molecule fits the pocket, it locks in and glows softly; the others drift on. Calm deep-blue and teal colours on a light background. Sliders for the number of molecules, the speed (temperature), the pocket size and the trail length, a seed box with Prev, Next and Random, and a counter that shows how many molecules are bound. Everything is fictional: no real compounds, logos, or medical claims. Open it when it is done.` |
| 00:41 | 👥 Attendees | Copilot app · `DAY-3.md` §1 step 6 | The same art prompt (it is in their guide), or their own theme. Helpers: install, restart, `/skills`. | |
| 00:47 | 🎤 Ali | Two volunteers' screens | Their art on screen. **Say:** "Now you make your own skill." | |

### 00:50-01:30 Your own skill, then your agent · attendees: DAY-3.md §2

| Time | Who | Where | Do | Paste |
| --- | --- | --- | --- | --- |
| 00:50 | 🎤 Ali | Copilot app › new session (tabs: skyscanner.com, trivago.com, visitcopenhagen.com) | Paste → it browses: Skyscanner flights → trivago hotel → Visit Copenhagen sights → the proposal page opens. Talk over it: **Say:** "Next time ask me only the city, the dates, and business or pleasure. Never sign in, book, or pay." | `Plan a made-up weekend trip to Copenhagen from New York, Friday 30 October to Monday 2 November, for one adult, for pleasure. Use the browser: flights on Skyscanner, a hotel near the centre on trivago, and three sights with ticket prices on Visit Copenhagen, the city's official tourism website. Never sign in, book, or pay, and say which prices you could not confirm. Then make a simple one-page website with my proposal and open it.` |
| 00:58 | 🎤 Ali | Copilot app, same session → it writes `~/.copilot/skills/travel-planner/SKILL.md` | **Say:** "Now you understood it." Paste. | `Now you understand what I want. Use the skill-creator skill to make a personal skill called travel-planner from what we just did: it asks me only the city, the dates, and business or pleasure, then does the same searches and builds the same one-page website. Never sign in, book, or pay. Keep it short and do not run any tests.` |
| 00:59 | 🎤 Ali | Copilot app › new session | Type → **travel-planner** is listed. | `/skills` |
| 01:00 | 🎤 Ali | Copilot app, same session | Type → it asks its questions → stop. **Say:** "You can download skills, and you can make your own." | `Plan a weekend in Lisbon.` |
| 01:02 | 👥 Attendees | Copilot app · `DAY-3.md` §2 steps 2-4 | Their made-up trip → their skill → new-session test. | |
| 01:15 | 🎤 Ali | Screen: `DAY-3.md` §2 step 5 (building-blocks table) → Copilot app › new session | **Say:** "A skill says how, an agent says who." Paste → open the file it made: `~/.copilot/agents/user-requirements.agent.md` (name, description, rules) → change one rule. | `Create a personal custom agent at ~/.copilot/agents/user-requirements.agent.md with name: user-requirements and a one-line description. It is a User Requirements agent for my website about a project planner in the GitHub repository agentic-dev-labs/alfarahn-hackaton. When I describe wishes, it drafts one ticket per wish with the sections What I want (my words), Which page (site/index.html unless I say otherwise), User story as "As a ..., I want ..., so that ...", Acceptance criteria as 2 or 3 "Given ..., when ..., then ..." that a person can check by clicking or counting, each with a checkbox, and Only change. It shows me every draft first. Only when I say yes does it create the tickets with the GitHub tools. When I ask it to improve a ticket, it shows the new text first and, only when I say yes, changes only the User story and Acceptance criteria sections and keeps every other line exactly as it is; then it reads the ticket again and tells me whether my own words under What I want are unchanged. It asks me one question at a time, never writes website code, and uses made-up people and data only.` |
| 01:18 | 🎤 Ali | Copilot app › new session | Type → **user-requirements** is listed. | `/agent` |
| 01:19 | 👥 Attendees | Copilot app · `DAY-3.md` §2 step 6 | Their agent, with their own repository name in the prompt. | |
| 01:29 | 🎤 Ali | Copilot app › **Customize > Plugins** › Awesome Copilot › **project-planning** | **Say:** "Break. No agent yet? A helper sits with you now. While you have coffee, AI plans a big project." **Install** (30 s) → quit the app fully, reopen → new session → paste → **Allow** → leave it running on screen. | `Use the project-planning plugin. Plan the launch of a made-up injectable medicine, Project Meridian, in 12 markets within 12 months. Write ROADMAP.md with: a 5-line brief; 9 epics (regulatory submission, manufacturing and supply, packaging and labelling, medical education, market access and pricing, patient support programme, safety reporting, IT systems and data, communications); under each epic 4 features, each with a user story, 3 Given/When/Then acceptance criteria, a quarter (Q1 to Q4), an owner role, and dependencies; then a table of the top 5 risks. Then create one GitHub issue per epic in agentic-dev-labs/meridian-demo with its features as a checklist, labelled with its first quarter. Everything is made up: no real products, people, or data.` |
| 01:30 | ☕ Break | Tables | Helpers finish skills and agents. You watch Meridian; backup: `meridian-demo` on GitHub. | |

### 01:45-02:30 Tickets, triage, criteria · attendees: DAY-3.md §3

| Time | Who | Where | Do | Paste |
| --- | --- | --- | --- | --- |
| 01:45 | 🎤 Ali | `ROADMAP.md` from the Meridian session (backup `final-workshop-david/demo/meridian/ROADMAP.md`) → github.com/agentic-dev-labs/meridian-demo › **Issues** | **Meridian, 3 min.** **Say:** "While you had coffee, AI planned a launch." Brief, 9 epics, risks → one issue per epic, labelled by quarter → open one: features as a checklist → read one story and its criteria. **Say:** "Every feature has criteria someone can check. That is what you do for your own website now." | |
| 01:48 | 🎤 Ali | GitHub › org **agentic-dev-labs** › **Projects**, then `alfarahn-hackaton` › **Agents > Automations** | **New project** → **Start from scratch: Board** → name `alfarahn website` → keep **Import items**, repository `alfarahn-hackaton` → **Create project** → top right **Workflows > Item added to project > Off**. **Say:** "Todo = approved, In Progress = being built, Done = finished." Then **Suggestions** › **Triage incoming issues** → read two lines of its prompt (**Say:** "it only suggests") → **Create automation**. | |
| 01:52 | 👥 Attendees | GitHub, their own repository · `DAY-3.md` §3 steps 1-3 | Board and triage. Helpers check: own repository (not the template), **Item added** Off, the automation listed. | |
| 01:57 | 🎤 Ali | Copilot app › new session › type `/agent` › **user-requirements** | Paste → read one draft aloud (story + Given/When/Then). | `Draft tickets for these wishes for my website: mark urgent tasks so they stand out; highlight today's column; add a Saturday column. Add one more ticket that asks for the same thing as my first wish in other words, so I can test the triage. Show me the drafts first.` |
| 01:59 | 🎤 Ali | Copilot app → GitHub › `alfarahn-hackaton` › **Issues** | Type → point at the tool it used. **Say:** "That is MCP again, now for GitHub." GitHub: 4 tickets under **No Status**. | `Yes, create them.` |
| 02:02 | 👥 Attendees | Copilot app · `DAY-3.md` §3 steps 4-5 | Their 4 tickets. Only reads GitHub? Helper connects the issue tools, or they paste drafts into **Issues > New issue > Requirement**. | |
| 02:09 | 🎤 Ali | GitHub › `alfarahn-hackaton` › **Agents**, then the copy ticket | "Running automation Triage incoming issues for new issue …" (about 2 min). Copy ticket: **Agent suggestions: Close → duplicate of #1** → **Accept all** → its card moves to **Done**. Open #1. **Say:** "Can I check each criterion by clicking or counting?" | |
| 02:11 | 🎤 Ali | Copilot app, the user-requirements session | Paste → it shows the new text. | `Rewrite criterion 2 of issue #1 so that I can check it by counting. Change nothing else.` |
| 02:12 | 🎤 Ali | Copilot app → GitHub › issue #1 | Type → own words unchanged. **Say:** "Validate means checkable, not GxP." | `Yes, update issue #1.` |
| 02:15 | 👥 Attendees | GitHub + Copilot app · `DAY-3.md` §3 steps 6-7 | Accept their duplicate; check every criterion; improve one. | |
| 02:26 | 🎤 Ali | GitHub › **Projects** › `alfarahn website` | Drag #1 (you build today) and #2 (Copilot tomorrow) into **Todo**. **Say:** "Todo is your approval." | |
| 02:28 | 👥 Attendees | Their board · `DAY-3.md` §3 step 8 | Two tickets in **Todo**; a neighbour checks one. | |

### 02:30-03:15 Build the approved ticket · attendees: DAY-3.md §4

| Time | Who | Where | Do | Paste |
| --- | --- | --- | --- | --- |
| 02:30 | 🎤 Ali | Codespace › Chat (**Agent**); the prompt is `docs/QUICK-COMMANDS.md` › Fetch Updates | **Say:** "Now VS Code, where your website lives." Paste → **Source Control**: commit `Fetch workshop updates` → **Push**. | `Fetch the latest updates from the main workshop repository: run python3 scripts/update_from_template.py and tell me in plain words what changed.` |
| 02:34 | 🎤 Ali | Board: #1 to **In Progress** → Codespace › Chat | Paste → read the plan aloud. | `Read issue #1 with gh issue view 1 and make a short plan to build it in site/index.html: what changes, and how I can check each acceptance criterion. Change nothing yet and wait for my yes.` |
| 02:36 | 🎤 Ali | Codespace › Chat → `site/index.html` → Chat `/start-website` (Website preview) | Paste → read the change, **Allow** → check each criterion by hand in the preview. | `Yes, build the plan. Change only what it needs and keep everything else. Do not run tests or scripts: I check it myself.` |
| 02:37 | 🎤 Ali | Codespace › Chat (only if a criterion fails) | Paste with what you really saw. **Say:** "Most useful sentence of the week." | `Criterion 2 of issue #1 fails. I expected [this]. I saw [that]. Fix only that.` |
| 02:38 | 👥 Attendees | Codespace · `DAY-3.md` §4 steps 1-7 | Fetch updates, plan, build, check every criterion, debug. | |
| 03:05 | 🎤 Ali | Room | "Hand up if every criterion passes." One volunteer: 30-second debug story. | |
| 03:14 | 🎤 Ali | Room | **Say:** "Now the computer re-checks it for you: tests." | |

### 03:15-03:45 Tests and how to run · attendees: DAY-3.md §5

| Time | Who | Where | Do | Paste |
| --- | --- | --- | --- | --- |
| 03:15 | 🎤 Ali | Codespace › Chat → `checks/test_issue1.py` → terminal → `site/index.html` | Paste → **Allow** `pytest checks` → green → change the heading or button text it names in `site/index.html`, never the test → save → `pytest checks` → red → **Ctrl+Z** → save → green. **Say:** "On Friday GitHub runs these on every change and takes phone screenshots." | `Write tests in checks/test_issue1.py for the acceptance criteria of issue #1 that can be checked from the files, using from website import Page as shown in checks/README.md. Give every assert a short message saying what I expected. Tell me which criteria stay manual checks. Include one check for an existing heading or button label in my page's HTML, and tell me the exact text to change for the red-test exercise. Do not change the website to make a test pass. Then run pytest checks.` |
| 03:20 | 👥 Attendees | Codespace · `DAY-3.md` §5 steps 1-3 | Their tests, in pairs: the neighbour checks. | |
| 03:32 | 🎤 Ali | Codespace › Chat → `site/README.md` | Paste → confirm statuses: #1 Done, #2 Todo, the rest No Status. **Say:** "Requirements traced to their tickets, plus how to run it: your validated brief." | `Add a section called How to build and run to the end of site/README.md, in plain words: how to open the page (/start-website), how to run the tests (pytest checks), how to run the build check (python -m app.site --check), and the manual checks for issue #1. Then add a section called Requirements: one line per ticket with its number, title, user story, and status expected after today's closing commit (Done for issue #1, Todo for the approved tickets for tomorrow, or No Status for an unapproved ticket). Do not guess the board's statuses; ask me to confirm them.` |
| 03:34 | 👥 Attendees | Codespace › `site/README.md` · `DAY-3.md` §5 step 4 | Their two README sections. | |

### 03:45-04:00 Checkpoint · attendees: DAY-3.md §6

| Time | Who | Where | Do | Paste |
| --- | --- | --- | --- | --- |
| 03:44 | 🎤 Ali | Room | **Say:** "Last step: close the ticket with a commit." | |
| 03:45 | 🎤 Ali | Codespace › **Source Control** (branch **main**, bottom left) → GitHub board | **Save All** → page, test, `site/README.md` → commit message (use #1's real title) → **Push** → board: #1 in **Done**. | `Mark urgent tasks so they stand out. Closes #1` |
| 03:48 | 👥 Attendees | Codespace › **Source Control** · `DAY-3.md` §6 | Commit and push; from 03:52 show a neighbour: art, skill, agent, board, ticket, green tests. | |
| 03:56 | 🎤 Ali | Room | **Say:** "Tomorrow: branches, pull requests, Copilot builds #2 in the cloud, your Code Review agent checks it. Bring your phone. Push, then stop your Codespace." | |

**Two starting points:** most attendees use their Monday repository (it gets today's guide at 02:30 with
Fetch Updates). Anyone without one, or wanting a clean start, makes a copy during the art time or the
break with a helper: template **Use this template** → owner **agentic-dev-labs** → name
`<username>-planner` → **Private** → Codespace → Chat **Agent** → `/create-website` → **Project
Planner** → commit `Add my first website` → push.

**Running late:** 00:27 ADO: the backlog and the 00:28 prompt only, skip the triage rows · 00:33 slow
installs → you finish the art on screen, they install at the break · 00:50 their own trip shortened to
the tourism site and the page · 01:02 skip the new-session test · 01:15 paste the agent prompt as it
is · 01:45 Meridian shortened to the roadmap file only · board and triage always before tickets ·
01:57 three tickets: two wishes and one copy · 02:11 improve only #1 · 02:34 skip the plan: paste
"Read issue #1 with gh issue view 1 and build it in site/index.html. Change only what it needs." ·
03:15 the README sections go with the 03:45 commit.

**Watch for**

- App says 404 or cannot find the repository → wrong account: sign out, sign in with the workshop account
- ADO asks to sign in or fails → say "a standard server, same idea", skip it, show the GitHub tools at 01:57
- ADO board shows no change → refresh the page (F5); a state it may not skip → let it go through **Active**
- No **algorithmic-art** after **Install** → app not fully quit: quit from the icon near the clock, reopen, new session, `/skills`
- No **Install** button, or blocked → company policy: use Awesome Copilot's **APNG Studio**, or they watch your screen
- Art page blank → the network blocks its drawing library: show the backup page
- Meridian takes more than 12 min or stops → say "it keeps working"; at 01:45 show the finished copy in `meridian-demo` and the saved `ROADMAP.md`
- Meridian issues missing or in the wrong repository → the prompt names `agentic-dev-labs/meridian-demo`; show the ones that exist
- Skyscanner or trivago blocks or shows a puzzle → tourism website only; never sign in, book, or pay
- **travel-planner** missing → new session, `/skills`; still missing → the guide's fallback writes `~/.copilot/skills/travel-planner/SKILL.md`
- **user-requirements** missing from `/agent` → new session; the file must be in `~/.copilot/agents/`
- Agent "can only read GitHub" → helper connects GitHub's issue tools in **Customize** (`https://api.githubcopilot.com/mcp/x/issues`, workshop sign-in), or they paste drafts into **Issues > New issue > Requirement**
- Tickets in the wrong repository → wrong repository name in the 01:15 agent prompt: close them as not planned, fix the file
- No triage session in **Agents** → the automation came after the tickets: make one more copy ticket, or comment `Duplicate of #1` and **Close issue**
- No **Agent suggestions** after 5 minutes → comment `Duplicate of #1` and **Close issue**
- New tickets land in **Todo** → **Item added to project** still on: switch off, drag back
- No **New project** → helper creates the board or arranges access
- Ticket lost their own words → copy back from its **edited** history
- Fetch Updates says changes are not committed → commit first, then fetch again
- `gh issue view` fails in the Codespace → paste the ticket's criteria into Chat instead
- Tests say **no tests ran** → file must be `checks/test_*.py`; rerun `pytest checks`
- Word changed but tests stayed green → change the HTML text the assertion names, never the test
- Commit without `Closes #1` → close the ticket by hand
- Real names, trips, or work data anywhere → everything stays made up

**Tonight (Wednesday to Thursday):** see **Before Thursday** under Thursday: push the template,
dry-run Day 4 on a practice copy, check the organisation's settings.

## Thursday

29 Oct · **2 h 45 min**, times from the start · their guide: **docs/DAY-4.md**, read in the template
on GitHub until §1 step 2 copies it into their repository · demo repo: `alfarahn-hackaton` · you:
slides, then the Codespace, GitHub, and the Copilot app · phone at hand for **Confirm access**
**Screen link:** `github.com/agentic-dev-labs/copilot-hackathon-template/blob/main/docs/DAY-4.md`
**Slides:** `final-workshop-david/day4-announcements.html` (**F** fullscreen, **N** notes, arrows)

🎤 Ali shows · 🤝 Ali and attendees together · 👥 attendees alone · **Where** = the app, page, file
or guide step to look at · **Paste** = the exact text (the same prompts are in their guide and in
`docs/QUICK-COMMANDS.md` › Thursday)

**What the audit showed (28 Oct, evening, read-only):** of about 50 workshop repositories, about
15 have their website on GitHub and about 27 have it only **uncommitted** in their Codespace.
Nobody has published yet (no `websiteName`), and nobody has tickets. So §1 is one commit and push
from the Codespace: **include all changes**. The few with no website at all build one with a helper
(`/create-website`, the guide's **Joining today**).

**Before Thursday (tonight):**

1. Review and push today's template changes to `main` (guides, the check starter with its
   Screenshots job, `scripts/pr_screenshots.py`, `scripts/ui_check.py`, the **Show my version**
   ticket template, the publisher's `version.json` environment). Then
   `gh run list -R agentic-dev-labs/copilot-hackathon-template -L 1` is green. Attendees fetch
   from GitHub: nothing new reaches them before this push.
2. Dry-run all of DAY-4.md on a fresh practice copy (template **Use this template** →
   `dryrun-day4`, **Private**), not on `alfarahn-hackaton`: that one stays like theirs for the live
   demo (website on `main`, no name, no checks). Keep from the dry run the pull request with its
   **UI check** comment and its **Reviewer automation:** comment, and the live footer: your backup
   screens.
3. In the dry run, note any label that differs from the guide and fix the guide: Copilot app
   **Projects +**, **Which repositories should this Project use?**, **Overview**, **Needs input**;
   the draft pull request and **Approve workflows to run**; both pictures in the comment (signed
   in); the trigger **Ready for review**, **Only this issue**, **Suggest tools**, the limits (Per
   run 100, Daily 300; the minimum is 30); **Run** with **Resource URL**.
4. Organisation: Copilot cloud agent on for every repository in agentic-dev-labs · automations
   allowed · Copilot app policy on · an AI-credit budget for about 45 cloud sessions and 45 Reviewer
   runs · Copilot code review stays off.
5. Copilot app updated on your laptop and signed in as **alfarahn**; Codespace of
   `alfarahn-hackaton` warm.

**30 min before:** slides open · tabs: screen link, `github.com/codespaces`, `alfarahn-hackaton`
(**Code**, **Actions**, **Issues**, **Pull requests**, **Settings**, **Agents**), the dry-run repo ·
Codespace open with Chat on **Agent** · Copilot app open, **Projects** visible · helpers know:
**commit all changes**, never a second codespace, and the "What you see" tables in DAY-4.md.

### 00:00-00:15 What's new · slides

| Time  | Who    | Where                                                      | Do                                                                                                                                                                                                                                  | Paste |
| ----- | ------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 00:00 | 🎤 Ali | Slide 1 **Classic SDLC: Linear**                           | **Say:** "This is how software was built: a team, a plan, sprints, and a release date. Work waited for the plan."                                                                                                                  |       |
| 00:02 | 🎤 Ali | Slide 2 **Evolving for the Agentic Era**                   | **Say:** "GitHub's message this week: any event can start software work now. 24 new triggers were just announced: a new ticket, a pull request, a failed check."                                                                |       |
| 00:03 | 🎤 Ali | Slide 3 **The stages stay. The jobs change.**              | **Say:** "We still plan, build, test, review, and release. Agents do more of each step; people decide."                                                                                                                            |       |
| 00:04 | 🎤 Ali | Slides 4-5: the Copilot app, Fusion, Canvases, Dreaming    | One **You get** line per card. Canvases: play the keynote at 9:39 only if on time.                                                                                                                                                 |       |
| 00:07 | 🎤 Ali | Slide 6 **Copilot Projects**                               | **Say:** "A project is mission control for one goal: it starts the work in parallel, remembers, and gives you one inbox. You use one in 45 minutes."                                                                              |       |
| 00:09 | 🎤 Ali | Slide 7 **Copilot Automations**                            | **Say:** "A trigger, a prompt, tools, and a credit limit. You build one after the break."                                                                                                                                          |       |
| 00:10 | 🎤 Ali | Slides 8-10                                                | Quality and security, infrastructure, the future: one sentence each. **Say:** "Agents propose; people decide."                                                                                                                     |       |
| 00:13 | 🎤 Ali | Slide 11 **Your website, version 1.1** → the screen link   | **Say:** "Today you do this chain on your own website: publish with a version, write a ticket, a Copilot project builds it, checks take screenshots, an automation reviews, you merge, and your page shows its version." Rejoin rule. |       |

### 00:15-00:50 Save and publish · attendees: DAY-4.md §1

| Time  | Who          | Where                                                                  | Do                                                                                                                                                                                                                       | Paste                                   |
| ----- | ------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| 00:15 | 🎤 Ali       | Screen link: `DAY-4.md` §1                                             | **Say:** "Most of your websites are still only in your Codespace, not on GitHub. Today one push saves your work, switches on checks and a version number, and publishes your website."                                  |                                         |
| 00:17 | 🤝 Both      | `github.com/codespaces` → their codespace · §1 step 1                  | Open it (about a minute) → Chat → **Agent**. **Say:** "Never create a second one: a new codespace does not have your unsaved work. Two listed? The one you used last."                                                |                                         |
| 00:19 | 🤝 Both      | Codespace › Chat · §1 step 2                                           | Paste → **Allow** each command → open `.github/workflows/publish-website.yml`: the last line says `version: 1.0.0.${{ github.run_number }}`, lined up with `website-name:`. **Say:** "Two switches: checks on every change, and a version on every release." | `Get my repository ready for Day 4. First run python3 scripts/update_from_template.py. Then copy .github/workflow-starters/check-my-website.yml to .github/workflows/check-my-website.yml. Then in .github/workflows/publish-website.yml change the line that starts with "# version:" into "version: 1.0.0.${{ github.run_number }}", with the same indentation. Change nothing else, and tell me in plain words what changed.` |
| 00:23 | 🤝 Both      | Codespace › Chat · §1 step 3                                           | Type → keep the suggested name or type one → it shows the address.                                                                                                                                                       | `/publish-website`                      |
| 00:25 | 🤝 Both      | Codespace › **Source Control** · §1 step 4                             | **File > Save All** → **Changes +** (all of them) → message → **Commit** → **... > Push**. **Say:** "Include everything: this is the moment your work reaches GitHub."                                                  | `Day 4: my website, checks and version` |
| 00:27 | 🎤 Ali       | GitHub › `alfarahn-hackaton` › **Actions**                             | Two runs start: **Publish my website** and **Check my website**. **Say:** "One push, two events: publish and check. Nobody pressed a deploy button."                                                                     |                                         |
| 00:28 | 👥 Attendees | `DAY-4.md` §1 steps 1-5                                                | Their push. Helpers: does **Source Control** list their `site/` files? All included? Push refused for a workflow file → the pencil fallback under **Watch for**.                                                        |                                         |
| 00:38 | 🎤 Ali       | **Publish my website** run → its summary → the address → `/version.json` | **Your website is live**, **Version 1.0.0.N** → open the address → add `/version.json`. **Say:** "Your website knows its version and its environment, Production. The page does not show it yet: that is your ticket." |                                         |
| 00:41 | 🎤 Ali       | **Check my website** run → **UI check** table → **Artifacts** › `home-phone.png` | **Say:** "A browser opened your page on a desktop and a phone. Red is fine today: it says what to look at. From now on these pictures come into every pull request."                                             |                                         |
| 00:43 | 👥 Attendees | `DAY-4.md` §1 steps 6-7                                                | Their address, `version.json`, and first check. Helpers: **That name is taken**; a red publish run (read its message).                                                                                                  |                                         |
| 00:49 | 🎤 Ali       | Room                                                                   | "Hands up: your website is live?" Not yet: a helper sits with them; you move on.                                                                                                                                          |                                         |

### 00:50-01:30 A Copilot project builds your ticket · attendees: DAY-4.md §2

| Time  | Who          | Where                                                                    | Do                                                                                                                                                                                                                                                                                       | Paste   |
| ----- | ------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| 00:50 | 🎤 Ali       | GitHub › **Issues > New issue > Show my version** · §2 step 1            | Read the user story and the three criteria aloud → **Create** → **#1**. **Say:** "One ticket that fits every website: the bottom of your page says where it runs and which version it is."                                                                                              |         |
| 00:52 | 👥 Attendees | §2 step 1                                                                | Their ticket. No **Show my version** in the list? Their §1 push is not on GitHub yet.                                                                                                                                                                                                     |         |
| 00:54 | 🎤 Ali       | GitHub › **Settings > Rules > Rulesets** · §2 step 2                     | **New ruleset > New branch ruleset** → `Protect main` → **Active** → **Add target > Include default branch** → keep **Restrict deletions** and **Block force pushes** → tick **Require a pull request before merging**, approvals **0** → bypass list empty → **Create** → **Confirm access** on your phone. **Say:** "From now on nobody pushes to main, not even you: every change is a pull request." |         |
| 00:57 | 👥 Attendees | §2 step 2                                                                | Their ruleset.                                                                                                                                                                                                                                                                            |         |
| 01:01 | 🎤 Ali       | Copilot app › **Projects +** · §2 steps 3-4                              | **Which repositories should this Project use?** → `alfarahn-hackaton` → **Add repositories** → paste → send → **Overview**: the session is under **Working**. **Say:** "This is mission control from slide 6: one goal, Copilot runs the work, and I watch one inbox."                 | `I want this project to release version 1.1 of my website. Build ticket #1 in my repository in the cloud, as one draft pull request. Change only what the ticket asks for, keep all content made up, and add the test it asks for in checks/. Start the pull request's description with "Closes #1". Do not merge anything. Give me the pull request's link when it is open.` (use the ticket's real number) |
| 01:04 | 👥 Attendees | §2 steps 3-5                                                             | Their project. No **Projects**, or nothing after five minutes → **Assign to Agent** on the ticket (the guide's table).                                                                                                                                                                   |         |
| 01:10 | 🎤 Ali       | Copilot app › **Overview** → the session                                 | Its plan and changes → **Needs input**: answer it → **Steer this session** if useful. **Say:** "When Copilot needs a decision or a permission, it asks me here. I decide."                                                                                                               |         |
| 01:14 | 🎤 Ali       | GitHub › **Pull requests** → the draft · §2 steps 6-7                    | **Files changed**: `site/index.html` and a test → wait until the title has no **[WIP]** → bottom of **Conversation**: **Approve workflows to run**. **Say:** "GitHub runs nothing Copilot wrote until a person allows it."                                                             |         |
| 01:18 | 🎤 Ali       | The pull request › the **UI check** comment · §2 step 8                  | The desktop and phone screenshots; the footer says **Preview**. **Say:** "Every pull request now brings its own screenshots. Preview, because nothing is released yet. Do not merge yet." Copilot slow? Show the dry-run pull request.                                                 |         |
| 01:20 | 👥 Attendees | §2 steps 5-8                                                             | Their pull request, approval, and comment.                                                                                                                                                                                                                                               |         |
| 01:29 | 🎤 Ali       | Room                                                                     | **Say:** "Break. Copilot keeps working while you have coffee."                                                                                                                                                                                                                          |         |
| 01:30 | ☕ Break     | Tables                                                                   | Helpers: stuck sessions → **Assign to Agent**; **Approve workflows to run**; pushes still missing.                                                                                                                                                                                       |         |

### 01:45-02:15 An automation reviews the pull request · attendees: DAY-4.md §3

| Time  | Who          | Where                                                                                       | Do                                                                                                                                                                                                                                                                                       | Paste   |
| ----- | ------------ | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| 01:45 | 🎤 Ali       | GitHub › **Agents > Automations > Create automation > Create manually** · §3 steps 1-6       | **Say:** "Slide 7: a trigger, a prompt, tools, and a limit. Now you build one." Name `Reviewer` → **Personal** → trigger **Ready for review** → **Configured tools can change: Only this issue** → paste the prompt → **Suggest tools**: keep reading and adding a comment → **AI credit limits**: Per run `100`, Daily `300` → **Create automation**. | `You review one pull request on my website. Read the pull request, the files it changes, and the ticket it closes, with its acceptance criteria. Read the newest "UI check" comment from github-actions too, with its desktop and phone screenshots. Then add one comment to the pull request, in plain words for a beginner, that starts with "Reviewer automation:". Give each acceptance criterion one line: Pass, Fail, or Check by hand, and why. Then name anything the pull request changed outside its ticket, and at most three things I should check by hand. End with "Ready to merge" or "Not yet". Never change files, push, approve, merge, or close anything.` |
| 01:52 | 👥 Attendees | §3 steps 1-6                                                                                | Their Reviewer.                                                                                                                                                                                                                                                                          |         |
| 02:00 | 🎤 Ali       | The draft → **Ready for review** → **Agents** (the session starts) → the comment · §3 steps 7-8 | Read the **Reviewer automation:** lines aloud → check one criterion against the screenshot. **Say:** "That click was the event. Nobody assigned the review. It can be wrong: my own check decides." Not a draft? **Run** → **Resource URL** → **Run now**.                           |         |
| 02:04 | 👥 Attendees | §3 steps 7-8                                                                                | Theirs starts; they check each line.                                                                                                                                                                                                                                                      |         |
| 02:14 | 🎤 Ali       | Room                                                                                        | **Say:** "Now the decision is yours: merge or not."                                                                                                                                                                                                                                       |         |

### 02:15-02:45 Merge, release, checkpoint · attendees: DAY-4.md §4

| Time  | Who          | Where                                                                                 | Do                                                                                                                                                                                                                                                  | Paste |
| ----- | ------------ | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 02:15 | 🎤 Ali       | The pull request → **Merge pull request > Confirm merge > Delete branch** · §4 steps 1-3 | "Never **Delete codespace**." → **Actions > Publish my website** (about 3 min) → the bottom of the website: **Production · Version 1.0.0.N** → #1 closed. **Say:** "The merge was the event that released it. The version tells everyone which release they see." |       |
| 02:20 | 👥 Attendees | §4 steps 1-3                                                                          | Merge, publish, the footer, the ticket closed.                                                                                                                                                                                                       |       |
| 02:30 | 🎤 Ali       | **Agents > Automations > Reviewer > Disable** → Codespace › **Source Control > ... > Pull** · §4 steps 4-5 | **Say:** "Every run costs credits: switch off what you do not use."                                                                                                                                                              |       |
| 02:32 | 👥 Attendees | §4 steps 4-6                                                                          | Disable, Pull, and show a neighbour: the project's **Overview**, the pull request with screenshots and review, the merge, the live footer.                                                                                                          |       |
| (if ahead) | 🎤 Ali | A second ticket's pull request says **has conflicts** (optional extra 1) | Comment on that pull request, wait for Copilot's new commit, then merge. **Say:** "Two pull requests changed the same page: Copilot fixes the overlap, you still decide." | `@copilot Resolve the merge conflicts with main. Change nothing else.` |
| 02:40 | 🎤 Ali       | Slide 11                                                                              | **Say:** "A ticket, a project, checks with screenshots, an automation, your merge, a live version: every step started by an event, every decision yours. Tomorrow the checks become required, every pull request gets a test copy of your website, and you approve each release. Push, then stop your Codespace." |       |

**Running late:** 00:28 slow pushes → do the 00:38-00:43 demo while they finish · 00:54 the ruleset
can wait until after the break: it only matters before the merge · 01:01 **Projects** slow or
missing for many → everyone uses **Assign to Agent** on #1 (the same draft pull request) · 01:45
automation late → you build it on screen, they merge after their own check and build theirs as an
extra · 02:15 the merge and **Disable** always happen.

**Watch for**

- **Source Control** lists only today's updates → the website is already on GitHub, or this is a new codespace: check `site/index.html` on GitHub and the other codespaces at `github.com/codespaces`
- Not all changes included → **Changes +**, commit again, push
- The update stops: workshop files not committed → undo that one file, paste the 00:19 prompt again
- Push refused for a workflow file → helper on GitHub: **Add file > Create new file** `.github/workflows/check-my-website.yml` with the starter's text, the pencil on `publish-website.yml` for the version line; then push the rest again
- **That name is taken** → `/publish-website` with another name, commit, push
- Publish red "needs attention" → read its message (missing `index.html`, files too big); never edit the workflow
- **UI check** red on `main` → fine today
- No **Show my version** under **New issue** → the §1 push is not on GitHub
- No **Projects** in the app → update the app; else **Assign to Agent**
- A session waits → **Needs input**: answer it
- Pull request without checks → **Approve workflows to run**; title still **[WIP]** → wait
- No screenshot comment → **Actions > Check my website > Screenshots** log; the pictures are also under **Artifacts**
- Broken pictures in the comment → signed out, or another account
- The Reviewer never starts → was it a draft? Trigger **Ready for review**; else **Run** with **Resource URL**; per-run limit at least 30
- Footer still **Preview** after the merge → reload; else the `version:` line still has its `#`
- Ticket still open → **Close issue**
- **Delete codespace** offered → never
- Real names or work data anywhere → everything stays made up

**Tonight (Thursday to Friday):** Friday assumes the checks, the ruleset, a version and a Copilot
pull request: see how far the room got and plan Friday's catch-up · disable your own demo
automations · githubstatus.com for **Actions**.

## Friday

30 Oct · 4 h, times from the start · guide: **docs/DAY-5.md** · phone at hand · your address
`https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io` (`<name>` = `websiteName` in
`config.json`; feature slot = `<name>-feature`) · prepared red run in your spare copy

| Time  | Who              | 📄 Attendees' file                   | Cue                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----- | ---------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 00:00 | 🎤 **Ali**       | **DAY-5.md §1** CI/CD in Plain Words | "Joining today? A helper starts you at the top of the Day 5 guide." → rejoin rule                                                                                                                                                                                                                                                                                                                                                                                       |
| 00:02 | 🎤 **Ali**       | DAY-5.md §1                          | "CI: every change built and tested automatically. CD: every checked change ready to publish. Deployment: here a person approves first."                                                                                                                                                                                                                                                                                                                                 |
| 00:10 | 🎤 **Ali**       | DAY-5.md §1                          | `.github/workflows/publish-website.yml`: `on:` (when it runs) · `permissions:` (what it may do) · `version:` (build number)                                                                                                                                                                                                                                                                                                                                             |
| 00:14 | 👥 **Attendees** | DAY-5.md §1                          | The three lines in their own file                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 00:18 | 🎤 **Ali**       | DAY-5.md §1                          | Only if on time: Agentic Workflows demo (public preview)                                                                                                                                                                                                                                                                                                                                                                                                                |
| 00:19 | 🎤 **Ali**       | DAY-5.md §1                          | "Since Thursday your checks run on every pull request. Today they become required."                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 00:20 | 🎤 **Ali**       | **DAY-5.md §2** Workflow Lab         | `copilot` → paste `Explain .github/workflows/check-my-website.yml in plain sentences: what starts it, what each job may do, and what each job does. Change nothing.` → in the file: `on:` (pull_request, push to main, workflow_dispatch) · `permissions: contents: read` · only **Screenshots** may write. "Only the job that runs none of the pull request's code may write."                                                                                                                                                                                                                                                                                                                            |
| 00:25 | 👥 **Attendees** | DAY-5.md §2                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 00:37 | 🎤 **Ali**       | DAY-5.md §2                          | **Actions > Check my website > Run workflow > Run workflow** → both checks green in about 3 min. "That button is the workflow_dispatch trigger."                                                                                                                                                                                                                                                                                                                                           |
| 00:40 | 👥 **Attendees** | DAY-5.md §2                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 00:44 | 🎤 **Ali**       | DAY-5.md §2                          | **Settings > Rules > Rulesets > Protect main** → **Require status checks to pass** → **Add checks**: **Check the website** + **UI check** → **Save changes** → **Confirm access**. "They appear only after they have run once."                                                                                                                                                                                                                                         |
| 00:46 | 👥 **Attendees** | DAY-5.md §2                          | Their checks required                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 00:49 | 🎤 **Ali**       | DAY-5.md §2                          | "Now break it on purpose."                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 00:50 | 🎤 **Ali**       | **DAY-5.md §3** CI Lab               | Branch `try-ci` → paste `Add a banner that says Sale at the very top of my first page, above its header. This is a test, so make it 900 pixels wide on every screen, even a phone: use min-width: 900px and do not let it shrink. Change nothing else.` → remove any `max-width` → commit, **Publish Branch**, PR · meanwhile the prepared red run: **UI check** red, **Merge** blocked → **Details**: "Wider than a phone screen" → the pull request's **UI check** comment: the phone screenshot (also **Summary > Artifacts > home-phone.png**) → `Why did the UI check on my pull request fail? Read its log and explain in two sentences.` → `Remove the banner you just added.` → push → green → merge → `main` → **Pull**. "Red is information, not failure." |
| 01:00 | 👥 **Attendees** | DAY-5.md §3                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 01:20 | 🎤 **Ali**       | DAY-5.md §3                          | Next ticket under **Issues** (none? **Issues > New issue > Requirement**: `Show a short welcome line under my headline`) → **Assign to Agent** (or the Copilot project) → **Assign**. "Copilot builds it during the break."                                                                                                                                                                                                                                                                                    |
| 01:22 | 👥 **Attendees** | DAY-5.md §3                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 01:26 | 🎤 **Ali**       | DAY-5.md §3                          | "Hands up: saw red? opened the phone screenshot? merged on green? a ticket with Copilot?"                                                                                                                                                                                                                                                                                                                                                                               |
| 01:29 | 🎤 **Ali**       | DAY-5.md §3                          | "Break. Next: a test copy for every PR, and nothing reaches production until you approve."                                                                                                                                                                                                                                                                                                                                                                              |
| 01:30 | ☕ **Break**     | —                                    | Helpers: required checks, stuck runs, tickets with Copilot                                                                                                                                                                                                                                                                                                                                                                                                              |
| 01:45 | 🎤 **Ali**       | **DAY-5.md §4** CD Lab               | "Two slots: feature slot = test copy per PR; production = your own address." → branch `slots` → paste `Copy .github/workflow-starters/deploy-feature-slot.yml to .github/workflows/deploy-feature-slot.yml, and copy .github/workflow-starters/publish-website-with-approval.yml over .github/workflows/publish-website.yml. Then explain in plain sentences what starts each workflow and what it may do. Change nothing else.` → show the **Wait for approval** job and `version:` line → PR → merge on green → **Settings > Environments > New environment** `production` → **Configure** → **Required reviewers**: you → **Save protection rules**                                                                                                                                     |
| 01:50 | 👥 **Attendees** | DAY-5.md §4                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 01:57 | 🎤 **Ali**       | DAY-5.md §4                          | Copilot's PR → **Files changed** first → **Approve workflows to run** ("nothing Copilot wrote runs until you say so") → **Actions > Deploy feature slot** → **Action required** → **Approve and run** (~3 min) → PR **View deployment**: yellow strip → check criteria → run `python3 scripts/smoke_test.py https://<name>-feature.thankfulrock-bf005377.eastus.azurecontainerapps.io` → note the **content** number. "Your own PRs skip both approvals."                                                                                                                 |
| 02:03 | 👥 **Attendees** | DAY-5.md §4                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 02:14 | 🎤 **Ali**       | DAY-5.md §4                          | **Files changed > Submit review > Approve** (say what you tested) → **Ready for review** → **Merge** → **Actions > Publish my website**: **Waiting** → **Review deployments** → tick **production** → **Approve and deploy** → run `python3 scripts/smoke_test.py https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io` on your own address: same **content**. "Production got exactly what you tested."                                                                                                                                             |
| 02:17 | 👥 **Attendees** | DAY-5.md §4                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 02:27 | 🎤 **Ali**       | DAY-5.md §4                          | "Hand up when production shows Copilot's change with the same content number."                                                                                                                                                                                                                                                                                                                                                                                          |
| 02:29 | 🎤 **Ali**       | DAY-5.md §4                          | "Now ship a bad release on purpose, and bring the good one back."                                                                                                                                                                                                                                                                                                                                                                                                       |
| 02:30 | 🎤 **Ali**       | **DAY-5.md §5** Recovery Lab         | Run `python3 scripts/smoke_test.py https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io --expect-text "<the sentence under my headline>"` → all PASS → note **content** and **version**: "The fingerprint of your good version."                                                                                                                                                                                                                                                                                                                                                                      |
| 02:33 | 👥 **Attendees** | DAY-5.md §5                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 02:38 | 🎤 **Ali**       | DAY-5.md §5                          | New branch → `Change the sentence under my headline to Oops, wrong words. Change nothing else.` → PR green, **View deployment** shows it ("where a tester catches it") → merge anyway → approve → the same smoke test: FAIL. "Test before and after every release."                                                                                                                                                                                                                 |
| 02:42 | 👥 **Attendees** | DAY-5.md §5                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 02:55 | 🎤 **Ali**       | DAY-5.md §5                          | Merged PR → **Revert** → **Create pull request** → green → merge → approve → the same smoke test: PASS, same content, higher version. "Revert is your rollback."                                                                                                                                                                                                                                                                                                                    |
| 02:58 | 👥 **Attendees** | DAY-5.md §5                          | The same                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 03:12 | 🎤 **Ali**       | DAY-5.md §5                          | "Each table: one screen, one speaker, three minutes."                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 03:15 | 👥 **Attendees** | **DAY-5.md §6** Team Demos           | Team demos by table, volunteers first, timer on screen: a ticket and its criteria, the Reviewer's comment (one point agreed, one checked differently), red then green, feature slot, approval, version, rollback                                                                                                                                                                                                                                                                                                 |
| 03:44 | 🎤 **Ali**       | DAY-5.md §6                          | "Last step: hand it over."                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 03:45 | 🎤 **Ali**       | **DAY-5.md §7** Handoff              | Paste `Write HANDOFF.md in plain words: the skills, agents, and plugins I made or installed, my Copilot project and my Reviewer automation (what starts it, what it may do, and its credit limits), how a ticket becomes a reviewed pull request, my ruleset (what it requires before a merge), my pipeline (Check my website with its tests, UI check, and screenshots, Deploy feature slot for every checked pull request, and Publish my website to production with approval and a version number, and what starts each), how to release and how to roll back with Revert, who owns releases (me), and open questions for IT. Add a short 'To make it real' list: which parts are made up or only in my browser today, and the route for each from the table in docs/DAY-5.md.` → read it, correct one sentence → branch, PR, merge → the guide's "To make it real" table: Power Apps, Power Automate, Power BI, Copilot Studio, Novo's GitHub Enterprise, Novo's validation for GxP                                                                                                                                                                                                                                                      |
| 03:48 | 👥 **Attendees** | DAY-5.md §7                          | HANDOFF.md merged · any automation switched off                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 03:57 | 🎤 **Ali**       | DAY-5.md §7                          | Thank the room → "Push, then stop your Codespace at github.com/codespaces."                                                                                                                                                                                                                                                                                                                                                                                             |

**[A]** 00:20

```text
Copy .github/workflow-starters/check-my-website.yml to .github/workflows/check-my-website.yml. Then explain each job and step in one plain sentence. Do not change anything else.
```

**[B]** 00:20, the top of the file afterwards

```yaml
on:
  workflow_dispatch:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read
```

**[C]** 00:50, the banner

```text
Add a banner that says Sale at the very top of my first page, above its header. This is a test, so make it 900 pixels wide on every screen, even a phone: use min-width: 900px and do not let it shrink. Change nothing else.
```

**[D]** 01:45, the slots

```text
Copy .github/workflow-starters/deploy-feature-slot.yml to .github/workflows/deploy-feature-slot.yml, and copy .github/workflow-starters/publish-website-with-approval.yml over .github/workflows/publish-website.yml. Then explain in plain sentences what starts each workflow and what it may do. Change nothing else.
```

**[E]** 01:57, smoke-test the feature slot

```bash
python3 scripts/smoke_test.py https://<name>-feature.thankfulrock-bf005377.eastus.azurecontainerapps.io
```

**[F]** 02:30-02:55, smoke-test production

```bash
python3 scripts/smoke_test.py https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io --expect-text "<the sentence under my headline>"
```

**[G]** 03:45, the handoff

```text
Write HANDOFF.md in plain words: my agent profiles (user-requirements and code-review: file, job, and how to run them), my travel-planner skill and the plugins I installed, my board and how a ticket moves from Todo to Done, my review rules, my ruleset (what it requires before a merge), my pipeline (Check my website with its tests and UI check, Deploy feature slot for every checked pull request, and Publish my website to production with approval and a version number, and what starts each), how to release and how to roll back with Revert, who owns releases (me), and open questions for IT. Add a short 'To make it real' list: which parts are made up or only in my browser today, and the route for each from the table in docs/DAY-5.md.
```

**Running late:** skip Agentic Workflows · 00:50 runs slow → show the prepared red run, they catch
up in the break · 01:57 no Copilot PR → they open their own small one (no approvals) and watch
yours · 02:30 they may skip the oops release; you show it and the **Revert** · demos 3 min each,
volunteer tables first.

**Watch for**

- No **Approve workflows to run** yet → Copilot still working (title starts [WIP]): wait for "Copilot finished work"
- No **View deployment** after green checks → **Actions > Deploy feature slot** waits for **Approve and run**
- Feature slot shows another PR → last one checked wins; the strip names it
- Banner leaves **UI check** green → it went inside the header, or Copilot added `max-width: 100%`
- **Check the website** / **UI check** missing from **Add checks** → they appear after one run
- Slow **UI check** → githubstatus.com, carry on, never re-run in a loop
- Red **UI check** on an untouched page → open `home-phone.png`, re-run once
- Typing lands in the editor after a CLI diff → click in the terminal first
- Oops PR blocked by a Day 3 test → "your tests caught it", pick another sentence
- Older **Deploy feature slot** run asks again after merge → leave it

## Preparation

- [ ] Template `main` green: `gh run list -R agentic-dev-labs/copilot-hackathon-template -L 1` (copies come from GitHub, not your laptop)
- [ ] Org: allowed models · AI-credit budget (~10 requests per `/create-website`, ~10 credits per `/publish-website`) · Codespaces paid by org, budget, 30-min idle · cloud agent on before Thu · code review off
- [ ] Friday red run ready: spare copy with checks merged, PR with the 900 px banner
- [ ] Version footer live on a practice site before Thursday
- [ ] Print `docs/QUICK-REFERENCE.md` for every table
- [ ] `MIN_REPLICAS: 1` in `website-publisher.yml` this week = websites always on, no wake-up wait (≈ USD 15/day for 80 sites) · back to 0 after the week · hosting fits 80 attendees plus Friday's feature slots (40 of 500 cores); registry Standard
- [ ] Hosting awake: container app `keep-warm` running in `cae-hackathon` (never delete it this week) · a publish that fails with "Azure is still starting" → wait 10 min → **Re-run all jobs**

**Evenings:** Monday, publish your copy if you skipped it at 14:20 · Wednesday and Thursday: see
**Tonight**.

**After the week** (agree each step with David): remove attendee members, cancel invitations ·
archive repos, delete published websites (including `showcase` and its repo `workshop-showcase`) and `keep-warm` · `MIN_REPLICAS` back to 0 · Thursday automation off ·
`FOUNDRY_*` client secret expires 1 Nov: renew or delete.
