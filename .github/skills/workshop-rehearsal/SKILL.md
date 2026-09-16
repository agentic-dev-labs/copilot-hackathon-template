---
name: workshop-rehearsal
description: Use when asked to run the complete workshop rehearsal in Codespaces, diagnose Python or NuGet package access, finish all nine labs, and verify GitHub Actions deployments without attendee Azure login.
---

# Workshop Rehearsal

Read [the rehearsal guide](../../../rehearsal/README.md) and then follow the complete task
instructions in [the rehearsal prompt](../../prompts/rehearse-workshop.prompt.md).
The prompt's frontmatter configures the local VS Code agent; its task instructions also apply
when this skill is used in an Agent Host or CLI session. Use tools available in the current client.

Day 1 uses public annual-report research, MarkItDown conversion, reviewed skill discovery,
a learner-created HTML brief, an interactive website, and browser storage. Deploy the **website**
target, then prepare the separate **vendor** target for Days 2-5. Use browser-based Codespaces
and its Bash terminal for everything. Presenter-local tools do not prove attendee availability.

Execute the labs and checks, not just a summary of the instructions. Preserve the source template;
complete exercises in the confirmed rehearsal copy. Use the helpers in `rehearsal/` for network
diagnostics, evidence, and exact-run Actions deployment. Use the pinned prepared Playwright MCP
and MarkItDown MCP through private stdio, and test actual invocations. Do not sign the attendee
into Azure, weaken TLS/sandboxing, expose MCP ports, or mark unsupported live features as passed.

Use [the official reference map](../../../docs/REFERENCES.md) and each lab's direct documentation.
Missing access or a required human approval is a concrete blocker, not an invitation to bypass it.
