# What to Show and When

Your script for the whole week. Everything you show, type and say is here, with the page the
attendees follow.

**How it works.** You show a step on your screen while they watch. Then it is **their turn**: they
do the same on their own copy, from the page named after the **·** in the heading. Say that page
out loud. Words in quotes are what you say. Text in `grey` or in a box is what you type or paste,
exactly.

**Cut on time.** At each **Cut** everyone moves on, finished or not. Anyone stuck moves on with the
room, and a helper catches them up in the next turn or the break. Helpers point; they never type
on an attendee's keyboard.

**The rejoin rule.** Say it on Monday at 10:45 and at the start of every later day: "Lost? Find the
row we are on in your guide's route table, open its link, and start there. Raise your hand."

**Every morning, 30 minutes before**

- Your demo Codespace open and warm, browser zoom about 150%, notifications off. Your own MCP
  servers off in it (**MCP: List Servers**, each one, **Disable**), so your Chat looks like theirs.
- The day's guide open in a tab, and this script on a second device or printed.
- Five minutes with the helpers: their tables, the rejoin rule, and the day's **Watch for** list.

Jump to: [Monday](#monday) · [Tuesday](#tuesday) · [Wednesday](#wednesday) ·
[Thursday](#thursday) · [Friday](#friday) · [Preparation](#preparation)

## Monday

**Day 1: GitHub and your first app.** 26 October, 09:00-15:00, rooms MKC 1D412 and 1D413. Until
the break they follow their repository's **README**; from 10:45, **docs/START-HERE.md**. The
headings are David's slide.

### 09:00-09:30 Sponsor welcome, ASTER teaser, glossary and GitHub basics

**09:00 Welcome** · they listen. David: the sponsor's SEFR video, then HZRW's ASTER Overview
teaser.

**09:15 This is GitHub** · they watch (README, "This Is GitHub"). On the template:

1. The files, and the README under them: "A repository is a project folder with a memory. Every
   snapshot you send up stays, and you can go back to it."
2. **Commits**, next to the clock: every snapshot. Open a file, then **History**. Press **/** to
   search. **Issues**: "To-do notes. On Wednesday you write your own, and on Thursday Copilot
   picks one up."
3. The five words on the README: repository, Codespace, Copilot, commit, push. "Saving keeps it on
   your screen; pushing sends it to GitHub. The order is always save, review, commit, push."

**09:28 Cut:** "Now you make your own copy, one click at a time, with me. Make exactly one."

### 09:30-10:00 Lab: Find files and Copilot Chat, ask and refine a question

**09:30 Your own copy** · they click along with you (README steps 1-2).

1. On the template: **Use this template > Create a new repository**.
2. **Owner** agentic-dev-labs, **name** your GitHub username, **Private** (it may start on
   Internal). Leave the rest, including **Jumpstart**. **Create repository**.
3. Point at the top: "agentic-dev-labs, your name, Private. Anything else, or no agentic-dev-labs
   in the list? Hand up." Then **Commits**: "Your first snapshot. Everything you make this week
   lives here."

**09:37 Your Codespace** · they click along with you (README steps 3-4).

1. **Code > Codespaces > Create codespace on main**, about a minute. "Never create a second one."
2. **Trust Folder & Continue**: "It is your own copy, and your website preview needs it."
3. Right-click **README.md** in the Explorer, **Open Preview**: "The same page, in your Codespace."
4. A banner about migrating customizations, or a Python or Ruff message? "Select X. Never Migrate."

**09:42 Ask: same question, different answers** · README steps 5-6.

1. The menu (three lines, top left), **View > Chat**, then **Ask** in the list at the bottom of the
   chat box: "Ask only answers. It never changes your files." Only **Agent** in the list, or
   **Sign In** at the bottom right? "Select Sign In once."
2. "Everyone asks exactly the same thing. Watch mine first." Type this and read the name out:
   `Invent a fun name for my workshop table. Reply with the name only.`
3. **Their turn.** Then: "Same name as your neighbour? Hands up." Many hands: "A likely name comes
   up often, but not always." Few: "Same question, different answers." Then: "Copilot does not
   look the name up. It writes a new answer each time. That is why we always check its work."

**09:48 Ask, then ask better** · README steps 7-8.

1. "Stay in this one chat all day. Never press New Chat."
2. Type `What is in the docs folder?` Open **docs** in the Explorer and compare.
3. Type `Say that as 3 short bullets for a beginner.` "I did not start over. I told it what I
   wanted."
4. **Their turn**, about three minutes. Helpers finish any copy or Codespace still missing.

**09:52 Ask cannot change files; then GenericAgent gets the web and becomes a Joker** · they
watch. They make their own agents on Wednesday; helpers keep finishing copies meanwhile.

1. Still in **Ask**, type `Please rewrite my README file, but much shorter.` It shows a shorter
   version in Chat, but the file stays the same: no **Keep** or **Undo** appear, and no **M** next
   to **README.md** in the Explorer. Never select **Apply** on its answer. "Ask only answers. It
   cannot change your files or do anything else for you."
2. In the same list, choose **GenericAgent**: "Every copy has this blank helper." Send this. It
   says it cannot go online:

   ```text
   What is the temperature in Princeton right now? Read https://api.open-meteo.com/v1/forecast?latitude=40.35&longitude=-74.66&current=temperature_2m&temperature_unit=fahrenheit
   ```

3. Open **Explorer > .github > agents > generic-agent.agent.md**: "The top decides what it can do.
   Now it can only read and search." In `tools`, after `"search"`, type a comma and a space, press
   **Ctrl+Space** and pick **web** (no list? type `"web"`). Save.
4. Still on GenericAgent, send the same question again. Select **Allow** twice: to visit the site,
   then to use what it read. Now it gives today's temperature. "Fresh data. The web tool reads a
   page you name; it is not a search engine. Check it against your phone."
5. Pick **Agent** and send this. **Allow** if it asks, then **Keep**. "Agent can change files. The
   words below the top decide how this helper behaves."

   ```text
   Turn GenericAgent into Joker: rename it Joker and make it end every reply with one short, clean joke. Keep its tools.
   ```

6. Pick **Joker** and type `Which rules do you follow in this repository? Three short bullets.` A
   joke at the end. Open **.github/copilot-instructions.md**, **Ctrl+F**, type `secrets`: "Never
   put credentials or secrets in code. Copilot reads this file before every chat, whichever agent
   you pick."

**09:59 Cut:** "Switch Chat from Ask to Agent. Agent can change your files, and you check every
change."

### 10:00-10:30 Create an idea note, save, review, commit, push and verify

**10:00 Your first website** · README, "Your First Website", steps 1-3.

1. Pick **Agent** (not Joker). Type `/create-website`, pick it from the list, press Enter.
2. Choose **Project Planner**: "Pick any. Not sure? The Project Planner." About a minute: talk over
   it.
3. It asks to run `python3 scripts/website_preview.py start`? "That opens your preview: Allow.
   Anything else you do not understand: hand up."
4. It opens beside Chat. Press **+** and add a made-up task. Point at **Explorer > site >
   index.html**: "You built a website by talking. The file is the proof, not Copilot saying done."
5. **Keep** under the chat box: "Keep accepts the change. Undo takes back everything you have not
   kept, so keep what you like."
6. **Their turn.**

**10:15 The idea note and your first push** · README, "Your First Website", steps 4-5.

1. Open **site > brief.md**: "This is the idea note on David's slide. Copilot wrote it; you add to
   it all week."
2. **File > Save All** (grey means already saved), then **Source Control**: "About 30 files the
   first time: your page and its pictures, fonts and styles." Yours also lists your agent file;
   theirs will not.
3. Hover over **Changes**, select **+**, type `Add my first website`, **Commit**, then
   **... > Push**.
4. On GitHub in a new tab: **site > brief.md** is there. "Push rejected, or a conflict? A helper.
   Never force a push."
5. **Their turn.**

**10:28 Cut:** "Break. Not on GitHub yet? Stay seated: a helper finishes it with you now."

### 10:30-10:45 Break

Switch to the warm Codespace of your prepared websites. Helpers check that every page is on
GitHub.

### 10:45-11:45 Lab: Create a website with /create-website and preview it

**10:45 More websites** · they watch (Lab 01, section 1).

1. Open **docs > START-HERE.md > Open Preview**: "From now on this is your guide, and I name the
   section every time." Then the rejoin rule.
2. Your prepared websites, saying they are prepared: Weather (drag the 3D chart), Princeton Map
   (the History filter, then 3D), Photo Studio (the sleepy cat becomes a watercolor), Lab Chase
   (20 seconds, then get caught by a meeting invite). "All of these were made the way you made
   yours: by describing them."

**10:55 Peek inside the code** · Lab 01, section 2. Back in your live Codespace.

1. Open **site > index.html**: "Only text." Select about five lines near the top and type:
   `Explain the lines I selected in plain English, one short sentence per line. I have never seen code before.`
2. **Ctrl+F**, `<h1>`. Change two headline words by typing; leave `<h1>` and `</h1>` alone.
   **File > Save**: the preview updates. "Code is only text, and you just changed it with your own
   hands. Broken? Ctrl+Z, then save."
3. **Their turn.**

**11:10 One more idea** · Lab 01, section 3.

1. Type `/create-website` again. It asks what you would like: `build my own idea`. Then:
   `A tracker for team requests with stages Submitted, Doing and Done.` Under two minutes: "It
   gets its own folder in site/ideas. Your first page stays exactly as it is."
2. Type `Make the headline friendlier. Leave the rest alone.` Then **Keep**.
3. **Their turn.** Helpers watch for Copilot changing the first page.

**11:30 Save and show** · Lab 01, section 4. **File > Save All**; **Source Control** lists only
what changed; a short message, **Commit**, **... > Push**; the idea's folder on GitHub. **Their
turn**, then they show a neighbour.

**11:44 Cut:** "Eyes up. Now you are the checker."

### 11:45-12:15 Trust but verify: check a button and a figure, fix and recheck

Lab 01, "Coached Verification Block".

1. **A button.** `/start-website` opens your first page. Type
   `Add a button that hides finished tasks.` "I expect the ticked task to disappear." Click it
   twice and compare. Right? **Keep**. Wrong? `I expected ..., but I saw ...` "Copilot saying it
   works is not a check." **Their turn.**
2. **A number** (11:55). Count it yourself: four example tasks plus this morning's, one ticked:
   **1 of 5 done**. Tick one: **2 of 5**. "Never trust a number you have not checked." **Their
   turn**, with the table in their lab.
3. **Write it down** (12:05). In **site/brief.md**: what you tried and what happened. Save, commit,
   push. **Their turn.**

**12:14 Cut:** "Lunch. Push first; your Codespace waits for you."

### 12:15-13:00 Lunch

### 13:00-14:00 Lab: Add a useful interaction, personalize and check

**13:00 A chart** · Lab 02, sections 1-2.

1. "Pick one: a chart, a chat or a picture. A chart if unsure."
2. Type `/add-chart`, then pick **Progress gauge** or the 3D **Week skyline**. About a minute; if
   it asks whether you can see it, **Yes**. Drag the 3D chart, then **Keep**.
3. Mention `/add-chat` (ask it "How many tasks are done?") and a picture ("the picture model may
   vary when the whole room asks at once"). **Their turn.**

**13:20 Check it** · Lab 02, section 3. "I expect one more done." Tick a task: the count and the
chart move together. Untick it: both go back. "A chart, and a chat, can be wrong too: count it
yourself." **Their turn.**

**13:35 Your own look** · Lab 02, sections 4-5.

1. Type this, then **Keep**:
   `Keep the page light. Try a sky blue look. Keep the text easy to read and leave the content and features unchanged.`
2. Type `Make the whole page bright purple with giant text.` Then **Undo** and **Yes**: "Undo takes
   back everything you have not kept. That is why we kept the chart and the look first. You can
   always go back."
3. **Their turn** (13:39). At 13:50 they write in **site/brief.md** what they tried, and show a
   neighbour.

**13:59 Cut:** "Now we save it and look back in time."

### 14:00-14:45 Lab: Save, share and keep building (publication optional)

**14:00 Copilot writes the message** · Lab 08, sections 1-2.

1. Save. In **Source Control** read what changed, and select **+** on each file you checked.
2. The **sparkle icon** in the message box. Fix one word, **Commit**, **... > Push**. "Read what it
   wrote: you sign it." **Their turn.**
3. 14:10, on GitHub: **Commits** (a narrow window shows only the clock), then **Add my first
   website**: green added, red removed. Then **site > index.html > History**: "A time machine for
   your work." **Their turn.**

**14:20 A challenge** · Lab 08, sections 3-4.

1. The challenge card: Bronze, Silver, Gold. **Their turn.**
2. Publish your own live copy now, because Thursday needs its address: `/publish-website`, accept
   the name, save, commit, push. Live in about three minutes. For them it is optional, with a
   helper (Lab 08, "Optional extras").
3. 14:35: open your published page a minute early (a sleeping page takes about 30 seconds to wake)
   and put it on screen: the room opens it on their phones.

**14:44 Cut:** "Pair sharing: one feature, and how you checked it."

### 14:45-15:00 Pair sharing and selected volunteer demonstrations

1. Pairs share while you pick two or three volunteers; then the volunteers on the big screen,
   about two minutes each.
2. **14:58 Cut:** "Push, then stop your Codespace: github.com/codespaces, **...**, **Stop
   codespace**. Closing the tab does not stop it. Tomorrow the green Code button reopens the same
   one."

**Running late?**

- 09:52: do step 1 only, then the Cut. The GenericAgent part is the only extra not on David's
  slide.
- 09:42: skip their own table names; they saw yours.
- 09:30 runs over: finish the first websites in the break with helpers. Never cut Lab 01.
- 10:45: show two prepared websites, Weather and Lab Chase.
- 13:00: skip the picture mention. 14:20: publish your copy in the evening instead.

**Watch for**

- No agentic-dev-labs in the owner list: not in the organization yet. The welcome desk.
- A second repository or Codespace: a helper sorts out which one to keep.
- **Trust Folder** declined: **Reload Window**, then trust.
- **Sign In** at the bottom right, or only **Agent** in the list: **Sign In** once.
- No **Keep** or **Undo**, and **Copilot** or **Manual permissions** at the bottom of Chat: they
  pressed New Chat. Back to the first chat, or a new one with **Local** chosen before typing.
- Still in **Ask** at 10:00: pick **Agent**.
- The preview closed: `/start-website`, or `/start-website <folder>` for an idea.
- Copilot changed the first page instead of making a folder: **Stop**, **Undo**, then
  `Build my own idea in its own folder.`
- **Undo** also removed the chart or the look: they were not kept. Ask again, then **Keep**.
- A `COMMIT_EDITMSG` tab: the message was empty. Close it, type the message in the box, commit.
- "Codespace is stopped" after lunch: **Restart codespace**, about a minute, nothing lost.
- The page's **Ask** bubble says the assistant is off: add a chart instead and tell a helper.
- Real names or data anywhere: everything stays made up.

## Tuesday

**Day 2: Your own business idea.** 27 October, 09:00-15:00, rooms MKC 1D412 and 1D413. David,
Jackie and Bill Leeson present; you help at the tables. Their guide: **docs/DAY-2-BUILD.md**.

### 09:00-09:30 David: Business/IT roles, approved tools and AI marketplace

They listen. Note questions to take to the tables.

### 09:30-10:30 Jackie: Power Platform, Dataverse and connector examples

They listen.

### 10:30-10:45 Break

Every table reopens Monday's Codespace: the green **Code** button, **Codespaces**, its name. Never
**Create codespace**.

### 10:45-11:45 Supported own-idea build with fictional local data · "Morning Build"

**10:45** The host restarts the room: "Open docs/DAY-2-BUILD.md, Morning Build. Tell your helper
your four answers. Lost later? Find the row for the time now."

1. **Four answers** (10 minutes, no files yet): who it is for, what they should be able to do, the
   smallest first version, and how they will check it.
2. **Build** (35 minutes): Monday's idea with `/start-website <folder>`, or a new one with
   `/create-website` and one sentence, in its own folder in `site/ideas/`. Nudge each idea towards
   a pattern that builds well: "Describe it as a tracker of ... with stages ..." or "a dashboard
   of ... by ... per month". Each attendee's idea and where to start:
   `archive/facilitator/ideas/TABLE-SUPPORT.md`.
3. **11:30, at every table:** "Save and push now: Bill starts at 11:45."

### 11:45-12:15 Bill Leeson: Building a Project Brain

They listen.

### 12:15-13:00 Lunch

### 13:00-14:00 Open build: improve an interaction, check behaviour and get help · "Improve One Interaction"

Help each person add one form, filter or choice, then check one thing at a time: clearer words (a
neighbour tries it), an empty box adds nothing, a filter or count matches the entries, and it works
with a keyboard and in a narrow window. "Expect, try, compare, improve, repeat." No CLI or MCP
today.

### 14:00-14:45 Supported building, fixes and optional assisted publication · "Fixes and Optional Publishing"

One fix at a time, checked again, then save, commit and push. Help anyone who wants to publish
with `/publish-website` (Lab 08's optional route). The preview is enough to finish.

### 14:45-15:00 Volunteer demonstrations and next step with the technical owner · "Show and Plan the Next Step"

1. The host runs the volunteers. Everyone writes their questions for IT: real data, access,
   systems, approval.
2. **14:52, at every table:** two or three wishes, one sentence each, under a heading **Next** in
   their idea's brief; save, commit, push. "These are Wednesday's tickets."
3. "Push, then stop your Codespace."

**Watch for**

- An own idea replacing Monday's page: it belongs in its own folder in `site/ideas/`.
- Real names or data in pages or prompts.
- Integration wishes (Outlook, PDFs, SharePoint, Access): onto the questions for IT, not into the
  page.
- Anyone leaving without **Next** wishes: they are Wednesday's tickets.

## Wednesday

**Day 3: VS Code and a Requirements agent.** 28 October, four hours; times count from the start.
MUKQ opens, then you. Their guide: **docs/TOOLS-PRACTICE.md**. Your demo website is your Monday
live copy: you do on it exactly what they do on theirs. A helper starts anyone without a website
(the guide's **No website yet?**).

### 00:00-00:20 MUKQ: Global and Microsoft perspectives on AI development

They listen. Ready on your screen: your demo website on GitHub, and its Codespace.

### 00:20-00:50 Ali: workspace setup, repo walkthrough and agent roles/tools · section 1

**00:20 A board** · section 1, steps 1-2. The rejoin rule, then: "Your Tuesday wishes become
tickets today, on your own board."

1. On your repository's page select the organization's name (before the slash), then **Projects >
   New project > Board**. Name it `<your username> website`. Keep **Import items from
   repository**, set **Repository** to your own (it shows the template first), **Create project**.
2. **Workflows > Item added to project > Off**: "Otherwise every new ticket lands straight in Todo,
   and approving is your job. Todo means approved, In Progress being built, Done finished." From
   now on, open the board from your repository's **Projects** tab.
3. **Their turn** (00:24). Helpers check each board names their own repository and the workflow
   is Off.

**00:31 A ticket** · section 1, steps 3-4.

1. **Issues > New issue > Requirement**. Title `Mark urgent tasks`; **What I want** in one or two
   plain sentences; **Which page** stays `site/index.html`; **Create**. It is #1, under **No
   Status** on the board. "A ticket is one thing you want next. Your agent adds the details later."
2. **Their turn** (00:34): two or three tickets from their **Next** wishes. You write two more
   meanwhile: `Highlight today's column` (#2) and `Add a Saturday column` (#3).

**00:39 Copilot in the terminal, and a tool** · section 1, steps 5-7.

1. The menu, **Terminal > New Terminal**, make it tall (**Maximize Panel Size**), type `copilot`.
   A model name on the bottom line means it is signed in. Otherwise `/login`, the first option,
   and the code at github.com/login/device.
2. Type this, then point at **List issues** above the answer:
   `Use the GitHub tools to list the open issues in my repository, with their numbers. Do not change anything.`
   "That is MCP, a plug that lets Copilot act on GitHub. Reading runs straight away; anything that
   changes something asks first. The same assistant as Chat, through another door."
3. "Ask answers. Agent changes files. A custom agent is a helper with one job. Tomorrow the cloud
   agent works on GitHub by itself."
4. **Their turn** (00:42). Anyone stuck in the terminal: the same sentence in Chat with **Agent**.

**00:49 Cut:** "Keep the terminal open. Eyes up: now you write your own helpers."

### 00:50-01:30 Build a User Requirements agent: instructions and output format · section 2

**00:50 The building blocks** · section 2, steps 1-2. They watch.

1. Open `.github/skills/create-website/SKILL.md`: "Remember /create-website? This is its recipe,
   mostly plain sentences. Today you write your own, much shorter."
2. In the Explorer: `.github/copilot-instructions.md` (instructions: standing rules),
   `.github/skills/` (a skill: a recipe, how), `.github/agents/` (an agent: a role card, who) and
   `.vscode/mcp.json` (tools: plugs). "Remember Monday's Joker? Today's agent gets a real job."
3. In the terminal type `/agent`: your Joker (theirs shows GenericAgent). **Esc**.

**00:56 The skill** · section 2, steps 3-4. Paste:

```text
Create a skill at .github/skills/user-stories/SKILL.md with name: user-stories and a description that says it turns one ticket for my website into a user story with acceptance criteria. Its steps: read the ticket's What I want and Which page; write one user story as "As a ..., I want ..., so that ..."; under it write 2 or 3 acceptance criteria as "Given ..., when ..., then ..." that a person can check by clicking or counting, each with a checkbox; list open questions instead of guessing. Its output fills the ticket's User story and Acceptance criteria sections, followed by Open questions. Made-up people and data only.
```

1. It asks to read **docs.github.com**: "GitHub's own help: choose 2, for the rest of this
   session." It shows the new file: **Yes**.
2. Open **SKILL.md**: "The name and description decide when Copilot loads it." Change one step
   into your own words; save.
3. **Their turn** (00:59).

**01:09 The agent** · section 2, steps 5-6. Paste:

```text
Create a custom agent file at .github/agents/user-requirements.agent.md with name: user-requirements and a one-line description. It is a User Requirements agent for my small website about a project planner. When I name a ticket by its number, it reads the ticket with the GitHub tools and uses the user-stories skill to draft its user story and acceptance criteria. It shows me the draft first. Only when I say yes does it update that ticket with the gh issue edit command: it reads the ticket's exact text with gh issue view NUMBER --json body --jq .body, changes only the User story and Acceptance criteria sections, keeps every other line exactly as it is, and gives the new text to gh issue edit NUMBER --body-file - through standard input, so quotes cannot break it. Then it reads the ticket again and tells me whether my own words under What I want are unchanged. When something is unclear it asks me one question at a time. It never writes code, never changes files, and uses made-up people and data only.
```

1. "It shows you a draft first, and changes the ticket only after your yes. The long gh part
   keeps your own words safe: paste it as it is, and change only your idea at the start."
2. Open **user-requirements.agent.md** and change one rule into your own words; save.
3. **Their turn** (01:12).

**01:22 Find it** · section 2, step 7. `/exit`, `copilot`, `/agent`: **user-requirements** is
listed. "One file, two doors: it is in Chat's agent picker too." **Their turn** (01:24).

**01:29 Cut:** "Break. After it, your agent writes its first criteria. No agent yet? A helper sits
with you now."

### 01:30-01:45 Break

Helpers add any missing skill or agent.

### 01:45-02:30 Agent lab: draft user stories and acceptance criteria, then validate · section 3

**01:45 The first criteria** · section 3, steps 1-3.

1. `/agent`, **user-requirements**, then
   `Write the user story and acceptance criteria for issue #1.` A ticket list pops up at `#1`:
   **Esc** once, then Enter. Answer any question it asks.
2. For each criterion: "Can I check it by clicking or counting?" Rewrite one:
   `Rewrite criterion 2 so that I can check it by counting. Change nothing else.` "Validate here
   means checkable. It is not GxP validation."
3. `Yes, update issue #1.` It reads the ticket again and asks to run the save, a short Python
   script around `gh issue edit`: "It checks your words stay the same. Allow it."
4. The ticket on GitHub: "Your own words under What I want are still there. Always check that."
5. **Their turn** (01:52); from 02:10 their other tickets. You do #2 and #3 meanwhile.

**02:20 Approve** · section 3, step 5. Drag #1 (today), #2 and #3 (for Copilot tomorrow) into
**Todo**: "Moving it to Todo is your approval: you are the product owner." Ask a neighbour to check
one ticket's criteria. **Their turn** (02:23): two tickets in **Todo**.

**02:29 Cut:** "Eyes up. We build the one you approved for today."

### 02:30-03:15 Build lab: implement an approved story, debug and verify the fix · section 4

1. `/exit`, `copilot`: back to ordinary Copilot, which can change files. Drag #1 to **In
   Progress**. Paste:

   ```text
   Read issue #1 with the GitHub tools and build it in site/index.html. Change only what it needs and keep everything else. Do not run tests or scripts: I check it myself. Then list how I can check each acceptance criterion.
   ```

2. Read what it wants to change before you allow it. In Chat `/start-website`, then check each
   criterion by hand, clicking and counting.
3. When one fails, the debug sentence: "That is the most useful sentence of the week."
   `Criterion 2 of issue #1 fails. I expected [this]. I saw [that]. Fix only that.`
4. **Their turn** (02:37): every criterion checked by hand, not on Copilot's word.
5. **03:05:** "Hand up if every criterion passes your own check." One volunteer tells a 30-second
   debug story.

**03:14 Cut:** "Now the computer re-checks it for you: tests."

### 03:15-03:45 Team build: add tests and document build and run commands · section 5

**03:15 Tests** · section 5, steps 1-3. Paste:

```text
Write tests in checks/test_issue1.py for the acceptance criteria of issue #1 that can be checked from the files, using from website import Page as shown in checks/README.md. Give every assert a short message saying what I expected. Tell me which criteria stay manual checks. Then run pytest checks.
```

1. **Yes** when it asks to run `pytest checks`: green **passed**.
2. Change one word a test looks for, save, `pytest checks`: red, with its message. **Ctrl+Z**,
   save, run again: green. "A test is a check the computer repeats for you after every change."
3. **Their turn** (03:20); tables help each other.

**03:32 The brief** · section 5, step 4. Paste:

```text
Add a section called How to build and run to site/brief.md, in plain words: how to open the page (/start-website), how to run the tests (pytest checks), how to run the build check (python -m app.site --check), and the manual checks for issue #1. Then add a section called Requirements: one line per ticket with its number, title, user story, and status today (Todo, In Progress, or Done).
```

It asks each ticket's status: pick it from the list. "This is David's validated brief: each
requirement traced to its ticket, and how to run it." **Their turn** (03:35), with their own idea's
brief.

**03:44 Cut:** "Last step: close the ticket with a commit."

### 03:45-04:00 Checkpoint: show the agent, requirements and working feature · section 6

1. Save. **Source Control**: the skill, the agent, the page, the test and the brief. Commit
   `Mark urgent tasks. Closes #1`, then **... > Push**. The board moves #1 to **Done** by itself.
2. **Their turn** (03:48). At 03:54 they show a neighbour four things: their agent and skill,
   their board, the finished ticket with its criteria, and the feature with green tests.
3. **03:59 Cut:** "Tomorrow Copilot's cloud agent builds the ticket waiting in Todo. Bring your
   phone: GitHub asks for your sign-in code when you change your repository's settings. Push,
   then stop your Codespace."

**Running late?**

- 00:20: make the board and write one ticket now, the others at 01:45. Never leave the board until
  after the tickets: a late import drops them all into **Todo**.
- 00:50: changing one step and one rule become optional.
- 01:45: criteria only on the two tickets they approve.
- 02:30: debug only when a criterion fails.
- 03:15: the brief's sections can be pushed with the 03:45 commit.

**Watch for**

- No **New project**: an organization setting. Add cards with **+ Add item** and `#`.
- A board that imported nothing (**Repository** left on the template): **+ Add item** and `#`,
  and point **Workflows > Auto-add to project** at their repository.
- New tickets landing in **Todo**: **Item added to project** is still on. Switch it off, then drag
  the others back to **No Status**.
- Tickets about what the page already does: "What do you want it to do next?"
- A terminal too short to show Copilot's question: **Maximize Panel Size**.
- A ticket that lost their own words: copy them back from the ticket's **edited** history, and
  remake the agent with the guide's full prompt.
- `gh issue edit` refused: paste the draft into the ticket by hand.
- The agent missing from `/agent`: `/exit`, then `copilot`.
- A commit without `Closes #1`: close the ticket by hand; the board still moves it.

**This evening:** on your demo website, assign #2 to Copilot (**Assign to Agent**), so its pull
request is ready on Thursday at 01:10. Then set up Thursday's 00:00 demo: the automation in Lab 03,
"Optional extras", step 3. It runs as you, on your allowance.

## Thursday

**Day 4: GitHub Copilot cloud agents.** 29 October, four hours including the break; times count
from the start. Their guide: **docs/DAY-4-BUILD.md**, and from 00:50 to 01:30
**labs/03-cloud-agent/README.md**. Same demo website. Keep your phone at hand: settings ask for
your sign-in code.

### 00:00-00:20 Cloud-agent overview: delegation, safeguards and human review · section 1

They listen. "Joining today? A helper starts you at the top of the Day 4 guide." Then the rejoin
rule.

1. **00:02 The road**, on the pull request Copilot opened for #2 last evening: feature branch, pull
   request, your review, merge, pipeline, live with a new version number. "Nobody pushes straight
   to main, not even you."
2. **00:05** **Issues > New issue > Requirement**, a new small wish; nobody assigns it. "Watch this
   ticket: we come back to it in ten minutes."
3. **00:07 Delegation and safeguards:** a ticket assigned to Copilot is built on its own `copilot/`
   branch, which cannot push to main; its pull request starts as a draft; checks on it wait for
   your approval; it follows your instructions and skills. "Delegating the work does not delegate
   the checking."
4. **00:12 Human review:** you read **Files changed**, try it, and decide, helped by your own Code
   Review agent.
5. **00:15** Back to the ticket: the story and criteria arrived by themselves. "An agent that starts
   by itself. You can set one up as an optional extra." Then switch it off: **Agents >
   Automations**, select it, **Disable**.
6. **00:18** Two volunteers say the road back.

**00:19 Cut:** "First the rules, then one small change down the road."

### 00:20-00:50 GitHub lab: practice branches and pull requests with a small change · section 2

**00:20 An address first** · section 2, before step 1. "No website address yet? /publish-website,
then save, commit and push now: after the ruleset, main takes only pull requests." **Their turn**
(00:22).

**00:25 Protect main** · section 2, step 1.

1. **Settings > Rules > Rulesets > New ruleset > New branch ruleset**. Name `Protect main`,
   **Enforcement status** **Active**, **Target branches > Add target > Include default branch**.
2. Keep **Restrict deletions** and **Block force pushes**; tick **Require a pull request before
   merging**, with approvals at **0**. Leave the bypass list empty. **Create**, then **Confirm
   access** with your phone.
3. "Zero approvals: you are alone in your repository, so you check before you merge. That code is
   yours alone: nobody else types it." **Their turn** (00:28).

**00:32 A version number** · section 2, steps 2-4.

1. Select `main` at the bottom left, **Create new branch...**, `feature/version-number`.
2. In **.github > workflows > publish-website.yml**, delete the `#` and the space before
   `version: 1.0.${{ github.run_number }}`; keep the indentation. "The run number is the build
   number: it goes up by one with every run."
3. In Copilot CLI:

   ```text
   In the footer of my first page, site/index.html, show the version from version.json, like Version 1.0.7. In my preview there is no version.json yet, so show Preview there. Change nothing else.
   ```

   The preview's footer says **Preview**. **Their turn** (00:36).

**00:42 Down the road** · section 2, steps 5-8.

1. Commit, **Publish Branch**, **Create Pull Request**. Asks to sign in? GitHub's yellow
   **Compare & pull request** banner instead.
2. On GitHub: **Files changed**, **Merge pull request**, **Confirm merge**, **Delete branch**.
   "GitHub may offer Delete codespace: never. That is your Codespace."
3. **Actions > Publish my website**. Green: your website's footer says **Version 1.0.N**.
4. In the Codespace: `main` at the bottom left, then **Source Control > ... > Pull**. **Their
   turn** (00:44).

**00:49 Cut:** "Your version appears in a couple of minutes. Now Copilot builds your next ticket."

### 00:50-01:30 Delegation lab: assign an approved requirement to Copilot · Lab 03

**00:50 Pick and check** · Lab 03, sections 1-2. On the board, #3 in **Todo**. Read its story and
criteria: "Could a stranger tell when it is done?" **Which page** names the right page. **Their
turn** (00:53).

**01:05 Assign it** · Lab 03, section 3. Under **Assignees**, **Assign to Agent** (or **Assignees >
Copilot**): base branch `main`, agent **Copilot**, prompt empty, **Assign**. Within a minute a draft
pull request appears and the card moves to **In Progress**. Open the session link. **Their turn**
(01:07). Copilot not listed: a helper, and they follow your pull request.

**01:10 Follow the work** · Lab 03, section 4. #2's pull request from last evening: its session log
(one step where it read files, one where it checked its work), the draft linked to the ticket, and
**Files changed**: "Only what the ticket asked for?" **Their turn** (01:14).

**01:29 Cut:** "Break. Copilot keeps working while you have coffee."

### 01:30-01:45 Break

Helpers: rulesets, live versions, assignments.

### 01:45-02:30 Build a Code Review agent: review rules and report format · section 4

**01:45 Review rules** · section 4, step 1. In Copilot CLI, paste:

```text
Create .github/instructions/review.instructions.md with applyTo: "site/**". List my rules for every change to my website: every acceptance criterion of the ticket is met; nothing outside the ticket changed; typed text is shown safely (textContent, never innerHTML); no new internet addresses, packages, keys, or real data; the page still works with a keyboard and in a narrow window; every button says what it does. Keep it under 15 lines.
```

Open the file: "applyTo says which files the rules are for. Rules written once: your review agent
checks against them, and Copilot follows them when it builds, here and in the cloud." **Their
turn** (01:49), with a last rule of their own.

**02:00 The Code Review agent** · section 4, steps 2-3. Paste:

```text
Create a custom agent file at .github/agents/code-review.agent.md with name: code-review and a one-line description. It is a Code Review agent for my website. When I give it a pull request number, it reads that pull request's changes and the ticket it is linked to, with its user story and acceptance criteria, and checks them against the rules in .github/instructions/review.instructions.md. It writes a report to reviews/pr-NUMBER.md as a table with the columns #, Severity (Must fix, Should fix, or Nice to have), File and line, What I found, Evidence (the exact line), and Suggested fix. Each finding is one or two plain sentences for a beginner. Problems that were already there before this pull request go in a separate table called "Already there before", so they do not block this change. If it cannot check something itself, it lists at most three short checks I can do by hand in the Website preview. It ends with "Verdict: Ready to merge" or "Verdict: Not yet". It never changes other files, comments on GitHub, or merges.
```

Open **code-review.agent.md** and change one rule. `/exit`, `copilot`, `/agent`: **code-review**
beside **user-requirements**. **Their turn** (02:04).

**02:20 Merge them** · section 4, step 4. Branch `review-tools`, commit both files, **Publish
Branch**, pull request, **Files changed**, merge; then `main` and **Pull**. **Their turn** (02:22).

**02:29 Cut:** "Two reviewers now look at Copilot's pull request: your agent and you."

### 02:30-03:15 Report lab: run the agent on a diff and verify its findings · section 5

**02:30 The review** · section 5, steps 1-3.

1. #2's pull request on GitHub, **Files changed**. Its number is N below.
2. `/agent`, **code-review**, then `Review pull request #N.` It asks before each command: **Yes**;
   for the read-only `gh` and `git` ones, option 2. It may offer to remember a fact: either answer.
   About five minutes.
3. Open `reviews/pr-N.md` and add a **My check** column: one **Confirmed** and one **Not a
   problem**, each with a reason. "Did it miss anything you saw?" No findings, or **Verdict: Not
   yet** only because it cannot try the page? Then your checks by hand are the **My check**. "An
   agent's report can be wrong, like any answer. Your checks decide."
4. **Their turn** (02:38). No Copilot pull request yet: they review their own from section 2.

**03:00 Try it yourself** · section 5, step 4. `/exit`, `copilot`, then
`Check out pull request #N so I can try it`. In Chat `/start-website`, each criterion; in the
terminal `pytest checks`. **Their turn** (03:03).

**03:14 Cut:** "Now ask Copilot to fix what you confirmed."

### 03:15-03:45 Iteration lab: request fixes with @copilot, retest and peer-review · section 6

1. **03:15** Comment on the pull request on GitHub:
   `@copilot Fix finding 1 from my review: [what is wrong]. Change nothing else.` No confirmed
   finding? `@copilot The Today label is small and easy to miss: make it a little bigger. Change nothing else.`
   It pushes a fix in a few minutes. "Peer review meanwhile." **Their turn** (03:18), then pairs
   check one criterion on each other's screen (03:22).
2. **03:32** `Pull the latest changes of this branch.` Check the criterion in the preview and run
   `pytest checks`. Back to `main` (`/exit`, `main` in the status bar, `copilot`): "code-review is
   listed only on main, because Copilot's branch is older than the agent." Review again; your
   **My check** notes stay. **Their turn** (03:35).

**03:44 Cut:** "Decision time: merge or not."

### 03:45-04:00 Checkpoint: review the report and decide whether to merge · section 7

1. **Ready for review**, **Merge pull request**; leave the **Reviewers** box alone. "Merge if every
   criterion passes and no Must fix is left; otherwise close it with a reason. Both are good
   decisions."
2. **Actions > Publish my website**: live with the next version in about three minutes. #2 is
   **Done** on the board (still open? **Close issue**).
3. In the Codespace, `main` and **Pull**. Save the report the same way: a branch, commit
   `reviews/pr-N.md`, a pull request, a merge. **Their turn** (03:49).
4. **03:59 Cut:** "Tomorrow GitHub checks every pull request for you, in a browser too. Push, then
   stop your Codespace."

**Running late?**

- 00:20: check the live version at the break.
- 00:50: Copilot slow? Move on, and come back to its pull request at 02:30.
- 02:30: one confirmed and one rejected finding are enough.
- 03:15: peer review always runs while Copilot works.

**Watch for**

- A push to `main` refused after the ruleset: expected. A branch and a pull request.
- The footer changed on an idea page: it belongs on the first page, `site/index.html`.
- A workflow-file push refused: a helper makes the same edit on GitHub with the pencil, on a new
  branch.
- The `version:` line with the wrong indentation.
- The live footer still says **Preview**: the `#` is still there, or that merge changed nothing in
  `site/`.
- **Delete codespace** offered after a merge: never.
- **Approve and run workflows** on a pull request: a helper first. It is a safeguard.
- A ticket still open after the merge: **Close issue** by hand.
- No Copilot review on pull requests: expected. Copilot code review is off.

**This evening:** #3's pull request from 01:05: review and merge it, or close it with a reason.
Before Friday, check githubstatus.com for **Actions**.

## Friday

**Day 5: CI/CD with GitHub Actions.** 30 October, four hours including the break; times count from
the start. Their guide: **docs/DAY-5-SHOWCASE.md**. Same demo website; the prepared red run is in
your spare copy. Keep your phone at hand.

Your website's address is `https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io`,
with `<name>` from `websiteName` in `config.json`. The feature slot adds `-feature` to the name.

### 00:00-00:20 CI/CD concepts: continuous integration, delivery and deployment · section 1

1. "Joining today? A helper starts you at the top of the Day 5 guide." Then the rejoin rule.
2. **00:02** "Continuous integration: every change is built and tested automatically. Continuous
   delivery: every checked change is ready to publish. Continuous deployment: it publishes by
   itself; here, a person approves first. Since yesterday every change is a pull request and every
   release has a number. Today: checks before merge, approval before release."
3. **00:10** Open `.github/workflows/publish-website.yml`: `on:` (when it runs), `permissions:`
   (what it may do), `version:` (the build number). **Their turn** (00:14): the three lines.
4. **00:18** Only if on time: the Agentic Workflows demo (public preview).

**00:19 Cut:** "Now you add the missing half: checks."

### 00:20-00:50 Workflow lab: edit a starter YAML file, triggers and permissions · section 2

**00:20 The check starter** · section 2, steps 1-3.

1. Branch `ci-checks`. In Copilot CLI:

   ```text
   Copy .github/workflow-starters/check-my-website.yml to .github/workflows/check-my-website.yml. Then explain each job and step in one plain sentence. Do not change anything else.
   ```

2. Open the new file and make the two edits its comments ask for. It then starts like this:

   ```yaml
   on:
     workflow_dispatch:
     pull_request:
     push:
       branches: [main]

   permissions:
     contents: read
   ```

   "Give a workflow only the permissions it needs: these checks only read." **Their turn** (00:25).

**00:37 Run them** · section 2, step 4. Commit, **Publish Branch**, pull request: both checks run on
it (**UI check** installs a browser first, about two minutes). Green: merge, delete the branch,
never **Delete codespace**. **Their turn** (00:40).

**00:44 Make them required** · section 2, step 5. **Settings > Rules > Rulesets > Protect main**,
tick **Require status checks to pass**, **Add checks**: **Check the website** and **UI check**,
**Save changes**, **Confirm access**. "They appear in the list only after they have run once."
**Their turn** (00:46).

**00:49 Cut:** "Now break it on purpose."

### 00:50-01:30 CI lab: build and test a pull request, inspect logs and fix failures · section 3

**00:50 Red on purpose** · section 3, steps 1-6.

1. Branch `try-ci`. In Copilot CLI:

   ```text
   Add a banner that says Sale at the very top of my first page, above its header. This is a test, so make it 900 pixels wide on every screen, even a phone: use min-width: 900px and do not let it shrink. Change nothing else.
   ```

   Read the change: any `max-width`? Ask it to remove that line. Commit, **Publish Branch**, pull
   request.
2. While it runs, open the prepared red run in your spare copy: **UI check** red, **Merge** blocked.
   **Details**: the table at the end of the log, "Wider than a phone screen". **Summary >
   Artifacts > home-phone.png** (it downloads): the banner sticks out.
3. `Why did the UI check on my pull request fail? Read its log and explain in two sentences.`
   Compare its answer with what you saw.
4. `Remove the banner you just added.` Commit and push: both green. Merge, delete the branch, then
   `main` and **Pull**. "Red is information, not failure." **Their turn** (01:00).

**01:20 A ticket for the break** · section 3, step 7. On the board, your next approved ticket in
**Todo**; none left? Write a small one first, such as `Show a short welcome line under my headline`,
and move it to **Todo**. Then **Assign to Agent**, **Assign**. "Copilot builds it during the break.
After the break it goes through your two slots." **Their turn** (01:22).

**01:26** "Hands up: who saw red? Who opened the phone screenshot? Who merged on green? Whose ticket
is with Copilot?"

**01:29 Cut:** "Break. Next: a test copy of your website for every pull request, and nothing
reaches production until you approve it."

### 01:30-01:45 Break

Helpers: required checks, stuck runs, tickets assigned to Copilot.

### 01:45-02:30 CD lab: approve and deploy a build to a training environment · section 4

**01:45 Two slots** · section 4, steps 1-2.

1. "Everything this week runs in the training environment. Your website now gets two slots: the
   feature slot, a test copy for each pull request, and production, your own address."
2. Branch `slots`. In Copilot CLI:

   ```text
   Copy .github/workflow-starters/deploy-feature-slot.yml to .github/workflows/deploy-feature-slot.yml, and copy .github/workflow-starters/publish-website-with-approval.yml over .github/workflows/publish-website.yml. Then explain in plain sentences what starts each workflow and what it may do. Change nothing else.
   ```

   Show the new **Wait for approval** job, and that the `version:` line is still there. Commit,
   **Publish Branch**, pull request, merge when green.
3. **Settings > Environments > New environment**, `production`, **Configure environment**. Tick
   **Required reviewers**, add yourself, **Save protection rules**. **Their turn** (01:50).

**01:57 Copilot's build in the feature slot** · section 4, steps 3-5.

1. Copilot's pull request: **Files changed** first. In the merge box, **Approve workflows to run**:
   "Nothing Copilot wrote runs until you say so." The checks take about two minutes.
2. **Actions > Deploy feature slot**: the newest run says **Action required**. Open it, **Approve
   and run**. About three minutes.
3. On the pull request, "deployed to feature-slot": **View deployment** opens `<name>-feature`,
   with the yellow strip (pull request, version, build). Check the ticket's criteria there, then
   run this and note the **content** number:

   ```bash
   python3 scripts/smoke_test.py https://<name>-feature.thankfulrock-bf005377.eastus.azurecontainerapps.io
   ```

   "Your own pull requests skip both approvals." **Their turn** (02:03).

**02:14 Approve, merge, release** · section 4, steps 6-7.

1. **Files changed > Submit review** (or **Review changes**), **Approve**, and a line on what you
   tested: "GitHub says it does not count as a required review; it is your record." Then **Ready
   for review**, **Merge pull request**.
2. **Actions > Publish my website** says **Waiting**: **Review deployments**, tick **production**,
   **Approve and deploy**. Green: your own address shows the change, no strip, a new version.
3. Smoke-test your own address: the same **content** number. "Production got exactly what you
   tested." An older **Deploy feature slot** run asking again: leave it. **Their turn** (02:17).

**02:27** "Hand up when production shows Copilot's change, with the same content number as your
feature slot."

**02:29 Cut:** "Now ship a bad release on purpose, and bring the good one back."

### 02:30-03:15 Recovery lab: smoke-test the app and redeploy a known-good build · section 5

1. **02:30 Smoke test** (step 1), with your address and the sentence under your headline:

   ```bash
   python3 scripts/smoke_test.py https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io --expect-text "<the sentence under my headline>"
   ```

   All **PASS**. Note **content** and **version**: "The content number is the fingerprint of your
   good version." **Their turn** (02:33).

2. **02:38 A bad release** (step 2). A new branch, then in Copilot CLI
   `Change the sentence under my headline to Oops, wrong words. Change nothing else.` A pull
   request: green checks, and **View deployment** shows the oops: "This is where a tester catches
   it." Merge anyway, approve the release, smoke test: **FAIL**. "No check knows your words: test
   before and after every release." **Their turn** (02:42).
3. **02:55 Roll back** (steps 3-4). The merged pull request, **Revert**, **Create pull request**;
   green; merge; approve the release. Smoke test: **PASS**, the same content, a higher version.
   "Revert is your rollback." **Their turn** (02:58).

**03:12 Cut:** "Each table: one screen and one speaker, three minutes each."

### 03:15-03:45 Team demos: show requirements, review report and CI/CD evidence · section 6

Host in table order with a timer on screen, about three minutes each, volunteer tables first. Each
table shows its board and one ticket's criteria; a confirmed and a rejected finding; red then green
with a screenshot; the feature slot with its strip; an approval; the version; a rollback. "An
honest 'this part does not work yet' beats a polished claim nobody checked."

**03:44 Cut:** "Last step: hand it over."

### 03:45-04:00 Handoff: share agent profiles, pipeline steps and release ownership · section 7

1. In Copilot CLI:

   ```text
   Write HANDOFF.md in plain words: my agent profiles (user-requirements and code-review: file, job, and how to run them), my user-stories skill, my board and how a ticket moves from Todo to Done, my review rules, my ruleset (what it requires before a merge), my pipeline (Check my website with its tests and UI check, Deploy feature slot for every checked pull request, and Publish my website to production with approval and a version number, and what starts each), how to release and how to roll back with Revert, who owns releases (me), and open questions for IT. Add a short 'To make it real' list: which parts are made up or only in my browser today, and the route for each from the table in docs/DAY-5-SHOWCASE.md.
   ```

2. Read it and correct one sentence; then a branch, a pull request, a merge.
3. The guide's "To make it real" table: Power Apps (a code app can keep the page's code), Power
   Automate, Power BI, Copilot Studio, Novo's own GitHub Enterprise, and Novo's validation process
   before any GxP use.
4. **Their turn** (03:48): HANDOFF.md merged, and any automation they made switched off.
5. **03:57 Cut:** thank the room. "Push, then stop your Codespace at github.com/codespaces."

**Running late?**

- Skip the Agentic Workflows demo.
- 00:50: runs slow? Show the prepared red run; they catch up in the break.
- 01:57: someone's Copilot pull request not ready? They open their own small pull request: it
  reaches the feature slot with no approval, and they watch Copilot's two approvals on your screen.
- 02:30: they can skip the oops release and just smoke-test before and after; show the bad release
  and the **Revert** on your screen.
- Demos: three minutes each, volunteer tables first.

**Watch for**

- No **Approve workflows to run** yet: Copilot is still working (a draft whose title starts with
  [WIP]). Wait for "Copilot finished work".
- No **View deployment** after green checks: **Actions > Deploy feature slot** waits for
  **Approve and run**.
- The feature slot shows another pull request: the last one checked wins; the strip names it.
- The banner leaves the **UI check** green: it went inside the header, or Copilot added
  `max-width: 100%`. Move it above the header and remove that line.
- **Check the website** or **UI check** missing from **Add checks**: they appear only after they
  have run once.
- A slow **UI check**: look at githubstatus.com; carry on and come back. Never re-run in a loop.
- A red **UI check** on an untouched page: open `home-phone.png`, then re-run once.
- Typing lands in the editor after a Copilot CLI diff closes: click in the terminal first.
- An oops pull request blocked by a Day 3 test that checks that sentence: "Your tests caught it."
  Pick another sentence.

## Preparation

**Before Monday**

- [x] This week's template changes are on GitHub's `main` (commit 1ff9eb8, 24 October, CI
      green): GenericAgent, the README's steps 5-8 and the guide fixes. Copies are made from
      GitHub, not from your laptop, so any later template change must reach `main` before 09:30
      on Monday too.
- [ ] Every day until Tuesday: `archive/facilitator/invitations/invite-attendees.ps1`, a dry run,
      then `-Send`; send Jackie the not-joined list. Invitations expire Tuesday 27 October at 12:15.
- [ ] Organization settings: the models attendees may use, the AI-credit budget (about 10 requests
      per `/create-website`, about 10 credits per `/publish-website`), Codespaces paid by the
      organization with a budget and a 30-minute idle timeout, and the Copilot cloud agent on for
      all repositories before Thursday. Copilot code review stays off.
- [ ] With David: the SEFR video and ASTER teaser running times, with sound tested in the room;
      whether attendees are split across the two rooms; who restarts the room on Tuesday at 10:45
      and who hosts 14:45; Days 3-5 start times, rooms and headcount; Friday's screen sharing,
      timer and demo order. David tries Use this template, a Codespace and `/create-website` once
      on a Novo laptop.
- [ ] Delete any rehearsal repository named after your username: your 09:30 live copy takes that
      name, and it stays your demo website all week.
- [ ] Monday's prepared websites in a separate repository: Weather, Princeton Map, Photo Studio and
      Lab Chase, built and checked, plus one published page. Keep its Codespace warm.
- [ ] Friday's red run: in a spare copy with the check starter merged, a pull request with the
      900-pixel banner above the header, so a finished red **UI check** is ready at 00:50.
- [ ] One practice run in a fresh Codespace with a non-owner, attendee-style account and Settings
      Sync off (synced settings hide the **Allow** prompts attendees see). Monday: the 09:30 copy,
      the 09:42 table name five times (**Retry**), the 09:52 demo (Ask on the README, then
      GenericAgent: web first, then the Joker), `/create-website` and the push, an own idea,
      `/add-chart`. Days 3-5: a board,
      `gh issue edit` updating a ticket, a workflow file pushed from the Codespace, **Confirm
      access**, **Assign to Agent**, the `production` environment form, and whether **Create Pull
      Request** asks to sign in.
- [ ] The version footer live on a practice website before Thursday.
- [ ] Print the quick reference, `docs/QUICK-REFERENCE.md`, for every table.
- [ ] Monday 08:30 welcome desk, for anyone not yet in the organization. Remote attendee BQMC: a
      Teams link and a named helper.
- [ ] Picture quota: with a full room most Photo Studio edits fall back to another model. Ask for
      more, or say so at 13:00.
- [ ] Decide whether published websites stay awake all week: `MIN_REPLICAS` in
      `.github/workflows/website-publisher.yml`. It is 0, so a first visit after a quiet spell
      takes about 30 seconds; 1 costs about USD 9 a day for 45 websites.

**Evenings:** Wednesday and Thursday each end with a **This evening** line above.

**After the week**, each step agreed with David first: remove attendee members (it stops seat
billing) and cancel pending invitations; archive the repositories and delete the published
websites; set `MIN_REPLICAS` back to 0 if you raised it; check the Thursday automation is off. The
`FOUNDRY_*` client secret expires on 1 November: renew it or delete it.

Old notes, the agenda and the setup guides are in `archive/`. You do not need them on the day.
