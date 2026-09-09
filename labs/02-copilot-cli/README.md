# Lab 02: Copilot CLI

**Objective:** Use interactive and non-interactive CLI workflows and delegate bounded work.

**Time-box:** 60 minutes, plus optional extras if you finish early

**Prerequisites:** Completed Lab 00; use the Codespace terminal. Delegation also needs cloud-agent access.

## Presenter Demonstration

The presenter shows interactive planning and execution, one bounded `-p` task, context and
usage controls, stopping/resuming, and cloud delegation. They then invoke a prepared managed
plugin's agent or skill and inspect its origin. A plugin is a distributable capability package;
it is not the CLI runtime, a model, or proof that every declared tool is permitted. Full authoring
and enterprise distribution come on Day 5. Attendees do not need to install the demo plugin here.

## Steps

1. Run `copilot` to start an interactive session and ask it to summarize the evaluator. Use `/help`
   to find plan and model controls. Inspect `/model` and `/context` where available without
   assuming the terminal session shares the VS Code chat's history.
2. Inspect requested tool calls. Approve only commands and files needed for the task; deny broad or destructive actions.
3. Exit, then run `copilot -p "List the ten controls implemented in src/vendor_assurance/evaluator.py"`.
4. Start another interactive session and ask for a test plan before any edits. Inspect `/help`, practise stopping a response, and find the available session-resume controls.
5. Use `/delegate` to send one well-scoped issue-sized task to the Copilot cloud agent.
6. Confirm the delegated goal names acceptance criteria and files in scope.
7. Open the resulting cloud task and note that execution is remote.

The provider/model, context window, reasoning effort, and amount of tool use can affect usage.
Start a fresh session for an unrelated task. Use compaction for a long related task, understanding
that details may be summarized. A permission prompt and an operating-system sandbox are different controls.

**Done when:** you can explain the difference between local CLI execution and cloud delegation, and can find the delegated task. If cloud access is unavailable, complete the local work and record the blocker for Lab 03.

The approval model keeps the operator in control: inspect proposed reads, edits, and commands rather than granting unnecessary access.

## What you just learned

Interactive mode supports iterative work, `copilot -p` supports scripted prompts, approvals bound tool use, and `/delegate` moves a task to the cloud agent.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Split a read-only task (5-10 min).** If `/fleet` is available, ask for separate summaries of
   the chunker and report writer. Check both against their files; do not start competing edits.
2. **Research a question (5-10 min).** If `/research` is available, investigate a topic in this
   repository and inspect its sources. Do not treat a generated reference as verified until opened.
3. **Inspect permissions (5 min).** Check the current permission mode and, where supported, `/sandbox`. Explain which actions still require approval; availability differs by OS and client version.
4. **Inspect scheduling (5 min).** Read `/after` and `/every` help. If you try a scheduled prompt, use a read-only task and remove the schedule before leaving the lab.
5. **Vague against precise.** Compare an ambiguous prompt with one that states acceptance criteria.
6. **Inspect a prepared plugin (5 min).** Use the available plugin/skill list to identify a
   component and its origin. No enterprise setting or new install is needed for this inspection.

## Official References

- [Copilot CLI overview](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli): modes, tools, model selection, context, and execution.
- [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference): current session, delegation, research, fleet, and scheduling commands.
- [Allowing and denying tools](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools) and [sandboxes](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes).
- [CLI context management](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/context-management) and [session history](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/chronicle).
- [Plugins](https://docs.github.com/en/copilot/concepts/agents/about-plugins), [installing plugins](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing), and [managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings).
- [Whole-week coverage and extras](../../docs/REFERENCES.md).
