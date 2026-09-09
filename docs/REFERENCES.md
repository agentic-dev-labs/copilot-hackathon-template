# Copilot Coverage and Official References

Use this guide during demonstrations, labs, and Q&A. The [agenda](AGENDA.md) sets the order;
each lab has its own short reference list. Product behavior was reviewed against official
documentation on **2026-09-09**. Links point to living documentation, not frozen feature promises.

For a complete run in a dedicated Codespaces copy, use the [rehearsal package](../rehearsal/README.md).
Its prompt, skill, package-network diagnostics, and exact-commit deployment checks use these
references without turning unavailable live features into a passed rehearsal.

**Coverage:** Day 1 introduces the main capability families. Later days teach their implementation.
**Demo** means a short presenter workflow; **Lab** means attendees perform it; **Tour** means a
prepared result or brief introduction; **Reference** means optional exploration, not required work.
Preview availability, UI names, models, and policies must be checked in the actual client.
Covering a family does not mean demonstrating every command, provider, or administrative API.

## Start Here

| Official documentation | When to use it |
|---|---|
| [Copilot features](https://docs.github.com/en/copilot/get-started/features) | Map assistive, agentic, customization, and administration capabilities |
| [Getting started](https://docs.github.com/en/copilot/get-started) | Choose a supported client and understand access |
| [Concepts](https://docs.github.com/en/copilot/concepts) | Understand models, context, agents, tools, policies, and usage |
| [How-to index](https://docs.github.com/en/copilot/how-tos) | Find the procedure for a specific surface or feature |
| [Reference index](https://docs.github.com/en/copilot/reference) | Check syntax, support matrices, and configuration keys |
| [Tutorials and cookbook](https://docs.github.com/en/copilot/tutorials) | Find small exercises for explaining, testing, refactoring, documenting, and planning |
| [Responsible use](https://docs.github.com/en/copilot/responsible-use) | Explain limitations, verification, and human accountability |
| [Feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) | Orient on client support; verify the target version rather than assuming parity |

## Day 1: See the Possibilities

Use one synthetic application across these demonstrations. Prepare slow results beforehand.
Attendees are not expected to configure every feature during the opening tour.

| Capability | Concrete demonstration | Practice and official reference |
|---|---|---|
| Surfaces and execution | Identify GitHub Chat, VS Code, CLI, the Copilot app, and Mobile; distinguish local, worktree, and cloud execution | Tour; [features](https://docs.github.com/en/copilot/get-started/features), [agents and environments](https://code.visualstudio.com/docs/agents/overview) |
| Codespaces and devcontainers | Open the running app, then show runtime versions, dependencies, shared extensions/settings, and forwarded port | Lab 00; [Codespaces](https://docs.github.com/en/codespaces/overview), [devcontainers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers) |
| Inline suggestions and next-edit suggestions | Accept part of a suggestion; edit one symbol and inspect a proposed follow-up | Demo/optional Lab 01; [inline suggestions](https://code.visualstudio.com/docs/editing/ai-powered-suggestions) |
| Inline chat and smart actions | Explain or refactor a selection; show Generate Tests and Fix actions | Demo/Lab 01; [inline chat](https://code.visualstudio.com/docs/chat/inline-chat), [smart actions](https://code.visualstudio.com/docs/editing/copilot-smart-actions) |
| Ask, Plan, Agent, and focused edits | Understand a file, agree a plan, implement a small change; identify Edit mode if the client provides it | Lab 01; [chat](https://code.visualstudio.com/docs/chat/chat-overview), [planning](https://code.visualstudio.com/docs/agents/run/planning) |
| Prompting and context | Give an outcome, constraints, relevant files, and a check; attach a selection, error, screenshot, or documentation | Lab 01; [best practices](https://docs.github.com/en/copilot/get-started/best-practices), [context and indexing](https://code.visualstudio.com/docs/agents/concepts/context) |
| Models and usage | Show Auto/model picker, available reasoning settings, and usage; distinguish a model from a specialist agent | Demo/Lab 02; [models](https://code.visualstudio.com/docs/agents/concepts/language-models), [supported models](https://docs.github.com/en/copilot/reference/ai-models/supported-models) |
| Browser feedback | Open the app, inspect it, interact, capture a screenshot, fix, and verify | Demo/optional Lab 04; [built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools) |
| Browser sharing and vision | Contrast an agent-opened isolated page with Share with Agent on a page you opened; add element comments or a screenshot | Demo; [browser sharing and feedback](https://code.visualstudio.com/docs/agents/run/browser-tools) |
| Tests and debugging | Generate a focused test, inspect a failure, fix the cause, and rerun; point out debugger support | Lab 01; [testing with AI](https://code.visualstudio.com/docs/agents/guides/test-with-copilot), [smart actions](https://code.visualstudio.com/docs/editing/copilot-smart-actions) |
| Recovery and sessions | Stop/steer, inspect a diff, restore a checkpoint, resume, and start a fresh conversation | Demo/Labs 01-02; [review and restore](https://code.visualstudio.com/docs/agents/run/review-code-edits), [sessions](https://code.visualstudio.com/docs/agents/concepts/sessions) |
| Reusable customization | Open the Customizations editor and identify instructions, prompts, agents, skills, MCP, hooks, and plugins | Tour then Labs 01/06/07; [customization editor](https://code.visualstudio.com/docs/agent-customization/overview), [comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) |
| Copilot CLI | Interactive plan, bounded tool request, `copilot -p`, context/session controls, then `/delegate` | Lab 02; [CLI overview](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli), [command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) |
| Managed plugin at hand | Invoke a prepared agent/skill and inspect where it came from; show the configured marketplace and effective settings | Tour, deeper Day 5; [plugins](https://docs.github.com/en/copilot/concepts/agents/about-plugins), [managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings) |
| GitHub collaboration | Branch, commit, PR, checks, review, and merge; inspect an AI-generated summary against the diff | Lab 08, deeper Day 3; [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow), [PR summaries](https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/create-a-pr-summary) |
| Cloud agent and code review | Open a prepared issue, session, PR, and review comment; explain what the human verifies | Tour, Labs 03/07 and Day 4; [cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent), [code review](https://docs.github.com/en/copilot/concepts/agents/code-review) |
| Automations and hooks | Show a completed event-triggered run and its generated report; distinguish the trigger from a lifecycle hook | Tour, Lab 07; [automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations), [hooks](https://docs.github.com/en/copilot/reference/hooks-reference) |
| Shared context and non-code work | Ask a prepared Space a factual question; summarize a synthetic report or create a comparison table/diagram | Tour/optional Lab 04; [Spaces](https://docs.github.com/en/copilot/concepts/context/spaces), [cookbook](https://docs.github.com/en/copilot/tutorials/copilot-cookbook) |
| Deployment | Read a workflow's tests, image build, deployment, and public URL | Lab 08, deeper Day 4; [Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart), [Container Apps](https://learn.microsoft.com/azure/container-apps/github-actions) |

Browser automation uses Copilot's **built-in browser tools**, not a separately installed browser
server. Confirm availability in the presenter client. A shared tab can expose its signed-in state;
share only the intended training page, then revoke access. A screenshot is not a repeatable CI test.
Checkpoints restore supported workspace changes; they do not reverse external writes or replace Git.

## Customization: Which File Does What?

| Mechanism | Purpose and scope | Official reference |
|---|---|---|
| Repository instructions and `AGENTS.md` | Persistent project guidance; support and precedence vary by client | [Instruction support](https://docs.github.com/en/copilot/reference/custom-instructions-support) |
| `.github/instructions/*.instructions.md` | Guidance selected by path or applicable context; not an authorization rule | [Instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) |
| `.github/prompts/*.prompt.md` | A deliberately invoked, reusable task with inputs | [Prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files) |
| `.github/agents/*.agent.md` | A role with instructions and a selected tool set | [Custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents), [configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration) |
| `.github/skills/<name>/SKILL.md` | On-demand workflow guidance with optional scripts and resources | [Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| `.github/hooks/*.json` | Code at specific lifecycle events; test failure behavior and input/output formats | [Hook reference](https://docs.github.com/en/copilot/reference/hooks-reference) |
| Workspace/repository MCP configuration | External tools and data, configured separately for each execution surface | [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp), [VS Code configuration](https://code.visualstudio.com/docs/agent-customization/mcp-servers) |
| Plugin and marketplace manifests | Package and distribute supported customizations; installation and tool permissions both matter | [Plugins](https://docs.github.com/en/copilot/concepts/agents/about-plugins), [CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) |
| Enterprise managed settings | Administrator-controlled defaults and restrictions, including approved plugin distribution | [Managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings) |

An agent file is not a separately trained model. A skill does not grant tool access. A plugin
packages capabilities but is not the process running them. An installed repository agent alone
does not prove enterprise distribution. Prompt-file and handoff support is not identical everywhere.

## Days 2-5: Go Deeper

| Session | What we do | Official reference |
|---|---|---|
| Day 2 / Lab 05 | Compare Power Platform connectors and a code app using the same Dataverse rows | [Power Automate and Dataverse](https://learn.microsoft.com/power-automate/dataverse/overview), [Web API operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api) |
| Day 2 / Lab 05 | Read/filter rows, create a fictional row, verify persistence, handle failures | [Query data](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query/overview), [create a row](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/create-entity-web-api) |
| Day 3 / Lab 03 | Specify an issue, follow the cloud session, review its PR, iterate on the correct branch | [Start tasks](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task), [review output](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output) |
| Day 3 / Lab 04 | Add remote GitHub MCP, limit toolsets, and verify an answer against its source | [GitHub MCP setup](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server), [toolsets](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/configure-toolsets) |
| Day 4 / Lab 07 | Configure an event trigger, run a bounded task, inspect its output, then disable the test automation | [Create automations](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations) |
| Day 4 / Lab 07 | Create metadata-only hook logging and test a harmless exact-tool denial | [Hook reference](https://docs.github.com/en/copilot/reference/hooks-reference) |
| Day 4 / review | Review generated code, investigate checks, distinguish suggestions from approvals | [Code review](https://docs.github.com/en/copilot/concepts/agents/code-review), [AI-generated code review](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code) |
| Day 4 / deployment | Explain CI, image builds, environment configuration, and service authentication | [Actions](https://docs.github.com/en/actions/writing-workflows/quickstart), [Container Apps deployment](https://learn.microsoft.com/azure/container-apps/github-actions) |
| Day 5 / Lab 06 | Author a role and skill, test present/missing facts, and hand off unchanged evaluator JSON | [Customizations](https://code.visualstudio.com/docs/agent-customization/overview), [skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [sessions and handoff](https://code.visualstudio.com/docs/agents/concepts/sessions) |
| Day 5 / distribution | Inspect org-agent source, plugin contents, marketplace, and effective enterprise settings | [Plugin standards](https://docs.github.com/en/copilot/concepts/agents/about-enterprise-plugin-standards), [managed settings reference](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings) |
| Day 5 / evaluations | Compare quotations and expected outcomes, test counterexamples, and distinguish product usage from correctness | [Evaluate customizations](https://code.visualstudio.com/docs/agent-customization/overview), [measure Copilot impact](https://docs.github.com/en/copilot/tutorials/roll-out-at-scale/measure-copilot-impact) |

The training evaluator is deterministic code, not a general document-understanding engine.
Keep its calculated output unchanged during agent handoffs; challenge suspected defects with
tests and human review. Official product links are reference material, not evidence from a vendor report.

## Optional Possibilities and Specialist Topics

These are included in the capabilities tour or available for Q&A. They are not extra mandatory labs.
Use prepared examples where setup, cost, data access, or preview support would delay the group.

| Topic | Place in the workshop | Official reference |
|---|---|---|
| Parallel work, subagents, worktrees, Agent Host | Day 1 tour; Day 5 demo/optional independent checks | [Sessions](https://code.visualstudio.com/docs/agents/concepts/sessions), [agent harnesses](https://code.visualstudio.com/docs/agents/concepts/agent-harnesses) |
| Agent Merge and newer session controls | Optional Day 5 preview; do not equate merge-ready with auto-merged | [VS Code release notes](https://code.visualstudio.com/updates) |
| Third-party coding agents | Optional Day 5 comparison, subject to policy and availability | [Third-party agents](https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents) |
| CLI research, fleet, scheduling, session history and remote control | Lab 02 extras or a prepared tour; remove test schedules | [CLI commands](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) |
| Copilot Memory and Spaces | Day 1 context tour; keep memory distinct from deliberately curated shared sources | [Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory), [Spaces](https://docs.github.com/en/copilot/concepts/context/spaces) |
| Copilot app, Mobile, Teams, Slack, Jira, Linear, Azure Boards | Day 1 surface tour; live integration only after separate setup | [Features](https://docs.github.com/en/copilot/get-started/features), [integrations](https://docs.github.com/en/copilot/how-tos/copilot-integrations) |
| Agentic Workflows versus UI automations | Optional Day 4 comparison of versioned automation and separately managed configuration | [Agentic Workflows](https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows) |
| Copilot SDK, custom tools, CLI extensions, ACP and LSP | Reference/optional pro-coder follow-up; building with Copilot differs from embedding an agent in an app | [SDK](https://docs.github.com/en/copilot/how-tos/copilot-sdk), [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference) |
| BYOK and local models | Reference/optional demonstration with separately approved configuration; not a policy workaround | [Language models](https://code.visualstudio.com/docs/agents/concepts/language-models) |
| Dictation and accessibility | Optional short demo; verify processing location and client settings | [VS Code release notes](https://code.visualstudio.com/updates), [accessibility](https://code.visualstudio.com/docs/configure/accessibility/accessibility) |
| Other IDEs, Java/.NET upgrades, migration and refactoring | Reference when relevant to attendees' own projects | [Feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix), [tutorials](https://docs.github.com/en/copilot/tutorials) |
| Code referencing and security tooling | Brief responsible-use orientation; security products may need separate entitlement | [Code referencing](https://docs.github.com/en/copilot/concepts/completions/code-referencing), [responsible use](https://docs.github.com/en/copilot/responsible-use) |
| Seats, policies, budgets, models, MCP governance, audit and telemetry | Presenter overview; administrator preparation, not attendee configuration work | [Administration](https://docs.github.com/en/copilot/how-tos/administer-copilot), [policy coverage](https://docs.github.com/en/copilot/reference/supported-surfaces-for-policies), [metrics](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics) |
| Sandboxes, permissions and exclusions | Explain the distinction; never describe prompt guidance as an OS boundary | [Sandboxes](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes), [trust and safety](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety) |
| Troubleshooting and customization diagnostics | Show how to inspect tools, discovery and errors using synthetic context | [Copilot troubleshooting](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-common-issues), [customization editor](https://code.visualstudio.com/docs/agent-customization/overview) |

## Small Tasks for Early Finishers

Pick one, spend **5-10 minutes**, then stop when the group moves on. No production data, paid
resource creation, new permissions, or unattended schedules. These do not extend the core timetable.

| Day | Small task | Observable result | Official help |
|---|---|---|---|
| 1 | Explain one unfamiliar function, then use inline chat to improve its name or readability | Inspect the diff and run its existing test | [Inline chat](https://code.visualstudio.com/docs/chat/inline-chat) |
| 1 | Generate a commit/PR summary for your own change | Correct any claim not supported by the diff | [Smart actions](https://code.visualstudio.com/docs/editing/copilot-smart-actions) |
| 2 | Add a visible assessed/unassessed row count | Counts match the displayed synthetic rows | [Query data](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query/overview) |
| 2 | Ask for a diagram of the app-to-Dataverse flow | Explain where credentials and filters belong | [Cookbook](https://docs.github.com/en/copilot/tutorials/copilot-cookbook) |
| 3 | Compare one read-only GitHub MCP answer with the issue page | Same issue number and acceptance criteria | [GitHub MCP](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server) |
| 3 | Query the facilitator's prepared Space | Identify which allowed sources support the answer | [Spaces](https://docs.github.com/en/copilot/concepts/context/spaces) |
| 4 | Count pre-tool and post-tool events in the training log | Explain why an attempted call is not a successful result | [Hook reference](https://docs.github.com/en/copilot/reference/hooks-reference) |
| 4 | Read a completed workflow run | Find its commit, tests, artifact build, and result | [Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) |
| 5 | Try the custom agent with missing evidence | It asks for input or reports uncertainty without inventing facts | [Custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents) |
| 5 | Inspect a prepared plugin's component list | Distinguish packaged instructions from enabled tools | [Plugins](https://docs.github.com/en/copilot/concepts/agents/about-plugins) |

## Recheck Before Delivery

- [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/) and [VS Code releases](https://code.visualstudio.com/updates): note releases, removals, and preview changes. A missing filter result is not proof of no releases.
- [Supported models](https://docs.github.com/en/copilot/reference/ai-models/supported-models): demonstrate the current picker rather than pinning a model name in the lesson.
- [Feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix) and [policy coverage](https://docs.github.com/en/copilot/reference/supported-surfaces-for-policies): desktop, Codespaces, CLI, and cloud sessions need separate checks.
- [Troubleshooting](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-common-issues): verify sign-in, discovery, permissions, and network access without revealing secrets.
- [Responsible use](https://docs.github.com/en/copilot/responsible-use): model output, code review suggestions, and usage metrics are not proof of correctness. Keep demonstrations synthetic and inspect actual results.