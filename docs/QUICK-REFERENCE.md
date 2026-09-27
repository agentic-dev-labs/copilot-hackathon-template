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
| Start my guided website | In Agent Chat run **`/create-website`** and pick one: Project Planner, Calendar, Ideas Wall, or Weather. It builds straight away. |
| Change its appearance | Creation asks only which website. Afterwards ask Chat for a light Fresh mint, Sky blue, or Soft coral palette, or any other change. |
| See my website beside Chat | Creation opens the preview. Later use **`/start-website`** to reopen the saved page without rebuilding it. |
| See an edit immediately | Ask for one colour or heading change and watch the preview; it updates by itself. |
| Stop my preview | Use **`/stop-website`**. The panel closes. Files and your entries stay; the Codespace keeps running. |
| Fix a blank preview | Show a helper the exact message. There is no server or port to fix. |

## One Good Request

"Change **this one thing** for **this audience**. Keep **these things** unchanged.
Explain the small plan first. I will check it by **this action and expected result**."

Continue the website you chose: one design improvement, then one feature improvement.
[Lab 02](../labs/02-copilot-cli/README.md) offers separate ideas for each of the four websites.
Use normal Chat for changes; do not rerun the creation interview for every edit.

## Preview Help

The learner needs no terminal. Creation opens the approved page automatically; start and stop
use the prepared preview panel. A helper can use **Workshop Website: Open Preview** or
**Close Preview** in the Command Palette, or the **Open Preview** button on an HTML file.
Do not install or configure tools during the lesson; new Codespaces must be rehearsed beforehand.
A preview is not a deployment. The page remembers entries in this browser only.

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

Official help: [Codespaces](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces),
[Markdown preview](https://code.visualstudio.com/docs/languages/markdown),
[Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).