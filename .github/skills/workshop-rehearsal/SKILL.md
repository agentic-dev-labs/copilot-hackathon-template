---
name: workshop-rehearsal
description: Use when asked to rehearse the eight active workshop labs and own-idea build in Codespaces, diagnose package access, and verify a selected GitHub Actions deployment without attendee Azure login or Dataverse prerequisites.
---

# Workshop Rehearsal

Read [the rehearsal guide](../../../rehearsal/README.md) and then follow the complete task
instructions in [the rehearsal prompt](../../prompts/rehearse-workshop.prompt.md).
The prompt's frontmatter configures the local VS Code agent; its task instructions also apply
when this skill is used in an Agent Host or CLI session. Use tools available in the current client.

Day 1 uses concepts, Chat, a learner-created website, manual behaviour/source checks, and
save/commit/push. Storage, research, presentations, and early publication are optional.
Day 2 is supported own-idea building with fictional app-local content, not an integration lab.
Day 3 introduces CLI/MCP/Playwright in the existing demonstration blocks. Day 4 adds saved
browser checks and one exact-commit website or local-sample vendor release. Use
browser-based Codespaces and Bash throughout. Presenter-local tools do not prove availability.

Execute the labs and checks, not just a summary of the instructions. Preserve the source template;
complete exercises in the confirmed rehearsal copy. Use the helpers in `rehearsal/` for network
diagnostics, evidence, and exact-run Actions deployment. Core setup must not depend on advanced
installs. Prepare CLI/browser profiles for Day 3 and the research profile only if selected.
Use pinned Playwright MCP through private stdio and verify actual invocation. Optional MarkItDown
and storage observations never replace core checks. The preserved post-workshop Dataverse guide
does not authorize live setup or writes during this run. Do not sign the attendee
into Azure, weaken TLS/sandboxing, expose MCP ports, or mark unsupported live features as passed.

Use [the official reference map](../../../docs/REFERENCES.md) and each lab's direct documentation.
Missing access or a required human approval is a concrete blocker, not an invitation to bypass it.
