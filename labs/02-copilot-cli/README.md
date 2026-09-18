# Lab 02: Make Your Website Useful

**Objective:** Add one useful interaction, personalise it, and check it yourself.

**Time-box:** 60 minutes

**Prerequisites:** Your working page and manual verification from Lab 01. Stay in the same
browser-based Codespace. No CLI, MCP, or automated browser checks are required today.
The folder name is retained for existing links; Copilot CLI is introduced in the **Day 3** technical track.

## Show, Try, Personalise

The presenter shows one small change, then you try it and personalise it. Keep **one** website.
For the shared weekend planner, add and remove fictional activities, then choose your own
small improvement. No app login, API keys, booking service, or database.

### 1. Agree one feature (10 minutes)

Tell Copilot your idea and audience. Limit the first version to one list, form, or selection.
Use a request like this, changing the subject to your idea:

> In site/index.html, let me add a fictional activity and remove it. Reject an empty name.
> Keep the rest of my page and checked figures unchanged. Propose the smallest change first.

Say your expected result aloud: "When I add Synthetic Picnic, it appears once in the list."
**Check:** the plan changes your existing page, not the framework or another application.

### 2. Build and open it (15 minutes)

Let Copilot implement the agreed change. Review the form labels, empty state, and buttons.
Use fictional entries only. Ask it to display entered names as text, not executable HTML.

If the morning server is still running, reuse it; saving static assets and refreshing is enough.
Otherwise run in the Codespace terminal:

```bash
uv run uvicorn app.site:app --host 0.0.0.0 --port 8000
```

Keep it running; use another terminal for commands. Open **Ports > 8000 > Open in Browser**.
If the port belongs to another process, use 8001 and forward it. Do not stop someone else's
server. Keep visibility **Private**. A preview depends on a running Codespace; it is not deployed.

### 3. Try it yourself (15 minutes)

| Try                       | Expected result                                           |
| ------------------------- | --------------------------------------------------------- |
| Add `Synthetic Picnic`    | It appears once in your list.                             |
| Remove that item          | That item disappears; unrelated items stay.               |
| Submit an empty name      | No empty item is added; the page explains what is needed. |
| Use Tab and Enter         | You can reach and use the controls without a mouse.       |
| Narrow the browser window | Text and buttons remain readable without overlapping.     |

Record what actually happened in your brief. If a check fails, tell Copilot the expected
and actual result, request a focused fix, and repeat that same check. Keeping data after a
refresh is a separate extension; it is not a failure if you have not requested it.

### 4. Make it yours (15 minutes)

Choose one change in wording, colour, arrangement, or a small extra interaction. Describe it
in your own words. Inspect the change and repeat the add/remove checks so an improvement
does not break an existing feature. Show a neighbour and ask what they found confusing.

### 5. Explain your result (5 minutes)

In `site/brief.md`, record what you checked, any limitations, and your next small improvement.
Save the files. The next block repeats review, commit, and push; you can also do that now.

**Done when:** one meaningful interaction works, you made one personal improvement, and
your manual checks and any remaining problems are recorded truthfully. Persistence is optional.

## When It Does Not Work

| Symptom                             | Action                                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------- |
| Blank or missing page               | Confirm `site/index.html`, server terminal, and port; ask Copilot to inspect the exact error |
| Data disappears after refresh       | Remembering data is optional; request it below when ready.                                   |
| A number differs from the source    | Stop and reconcile the value and unit before sharing.                                        |
| Preview works but asset check fails | Keep only allowed website assets under `site/`; move PDFs/extracts to `research/`            |

## Optional extras

1. **Remember my list.** Ask: "Remember my activities in this browser after a refresh. Show a
   useful message if saving is unavailable. Do not store private information or clear other
   apps' data." Add an item, refresh, confirm it remains, remove it, and refresh again.
   The usual implementation is localStorage. It is not a shared database or secret storage;
   a different browser or deployed URL has separate data. The helper checks invalid saved
   data and unavailable storage; you do not need to learn JSON to try the feature.
2. Add sorting, a theme switch, or favourites, then repeat your original checks.
3. Ask for a smaller or clearer version of a control. Stop at one change before asking for more.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) and [storage errors](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API).
- [Forwarded ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace), [reviewing changes](https://code.visualstudio.com/docs/agents/run/review-code-edits), and [whole-week topic map](../../docs/REFERENCES.md).
