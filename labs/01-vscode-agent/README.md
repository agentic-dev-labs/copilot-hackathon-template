# Lab 01: Build with VS Code agent mode

**Objective:** Use agent mode and repository guidance to change your own running app, then prove the change with a test.

**Time-box:** 60 minutes, plus optional extras if you finish early

**Prerequisites:** Completed Lab 00, an active Codespace, and your name set in `config.json`.

## Presenter Demonstration

Watch one small change move from inline suggestions/next-edit suggestions and inline chat to
Ask, Plan, and Agent. The presenter adds focused context, inspects the model/Auto picker,
generates and runs a test, and verifies the page with built-in browser tools. They also show
stopping/steering, a diff, and checkpoint restoration. If Edit mode is offered by the client,
identify it as another scoped editing choice, not a required lab mode.

In the browser, distinguish **Add to Chat** (selected context) from **Share with Agent**
(access to an existing tab). The Customizations editor introduces the files you will create
below. Product links are in [Official References](#official-references).

## Steps

1. Read `.github/copilot-instructions.md` and `AGENTS.md`. The first is Copilot-specific; the second is shared repository guidance supported by several agents, including Copilot. Instruction-file support varies by client, and instructions guide behavior rather than enforce access permissions.
2. Create a working branch for the lab. Start the app with `uv run uvicorn app.main:app --reload` and open the forwarded port 8000. Inspect the model picker; keep the default or Auto if offered. A model choice does not replace the task's instructions or tests.
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

8. Generate the evaluator result before invoking the prompt. Run these commands from the
   repository root in a second Codespace terminal:

   ```bash
   mkdir -p reports/baseline
   uv run vendor-assurance src/vendor_assurance/samples/synthetic_soc2_report.md --as-of 2026-10-26 --output-directory reports/baseline/ > reports/evaluation.json
   ```

   Invoke `/explain-evidence` in a new chat. Supply the synthetic source path and attach
   `reports/evaluation.json`; `agent: ask` selects the built-in Ask role, not a missing
   repository agent. Check the answer against the source and JSON. A general explanation
   of a finding is not permission for the model to recalculate its score.
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

**Done when:** your page change and tests work, both customization files are committed on your
working branch, and the prompt runs in a fresh chat with real evaluator JSON attached.
Review all staged files; generated practice output is not needed in your code-change commit.

## What you just learned

Instructions and prompts are different tools. Instructions apply automatically and can be scoped to
paths; prompt files are invoked deliberately when you want a task repeated the same way. Agent mode
can edit, run and test across files while you stay in control of the diff.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Improve the page (5-10 min).** Use element comments if available in your VS Code build, or attach a screenshot. Ask for one small change and inspect the result.
2. **Try lighter-weight assistance (5 min).** Use inline chat or the Explain/Generate Tests
   smart action on a selection. If `/btw` is available in this client, try a harmless side question.
3. **Keep context focused (5 min).** Start a new chat with only the relevant source file and a harmless response preference. Compare it with a long chat. Do not create contradictory safety or evidence rules.
4. **Vague against precise.** Ask for the table to be sorted by score twice, once vaguely and once
   with acceptance criteria. Keep both answers side by side.
5. **Practise recovery (5 min).** In a separate scratch change, inspect the diff and restore a
   checkpoint if supported. Do not restore over other people's work. Checkpoints do not replace
   commits and do not reverse external service writes.

## Official References

- [Inline and next-edit suggestions](https://code.visualstudio.com/docs/editing/ai-powered-suggestions), [inline chat](https://code.visualstudio.com/docs/chat/inline-chat), and [smart actions](https://code.visualstudio.com/docs/editing/copilot-smart-actions).
- [Chat and context controls](https://code.visualstudio.com/docs/chat/chat-overview), [context/indexing](https://code.visualstudio.com/docs/agents/concepts/context), [planning](https://code.visualstudio.com/docs/agents/run/planning), and [model choice](https://code.visualstudio.com/docs/agents/concepts/language-models).
- [Prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files), [custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions), and [instruction support by client](https://docs.github.com/en/copilot/reference/custom-instructions-support).
- [Built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools): navigation, sharing, element feedback, and verification without an extra server.
- [Review and restore changes](https://code.visualstudio.com/docs/agents/run/review-code-edits) and [testing with AI](https://code.visualstudio.com/docs/agents/guides/test-with-copilot).
- [Whole-week coverage and extras](../../docs/REFERENCES.md).
