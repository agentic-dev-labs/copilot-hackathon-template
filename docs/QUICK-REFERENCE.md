# Workshop Quick Reference

Print this short sheet beside the learner's laptop. The presenter shows each action first;
wait for the current step rather than racing through a long lab. Use fictional information only.

| I want to... | Where to go / what to check |
| --- | --- |
| Find the instructions | Open the assigned repository's README, then **Start here**. In Codespaces, open **Explorer > docs > START-HERE.md**. |
| Read a Markdown guide | Right-click the `.md` file in Explorer and select **Open Preview**. Editing view and readable preview are the same file. |
| Find a file | **Explorer**, the files icon on the left; click a folder to expand it and a file to open it. |
| Ask Copilot | **View > Chat**. Start with a question, then describe one small change. |
| Stop an overbroad request | Select **Stop** in Chat. Inspect what already changed; stopping does not undo it. |
| Inspect a change | **Source Control**, the branching-lines icon; select the changed file and compare the actual before/after. |
| Save work | **File > Save**. This updates the working file, not GitHub. |
| Record a version | Review files, select **+** beside only the intended files, type a short message, then **Commit**. |
| Send it to GitHub | **Source Control > ... > Push**. Open the same branch on GitHub and confirm the changed file is there. |
| Start my guided website | In Agent Chat run **`/create-website`**. Choose a starter, answer one question at a time, and approve the small plan. |
| Choose its appearance | Choose a fictional project name, logo style, and a light Fresh mint, Sky blue, or Soft coral palette; describe one or two useful features. |
| See my website beside Chat | Creation opens the first preview. Later use **`/start-website`** to reopen the saved page without rebuilding it. |
| Open it by hand | Open the HTML file, then **Live Preview: Show Preview (Internal Browser)** from the Command Palette. Save edits to refresh. |
| Stop my preview | Use **`/stop-website`**, or **Live Preview: Stop Server** in the Command Palette. Files stay unchanged; the Codespace keeps running. |
| Fix a blank embedded preview | Keep ports **3000/3001 Private**, open their forwarded links once through Ports for GitHub authentication, then reopen the preview. Ask a helper if blocked. |

## One Good Request

"Change **this one thing** for **this audience**. Keep **these things** unchanged.
Explain the small plan first. I will check it by **this action and expected result**."

Continue the website you chose: one design improvement, then one feature improvement.
[Lab 02](../labs/02-copilot-cli/README.md) offers separate weekend, project, and budget examples.
Use normal Chat for changes; do not rerun the creation interview for every edit.

## Preview Fallback With a Helper

The main route needs no terminal. If Live Preview cannot run, the helper introduces this
manual-refresh fallback in the **Codespaces Bash terminal**:

```bash
uv run uvicorn app.site:app --host 0.0.0.0 --port 8000
```

Leave it running and use **Ports > 8000 > Open in Browser**, keeping it private. Save files and
refresh manually on this fallback. Ask about a busy port or error. Your laptop's localhost is
not this Codespace. Neither preview is a deployment; temporary form entries can reset on reload.

## Trust but Verify

**Expect -> try -> compare -> improve -> repeat.** Click the button yourself. Try empty input.
Compare a number, unit, and calculation with the supplied source. Repeat the check after a fix.
"Copilot says it works" is not evidence. A screenshot alone does not prove a button works.

## Your Finish

**Monday:** one guided starter, personalised and checked, with work saved on GitHub and shown
to a neighbour/helper. Only then try an own-idea extension without replacing the first page.
**Tuesday:** your own prototype or an improved default, one checked journey, and questions for IT.
No required database, CLI, MCP, public deployment, or storage setup on either beginner day.

Ask for help with sign-in, conflicts, permissions, or unfamiliar commands. Never paste secrets
or real work records into Chat. Do not delete accounts or remove training access yourself.
Rotate the driver in pairs; do not edit the same files concurrently. Save and push before stopping
your Codespace through the Codespaces menu; closing its browser tab does not immediately stop it.

[Monday guide](START-HERE.md) | [Tuesday building](DAY-2-BUILD.md) | [Agenda](AGENDA.md)

Official help: [Codespaces](https://docs.github.com/en/codespaces/overview),
[Markdown preview](https://code.visualstudio.com/docs/languages/markdown),
[Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices),
[Live Preview](https://github.com/microsoft/vscode-livepreview).