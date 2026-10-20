# Workshop Quick Reference

Keep this short sheet beside you. The presenter shows each step first, so wait for the current
step instead of racing ahead. Use made-up information only.

| I want to... | Where to go |
| --- | --- |
| Find today's guide | Monday until 10:30: the **README** on your repository's GitHub page. Then, in the Explorer, **docs > START-HERE.md**, or the guide the presenter names. |
| Read a guide nicely | Right-click the `.md` file in the Explorer and choose **Open Preview**. It is the same file. |
| Find a file | The **Explorer** is the files icon on the left. Select a folder to open it. |
| Ask Copilot | **View > Chat**. Choose **Ask** for questions, or **Agent** when Copilot should change files. Start with a question, then ask for one small change. |
| Stop Copilot | Select **Stop** in Chat, then look at what already changed. Stopping does not undo it. |
| Undo Copilot's change | Select **Undo** in Chat after the change. To go back further, hover over an earlier question and select **Restore Checkpoint**. |
| Ask what code means | Select a few lines in a file, then ask Chat: "Explain the lines I selected in plain English." |
| See what changed | **Source Control**, the branching-lines icon. Select a file to compare before and after. |
| Save | **File > Save**. This keeps the change in the file, not on GitHub yet. |
| Take a snapshot | In Source Control, select **+** next to the files you checked, type a short message, then **Commit**. |
| Let Copilot write the message | Select the **sparkle icon** in the Source Control message box. Read it and fix anything untrue. |
| See my history on GitHub | On your repository page select **Commits**. On a file, select **History**. |
| Send it to GitHub | **Source Control > ... > Push**. Then open your repository on GitHub to see it. |
| Build my first website | In Chat choose **Agent**, then type **`/create-website`** and pick one of the four websites. |
| Build my own idea | Run **`/create-website`** again and choose your own idea. It gets its own folder under `site/ideas/`. |
| See my website | **`/start-website`** opens it beside Chat. For an idea, add its folder name: `/start-website team-lunch`. |
| Close my website | **`/stop-website`**. Your files and entries stay. |
| Change how it looks | Just ask, for example: "Try a sky blue look. Keep everything else the same." |
| Show Copilot a picture | Drag the picture from the Explorer into the chat box, then ask, for example: "Make my page look like this sketch." |
| Draw a picture for my page | Ask: "Draw a picture for my header: a friendly rocket, in my colors." It appears in a few seconds. |
| Change a picture | Ask: "Change my header picture: make it a night scene." The old picture stays, so you can go back. |
| Add a chat to my page | Type **`/add-chat`**, then select **Ask** at the bottom right of your page. Check its answers yourself. |
| Paste into the terminal | **Ctrl+V** (Windows) or **Cmd+V** (Mac). Allow clipboard access if the browser asks. |
| Use Copilot in the terminal (Day 3) | Type `copilot` and press Enter. Type `/exit` to leave. |
| Use my own agent (Days 3-4) | In Copilot CLI type `/agent` and choose it. After creating a new agent, type `/exit` and `copilot` once so it appears. |
| Run my tests (Days 3-5) | In the terminal type `pytest checks`. Green means pass; red shows what failed. |
| Start a branch (Days 4-5) | Select the branch name at the bottom left, then **Create new branch...**. Go back by choosing `main`, then **Pull**. |
| Hand a story to Copilot (Day 4) | On GitHub: **Issues > New issue > User story for Copilot**, then **Assignees > Copilot**. |
| Approve a release (Day 5) | On GitHub: **Actions**, open the waiting run, **Review deployments > Approve and deploy**. |
| Smoke-test my website (Day 5) | `python3 scripts/smoke_test.py https://<my website address>` |
| Something looks broken | Show a helper the exact message. Do not install anything. |

## One Good Request

"Change **this one thing** for **this audience**. Keep **these things** unchanged. Explain the
small plan first. I will check it by **this action and expected result**."

[Lab 02](../labs/02-make-it-useful/README.md) has ideas for each of the four websites.

## Trust, but Verify

**Expect -> try -> compare -> improve -> repeat.** Click the button yourself. Try an empty entry.
Count a number yourself. Check again after a fix. "Copilot says it works" is not a check, and a
screenshot alone does not prove a button works.

## Your Finish Each Day

**Monday:** your first website, made your own and checked, saved on GitHub, and shown to a neighbor.
**Tuesday:** a first version of your own idea (or a better Monday page), one check, and questions for IT.
Nothing extra is required on Monday or Tuesday: no database, CLI, MCP, or setup. Publishing is
optional, with a helper.
**Wednesday:** your own User Requirements agent, a requirements file with an approved story,
that story working on your page, and green `pytest checks`.
**Thursday:** a merged practice pull request, a story built by Copilot's cloud agent, your own
Code Review agent's report with every finding checked by you, and a merge-or-not decision.
**Friday:** a check that runs on every pull request, a release you approved, a bad release
rolled back, your team demo, and a HANDOFF.md.

Ask a helper about sign-in, conflicts, permissions, or any command you do not understand. Never
paste passwords or real work records into Chat. Do not delete accounts or remove training access
yourself. In pairs, take turns at the keyboard. Before you leave, push your work, then stop your
Codespace at github.com/codespaces; closing the browser tab does not stop it.

[Monday guide](START-HERE.md) | [Tuesday building](DAY-2-BUILD.md) | [Wednesday agents](TOOLS-PRACTICE.md) |
[Thursday cloud agents](DAY-4-BUILD.md) | [Friday CI/CD](DAY-5-SHOWCASE.md) | [Your week](../README.md#your-week)

Official help: [Codespaces](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces),
[Markdown preview](https://code.visualstudio.com/docs/languages/markdown),
[Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
