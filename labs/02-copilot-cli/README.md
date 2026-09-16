# Lab 02: Make It Yours and Make It Remember

**Objective:** Create a useful interactive feature, save its state in the browser, and verify
what actually happens. You can extend the morning presentation or make a small website of your own.

**Time-box:** 60 minutes

**Prerequisites:** Lab 00, the morning research/HTML block, and prepared Playwright MCP.
Use browser-based VS Code in Codespaces. All terminal commands below run in the Codespace's Bash
terminal. The folder name is retained for existing links; the short CLI introduction is now Lab 00.

## Show, Try, Personalise

The presenter alternates small demonstrations with your practice. Work on **one** website.
Choose the morning brief plus saved notes/favourites, or a fictional holiday planner, reading
tracker, recipe collection, or event planner. No login, external database, API keys, paid maps,
or live booking integration is needed. Website code is a means to your useful outcome.

### 1. Agree one feature (10 minutes)

Tell Copilot your idea and audience. Limit the first version to one list, form, or selection.
Use a request like this, changing the subject to your idea:

> Extend my site/index.html with a list of questions to explore. Let me add a question, mark it
> complete, and remove it. Keep my verified figures and source links unchanged. Use semantic
> HTML, CSS, and JavaScript. Propose the smallest change before editing; no new framework.

If starting another idea, keep the reviewed morning presentation as `site/presentation.html`
and use `site/index.html` for the new entry point. Ask before replacing files. Watch the proposed
change, stop an overbroad request, and inspect the actual diff in **Source Control**.

### 2. Build and open it (15 minutes)

Approve the small plan and let Copilot implement it. Review the form labels, empty state, and
buttons. Use fictional entries and render entered text safely, not as raw HTML.

If the morning server is still running, reuse it; saving static assets and refreshing is enough.
Otherwise run in the Codespace terminal:

```bash
uv run uvicorn app.site:app --host 0.0.0.0 --port 8000
```

Keep it running; use another terminal for commands. Open **Ports > 8000 > Open in Browser**.
If the port belongs to another process, use 8001 and forward it. Do not stop someone else's
server. Keep visibility **Private**. A preview depends on a running Codespace; it is not deployed.

### 3. Remember information (15 minutes)

> Save this list in localStorage under a unique key for this app. After a refresh, restore it.
> Reject empty input, handle invalid saved JSON and unavailable storage, and show a useful
> error without breaking the page. Never clear storage belonging to other sites or applications.

Manually add a fictional item, refresh, confirm it remains, remove it, and refresh again.
Then change one thing about the appearance to suit your idea. Do not add real work notes or
confidential data. localStorage is not encrypted secret storage or a shared team database.

### 4. Verify with a browser (15 minutes)

Use Playwright MCP in the same Codespace with this request:

> Open http://localhost:8000 in your browser. Add a unique fictional item, refresh, and verify
> it persists. Remove that item, refresh, and verify it is gone. Check keyboard access and a
> narrow screen. Save screenshots under research/browser/. If a check fails, explain it, fix
> the smallest problem, and repeat that check. Do not invent a defect to demonstrate a fix.

Use your actual port. The automation browser has **separate** storage from your preview tab.
An item entered by you will not automatically appear in Playwright. Its isolated session loses
storage when closed; verify reload persistence within the same session. Screenshots and tool
observations are not a saved CI test. If MCP is blocked, record that and perform the manual
journey; do not call it an automated pass or make the MCP port public.

### 5. Explain your result (5 minutes)

Show a neighbour what it does and one request that improved it. In `site/brief.md`, record
what you checked, any limitations, and how this could help your work. Ask Copilot to review
its own claims against the diff and observed browser results.

**Done when:** your own HTML experience works, one meaningful interaction survives a refresh
in the same browser, removal works after another refresh, and desktop/narrow-screen checks
are recorded truthfully. You can explain why the preview and automation browser have different data.

## When It Does Not Work

| Symptom | Action |
| --- | --- |
| Blank or missing page | Confirm `site/index.html`, server terminal, and port; ask Copilot to inspect the exact error |
| Data disappears after deployment | Different origin means different localStorage; repeat the check at the deployed URL |
| Playwright cannot see your item | Its browser context is separate; create a fictional test item there |
| Chart looks plausible but differs from facts | Stop and reconcile the source values before publishing |
| Preview works but asset check fails | Keep only allowed website assets under `site/`; move PDFs/extracts to `research/` |

## Optional extras

1. Add JSON export/import with input validation so fictional browser data can move to the deployed origin.
2. Add a theme switch, sorting, or favourites without replacing verified content.
3. Ask Copilot to turn the observed journey into a repeatable Playwright test. Running it once
   does not automatically wire it into CI. Keep automation screenshots out of the published site.
4. Try a bounded CLI request in the **Codespace terminal**, such as
   `copilot -p "Read site/brief.md and suggest one usability question. Do not change files."`.
   Do not enable blanket tool permissions; editor and CLI sessions are separate.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices) and [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) and [browser testing](https://playwright.dev/docs/intro).
- [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) and [storage errors](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API).
- [Forwarded ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace), [reviewing changes](https://code.visualstudio.com/docs/agents/run/review-code-edits), and [whole-week topic map](../../docs/REFERENCES.md).
