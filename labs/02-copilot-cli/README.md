# Lab 02: Copilot CLI

**Objective:** Use interactive and non-interactive CLI workflows and delegate bounded work.

**Time-box:** 60 minutes, plus optional extras if you finish early

**Prerequisites:** Completed Lab 00; use the Codespace terminal. Delegation also needs cloud-agent access.

## Steps

1. Run `copilot` to start an interactive session and ask it to summarize the evaluator.
2. Inspect requested tool calls. Approve only commands and files needed for the task; deny broad or destructive actions.
3. Exit, then run `copilot -p "List the ten controls implemented in src/vendor_assurance/evaluator.py"`.
4. Start another interactive session and ask for a test plan before any edits. Inspect `/help`, practise stopping a response, and find the available session-resume controls.
5. Use `/delegate` to send one well-scoped issue-sized task to the Copilot cloud agent.
6. Confirm the delegated goal names acceptance criteria and files in scope.
7. Open the resulting cloud task and note that execution is remote.

**Done when:** you can explain the difference between local CLI execution and cloud delegation, and can find the delegated task. If cloud access is unavailable, complete the local work and record the blocker for Lab 03.

The approval model keeps the operator in control: inspect proposed reads, edits, and commands rather than granting unnecessary access.

## What you just learned

Interactive mode supports iterative work, `copilot -p` supports scripted prompts, approvals bound tool use, and `/delegate` moves a task to the cloud agent.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Split the work.** Use `/fleet` to break one request into independent subtasks and run them in
   parallel.
2. **Ask it to go and read.** Use `/research` on a topic in this repository and see how the answer
   differs from a plain question.
3. **Inspect permissions (5 min).** Check the current permission mode and, where supported, `/sandbox`. Explain which actions still require approval; availability differs by OS and client version.
4. **Inspect scheduling (5 min).** Read `/after` and `/every` help. If you try a scheduled prompt, use a read-only task and remove the schedule before leaving the lab.
5. **Vague against precise.** Compare an ambiguous prompt with one that states acceptance criteria.
