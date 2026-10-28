# Day 3: VS Code and a Requirements Agent

Today you meet the newest way to work with Copilot: the **GitHub Copilot app** on your laptop,
with **plugins** from two **marketplaces**. You make something fun with a skill someone else
wrote, then turn a trip you plan into a **skill of your own**. The same idea gives you a **User
Requirements agent**: it writes **tickets** for the website you built on Monday, an **AI
triage** helper on GitHub spots the copies, and you check every **acceptance criterion** so
anyone can tell when a ticket is done. Then Copilot builds one approved ticket in your
Codespace, and you test it. The presenter shows every step first; then you do the same.
Everything stays made up: no real people, trips, or work data.

**This guide is new today.** Read it in the workshop template on GitHub (the presenter shows the
link); your own copy receives it in [section 4](#4-build-the-approved-ticket).

**Two ways to start.** Most people use their repository from Monday, with the website they built
then. **No repository, or want a clean start?** During the art time or the break, a helper sits
with you: on the workshop template select **Use this template > Create a new repository**, owner
**agentic-dev-labs**, a name such as `<your username>-planner`, **Private**, then **Code >
Codespaces > Create codespace on main**. In Chat choose **Agent**, run `/create-website`, pick the
**Project Planner**, then save, commit with the message `Add my first website`, and push. Both
ways meet again at [section 3](#3-tickets-ai-triage-and-criteria).

## Today's Route

Times count from the start of the session.

| Elapsed     | What happens                                                                                                 | You are finished when                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| 00:00-00:20 | MUKQ: global and Microsoft perspectives on AI development                                                    | You listened; no laptop needed.                                                                           |
| 00:20-00:50 | [Workspace setup, repository walkthrough, and agent roles and tools](#1-copilot-app-plugins-and-a-fun-skill) | The Copilot app runs, a plugin from a second marketplace is installed, and its skill made your animation. |
| 00:50-01:30 | [Build a User Requirements agent: instructions and output format](#2-your-own-skill-then-your-own-agent)     | Your travel skill works in a new session, and `/agent` lists your **user-requirements** agent.            |
| 01:30-01:45 | Break                                                                                                        |                                                                                                           |
| 01:45-02:30 | [Draft user stories and acceptance criteria, then validate](#3-tickets-ai-triage-and-criteria)               | Triage caught your copy, every open ticket has criteria you can check, and two are in **Todo**.           |
| 02:30-03:15 | [Implement the approved ticket, debug, and verify](#4-build-the-approved-ticket)                             | Every acceptance criterion passes your own check.                                                         |
| 03:15-03:45 | [Add tests and write down how to build and run](#5-add-tests-and-how-to-run)                                 | `pytest checks` is green, and `site/README.md` lists your requirements and how to run it.                 |
| 03:45-04:00 | [Checkpoint](#6-checkpoint)                                                                                  | Your ticket closed itself and moved to **Done**.                                                          |

**Lost?** Find the row the room is on (the presenter names it at the start of every block),
select its link, and start there. Raise your hand: a helper catches you up on what you skipped.

## New Words for Today

| Word                | Plain meaning                                                                        |
| ------------------- | ------------------------------------------------------------------------------------ |
| Copilot app         | Copilot as an app on your laptop: sessions, your tickets, and plugins in one window. |
| Plugin              | A package of skills and agents someone else wrote, installed with one click.         |
| Marketplace         | A shop window of plugins. Awesome Copilot is built in; you can add others.           |
| Ticket (issue)      | One thing you want, written on GitHub under **Issues**, with a number such as #1.    |
| Project board       | A page of cards, one per ticket, in columns: Todo, In Progress, and Done.            |
| Automation          | A helper that starts by itself when something happens, such as a new ticket.         |
| Triage              | Sorting new tickets: what kind, already asked for, ready to build?                   |
| Terminal            | The panel below the editor where you type commands.                                  |
| Tool (MCP)          | A plug that lets Copilot do something, such as read your tickets on GitHub.          |
| Instructions        | Standing rules Copilot reads before every request, in a short file.                  |
| Skill               | A recipe in a folder: how to do one job, step by step, in a fixed format.            |
| Custom agent        | A helper with one job that you describe in a short file, like a role card.           |
| User story          | "As a ..., I want ..., so that ..." : who needs what, and why.                       |
| Acceptance criteria | Checks that say when a ticket is done: "Given ..., when ..., then ...".              |
| Test                | A short file that checks your page for you. Green means pass, red means fail.        |

## 1. Copilot App, Plugins, and a Fun Skill

**00:20-00:50.** Follow the presenter click by click.

1. **Open the GitHub Copilot app** on your laptop and select **Sign in to GitHub**. Use your
   **workshop account**, the one that owns your repository: Copilot only sees what that account
   can open. Never paste a password or token into Copilot. **No app?** Pair with a neighbor and
   tell a helper.
2. **Look around.** The sidebar shows **Sessions** (your conversations with an agent), **My
   work** (your tickets on GitHub), **Automations** (tasks that start by themselves), and
   **Customize** (plugins, skills, and tools). Under the message box you choose how Copilot
   works: **Interactive** (it works with you), **Plan** (it plans, you approve), or **Autopilot**
   (it works alone). Set tool permissions to **Ask every time** today, so you approve each step.
3. **Browse a marketplace.** Open **Customize > Plugins**. **Awesome Copilot** is already there:
   a community shop window of plugins. Look around for a minute; install nothing yet.
4. **Add a second marketplace.** Still in **Plugins**, add the marketplace `anthropics/skills`
   from Anthropic, the makers of Claude; it shows as **anthropic-agent-skills**. Open its
   **example-skills** plugin and read what it contains and its licence first: a plugin runs on
   your laptop, so you read before you install. Then select **Install**.
5. **Restart.** Quit the app completely, also from its icon near the clock, open it again, and
   start a **new session**: plugins load when the app and a session start. Type `/skills` and
   find **algorithmic-art**.
6. **Make art.** Ask: "Do you have art skills?" Then paste this, or describe your own theme:

   > Use the algorithmic-art skill. Title it "Induced Fit". Made-up drug-like molecules, little
   > ball-and-stick shapes with blue, teal and white atoms, drift through calm water around a
   > made-up protein with a curved pocket in the centre. When a molecule fits the pocket, it locks
   > in and glows softly; the others drift on. Calm deep-blue and teal colours on a light
   > background. Sliders for the number of molecules, the speed (temperature), the pocket size
   > and the trail length, a seed box with Prev, Next and Random, and a counter that shows how
   > many molecules are bound. Everything is fictional: no real compounds, logos, or medical
   > claims. Open it when it is done.

   Allow it to read the skill and write its files, then open the page it made. Move the
   sliders and select **Regenerate**. **Check:** your animation moves, and you can name the
   skill that made it.

A **skill** is a recipe, a **plugin** is a package of skills and agents, and a
**marketplace** is the shop window. **Agent roles:** Chat's **Ask** only answers, **Agent** can
change files, a **custom agent** is a helper you give one job and clear rules, and tomorrow
the **cloud agent** works by itself on GitHub.

**Blank page?** Your network may block the drawing library it loads: show a helper and follow
the presenter's screen. **No Install button, or no algorithmic-art after the restart?** Your
company may block that marketplace: use **Awesome Copilot** instead, for example its **APNG
Studio** plugin, which builds animations inside the app.

## 2. Your Own Skill, Then Your Own Agent

**00:50-01:30.** The presenter plans a made-up trip by chatting, then turns the chat into a
skill. You do the same, then you make your User Requirements agent.

1. **Watch.** The presenter asks for flights on Skyscanner, a hotel on trivago, and three
   sights on the city's own tourism website, then a one-page proposal website, and says out
   loud what the skill should do next time.
2. **Your trip.** Start a new session, paste this, and change the bracketed parts:

   > Plan a made-up weekend trip to [a city] from [your city], [Friday to Monday dates], for one
   > adult, for pleasure. Use the browser: flights on Skyscanner, a hotel near the centre on
   > trivago, and three sights with ticket prices on the city's official tourism website. Never
   > sign in, book, or pay, and say which prices you could not confirm. Then make a simple
   > one-page website with my proposal and open it.

   Prices change and some websites block robots: if one fails, let it use the tourism website.

3. **Your skill.** In the same session, paste:

   > Now you understand what I want. Use the skill-creator skill to make a personal skill called
   > travel-planner from what we just did: it asks me only the city, the dates, and business or
   > pleasure, then does the same searches and builds the same one-page website. Never sign in,
   > book, or pay. Keep it short and do not run any tests.

   **No skill-creator?** Ask instead: "Write that skill yourself in my personal skills folder,
   ~/.copilot/skills/travel-planner/SKILL.md."

4. **Prove it.** Start a **new session**, type `/skills`, and find **travel-planner**. Ask: "Plan a
   weekend in Lisbon." It asks you its questions: that is your skill at work. You may stop it
   there.
5. **Meet the building blocks.** You now know three of them; the fourth is next:

   | Building block | What it does                                      | Where it lives                                     |
   | -------------- | ------------------------------------------------- | -------------------------------------------------- |
   | Instructions   | Standing rules Copilot reads before every request | `.github/copilot-instructions.md`, your repository |
   | Skill          | A recipe: how a job is done, in a fixed format    | Your travel-planner; `/create-website` on Monday   |
   | Custom agent   | A helper with one job, its own rules and tools    | Your user-requirements agent, next                 |
   | Tools (MCP)    | Plugs that let Copilot act, like GitHub's tools   | **Customize** in the app                           |

   A **skill** says _how_ a job is done. An **agent** says _who_ does it: its role and its rules.
   You make both by describing them in plain words.

6. **Your User Requirements agent.** Start a new session, paste this, and change the bracketed
   parts:

   > Create a personal custom agent at ~/.copilot/agents/user-requirements.agent.md with
   > `name: user-requirements` and a one-line description. It is a User Requirements agent for my
   > website about [your Monday website, such as a project planner] in the GitHub repository
   > [agentic-dev-labs/your-repository]. When I describe wishes, it drafts one ticket per wish
   > with the sections What I want (my words), Which page (site/index.html unless I say
   > otherwise), User story as "As a ..., I want ..., so that ...", Acceptance criteria as 2 or 3
   > "Given ..., when ..., then ..." that a person can check by clicking or counting, each with a
   > checkbox, and Only change. It shows me every draft first. Only when I say yes does it create
   > the tickets with the GitHub tools. When I ask it to improve a ticket, it shows the new text
   > first and, only when I say yes, changes only the User story and Acceptance criteria
   > sections and keeps every other line exactly as it is; then it reads the ticket again and
   > tells me whether my own words under What I want are unchanged. It asks me one question at
   > a time, never writes website code, and uses made-up people and data only.

7. Open the file it made (it shows where) and read it: the **name** and **description** between
   the two `---` lines tell Copilot when to use it; below them are its rules. Change one rule
   into your own words and save. Start a **new session** and type `/agent`:
   **user-requirements** is in the list.

**Check:** `/skills` lists travel-planner, and `/agent` lists user-requirements.

## 3. Tickets, AI Triage, and Criteria

**01:45-02:30.** On GitHub you set up a board and an AI triage helper; in the app your agent
writes the tickets; back on GitHub you check them.

1. **Make your board.** At the top of your repository's page, select the organization's name,
   the part before the slash. Open **Projects > New project**. In the **Create project** window,
   under **Start from scratch**, choose **Board**, and name it after yourself, such as
   `<your username> website`: everyone's board lives in the same organization. Leave **Import
   items from repository** ticked, and under **Repository** choose your own repository: it shows
   the workshop template at first, and typing your username in its search box finds yours. Select
   **Create project**.
2. **Approving stays your decision.** At the top right of your board, select **Workflows**, then
   **Item added to project**, and switch it **Off**; otherwise GitHub puts every new ticket
   straight into **Todo**. Leave **Auto-add to project** and **Item closed** on: the import
   already set them up, so new tickets reach your board, and a closed ticket moves to **Done**.
   Open the board from your repository's **Projects** tab: it is already listed there.
   **Todo** means approved and ready to build, **In Progress** means being built, and **Done**
   means finished. Only people who can open your repository can read your tickets.

   **No New project button?** Ask a helper to create your board or give you access. You can
   write tickets while you wait. **Ticket or board missing?** Use **+ Add item** on the board and
   select the ticket, or **Link a project** on your repository's **Projects** tab and select the board.

3. **Turn on AI triage.** On your repository's page select **Agents**, then **Automations**.
   Under **Suggestions** select **Triage incoming issues**, read what it does, and select
   **Create automation**. From now on Copilot looks at every new ticket by itself: what kind it
   is, whether it repeats an earlier one, and whether it is ready to build. It only suggests;
   you decide.
4. **Your own idea.** Choose three things you want _next_ on the website you built on Monday:
   the wishes you wrote under **Next** in `site/README.md` on Tuesday are a good start. A wish
   about something your page already does leaves nothing to build.
5. **Let your agent write the tickets.** In the app, start a new session, type `/agent`, choose
   **user-requirements**, and paste this with your three wishes:

   > Draft tickets for these wishes for my website: [wish 1]; [wish 2]; [wish 3]. Add one more
   > ticket that asks for the same thing as my first wish in other words, so I can test the
   > triage. Show me the drafts first.

   Read the drafts and ask for changes, then say: "Yes, create them." Above the answer the app
   shows the GitHub tool it used: a plug, through **MCP**, that lets Copilot act on GitHub.
   Each ticket gets a number, such as **#1**, and joins your board under **No Status**: written,
   not approved yet.

   **It says it can only read GitHub?** Ask a helper to connect GitHub's issue tools with you,
   or write each draft yourself: **Issues > New issue > Requirement**, paste the draft, and
   select **Create**.

6. **Watch the triage.** On GitHub open **Agents**: one session runs for each new ticket, for
   about two minutes. Then open your copy: at the top, **Agent suggestions** say **Close →
   duplicate of #...**. Select **Accept all**: the copy closes and its card moves to **Done**.
   Your other tickets get a type, and maybe a comment asking for more detail. **No suggestion
   after five minutes?** Comment `Duplicate of #1` (your first ticket's number) and select
   **Close issue**.
7. **Validate** each acceptance criterion of your open tickets: can you check it yourself by
   clicking or counting? If not, ask your agent: "Rewrite criterion 2 of issue #1 so that I can
   check it by counting. Change nothing else." Say yes when it shows the new text, then open the
   ticket on GitHub: **your own words under What I want are unchanged**. Here _validate_ means
   checking that every criterion can be checked. It is not GxP validation: your practice
   website is a prototype with made-up data, not a validated system.

   **If something goes wrong:** your own words changed? Tell a helper: the ticket's **edited**
   menu keeps every earlier version. If Copilot says it may not update the ticket, copy its
   draft, select **...** and **Edit** on the ticket, paste the draft under **User story** and
   **Acceptance criteria**, and save.

8. **Approve.** Choose one small ticket to build today. On your board, drag its card into
   **Todo**: approved, ready to build. Ask a neighbor: "Could you check this ticket's criteria?"
   Approve a second ticket the same way: tomorrow Copilot's cloud agent builds it for you.

**Check:** triage caught your copy, every open ticket has a story and criteria you could check,
and two tickets are in **Todo**.

## 4. Build the Approved Ticket

**02:30-03:15.** Now you switch to VS Code: your Codespace, where your website lives.

1. **Open your Codespace** with the green **Code** button on your repository's page. Never create
   a second one. Open Chat and choose **Agent**. Bring today's guide into your own copy: open
   **docs > QUICK-COMMANDS.md**, paste its **Fetch Updates** prompt into Chat, then commit with
   the message `Fetch workshop updates` and push.
2. On your board, drag the ticket you build today into **In Progress**.
3. **Plan first.** Ask: "Read issue #1 with `gh issue view 1` and make a short plan to build it
   in site/ideas/team-lunch/index.html: what changes, and how I can check each acceptance
   criterion. Change nothing yet and wait for my yes." Use your own ticket's number and your own
   page, such as `site/index.html`. Read the plan and ask for a change if something is missing.
4. **Build.** Say: "Yes, build the plan. Change only what it needs and keep everything else. Do
   not run tests or scripts: I check it myself." Read what it wants to change before you allow
   it.
5. In Chat, run `/start-website team-lunch`
   (your own folder's name) if the preview is closed, and watch the change appear.
6. Check every acceptance criterion yourself, by clicking and counting.
7. **Debug:** if one fails, say exactly what happened: "Criterion 2 of issue #1 fails. I
   expected [this]. I saw [that]. Fix only that." Then check that criterion again, and the
   others too.

**Check:** every criterion of your approved ticket passes your own check in the preview.

## 5. Add Tests and How to Run

**03:15-03:45.** Work with your table: compare tickets and help each other.

1. In Chat, with **Agent** chosen, ask: "Write tests in checks/test_issue1.py for the acceptance criteria of issue #1
   that can be checked from the files, using `from website import Page` as shown in
   checks/README.md. Give every assert a short message saying what I expected. Tell me which
   criteria stay manual checks. Include one check for an existing heading or button label in
   my page's HTML, and tell me the exact text to change for the red-test exercise. Do not
   change the website to make a test pass. Then run `pytest checks`." Use your own ticket's
   number and name the test file to match, such as `checks/test_issue7.py` for #7.
2. If Copilot asks to run `pytest checks`, read the request and choose **Allow**.
   A request waits until you answer, so look at Chat if nothing seems to happen.
   **Check:** the terminal says `passed` in green.
3. **Break it on purpose:** in your page's HTML, change the exact text Copilot identified,
   leaving the test unchanged. Save and run
   `pytest checks` again. It turns red and says what it expected. Undo your change with
   **Ctrl+Z** (**Cmd+Z** on a Mac), save, and run it again: green.
4. Ask: "Add a section called How to build and run to the end of site/README.md, in plain
   words: how to open the page (/start-website), how to run the tests (pytest checks), how to run
   the build check (python -m app.site --check), and the manual checks for issue #1. Then add a
   section called Requirements: one line per ticket with its number, title, user story, and
   status expected after today's closing commit (Done for issue #1, Todo for the approved
   ticket for tomorrow, or No Status for an unapproved ticket). Do not guess the board's
   statuses; ask me to confirm them." Use your own ticket's number and page. Confirm each
   status against your board and the ticket you are about to finish.
   Read both sections and correct anything that is wrong. `site/README.md` is now your
   website's validated README: your checked requirements, each one traced to its ticket, and how
   to run it. Here too, checked does not mean GxP validated.

## 6. Checkpoint

**03:45-04:00.**

1. Check that the branch at the bottom left is **main**. Save all files. Open **Source Control** and review the files: your page, your
   test, and `site/README.md` (your skill and agent live in the app on your laptop). Commit with a message that ends with `Closes` and your ticket's number,
   for example `Mark urgent tasks. Closes #1`, then **... > Push**.
2. Open your board: the ticket closed itself and moved to **Done**. `Closes #1` in a commit that
   reaches `main` closes the ticket, and the board moves closed tickets to **Done** by itself.
   If it stays open, check the ticket number and that your commit reached `main`; ask a helper
   before trying again. Check that the status in `site/README.md` now matches the board.
3. Show a neighbor or a helper five things: your art, your travel skill and requirements agent,
   your board, the finished ticket with its criteria, and the working feature with its green
   tests.

**Done when:** your art and your **travel-planner** skill work in the Copilot app, `/agent` lists
your User Requirements agent, triage caught your copy, your tickets have user stories with
checkable acceptance criteria, `site/README.md` lists them, one ticket works in your preview with
green `pytest checks` and is **Done** on your board, and another approved ticket waits in **Todo**
for tomorrow. If sign-in is blocked, follow the presenter's screen and tell a helper.

**What you just learned:** plugins and skills from a marketplace add new abilities in a minute,
and you can turn your own way of working into a skill. A ticket holds one thing you want, the
board shows where every ticket stands, and an automation can triage new tickets for you while
you keep the decision. Tools (MCP) let Copilot act on GitHub, a skill is a recipe, and an agent
is a role: all short files you write in plain words. Acceptance criteria make "done" checkable,
and tests keep checking it after every change. Tomorrow Copilot's cloud agent builds your next
ticket on GitHub: see the [Day 4 guide](DAY-4.md).

## Optional extras

1. In the app, type `/rubber-duck` and ask for a second opinion on your trip plan: a different
   model reviews it.
2. Install **APNG Studio** from Awesome Copilot and build a short animation frame by frame.
3. On your board, add a field called **Priority** with the options Must, Should, and Could, and
   set it on every ticket.
4. In the app, type `/chronicle standup` for a summary of today's sessions.
5. Add a chat to your page with `/add-chat`, then check one of its answers against your page.

## Official References

- [Getting started with the GitHub Copilot app](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app),
  [agent sessions and modes](https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions),
  and [plugins and marketplaces](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-cli-plugins).
- [Automations with Copilot cloud agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations)
  and [marking a ticket as a duplicate](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/marking-issues-or-pull-requests-as-a-duplicate).
- [About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues),
  [about projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects),
  [creating a project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project),
  and [the board's built-in automations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations).
- [Adding new tickets automatically](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically)
  and [linking your board to your repository](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/adding-your-project-to-a-repository).
- [Closing a ticket with `Closes #1`](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).
- [Custom agents in Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
  and [custom agents in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-agents).
- [Agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) and
  [adding skills for Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).
- [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp) and the
  [customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).
- [Testing in VS Code](https://code.visualstudio.com/docs/debugtest/testing).
