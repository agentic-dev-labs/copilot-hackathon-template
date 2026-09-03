# Lab 07: Automations and hooks

**Objective:** Make the agent run without a human starting it, and make every agent action auditable.

**Time-box:** 60 minutes

**Prerequisites:** Completed Lab 03, write access to your repository, and a private or internal repository.

Automations are how a review runs itself. Hooks are how you prove what it did. Together
they answer the two questions a regulated organization always asks: *can this run
unattended*, and *can we show an auditor what happened*.

## Part A: Automations (30 minutes)

An automation defines a task once and runs it whenever a trigger fires, instead of you
starting a session each time. You are no longer designing a conversation. You are designing
four things:

| You design | In an automation, that is |
|---|---|
| A **trigger** | a schedule, or an issue opened, or a pull request opened or updated |
| An **instruction set** | the automation prompt, plus the repository custom instructions |
| A **tool surface** | the tools you grant it, and nothing more |
| An **escalation policy** | a draft pull request, human review, and required workflow approval |

Start with the trigger, not the model. Old automation runs the same path every time; an
agent chooses a path each time, which is exactly why the tool surface and the escalation
policy matter more than the prompt.

1. Open the **Agents** tab in the repository and select the **Automations** pane.
2. Create an automation named `Review a vendor report`.
3. Give it a prompt narrow enough to test. This one is the whole task in four lines:

   > Read the SOC 2 report named in the issue body, from `src/vendor_assurance/samples/`.
   > Run `vendor-assurance <that path> --output-directory reports/`.
   > Commit the generated report on a new branch.
   > Open a draft pull request quoting the score and the gaps list in its description.

4. Choose a trigger. Use **when an issue is created** for this one:
   - on a schedule (hourly, daily, or weekly)
   - when an issue is created
   - when an issue or pull request comment is created
   - when a pull request is opened
   - when a pull request is synchronized
5. Add a search query filter so the automation only fires on issues you intend, such as
   `label:vendor-review`.
6. Select tools. Use **Suggest tools**, then remove everything the task does not need.
7. Open an issue naming one of the three sample reports, then watch the session run.
8. Open the draft pull request it produced. The committed report is the deliverable; the draft
   pull request is the review gate. Nobody started this, and nobody can merge it unreviewed.

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
- By default, automations **ignore events from users without write access**. This is a
  prompt-injection defence: an outsider opening an issue cannot steer your agent.
- Pull requests are attributed to the creator, and a creator cannot approve their own
  pull request, so review control is preserved.
- Workflows still do not run until someone with write access approves them.
- Tool selection is the real scope control. Grant least privilege.

## Part B: Hooks (30 minutes)

Hooks run shell commands at defined points in an agent's workflow. They are the audit
trail and the policy gate.

1. Create `.github/hooks/audit.json` in your team repository:

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "type": "command",
        "bash": "mkdir -p logs && echo \"session start $(date -u +%FT%TZ)\" >> logs/agent-audit.log",
        "timeoutSec": 10
      }
    ],
    "preToolUse": [
      {
        "type": "command",
        "bash": "cat >> logs/agent-audit.jsonl",
        "timeoutSec": 10
      }
    ]
  }
}
```

2. Start a Copilot CLI session in the Codespace and run any small task.
3. Inspect `logs/agent-audit.log` and `logs/agent-audit.jsonl`.
4. Identify, from the log alone, which tools the agent asked to use.
5. Discuss which hook you would use to **block** a command rather than record it.

### Hook types

| Hook | Fires when | Typical use |
|---|---|---|
| `sessionStart` | a session begins or resumes | initialise, log for audit |
| `userPromptSubmitted` | a prompt is submitted | record the request |
| `preToolUse` | before any tool runs | **approve or deny**, enforce policy |
| `postToolUse` | after a tool completes | audit trail, metrics |
| `agentStop` | the agent finishes responding | archive the session |
| `subagentStop` | a subagent finishes | inspect delegated work |
| `errorOccurred` | an error is raised | alerting, error patterns |
| `sessionEnd` | the session ends | clean up, archive reports |

`preToolUse` is the powerful one: it can approve or deny a tool execution, which is how you
block dangerous commands or require approval for sensitive operations.

Hooks live in `.github/hooks/*.json` in the repository and apply to Copilot cloud agent and
Copilot CLI. Copilot CLI also reads personal hooks from `~/.copilot/hooks/*.json`. Use the
`powershell` key alongside `bash` when the agent may run on Windows.

### Constraints

- Hooks run **synchronously and block the agent**. Keep them under about five seconds.
- The default timeout is 30 seconds; set `timeoutSec` deliberately.
- Never log secrets. Validate any untrusted input a hook processes.
- Be careful with hooks that make network calls; they add latency and can leak data.

## What you just learned

Automations remove the human trigger while keeping human review, and hooks turn agent
activity into evidence you can hand to an auditor.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Write the blocking hook.** A `preToolUse` hook that denies any command touching a path outside
   the repository. Describe how you would test it safely before trusting it.
2. **Trigger from a comment.** Add a second automation that fires when somebody comments on a pull
   request, for example to draft release notes.
3. **Automate in Actions instead.** Look at GitHub Agentic Workflows, where the automation lives in
   your repository as a versioned file and is reviewed through a pull request - the opposite
   trade-off to the automations you just built.
4. **Read your own audit trail.** From `logs/agent-audit.jsonl` alone, reconstruct what the agent
   did and decide whether it would satisfy an auditor.
