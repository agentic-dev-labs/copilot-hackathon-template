# Day 3: VS Code and a Requirements Agent

Today you write your own **User Requirements agent**, a helper that turns your idea into user
stories that anyone can check. Then you build one approved story, test it, and show it. You work
in the same Codespace, on the website and idea you already have, mostly by typing plain
sentences to **Copilot CLI** in the terminal. Nothing is installed on your laptop, and
everything stays made up.

**No website yet?** In Chat choose **Agent**, run `/create-website`, and pick the Project
Planner. A helper gets you started while the room continues.

## Today's Route

Times count from the start of the session.

| Elapsed     | What happens                                                          | You are finished when                                             |
| ----------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 00:00-00:20 | MUKQ: global and Microsoft perspectives on AI development             | You listened; no laptop needed.                                   |
| 00:20-00:50 | [Workspace setup, repository walkthrough, and agent roles and tools](#1-workspace-and-agent-roles) | Copilot CLI is signed in and answered a question about your page. |
| 00:50-01:30 | [Build a User Requirements agent](#2-build-your-user-requirements-agent) | Your agent file exists and Copilot CLI lists it.                  |
| 01:30-01:45 | Break                                                                 |                                                                   |
| 01:45-02:30 | [Draft user stories and acceptance criteria, then validate](#3-draft-and-validate-user-stories) | Your requirements file has one story marked **Approved**.         |
| 02:30-03:15 | [Implement the approved story, debug, and verify](#4-build-the-approved-story) | Every acceptance criterion passes your own check.                 |
| 03:15-03:45 | [Add tests and write down how to build and run](#5-add-tests-and-how-to-run) | `pytest checks` is green, and your brief says how to run it.      |
| 03:45-04:00 | [Checkpoint](#6-checkpoint)                                           | You showed the agent, the story, and the working feature.        |

## New Words for Today

| Word                | Plain meaning                                                                          |
| ------------------- | -------------------------------------------------------------------------------------- |
| Terminal            | The panel below the editor where you type commands.                                    |
| Copilot CLI         | Copilot inside the terminal. The same assistant as Chat, through a different door.      |
| Custom agent        | A helper with one job that you describe in a short file, like a role card.             |
| User story          | "As a ..., I want ..., so that ..." : who needs what, and why.                         |
| Acceptance criteria | Checks that say when a story is done: "Given ..., when ..., then ...".                 |
| Test                | A short file that checks your page for you. Green means pass, red means fail.          |

## 1. Workspace and Agent Roles

**00:20-00:50.** The presenter shows each step, then you try it.

1. Open your Codespace with the green **Code** button on your repository's page. Never create a
   second one.
2. Open the menu (the three lines at the top left), then **Terminal > New Terminal**. Type
   `copilot` and press Enter. If it asks whether you trust this folder, choose yes.
3. Sign in once: type `/login`, press Enter, and choose the first option. Copilot shows a short
   code. Open [github.com/login/device](https://github.com/login/device) in a new browser tab,
   type the code, and select **Authorize**. Never paste a password or token into Copilot.
4. Ask: "Read site/brief.md and site/index.html. In three short bullet points, explain what my
   website does. Do not change any files." **Check:** compare its answer with your page.
5. Type `/agent` and press Enter to see the list of agents. It is empty today: you add your own
   next. Press **Esc** to close it.

When Copilot wants to read a file, change a file, or run a command, it asks first. Read what it
wants to do, and say yes only to what you understand. **Agent roles:** Chat's **Ask** only
answers, **Agent** can change files, and a custom agent is a helper you give one job and clear
rules.

## 2. Build Your User Requirements Agent

**00:50-01:30.** An agent is a short text file in `.github/agents/`. You describe the job in
plain words; Copilot writes the file; you read it and make it yours.

1. In Copilot CLI, paste this, and change the parts in brackets to fit your idea:

   > Create a custom agent file at .github/agents/user-requirements.agent.md with
   > `name: user-requirements` and a one-line description. It is a User Requirements agent for
   > my small website about [my idea]. When I name a brief.md, it writes 3 to 5 user stories,
   > numbered US-1, US-2, and so on, each as "As a ..., I want ..., so that ...", marked Must,
   > Should, or Could. Under each story it writes 2 or 3 acceptance criteria as
   > "Given ..., when ..., then ..." that a person can check by clicking or counting. It lists
   > open questions instead of guessing. It saves everything to requirements.md next to that
   > brief. It never writes code or changes other files, and uses made-up people and data only.

2. Open **Explorer > .github > agents > user-requirements.agent.md**. The lines between the two
   `---` lines at the top are its **name** and **description**: they tell Copilot when to use
   it. Below them are its rules. Change one rule into your own words and save.
3. Copilot CLI loads agents when it starts, so type `/exit`, then `copilot` again. Type `/agent`:
   **user-requirements** is now in the list.

**Check:** your agent file exists, and `/agent` lists it. The same file also appears in Chat's
agent picker in VS Code: one file, two doors.

## 3. Draft and Validate User Stories

**01:45-02:30.**

1. Type `/agent`, choose **user-requirements**, and ask: "Write the requirements for my website
   from site/brief.md." For an idea in its own folder, name its brief instead, for example
   `site/ideas/team-lunch/brief.md`.
2. Open the new **requirements.md** next to the brief. Read every story.
3. **Validate** each acceptance criterion: can you check it yourself by clicking or counting? If
   not, ask the agent to rewrite only that one: "Rewrite the criteria of US-2 so that I can check
   them by counting. Change nothing else."
4. Choose one small Must story to build today. Under it, type `Approved: yes` and today's date.
   Ask a neighbor: "Is this story clear enough that you could check it?"

**Check:** one story is marked **Approved**, and you could check every one of its criteria.

## 4. Build the Approved Story

**02:30-03:15.** Now leave the requirements agent: type `/exit`, then `copilot`, so you are back
to ordinary Copilot.

1. Ask: "Implement US-1 from site/requirements.md in site/index.html. Change only what US-1
   needs and keep everything else. Then list how I can check each acceptance criterion." Use your
   own story number and your own files.
2. Read what it wants to change before you allow it. In Chat, run `/start-website` if the
   preview is closed, and watch the change appear.
3. Check every acceptance criterion yourself, by clicking and counting.
4. **Debug:** if one fails, say exactly what happened: "Criterion 2 of US-1 fails. I expected
   [this]. I saw [that]. Fix only that." Then check that criterion again, and the others too.

**Check:** every criterion of your approved story passes your own check in the preview.

## 5. Add Tests and How to Run

**03:15-03:45.** Work with your table: compare stories and help each other.

1. Ask Copilot CLI: "Write tests in checks/test_us1.py for the acceptance criteria of US-1 that
   can be checked from the files, using `from website import Page` as shown in checks/README.md.
   Add the others to a Manual checks list in my requirements file. Then run `pytest checks`."
2. **Check:** the terminal says `passed` in green.
3. **Break it on purpose:** in your page change one word that a test looks for, save, and run
   `pytest checks` again. It turns red and says what it expected. Undo your change with
   **Ctrl+Z** (**Cmd+Z** on a Mac), save, and run it again: green.
4. Ask: "Add a section called How to build and run to my brief, in plain words: how to open the
   page (/start-website), how to run the tests (pytest checks), and how to run the build check
   (python -m app.site --check)." Read it and correct anything that is wrong.

## 6. Checkpoint

**03:45-04:00.**

1. Save. Open **Source Control** and review the files: your agent, requirements, page, and test.
   Commit with a short message, then **... > Push**. Open GitHub and find your agent file.
2. Show a neighbor or a helper three things: your agent file, your approved story, and the
   working feature with its green tests.

**Done when:** your own requirements agent is on GitHub, your requirements file has an approved
story with checkable acceptance criteria, that story works in your preview, and `pytest checks`
passes. If sign-in is blocked, follow the presenter's screen and tell a helper; it is not a
reason to install anything.

**What you just learned:** an agent is a short file you write in plain words. User stories make
"what we want" checkable, and tests keep checking it for you after every change. Tomorrow you
hand an approved story to Copilot's cloud agent: see the [Day 4 guide](DAY-4-BUILD.md).

## Optional extras

1. Choose your agent in VS Code Chat's agent picker and ask the same question there. Compare
   the two answers.
2. Ask Copilot CLI to read your recent commits with its built-in GitHub tools, then compare with
   **Commits** on GitHub. [Lab 04](../labs/04-mcp/README.md) shows the same in Chat.
3. Write an instructions file and your own `/make-image` picture skill, or add a chat to your
   page, with [Lab 06](../labs/06-teach-copilot/README.md).
4. In Copilot CLI, type `/help` and find one command you would like to try later.

## Official References

- [Copilot CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart) and
  [using Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview).
- [Custom agents in Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
  and [custom agents in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-agents).
- [Testing in VS Code](https://code.visualstudio.com/docs/debugtest/testing).
- [Topic map (for presenters)](REFERENCES.md).
