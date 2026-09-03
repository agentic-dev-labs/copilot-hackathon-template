# Lab 01: Build with VS Code agent mode

**Objective:** Use agent mode and repository guidance to change your own running app, then prove the change with a test.

**Time-box:** 60 minutes, plus optional extras if you finish early

**Prerequisites:** Completed Lab 00, an active Codespace, and your name set in `config.json`.

## Steps

1. Read `.github/copilot-instructions.md` and identify the evidence and data rules. Everything the agent does is shaped by that file.
2. Start the app with `uvicorn app.main:app --reload` and open the forwarded port 8000. This is your page.
3. Open Copilot Chat, select **Agent**, and ask it to add a **Gaps** column to the table in `app/main.py`.
4. Review the proposed plan and the list of files before approving any edit. Reject anything that touches files you did not expect.
5. Reload the page and confirm your change is visible.
6. Ask the agent to add a test covering a document with no text, then run the targeted test and explain the result.
7. Create `.github/prompts/explain-evidence.prompt.md` with a reusable prompt that asks for direct evidence and one-sentence reasoning.
8. Invoke that prompt on a synthetic sample and check that every claim carries a quotation.
9. Create `.github/instructions/tests.instructions.md` beginning with `applyTo: "tests/**"`, saying
   that every test must assert on a quoted string from the source document. Ask the agent for another
   test and watch it obey a rule that applies only inside `tests/`.

## What you just learned

Instructions and prompts are different tools. Instructions apply automatically and can be scoped to
paths; prompt files are invoked deliberately when you want a task repeated the same way. Agent mode
can edit, run and test across files while you stay in control of the diff.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Argue with it in the browser.** In the integrated browser, select two or three elements on your
   page and comment on each, then let the agent fix them in one batch.
2. **Ask a side question.** Type `/btw` to open a side conversation that borrows the current context
   while the main one keeps running.
3. **Personal versus repository instructions.** Add a personal instruction in VS Code settings that
   contradicts `.github/copilot-instructions.md`, and work out which one wins.
4. **Vague against precise.** Ask for the table to be sorted by score twice, once vaguely and once
   with acceptance criteria. Keep both answers side by side.
