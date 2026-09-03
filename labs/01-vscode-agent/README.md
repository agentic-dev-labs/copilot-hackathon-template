# Lab 01: Build with VS Code agent mode

**Objective:** Use agent mode and repository guidance to change your own running app, then prove the change with a test.

**Time-box:** 75 minutes

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

## What you just learned

Repository instructions shape every interaction, prompt files capture reusable task context, and agent mode can edit, run, and test across files while you stay in control of the diff.

**Stretch goal:** Ask the agent to sort the table by score, and compare a vague request with one that states acceptance criteria.
