# What to Show and When

| Who | Means |
| --- | --- |
| 🎤 **Ali** | You show it on your screen. They watch, hands off keyboards. |
| 🤝 **Ali + attendees** | They click along with you, one click at a time. |
| 👥 **Attendees** | They do it alone, from their guide. You and the helpers walk the room. |

**Where in their guide** is the file they have open, then the heading in it, then the numbered
steps under that heading: `docs/DAY-2-BUILD.md` › Morning Build › steps 1-2. Say it out loud.
Quotes are what you say. `Grey` in **Do** is what you type. **[A]** is a box under the day's
table: paste it exactly.

**Cut on time.** At every **Say** row everyone moves on, finished or not. Helpers catch up anyone
stuck; they point, they never type for them.

**Rejoin rule**, on Monday at 10:45 and at the start of every later day: "Lost? Find the row we are
on in your guide's route table, open its link, and start there. Raise your hand."

**Every morning, 30 minutes before:**

- Demo Codespace open and warm, zoom about 150%, notifications off, your own MCP servers off
  (**MCP: List Servers**, each one, **Disable**), today's guide in a tab.
- Five minutes with the helpers: their tables, the rejoin rule, the day's **Watch for**.
- **Pushed a fix to the template since yesterday?** At the rejoin rule, say: "Open the Quick
  Reference, Get Unstuck, and paste the first sentence: Get the latest workshop fixes." It copies
  only guides, labs, prepared skills, scripts and starters; their website and own files stay.

**Monday only, before 09:00: the guardrail pre-flight.**

1. Create the demo Codespace fresh that morning, with **Settings Sync** off
   (github.com/settings/codespaces), so your personal agents and extensions stay off the big
   screen. Rehearse in a different Codespace.
2. **Trust Folder & Continue**. In Chat, **Sign In** at the bottom right if it shows.
3. Open `.github/agents/generic-agent.agent.md`: line 4 reads `tools: ["read", "search"]`.
4. **+** for a new chat: the button under the chat box says **Local**. Pick **GenericAgent**.
5. Ask `How is the weather in Princeton today?`: it must say it has no live weather access.
6. Any check fails: use another fresh Codespace. Never fix it on stage.
7. Start one more new chat (**+**) for the room.

Jump to: [Monday](#monday) · [Tuesday](#tuesday) · [Wednesday](#wednesday) ·
[Thursday](#thursday) · [Friday](#friday) · [Preparation](#preparation)

## Monday

**Day 1: GitHub and your first app.** 26 October, 09:00-15:00, rooms MKC 1D412 and 1D413. Until
10:30 they follow their repository's **README**; then **docs/START-HERE.md**.

| Time | Who | Do | Where in their guide |
| --- | --- | --- | --- |
| **09:00-09:30** | | **Sponsor welcome, ASTER teaser, glossary and GitHub basics** | |
| 09:00 | 🗣️ David | The sponsor's SEFR video, then HZRW's ASTER Overview teaser. | |
| 09:15 | 🎤 Ali | **GitHub tour** on the template page (github.com/agentic-dev-labs/copilot-hackathon-template). They only watch. See the tour table under this day's table. | `README.md` › This Is GitHub › steps 1-3 and the word table |
| 09:28 | 🎤 Ali | **Say:** "Now you make your own copy, one click at a time, with me. Make exactly one." | |
| **09:30-10:00** | | **Lab: Find files and Copilot Chat, ask and refine a question** | |
| 09:30 | 🤝 Ali + attendees | **Use this template > Create a new repository**. Owner **agentic-dev-labs**, name = GitHub username, **Private** (it may start on Internal), leave **Jumpstart**, **Create repository**. "Top of the page: agentic-dev-labs, your name, Private? Anything else: hand up." | `README.md` › Find Your Files and Copilot Chat › steps 1-2 |
| 09:37 | 🤝 Ali + attendees | **Code > Codespaces > Create codespace on main** (about a minute), **Trust Folder & Continue**, then right-click **README.md > Open Preview**. A pop-up in a corner (customizations or Python)? "Close it with its **X**. Never select **Migrate**." | `README.md` › Find Your Files and Copilot Chat › steps 3-4 |
| 09:40 | 🤝 Ali + attendees | **Sign in to Copilot.** ☰ menu > **View > Chat**. **Sign In** at the bottom right: select it, follow the GitHub prompts, **Authorize**. "No sign-in, no answers." Check: the button under the chat box says **Local**. | `README.md` › Find Your Files and Copilot Chat › step 5 |
| 09:42 | 🎤 Ali | **Ask** in the list at the bottom of the chat box: "Ask only answers." Type `Invent a fun name for my workshop table. Reply with the name only.` and read the name out. | `README.md` › Find Your Files and Copilot Chat › steps 5-6 |
| 09:44 | 👥 Attendees | The same question. | `README.md` › Find Your Files and Copilot Chat › steps 5-6 |
| 09:46 | 🎤 Ali | "Same name as your neighbour? Hands up." Then: "Copilot writes a new answer each time. That is why we always check its work." | `README.md` › Find Your Files and Copilot Chat › step 6 |
| 09:48 | 🎤 Ali | "Stay in this one chat all day." Type `What is in the docs folder?` and compare with **docs** in the Explorer. Then `Reply with exactly 5 bullet points, Monday to Friday, one per day, each 5 words or fewer. No other text.` Count the words of one bullet out loud. "Ask precisely and you get what you ask for. I did not start over: I told it what I wanted." | `README.md` › Find Your Files and Copilot Chat › steps 7-8 |
| 09:49 | 👥 Attendees | The same two questions. Helpers finish any missing copy or Codespace. | `README.md` › Find Your Files and Copilot Chat › steps 7-8 |
| 09:52 | 🎤 Ali | **Ask cannot change files.** Still in **Ask**: `Please rewrite my README file, but much shorter.` A shorter version appears in Chat, but no **Keep** or **Undo**, and no **M** next to README.md. Never select **Apply**. "Ask only answers." | They watch: `README.md` › Find Your Files and Copilot Chat › after step 8 |
| 09:53 | 🎤 Ali | **GenericAgent** from the same list (not **Agent**). Type `How is the weather in Princeton today?`: "no live weather access." Say: "A guardrail: the top of the file decides what an agent can reach." Open `.github/agents/generic-agent.agent.md`, on line 4 after `"search"` type `, "execute"`, save. Type `How is the weather in Princeton today?` again: it asks to run `curl` ("it still asks me first"), **Allow**: today's weather. "One word gave it a terminal, and a terminal reaches the internet. Give an agent only the doors it needs." Set line 4 back to `tools: ["read", "search"]` and save. | They watch: `README.md` › Find Your Files and Copilot Chat › after step 8 |
| 09:57 | 🎤 Ali | **Say:** "Questions about Ask or agents? One or two now." | |
| 09:59 | 🎤 Ali | **Say:** "Switch Chat from Ask to Agent. Agent can change your files, and you check every change." | |
| **10:00-10:30** | | **Create an idea note, save, review, commit, push and verify** | |
| 10:00 | 🎤 Ali | **Agent**, `/create-website`, **Project Planner**; about a minute, talk over it. It asks to run `python3 scripts/website_preview.py start`: **Allow**, "that opens your preview". **+** a made-up task. Point at **site > index.html**: "The file is the proof, not Copilot saying done." **Keep**: "Undo takes back everything you have not kept." | `README.md` › Your First Website › steps 1-4 |
| 10:05 | 👥 Attendees | Their first website; the Project Planner if unsure. | `README.md` › Your First Website › steps 1-4 |
| 10:15 | 🎤 Ali | **site > brief.md**: "The idea note on David's slide; you add to it all week." **File > Save All**, **Source Control** (about 30 files the first time), **+** on **Changes**, `Add my first website`, **Commit**, **... > Push**. On GitHub: **site > brief.md**. | `README.md` › Your First Website › steps 5-6 |
| 10:19 | 👥 Attendees | Save, commit, push, and find it on GitHub. | `README.md` › Your First Website › steps 5-6 |
| 10:28 | 🎤 Ali | **Say:** "Break. Not on GitHub yet? Stay seated: a helper finishes it with you now." | |
| **10:30-10:45** | ☕ Break | Switch to the Codespace of your prepared websites. Helpers check every page is on GitHub. | |
| **10:45-11:45** | | **Lab: Create a website with /create-website and preview it** | |
| 10:45 | 🎤 Ali | **docs > START-HERE.md > Open Preview**: "Your guide from now on." The rejoin rule. Your prepared websites, saying they are prepared: Weather (drag the 3D chart), Princeton Map (History, then 3D), Photo Studio (the sleepy cat as a watercolor), Lab Chase (20 seconds). "All made by describing them." | `docs/START-HERE.md` › Today's Route, then `labs/01-first-website/README.md` › 1. See What Else You Can Build |
| 10:55 | 🎤 Ali | Back in your live Codespace: **site > index.html**, select about five lines near the top, paste **[A]**. **Ctrl+F** `<h1>`, change two words, **File > Save**: the preview updates. "Code is only text." | `labs/01-first-website/README.md` › 2. Peek Inside the Code › steps 1-4 |
| 11:00 | 👥 Attendees | Lines explained; headline changed by hand. | `labs/01-first-website/README.md` › 2. Peek Inside the Code › steps 1-4 |
| 11:10 | 🎤 Ali | `/create-website`, answer `build my own idea`, then `A tracker for team requests with stages Submitted, Doing and Done.` Under two minutes, in its own folder in site/ideas. Then `Make the headline friendlier. Leave the rest alone.` and **Keep**. "Your first page stays." | `labs/01-first-website/README.md` › 3. Build One More Idea › steps 1-4 |
| 11:14 | 👥 Attendees | One own idea in its own folder. Helpers watch for Copilot changing the first page. | `labs/01-first-website/README.md` › 3. Build One More Idea › steps 1-4 |
| 11:30 | 🎤 Ali | **File > Save All**, **Source Control** (only what changed), a message, **Commit**, **... > Push**; the idea's folder on GitHub. | `labs/01-first-website/README.md` › 4. Save and Show |
| 11:32 | 👥 Attendees | Pushed, and shown to a neighbour. | `labs/01-first-website/README.md` › 4. Save and Show |
| 11:44 | 🎤 Ali | **Say:** "Eyes up. Now you are the checker." | |
| **11:45-12:15** | | **Trust but verify: check a button and a figure, fix and recheck** | |
| 11:45 | 🎤 Ali | `/start-website`, then `Add a button that hides finished tasks.` "I expect the ticked task to disappear." Click it twice, compare. Right: **Keep**. Wrong: `I expected ..., but I saw ...` | `labs/01-first-website/README.md` › Coached Verification Block › step 1 |
| 11:49 | 👥 Attendees | One button checked. | `labs/01-first-website/README.md` › Coached Verification Block › step 1 |
| 11:55 | 🎤 Ali | Count: four example tasks plus this morning's, one ticked: **1 of 5 done**. Tick one: **2 of 5**. "Never trust a number you have not checked." | `labs/01-first-website/README.md` › Coached Verification Block › step 2 |
| 11:57 | 👥 Attendees | One number counted, with the table in their lab. | `labs/01-first-website/README.md` › Coached Verification Block › step 2 |
| 12:05 | 🎤 Ali | In **site/brief.md**: what you tried and what happened. Save, commit, push. | `labs/01-first-website/README.md` › Coached Verification Block › step 3 |
| 12:07 | 👥 Attendees | Written down and pushed. | `labs/01-first-website/README.md` › Coached Verification Block › step 3 |
| 12:14 | 🎤 Ali | **Say:** "Lunch. Push first; your Codespace waits for you." | |
| **12:15-13:00** | ☕ Lunch | | |
| **13:00-14:00** | | **Lab: Add a useful interaction, personalize and check** | |
| 13:00 | 🎤 Ali | "Pick one: a chart, a chat or a picture. A chart if unsure." `/add-chart`, **Progress gauge** or the 3D **Week skyline**; about a minute, and if it asks whether you see it: **Yes**. Drag it, **Keep**. Mention `/add-chat` and pictures: "the picture model may vary." | `labs/02-make-it-useful/README.md` › 1. Choose Your Feature and 2. Add It |
| 13:09 | 👥 Attendees | Their feature added. | `labs/02-make-it-useful/README.md` › 1. Choose Your Feature and 2. Add It |
| 13:20 | 🎤 Ali | "I expect one more done." Tick a task: the count and the chart move; untick: both go back. "A chart can be wrong too: count it yourself." | `labs/02-make-it-useful/README.md` › 3. Check It Yourself |
| 13:23 | 👥 Attendees | Checked against their own count. | `labs/02-make-it-useful/README.md` › 3. Check It Yourself |
| 13:35 | 🎤 Ali | Paste **[B]**, **Keep**. Then `Make the whole page bright purple with giant text.` and **Undo**, **Yes**: "Undo takes back everything you have not kept." | `labs/02-make-it-useful/README.md` › 4. Make the Design Yours |
| 13:39 | 👥 Attendees | One look kept, one **Undo**. From 13:50: a note in their brief, shown to a neighbour. | `labs/02-make-it-useful/README.md` › 4. Make the Design Yours and 5. Write It Down |
| 13:59 | 🎤 Ali | **Say:** "Now we save it and look back in time." | |
| **14:00-14:45** | | **Lab: Save, share and keep building (publication optional)** | |
| 14:00 | 🎤 Ali | **Source Control**, **+** on the files you checked, the **sparkle icon**, fix a word, **Commit**, **... > Push**. "Read what it wrote: you sign it." | `labs/08-save-and-share/README.md` › 1. Let Copilot Write the Message › steps 1-4 |
| 14:03 | 👥 Attendees | Committed and pushed. | `labs/08-save-and-share/README.md` › 1. Let Copilot Write the Message › steps 1-4 |
| 14:10 | 🎤 Ali | On GitHub: **Commits**, then **Add my first website** (green added, red removed), then **site > index.html > History**: "A time machine for your work." | `labs/08-save-and-share/README.md` › 2. Explore Your Work on GitHub › steps 5-7 |
| 14:13 | 👥 Attendees | Their own history found. | `labs/08-save-and-share/README.md` › 2. Explore Your Work on GitHub › steps 5-7 |
| 14:20 | 🎤 Ali | The challenge card: Bronze, Silver, Gold. Then publish your copy, because Thursday needs its address: `/publish-website`, accept the name, save, commit, push; about three minutes. | `labs/08-save-and-share/README.md` › 3. Take a Challenge; publishing: Optional extras › Publish Your Page |
| 14:22 | 👥 Attendees | One challenge level; publishing is optional, with a helper. | `labs/08-save-and-share/README.md` › 3. Take a Challenge; publishing: Optional extras › Publish Your Page |
| 14:35 | 🎤 Ali | Your published page on screen; open it a minute early, because it wakes in about 30 seconds. They open it on their phones. | `labs/08-save-and-share/README.md` › Optional extras › Publish Your Page |
| 14:36 | 👥 Attendees | Show a neighbour one feature; write the next idea in the brief. | `labs/08-save-and-share/README.md` › 4. Show It › step 8 |
| 14:44 | 🎤 Ali | **Say:** "Pair sharing: one feature, and how you checked it." | |
| **14:45-15:00** | | **Pair sharing and selected volunteer demonstrations** | |
| 14:45 | 👥 Attendees | Pairs share. You pick two or three volunteers. | `docs/START-HERE.md` › Today's Route › 14:45-15:00 Pair sharing |
| 14:50 | 🎤 Ali | The volunteers on the big screen, about two minutes each. | |
| 14:58 | 🎤 Ali | **Say:** "Push, then stop your Codespace at github.com/codespaces. Closing the tab does not stop it." | |

Why `"execute"` and not `"web"` at 09:53: a Local chat in a browser Codespace has no web tool for
any agent, so `"web"` unlocks nothing (tested 25 October). Only your demo copy changes, and you set
it back straight after.

**09:15 GitHub tour.** On the big screen, on the template's GitHub page:

| # | You click | They see | You say |
| --- | --- | --- | --- |
| 1 | Nothing; point at the files | The template's files | "A repository is a folder with a memory." |
| 2 | **Commits** (clock icon, above the files) | Every saved version | "Every saved snapshot." |
| 3 | Back, **README.md**, then **History** (top right) | That file's changes | "How one file changed." |
| 4 | Back, scroll to the README's word table | Repository, Codespace, Copilot, Commit, Push | Read them, then: "Save, review, commit, push: always in that order." |

**[A]** 10:55:

```text
Explain the lines I selected in plain English, one short sentence per line. I have never seen code before.
```

**[B]** 13:35:

```text
Keep the page light. Try a sky blue look. Keep the text easy to read and leave the content and features unchanged.
```

**Running late:** 09:52, show only the README in Ask, then go to 09:59 · 09:44, skip their own
table names · 09:30 runs over: finish first websites in the break; never cut Lab 01 · 10:45, show
only Weather and Lab Chase · 13:00, skip the picture mention · 14:20, publish your copy in the
evening.

**Watch for**

- No agentic-dev-labs in the owner list: not in the organization yet. The welcome desk.
- A second repository or Codespace: a helper sorts out which one to keep.
- **Trust Folder** declined: **Reload Window**, then trust.
- **Sign In** at the bottom right, or Chat never answers: **Sign In**, GitHub prompts, **Authorize**.
- At 09:53 GenericAgent answers the first weather question with 57°F: that is the Weather starter's sample file
  in this repository, not today's weather. Say so: "Check its work." Then add `"execute"`.
- No **Keep** or **Undo**, or the button under the chat box says **Copilot**: an old chat reopened.
  Select **+**; if it still says **Copilot**, select it > **Local** before typing.
- GenericAgent goes online, check in this order:
  1. The chat title starts with **Local ·**. Not? **+** for a new chat (your own settings reopen
     old chats, so always start the demo with **+**).
  2. Line 4 reads `tools: ["read", "search"]`. `tools: []` means every tool, not none. Edit the
     line by hand; never use **Configure Tools**, which rewrites it.
  3. Both right and still online: the agent was renamed in this Codespace. Use a fresh one.
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

| Time | Who | Do | Where in their guide |
| --- | --- | --- | --- |
| **09:00-09:30** | 🗣️ David | **Business/IT roles, approved tools and AI marketplace.** Note questions for the tables. | |
| **09:30-10:30** | 🗣️ Jackie | **Power Platform, Dataverse and connector examples.** | |
| **10:30-10:45** | ☕ Break | Every table reopens Monday's Codespace: **Code > Codespaces**, its name. Never **Create codespace**. | |
| **10:45-11:45** | | **Supported own-idea build with fictional local data** | |
| 10:45 | 🗣️ Host | **Say:** "Open docs/DAY-2-BUILD.md, Morning Build. Tell your helper your four answers. Lost later? Find the row for the time now." | `docs/DAY-2-BUILD.md` › Morning Build |
| 10:46 | 👥 Attendees | Four answers, no files yet (10 minutes): who it is for, what they can do, the smallest first version, how to check it. Then build (35 minutes): `/start-website <folder>` for Monday's idea, or `/create-website` and one sentence. | `docs/DAY-2-BUILD.md` › Morning Build › steps 1-2 |
| 10:46 | 🎤 Ali | At the tables. Nudge: "Describe it as a tracker of ... with stages ..." or "a dashboard of ... by ... per month". Each attendee's idea: `archive/facilitator/ideas/TABLE-SUPPORT.md`. | |
| 11:30 | 🎤 Ali | **Say**, at every table: "Save and push now: Bill starts at 11:45." | `docs/DAY-2-BUILD.md` › Morning Build › step 3 |
| **11:45-12:15** | 🗣️ Bill Leeson | **Building a Project Brain.** | |
| **12:15-13:00** | ☕ Lunch | | |
| **13:00-14:00** | 👥 Attendees | **Open build: improve an interaction, check behaviour and get help.** One form, filter or choice, checked one thing at a time: clear words, an empty entry, a count, the keyboard and a narrow window. You and the helpers at the tables. | `docs/DAY-2-BUILD.md` › Improve One Interaction › the four bullets |
| **14:00-14:45** | 👥 Attendees | **Supported building, fixes and optional assisted publication.** One fix at a time, then save, commit, push. You help anyone publishing with `/publish-website`. | `docs/DAY-2-BUILD.md` › Fixes and Optional Publishing |
| **14:45-15:00** | | **Volunteer demonstrations and next step with the technical owner** | |
| 14:45 | 🗣️ Host | Volunteers show. Everyone notes questions for IT: data, access, systems, approval. | `docs/DAY-2-BUILD.md` › Show and Plan the Next Step |
| 14:52 | 🎤 Ali | **Say**, at every table: "Two or three wishes under Next in your brief, then save, commit, push. These are Wednesday's tickets. Then stop your Codespace." | `docs/DAY-2-BUILD.md` › Show and Plan the Next Step › the **Next** wishes |

**Watch for:** an own idea replacing Monday's page (it belongs in its own folder in `site/ideas/`);
real names or data; integration wishes such as Outlook, PDFs, SharePoint or Access (onto the
questions for IT, not into the page); anyone leaving without **Next** wishes.

## Wednesday

**Day 3: VS Code and a Requirements agent.** 28 October, four hours; times count from the start.
Their guide: **docs/TOOLS-PRACTICE.md**. Your demo website is your Monday live copy. A helper
starts anyone without a website (the guide's **No website yet?**).

| Time | Who | Do | Where in their guide |
| --- | --- | --- | --- |
| **00:00-00:20** | 🗣️ MUKQ | **Global and Microsoft perspectives on AI development.** You: your demo website and its Codespace ready. | |
| **00:20-00:50** | | **Ali: workspace setup, repo walkthrough and agent roles/tools** | |
| 00:20 | 🎤 Ali | The rejoin rule. "Your Tuesday wishes become tickets today." On your repository's page: the organization's name, **Projects > New project > Board**, `<your username> website`, keep **Import items from repository**, **Repository** = your own, **Create project**. Then **Workflows > Item added to project > Off**: "Approving is your job. Todo is approved, In Progress is being built, Done is finished." | `docs/TOOLS-PRACTICE.md` › 1. Tickets, Board, and Tools › steps 1-2 |
| 00:24 | 👥 Attendees | Their board. Helpers check it names their own repository and the workflow is Off. | `docs/TOOLS-PRACTICE.md` › 1. Tickets, Board, and Tools › steps 1-2 |
| 00:31 | 🎤 Ali | **Issues > New issue > Requirement**: `Mark urgent tasks`, **What I want** in plain words, **Which page** stays `site/index.html`, **Create**: #1, under **No Status**. "One thing you want next." | `docs/TOOLS-PRACTICE.md` › 1. Tickets, Board, and Tools › steps 3-4 |
| 00:34 | 👥 Attendees | Two or three tickets from their **Next** wishes. You meanwhile: `Highlight today's column` (#2) and `Add a Saturday column` (#3). | `docs/TOOLS-PRACTICE.md` › 1. Tickets, Board, and Tools › steps 3-4 |
| 00:39 | 🎤 Ali | ☰ menu > **Terminal > New Terminal**, **Maximize Panel Size**, `copilot`. A model name at the bottom means signed in; otherwise `/login` and github.com/login/device. Paste **[A]** and point at **List issues**: "That is MCP, a plug that lets Copilot act on GitHub." "Ask answers, Agent changes files, a custom agent has one job, and tomorrow the cloud agent works on GitHub." | `docs/TOOLS-PRACTICE.md` › 1. Tickets, Board, and Tools › steps 5-7 |
| 00:42 | 👥 Attendees | Signed in, tickets listed. Stuck in the terminal: the same sentence in Chat with **Agent**. | `docs/TOOLS-PRACTICE.md` › 1. Tickets, Board, and Tools › steps 5-7 |
| 00:49 | 🎤 Ali | **Say:** "Keep the terminal open. Eyes up: now you write your own helpers." | |
| **00:50-01:30** | | **Build a User Requirements agent: instructions and output format** | |
| 00:50 | 🎤 Ali | Open `.github/skills/create-website/SKILL.md`: "The recipe behind /create-website." Then `.github/copilot-instructions.md` (rules), `.github/skills/` (how), `.github/agents/` (who: "Remember Monday's GenericAgent? Today's agent gets a real job.") and `.vscode/mcp.json` (plugs). `/agent` lists GenericAgent; **Esc**. | `docs/TOOLS-PRACTICE.md` › 2. Build Your User Requirements Agent › steps 1-2 |
| 00:56 | 🎤 Ali | Paste **[B]**. Asked to read docs.github.com: **2**. The new file: **Yes**. Open SKILL.md and change one step. | `docs/TOOLS-PRACTICE.md` › 2. Build Your User Requirements Agent › steps 3-4 |
| 00:59 | 👥 Attendees | Their skill. | `docs/TOOLS-PRACTICE.md` › 2. Build Your User Requirements Agent › steps 3-4 |
| 01:09 | 🎤 Ali | Paste **[C]**: "A draft first; it changes a ticket only after your yes. Paste it as it is." Open the agent file and change one rule. | `docs/TOOLS-PRACTICE.md` › 2. Build Your User Requirements Agent › steps 5-6 |
| 01:12 | 👥 Attendees | Their agent. | `docs/TOOLS-PRACTICE.md` › 2. Build Your User Requirements Agent › steps 5-6 |
| 01:22 | 🎤 Ali | `/exit`, `copilot`, `/agent`: **user-requirements** is listed. "One file, two doors: Chat has it too." | `docs/TOOLS-PRACTICE.md` › 2. Build Your User Requirements Agent › step 7 |
| 01:24 | 👥 Attendees | Their agent listed. | `docs/TOOLS-PRACTICE.md` › 2. Build Your User Requirements Agent › step 7 |
| 01:29 | 🎤 Ali | **Say:** "Break. No agent yet? A helper sits with you now." | |
| **01:30-01:45** | ☕ Break | Helpers add missing skills and agents. | |
| **01:45-02:30** | | **Agent lab: draft user stories and acceptance criteria, then validate** | |
| 01:45 | 🎤 Ali | `/agent`, **user-requirements**, `Write the user story and acceptance criteria for issue #1.` (a list pops up: **Esc** once). Each criterion: "Can I check it by clicking or counting?" `Rewrite criterion 2 so that I can check it by counting. Change nothing else.` "Validate means checkable, not GxP." `Yes, update issue #1.` and allow the save. On GitHub: "Your own words are still there." | `docs/TOOLS-PRACTICE.md` › 3. Draft and Validate the Criteria › steps 1-3 |
| 01:52 | 👥 Attendees | Their first ticket; from 02:10 the others. You do #2 and #3. | `docs/TOOLS-PRACTICE.md` › 3. Draft and Validate the Criteria › steps 1-4 |
| 02:20 | 🎤 Ali | Drag #1 (today), #2 and #3 (Copilot, tomorrow) into **Todo**: "Todo is your approval." A neighbour checks one ticket. | `docs/TOOLS-PRACTICE.md` › 3. Draft and Validate the Criteria › step 5 |
| 02:23 | 👥 Attendees | Two tickets in **Todo**. | `docs/TOOLS-PRACTICE.md` › 3. Draft and Validate the Criteria › step 5 |
| 02:29 | 🎤 Ali | **Say:** "Eyes up. We build the one you approved for today." | |
| **02:30-03:15** | | **Build lab: implement an approved story, debug and verify the fix** | |
| 02:30 | 🎤 Ali | `/exit`, `copilot`; #1 to **In Progress**; paste **[D]**; read the change before allowing it. **Say:** "On screen I build my first page. You use your ticket's page from **Which page**, as in your guide." In Chat `/start-website`; check each criterion by hand. Fails? `Criterion 2 of issue #1 fails. I expected [this]. I saw [that]. Fix only that.` "The most useful sentence of the week." | `docs/TOOLS-PRACTICE.md` › 4. Build the Approved Ticket › steps 1-5 |
| 02:37 | 👥 Attendees | Every criterion checked by hand, not on Copilot's word. | `docs/TOOLS-PRACTICE.md` › 4. Build the Approved Ticket › steps 1-5 |
| 03:05 | 🎤 Ali | "Hand up if every criterion passes." One volunteer: a 30-second debug story. | |
| 03:14 | 🎤 Ali | **Say:** "Now the computer re-checks it for you: tests." | |
| **03:15-03:45** | | **Team build: add tests and document build and run commands** | |
| 03:15 | 🎤 Ali | Paste **[E]**; **Yes** to `pytest checks`: green. Change a word a test checks, run it: red. **Ctrl+Z**, save, run: green. "A test repeats your check after every change." | `docs/TOOLS-PRACTICE.md` › 5. Add Tests and How to Run › steps 1-3 |
| 03:20 | 👥 Attendees | Their tests; tables help each other. | `docs/TOOLS-PRACTICE.md` › 5. Add Tests and How to Run › steps 1-3 |
| 03:32 | 🎤 Ali | Paste **[F]**; pick each ticket's status from the list. **Say:** "Mine is site/brief.md. Yours is your idea's brief, as in your guide." "David's validated brief: each requirement traced to its ticket." | `docs/TOOLS-PRACTICE.md` › 5. Add Tests and How to Run › step 4 |
| 03:35 | 👥 Attendees | Their brief. | `docs/TOOLS-PRACTICE.md` › 5. Add Tests and How to Run › step 4 |
| 03:44 | 🎤 Ali | **Say:** "Last step: close the ticket with a commit." | |
| **03:45-04:00** | | **Checkpoint: show the agent, requirements and working feature** | |
| 03:45 | 🎤 Ali | Save; **Source Control**: skill, agent, page, test, brief. Commit `Mark urgent tasks. Closes #1`, **... > Push**: the board moves #1 to **Done**. | `docs/TOOLS-PRACTICE.md` › 6. Checkpoint › steps 1-2 |
| 03:48 | 👥 Attendees | Commit and push. From 03:54, show a neighbour: agent and skill, board, finished ticket, green tests. | `docs/TOOLS-PRACTICE.md` › 6. Checkpoint › steps 1-3 |
| 03:59 | 🎤 Ali | **Say:** "Tomorrow Copilot builds the ticket waiting in Todo. Bring your phone. Push, then stop your Codespace." | |

**[A]** 00:39:

```text
Use the GitHub tools to list the open issues in my repository, with their numbers. Do not change anything.
```

**[B]** 00:56, the skill:

```text
Create a skill at .github/skills/user-stories/SKILL.md with name: user-stories and a description that says it turns one ticket for my website into a user story with acceptance criteria. Its steps: read the ticket's What I want and Which page; write one user story as "As a ..., I want ..., so that ..."; under it write 2 or 3 acceptance criteria as "Given ..., when ..., then ..." that a person can check by clicking or counting, each with a checkbox; list open questions instead of guessing. Its output fills the ticket's User story and Acceptance criteria sections, followed by Open questions. Made-up people and data only.
```

**[C]** 01:09, the agent:

```text
Create a custom agent file at .github/agents/user-requirements.agent.md with name: user-requirements and a one-line description. It is a User Requirements agent for my small website about a project planner. When I name a ticket by its number, it reads the ticket with the GitHub tools and uses the user-stories skill to draft its user story and acceptance criteria. It shows me the draft first. Only when I say yes does it update that ticket with the gh issue edit command: it reads the ticket's exact text with gh issue view NUMBER --json body --jq .body, changes only the User story and Acceptance criteria sections, keeps every other line exactly as it is, and gives the new text to gh issue edit NUMBER --body-file - through standard input, so quotes cannot break it. Then it reads the ticket again and tells me whether my own words under What I want are unchanged. When something is unclear it asks me one question at a time. It never writes code, never changes files, and uses made-up people and data only.
```

**[D]** 02:30, the build:

```text
Read issue #1 with the GitHub tools and build it in site/index.html. Change only what it needs and keep everything else. Do not run tests or scripts: I check it myself. Then list how I can check each acceptance criterion.
```

**[E]** 03:15, the tests:

```text
Write tests in checks/test_issue1.py for the acceptance criteria of issue #1 that can be checked from the files, using from website import Page as shown in checks/README.md. Give every assert a short message saying what I expected. Tell me which criteria stay manual checks. Then run pytest checks.
```

**[F]** 03:32, the brief:

```text
Add a section called How to build and run to site/brief.md, in plain words: how to open the page (/start-website), how to run the tests (pytest checks), how to run the build check (python -m app.site --check), and the manual checks for issue #1. Then add a section called Requirements: one line per ticket with its number, title, user story, and status today (Todo, In Progress, or Done).
```

**Running late:** 00:20, the board and one ticket now, the rest at 01:45; never leave the board
until after the tickets, because a late import drops them all into **Todo** · 00:50, changing one
step and one rule become optional · 01:45, criteria only on the two tickets they approve · 02:30,
debug only when a criterion fails · 03:15, the brief can be pushed with the 03:45 commit.

**Watch for**

- No **New project**: an organization setting. Add cards with **+ Add item** and `#`.
- A board that imported nothing: **+ Add item** and `#`, and point **Workflows > Auto-add to
  project** at their repository.
- New tickets landing in **Todo**: **Item added to project** is still on. Switch it off and drag
  them back to **No Status**.
- Tickets about what the page already does: "What do you want it to do next?"
- A terminal too short for Copilot's question: **Maximize Panel Size**.
- A ticket that lost their own words: copy them back from its **edited** history, and remake the
  agent with the full prompt.
- `gh issue edit` refused: paste the draft into the ticket by hand.
- The agent missing from `/agent`: `/exit`, then `copilot`.
- A commit without `Closes #1`: close the ticket by hand.

**This evening:** on your demo website, assign #2 to Copilot (**Assign to Agent**), so its pull
request is ready on Thursday at 01:10. Set up the automation for Thursday's 00:05 demo:
`labs/03-cloud-agent/README.md` › Optional extras › step 3. It runs as you, on your allowance.

## Thursday

**Day 4: GitHub Copilot cloud agents.** 29 October, four hours with the break; times count from
the start. Their guide: **docs/DAY-4-BUILD.md**, and **labs/03-cloud-agent/README.md** from 00:50
to 01:30. Same demo website. Phone at hand: settings ask for your sign-in code.

| Time | Who | Do | Where in their guide |
| --- | --- | --- | --- |
| **00:00-00:20** | | **Cloud-agent overview: delegation, safeguards and human review** | |
| 00:00 | 🎤 Ali | "Joining today? A helper starts you at the top of the Day 4 guide." The rejoin rule. | `docs/DAY-4-BUILD.md` › top: **Joining today?** and Today's Route |
| 00:02 | 🎤 Ali | The road, on Copilot's pull request for #2: branch, pull request, review, merge, pipeline, live with a version. "Nobody pushes straight to main, not even you." | `docs/DAY-4-BUILD.md` › 1. How a Change Reaches Your Website › bullets 1-2 (the road, delegation) |
| 00:05 | 🎤 Ali | **Issues > New issue > Requirement**, a small wish; nobody assigns it. "We come back to it in ten minutes." | `docs/DAY-4-BUILD.md` › 1. How a Change Reaches Your Website › bullet 3 (an agent that starts by itself) |
| 00:07 | 🎤 Ali | Safeguards: its own `copilot/` branch, a draft pull request, checks that wait for your approval, your instructions and skills. "Delegating the work does not delegate the checking." 00:12, human review: read **Files changed**, try it, decide. | `docs/DAY-4-BUILD.md` › 1. How a Change Reaches Your Website › bullets 4-5 (safeguards, human review) |
| 00:15 | 🎤 Ali | The 00:05 ticket: its story and criteria arrived by themselves. "An agent that starts by itself." Then **Agents > Automations**, **Disable**. At 00:18 two volunteers say the road back. | `docs/DAY-4-BUILD.md` › 1. How a Change Reaches Your Website › bullet 3 (an agent that starts by itself) |
| **00:20-00:50** | | **GitHub lab: practice branches and pull requests with a small change** | |
| 00:20 | 🎤 Ali | "No website address yet? `/publish-website`, then save, commit, push now: after the ruleset, main takes only pull requests." | `docs/DAY-4-BUILD.md` › 2. Protect Main and Version Your Releases › **Your website needs an address**, before step 1 |
| 00:22 | 👥 Attendees | Publish, if needed. | `docs/DAY-4-BUILD.md` › 2. Protect Main and Version Your Releases › **Your website needs an address**, before step 1 |
| 00:25 | 🎤 Ali | **Settings > Rules > Rulesets > New ruleset > New branch ruleset**: `Protect main`, **Active**, **Add target > Include default branch**; keep **Restrict deletions** and **Block force pushes**; tick **Require a pull request before merging** with **0** approvals; bypass list empty; **Create**; **Confirm access** on your phone. "Zero approvals: you check before you merge." | `docs/DAY-4-BUILD.md` › 2. Protect Main and Version Your Releases › step 1 |
| 00:28 | 👥 Attendees | Their ruleset. | `docs/DAY-4-BUILD.md` › 2. Protect Main and Version Your Releases › step 1 |
| 00:32 | 🎤 Ali | `main` at the bottom left, **Create new branch...**, `feature/version-number`. In `publish-website.yml` delete the `#` and the space before `version: 1.0.${{ github.run_number }}`, keeping the indentation. Paste **[A]**: the footer says **Preview**. "The run number is the build number." | `docs/DAY-4-BUILD.md` › 2. Protect Main and Version Your Releases › steps 2-4 |
| 00:36 | 👥 Attendees | The same change. | `docs/DAY-4-BUILD.md` › 2. Protect Main and Version Your Releases › steps 2-4 |
| 00:42 | 🎤 Ali | Commit, **Publish Branch**, **Create Pull Request** (asked to sign in? GitHub's **Compare & pull request**). **Files changed**, **Merge pull request**, **Confirm merge**, **Delete branch**: "Never Delete codespace." **Actions** green: the footer shows **Version 1.0.N**. In the Codespace: `main`, **... > Pull**. | `docs/DAY-4-BUILD.md` › 2. Protect Main and Version Your Releases › steps 5-8 |
| 00:44 | 👥 Attendees | The same; a slow run is checked at the break. | `docs/DAY-4-BUILD.md` › 2. Protect Main and Version Your Releases › steps 5-8 |
| 00:49 | 🎤 Ali | **Say:** "Your version appears in a couple of minutes. Now Copilot builds your next ticket." | |
| **00:50-01:30** | | **Delegation lab: assign an approved requirement to Copilot** | |
| 00:50 | 🎤 Ali | The board: #3 in **Todo**. Read its story and criteria: "Could a stranger tell when it is done?" **Which page** names the right page. | `labs/03-cloud-agent/README.md` › 1. Pick the Ticket and 2. Check the Ticket |
| 00:53 | 👥 Attendees | Their ticket picked and checked. | `labs/03-cloud-agent/README.md` › 1. Pick the Ticket and 2. Check the Ticket |
| 01:05 | 🎤 Ali | **Assignees > Assign to Agent**: base `main`, agent **Copilot**, prompt empty, **Assign**. A draft pull request within a minute, and the card moves to **In Progress**. Open the session link. | `labs/03-cloud-agent/README.md` › 3. Assign It to Copilot › steps 1-3 |
| 01:07 | 👥 Attendees | Theirs assigned. Copilot not listed: a helper, and they follow your pull request. | `labs/03-cloud-agent/README.md` › 3. Assign It to Copilot › steps 1-3 |
| 01:10 | 🎤 Ali | #2's pull request from last evening: the session log (one step reading, one checking), the draft linked to the ticket, **Files changed**: "Only what the ticket asked for?" | `labs/03-cloud-agent/README.md` › 4. Follow the Work › steps 1-4 |
| 01:14 | 👥 Attendees | Their log and draft. | `labs/03-cloud-agent/README.md` › 4. Follow the Work › steps 1-4 |
| 01:29 | 🎤 Ali | **Say:** "Break. Copilot keeps working while you have coffee." | |
| **01:30-01:45** | ☕ Break | Helpers: rulesets, live versions, assignments. | |
| **01:45-02:30** | | **Build a Code Review agent: review rules and report format** | |
| 01:45 | 🎤 Ali | Paste **[B]**. Open the file: "applyTo says which files. Rules written once: your review agent checks them, and Copilot follows them, here and in the cloud." | `docs/DAY-4-BUILD.md` › 4. Build Your Code Review Agent › step 1 |
| 01:49 | 👥 Attendees | Their rules, with a last rule of their own. | `docs/DAY-4-BUILD.md` › 4. Build Your Code Review Agent › step 1 |
| 02:00 | 🎤 Ali | Paste **[C]**; change one rule. `/exit`, `copilot`, `/agent`: **code-review** beside **user-requirements**. | `docs/DAY-4-BUILD.md` › 4. Build Your Code Review Agent › steps 2-3 |
| 02:04 | 👥 Attendees | Their Code Review agent. | `docs/DAY-4-BUILD.md` › 4. Build Your Code Review Agent › steps 2-3 |
| 02:20 | 🎤 Ali | Branch `review-tools`, commit both files, **Publish Branch**, pull request, **Files changed**, merge; then `main` and **Pull**. | `docs/DAY-4-BUILD.md` › 4. Build Your Code Review Agent › step 4 |
| 02:22 | 👥 Attendees | The same. | `docs/DAY-4-BUILD.md` › 4. Build Your Code Review Agent › step 4 |
| 02:29 | 🎤 Ali | **Say:** "Two reviewers now look at Copilot's pull request: your agent and you." | |
| **02:30-03:15** | | **Report lab: run the agent on a diff and verify its findings** | |
| 02:30 | 🎤 Ali | #2's pull request (number N), **Files changed**. `/agent`, **code-review**, `Review pull request #N.` **Yes** to each command; option 2 for the read-only `gh` and `git` ones; about five minutes. In `reviews/pr-N.md` add **My check**: one **Confirmed**, one **Not a problem**, each with a reason. "Your checks decide." | `docs/DAY-4-BUILD.md` › 5. Review Copilot's Pull Request › steps 1-3 |
| 02:38 | 👥 Attendees | The same. No Copilot pull request yet: they review their own pull request from section 2. | `docs/DAY-4-BUILD.md` › 5. Review Copilot's Pull Request › steps 1-3 |
| 03:00 | 🎤 Ali | `/exit`, `copilot`, `Check out pull request #N so I can try it`. In Chat `/start-website`, each criterion; in the terminal `pytest checks`. | `docs/DAY-4-BUILD.md` › 5. Review Copilot's Pull Request › step 4 |
| 03:03 | 👥 Attendees | The same. | `docs/DAY-4-BUILD.md` › 5. Review Copilot's Pull Request › step 4 |
| 03:14 | 🎤 Ali | **Say:** "Now ask Copilot to fix what you confirmed." | |
| **03:15-03:45** | | **Iteration lab: request fixes with @copilot, retest and peer-review** | |
| 03:15 | 🎤 Ali | Comment on the pull request: **[D]**, or **[E]** when no finding was confirmed. "Peer review while Copilot works." | `docs/DAY-4-BUILD.md` › 6. Ask for Fixes and Retest › step 1 |
| 03:18 | 👥 Attendees | Their comment. From 03:22, pairs check one criterion on each other's screen. | `docs/DAY-4-BUILD.md` › 6. Ask for Fixes and Retest › steps 1 and 3 |
| 03:32 | 🎤 Ali | `Pull the latest changes of this branch.` Recheck in the preview and run `pytest checks`. `/exit`, `main` in the status bar, `copilot`: "code-review is only on main, because Copilot's branch is older." Review again; **My check** stays. | `docs/DAY-4-BUILD.md` › 6. Ask for Fixes and Retest › step 2 |
| 03:35 | 👥 Attendees | The same. | `docs/DAY-4-BUILD.md` › 6. Ask for Fixes and Retest › step 2 |
| 03:44 | 🎤 Ali | **Say:** "Decision time: merge or not." | |
| **03:45-04:00** | | **Checkpoint: review the report and decide whether to merge** | |
| 03:45 | 🎤 Ali | **Ready for review**, **Merge pull request**; leave **Reviewers** alone. "Merge if every criterion passes and no Must fix is left; otherwise close it with a reason." **Actions** green, about three minutes: the next version is live and #2 is **Done** (else **Close issue**). In the Codespace `main`, **Pull**; save the report by branch, pull request and merge. | `docs/DAY-4-BUILD.md` › 7. Checkpoint: Merge or Not › steps 1-3 |
| 03:49 | 👥 Attendees | Merge or close; their report saved. | `docs/DAY-4-BUILD.md` › 7. Checkpoint: Merge or Not › steps 1-3 |
| 03:59 | 🎤 Ali | **Say:** "Tomorrow GitHub checks every pull request for you, in a browser too. Push, then stop your Codespace." | |

**[A]** 00:32, the footer:

```text
In the footer of my first page, site/index.html, show the version from version.json, like Version 1.0.7. In my preview there is no version.json yet, so show Preview there. Change nothing else.
```

**[B]** 01:45, the review rules:

```text
Create .github/instructions/review.instructions.md with applyTo: "site/**". List my rules for every change to my website: every acceptance criterion of the ticket is met; nothing outside the ticket changed; typed text is shown safely (textContent, never innerHTML); no new internet addresses, packages, keys, or real data; the page still works with a keyboard and in a narrow window; every button says what it does. Keep it under 15 lines.
```

**[C]** 02:00, the Code Review agent:

```text
Create a custom agent file at .github/agents/code-review.agent.md with name: code-review and a one-line description. It is a Code Review agent for my website. When I give it a pull request number, it reads that pull request's changes and the ticket it is linked to, with its user story and acceptance criteria, and checks them against the rules in .github/instructions/review.instructions.md. It writes a report to reviews/pr-NUMBER.md as a table with the columns #, Severity (Must fix, Should fix, or Nice to have), File and line, What I found, Evidence (the exact line), and Suggested fix. Each finding is one or two plain sentences for a beginner. Problems that were already there before this pull request go in a separate table called "Already there before", so they do not block this change. If it cannot check something itself, it lists at most three short checks I can do by hand in the Website preview. It ends with "Verdict: Ready to merge" or "Verdict: Not yet". It never changes other files, comments on GitHub, or merges.
```

**[D]** 03:15, a confirmed finding:

```text
@copilot Fix finding 1 from my review: [what is wrong]. Change nothing else.
```

**[E]** 03:15, no confirmed finding:

```text
@copilot The Today label is small and easy to miss: make it a little bigger. Change nothing else.
```

**Running late:** 00:20, check the live version at the break · 00:50, Copilot slow? Move on and
come back to its pull request at 02:30 · 02:30, one confirmed and one rejected finding are
enough · 03:15, peer review always runs while Copilot works.

**Watch for**

- A push to `main` refused after the ruleset: expected. A branch and a pull request.
- The footer changed on an idea page: it belongs on the first page, `site/index.html`.
- A workflow-file push refused: a helper makes the same edit on GitHub with the pencil, on a new
  branch.
- The `version:` line with the wrong indentation.
- The live footer still says **Preview**: the `#` is still there, or that merge changed nothing
  in `site/`.
- **Delete codespace** offered after a merge: never.
- **Approve and run workflows** on a pull request: a helper first. It is a safeguard.
- A ticket still open after the merge: **Close issue** by hand.
- No Copilot review on pull requests: expected. Copilot code review is off.

**This evening:** #3's pull request from 01:05: review and merge it, or close it with a reason.
Before Friday, check githubstatus.com for **Actions**.

## Friday

**Day 5: CI/CD with GitHub Actions.** 30 October, four hours with the break; times count from the
start. Their guide: **docs/DAY-5-SHOWCASE.md**. Same demo website; the prepared red run is in your
spare copy. Phone at hand. Your address: `https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io`,
with `<name>` from `websiteName` in `config.json`; the feature slot adds `-feature` to the name.

| Time | Who | Do | Where in their guide |
| --- | --- | --- | --- |
| **00:00-00:20** | | **CI/CD concepts: continuous integration, delivery and deployment** | |
| 00:00 | 🎤 Ali | "Joining today? A helper starts you at the top of the Day 5 guide." The rejoin rule. | `docs/DAY-5-SHOWCASE.md` › top: **Joining today?** and Today's Route |
| 00:02 | 🎤 Ali | "Continuous integration: every change is built and tested automatically. Continuous delivery: every checked change is ready to publish. Continuous deployment: it publishes by itself; here a person approves first. Today: checks before merge, approval before release." | `docs/DAY-5-SHOWCASE.md` › 1. CI/CD in Plain Words |
| 00:10 | 🎤 Ali | `.github/workflows/publish-website.yml`: `on:` (when it runs), `permissions:` (what it may do), `version:` (the build number). | `docs/DAY-5-SHOWCASE.md` › 1. CI/CD in Plain Words |
| 00:14 | 👥 Attendees | The three lines in their own file. | `docs/DAY-5-SHOWCASE.md` › 1. CI/CD in Plain Words |
| 00:18 | 🎤 Ali | Only if on time: the Agentic Workflows demo (public preview). | |
| 00:19 | 🎤 Ali | **Say:** "Now you add the missing half: checks." | |
| **00:20-00:50** | | **Workflow lab: edit a starter YAML file, triggers and permissions** | |
| 00:20 | 🎤 Ali | Branch `ci-checks`. Paste **[A]**. Edit the top of the new file to match **[B]**. "Only the permissions it needs: these checks only read." | `docs/DAY-5-SHOWCASE.md` › 2. Workflow Lab › steps 1-3 |
| 00:25 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 2. Workflow Lab › steps 1-3 |
| 00:37 | 🎤 Ali | Commit, **Publish Branch**, pull request: both checks run (**UI check** about two minutes). Green: merge, delete the branch, never **Delete codespace**. | `docs/DAY-5-SHOWCASE.md` › 2. Workflow Lab › step 4 |
| 00:40 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 2. Workflow Lab › step 4 |
| 00:44 | 🎤 Ali | **Settings > Rules > Rulesets > Protect main**: **Require status checks to pass**, **Add checks**: **Check the website** and **UI check**, **Save changes**, **Confirm access**. "They appear only after they have run once." | `docs/DAY-5-SHOWCASE.md` › 2. Workflow Lab › step 5 |
| 00:46 | 👥 Attendees | Their checks required. | `docs/DAY-5-SHOWCASE.md` › 2. Workflow Lab › step 5 |
| 00:49 | 🎤 Ali | **Say:** "Now break it on purpose." | |
| **00:50-01:30** | | **CI lab: build and test a pull request, inspect logs and fix failures** | |
| 00:50 | 🎤 Ali | Branch `try-ci`, paste **[C]**; remove any `max-width`; commit, **Publish Branch**, pull request. Meanwhile your spare copy's red run: **UI check** red, **Merge** blocked; **Details**: "Wider than a phone screen"; **Summary > Artifacts > home-phone.png**. Then `Why did the UI check on my pull request fail? Read its log and explain in two sentences.` and `Remove the banner you just added.` Push: green, merge, `main`, **Pull**. "Red is information, not failure." | `docs/DAY-5-SHOWCASE.md` › 3. CI Lab › steps 1-6 |
| 01:00 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 3. CI Lab › steps 1-6 |
| 01:20 | 🎤 Ali | The next approved ticket in **Todo** (none left? write `Show a short welcome line under my headline` and move it to **Todo**), then **Assign to Agent**, **Assign**. "Copilot builds it during the break." | `docs/DAY-5-SHOWCASE.md` › 3. CI Lab › step 7 |
| 01:22 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 3. CI Lab › step 7 |
| 01:26 | 🎤 Ali | "Hands up: who saw red? Opened the phone screenshot? Merged on green? Has a ticket with Copilot?" | |
| 01:29 | 🎤 Ali | **Say:** "Break. Next: a test copy for every pull request, and nothing reaches production until you approve it." | |
| **01:30-01:45** | ☕ Break | Helpers: required checks, stuck runs, tickets with Copilot. | |
| **01:45-02:30** | | **CD lab: approve and deploy a build to a training environment** | |
| 01:45 | 🎤 Ali | "Two slots: the feature slot, a test copy for each pull request, and production, your own address." Branch `slots`, paste **[D]**; show the **Wait for approval** job and the `version:` line; pull request, merge on green. **Settings > Environments > New environment** `production`, **Configure environment**, **Required reviewers**: you, **Save protection rules**. | `docs/DAY-5-SHOWCASE.md` › 4. CD Lab › steps 1-2 |
| 01:50 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 4. CD Lab › steps 1-2 |
| 01:57 | 🎤 Ali | Copilot's pull request: **Files changed** first, then **Approve workflows to run**: "Nothing Copilot wrote runs until you say so." **Actions > Deploy feature slot**: **Action required**, **Approve and run** (about three minutes). On the pull request **View deployment**: the yellow strip. Check the criteria; smoke-test with **[E]**; note the **content** number. "Your own pull requests skip both approvals." | `docs/DAY-5-SHOWCASE.md` › 4. CD Lab › steps 3-5 |
| 02:03 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 4. CD Lab › steps 3-5 |
| 02:14 | 🎤 Ali | **Files changed > Submit review > Approve**, with what you tested. **Ready for review**, **Merge pull request**. **Actions > Publish my website**: **Waiting**, **Review deployments**, tick **production**, **Approve and deploy**. Smoke-test your own address: the same **content**. "Production got exactly what you tested." | `docs/DAY-5-SHOWCASE.md` › 4. CD Lab › steps 6-7 |
| 02:17 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 4. CD Lab › steps 6-7 |
| 02:27 | 🎤 Ali | "Hand up when production shows Copilot's change with the same content number." | |
| 02:29 | 🎤 Ali | **Say:** "Now ship a bad release on purpose, and bring the good one back." | |
| **02:30-03:15** | | **Recovery lab: smoke-test the app and redeploy a known-good build** | |
| 02:30 | 🎤 Ali | Run **[F]**: all **PASS**. Note **content** and **version**: "The fingerprint of your good version." | `docs/DAY-5-SHOWCASE.md` › 5. Recovery Lab › step 1 |
| 02:33 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 5. Recovery Lab › step 1 |
| 02:38 | 🎤 Ali | A new branch; `Change the sentence under my headline to Oops, wrong words. Change nothing else.` Pull request: green, and **View deployment** shows it: "Where a tester catches it." Merge anyway, approve, run **[F]**: **FAIL**. "Test before and after every release." | `docs/DAY-5-SHOWCASE.md` › 5. Recovery Lab › step 2 |
| 02:42 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 5. Recovery Lab › step 2 |
| 02:55 | 🎤 Ali | The merged pull request: **Revert**, **Create pull request**, green, merge, approve. Run **[F]**: **PASS**, the same content, a higher version. "Revert is your rollback." | `docs/DAY-5-SHOWCASE.md` › 5. Recovery Lab › steps 3-4 |
| 02:58 | 👥 Attendees | The same. | `docs/DAY-5-SHOWCASE.md` › 5. Recovery Lab › steps 3-4 |
| 03:12 | 🎤 Ali | **Say:** "Each table: one screen and one speaker, three minutes each." | |
| **03:15-03:45** | | **Team demos: show requirements, review report and CI/CD evidence** | |
| 03:15 | 👥 Attendees | By table, about three minutes each, volunteers first; you host with a timer on screen. Their board and one ticket's criteria; a confirmed and a rejected finding; red then green with a screenshot; the feature slot; an approval; the version; a rollback. | `docs/DAY-5-SHOWCASE.md` › 6. Team Demos › points 1-3 |
| 03:44 | 🎤 Ali | **Say:** "Last step: hand it over." | |
| **03:45-04:00** | | **Handoff: share agent profiles, pipeline steps and release ownership** | |
| 03:45 | 🎤 Ali | Paste **[G]**; read it, correct one sentence; branch, pull request, merge. The guide's "To make it real" table: Power Apps, Power Automate, Power BI, Copilot Studio, Novo's own GitHub Enterprise, and Novo's validation process for anything GxP. | `docs/DAY-5-SHOWCASE.md` › 7. Handoff |
| 03:48 | 👥 Attendees | HANDOFF.md merged; any automation they made switched off. | `docs/DAY-5-SHOWCASE.md` › 7. Handoff |
| 03:57 | 🎤 Ali | Thank the room. **Say:** "Push, then stop your Codespace at github.com/codespaces." | |

**[A]** 00:20:

```text
Copy .github/workflow-starters/check-my-website.yml to .github/workflows/check-my-website.yml. Then explain each job and step in one plain sentence. Do not change anything else.
```

**[B]** 00:20, the top of the file afterwards:

```yaml
on:
  workflow_dispatch:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read
```

**[C]** 00:50, the banner:

```text
Add a banner that says Sale at the very top of my first page, above its header. This is a test, so make it 900 pixels wide on every screen, even a phone: use min-width: 900px and do not let it shrink. Change nothing else.
```

**[D]** 01:45, the slots:

```text
Copy .github/workflow-starters/deploy-feature-slot.yml to .github/workflows/deploy-feature-slot.yml, and copy .github/workflow-starters/publish-website-with-approval.yml over .github/workflows/publish-website.yml. Then explain in plain sentences what starts each workflow and what it may do. Change nothing else.
```

**[E]** 01:57, smoke-test the feature slot:

```bash
python3 scripts/smoke_test.py https://<name>-feature.thankfulrock-bf005377.eastus.azurecontainerapps.io
```

**[F]** 02:30 to 02:55, smoke-test production:

```bash
python3 scripts/smoke_test.py https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io --expect-text "<the sentence under my headline>"
```

**[G]** 03:45, the handoff:

```text
Write HANDOFF.md in plain words: my agent profiles (user-requirements and code-review: file, job, and how to run them), my user-stories skill, my board and how a ticket moves from Todo to Done, my review rules, my ruleset (what it requires before a merge), my pipeline (Check my website with its tests and UI check, Deploy feature slot for every checked pull request, and Publish my website to production with approval and a version number, and what starts each), how to release and how to roll back with Revert, who owns releases (me), and open questions for IT. Add a short 'To make it real' list: which parts are made up or only in my browser today, and the route for each from the table in docs/DAY-5-SHOWCASE.md.
```

**Running late:** skip the Agentic Workflows demo · 00:50, runs slow? Show the prepared red run;
they catch up in the break · 01:57, a Copilot pull request not ready? They open their own small
one, which reaches the feature slot without approvals, and watch Copilot's two approvals on
your screen · 02:30, they can skip the oops release and smoke-test before and after; you show the
bad release and the **Revert** · demos three minutes each, volunteer tables first.

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
- An older **Deploy feature slot** run asking again after the merge: leave it.

## Preparation

**Before Monday**

- [ ] The latest template changes are on GitHub's `main` with CI green: check
      `gh run list -R agentic-dev-labs/copilot-hackathon-template -L 1`. Copies are made from
      GitHub, not from your laptop, so any later template change must reach `main` before 09:30
      on Monday too.
- [ ] Every day until Tuesday: `archive/facilitator/invitations/invite-attendees.ps1`, a dry run,
      then `-Send`; send Jackie the not-joined list. Invitations expire Tuesday 27 October at 12:15.
- [ ] Organization settings: the models attendees may use, the AI-credit budget (about 10 requests
      per `/create-website`, about 10 credits per `/publish-website`), Codespaces paid by the
      organization with a budget and a 30-minute idle timeout, and the Copilot cloud agent on for
      all repositories before Thursday. Copilot code review stays off.
- [ ] With David: the SEFR video and ASTER teaser running times, with sound tested in the room;
      whether attendees are split across the two rooms; who hosts Tuesday at 10:45 and 14:45;
      Days 3-5 start times, rooms and headcount; Friday's screen sharing, timer and demo order.
      David tries Use this template, a Codespace and `/create-website` once on a Novo laptop.
- [ ] Delete any rehearsal repository named after your username: your 09:30 live copy takes that
      name, and it stays your demo website all week.
- [ ] Monday's prepared websites in a separate repository: Weather, Princeton Map, Photo Studio and
      Lab Chase, built and checked, plus one published page. Keep its Codespace warm.
- [ ] Friday's red run: in a spare copy with the check starter merged, a pull request with the
      900-pixel banner above the header, so a finished red **UI check** is ready at 00:50.
- [ ] One practice run in a fresh Codespace with a non-owner, attendee-style account and Settings
      Sync off (synced settings hide the **Allow** prompts attendees see). Monday: the 09:30 copy,
      the 09:42 table name five times (**Retry**), the 09:52 demo (Ask on the README, then
      GenericAgent: refuses the weather, then `"execute"` and it answers), `/create-website` and the push, an own idea,
      `/add-chart`. Days 3-5: a board, `gh issue edit` updating a ticket, a workflow file pushed
      from the Codespace, **Confirm access**, **Assign to Agent**, the `production` environment
      form, and whether **Create Pull Request** asks to sign in.
- [ ] The version footer live on a practice website before Thursday.
- [ ] Print the quick reference, `docs/QUICK-REFERENCE.md`, for every table.
- [ ] Monday 08:30 welcome desk, for anyone not yet in the organization. Remote attendee BQMC: a
      Teams link and a named helper.
- [ ] Picture quota: with a full room most Photo Studio edits fall back to another model. Ask for
      more, or say so at 13:00.
- [ ] Decide whether published websites stay awake all week: `MIN_REPLICAS` in
      `.github/workflows/website-publisher.yml`. It is 0, so a first visit after a quiet spell
      takes about 30 seconds; 1 costs about USD 9 a day for 45 websites.

**Evenings:** Monday, publish your copy if you did not at 14:20. Wednesday and Thursday end with a
**This evening** line above.

**After the week**, each step agreed with David first: remove attendee members (it stops seat
billing) and cancel pending invitations; archive the repositories and delete the published
websites; set `MIN_REPLICAS` back to 0 if you raised it; check the Thursday automation is off. The
`FOUNDRY_*` client secret expires on 1 November: renew it or delete it.

Old notes, the agenda and the setup guides are in `archive/`. You do not need them on the day.
