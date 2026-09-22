# Your First Website With Copilot

Today you will describe an idea, build a small page, check it yourself, and save your work.
You do not need to know how to code. Everything happens in your browser-based Codespace;
nothing is installed on your laptop. Use fictional examples, never private work information.
The presenter demonstrates every essential click, then pauses for your turn. You are not
expected to work through this guide independently. Keep the [printable quick reference](QUICK-REFERENCE.md)
beside you. Monday starts with a guided fictional website; the presenter uses the weekend
planner, with project and budget planners as supported choices. Tuesday protects own-idea building.

## First Block: Understand the Workspace

**09:00-09:30: concepts only. No terminal commands.** Watch the presenter point to the
screenshots below. You do not need to create anything yet.

| Word         | Plain meaning                                                              |
| ------------ | -------------------------------------------------------------------------- |
| GitHub       | The service where your project and its recorded versions are kept.         |
| Repository   | Your project's files and version history, often shortened to "repo".       |
| Codespace    | A working computer in the cloud that you open in your browser.             |
| VS Code      | The editor you see inside that Codespace.                                  |
| Copilot Chat | The assistant you ask questions and request changes from. It can be wrong. |
| Prompt       | Your request to the assistant.                                             |
| File         | One saved piece of your project, such as a note or a web page.             |
| Save         | Update a working file in the Codespace.                                    |
| Commit       | Record a version of selected changes with a short message.                 |
| Push         | Send those commits to your repository on GitHub.                           |
| Preview      | Open your running page to inspect it. This is not a deployment.            |

The sequence is **save -> review -> commit -> push**. Saving does not push. Pushing does
not publish a running website. A chat response is not a saved file unless the file exists.

**Say it back:** Which place holds your working files? Which action sends a recorded version
to GitHub? Where will you check whether the page actually works?

Codespaces provides a familiar VS Code editor with a cloud runtime. A corporate desktop may
have different extensions, authentication, and permissions. Codespaces does not bypass policy
or prevent every external action; use only approved training access and fictional information.

## Find Your Way Around

These are **official documentation screenshots**, not captures of this workshop or proof of
live readiness. Names, colours, positions, and button labels may differ in your Codespace.
The captions are the workshop labels. The presenter points to the matching control on the
actual browser-based screen. No desktop installation is needed.

To read this Markdown file comfortably in Codespaces, find it under **Explorer > docs**,
right-click **START-HERE.md**, and select **Open Preview**. The presenter will show this first.
To return to editing a file, select its editor tab; preview and editing do not create two copies.

### A. Files, Editor, and Chat

![Official labelled VS Code layout: activity bar and Explorer on the left, editor in the centre, secondary sidebar for Chat on the right, and panel below.](https://code.visualstudio.com/assets/docs/editing/userinterface/hero.png)

**Files:** the Explorer in the left sidebar. **Editor:** the opened file in the centre.
**Chat:** normally the right sidebar; open it with **View > Chat** if hidden. Ignore the lower
panel for now. This general VS Code layout image is not a Codespaces session capture.

Source: [Microsoft's VS Code layout guide](https://code.visualstudio.com/docs/getstarted/userinterface).

### B. Review and Record a Change

![GitHub Codespaces screenshot highlighting the plus button used to stage reviewed files in Source Control.](https://docs.github.com/assets/images/help/codespaces/codespaces-commit-stage.png)

**Source Control:** the branching-lines icon on the left. **Changes:** files that differ from
the recorded version. **Plus:** select a reviewed file for your next commit; use the plus beside
that file rather than selecting unrelated changes.

![GitHub Codespaces screenshot highlighting a short commit message and the Commit button.](https://docs.github.com/assets/images/help/codespaces/vscode-commit-button.png)

**Message:** what you changed. **Commit:** record that version. After committing, use the
Source Control **... > Push** command. Our repositories already exist: do not create a new
public repository by following a screenshot's example project.

Source: [GitHub's Codespaces source-control guide](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).

### C. Preview, When We Start Building

![GitHub Codespaces screenshot highlighting the Ports tab and globe button that opens a preview in a browser.](https://docs.github.com/assets/images/help/codespaces/quickstart-forward-port.png)

**Website preview:** open your generated HTML file and choose **Live Preview: Show Preview
(Internal Browser)** from the Command Palette. Keep Chat beside the page in the same window.
This differs from **Open Preview**, which displays a Markdown document. Saved changes refresh
the website automatically; the code tab can be closed without losing the files.

**Ports:** the lower panel listing running previews. **Globe / Open in Browser:** open a private
forwarded URL if access is needed. Live Preview normally uses **3000** and **3001**; keep both
**Private**. Open those URLs once to complete normal GitHub redirects, then reopen the embedded
preview. Use the private external tab if browser policy blocks embedding. A helper can use the
Python preview on **8000** as a manual-refresh fallback; no terminal is needed on the main route.

Source: [GitHub's Codespaces quickstart](https://docs.github.com/en/codespaces/getting-started/quickstart).
GitHub Docs screenshots are reproduced by reference, unmodified, under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with the
[source licence and disclaimer](https://github.com/github/docs/blob/main/LICENSE).
If an image is blocked, use its descriptive caption and ask the presenter to point to the control.

## Today's Route

| When        | Open                                        | You are finished when                                         |
| ----------- | ------------------------------------------- | ------------------------------------------------------------- |
| 09:30-10:00 | [Lab 00](../labs/00-setup/README.md)        | You can find your files and ask Chat a question.              |
| 10:00-10:30 | [Your first note](#your-first-note)         | Your reviewed note is visible in your GitHub repository.      |
| 10:45-11:45 | [Lab 01](../labs/01-vscode-agent/README.md) | Your first page opens in a private preview.                   |
| 11:45-12:15 | Lab 01's verification block                 | You checked a page behaviour and a number against its source. |
| 13:00-14:00 | [Lab 02](../labs/02-copilot-cli/README.md)  | One useful interaction works.                                 |
| 14:00-14:45 | [Lab 08](../labs/08-deploy/README.md)       | Your work is reviewed and pushed; you can keep improving it.  |
| 14:45-15:00 | Pair playback                               | You show one feature and explain how you checked it.          |

The lab numbers are retained for existing links; follow this route, not numerical order.
The [agenda](AGENDA.md) includes breaks, lunch, and the rest of the week.

## Your First Note

This coached **10:00-10:30** block follows Lab 00; it is not extra work inside its 30 minutes.
Use the same Codespace. The presenter demonstrates each step, then pauses for your turn.

1. In Chat choose the built-in **Agent** when the presenter shows it. Ask:
   "Create site/brief.md with my idea: a fictional weekend planner. Include who it is for,
   three things it should show, and one thing I can check. Do not build the website yet."
   The weekend planner is the default; you may describe a fictional project or budget planner
   instead. In Lab 01, `/create-website` asks about your audience, logo, colors, and features,
   one question at a time. Record unrelated ideas for after you finish, check, save, and show
   this first website rather than repeatedly starting again.
2. Open the new file from **Explorer > site > brief.md**. Read it and correct one sentence.
   **Check:** it describes your idea, not a different application.
3. Use **File > Save**. Open **Source Control**, select the note, and read the actual change.
   **Check:** only your intended file is being selected.
4. Select its **+**, type `Describe my website idea`, then **Commit**. Use **... > Push**.
   **Check:** open your assigned repository in a separate GitHub tab, select the same branch,
   and open the note. Your edited sentence must be there.

If Git asks for a new repository, rejects a push, or reports a conflict, stop and ask a helper.
Use the assigned working branch; a helper handles any required pull request. Never force a push
or change permissions. If working in a pair, rotate the driver instead of editing concurrently.

## The Habit to Keep

**Expect -> try -> compare -> improve -> repeat.** Say what you expect, try it yourself,
compare with the source or intended behaviour, and request one correction if needed.
"Copilot says it works" is not a check. A failed check is useful information, not lost progress.

If Copilot starts changing more than you asked, select **Stop**, inspect what already changed,
and ask for a smaller task. Stopping does not undo completed changes. Ask a helper before
restoring or discarding work. Do not approve an unfamiliar command just to clear a prompt.

Tomorrow, follow [Build Your Own Idea](DAY-2-BUILD.md). Keep today's work; a helper will explain
whether you continue the same project or use a separately prepared one. No database connection
or training-account removal is needed to continue.

## Official References

- [Codespaces overview](https://docs.github.com/en/codespaces/overview).
- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Review AI changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Source control in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Microsoft Live Preview](https://github.com/microsoft/vscode-livepreview): same-window preview and refresh on save.
- [Week's topic map](REFERENCES.md).
