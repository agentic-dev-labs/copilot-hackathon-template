# Delivery: Ali's Minute-by-Minute Script

**Always look in this folder.** [WEEK.md](WEEK.md) is the overview and every slot's timings; this
file is how to deliver them: the minutes inside each slot, the words to say, the cuts, what to drop
when late, what goes wrong, and the preparation lists. Day 1-2 times are clock times; Days 3-5 are
elapsed from the session start, as on David's slides ([1](../1.png), [2](../2.png), [3](../3.png),
[4](../4.png), [5](../5.png)).

Private and git-ignored with this folder; never commit it. It is the only delivery script: the
earlier `facilitator/DELIVERY-SCRIPT.md` is gone, and nothing outside this folder holds the plan.

## How Every Block Runs

| Mode | What happens | What Ali says |
| ---- | ------------ | ------------- |
| TALK | A speaker presents. Laptops stay closed or idle. | - |
| SHOW | Ali shows one step for 2-5 minutes. Hands off keyboards. | "Eyes up." |
| WITH | Everyone clicks along with Ali, one click at a time. Used only for the 09:30 copy and Codespace. | "Do it with me." |
| DO | Attendees repeat the step on their own repository, from the page named on screen. Ali and the helpers walk the room. | "Your turn: open [page], section [n]." |
| CHECK | One visible result, signalled by a raised hand or a thumbs up. | "Hand up when you see ..." |
| CUT | At the planned minute everyone moves on, finished or not. | "Hands off. Wherever you are is fine. Next: [page], section [n]." |

- **Keep the current block on screen.** Put the block name and the page to open in a corner of the
  shared screen, or on the second screen. A lost attendee only needs that line.
- **The rejoin rule**, said on Monday at 10:45 and at the start of every later day: "Lost? Find the
  row we are on in Today's Route, open its link, and start there. Raise your hand." Every attendee
  guide carries the same **Lost?** line.
- **Nobody stays behind alone.** At a cut, a stuck attendee moves on with the room; a helper
  finishes the skipped step with them during the next DO or the break. Helpers point; they never
  type on an attendee's keyboard.
- **Helpers:** one per 8-10 people, each with fixed tables. At every CUT each helper scans their
  tables and raises a hand to Ali if more than two people are blocked on the same thing: that is
  a room problem, so show the fix on the big screen once.

## Before the Week

- [ ] Run `facilitator/invitations/invite-attendees.ps1` daily (dry run, then `-Send`), and send
      Jackie the not-joined list. Send the two Outlook drafts (Shihan, the EMU tip) once reviewed.
- [ ] GitHub settings (UI): models (Claude Haiku 5.5, Claude Sonnet 5.5, GPT-5.6 Luna and Auto; the
      STATUS list leaves out Luna, so decide), the AI-credit budget (measured 19 October: about 10
      requests per `/create-website`, about 10 credits per `/publish-website`; every request also
      carries about 45,000 tokens of always-loaded instructions from `AGENTS.md` and
      `.github/copilot-instructions.md`, and trimming them for attendee copies is still open),
      Codespaces paid by
      the organization with a budget and a 30-minute idle timeout, and the Copilot cloud agent on
      for all repositories (Day 4), budgeted for one session per attendee plus follow-ups.
      **Copilot code review stays off** (decided 21 October).
- [x] Template changes pushed to `main` on 22 October (`550015a`, then `69f78a8`); CI is green,
      including the `ui-check` job with the browser sandbox on.
- [ ] Prove the publisher's `version` input live: a practice website with `version:` switched on,
      its first page's footer and `/healthz` showing the version.
- [ ] David on a Novo laptop in the office: Use this template, Codespace, Chat in Agent,
      `/create-website`, Project Planner, and the Website preview shows it.
- [ ] Confirm with David: who restarts the room at 10:45 on Tuesday and who hosts 14:45; Bill
      Leeson's 11:45 talk; Day 3-5 start times, rooms and expected headcount.
- [ ] **Day 1 demo repository**, separate from the live copy you make at 09:30: Weather, Princeton
      Map, Photo Studio and Lab Chase built and checked, plus one published page. Keep its Codespace
      warm. Delete any rehearsal repository named after your username, so your live copy can take
      that name.
- [ ] **Day 3 demo website** (a Project Planner copy): two or three Requirement tickets (the first
      is "Mark urgent tasks"; "hide finished" was Monday's 11:45 button) and a Board project named
      `alfarahn website`, made with **Import items from repository**. Check once with an
      attendee-style account in a Codespace: members may create projects, the board shows in the
      repository's **Projects** tab, new tickets land on it, `gh issue edit` may update a ticket
      (if refused, attendees paste by hand), and a `Closes #N` commit moves the card to **Done**.
- [ ] **Days 4-5 demo repository:** the `Protect main` ruleset, the version showing live, and the
      check starter merged once, so **Check the website** and **UI check** can be picked as required
      checks. Push a branch that changes `.github/workflows/` from a real Codespace; if refused,
      the fallback is the GitHub web editor, committing to a new branch.
- [ ] **The evening before Day 4:** assign an approved demo ticket to Copilot, so its pull request is
      ready; set up the criteria automation from Lab 03's extras on the demo repository (user-stories
      skill on `main`; **Agents > Automations**, trigger "issue created", filter
      `label:enhancement`). It runs as you, on your allowance: disable it after Thursday.
- [ ] **Before Day 5:** a red pull request on the demo repository (the 900-pixel banner above the
      header), so the log table and `home-phone.png` are ready while the live run is still going.
- [ ] One run-through of Monday in a fresh attendee-style Codespace, with a non-owner account and
      Settings Sync off (your synced extensions slow it and hide the **Allow** prompts attendees
      see): the 09:30 copy, the 10:00 `/create-website` and push, the 10:45 own idea, and the 13:00
      `/add-chart`. **Not yet done for prompts:** the 22 October rehearsal ran in a browser whose
      synced settings auto-approve every terminal command (`"/.*/": true`), so it showed no
      **Allow** prompts at all. Count them per build in this run, and if the preview helper's
      prompt is the only one, consider a narrow workspace rule for it. With the same account,
      check the owner-only steps of Days 3-5 that the 22 October run could not prove: pushing a
      workflow file from the Codespace, the ruleset's **Confirm access**, **Assign to Agent**, the
      `training` environment form, and whether **Create Pull Request** in VS Code still asks to
      sign in to GitHub Enterprise.
- [ ] Rehearse the 09:42 table-name step in that Codespace, in **Ask**, on the model attendees get:
      five tries in the first chat (**Retry** under the answer asks again), noting how many
      different names you see. Checked through Copilot CLI with the repository's instructions on
      23 October: just a name in 15 of 15 tries; different names in 5 tries: Auto 4, Claude Haiku
      5.5 3, GPT-5.6 Luna 3.
- [ ] Two notices a fresh Codespace shows: Chat's "customization migrations" banner (prompt files to
      skills, `.vscode/mcp.json` to `.mcp.json`) and Ruff's "No Python environment extension"
      message. Migrate, or drop the Ruff editor extension for attendees, before Monday; otherwise
      tell the room at 09:37, as the Codespaces open, to ignore both.
- [ ] Pictures: gpt-image-2 allows about two edits a minute, so with a full room most Photo Studio
      edits fall back to FLUX Kontext. Request more quota, or say at 13:05 that the picture model
      may vary.
- [ ] Decide whether websites stay awake all week: `MIN_REPLICAS: 1` in the publisher from Monday to
      Friday (about USD 9 a day for 45 websites), back to 0 afterwards; see `infra/README.md`. It is
      0 today, so a first visit after a quiet spell takes about 30 seconds.
- [ ] Print the day's page of [WEEK.md](WEEK.md) for each helper, and the attendee
      [quick reference](../../docs/QUICK-REFERENCE.md) for every table.
- [ ] Remote attendee BQMC (North Carolina): a Teams link and a named helper.
- [ ] 08:30 welcome desk on Monday: anyone not yet in the organization joins there. Pending
      invitations expire Tuesday 27 October at 12:15 Princeton time.

## Every Morning, 30 Minutes Before

- [ ] The demo Codespace open and warm; browser zoom about 150%; notifications off; personal MCP
      servers disabled for this workspace (**MCP: List Servers**, each one, **Disable**).
- [ ] The day's guide open in a tab, and this run sheet on a second device or printed.
- [ ] Five-minute helper huddle: their tables, the rejoin rule, and the day's **Watch for** list.
- [ ] The first page to open on screen as people sit down: Monday the template link; Tuesday the
      Day 2 guide; Wednesday to Friday that day's guide.

## Day 1, Monday 26 October: GitHub and Your First App

Rooms MKC 1D412 and 1D413. Until 10:30 attendees use only their repository's README; from 10:45
the route is `docs/START-HERE.md`.

| Time | Mode | Ali: shows and says | Attendees: do, and where |
| ---- | ---- | ------------------- | ------------------------ |
| 08:30 | - | Welcome desk open; the template link on screen. | Seated, browser signed in to GitHub |
| **09:00–09:30** | | **Sponsor welcome (SEFR video), ASTER Overview teaser (HZRW), glossary and GitHub basics (concepts only)** | **README › This Is GitHub** |
| 09:00 | TALK | The sponsor's SEFR video, then HZRW's ASTER teaser. Agree their running time with David; the tour gets the rest. | Listen |
| 09:15 | SHOW | On the template: files, README, **Commits**, a file's **History**, search with **/**, **Issues**. "A repository is a folder with a memory: every snapshot you send up stays, and you can go back to it." The five words, then: "Saving keeps it on your screen. Pushing sends it to GitHub. The order is always save, review, commit, push." | Watch; look along on the template, changing nothing |
| 09:28 | CUT | "Now you make your own copy, one click at a time, with me. Make exactly one." | README › Find Your Files and Copilot Chat |
| **09:30–10:00** | | **Lab: Find files and Copilot Chat, ask and refine a question** | **README › Find Your Files and Copilot Chat** |
| 09:30 | WITH | **Use this template > Create a new repository**: owner **agentic-dev-labs**, name = your GitHub username, **Private**, **Create repository**. "Check the top of the page: agentic-dev-labs, your name, Private. Anything else: hand up." | Step 1 with Ali. Helpers fix anyone who cannot pick agentic-dev-labs |
| 09:37 | WITH | **Code > Codespaces > Create codespace on main**. While it loads: "This is your repository: the same files, this page, one snapshot under Commits." **Trust Folder & Continue**: "It is your own copy, and your website preview needs it." Explorer, README, **Open Preview**. If Chat's migrations banner or Ruff's message appears: "Ignore both." If the bottom right says **Sign In**, or the list shows only **Agent**: "Select Sign In once." | Steps 2-4 with Ali |
| 09:42 | SHOW | **View > Chat** (the three-line menu at the top left), **Ask**: "Ask only answers; it never changes your files." "Everyone will ask Copilot exactly the same thing. Watch mine first." Type "Invent a fun name for my workshop table. Reply with the name only." and read the name out. | Watch |
| 09:44 | DO | Walk the room. Then hands up: "Who got the same name as their neighbour?" Many hands: "A likely name comes up often, but not always." Few hands: "Same question, different answers." Either way: "Copilot does not look the name up: it writes a new answer each time, picking likely words. That is why you check its work." | Steps 5-6: Chat in **Ask**, their table name compared with a neighbour's, then hands up |
| 09:48 | SHOW | Same chat: the three-sentence question, then "Use an everyday example and make it shorter." "A better question gives Copilot more to go on. Stay in this one chat all day: a new chat starts a slower kind of session." | Watch |
| 09:50 | DO | Walk the room; helpers finish any copy or Codespace that is not open yet. | Steps 7-8: their question, checked against the five words, then refined |
| 09:57 | CHECK | "Hand up if Chat answered your question and your follow-up." Helpers note anyone without a Codespace. | |
| 09:59 | CUT | "Switch Chat from Ask to Agent. Agent can change your files, and you check every change." | README › Your First Website |
| **10:00–10:30** | | **Create an idea note, save, review, commit, push and verify** | **README › Your First Website** |
| 10:00 | SHOW | **Agent**, `/create-website`, **Project Planner**; about 50 seconds later it opens beside Chat (if Chat asks to run `python3 scripts/website_preview.py start`: "That opens your preview: Allow. Anything else you don't understand: hand up."); **+** a made-up entry. "You just built a website by talking. The proof is the new file in Explorer > site, not Copilot saying done." Then **Keep** under the chat box: "Keep accepts the change. Undo takes back everything you have not kept, so keep what you like." | Watch |
| 10:05 | DO | Walk. | Steps 1-3: their first website (the Project Planner if unsure) |
| 10:15 | SHOW | `site/brief.md`: "This is the idea note on David's slide. Copilot wrote it; you add to it all week." **File > Save All** (grey means already saved: the Codespace saves by itself), Source Control ("about 30 files the first time: expected"), **+** on **Changes**, `Add my first website`, **Commit**, **... > Push**, then GitHub, **site**, **brief.md**. | Watch |
| 10:19 | DO | Walk. | Steps 4-5: saved, pushed, found on GitHub |
| 10:28 | CUT | "Break. Not on GitHub yet? Stay seated: a helper finishes it with you now." | |
| 10:30 | BREAK | Switch to the warm demo Codespace. | Helpers: every page on GitHub |
| **10:45–11:45** | | **Lab: Create a website with /create-website and preview it** | **Lab 01** |
| 10:45 | SHOW | "From now on your route is START-HERE, and I name the section every time. Lost? Find the row we are on, open it, start there." Then, saying they are prepared: Weather in 3D (drag the chart), Princeton Map (the History filter, then 3D), Photo Studio (the sleepy cat becomes a watercolor), Lab Chase (20 seconds, get caught by a meeting invite). "All of these were made the way you made yours: by describing them." | Watch (Lab 01, section 1) |
| 10:55 | SHOW | Back in your live copy: `site/index.html`, select five lines, "Explain the lines I selected in plain English...". **Ctrl+F** `<h1>`, change two words, save, the preview updates. "Code is only text, and you just changed it with your own hands." | Watch |
| 11:00 | DO | Walk. | Lab 01, section 2: lines explained, headline changed by hand |
| 11:10 | SHOW | `/create-website` again; it asks in plain words, so answer "build my own idea": "A tracker for team requests with stages Submitted, Doing and Done." Talk over the build (under two minutes): it gets its own folder in `site/ideas/`. Then "Make the headline friendlier. Leave the rest alone.", and **Keep**. "Your first page stays exactly as it is." | Watch |
| 11:14 | DO | Walk; watch for Copilot changing the first page. | Lab 01, section 3: one own idea in its own folder |
| 11:30 | SHOW | **Save All**; Source Control lists only what changed; commit, push; the idea's folder on GitHub. | Watch |
| 11:32 | DO | Walk. | Lab 01, section 4: shown to a neighbor, pushed |
| 11:44 | CUT | "Eyes up. Now you are the checker." | Lab 01 › Coached Verification Block |
| **11:45–12:15** | | **Trust but verify: check a button and a figure, fix and recheck** | **Lab 01 › Coached Verification Block** |
| 11:45 | SHOW | `/start-website` opens the first page. Ask for "hide finished tasks". "I expect the ticked task to disappear." Click it twice; compare. "Copilot can be wrong; you are the checker. 'Copilot says it works' is not a check." | Watch |
| 11:49 | DO | Walk. | Step 1: one button checked |
| 11:55 | SHOW | Count it: the sheet's example says 1 of 4, but with this morning's task it is **1 of 5 done**; tick one: **2 of 5**. "Count what is on your page, not what the sheet says. If yours is wrong, say: I expected ..., I saw ... Then check again." | Watch |
| 11:57 | DO | Walk. | Step 2: one number counted, from the table |
| 12:05 | SHOW | What you tried and what happened, written in `site/brief.md`; save, commit, push. | Watch |
| 12:07 | DO | Walk. | Step 3: written down and pushed |
| 12:14 | CUT | "Lunch. Push first; your Codespace waits for you." | |
| **13:00–14:00** | | **Lab: Add a useful interaction, personalize and check** | **Lab 02** |
| 13:00 | SHOW | The three features: a chart, a chat, a picture. "Pick one; a chart if unsure." | Lab 02, section 1: they pick |
| 13:05 | SHOW | `/add-chart`, the **Progress gauge** or the 3D **Week skyline** (drag it); about a minute; it asks whether you can see it: **Yes**, then **Keep**. Mention `/add-chat` ("How many tasks are done?") and a picture ("the picture model may vary when the whole room asks at once"). | Watch |
| 13:09 | DO | Walk. | Lab 02, section 2: their feature added |
| 13:20 | SHOW | Tick a task: the chart follows. Count it yourself. "A chart, and a chat, can be wrong too." | Watch |
| 13:23 | DO | Walk. | Lab 02, section 3: checked against their own count |
| 13:35 | SHOW | "Try a sky blue look. Keep everything else the same." Then **Keep**. Then "bright purple, giant text" (about a minute), **Undo**, **Yes**. "Undo takes back everything you have not kept: that's why we kept the chart and the look first. Now you know you can always go back." | Watch |
| 13:39 | DO | Walk. | Lab 02, section 4: one look change and one **Undo** |
| 13:50 | DO | Walk. | Lab 02, section 5: written in the brief, shown to a neighbor |
| 13:59 | CUT | "Now we save it and look back in time." | Lab 08 |
| **14:00–14:45** | | **Lab: Save, share and keep building (publication optional)** | **Lab 08** |
| 14:00 | SHOW | Source Control, **+**, the sparkle icon writes the message; fix one word; commit; push. "Read what it wrote: you sign it." | Watch |
| 14:03 | DO | Walk. | Lab 08, section 1 |
| 14:10 | SHOW | GitHub **Commits** (in a narrow window only the clock icon shows), `Add my first website`, the green lines; `site/index.html`, **History**. "A time machine for your work." | Watch |
| 14:13 | DO | Walk. | Lab 08, section 2 |
| 14:20 | SHOW | The challenge card: Bronze, Silver, Gold. Optional: `/publish-website` on your page, then push; it is live in about three minutes. | Watch |
| 14:22 | DO | Helpers help anyone who wants to publish. | Lab 08, section 3: one challenge level |
| 14:35 | DO | Open your published link yourself a minute before (a sleeping website takes about 30 seconds to wake), then put it on screen: the room opens it on their phones. | Lab 08, section 4: shown to a neighbor, next idea in the brief |
| 14:44 | CUT | "Pair sharing: one feature, and how you checked it." | |
| **14:45–15:00** | | **Pair sharing and selected volunteer demonstrations** | **START-HERE › Today's Route** |
| 14:45 | DO | Pick two or three volunteers while pairs share. | Pairs: one feature and its check |
| 14:50 | SHOW | The volunteers on the big screen, about two minutes each. | Watch |
| 14:58 | CUT | "Push, then stop your Codespace at github.com/codespaces. Tomorrow the green Code button reopens the same one." | |

**If late:** at 09:44 skip the attendees' own table names (step 6): they saw yours on screen, so
say the lesson and go straight to the question. If 09:30 runs over, finish the first websites in
the break with helpers and never shorten Lab 01. At 10:45 show two prepared websites (Weather and Lab Chase) instead of four. At
13:00 skip the picture mention; the sketch stays optional. At 14:20 drop your own publishing.

**Watch for:** a whole table with the same name (fine: a likely name comes up often; ask who got a
different one); **Sign In** at the bottom right, or only **Agent** in the list (select **Sign In**
once); a chat that says
**Copilot** or **Manual permissions** at the bottom, with no **Keep** or **Undo** (someone chose
**New Chat**: go back to the first chat, or start one and choose **Local** before typing); not in
the organization yet (cannot pick agentic-dev-labs as owner: a helper or
the welcome desk); a second repository or Codespace; **Trust Folder** declined (Reload Window and
trust); "Codespace is stopped" after lunch (**Restart codespace**: about a minute, nothing lost);
Chat still in **Ask** at 10:00; unsaved files; the preview closed (`/start-website`, or
`/start-website <folder>` for an idea); Copilot changing the first page instead of making a new
folder (**Stop**, **Undo**, "Build my own idea in its own folder"); an **Undo** that also removed
the chart or the look (they were not kept: ask again, then **Keep**); a commit with an empty
message opening a `COMMIT_EDITMSG` tab (close it, type the message in the box, commit again);
the side bar vanishing after a click on the Source Control icon that was already open (click it
again); a diff where the whole file changed (the attendee's own Format On Save setting: harmless);
the chat saying the assistant is off (add a chart instead and tell a helper); any real data (it
stays made up).

## Day 2, Tuesday 27 October: Your Own Business Idea

Not Ali's day to present: David, Jackie and Bill Leeson give the talks, and Ali is table support.
Use `facilitator/ideas/TABLE-SUPPORT.md` to nudge ideas towards the Request Tracker or the Team
Dashboard pattern.

| Time | Mode | Ali, at the tables | Attendees: do, and where |
| ---- | ---- | ------------------ | ------------------------ |
| 09:00 | TALK | David: Business/IT roles, approved tools and AI marketplace. Note questions to take to the tables. | Listen |
| 09:30 | TALK | Jackie: Power Platform, Dataverse and connector examples. | Listen |
| 10:30 | BREAK | Every table: reopen Monday's Codespace from the green **Code** button, **Codespaces**, its name. Never **Create**. | Day 2 guide › Today's Route |
| 10:45 | DO | The host restarts the room in one minute: "Open docs/DAY-2-BUILD.md, Morning Build. Tell your helper your four answers. Lost later? Find the row for the time now." | Morning Build, step 1: four answers agreed (10 minutes) |
| 10:55 | DO | Help build; steer each idea to a tracker or a dashboard. | Step 2: one page built or continued (35 minutes) |
| 11:30 | CUT | Each table: "Save and push now: Bill starts at 11:45." | Step 3: saved and pushed (15 minutes) |
| 11:45 | TALK | Bill Leeson: Building a Project Brain. | Listen |
| 13:00 | DO | At the tables. | Improve One Interaction |
| 14:00 | DO | Help with `/publish-website` for anyone who wants it. | Fixes and Optional Publishing |
| 14:45 | DO | The host runs the volunteers. At 14:52, every table: two or three **Next** wishes in the brief, pushed. | Show and Plan the Next Step |

**Watch for:** an own idea replacing Monday's page (it gets its own folder in `site/ideas/`); real
names or data in pages or prompts; integration wishes such as Outlook, PDFs or SharePoint (onto the
questions-for-IT list, not into the page); anyone leaving without **Next** wishes: they are
Wednesday's tickets.

## Day 3, Wednesday 28 October: VS Code and a Requirements Agent

Four hours, elapsed. Before 00:00 and from 00:20, a helper gets anyone without a website started
with the Project Planner (the guide's **No website yet?**).

| Time | Mode | Ali: shows and says | Attendees: do, and where |
| ---- | ---- | ------------------- | ------------------------ |
| **00:00–00:20** | | **MUKQ: Global and Microsoft perspectives on AI development** | |
| 00:00 | TALK | MUKQ presents. Ali: the demo website, its board, and a signed-in terminal ready. | Listen |
| **00:20–00:50** | | **Ali: workspace setup, repo walkthrough and agent roles/tools** | **Day 3 guide, section 1** |
| 00:20 | SHOW | "Your Tuesday wishes become tickets today, on your own board." The organization's name, **Projects > New project > Board**, `alfarahn website`; keep **Import items from repository** and switch **Repository** to your own ("it shows the template first"); **Create project**. Then **Workflows > Item added to project > Off**: "Otherwise GitHub drops every new ticket straight into Todo, and approving is your job. Todo means approved, In Progress being built, Done finished." Then the repository's **Projects** tab. | Watch |
| 00:24 | DO | Walk; check each board names the attendee's repository and the workflow says Off. | Section 1, steps 1-2: their board |
| 00:31 | SHOW | **Issues > New issue > Requirement**: "Mark urgent tasks", **What I want** in plain words, **Which page**, **Create**: #1, and it appears on the board under **No Status**. "A ticket is one thing you want next. Your agent adds the details later." | Watch |
| 00:34 | DO | Walk. | Section 1, steps 3-4: two or three tickets from their **Next** wishes |
| 00:39 | SHOW | The Codespace, **Terminal > New Terminal**, `copilot`: the model name on the bottom line means it is signed in (`/login` with the device code only if it asks). Then "Use the GitHub tools to list the open issues in my repository, with their numbers. Do not change anything." Point at **List issues** above the answer: "That line is MCP: a plug that lets Copilot act on GitHub. Reading runs straight away; anything that changes something asks first." "The same assistant as Chat, through another door." Agent roles: "Ask answers. Agent changes files. A custom agent is a helper with one job. Tomorrow the cloud agent works on GitHub by itself." | Watch |
| 00:42 | DO | Walk; anyone stuck in the terminal switches to Chat with **Agent**. | Section 1, steps 5-7: signed in, tickets listed |
| 00:49 | CUT | "Keep the terminal open. Eyes up: now you write your own helpers." | Section 2 |
| **00:50–01:30** | | **Build a User Requirements agent: instructions and output format** | **Day 3 guide, section 2** |
| 00:50 | SHOW | Start with Monday's skill: open `.github/skills/create-website/SKILL.md`. "Remember `/create-website`? This is the recipe behind it, written mostly in plain sentences. Today you write your own, much shorter." Then the four building blocks in the Explorer: `.github/copilot-instructions.md`, `.github/skills/`, `.github/agents/`, `.vscode/mcp.json`. `/agent`: "None yet: yours arrives next. The warning about two workshop files is for a later example: ignore it." "Instructions are standing rules, a skill is a recipe, an agent is a role card, a tool is a plug. A skill says how; an agent says who." | Watch (section 2, steps 1-2) |
| 00:56 | SHOW | Paste the skill prompt. It asks to read **docs.github.com** pages: "GitHub's own help: choose 2, for the rest of this session." It shows the new file beside the terminal: **Yes**. Open `SKILL.md`: "The name and description decide when Copilot loads it." Change one step. | Watch |
| 00:59 | DO | Walk. | Section 2, steps 3-4: their skill, one step in their words |
| 01:09 | SHOW | Paste the agent prompt ("my small website about a project planner"); open the agent file; change one rule. "It shows you a draft first, and changes the ticket only after your yes. The long `gh` part keeps your own words safe: paste it as it is." | Watch |
| 01:12 | DO | Walk. | Section 2, steps 5-6: their agent, one rule in their words |
| 01:22 | SHOW | `/exit`, `copilot`, `/agent`: **user-requirements** is listed. "One file, two doors: it is in Chat's agent picker too." | Watch |
| 01:24 | DO | Walk. | Section 2, step 7: the agent listed |
| 01:29 | CUT | "Break. After it, your agent writes its first criteria. No agent yet? A helper sits with you now." | |
| 01:30 | BREAK | | Helpers: missing skills and agents |
| **01:45–02:30** | | **Agent lab: draft user stories and acceptance criteria, then validate** | **Day 3 guide, section 3** |
| 01:45 | SHOW | `/agent`, **user-requirements**, "Write the user story and acceptance criteria for issue #1." (a ticket list pops up at `#1`: **Esc** once, then Enter). It may ask a question first; answer it. Read the draft. For each criterion: "Can I check it by clicking or counting?" Rewrite one: "Rewrite criterion 2 so that I can check it by counting. Change nothing else." "Validate here means checkable, not GxP validation." Then **Yes**; it re-reads the ticket and asks to run the save (rehearsed: a short Python script around `gh issue edit`): "It checks your words stay the same; allow it." Show the ticket on GitHub: "Your own words are still there. Always check that." | Watch |
| 01:52 | DO | Walk; `gh` refused: paste the draft by hand. A ticket that lost its own words: the ticket's **edited** menu shows the earlier version to copy back, and the agent file needs the guide's full prompt. | Section 3, steps 1-3 on their first ticket |
| 02:10 | DO | Walk. | Section 3, step 4: their other tickets |
| 02:20 | SHOW | On the board, one card into **Todo** for today and one for tomorrow. "Moving it to Todo is your approval: you are the product owner." Ask a neighbor to check one ticket's criteria. | Watch |
| 02:23 | DO | Walk. | Section 3, step 5: two tickets in **Todo** |
| 02:29 | CUT | "Eyes up. We build the one you approved for today." | Section 4 |
| **02:30–03:15** | | **Build lab: implement an approved story, debug and verify the fix** | **Day 3 guide, section 4** |
| 02:30 | SHOW | `/exit`, `copilot`; the card to **In Progress**; "Read issue #1 with the GitHub tools and build it in site/index.html. Change only what it needs and keep everything else. Do not run tests or scripts: I check it myself. Then list how I can check each acceptance criterion." (Rehearsed: without that sentence it wrote and asked to run an 86-line test script, about four minutes.) Read the change before allowing it; `/start-website`; each criterion checked by hand. Then the debug sentence: "Criterion 2 of issue #1 fails. I expected [this]. I saw [that]. Fix only that." "That is the most useful sentence of the week." | Watch |
| 02:37 | DO | Walk; every criterion checked by hand, not on Copilot's word. | Section 4, steps 1-5 |
| 03:05 | CHECK | "Hand up if every criterion passes your own check." One volunteer tells a 30-second debug story. | |
| 03:14 | CUT | "Now the computer re-checks it for you: tests." | Section 5 |
| **03:15–03:45** | | **Team build: add tests and document build and run commands** | **Day 3 guide, section 5** |
| 03:15 | SHOW | The test prompt writes `checks/test_issue1.py`; `pytest checks` is green; change a word a test looks for: red, with its message; **Ctrl+Z**: green. "A test is a check the computer repeats for you after every change." | Watch |
| 03:20 | DO | Tables help each other and compare tickets. | Section 5, steps 1-3 |
| 03:32 | SHOW | The brief prompt: "How to build and run" and a **Requirements** list (ticket, story, status). "This is David's validated brief: each requirement traced to its ticket, and how to run it." | Watch |
| 03:35 | DO | Walk. | Section 5, step 4 |
| 03:44 | CUT | "Last step: close the ticket with a commit." | Section 6 |
| **03:45–04:00** | | **Checkpoint: show the agent, requirements and working feature** | **Day 3 guide, section 6** |
| 03:45 | SHOW | Source Control: skill, agent, page, test and brief; commit `Mark urgent tasks. Closes #1`; **... > Push**; the board moves the card to **Done** by itself. | Watch |
| 03:48 | DO | Walk. | Section 6, steps 1-2 |
| 03:54 | DO | Walk. | Section 6, step 3: four things shown to a neighbor |
| 03:59 | CUT | "Tomorrow Copilot's cloud agent builds the ticket waiting in Todo. Bring your phone: GitHub asks for your sign-in code when you change your repository's settings. Push, then stop your Codespace." | |

**If late:** at 00:20 make the board and write one ticket now, and the rest at 01:45; never put
the board off until after the tickets, because a late import drops them all into **Todo**. At
00:50 the "change one step" and "change one rule" edits become optional. At 01:45 put
criteria on only the two tickets to approve. At 02:30 debug only when a criterion fails. At 03:15
the brief's sections can be pushed with the 03:45 commit.

**Watch for:** no **New project** (an organization setting: add cards with **+ Add item** and `#`);
a board that imported nothing (**Repository** left on the workshop template: add the cards with
**+ Add item** and `#`, and point **Workflows > Auto-add to project** at their repository); new
tickets landing in **Todo** (the **Item added to project** workflow is still on: switch it off,
write the next ticket, then drag the others into **No Status**, gripping the card beside its
title); tickets about what the page already does ("What do you want next?"); a terminal too short
to show Copilot's question (**Maximize Panel Size**, the square at its top right); a
`docs.github.com` reading prompt (option 2); a ticket that lost the attendee's own words (the
agent was made from a shortened prompt: copy the words back from the ticket's **edited**
history and recreate the agent with the guide's full prompt); `gh issue edit`
refused (paste the draft by hand); the agent missing from `/agent` (`/exit`, `copilot`); a commit
without `Closes #1` (close the ticket by hand; the board still moves it); anyone stuck in the
terminal (the same sentence in Chat with **Agent**).

## Day 4, Thursday 29 October: GitHub Copilot Cloud Agents

Four hours including the break, elapsed.

| Time | Mode | Ali: shows and says | Attendees: do, and where |
| ---- | ---- | ------------------- | ------------------------ |
| **00:00–00:20** | | **Cloud-agent overview: delegation, safeguards and human review** | **Day 4 guide, section 1** |
| 00:00 | - | "Joining today? A helper starts you at the top of the Day 4 guide." | Newcomers: **Joining today?** with a helper |
| 00:02 | SHOW | The road, on a real pull request: feature branch, pull request, your review, merge, pipeline, live with a new version number. "Nobody pushes straight to main, not even you." | Listen |
| 00:05 | SHOW | On the demo repository, **Issues > New issue > Requirement**, a new wish; nobody assigns it. "Watch this ticket: we come back to it in ten minutes." | Listen |
| 00:07 | SHOW | Delegation and safeguards: an approved ticket assigned to Copilot works on its own `copilot/` branch, opens a draft pull request, and its checks wait for your approval; it follows your instructions and skills. "Delegating the work does not delegate the checking." | Listen |
| 00:12 | SHOW | Human review: you read **Files changed**, try it, and decide, helped by your own Code Review agent. | Listen |
| 00:15 | SHOW | Back to the ticket: the story and criteria arrived by themselves. "An agent that fires against the repository. You can set one up as an optional extra." | Listen |
| 00:18 | CHECK | Two volunteers say the road back. | |
| 00:19 | CUT | "First the rules, then one small change down the road." | Section 2 |
| **00:20–00:50** | | **GitHub lab: practice branches and pull requests with a small change** | **Day 4 guide, section 2** |
| 00:20 | SHOW | "No address yet? `/publish-website`, save, commit and push now: after the ruleset, main takes only pull requests." | Watch |
| 00:22 | DO | Walk. | Those without an address publish; the others read step 1 |
| 00:25 | SHOW | **Settings > Rules > Rulesets > New branch ruleset**: `Protect main`, **Active**, **Include default branch**, **Require a pull request before merging** with 0 approvals, the bypass list empty, **Create**; GitHub asks to **Confirm access** with your authentication app (rehearsed). "Zero approvals: you are alone in your repository, so you check before you merge. That code is yours alone: nobody else types it." | Watch |
| 00:28 | DO | Walk. | Section 2, step 1 |
| 00:32 | SHOW | Branch `feature/version-number`; in `publish-website.yml` delete the `#` and the space before `version:`, keeping the indentation; the footer prompt, on the first page `site/index.html` (the address opens that page): **Preview** in the preview. "The run number is the build number: it goes up by one with every run." | Watch |
| 00:36 | DO | Walk. | Section 2, steps 2-4 |
| 00:42 | SHOW | Commit, **Publish Branch**, **Create Pull Request** (if VS Code asks to sign in, as it did in the rehearsal: GitHub's yellow **Compare & pull request** banner instead), **Files changed**, merge, delete the branch ("GitHub now offers **Delete codespace**: never. That is your Codespace."), **Actions**, the live footer **Version 1.0.N**; back to `main` and **Pull**. | Watch |
| 00:44 | DO | Walk; a slow run is checked at the break. | Section 2, steps 5-8 |
| 00:49 | CUT | "Your version appears in a couple of minutes. Now Copilot builds your next ticket." | Lab 03 |
| **00:50–01:30** | | **Delegation lab: assign an approved requirement to Copilot** | **Lab 03** (Day 4 guide, section 3) |
| 00:50 | SHOW | The board, a ticket in **Todo**, its criteria read once more: "Could a stranger tell when it is done?" **Which page** names the right page. | Watch |
| 00:53 | DO | Walk. | Lab 03, sections 1-2: a ticket picked and checked |
| 01:05 | SHOW | **Assign to Agent** under **Assignees** (or **Assignees > Copilot**): base branch `main`, agent **Copilot**, **Assign**. Rehearsed: within a minute a draft pull request appears and the board moves the card to **In Progress** by itself. Then the session link. | Watch |
| 01:07 | DO | Copilot not listed: a helper, and they follow your pull request instead. | Lab 03, section 3 |
| 01:10 | SHOW | The demo ticket you assigned last evening: its session log, its draft pull request linked to the ticket, **Files changed**. | Watch |
| 01:14 | DO | Walk. | Lab 03, section 4: their log and draft pull request |
| 01:29 | CUT | "Break. Copilot keeps working while you have coffee." | |
| 01:30 | BREAK | | Helpers: rulesets, live versions, assignments |
| **01:45–02:30** | | **Build a Code Review agent: review rules and report format** | **Day 4 guide, section 4** |
| 01:45 | SHOW | The review-rules prompt writes `.github/instructions/review.instructions.md` with `applyTo: "site/**"`. "Rules written once: your review agent checks against them, and Copilot follows them when it builds, here and in the cloud." | Watch |
| 01:49 | DO | Walk. | Section 4, step 1 |
| 02:00 | SHOW | The agent prompt writes `.github/agents/code-review.agent.md`: the report table and the verdict; change one rule; `/exit`, `copilot`, `/agent` lists **code-review** beside **user-requirements**. | Watch |
| 02:04 | DO | Walk. | Section 4, steps 2-3 |
| 02:20 | SHOW | Branch `review-tools`, commit both files, **Publish Branch**, pull request, **Files changed**, merge, `main`, **Pull**. | Watch |
| 02:22 | DO | Walk. | Section 4, step 4 |
| 02:29 | CUT | "Two reviewers now look at Copilot's pull request: your agent and you." | Section 5 |
| **02:30–03:15** | | **Report lab: run the agent on a diff and verify its findings** | **Day 4 guide, section 5** |
| 02:30 | SHOW | Copilot's pull request (#5), **Files changed**; `/agent`, **code-review**, "Review pull request #5." It asks before each read-only `gh` and `git` command (option 2 stops repeats) and may offer to remember a fact (either answer is fine); about five minutes. `reviews/pr-5.md`; a **My check** column with one **Confirmed** and one **Not a problem**, each with a reason; "Did it miss anything you saw?" Rehearsed: a small clean change can have no findings and **Verdict: Not yet** only because the agent cannot try the page; then the checks by hand are the **My check**. "An agent's report can be wrong, like any answer. Your checks decide." | Watch |
| 02:38 | DO | Walk; no Copilot pull request yet: they review their own from section 2. | Section 5, steps 1-3 |
| 03:00 | SHOW | `/exit`, `copilot`, "Check out pull request #5 so I can try it"; `/start-website`; each criterion; `pytest checks`. | Watch |
| 03:03 | DO | Walk. | Section 5, step 4 |
| 03:14 | CUT | "Now ask Copilot to fix what you confirmed." | Section 6 |
| **03:15–03:45** | | **Iteration lab: request fixes with @copilot, retest and peer-review** | **Day 4 guide, section 6** |
| 03:15 | SHOW | On the pull request: "@copilot Fix finding 1 from my review: ... Change nothing else." No finding? Something small they noticed, such as "the Today label is small: make it a little bigger". Rehearsed: Copilot pushed the fix in about a minute. "Peer review meanwhile." | Watch |
| 03:18 | DO | Walk. | Section 6, step 1 |
| 03:22 | DO | Pairs. | Section 6, step 3: a neighbor checks one criterion |
| 03:32 | SHOW | "Pull the latest changes of this branch"; retest; then back to `main` (`/exit`, `main` in the status bar, `copilot`): **code-review** is listed only on `main`, because Copilot's branch is older than the agent. Review again; the **My check** notes stay. | Watch |
| 03:35 | DO | Walk. | Section 6, step 2 |
| 03:44 | CUT | "Decision time: merge or not." | Section 7 |
| **03:45–04:00** | | **Checkpoint: review the report and decide whether to merge** | **Day 4 guide, section 7** |
| 03:45 | SHOW | **Ready for review**, **Merge pull request** (leave the **Reviewers** box alone), **Actions > Publish my website**, live with the next version; the ticket in **Done**. Rehearsed: merge to live version about three minutes. "Merge if every criterion passes and no Must fix is left; otherwise close it with a reason. Both are good decisions." | Watch |
| 03:49 | DO | Walk. | Section 7, steps 1-3 |
| 03:59 | CUT | "Tomorrow GitHub checks every pull request for you, in a browser too. Push, then stop your Codespace." | |

**If late:** at 00:20 check the live version at the break. At 00:50, if Copilot is slow, move on
and come back to its pull request at 02:30. At 02:30 one confirmed and one rejected finding are
enough. At 03:15 peer review always runs while Copilot works.

**Watch for:** a push to `main` refused after the ruleset (expected: a branch and a pull request);
the footer change made on an idea page (it belongs on the first page, `site/index.html`, which the
address opens);
a workflow-file push refused (the web editor on a new branch); the `version:` line pasted with the
wrong indentation; the live footer still saying **Preview** (the `#` is still there, or no `site/`
change in that merge); a ticket still open after the merge (close it by hand). No Copilot review
appears on pull requests: Copilot code review is off by decision. For fast tables only: the
automation from Lab 03's extras in their own repository, then switched off.

## Day 5, Friday 30 October: CI/CD with GitHub Actions

Four hours including the break, elapsed.

| Time | Mode | Ali: shows and says | Attendees: do, and where |
| ---- | ---- | ------------------- | ------------------------ |
| **00:00–00:20** | | **CI/CD concepts: continuous integration, delivery and deployment** | **Day 5 guide, section 1** |
| 00:00 | - | "Joining today? A helper starts you at the top of the Day 5 guide." | Newcomers: **Joining today?** with a helper |
| 00:02 | SHOW | "Continuous integration: every change is built and tested automatically. Continuous delivery: every checked change is ready to publish. Continuous deployment: it publishes by itself; here, a person approves first. Since yesterday every change is a pull request and every release has a number. Today: checks before merge, approval before release." | Listen |
| 00:10 | SHOW | `publish-website.yml`: `on:` (when it runs), `permissions:` (what it may do), `version:` (the build number). | Watch |
| 00:14 | DO | Walk. | Section 1: the three lines found in their own file |
| 00:18 | SHOW | Only if on time: the Agentic Workflows demo (public preview). | Watch |
| 00:19 | CUT | "Now you add the missing half: checks." | Section 2 |
| **00:20–00:50** | | **Workflow lab: edit a starter YAML file, triggers and permissions** | **Day 5 guide, section 2** |
| 00:20 | SHOW | Branch `ci-checks`; Copilot copies the check starter and explains each job; under `on:` add `pull_request:` and a push to `main`; `contents: write` becomes `contents: read`. "Give a workflow only the permissions it needs: these checks only read." | Watch |
| 00:25 | DO | Walk. | Section 2, steps 1-3 |
| 00:37 | SHOW | Commit, **Publish Branch**, pull request: both checks run on it (the UI check installs a browser first, about two minutes; the 22 October rehearsal fixed a 14-minute install); merge on green. | Watch |
| 00:40 | DO | Walk. | Section 2, step 4 |
| 00:44 | SHOW | **Rulesets > Protect main > Require status checks to pass**, add **Check the website** and **UI check**, **Save changes**: **Confirm access** again (rehearsed), so phones ready. "They appear in the list only after they have run once." | Watch |
| 00:46 | DO | Walk. | Section 2, step 5 |
| 00:49 | CUT | "Now break it on purpose." | Section 3 |
| **00:50–01:30** | | **CI lab: build and test a pull request, inspect logs and fix failures** | **Day 5 guide, section 3** |
| 00:50 | SHOW | Branch `try-ci`, the guide's banner prompt (`min-width: 900px`, "do not let it shrink"): rehearsed, the short prompt got `max-width: 100%` and the check stayed green, so read the diff and remove any `max-width`. Pull request. While it runs, open the prepared red run: **UI check** red and **Merge** blocked ("Merging is blocked due to failing merge requirements"); **Details**, the table "Wider than a phone screen by 510 pixels"; **Summary > Artifacts > home-phone.png** (it downloads); "Why did the UI check fail?" (Copilot read the log and said the same); remove the banner; green; merge. "Red is information, not failure." | Watch |
| 01:00 | DO | Walk. | Section 3, steps 1-6 |
| 01:20 | SHOW | Section 3, step 7: the board, the next approved ticket, **Assign to Agent**, **Assign**. "Copilot builds it during the break. After the break it goes through your two slots." No approved ticket left: a small one from the **Requirement** template, moved to **Todo** first. | Watch |
| 01:22 | DO | Walk. | Section 3, step 7: a ticket assigned to Copilot |
| 01:26 | CHECK | "Hands up: who saw red? Who opened the phone screenshot? Who merged on green? Whose ticket is with Copilot?" | |
| 01:29 | CUT | "Break. Next: a test copy of your website for every pull request, and nothing reaches production until you approve it." | |
| 01:30 | BREAK | | Helpers: required checks, stuck runs, tickets assigned to Copilot |
| **01:45–02:30** | | **CD lab: approve and deploy a build to a training environment** | **Day 5 guide, section 4** |
| 01:45 | SHOW | "Everything this week is the training environment. Your website now gets two slots: the feature slot, a test copy of each pull request, and production, your real address." Branch `slots`: Copilot CLI copies both starters (`deploy-feature-slot.yml`, and the approval starter over `publish-website.yml`; the `version:` line stays); pull request, green, merge. **Settings > Environments > New environment** `production`, **Configure environment**, **Required reviewers**: yourself, **Save protection rules** (rehearsed: no **Confirm access** here). | Watch |
| 01:50 | DO | Walk. | Section 4, steps 1-2 |
| 01:57 | SHOW | Copilot's pull request: **Files changed** first. Merge box: "2 workflows awaiting approval", **Approve workflows to run**: "Nothing Copilot wrote runs until you say so." Checks green in about two minutes. **Actions > Deploy feature slot**: the newest run says **Action required**, "This workflow is awaiting approval from a maintainer", **Approve and run**: "This is the slide: approve and deploy a build to the training environment." About three and a half minutes later the pull request says "deployed to feature-slot": **View deployment** opens `<name>-feature` with the yellow strip (pull request, version 1.0.N-feature, build). Check the ticket's criteria there; smoke test the `-feature` address and note the **content** number. Your own pull requests skip both approvals (rehearsed). | Watch |
| 02:03 | DO | Walk. | Section 4, steps 3-5 |
| 02:14 | SHOW | **Files changed > Submit review > Approve**, a line on what you tested ("GitHub says it does not count as a required review, because you worked with Copilot: it is your record"), **Submit review**, **Ready for review**, **Merge pull request**, **Confirm merge**. **Actions > Publish my website** says **Waiting**: **Review deployments**, tick **production**, **Approve and deploy**; live about three minutes later, without the strip; smoke test: the same **content** number as the feature slot. "Production got exactly what you tested." An older **Deploy feature slot** run may say **Action required** again: "Leave it: it is Copilot's first draft and does nothing." | Watch |
| 02:17 | DO | Walk. | Section 4, steps 6-7 |
| 02:27 | CHECK | "Hand up when production shows Copilot's change, with the same content number as your feature slot." | |
| 02:29 | CUT | "Now ship a bad release on purpose, and bring the good one back." | Section 5 |
| **02:30–03:15** | | **Recovery lab: smoke-test the app and redeploy a known-good build** | **Day 5 guide, section 5** |
| 02:30 | SHOW | `python3 scripts/smoke_test.py <address> --expect-text "<the sentence under my headline>"`: all PASS. Note **content** and **version**: "The content number is the fingerprint of your good version." | Watch |
| 02:33 | DO | Walk. | Section 5, step 1 |
| 02:38 | SHOW | "Oops, wrong words": pull request, green checks, and a few minutes later **View deployment** shows the oops in the feature slot, with no approval asked because it is your own pull request. "This is where a tester catches it." Merge it anyway, approve, smoke test FAIL. "No check knows your words: test before and after every release." | Watch |
| 02:42 | DO | Walk. | Section 5, step 2 |
| 02:55 | SHOW | The merged pull request, **Revert**, merge, approve; smoke test PASS, the same content and a higher version. "Revert is your rollback." | Watch |
| 02:58 | DO | Walk. | Section 5, steps 3-4 |
| 03:12 | CUT | "Each table: one screen and one speaker, three minutes each." | Section 6 |
| **03:15–03:45** | | **Team demos: show requirements, review report and CI/CD evidence** | **Day 5 guide, section 6** |
| 03:15 | - | Host in table order with a timer on screen, about three minutes each. "An honest 'this part does not work yet' beats a polished claim nobody checked." | Each table: the board and one ticket's criteria; a confirmed and a rejected finding; red then green with a screenshot; the feature slot with its strip; an approval; the version; a rollback |
| 03:44 | CUT | "Last step: hand it over." | Section 7 |
| **03:45–04:00** | | **Handoff: share agent profiles, pipeline steps and release ownership** | **Day 5 guide, section 7** |
| 03:45 | SHOW | The HANDOFF.md prompt; read it; correct one sentence; branch, pull request, merge. The "To make it real" table: Power Apps or a code app, Power Automate, Power BI, Copilot Studio, Novo's own GitHub Enterprise, and Novo's validation process before any GxP use. | Watch |
| 03:48 | DO | Walk. | Section 7: HANDOFF.md merged; any automation switched off |
| 03:57 | CUT | Thank the room. "Push, then stop your Codespace at github.com/codespaces." | |

**If late:** skip the Agentic Workflows demo. At 00:50, if the runs are slow, show the prepared
red run and let attendees catch up during the break. At 01:57, if someone's Copilot pull request
is not ready, they make one small change on a branch and open their own pull request: its feature
slot deploys with no approval to click, and they watch Copilot's two approvals on your screen. At
02:30 attendees can skip the "Oops" release and just smoke-test before and after; show the bad
release and the **Revert** on your screen. Keep demos to three minutes, volunteer tables first.

**Watch for:** no **Approve workflows to run** yet (Copilot is still working: the pull request is
a draft whose title starts with [WIP], so wait for "Copilot finished work"); no **View deployment**
after green checks (the **Deploy feature slot** run waits under **Actions** for **Approve and run**);
a second **Deploy feature slot** run with **Action required** after the merge (Copilot's first
draft: leave it); a feature slot showing another pull request (the last one checked wins; the strip
names it); a banner that leaves the **UI check** green (it went inside the header, which cuts it
off, or Copilot added `max-width: 100%`: ask it to move the banner above the header and remove that
line); required-check names that do not match (**Check the website**, **UI check**: they
appear only after the starter has run once); a slow UI check (the 22 October rehearsal removed the
14-minute `--with-deps` install; if a run still waits, [githubstatus.com](https://www.githubstatus.com/)
may show **Actions** degraded, so check it before the session and keep the prepared runs open); a red UI check
on an untouched page (open `home-phone.png`, re-run once); keystrokes landing in the editor after
a Copilot CLI diff closes (click in the terminal before typing); Chat's "2 workspace customizations
need an update" notice (select the **X**, never **Migrate**); an "Oops" pull request that CI blocks
because a Day 3 test checks that sentence ("Your tests caught it": pick another sentence).

## After the Week

Remove attendee members (it stops seat billing), cancel pending invitations, archive the
repositories, delete published websites, switch off the Day 4 automation, and set `MIN_REPLICAS`
back to 0 if you raised it. The `FOUNDRY_*` client secret expires on 1 November: renew it or
delete it. Proposed teardown of the hosting itself: delete the resource group on Friday 6 November,
if David agrees (one command in `infra/README.md`).
