# Cue sheet: Thursday and Friday

🎤 Ali shows · 🤝 Ali and attendees together · 👥 attendees alone · **Say:** what you say ·
**Paste** = what they type or paste, ten words at most · §n = the section of their guide.

**Tool** = where your screen is. One tool per row:

| Tool           | What it is                                                                         |
| -------------- | ---------------------------------------------------------------------------------- |
| 📽️ Slides      | `final-workshop-david/day4-announcements.html` in your browser                     |
| 💻 Codespace   | VS Code in the browser: their own Codespace (Chat, Source Control, Explorer). Never the terminal |
| 🌐 GitHub      | github.com in the browser: the repository's Issues, Actions, Settings, Pull requests, Agents |
| 🤖 Copilot app | The GitHub Copilot desktop app on the laptop                                       |
| 🗣️ Room        | No screen change: talk to the room                                                 |

**Rejoin rule** (both mornings): "Lost? Find our row in your guide's route table, open its link,
start there. Hand up, and a helper catches you up."
**Every morning, 30 min before:** demo Codespace open and warm · zoom 150% · notifications off ·
your own MCP servers off · today's guide in a tab · 5 min with the helpers.
Monday to Wednesday and the old lists: `archive/SCRIPT.wednesday-to-friday-2026-10-28.md`.

## Thursday

29 Oct · **2 h 45 min**, times from the start · their guide: **docs/DAY-4.md**, read in the
template on GitHub until §1 step 2 copies it into their repository · phone at hand for **Confirm
access**
**Screen link:** `github.com/agentic-dev-labs/copilot-hackathon-template/blob/main/docs/DAY-4.md`
**Slides:** `final-workshop-david/day4-announcements.html` (**F** fullscreen, **N** notes, arrows)

**Your part:** the slides, then §1 together: you publish **your old repository
`alfarahn-hackaton`, in its existing codespace, exactly like them** (it also has uncommitted work
and the commented version line). From §2 they lead with the guide: open each block with its slide
in one sentence, then walk the room. Show a step on screen only when three or more hands are stuck
on the same step. DAY-4.md starts each section with **Slide:** and its name, and its table **What
You Saw on the Slides** links each slide to a section.

**Where they are (audit, 28 Oct evening):** about 15 repositories have the website on GitHub;
about 27 have it only **uncommitted** in their Codespace; nobody has published or written tickets.
So §1 is one commit and push from the Codespace that **includes all changes**. Anyone with no
website builds one with a helper (`/create-website`, the guide's **Joining today**). Four
repositories in the organisation are not copies of the template: those attendees start with
**Joining today**.

**Before Thursday:**

1. ✅ Done 28 Oct: the template's `main` is pushed (`759814b`) and its CI is green.
2. Dry-run DAY-4.md on a fresh practice copy (**Use this template** → `dryrun-day4`, **Private**),
   **not** on `alfarahn-hackaton`: that one stays like theirs for the live §1. Keep the dry run's
   pull request with the **UI check** and Reviewer comments, and its live footer: your backup.
3. In the dry run, check that `/publish-website` copied `check-my-website.yml` into
   `.github/workflows/` and switched on the `version:` line, and fix the guide wherever a label
   differs: **Projects +**, **Which repositories should this Project use?**, **Overview**,
   **Needs input**, **Approve workflows to run**, both pictures in the comment, the trigger
   **Ready for review**, **Only this issue**, **Suggest tools**, the credit limits, **Run** with
   **Resource URL**.
4. Organisation: Copilot cloud agent on for all repositories · automations allowed · Copilot app
   policy on · AI-credit budget for about 45 cloud sessions and 45 Reviewer runs · Copilot code
   review off.
5. Copilot app updated, signed in as **alfarahn**.

**30 min before:** browser tabs in this order: 📽️ the slides · 🌐 the screen link · 🌐
`github.com/codespaces` · 🌐 `alfarahn-hackaton` (**Actions**, **Issues**, **Pull requests**,
**Settings**, **Agents**) · 🌐 the dry-run repository · 🤖 the Copilot app open with **Projects**
visible. Helpers know: **commit all changes**, never a second codespace, they lead from §2, and
the "What you see" tables in DAY-4.md.

### 00:00-00:15 What's new · slides

| Time  | Who    | Tool      | Where                                                    | Do                                                                                                                                                                                                                                    |
| ----- | ------ | --------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 00:00 | 🎤 Ali | 📽️ Slides | Slide 1 **Classic SDLC: Linear**                         | **Say:** "This is how software was built: a team, a plan, sprints, and a release date. Work waited for the plan."                                                                                                                     |
| 00:02 | 🎤 Ali | 📽️ Slides | Slide 2 **Evolving for the Agentic Era**                 | **Say:** "GitHub's message this week: any event can start software work now. 24 new triggers were just announced: a new ticket, a pull request, a failed check."                                                                      |
| 00:03 | 🎤 Ali | 📽️ Slides | Slide 3 **The stages stay. The jobs change.**            | **Say:** "We still plan, build, test, review, and release. Agents do more of each step; people decide."                                                                                                                               |
| 00:04 | 🎤 Ali | 📽️ Slides | Slides 4-5: the Copilot app, Fusion, Canvases, Dreaming  | One **You get** line per card. Canvases: play the keynote at 9:39 only if on time.                                                                                                                                                    |
| 00:07 | 🎤 Ali | 📽️ Slides | Slide 6 **Copilot Projects**                             | **Say:** "A project is mission control for one goal: it starts the work in parallel, remembers, and gives you one inbox. You use one in 45 minutes."                                                                                  |
| 00:09 | 🎤 Ali | 📽️ Slides | Slide 7 **Copilot Automations**                          | **Say:** "A trigger, a prompt, tools, and a credit limit. You build one after the break."                                                                                                                                             |
| 00:10 | 🎤 Ali | 📽️ Slides | Slides 8-10                                              | Quality and security, infrastructure, the future: one sentence each. **Say:** "Agents propose; people decide."                                                                                                                        |
| 00:13 | 🎤 Ali | 📽️ Slides | Slide 11 **Your website, version 1.1**                   | **Say:** "Today you do this chain on your own website: publish with a version, write a ticket, a Copilot project builds it, checks take screenshots, an automation reviews, you merge, and your page shows its version." Rejoin rule. |

### 00:15-00:50 Publish together, in your old repository · DAY-4.md §1

| Time  | Who          | Tool         | Where                                                                                      | Do                                                                                                                                                                                                                                           | Paste                                         |
| ----- | ------------ | ------------ | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| 00:15 | 🎤 Ali       | 🌐 GitHub    | The screen link: DAY-4.md §1                                                               | **Say:** "Slide 2 in practice: your push is the event. Most of your websites are still only in your Codespace. One push saves your work, switches on checks and a version number, and publishes it. I do each step in my old repository, you do it right after in yours." |                                               |
| 00:17 | 🤝 Both      | 💻 Codespace | Open it from `github.com/codespaces`: yours is `alfarahn-hackaton` · §1 step 1             | Wait about a minute → Chat → **Agent**. **Say:** "Never create a second one: a new codespace does not have your unsaved work. Two listed? The one you used last."                                                                            |                                               |
| 00:19 | 🤝 Both      | 💻 Codespace | Chat, **Agent** · §1 step 2                                                                | Send → **Allow** when Copilot runs the update → it lists what it brought: today's guide, the ticket template, the checks starter, a newer `/publish-website`. **Say:** "No commands today: you ask, Copilot runs, you allow." | `Fetch the latest updates from the main workshop repository.` |
| 00:22 | 🤝 Both      | 💻 Codespace | Chat, **Agent** · §1 step 3                                                                | Keep the suggested name or type one → it shows the address and says checks and version are on → **Source Control** lists `check-my-website.yml` and `publish-website.yml`. **Say:** "Two switches: checks on every change, a version on every release." | `/publish-website`                            |
| 00:25 | 🤝 Both      | 💻 Codespace | **Source Control** · §1 step 4                                                             | **File > Save All** → **Changes +** (all of them) → the message → **Commit** → **... > Push**. **Say:** "Include everything: this is the moment your work reaches GitHub."                                                                   | `Day 4: my website, checks and version`       |
| 00:27 | 🎤 Ali       | 🌐 GitHub    | `alfarahn-hackaton` › **Actions** · §1 step 5                                              | Two runs start: **Publish my website** and **Check my website**. **Say:** "One push, two events: publish and check. Nobody pressed a deploy button."                                                                                         |                                               |
| 00:28 | 👥 Attendees | 💻 Codespace | §1 steps 1-5                                                                               | Their push. Helpers: does **Source Control** list their `site/` files? All included? Push refused for a workflow file → **Watch for**.                                                                                                      |                                               |
| 00:38 | 🎤 Ali       | 🌐 GitHub    | **Actions** › **Publish my website** › its summary → the address → `/version.json` · §1 step 6 | **Your website is live**, **Version 1.0.0.N** → open the address → add `/version.json`. **Say:** "Your website knows its version and its environment, Production. The page does not show it yet: that is your ticket."                   |                                               |
| 00:41 | 🎤 Ali       | 🌐 GitHub    | **Actions** › **Check my website** › the **UI check** table → **Artifacts** › `home-phone.png` · §1 step 7 | **Say:** "A browser opened your page on a desktop and a phone. Red is fine today: it says what to look at. From now on these pictures come into every pull request."                                                         |                                               |
| 00:43 | 👥 Attendees | 🌐 GitHub    | §1 steps 6-7                                                                               | Their address, `version.json`, and first check. Helpers: **That name is taken**; a red publish run (read its message).                                                                                                                      |                                               |
| 00:49 | 🎤 Ali       | 🗣️ Room      |                                                                                            | "Hands up: your website is live?" Not yet: a helper stays with them. **Say:** "From here you lead, with the guide. I walk the room."                                                                                                         |                                               |

### 00:50-01:30 A Copilot project builds the ticket · DAY-4.md §2 · they lead

| Time     | Who                    | Tool                 | Where                                                                                | Do                                                                                                                                                                                                       | Paste                                             |
| -------- | ---------------------- | -------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| 00:50    | 🎤 Ali                 | 📽️ Slides            | Slide 6, then the screen link at §2                                                  | **Say:** "Slide 6, now yours: write the **Show my version** ticket, protect main, and give a Copilot project ten words. Then follow it in **Overview**, one inbox for review. Do not merge yet. Hands up when stuck." |                                                   |
| 00:52    | 👥 Attendees           | 🌐 GitHub            | **Issues > New issue > Show my version** · §2 step 1                                 | Read it → **Create** → ticket **#1**.                                                                                                                                                                    |                                                   |
| 00:54    | 👥 Attendees           | 🌐 GitHub            | **Settings > Rules > Rulesets > New ruleset > New branch ruleset** · §2 step 2       | `Protect main` → **Active** → **Include default branch** → **Require a pull request before merging**, approvals **0** → **Create** → **Confirm access** on the phone.                                   |                                                   |
| 00:58    | 👥 Attendees           | 🤖 Copilot app       | **Projects +** → their repository → **Add repositories** · §2 steps 3-5              | Send the goal → **Overview**: the session under **Working**; answer anything under **Needs input**.                                                                                                     | `Build ticket #1 in the cloud as a pull request.` |
| 01:10    | 👥 Attendees           | 🌐 GitHub            | **Pull requests** → the draft · §2 steps 6-8                                         | **Files changed** → no **[WIP]** in the title → **Approve workflows to run** → about 3 min → the **UI check** comment: desktop and phone, footer **Preview**. Do not merge.                             |                                                   |
| any time | 🎤 Ali (3+ hands only) | where they are stuck | Your own screen                                                                      | Show only that step: 🌐 the ruleset, 🤖 **Projects +**, or 🌐 **Approve workflows to run**. Copilot slow? 🌐 Show the dry-run pull request with its screenshots.                                        |                                                   |
| 01:29    | 🎤 Ali                 | 🗣️ Room              |                                                                                      | **Say:** "Break. Copilot keeps working while you have coffee. Do not merge yet."                                                                                                                         |                                                   |
| 01:30    | ☕ Break               | 🗣️ Room              | Tables                                                                               | Helpers: stuck sessions → 🌐 **Assign to Agent** on the ticket; **Approve workflows to run**; pushes still missing.                                                                                     |                                                   |

### 01:45-02:15 An automation reviews the pull request · DAY-4.md §3 · they lead

| Time  | Who          | Tool      | Where                                                                                       | Do                                                                                                                                                                                                         | Paste                                                        |
| ----- | ------------ | --------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 01:45 | 🎤 Ali       | 📽️ Slides | Slide 7, then the screen link at §3                                                         | **Say:** "Slide 7, now yours: a trigger, a prompt, tools, and a credit limit. Your Reviewer starts when you click **Ready for review**, and comments with your name: a personal automation acts as you." |                                                              |
| 01:47 | 👥 Attendees | 🌐 GitHub | Their repository › **Agents** › **Automations** › **Create automation** › **Create manually** · §3 steps 1-6 | `Reviewer` → **Personal** → trigger **Ready for review** → **Only this issue** → the prompt → **Suggest tools** (read and comment only) → **Per run** `100`, **Daily** `300` → **Create automation**. | `Review this pull request against its ticket. Only comment.` |
| 01:58 | 👥 Attendees | 🌐 GitHub | Their draft pull request → **Ready for review** → **Agents** (the session) · §3 steps 7-8   | A few minutes later the Reviewer's comment → check each point against the ticket and the screenshots. No **Ready for review**? **Run** → **Resource URL** → **Run now**.                                |                                                              |
| 02:08 | 🎤 Ali       | 🌐 GitHub | A volunteer's pull request on your screen                                                   | Read the Reviewer's comment aloud → check one point against the screenshot. **Say:** "That click was the event. Nobody assigned the review. It can be wrong: your own check decides."                     |                                                              |

### 02:15-02:45 Merge, release, checkpoint · DAY-4.md §4 · they lead

| Time       | Who          | Tool         | Where                                                                                    | Do                                                                                                                                                                                                                                                                                                       | Paste                                         |
| ---------- | ------------ | ------------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| 02:15      | 🎤 Ali       | 🗣️ Room      | The screen link at §4                                                                    | **Say:** "You decide, agents do: merge it, and about three minutes later your footer says Production and the version. Never **Delete codespace**."                                                                                                                                                      |                                               |
| 02:17      | 👥 Attendees | 🌐 GitHub    | The pull request → **Merge pull request > Confirm merge > Delete branch** · §4 steps 1-3 | **Actions** › **Publish my website** green → their website's footer: **Production · Version 1.0.0.N** → ticket #1 closed.                                                                                                                                                                               |                                               |
| 02:27      | 👥 Attendees | 🌐 GitHub    | **Agents > Automations > Reviewer > Disable** · §4 step 4                                | Every run costs credits.                                                                                                                                                                                                                                                                                 |                                               |
| 02:29      | 👥 Attendees | 💻 Codespace | **Source Control > ... > Pull** · §4 steps 5-6                                           | Their Codespace gets Copilot's change → show a neighbour: the project's **Overview**, the pull request, the merge, the live footer.                                                                                                                                                                     |                                               |
| (if ahead) | 👥 Attendees | 🌐 GitHub    | A second ticket's pull request that **has conflicts** · optional extra 1                  | Comment, wait for Copilot's new commit, then merge.                                                                                                                                                                                                                                                      | `@copilot Fix the merge conflicts with main.` |
| 02:40      | 🎤 Ali       | 📽️ Slides    | Slide 11                                                                                 | **Say:** "A ticket, a project, checks with screenshots, an automation, your merge, a live version: every step started by an event, every decision yours. Tomorrow the checks become required, every pull request gets a test copy of your website, and you approve each release. Push, then stop your Codespace." |                                               |

**Running late:** 00:28 slow pushes → do the 00:38-00:43 demo while they finish · the ruleset can
wait until after the break: it only matters before the merge · **Projects** slow or missing for
many → everyone uses 🌐 **Assign to Agent** on #1 (the same draft pull request) · 01:47
automations late → build yours on screen, they merge after their own check · 02:15 the merge and
**Disable** always happen.

**Watch for**

- 💻 **Source Control** lists only today's updates → the website is already on GitHub, or this is a new codespace: check `site/index.html` on GitHub and the other codespaces at `github.com/codespaces`
- 💻 Not all changes included → **Changes +**, commit again, push
- 💻 The update stops: workshop files not committed → undo that one file, send the 00:19 prompt again
- 💻 Copilot cannot find how to update → send `Follow docs/QUICK-COMMANDS.md to fetch the workshop updates.`; no such page → not a copy of the template: **Joining today** with a helper, who moves their `site/` folder across
- 💻 `/publish-website` did not switch on the checks or the version → run it again: it adds only what is missing
- 💻 Push refused for a workflow file → helper on 🌐 GitHub: **Add file > Create new file** `.github/workflows/check-my-website.yml` with the starter's text, the pencil on `publish-website.yml` for the version line; then push the rest again
- 🌐 **That name is taken** → 💻 `/publish-website` with another name, commit, push
- 🌐 Publish red "needs attention" → read its message (missing `index.html`, files too big); never edit the workflow
- 🌐 **UI check** red on `main` → fine today
- 🌐 No **Show my version** under **New issue** → the §1 push is not on GitHub
- 🤖 No **Projects** in the app → update the app; else 🌐 **Assign to Agent**
- 🤖 A session waits → **Needs input**: answer it
- 🤖 Session finished, no pull request → **Create PR** in the session
- 🌐 Pull request without checks → **Approve workflows to run**; title still **[WIP]** → wait
- 🌐 No screenshot comment → **Actions > Check my website > Screenshots** log; the pictures are also under **Artifacts**
- 🌐 Broken pictures in the comment → signed out, or another account
- 🌐 The Reviewer never starts → was it a draft? Trigger **Ready for review**; else **Run** with **Resource URL**; per-run limit at least 30
- 🌐 "The Reviewer's comment has my name" → right: a personal automation acts as you
- 🌐 Footer still **Preview** after the merge → reload; else ask in 💻 Chat: "Is my version number switched on?"
- 🌐 Ticket still open → **Close issue**
- 🌐 **Delete codespace** offered → never
- Real names or work data anywhere → everything stays made up

**Tonight (Thursday to Friday):** see how far the room got and plan Friday's catch-up (Friday
assumes the checks, the ruleset, a version and a Copilot pull request) · disable your own demo
automations · githubstatus.com for **Actions**.

## Friday

30 Oct · 4 h, times from the start · their guide: **docs/DAY-5.md** · phone at hand · your address
`https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io` (`<name>` = `websiteName` in
`config.json`; the feature slot is `<name>-feature`) · every prompt goes into 💻 Chat (**Agent**):
Copilot runs the commands, they select **Allow**; nobody types a command or an address.

**Before Friday:** a prepared red run in a spare copy (checks on, a pull request with the 900 px
banner) · the template's `main` green · githubstatus.com for **Actions**.

### 00:00-00:20 CI/CD in plain words · DAY-5.md §1

| Time  | Who          | Tool         | Where                                         | Do                                                                                                                                               |
| ----- | ------------ | ------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 00:00 | 🎤 Ali       | 🗣️ Room      |                                               | "Joining today? A helper starts you with Day 4, section 1." Rejoin rule.                                                                         |
| 00:02 | 🎤 Ali       | 🌐 GitHub    | The template's DAY-5.md §1                    | **Say:** "CI: every change built and tested automatically. CD: every checked change ready to publish. Deployment: here a person approves first." |
| 00:10 | 🎤 Ali       | 💻 Codespace | **Explorer** › `.github/workflows/publish-website.yml` | `on:` (when it runs) · `permissions:` (what it may do) · `version:` (1.0.0 and the build number).                                        |
| 00:14 | 👥 Attendees | 💻 Codespace | The same file · DAY-5.md §1                   | The three lines in their own file.                                                                                                               |
| 00:18 | 🎤 Ali       | 🌐 GitHub    |                                               | Only if on time: Agentic Workflows demo (public preview).                                                                                        |
| 00:19 | 🎤 Ali       | 🗣️ Room      |                                               | **Say:** "Since Thursday your checks run on every pull request. Today they become required."                                                     |

### 00:20-00:50 Workflow lab · DAY-5.md §2

| Time  | Who          | Tool         | Where                                                       | Do                                                                                                                                                                                                         | Paste                                                                            |
| ----- | ------------ | ------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| 00:20 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §2 step 1                                  | Paste → then in the file: `on:` (pull_request, push to main, workflow_dispatch) · `permissions: contents: read` · only **Screenshots** may write. **Say:** "Only the job that runs none of the pull request's code may write." | `Explain my Check my website workflow. Change nothing.` |
| 00:25 | 👥 Attendees | 💻 Codespace | §2 step 1                                                   | The same.                                                                                                                                                                                                  |                                                                                  |
| 00:37 | 🎤 Ali       | 🌐 GitHub    | **Actions > Check my website > Run workflow** · §2 step 2   | Both checks green in about 3 min. **Say:** "That button is the workflow_dispatch trigger."                                                                                                                 |                                                                                  |
| 00:40 | 👥 Attendees | 🌐 GitHub    | §2 step 2                                                   | The same.                                                                                                                                                                                                  |                                                                                  |
| 00:44 | 🎤 Ali       | 🌐 GitHub    | **Settings > Rules > Rulesets > Protect main** · §2 step 3  | **Require status checks to pass** → **Add checks**: **Check the website** and **UI check** → **Save changes** → **Confirm access**. **Say:** "They appear only after they have run once."                  |                                                                                  |
| 00:46 | 👥 Attendees | 🌐 GitHub    | §2 step 3                                                   | Their checks required.                                                                                                                                                                                     |                                                                                  |
| 00:49 | 🎤 Ali       | 🗣️ Room      |                                                             | **Say:** "Now break it on purpose."                                                                                                                                                                        |                                                                                  |

### 00:50-01:30 CI lab · DAY-5.md §3

| Time  | Who          | Tool         | Where                                                         | Do                                                                                                                                                       | Paste                                                 |
| ----- | ------------ | ------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 00:50 | 🎤 Ali       | 💻 Codespace | New branch `try-ci` → Chat, **Agent** · §3 steps 1-2          | Paste → remove any `max-width` → commit → **Publish Branch** → create the pull request.                                                                 | `Add a Sale banner above my header, min-width 900px.` |
| 00:52 | 🎤 Ali       | 🌐 GitHub    | The prepared red run's pull request · §3 steps 3-4            | **UI check** red, **Merge** blocked → **Details**: "Wider than a phone screen" → the **UI check** comment: the phone screenshot. **Say:** "Red is information, not failure." |                                                       |
| 00:55 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §3 step 5                                   | Paste → compare its answer with the log.                                                                                                                 | `Why did my pull request's UI check fail?`            |
| 00:57 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §3 step 6                                   | Paste → commit → push.                                                                                                                                   | `Remove the banner you just added.`                   |
| 00:59 | 🎤 Ali       | 🌐 GitHub    | The pull request · §3 step 6                                  | Both green → **Merge** → **Delete branch** (never **Delete codespace**).                                                                                 |                                                       |
| 01:00 | 👥 Attendees | 💻 Codespace | §3 steps 1-6, then switch to `main` → **Pull**                | The same, with 🌐 GitHub for the pull request.                                                                                                           |                                                       |
| 01:20 | 🎤 Ali       | 🌐 GitHub    | **Issues** · §3 step 7                                        | Their next ticket (none? **New issue > Requirement**, such as "Show a short welcome line under my headline") → **Assignees > Assign to Agent**, or 🤖 the Copilot project. **Say:** "Copilot builds it during the break." |                                                       |
| 01:22 | 👥 Attendees | 🌐 GitHub    | §3 step 7                                                     | The same.                                                                                                                                                |                                                       |
| 01:26 | 🎤 Ali       | 🗣️ Room      |                                                               | "Hands up: saw red? opened the phone screenshot? merged on green? a ticket with Copilot?"                                                               |                                                       |
| 01:29 | 🎤 Ali       | 🗣️ Room      |                                                               | **Say:** "Break. Next: a test copy for every pull request, and nothing reaches production until you approve."                                           |                                                       |
| 01:30 | ☕ Break     | 🗣️ Room      | Tables                                                        | Helpers: required checks, stuck runs, tickets with Copilot.                                                                                             |                                                       |

### 01:45-02:30 CD lab · DAY-5.md §4

| Time  | Who          | Tool         | Where                                                        | Do                                                                                                                                                                                                                                   | Paste                                                                                                     |
| ----- | ------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| 01:45 | 🎤 Ali       | 💻 Codespace | New branch `slots` → Chat, **Agent** · §4 step 1             | **Say:** "Two slots: the feature slot is a test copy of each pull request; production is your own address." Paste → check `deploy-feature-slot.yml` in `.github/workflows/`, the **Wait for approval** job and the `version:` line in `publish-website.yml` → commit → **Publish Branch**. | `Switch on the two Day 5 workflow starters.`                                                              |
| 01:47 | 🎤 Ali       | 🌐 GitHub    | The `slots` pull request                                     | Create it → merge on green.                                                                                                                                                                                                          |                                                                                                           |
| 01:48 | 🎤 Ali       | 🌐 GitHub    | **Settings > Environments** · §4 step 2                      | **New environment** `production` → **Configure environment** → **Required reviewers**: you → **Save protection rules**.                                                                                                             |                                                                                                           |
| 01:50 | 👥 Attendees | 💻 Codespace | §4 steps 1-2                                                 | The same, with 🌐 GitHub for the pull request and the environment.                                                                                                                                                                  |                                                                                                           |
| 01:57 | 🎤 Ali       | 🌐 GitHub    | Copilot's pull request · §4 steps 3-5                        | **Files changed** first → **Approve workflows to run** ("nothing Copilot wrote runs until you say so") → **Actions > Deploy feature slot** → **Action required** → **Approve and run** (about 3 min) → **View deployment**: the yellow strip → check the criteria. **Say:** "Your own pull requests skip both approvals." |                                                                                                           |
| 02:01 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §4 step 5                                  | Smoke test the feature slot → note the **content** number.                                                                                                                                                                           | `Smoke-test my feature slot.` |
| 02:03 | 👥 Attendees | 🌐 GitHub    | §4 steps 3-5                                                 | The same, with 💻 the smoke test.                                                                                                                                                                                                   |                                                                                                           |
| 02:14 | 🎤 Ali       | 🌐 GitHub    | The pull request → **Actions** · §4 steps 6-7                | **Files changed > Submit review > Approve** (say what you tested) → **Ready for review** → **Merge** → **Publish my website**: **Waiting** → **Review deployments** → tick **production** → **Approve and deploy** → the footer says **Production** with a new version. |                                                                                                           |
| 02:16 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §4 step 7                                  | Smoke test your own address: the same **content**. **Say:** "Production got exactly what you tested."                                                                                                                              | `Smoke-test my website.` |
| 02:17 | 👥 Attendees | 🌐 GitHub    | §4 steps 6-7                                                 | The same, with 💻 the smoke test.                                                                                                                                                                                                   |                                                                                                           |
| 02:27 | 🎤 Ali       | 🗣️ Room      |                                                              | "Hand up when production shows Copilot's change with the same content number."                                                                                                                                                      |                                                                                                           |
| 02:29 | 🎤 Ali       | 🗣️ Room      |                                                              | **Say:** "Now ship a bad release on purpose, and bring the good one back."                                                                                                                                                          |                                                                                                           |

### 02:30-03:15 Recovery lab · DAY-5.md §5

| Time  | Who          | Tool         | Where                                                 | Do                                                                                                                                         | Paste                                                                                                                                              |
| ----- | ------------ | ------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 02:30 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §5 step 1                           | With your own sentence from under your headline → all PASS → note the **content** and the **version**. **Say:** "The fingerprint of your good version." | `Smoke-test my website. It must show: <your sentence>` |
| 02:33 | 👥 Attendees | 💻 Codespace | §5 step 1                                             | The same.                                                                                                                                  |                                                                                                                                                    |
| 02:38 | 🎤 Ali       | 💻 Codespace | New branch → Chat, **Agent** · §5 step 2              | Paste → commit → **Publish Branch**.                                                                                                       | `Change the sentence under my headline to: Oops, wrong words.`                                                                                     |
| 02:39 | 🎤 Ali       | 🌐 GitHub    | The pull request · §5 step 2                          | Green, **View deployment** shows the oops ("where a tester catches it") → merge anyway → **Review deployments** → approve.                 |                                                                                                                                                    |
| 02:41 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §5 step 2                           | The same smoke-test prompt: FAIL. **Say:** "Test before and after every release."                                                         |                                                                                                                                                    |
| 02:42 | 👥 Attendees | 💻 Codespace | §5 step 2                                             | The same, with 🌐 GitHub for the pull request and the approval.                                                                            |                                                                                                                                                    |
| 02:55 | 🎤 Ali       | 🌐 GitHub    | The merged pull request · §5 step 3                   | **Revert** → **Create pull request** → green → merge → approve the release.                                                               |                                                                                                                                                    |
| 02:57 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §5 step 4                           | The same smoke-test prompt: PASS, the same content, a higher version. **Say:** "Revert is your rollback."                                |                                                                                                                                                    |
| 02:58 | 👥 Attendees | 🌐 GitHub    | §5 steps 3-4                                          | The same, with 💻 the smoke test.                                                                                                          |                                                                                                                                                    |
| 03:12 | 🎤 Ali       | 🗣️ Room      |                                                       | **Say:** "Each table: one screen, one speaker, three minutes."                                                                             |                                                                                                                                                    |

### 03:15-04:00 Demos and handoff · DAY-5.md §6-7

| Time  | Who          | Tool         | Where                          | Do                                                                                                                                                                                                                  | Paste                                                       |
| ----- | ------------ | ------------ | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 03:15 | 👥 Attendees | 🗣️ Room      | Their own screens · §6         | By table, volunteers first, timer on screen: a ticket and its criteria, the Reviewer's comment (one point agreed, one checked differently), red then green, the feature slot, an approval, the version, a rollback. |                                                             |
| 03:44 | 🎤 Ali       | 🗣️ Room      |                                | **Say:** "Last step: hand it over."                                                                                                                                                                                 |                                                             |
| 03:45 | 🎤 Ali       | 💻 Codespace | Chat, **Agent** · §7           | Paste → read it, correct one sentence → branch, commit, **Publish Branch**.                                                                                                                                        | `Write HANDOFF.md as section 7 of docs/DAY-5.md describes.` |
| 03:47 | 🎤 Ali       | 🌐 GitHub    | The HANDOFF pull request · §7  | Merge → the guide's "To make it real" table: Power Apps, Power Automate, Power BI, Copilot Studio, Novo's GitHub Enterprise, Novo's validation for GxP → **Agents > Automations**: anything still on → **Disable**. |                                                             |
| 03:48 | 👥 Attendees | 💻 Codespace | §7                             | HANDOFF.md merged with 🌐 GitHub · any automation switched off.                                                                                                                                                    |                                                             |
| 03:57 | 🎤 Ali       | 🗣️ Room      |                                | Thank the room. **Say:** "Push, then stop your Codespace at github.com/codespaces."                                                                                                                                 |                                                             |

**Running late:** skip Agentic Workflows · 00:50 slow runs → show the prepared red run, they
catch up in the break · 01:57 no Copilot pull request → they open their own small one (no
approvals) and watch yours · 02:30 they may skip the oops release: you show it and the **Revert** ·
demos 3 min each, volunteer tables first.

**Watch for**

- 🌐 No **Approve workflows to run** yet → Copilot still working (title starts **[WIP]**): wait for "Copilot finished work"
- 🌐 No **View deployment** after green checks → **Actions > Deploy feature slot** waits for **Approve and run**
- 🌐 The feature slot shows another pull request → the last one checked wins; the strip names it
- 🌐 The banner leaves **UI check** green → it went inside the header, or Copilot added `max-width: 100%`
- 💻 `deploy-feature-slot.yml` missing, or two publish workflows → Copilot copied a starter wrongly: `publish-website-with-approval.yml` goes **over** `publish-website.yml`
- 🌐 **Check the website** or **UI check** missing from **Add checks** → they appear after one run
- 🌐 Slow **UI check** → githubstatus.com, carry on, never re-run in a loop
- 🌐 Red **UI check** on an untouched page → open `home-phone.png`, re-run once
- 🌐 The oops pull request blocked by an earlier test → "your tests caught it", pick another sentence
- 🌐 An older **Deploy feature slot** run asks again after the merge → leave it

**After Friday** (agree each step with David): remove attendee members and invitations · archive
the repositories, delete the published websites (also `showcase` with `workshop-showcase`) and
`keep-warm` · `MIN_REPLICAS` back to 0 in `website-publisher.yml` · attendees' automations
disabled · `FOUNDRY_*` client secret expires 1 Nov: renew or delete.
