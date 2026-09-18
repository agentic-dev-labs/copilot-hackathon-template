# Lab 01: Build Your First Page

**Objective:** Turn your idea into a small website and open it in your browser.

**Time-box:** 60 minutes

**Prerequisites:** Lab 00 and the separate first-note/save/commit/push block in the
[beginner guide](../../docs/START-HERE.md#your-first-note). Use the same Codespace and the
built-in coding Agent in Chat. No research downloads, extra tools, or skills are required.

Work on one page using the shared **fictional weekend planner** brief. Follow the same actions
as the presenter, then personalise the title, activities, and appearance. Own-idea building is
Tuesday's main work. No bookings, accounts, paid services, or real work data.
The presenter shows one action for 3-5 minutes; you try it before the next demonstration.

## 1. Describe a Small Page (15 minutes)

Open Chat and use the shared request, then personalise it after the first page works:

> Read site/brief.md. Create my first page at site/index.html: a fictional weekend planner
> with a title and three activity cards. Include a clearly labelled fictional budget section.
> Use simple HTML, CSS, and JavaScript with local assets. No framework, login, or external service.
> Tell me the small plan before editing, and keep changes inside site/.

Read the plan and ask for a smaller version if needed. Then let Copilot build it.
**You should see:** a new file under **Explorer > site**. **Check:** open it and confirm
the title and activity names match your request. A response saying "created" is not enough.

## 2. Open Your Preview (20 minutes)

The presenter now introduces the **terminal**: a place to give the Codespace a command.
This is not another AI chat. Open **View > Terminal** and run this one prepared command:

```bash
uv run uvicorn app.site:app --host 0.0.0.0 --port 8000
```

Leave that terminal running. Open **Ports > 8000 > Open in Browser** using the globe button
shown in the beginner guide. Keep visibility **Private**.
**You should see:** your page in a browser tab. **Check:** its title is the one you requested.

Your laptop's localhost is not this Codespace. Use the forwarded link from Ports. The preview
lasts while your Codespace and server run; it is not a deployed website. If a helper finds
8000 already occupied, use 8001 and its forwarded link; never stop somebody else's process.

## 3. Make One Change (15 minutes)

Ask: "Change the title to My Saturday Plan and make the activity text easier to read.
Leave the rest alone." Use your own title if you prefer.

Read the changed file in **Source Control**, save it, and refresh the preview.
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
| Old title                       | Save the changed file, refresh the preview, and check you opened the right tab. |
| Command failed                  | Show a helper the error. Do not install software on your laptop.                |
| Copilot changes unrelated files | Stop, inspect the diff, and ask for the smallest correction.                    |
| Button or total is wrong        | State expected versus actual, request a fix, then repeat the check.             |

## Optional extras

1. Make the page comfortable to read in a narrow browser window.
2. Improve the labels or empty state, checking that the original behaviour still works.
3. Use a different fictional price list and verify its units and arithmetic.
   Keep exploring your page; later research and presentation exercises are not prerequisites.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Codespaces ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).
- [Review AI changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Source control](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Whole-week topic map and optional research](../../docs/REFERENCES.md).
