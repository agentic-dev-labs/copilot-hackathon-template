---
name: workshop-rehearsal
description: Use when asked to rehearse the five active workshop labs and the Day 2-5 sessions in Codespaces, diagnose package access, and verify an optional GitHub Actions website deployment without attendee Azure login or Dataverse prerequisites.
---

# Workshop Rehearsal

Read [the rehearsal guide](../../../rehearsal/README.md), then follow the complete task
instructions in [the rehearsal prompt](../../prompts/rehearse-workshop.prompt.md). The prompt's
frontmatter configures the local VS Code agent; its task instructions also apply when this skill
is used in an Agent Host or CLI session. Use tools available in the current client.

## Day Boundaries

- **Day 1** — concepts, Chat, a learner-created website, manual behaviour/source checks, and
  save/commit/push. Storage, research, presentations, and early publication are optional.
- **Day 2** — supported own-idea building with fictional app-local content, not an integration lab.
- **Day 3** — tickets on a project board, Copilot CLI sign-in, a learner-described User
  Requirements agent that adds criteria to each ticket, one approved ticket built, `pytest checks`
  tests, and the ticket closed by its commit. Labs 04 and 06 are optional.
- **Day 4** — a practice pull request, an approved ticket delegated to the cloud agent (Lab 03), a
  learner-described Code Review agent whose findings are verified, `@copilot` fixes, a merge decision.
- **Day 5** — CI/CD: starter check workflow, red then green pull request, Copilot's ticket tried
  in a feature slot, approval-gated publish to the `production` slot, smoke test and revert, team
  demos (human rehearsal), and HANDOFF.md.

Use browser-based Codespaces and Bash throughout. Presenter-local tools do not prove availability.

## Rehearsal Rules

- Execute the labs and checks, not just a summary of the instructions.
- Preserve the source template; complete exercises in the confirmed rehearsal copy.
- Use the helpers in `rehearsal/` for network diagnostics, evidence, and exact-run Actions
  deployment. Core setup must not depend on advanced installs.
- Attendees run no browser profile; the optional Lab 04 browser check is a presenter demonstration.
  Prepare the research profile only if selected. Advanced post-workshop topics stay outside this run.
- Use pinned Playwright MCP through private stdio only in an owner-approved environment where
  Chromium's sandbox starts, and verify actual invocation.
- Optional MarkItDown and storage observations never replace core checks.
- The preserved post-workshop Dataverse guide does not authorize live setup or writes during
  this run.
- Do not sign the attendee into Azure, weaken TLS/sandboxing, expose MCP ports, or mark
  unsupported live features as passed.

Use [the official reference map](../../../docs/REFERENCES.md) and each lab's direct
documentation. Missing access or a required human approval is a concrete blocker, not an
invitation to bypass it.
