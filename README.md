# Build Your Own Website Just by Talking to AI

**No coding. Nothing to install. Just your web browser and your ideas.**

In this five-day workshop you tell GitHub Copilot, an AI helper, what you want in plain words,
and it builds it with you. You will even draw your own pictures with AI and give your website a
chat assistant that answers questions about it. By Friday you will have made something of your own, checked that it
really works, and shown it to the room. You have never used GitHub or written code? Perfect.
This workshop was made for you.

**When and where:** October 26-30, 2026, in Princeton, New Jersey. On Monday and Tuesday we
are in rooms MKC 1D412 and 1D413. Monday and Tuesday are full days, and Wednesday to Friday are
mornings. Your calendar invitation has the exact times.

## Your Week

| Day           | What you do                                                                   | What you take home                                  |
| ------------- | ----------------------------------------------------------------------------- | --------------------------------------------------- |
| **Monday**    | Meet GitHub and Copilot, build your first website just by asking, and peek at its code | A working website you made your own and checked |
| **Tuesday**   | Hear how business and IT work together, then build your own idea with help    | The first version of your own idea                  |
| **Wednesday** | Learn a few more Copilot tricks, then pick the idea you will build            | Your own picture skill, a chat on your page, and a plan |
| **Thursday**  | Build day, with helpers at every table                                        | Something that works, ready to show                 |
| **Friday**    | Show what you built or learned, in about three minutes                        | Your story, and ideas for what to try next          |

Every step follows the same rhythm: **watch, try, make it yours, check it, share it.**

## Monday Morning: Follow Along

This page is your only guide until 10:30. The presenter shows each step on their own
repository, and you do the same on yours, alongside them or straight after. Then the next
step. You do not need to read ahead, and you cannot break anything by looking.

### This Is GitHub

**09:00-09:30, after the welcome, the SEFR video, and the ASTER Overview teaser.** Concepts
only: no commands. Watch each step, then try it on your own repository.

1. **This is GitHub:** a website that keeps projects and every saved version of them.
2. **This is a repository:** a project's folder on GitHub. Open the workshop **template** link
   your facilitator sent you: the starting copy everyone uses. You see a list of files and,
   under them, this page.
3. **Make your own repository**, step by step with the presenter. On the template, select
   **Use this template > Create a new repository**, then:
   - **Owner:** choose **agentic-dev-labs**, not your own name.
   - **Repository name:** your GitHub username, for example `AliFarahnak`. Your website uses it.
   - **Visibility:** choose **Private**.
   - Select **Create repository**.

   **Check:** the top of the page shows **agentic-dev-labs /** your name and a **Private** label.
   If it shows anything else, raise your hand. Make only one. Working in a pair? Only the person
   at the keyboard makes one, and a helper adds the partner.
4. **Start your Codespace now, so it is ready later.** On your new repository's page, select the
   green **Code** button, then **Codespaces**, then **Create codespace on main**. It opens in a new
   tab and takes a few minutes. Leave it loading and come back to this tab.
5. **Look around your own repository** while it loads:
   - **See every snapshot:** select **Commits** (next to the clock icon). Your first one is there.
   - **Read any file:** select a file name. Pages ending in `.md`, like this one, show nicely.
   - **Look back in time:** open a file and select **History** to see how it changed.
   - **Search:** press **/** on your keyboard and type a word.
   - **To-do notes:** open **Issues**. Later this week you will see how Copilot can pick one up.

| Word       | Think of it as...                                                           |
| ---------- | --------------------------------------------------------------------------- |
| Repository | Your project folder on GitHub, with its whole history.                      |
| Codespace  | A computer in the cloud that opens in your browser.                         |
| Copilot    | A helper you talk to. It is clever but can be wrong, so you check its work. |
| Commit     | A snapshot of your work, with a short label saying what changed.            |
| Push       | Sending your snapshots up to GitHub, where they are safe.                   |

The order is always **save -> review -> commit -> push**. Saving does not send anything to
GitHub; pushing does.

**Done when:** you have your own private repository in agentic-dev-labs, its Codespace is
loading, and you found its files, its list of commits, and one file's history.

### Find Your Files and Copilot Chat

**09:30-10:00.** Do each step with the presenter, or straight after.

1. Switch to your Codespace's tab. If you closed it, select the green **Code** button on your
   repository's page, then **Codespaces**, and open the one listed there. Never create a second
   one. If it is still loading or shows an error, tell a helper. Nothing goes on your laptop.
2. In the **Explorer**, the file list on the left, right-click **README.md** and choose
   **Open Preview**. It is this page, now inside your Codespace. To see the plain text, select
   its other tab.
3. Open Chat with **View > Chat** and choose **Ask** from the list. **Ask** only answers; it
   never changes your files.
4. Ask: "Explain the difference between my repository, Codespace, and Copilot in three short
   sentences. Do not change files or run commands."
   **Check:** compare the answer with the five words above. Does it match?
5. Then ask: "Use an everyday example and make it shorter."
   **Check:** is it clearer now? You can always ask again, or say that something is wrong.
6. Ask: "Suggest three small features for a made-up team project planner. No logins. Do not
   create anything yet." Pick one you like.

**Done when:** your Codespace is open, you can find the Explorer and Chat, and you asked Copilot
a question and a follow-up. If sign-in or Copilot is missing, ask a helper. Never install
anything on your laptop.

### Your First Note

**10:00-10:30.** The presenter makes a note on their repository; you make yours.

1. In Chat, choose **Agent** when the presenter shows it: **Agent** can change your files. Type:
   "Create site/brief.md with my idea: a made-up project planner for a team week. Include who
   it is for, three things it should show, and one thing I can check. Do not build the website yet."
   You may describe a calendar, an ideas wall, or a weather page instead.
2. Open **Explorer > site > brief.md**. Read it and change one sentence into your own words.
   **Check:** it describes your idea, not something else.
3. Choose **File > Save**. Open **Source Control** and select the note to see what changed.
   **Check:** only your note is listed.
4. Select the **+** next to it, type `Describe my website idea`, select **Commit**, then
   **... > Push**.
   **Check:** open your repository on GitHub in a new browser tab and open **site/brief.md**.
   Your sentence is there.

You work in your own repository, on the `main` branch unless a helper says otherwise. If
anything asks you to create another repository, says a push was rejected, or mentions a
conflict, stop and ask a helper. Never force a push. If you work in a pair, take turns at the
keyboard.

**Done when:** your note is on GitHub.

### Next: Your First Website

At **10:45**, after the break, the presenter shows `/create-website`. Then open
[Lab 01](labs/01-first-website/README.md) and follow along. Your route for the rest of the day,
a picture guide to the screen, and the full word list are in [START-HERE](docs/START-HERE.md).
Tomorrow, the green **Code** button reopens the same Codespace.

## Four Golden Rules

1. **Use made-up data only.** Never real names, customers, patients, or work records.
2. **Check it yourself.** "Copilot says it works" is not proof. Click it and count it.
3. **Save often.** Save, commit, and push, then look for your work on GitHub.
4. **Stuck? Raise your hand.** Never install anything or approve something you do not understand.

## What Is in This Repository

| Folder          | What is inside                                                    |
| --------------- | ----------------------------------------------------------------- |
| `docs/`         | Your daily guides. After this page, Monday's is `docs/START-HERE.md`. |
| `labs/`         | Step-by-step exercises. The daily guides tell you which to open.  |
| `site/`         | Your website lives here once you build it.                        |
| Everything else | Behind-the-scenes tools that make the workshop run. Ignore them.  |

## For Facilitators

[Agenda](docs/AGENDA.md) · [Facilitator runbook](docs/FACILITATOR.md) ·
[Prerequisites](docs/PREREQS.md) · [Rehearsal](rehearsal/README.md) ·
[Topic map](docs/REFERENCES.md) · [Advanced post-workshop reference](post-workshop/advanced/README.md)

**Learn more:** [About GitHub Copilot](https://docs.github.com/en/copilot/get-started/about-github-copilot) ·
[What is a Codespace?](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces) ·
[How work flows on GitHub](https://docs.github.com/en/get-started/using-github/github-flow)
