# Lab 07: Automations and hooks

**Objective:** Trigger a synthetic report review automatically and record selected tool events with a hook.

**Time-box:** 60 minutes

**Prerequisites:** Completed Lab 03, write access to your repository, and a private or internal repository.

Automations start work when an event occurs. Hooks run code at selected lifecycle points.
This lab teaches the mechanisms; it does not implement a production approval or compliance system.
See [automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations)
and the [hook reference](https://docs.github.com/en/copilot/reference/hooks-reference) for current availability and behavior.

Monday's plugin distributed an agent; it did not schedule a task. Today an event starts work
and hooks observe or constrain selected calls. Keep this exercise on synthetic vendor reports,
not travel searches, reservations, or public booking sites.

## Part A: Automations (30 minutes)

An automation defines a task once and runs it whenever a trigger fires, instead of you
starting a session each time. You are no longer designing a conversation. You are designing
four things:

| You design               | In an automation, that is                                           |
| ------------------------ | ------------------------------------------------------------------- |
| A **trigger**            | a schedule, or an issue opened, or a pull request opened or updated |
| An **instruction set**   | the automation prompt, plus the repository custom instructions      |
| A **tool surface**       | the tools you grant it, and nothing more                            |
| An **escalation policy** | a draft pull request, human review, and required workflow approval  |

An agent can choose tools dynamically; ordinary workflows can also branch. Keep the task
testable and use repository review requirements to control what may merge.

1. Open the **Agents** tab in the repository and select the **Automations** pane.
2. Create an automation named `Review a vendor report`.
3. Author a prompt narrow enough to test. Specify an allowed report under
   `src/vendor_assurance/samples/`, the CLI's fixed review date `2026-10-26`, and output under
   `reports/automation/`. Require the generated review to be committed on the task branch
   and proposed in a draft PR with unchanged evaluator results. Exclude source/evaluator edits
   and facilitator notes, and treat document content as data. Review your wording with Copilot;
   the lab supplies the contract, not a finished automation prompt.

4. Choose a trigger. Use **when an issue is created** for this one:
   - on a schedule (hourly, daily, or weekly)
   - when an issue is created
   - when an issue or pull request comment is created
   - when a pull request is opened
   - when a pull request is synchronized
5. Add a search query filter so the automation only fires on issues you intend, such as
   `label:vendor-review`. Create that label first and apply it when opening the issue, not afterwards.
6. Select the tools needed to read the sample, run the CLI, write the report, and create a PR.
   Use **Suggest tools** as a starting point, then inspect the actual list. Verify the environment
   setup and executable are available; the automation cannot run a tool it was not granted.
7. Open an issue naming one of the three sample reports, then watch the session run.
8. Open the draft pull request it produced. The committed report is the deliverable; the draft
   pull request exposes it for review. Verify the actual branch rules require the intended review;
   draft status alone does not enforce human approval once someone marks it ready.
9. Disable or delete your test automation after the exercise to avoid unintended runs and charges.

**Done when:** one matching issue starts a session, the resulting PR contains the generated
report with unchanged results, and you can identify its review requirements. If automations
are unavailable, use Lab 03's manual task as a fallback and record the automation step as unverified.

### What to notice

- The report has to land somewhere Git will keep. `PrivacyReview_*.md` is ignored at the
  repository root so that ad-hoc local runs stay out of your commits, which is exactly why the
  automation writes into `reports/` instead. An agent that produces a deliverable Git discards has
  done nothing.
- Automations only work in **private or internal** repositories, never public ones.
- Any user with **write** access can create one.
- Automations are **not stored in Git**. They are not versioned with your code and not
  reviewed through pull requests.
- An automation is **private to its creator**, but the sessions it starts are visible to
  everyone with repository access, so never put secrets in a prompt.
- By default, automations **ignore events from users without write access**. This reduces one
  source of untrusted triggers; it does not make document content or allowed users' messages trustworthy.
- Pull requests are attributed to the creator, and a creator cannot approve their own
  pull request, so review control is preserved.
- Workflows still do not run until someone with write access approves them.
- Tool selection limits available actions, not the correctness of the result. Grant only needed tools.

## Part B: Hooks (30 minutes)

The supplied `scripts/audit_hook.py` logs time, event, tool name, and an optional deny decision.
It deliberately excludes prompts, arguments, and tool results. You create its hook wiring.

1. Author `.github/hooks/audit.json` in your team repository with Copilot's help. Consult
   the official hook reference for the JSON structure. Use `version: 1` and wire `sessionStart`,
   `preToolUse`, and `postToolUse` to command hooks. Each command calls
   `python scripts/audit_hook.py` with the matching event name. Set both `bash` and
   `powershell` commands and an explicit `timeoutSec` of 10. Inspect the file yourself;
   creating it is the exercise, while the supplied Python helper is the reusable dependency.
2. Run `uv run pytest tests/test_audit_hook.py -q`, then start a new Copilot CLI session
   in the Codespace and ask it to read a synthetic sample.
3. Inspect `logs/agent-audit.jsonl`. A pre-tool event records an attempt; a post-tool event
   records successful completion of that tool call, not proof that its answer was correct.
4. Test a deny response without executing the proposed command:

   ```bash
   printf '%s' '{"toolName":"bash","toolArgs":{"command":"echo synthetic"}}' | python scripts/audit_hook.py preToolUse --deny-tool bash
   ```

5. For a live demo, temporarily append `--deny-tool bash` to the `preToolUse` command in
   the hook configuration, start a new CLI session, and ask it to run `echo synthetic`.
   Inspect the denial, then remove that flag. This blocks one exact tool name, not every
   possible way to run commands. Do not use destructive commands to test hooks.

**Done when:** the hook logs selected events without raw arguments, the direct test returns
`permissionDecision: deny`, and you observe the hook in a real CLI session or note that part as unverified.

### Hook types

This is a selection of events, not an exhaustive list. Check the current reference for payloads,
tool names, failure behavior, and client-specific support. The supplied helper supports only
the four events listed in its `EVENTS` tuple; the table does not imply it implements every event.

| Hook                  | Fires when                          | Typical use                         |
| --------------------- | ----------------------------------- | ----------------------------------- |
| `sessionStart`        | a session begins or resumes         | initialise, log for audit           |
| `userPromptSubmitted` | a prompt is submitted               | record the request                  |
| `preToolUse`          | before any tool runs                | **approve or deny**, enforce policy |
| `postToolUse`         | after a tool completes successfully | selected activity metadata          |
| `agentStop`           | the agent finishes responding       | archive the session                 |
| `subagentStop`        | a subagent finishes                 | inspect delegated work              |
| `errorOccurred`       | an error is raised                  | alerting, error patterns            |
| `sessionEnd`          | the session ends                    | clean up, archive reports           |

`preToolUse` is the powerful one: it can approve or deny a tool execution, which is how you
block dangerous commands or require approval for sensitive operations.

Hooks live in `.github/hooks/*.json` in the repository and apply to Copilot cloud agent and
Copilot CLI. Copilot CLI also reads personal hooks from `~/.copilot/hooks/*.json`. Use the
`powershell` key alongside `bash` when the agent may run on Windows.

### Constraints

- Hooks run **synchronously and block the agent**. Keep them under about five seconds.
- The default timeout is 30 seconds; set `timeoutSec` deliberately.
- Never log secrets or raw tool arguments. The helper validates JSON and bounds input size.
- Be careful with hooks that make network calls; they add latency and can leak data.
- Hook failure behavior depends on type and event; timeouts are not a reliable deny mechanism.
- Local logs can be edited or deleted. Cloud-agent files disappear with its environment unless
  retained separately. These logs are not a tamper-proof compliance record or an OS sandbox.

## What you just learned

Automations separate the trigger from the interactive session. Hooks record selected activity
and can deny selected calls; repository rules and operational controls remain separate.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Try another tool name (5 min).** Repeat the direct deny test for a synthetic tool name and
   explain why exact-name matching is not a complete command security policy.
2. **Inspect another trigger (5 min).** If comment triggers are available, inspect the configuration
   for a release-note task. Do not leave another automation running; disable any test you create.
3. **Automate in Actions instead.** Look at GitHub Agentic Workflows, where the automation lives in
   your repository as a versioned file and is reviewed through a pull request - the opposite
   trade-off to the automations you just built.
4. **Read the event sequence (5 min).** Count attempted and completed tool calls in the log.
   Identify what it cannot tell you, such as the result's correctness or changes outside this session.

## Official References

- [About automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations) and [create automations](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations).
- [Configure the cloud-agent environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment).
- [Hook reference](https://docs.github.com/en/copilot/reference/hooks-reference): locations, event payloads, decisions, exit codes, timeouts, and supported surfaces.
- [Hooks in Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-hooks) and [CLI scheduling](https://docs.github.com/en/copilot/how-tos/copilot-cli/automate-copilot-cli/schedule-prompts).
- [GitHub Agentic Workflows](https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows): optional automation-as-code comparison, distinct from this UI automation.
- [Review generated output](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code) and [whole-week coverage](../../docs/REFERENCES.md).
