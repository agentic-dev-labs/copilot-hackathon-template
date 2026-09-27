# Lab 02: Make Your Website Useful

**Objective:** Improve your chosen website's design, add one useful feature, and check the result yourself.

**Time-box:** 60 minutes

**Prerequisites:** Your working page and manual verification from Lab 01. Stay in the same
browser-based Codespace. No CLI, MCP, or automated browser checks are required today.
The folder name is retained for existing links; Copilot CLI is introduced in the **Day 3** technical track.

## Show, Try, Personalise

The presenter shows one small change, then you try it and personalise it. Keep improving your
chosen page before beginning a separate own-idea page.
Use normal conversation with Copilot, not a new creation interview for every change. Your
category and its later ideas are already in your brief. No app login, API keys, booking
service, or database. Your page already remembers your entries in this browser.

### 1. Choose Your Next Two Changes (10 minutes)

Choose **one appearance change** and **one feature change** from your category. These are
options, not a list to finish. If a feature already works, improve it or pick another one.

| Your Website | Appearance Ideas | Feature Ideas |
| --- | --- | --- |
| Project Planner | Sky blue or Soft coral palette, bigger cards, a calmer header | Owner name on each card, due dates, hide finished tasks |
| Calendar | Colour notes by type, larger day numbers, a softer today highlight | Start times, a "this week" count, your country's public holidays |
| Ideas Wall | Larger notes, different sticky-note colours, a bolder headline | A vote button with a count, themes to group ideas, search |
| Weather | A different palette, larger temperature, a friendlier headline | Celsius/Fahrenheit switch, a "what to wear" tip, sunrise and sunset |

Ask: "Read my brief and look at my existing page. I want to improve [appearance] and
[feature]. Suggest two small changes, without building them yet. Keep the rest working."

Say the expected result before approving each change. Work on this website, not another
application. The presenter uses the Project Planner; follow the same process for your category.

### 2. Make the Design Yours (15 minutes)

Describe the appearance in ordinary words. Choose one request, or write your own:

> Keep the page light. Try the Sky blue palette. Keep the text readable and leave the
> content and features unchanged.

> Make the cards easier to scan: give them more space and make the + buttons easier to see.
> Keep my colours.

> Make my page name more prominent and the header artwork a little smaller. Keep the layout
> simple, with no video or new package.

Approve one change, inspect the diff, save, and watch the Website preview update beside
Chat. Explain what you like or what still needs changing. You do not need a design-system name,
CSS codes, or a new framework to request a better design. Keep the page lightweight and local.

If the preview is closed, use **`/start-website`**; Copilot reopens it beside Chat. There is
no server or port to manage. Follow
[Lab 01](../01-vscode-agent/README.md#2-open-your-preview-20-minutes) if blocked.

### 3. Add One Feature for Your Category (15 minutes)

Use one of these requests, adapted to what your site already does:

| Category | Suggested Copilot Request |
| --- | --- |
| Project Planner | "Add an owner name to each task card, shown small under the title, and let me type it when I add a task. Keep the design unchanged." |
| Calendar | "Let me give each note a type: meeting, personal, or deadline, each with its own colour. Keep the design unchanged." |
| Ideas Wall | "Add a thumbs-up button with a count to each idea, and a button to sort by most votes. Keep the design unchanged." |
| Weather | "Add a switch between Celsius and Fahrenheit that remembers my choice. Keep the design unchanged." |

Ask for the smallest plan first, approve it, and let Copilot edit. Ask it to display entered
text as text, not executable HTML. Save the changes and watch the preview update; your saved
entries stay.

### 4. Try, Compare, and Refine (15 minutes)

Use the supplied starting values for your category, not all four. Press **Start again with the
examples** first:

| Your Website | One Example Check |
| --- | --- |
| Project Planner | 1 of 4 done. Tick a second task: 2 of 4, and the bar grows. Untick it: 1 of 4 again. |
| Calendar | 3 notes planned. Add one on Friday: 4. Drag it to Monday: still 4, now on Monday. |
| Ideas Wall | 3 ideas. Add one: 4. Drag it to the front, then remove it: 3 again. |
| Weather | Switch city and compare today's temperature with **the raw forecast data** link. |

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
improvement, and a manual result check recorded truthfully. Saved entries in the browser are
a bonus, not a requirement.

## When It Does Not Work

| Symptom                             | Action                                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------- |
| Blank or missing page               | Show the helper the exact start result; confirm the intended page exists under site/. |
| Data disappears after refresh       | Show the helper; the page should remember entries in this browser.                           |
| A number differs from the source    | Stop and reconcile the value and unit before sharing.                                        |
| Preview works but asset check fails | Keep only allowed website assets under `site/`; move PDFs/extracts to `research/`            |

## Optional extras

1. **Build your own idea (fast finishers).** Only after your page is checked, saved to GitHub,
   and shown to a neighbour/helper: run `/create-website`, choose your own idea, and describe it
   in one sentence. Copilot builds it as an own-idea extension in a separate folder under
   `site/ideas/`, just as beautiful as your first page, which stays unchanged. If time runs
   out, stop and move on; Tuesday protects more own-idea building time.
2. Add sorting, a theme switch, or favourites, then repeat your original checks.
3. Ask for a smaller or clearer version of a control. Stop at one change before asking for more.
4. Entries are remembered with localStorage in this browser. It is not a shared database or
   secret storage; a different browser or deployed URL has separate data.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) and [storage errors](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API).
- [Forwarded ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace), [reviewing changes](https://code.visualstudio.com/docs/agents/run/review-code-edits), and [whole-week topic map](../../docs/REFERENCES.md).
