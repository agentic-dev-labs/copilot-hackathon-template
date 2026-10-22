# Build Your Own Website Just by Talking to AI

**No coding. Nothing to install. Just your web browser and your ideas.**

In this five-day workshop you tell GitHub Copilot, an AI helper, what you want in plain words,
and it builds it with you. Later in the week you write your own AI helpers, called agents, the
same way: one that turns your idea into checkable user stories, and one that reviews Copilot's
work. By Friday GitHub checks every change for you, and you have made something of your own,
checked that it really works, and shown it to the room. You have never used GitHub or written
code? Perfect. This workshop was made for you.

**When and where:** October 26-30, 2026, in Princeton, New Jersey. On Monday and Tuesday we
are in rooms MKC 1D412 and 1D413. Monday and Tuesday are full days, and Wednesday to Friday are
four-hour sessions. Your calendar invitation has the exact times.

## Your Week

| Day           | What you do                                                                   | What you take home                                  |
| ------------- | ----------------------------------------------------------------------------- | --------------------------------------------------- |
| **Monday**    | Meet GitHub and Copilot, build your first website just by asking, and peek at its code | A working website you made your own and checked |
| **Tuesday**   | Hear how business and IT work together, then build your own idea with help    | The first version of your own idea                  |
| **Wednesday** | Turn your idea into tickets on a project board, write your own requirements agent that adds checkable criteria, and build one ticket | Your board, your agent, and a tested feature |
| **Thursday**  | Practice pull requests, hand your next ticket to Copilot's cloud agent, and review it with your own review agent | A reviewed change you decided to merge or not |
| **Friday**    | Let GitHub check every change, approve each release, and roll back a bad one; then demos | A checked, approved, recoverable website and a handoff note |

Every step follows the same rhythm: **watch, try, make it yours, check it, share it.**

## Monday Morning: Follow Along

This page is your only guide until 10:30. The presenter shows each step on their own
repository, and you do the same on yours, alongside them or straight after. Then the next
step. You do not need to read ahead, and you cannot break anything by looking.

**Lost?** Find the heading below with the time now and start at its first step. Raise your
hand: a helper catches you up on what you skipped.

### This Is GitHub

**09:00-09:30, after the welcome, the SEFR video, and the ASTER Overview teaser.** Concepts
only: no commands. Just watch; you make your own copy at 09:30.

1. **This is GitHub:** a website that keeps projects and every saved version of them.
2. **This is a repository:** a project's folder on GitHub. Open the workshop **template** link
   your facilitator sent you: the starting copy everyone uses. You see a list of files and,
   under them, this page.
3. **Look around** while the presenter shows each part:
   - **See every snapshot:** **Commits**, next to the clock icon.
   - **Read any file:** select a file name. Pages ending in `.md`, like this one, show nicely.
   - **Look back in time:** open a file and select **History** to see how it changed.
   - **Search:** press **/** on your keyboard and type a word.
   - **To-do notes:** **Issues**. Later this week you will see how Copilot can pick one up.

| Word       | Think of it as...                                                           |
| ---------- | --------------------------------------------------------------------------- |
| Repository | Your project folder on GitHub, with its whole history.                      |
| Codespace  | A computer in the cloud that opens in your browser.                         |
| Copilot    | A helper you talk to. It is clever but can be wrong, so you check its work. |
| Commit     | A snapshot of your work, with a short label saying what changed.            |
| Push       | Sending your snapshots up to GitHub, where they are safe.                   |

The order is always **save -> review -> commit -> push**. Saving does not send anything to
GitHub; pushing does.

**Done when:** you know the five words above. Nothing to do on your laptop yet.

### Find Your Files and Copilot Chat

**09:30-10:00.** Do each step with the presenter, or straight after.

1. **Make your own repository.** On the template, select
   **Use this template > Create a new repository**, then:
   - **Owner:** choose **agentic-dev-labs**, not your own name.
   - **Repository name:** your GitHub username, for example `AliFarahnak`. Your website uses it.
   - **Visibility:** choose **Private**. It may start on **Internal**.
   - Leave everything else as it is, including the optional **Jumpstart** box, and select
     **Create repository**.

   **Check:** the top of the page shows **agentic-dev-labs /** your name and a **Private** label.
   If it shows anything else, or **agentic-dev-labs** is not in the list, raise your hand.
   Make only one. Working in a pair? Only the person at the keyboard makes one, and a helper
   adds the partner.
2. **This is your repository.** The presenter shows it: the same files as the template, this
   page under them, and your first snapshot under **Commits**. Everything you make this week
   lives here.
3. **Open your Codespace.** Select the green **Code** button, then **Codespaces**, then
   **Create codespace on main**. It opens in a new tab in about a minute. If it asks
   **Do you trust the authors of the files in this folder?**, choose **Trust Folder & Continue**:
   it is your own copy of the workshop, and your website preview needs it. Never create a
   second Codespace. If it shows an error, tell a helper. Nothing goes on your laptop.
4. In the **Explorer**, the file list on the left, right-click **README.md** and choose
   **Open Preview**. It is this page, now inside your Codespace. To see the plain text, select
   its other tab.
5. Open Chat with **View > Chat** and choose **Ask** from the list. **Ask** only answers; it
   never changes your files. In the browser, **View** is in the menu with three lines at the top
   left. Only **Agent** in the list, or **Sign In** at the bottom right? Select **Sign In** once.
6. **Guess the next word.** The presenter shows how Copilot writes: it picks a likely next word,
   one word at a time. Now you try. Type `/next-word`, pick it from the list, then type
   **What a nice day, let's go to the** and press Enter.
   **Check:** which word did you get? Raise your hand for it when the presenter asks. The
   percentages are Copilot's own rough estimate, not a measurement.
7. Stay in this chat all day; you do not need a new one. Ask: "Explain the difference between my
   repository, Codespace, and Copilot in three short sentences. Do not change files or run
   commands."
   **Check:** compare the answer with the five words above. Does it match?
8. Then ask: "Use an everyday example and make it shorter."
   **Check:** is it clearer now? A better question gives Copilot more to go on. You can always
   ask again, or say that something is wrong.

**Done when:** you have your own private repository in agentic-dev-labs, its Codespace is open,
you saw Copilot guess the next word, and you asked Copilot a question and a follow-up. If sign-in
or Copilot is missing, ask a helper. Never install anything on your laptop.

### Your First Website

**10:00-10:30.** The presenter shows `/create-website` on their repository; you do the same on
yours.

1. In Chat, choose **Agent** instead of **Ask**: **Agent** can change your files. Type
   **`/create-website`**, pick it from the list, and press Enter.
2. Copilot asks one question: which website would you like to make? Choose **Project Planner**,
   **Calendar**, **Ideas Wall**, **Weather**, **Princeton Map**, **Photo Studio**, or
   **My own idea**. The presenter builds the Project Planner; pick it if you are unsure.
3. Copilot builds it and opens it in the **Website preview** beside Chat, named after your
   repository, for example **AliFarahnak Project Planner**. While it builds, Copilot may ask to
   run `python3 scripts/website_preview.py start`, the helper that opens your preview: select
   **Allow**. If it asks to run anything else you do not understand, raise your hand. Press **+**
   and add a made-up entry.
   **Check:** a new **index.html** appears in **Explorer > site**. Seeing the file is the
   proof, not Copilot saying "done". Then select **Keep** under the chat box: it accepts the
   change. Do this whenever you like a change, because **Undo** takes back every change you
   have not kept.
4. Open **Explorer > site > brief.md**. This is your idea note, the README of your website:
   Copilot wrote what your page is for and how you can check it. You add to it all week.
5. **Save it on GitHub.** Choose **File > Save All**; if it is grey, everything is already
   saved. Then open **Source Control**. This first time it lists many files: your page plus the
   pictures, fonts and styles it needs. That is expected. Hover over **Changes** and select its
   **+** to include them all, type `Add my first website`, select **Commit**, then **... > Push**.
   **Check:** open your repository on GitHub in a new browser tab, open **site**, then
   **brief.md**. It is there.

You work in your own repository, on the `main` branch unless a helper says otherwise. If
anything asks you to create another repository, says a push was rejected, or mentions a
conflict, stop and ask a helper. Never force a push. If you work in a pair, take turns at the
keyboard. If `/create-website` is not in the list or the preview does not open, show a helper.

**Done when:** your page opens beside Chat and it is on GitHub.

### Next: Make It Yours

At **10:45**, after the break, the presenter shows more websites you can build. Then open
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
