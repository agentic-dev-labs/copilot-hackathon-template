# Lab 01: Build Your First Page

**Objective:** Turn your idea into a small website and open it in your browser.

**Time-box:** 60 minutes

**Prerequisites:** Lab 00 and the separate first-note/save/commit/push block in the
[beginner guide](../../docs/START-HERE.md#your-first-note). Use the same Codespace and the
built-in coding Agent in Chat. The guided skill and Live Preview are already provided;
no research downloads, tool installation, or skill authoring is required.

Choose one fictional starter: **weekend planner**, **project planner**, or **budget planner**.
The presenter demonstrates the weekend planner; choose it when unsure. Follow the same
actions, then personalise the title and appearance. Finish, check, save, and show this starter
before an own-idea extension. Tuesday protects more own-idea building time. No bookings,
accounts, paid services, real company branding, or real work data.
The presenter shows one action for 3-5 minutes; you try it before the next demonstration.

## 1. Describe a Small Page (15 minutes)

In Agent Chat type **`/create-website`**, select it from the menu, and send it.
It should ask one question and wait: choose your starter, title, audience, logo style, colors,
and useful features. Accept the recommended defaults when unsure. No diagram tool, image API
key, or technical specification is needed.
Read the small plan and approve it before anything is built. The helper can show where the
prepared workflow lives; you do not need to author or install a skill.

If the command is missing, ask the helper to open and attach
[the prepared workflow](../../.github/skills/create-website/SKILL.md) to Agent Chat and say
"Follow this guided website workflow; ask me the first question and wait."
The existing HTML/CSS/JavaScript stack stays unchanged. CSS and a local font provide the
shared look; Copilot creates your own page and interaction, not a copy of a finished website.

**You should see:** a new file under **Explorer > site**. **Check:** open it and confirm
the title and activity names match your request. A response saying "created" is not enough.

## 2. Open Your Preview (20 minutes)

After building, the guided workflow tries to open this preview, using supported editor tools
or guiding the action below. If stopped or closed later, use **`/start-website`** to reopen
your existing page. **`/stop-website`** stops preview without deleting it. These commands do
not repeat the creation interview or publish a site. A helper handles missing tool support.

1. Open **Explorer > site > index.html**.
2. Open **View > Command Palette** and choose **Live Preview: Show Preview (Internal Browser)**.
3. Keep the website preview in the centre and Copilot Chat on the right. Close the code tab
   if it gets in the way; your files remain saved.
4. Ask for a small change, save the edited file, and watch the preview refresh automatically.

**You should see:** your page inside the same Codespaces browser tab. **Check:** its title
is the one you requested. This is a live-refresh website preview, not Markdown Open Preview.
Temporary form entries may reset when a page reloads; remembering entries is optional.

If the preview is blank or asks for access, open **Ports**. Keep **3000** and **3001**
**Private**, open their forwarded URLs with **Open in Browser**, allow the normal GitHub
authentication redirects, then close those tabs and reopen the embedded preview. These are
the page and refresh connections. A helper checks the actual ports if either number was busy.
Never make a port public to fix embedding. An external private tab remains a valid fallback.

### Python Fallback With a Helper

If Live Preview cannot run, the helper introduces the terminal and this prepared command:

```bash
uv run uvicorn app.site:app --host 0.0.0.0 --port 8000
```

Leave that terminal running. Open **Ports > 8000 > Open in Browser** and keep visibility
**Private**. Save files and refresh manually on this fallback; it is not the live-refresh server.

Your laptop's localhost is not this Codespace. Use the forwarded link from Ports. The preview
lasts while your Codespace and server run; it is not a deployed website. If a helper finds
8000 already occupied, use 8001 and its forwarded link; never stop somebody else's process.

## 3. Make One Change (15 minutes)

Ask: "Change the title to My Saturday Plan and make the activity text easier to read.
Leave the rest alone." Use your own title if you prefer.

Read the changed file in **Source Control** and save it; the embedded preview refreshes.
**Check:** your requested change is visible and the other content still works.
If too much changed, stop and ask for a focused correction. Stopping is not an undo.

## 4. Explain What You Built (10 minutes)

Show a neighbour the page and the file that produces it. Ask them to find an activity.
Record one thing to improve in your brief. Save, review, commit, and push using the sequence
you already practised. Check the same branch on GitHub.

**Done when:** your own page opens in a private preview, one requested change is visible,
and you can find both the file and its saved version in GitHub.

## Coached Verification Block

**11:45-12:15**, outside the 60-minute lab: **trust but verify** is today's main habit.
Use **expect -> try -> compare -> improve -> repeat**; do not invent a defect for the exercise.

1. **Check behaviour (10 minutes).** Ask for a button that shows or hides the activity list.
   Predict what will happen, click it twice, and compare. If it fails, tell Copilot what you
   expected and what you actually saw. Try the same action again after a fix.
2. **Check a number (10 minutes).** Use the source below. Ask Copilot to show the two activity
   costs and their total on your page. Compare both amounts and the currency with the source,
   then calculate the total yourself: **USD 13 per person**. Do not accept a different unit.
3. **Record the check (10 minutes).** In your brief write what you tried, what happened, and
   any remaining limitation. A screenshot or confident answer alone does not prove behaviour.
   Save and review any final changes before committing and pushing.

For project or budget starters, use your selected entry in
[the fictional briefs](../../.github/skills/create-website/assets/starters.json): the project
starts at **USD 75**, with **USD 25** remaining and **one of three tasks done**; the budget
starts at **USD 350**, with **USD 150** remaining. Check your own figure and unit manually.

### Supplied Fictional Price List

This is synthetic source material for checking a figure, not live travel research.

| Activity               | Price per person |
| ---------------------- | ---------------- |
| Synthetic museum visit | USD 8            |
| Synthetic garden visit | USD 5            |

For a public-source alternative, the facilitator can show one value from the
[official five-year overview](https://annualreport.novonordisk.com/2025/introducing-novo-nordisk/five-year-overview.html)
and the labelled [prepared facts](../../docs/annual-report-facts.json). Check year, unit, and
value against the original. This replaces the price check; it is not a PDF research assignment.

## When It Does Not Work

| What you see                    | Next action                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------- |
| Blank or missing page           | Ask a helper to check the file, running server, and actual port.                |
| Old title                       | Save, check the preview tab and its refresh connection; the Python fallback needs a manual refresh. |
| Command failed                  | Show a helper the error. Do not install software on your laptop.                |
| Copilot changes unrelated files | Stop, inspect the diff, and ask for the smallest correction.                    |
| Button or total is wrong        | State expected versus actual, request a fix, then repeat the check.             |

## Optional extras

1. Make the page comfortable to read in a narrow browser window.
2. Improve the labels or empty state, checking that the original behaviour still works.
3. Use a different fictional price list and verify its units and arithmetic.
4. After completing your checks, saving to GitHub, and showing a neighbour/helper, invoke
   `/create-website` again for an own-idea extension. Agree a separate folder under `site/ideas/`;
   never replace your first page. Keeping your current page and improving it is equally valid.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Codespaces ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).
- [Review AI changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Source control](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Live Preview](https://github.com/microsoft/vscode-livepreview) and [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).
- [Whole-week topic map and optional research](../../docs/REFERENCES.md).
