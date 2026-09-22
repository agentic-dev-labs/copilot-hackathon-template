# Lab 02: Make Your Website Useful

**Objective:** Improve your chosen website's design, add one useful feature, and check the result yourself.

**Time-box:** 60 minutes

**Prerequisites:** Your working page and manual verification from Lab 01. Stay in the same
browser-based Codespace. No CLI, MCP, or automated browser checks are required today.
The folder name is retained for existing links; Copilot CLI is introduced in the **Day 3** technical track.

## Show, Try, Personalise

The presenter shows one small change, then you try it and personalise it. Keep improving your
chosen starter before beginning a separate own-idea extension.
Use normal conversation with Copilot, not a new creation interview for every change. Your
category, title, audience, logo, and first features are already in your brief. Keep those choices
unless you ask to change them. No app login, API keys, booking service, or database.

### 1. Choose Your Next Two Changes (10 minutes)

Choose **one appearance change** and **one feature change** from your category. These are
options, not a list to finish. If a feature already works, improve it or pick another one.

| Your Website | Appearance Ideas | Feature Ideas |
| --- | --- | --- |
| Weekend planner | Lighter colors, clearer activity images or symbols, easier-to-read costs | Add/remove activities, filter by activity type, show a remaining budget |
| Project planner | Clearer task rows, distinct status labels, a smaller project header | Mark tasks complete, filter by status, add a task or a priority |
| Budget planner | Larger totals, clearer expense labels, a calm light palette | Add/remove expenses, filter by category, show a warning when over budget |

Ask: "Read my brief and look at my existing page. I want to improve [appearance] and
[feature]. Suggest two small changes, without building them yet. Keep the rest working."

Say the expected result before approving each change. Work on this website, not another
application. The presenter uses the weekend planner; follow the same process for your category.

### 2. Make the Design Yours (15 minutes)

Describe the appearance in ordinary words. Choose one request, or write your own:

> Keep the page light. Try the Sky blue palette with a pale peach accent. Keep the text readable
> and leave the content and features unchanged.

> Make the list easier to scan: align the amounts, give the rows more space, and make the
> main action clear. Keep my logo and colors.

> Make my fictional project name more prominent and its symbol smaller. Keep the layout
> simple, with no large banner, video, or new package.

Approve one change, inspect the diff, save, and watch the embedded Live Preview update beside
Chat. Explain what you like or what still needs changing. You do not need a design-system name,
CSS codes, or a new framework to request a better design. Keep the page lightweight and local.

If the preview is closed, use **`/start-website`**, or open `site/index.html` and run **Live Preview: Show Preview
(Internal Browser)** from the Command Palette. Keep ports 3000/3001 private. Follow
[Lab 01](../01-vscode-agent/README.md#2-open-your-preview-20-minutes) for authentication or the
helper's manual-refresh Python fallback. Do not make a port public or stop another process.

### 3. Add One Feature for Your Category (15 minutes)

Use one of these requests, adapted to what your site already does:

| Category | Suggested Copilot Request |
| --- | --- |
| Weekend planner | "Let me add and remove a fictional activity with a cost. Reject empty names and negative costs. Update the total. Keep the design unchanged." |
| Project planner | "Let me mark a task complete and show only unfinished tasks. Keep completed tasks so I can see them again. Update the completed count. Keep the design unchanged." |
| Budget planner | "Let me add a fictional expense and see the remaining budget update. If the total exceeds the budget, show the amount over budget in words as well as color. Keep the design unchanged." |

Ask for the smallest plan first, approve it, and let Copilot edit. Ask it to display entered
names as text, not executable HTML. Save the changes. Live refresh may reset temporary entries;
that is expected unless you have chosen the optional remembering feature.

### 4. Try, Compare, and Refine (15 minutes)

Use the supplied fictional starting values for your category, not all three:

| Your Website | One Example Check |
| --- | --- |
| Weekend planner | The starting total is USD 13 per person. Add Synthetic Picnic at USD 4: it becomes USD 17. Remove it: USD 13 again. |
| Project planner | Start with one of three tasks done. Complete a second: two of three. The unfinished filter shows one task; switching back shows all three. |
| Budget planner | Start with USD 350 spent from USD 500. Add a USD 30 expense: USD 380 spent and USD 120 remaining. Remove it: USD 150 remaining. |

If you chose another feature or changed the entries, write your expected result first from
your current fictional data. Also try an empty input or empty filtered view, keyboard Tab/Enter,
and a narrow preview window. Do old features still work? Are controls readable and reachable?

When something is wrong, say: "I expected [result]. I actually saw [result]. Fix only that,
and keep [working feature] unchanged." Try the same check again after the fix. A confident
Chat answer or a screenshot is not proof of a working interaction.

### 5. Explain and Save Your Result (5 minutes)

Show a neighbour your visual change and your feature. In `site/brief.md`, record what you
tried, what happened, any limitations, and your next improvement. Save the files. The next
block repeats review, commit, and push; you can also do that now.
Leave preview open while improving. When finished previewing, **`/stop-website`** stops it
without deleting files; the Codespace continues running until you stop it separately.

**Done when:** your chosen category has a personal design change, one working feature
improvement, and a manual result check recorded truthfully. Persistence is optional.

## When It Does Not Work

| Symptom                             | Action                                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------- |
| Blank or missing page               | Confirm the intended HTML file, Live Preview, and private forwarded ports; follow Lab 01's fallback. |
| Data disappears after refresh       | Remembering data is optional; request it below when ready.                                   |
| A number differs from the source    | Stop and reconcile the value and unit before sharing.                                        |
| Preview works but asset check fails | Keep only allowed website assets under `site/`; move PDFs/extracts to `research/`            |

## Optional extras

1. **Remember my list.** Ask: "Remember my fictional activities, tasks, or expenses in this browser after a refresh. Show a
   useful message if saving is unavailable. Do not store private information or clear other
   apps' data." Add an item, refresh, confirm it remains, remove it, and refresh again.
   The usual implementation is localStorage. It is not a shared database or secret storage;
   a different browser or deployed URL has separate data. The helper checks invalid saved
   data and unavailable storage; you do not need to learn JSON to try the feature.
2. Add sorting, a theme switch, or favourites, then repeat your original checks.
3. Ask for a smaller or clearer version of a control. Stop at one change before asking for more.
4. Only after the starter is checked, saved to GitHub, and shown to a neighbour/helper, try an
   own-idea extension in a separate folder. Preserve your first website; starting over is not required.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) and [storage errors](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API).
- [Forwarded ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace), [reviewing changes](https://code.visualstudio.com/docs/agents/run/review-code-edits), and [whole-week topic map](../../docs/REFERENCES.md).
