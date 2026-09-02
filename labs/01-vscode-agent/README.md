# Lab 01: Build with VS Code agent mode

**Objective:** Use agent mode and repository guidance to make a small, tested Python change.

**Time-box:** 75 minutes

**Prerequisites:** Completed Lab 00 and an active Codespace.

## Steps

1. Read `.github/copilot-instructions.md` and identify the evidence and data rules.
2. Open Copilot Chat, select **Agent**, and ask it to add a test for an empty document.
3. Review the proposed plan and files before approving edits.
4. Ask the agent to run the targeted test and explain the result.
5. Create `.github/prompts/explain-evidence.prompt.md` with a reusable prompt that asks for direct evidence and one-sentence reasoning.
6. Invoke that prompt on the synthetic report and check that every claim has a quotation.
7. Review the diff and keep only changes that satisfy the request.

## What you just learned

Repository instructions shape every interaction, while prompt files capture reusable task context and agent mode can edit and test across files.

**Stretch goal:** Add acceptance criteria to the prompt file and compare the response.
