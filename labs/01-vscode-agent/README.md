# Lab 01: Build Your First Page

**Objective:** Turn your idea into a small website and open it in your browser.

**Time-box:** 60 minutes

**Prerequisites:** Lab 00 and the separate first-note/save/commit/push block in the
[beginner guide](../../docs/START-HERE.md#your-first-note). Use the same Codespace and the
built-in coding Agent in Chat. The guided skill, design kit, and preview panel are already provided;
no research downloads, tool installation, or skill authoring is required.

Choose one starter: **Project Planner**, **Calendar**, **Ideas Wall**, or **Weather**.
The presenter demonstrates the Project Planner; choose it when unsure. Follow the same
actions, then improve it by asking. Finish, check, save, and show this page before an own-idea
page. Fast finishers build their own idea next; everyone else moves on and continues on
Tuesday. No bookings, accounts, paid services, real company branding, or real work data.
The presenter shows one action for 3-5 minutes; you try it before the next demonstration.

## 1. Pick Your Website (15 minutes)

In Agent Chat type **`/create-website`**, select it from the menu, and send it.
It asks one question, which website you want, and then builds it straight away. The page is
named after your repository, for example **AliFarahnak Project Planner**. No names, colours,
or technical choices are needed now; you change anything later just by asking.
The helper can show where the prepared workflow lives; you do not need to author or install a skill.

If the command is missing, ask the helper to open and attach
[the prepared workflow](../../.github/skills/create-website/SKILL.md) to Agent Chat and say
"Follow this guided website workflow; ask me the first question and wait."
Copilot starts from a tested, beautiful design for your choice: one self-contained page, a
small file of fictional sample entries, and a local kit with animated artwork. You do not
choose or install anything.

**You should see:** a new `index.html` under **Explorer > site**. **Check:** open it and confirm
the title uses your repository name. A response saying "created" is not enough.

## 2. Open Your Preview (20 minutes)

After the first build, Copilot opens your page in the **Website preview** panel beside Chat.
If closed later, use **`/start-website`** to reopen the saved page.
**`/stop-website`** closes the panel without deleting the page.
These commands do not repeat the interview or publish anything.

1. Check that your website is visible beside Chat with your repository's name.
2. Press **+** to add one fictional entry, drag it somewhere else, then ask for one small change.
3. Watch the change appear by itself. Your added entry should still be there.
4. Try `/stop-website`, then `/start-website`. Confirm the same page returns.

**You should see:** your page inside the same Codespaces browser tab. **Check:** its title
uses your repository name. This is a live website preview, not Markdown Open Preview.
The page remembers entries in this browser; **Start again with the examples** brings back the start.

### If Preview Is Blocked

Show the helper the exact result; do not install tools or repeatedly open panels.
A helper can check `python3 scripts/website_preview.py status`. There is no server or
port to fix: the panel reads your file directly. A missing helper is a preparation issue,
not a learner exercise. The preview is not a deployment.

## 3. Make One Change (15 minutes)

Ask for one change in ordinary words, for example: "Add a Saturday column" (Project Planner),
"Start the week on Sunday" (Calendar), "Make the notes bigger" (Ideas Wall), or "Add Paris
as a starting city" (Weather). Add: "Leave the rest alone."

Read the changed file in **Source Control** and save it; the preview updates by itself.
**Check:** your requested change is visible and the other content still works.
If too much changed, stop and ask for a focused correction. Stopping is not an undo.

## 4. Explain What You Built (10 minutes)

Show a neighbour the page and the file that produces it. Ask them to add and move one entry.
Record one thing to improve in your brief. Save, review, commit, and push using the sequence
you already practised. Check the same branch on GitHub.

**Done when:** your own page opens in a private preview, one requested change is visible,
and you can find both the file and its saved version in GitHub.

## Coached Verification Block

**11:45-12:15**, outside the 60-minute lab: **trust but verify** is today's main habit.
Use **expect -> try -> compare -> improve -> repeat**; do not invent a defect for the exercise.

1. **Check behaviour (10 minutes).** Ask for one new button, such as "hide finished tasks",
   "show only this week", or "shuffle the ideas". Predict what will happen, click it twice,
   and compare. If it fails, tell Copilot what you expected and what you actually saw. Try the
   same action again after a fix.
2. **Check a number (10 minutes).** Press **Start again with the examples**, then do your
   category's check below yourself. Do not accept a number you have not counted or compared.
3. **Record the check (10 minutes).** In your brief write what you tried, what happened, and
   any remaining limitation. A screenshot or confident answer alone does not prove behaviour.
   Save and review any final changes before committing and pushing.

| Your Website | Check It Yourself |
| --- | --- |
| Project Planner | 4 tasks and 1 ticked, so the bar reads **1 of 4 done**. Tick one more: 2 of 4. |
| Calendar | **3 notes planned**: today, tomorrow, and in three days. Add one: 4 notes planned. |
| Ideas Wall | **3 ideas**. Add one: 4 ideas. Remove one: back to 3. |
| Weather | Open **the raw forecast data** link and compare today's temperature with the page. |

The figures come from [the starters](../../.github/skills/create-website/assets/starters.json).
Weather is the only page with live data, so its numbers change; comparing with the source is
the check. If live weather is blocked, the page says it is showing sample weather.

For a public-source alternative, the facilitator can show one value from the
[official five-year overview](https://annualreport.novonordisk.com/2025/introducing-novo-nordisk/five-year-overview.html)
and the labelled [prepared facts](../../docs/annual-report-facts.json). Check year, unit, and
value against the original. This replaces the count check; it is not a PDF research assignment.

## When It Does Not Work

| What you see                    | Next action                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------- |
| Blank or missing page           | Show a helper the exact message; there is no server or port to fix.             |
| Old title                       | Save once, then show the helper the unchanged preview; do not refresh the whole Codespace. |
| Command failed                  | Show a helper the error. Do not install software on your laptop.                |
| Copilot changes unrelated files | Stop, inspect the diff, and ask for the smallest correction.                    |
| Button or count is wrong        | State expected versus actual, request a fix, then repeat the check.             |

## Optional extras

1. **Build your own idea (fast finishers).** After your checks, saving to GitHub, and showing a
   neighbour/helper, run `/create-website` again and choose your own idea. Describe it in one
   sentence; Copilot builds it just as beautifully in its own folder under `site/ideas/`. Your
   first page stays unchanged. If time runs out, move on to the next lab; Tuesday has more time.
2. Make the page comfortable to read in a narrow browser window.
3. Try one of the later ideas in your brief, such as due dates or colours by type.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Codespaces ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).
- [Review AI changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Source control](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [VS Code webviews](https://code.visualstudio.com/api/extension-guides/webview) and [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).
- [Whole-week topic map and optional research](../../docs/REFERENCES.md).
