# Advanced Reference: Automations, Hooks, and Release Readiness

> **Post-workshop reference, not a workshop lab.** On 14 October 2026 the owner simplified
> Days 3-5 for first-time users, so this material left the schedule. Days, clock times, lab
> numbers, and time-boxes below are historical. Use it later with a technical owner; it does
> not change the [current agenda](../../AGENDA.md). See [the advanced index](README.md).

**Objective:** Trigger a synthetic report review automatically and record selected tool events with a hook.

**Original time-box:** 60 minutes

**Prerequisites:** Completed Lab 03, write access to your repository, and a private or internal repository.

Automations start work when an event occurs. Hooks run code at selected lifecycle points.
This lab teaches the mechanisms; it does not implement a production approval or compliance system.
See [automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations)
and the [hook reference](https://docs.github.com/en/copilot/reference/hooks-reference) for current availability and behavior.

Wednesday's CLI and browser-tool tasks were interactive; they did not schedule a task. Today an event
starts work and hooks observe or constrain selected calls. Keep this exercise on synthetic
vendor reports, not annual-report downloads or production systems. All commands run in the
Codespace Bash terminal. Show and try one trigger, then one harmless hook, in the same time-box.

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
   `python scripts/audit_hook.py` with the matching event name. Set the `bash` command
   and an explicit `timeoutSec` of 10. Inspect the file yourself;
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

`preToolUse` can approve or deny a selected tool execution. This example demonstrates an
exact-name denial; it is not a complete dangerous-command policy or security boundary.

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

## Separate Readiness Block: Save a Browser Check

This is the **11:15-12:30** coached block in the agenda, following the 10:45 demonstration.
It is not additional work inside Lab 07's 60-minute time-box. Use one already observed journey
on your own website or the prepared synthetic vendor reader. A new technical attendee can use
the reader without building a Monday website or connecting live Dataverse.

1. **Agree and author a check (15 minutes).** Ask Copilot to create `scripts/check_browser.cjs`
   using Node's assertion library and the already pinned Playwright package under
   `.devcontainer/browser/node_modules/playwright`. No new test framework or package install.
   Accept an explicit `CHECK_URL`, use headless Chromium with `chromiumSandbox: true` and its
   installed executable, bound waits to ten seconds, and close the browser in `finally`.
   Assert the expected heading and one real interaction, not just that navigation returned.
   Use fresh fictional entries; do not assume Monday's browser data exists in this context.
2. **Run and inspect (20 minutes).** With your preview server running, execute:

   ```bash
   CHECK_URL=http://localhost:8000 node scripts/check_browser.cjs
   ```

   Use the actual port. Run it twice and require repeatable results and a nonzero exit on a
   failed assertion. Inspect the assertions against the page; a script that merely takes a
   screenshot is not a test. Do not claim a tool observation as this saved script's result.

3. **Review and release (25 minutes).** Review the generated script and app diff, run repository
   tests/lint, and inspect CI for the tested commit. A saved browser script does not run in CI
   until a workflow explicitly calls it with its server and dependencies prepared. Record
   local-browser and CI coverage separately. Publish the intended website or vendor target
   through the existing workflow, following Lab 08's helper checks; never enable public writes.
   Choose one target and leave **connect_dataverse** unchecked. For the vendor reader, verify
   the expected local synthetic source; it is not a failed Dataverse connection. A live database
   integration belongs to the preserved post-workshop reference, not this release gate.
4. **Record evidence (15 minutes).** Identify the actual commit, check exits, workflow run, and
   verified endpoint. Repeat the meaningful interaction at that endpoint. Record pending or
   blocked deployment work rather than substituting an older healthy revision. Note one gap
   before a real rollout, and the owner of retention/cleanup.

**Readiness checked when:** the saved browser check runs repeatably, its assertions match the
intended behaviour, the selected deployment is verified, and unsupported claims or remaining
gaps are explicit. No workshop result certifies a regulated production system.

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
- [Review generated output](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code) and [whole-week coverage](../../REFERENCES.md).
