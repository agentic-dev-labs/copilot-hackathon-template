# Your First Website With Copilot

Welcome! Today you will build a small website just by describing it, check that it works, and
save it on GitHub. You do not need to know how to code. Everything happens in your web browser;
nothing is installed on your laptop. Use made-up examples only, never real work information.

The presenter shows every step first, then gives you time to try it. You do not need to read
ahead. Keep the [printable quick reference](QUICK-REFERENCE.md) beside you.

## First Block: Understand the Workspace

**09:00-09:30: concepts only. No terminal commands.** Just watch and listen.

| Word         | What it means                                                     |
| ------------ | ----------------------------------------------------------------- |
| GitHub       | The website where your project and its saved versions are kept.   |
| Repository   | Your project: its files and their history. Often called a "repo". |
| Codespace    | A computer in the cloud that you use through your browser.        |
| VS Code      | The program you see inside the Codespace.                         |
| Copilot Chat | The AI assistant you talk to. It is helpful, but it can be wrong. |
| Ask          | In Chat: Copilot only answers. It never changes your files.       |
| Agent        | In Chat: Copilot can change your files. You check each change.    |
| Prompt       | What you type to ask Copilot for something.                       |
| File         | One piece of your project, such as a note or a web page.          |
| Save         | Keep your latest change in the file.                              |
| Commit       | Take a labeled snapshot of your saved changes.                    |
| Push         | Send your snapshots up to GitHub.                                 |
| Preview      | Look at your page while you build it. Only you can see it.        |

The order is always **save -> review -> commit -> push**. Saving does not send anything to
GitHub; pushing does. An answer in Chat is not a file until you can see the file.

**Say it back:** Where are your files? Which step sends your work to GitHub? How will you know
your page really works?

## Find Your Way Around

These are **official documentation screenshots**, so names and colors may look a little
different in your Codespace. The presenter points to each part on the real screen.

To read this guide comfortably, right-click **docs > START-HERE.md** in the Explorer and choose
**Open Preview**. The presenter shows this first. To go back to the plain text, select its tab.

### A. Files, Editor, and Chat

![The VS Code window: the Explorer with files on the left, the editor in the middle, Chat on the right, and a panel at the bottom.](https://code.visualstudio.com/assets/docs/editing/userinterface/hero.png)

**Files** are on the left, in the **Explorer**. **The editor** in the middle shows the file you
opened. **Chat** is on the right; if you cannot see it, choose **View > Chat**. Ignore the panel
at the bottom for now.

Source: [Microsoft's VS Code layout guide](https://code.visualstudio.com/docs/editing/getting-started/userinterface).

### B. Review and Save a Version

![Source Control in a Codespace, with the plus button that selects a checked file.](https://docs.github.com/assets/images/help/codespaces/codespaces-commit-stage.png)

**Source Control** is the icon that looks like branching lines. It lists every file you changed.
Select the **+** next to a file you checked to include it in your next snapshot.

![A short commit message and the Commit button.](https://docs.github.com/assets/images/help/codespaces/vscode-commit-button.png)

Type a short **message** about what you changed, select **Commit**, then choose **... > Push**.
Your repository already exists, so never create a new one.

Source: [GitHub's Codespaces source-control guide](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
GitHub Docs screenshots are shown unmodified under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
with the [source license and disclaimer](https://github.com/github/docs/blob/main/LICENSE).
If an image does not load, read its caption and ask the presenter to point to the button.

### C. Your Website Preview

When you build your website, it opens in a **Website preview** panel beside Chat and updates by
itself as it changes. `/start-website` opens it again and `/stop-website` closes it; your files
stay saved. This is different from **Open Preview**, which shows a document like this one.

## Today's Route

| When        | Open                                          | You are finished when                                   |
| ----------- | --------------------------------------------- | ------------------------------------------------------- |
| 09:30-10:00 | [Lab 00](../labs/00-setup/README.md)          | You can find your files and ask Chat a question.        |
| 10:00-10:30 | [Your first note](#your-first-note)           | Your note is saved on GitHub.                           |
| 10:30-10:45 | Break                                         |                                                         |
| 10:45-11:45 | [Lab 01](../labs/01-first-website/README.md)  | Your first page opens beside Chat.                      |
| 11:45-12:15 | Lab 01's checking block                       | You checked a button and a number yourself.             |
| 12:15-13:00 | Lunch                                         |                                                         |
| 13:00-14:00 | [Lab 02](../labs/02-make-it-useful/README.md) | Your page has your own look and one new feature.        |
| 14:00-14:45 | [Lab 08](../labs/08-save-and-share/README.md) | Your work is saved on GitHub and you keep improving it. |
| 14:45-15:00 | Pair sharing                                  | You showed one feature and how you checked it.          |

Lab numbers are just names, so follow this table from top to bottom. For the other days, see
[your week](../README.md#your-week).

## Your First Note

**10:00-10:30.** The presenter shows each step, then pauses for your turn.

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
anything asks you to create a new repository, says a push was rejected, or mentions a
conflict, stop and ask a helper. Never force a push. If you work in a pair, take turns at the
keyboard.

## The Habit to Keep

**Expect -> try -> compare -> improve -> repeat.** Say what you expect, try it yourself, compare
what you see, and ask for one fix if needed. "Copilot says it works" is not a check. A failed
check is useful information, not lost work.

If Copilot starts changing more than you asked, select **Stop** in Chat, look at what changed,
and ask for something smaller. Stopping does not undo changes, but **Undo** in Chat does: after
each change Copilot shows **Keep** and **Undo**, and you will practice this in Lab 02. Never
approve a command you do not understand.

Tomorrow you build your own idea with [Build Your Own Idea](DAY-2-BUILD.md). Your work from today stays.

## Official References

- [Codespaces overview](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces).
- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Review AI changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Source control in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Topic map (for presenters)](REFERENCES.md).
