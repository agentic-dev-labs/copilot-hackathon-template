# Lab 01: Build with VS Code agent mode

**Objective:** Use agent mode and repository guidance to change your own running app, then prove the change with a test.

**Time-box:** 60 minutes, plus optional extras if you finish early

**Prerequisites:** Completed Lab 00, an active Codespace, and your name set in `config.json`.

## Steps

1. Read `.github/copilot-instructions.md` and `AGENTS.md`. The first is Copilot-specific; the second is shared repository guidance supported by several agents, including Copilot. Instruction-file support varies by client, and instructions guide behavior rather than enforce access permissions.
2. Start the app with `uvicorn app.main:app --reload` and open the forwarded port 8000. This is your page.
3. Use **Ask** to understand the page, then **Plan** to propose a Gaps column. Include the relevant files as context. In **Agent**, request the implementation: show evaluator-generated gaps for each sample, show `No gaps identified` for the strongest sample, and escape displayed text.
4. Review the plan, tool requests and diff. Stop or reject changes outside the task; do not assume every edit will ask for approval under every permission mode.
5. Reload the page and confirm your change is visible.
6. Ask for a test of the new column and an evaluator test for an empty document: zero passes, ten `Unclear` results, no invented evidence. Reuse existing tests where appropriate. Run the targeted checks, then the full test suite and lint.
7. Create `.github/prompts/explain-evidence.prompt.md`:

   ```markdown
   ---
   description: Explain one synthetic report's evidence without changing its score.
   agent: ask
   ---
   Read ${input:report:Path to the synthetic report} and the attached evaluator result.
   Explain one finding using its exact source quotation and one sentence of reasoning.
   If the report is silent, say so. Do not invent evidence or change the calculated status.
   ```

8. Invoke `/explain-evidence` in a new chat, supply a sample path and its CLI result, and compare the answer with the source.
9. Create `.github/instructions/tests.instructions.md`:

   ```markdown
   ---
   description: Keep workshop tests reproducible and evidence-backed.
   applyTo: "tests/**/*.py"
   ---
   Use synthetic fixtures and pass a fixed review date for time-dependent scoring tests.
   For evidence tests, assert that nonempty quotations occur exactly in the source.
   Mock cloud calls; do not depend on credentials or live services in unit tests.
   ```

   Ask for another test, inspect which instructions were loaded, and verify the resulting assertions.

**Done when:** your page change and tests work, both customization files are committed on your working branch, and the prompt runs in a fresh chat.

## What you just learned

Instructions and prompts are different tools. Instructions apply automatically and can be scoped to
paths; prompt files are invoked deliberately when you want a task repeated the same way. Agent mode
can edit, run and test across files while you stay in control of the diff.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Improve the page (5-10 min).** Use element comments if available in your VS Code build, or attach a screenshot. Ask for one small change and inspect the result.
2. **Ask a side question.** Type `/btw` to open a side conversation that borrows the current context
   while the main one keeps running.
3. **Keep context focused (5 min).** Start a new chat with only the relevant source file and a harmless response preference. Compare it with a long chat. Do not create contradictory safety or evidence rules.
4. **Vague against precise.** Ask for the table to be sorted by score twice, once vaguely and once
   with acceptance criteria. Keep both answers side by side.
