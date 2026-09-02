# Lab 02: Copilot CLI

**Objective:** Use interactive and non-interactive CLI workflows and delegate bounded work.

**Time-box:** 75 minutes

**Prerequisites:** Completed Lab 00; use the Codespace terminal.

## Steps

1. Run `copilot` to start an interactive session and ask it to summarize the evaluator.
2. Inspect requested tool calls. Approve only commands and files needed for the task; deny broad or destructive actions.
3. Exit, then run `copilot -p "List the ten controls implemented in src/vendor_assurance/evaluator.py"`.
4. Start another interactive session and ask for a test plan before any edits.
5. Use `/delegate` to send one well-scoped issue-sized task to the Copilot cloud agent.
6. Confirm the delegated goal names acceptance criteria and files in scope.
7. Open the resulting cloud task and note that execution is remote.

The approval model keeps the operator in control: inspect proposed reads, edits, and commands rather than granting unnecessary access.

## What you just learned

Interactive mode supports iterative work, `copilot -p` supports scripted prompts, approvals bound tool use, and `/delegate` moves a task to the cloud agent.

**Stretch goal:** Compare results from an ambiguous prompt and one with explicit acceptance criteria.
