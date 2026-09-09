# Facilitator runbook

Use the [agenda](AGENDA.md) for timing and the [coverage guide](REFERENCES.md) for official
links to every feature family. Day 1 establishes breadth, including prepared examples of later
workflows; Days 2-5 provide depth. Keep the reference guide open for attendee questions.

## Demonstration preparation

Prepare these results before Day 1 so network waits and preview setup do not consume lab time:

| Block | Live core | Prepared result or fallback |
|---|---|---|
| Opening tour | Working app, Codespaces/devcontainer, GitHub Chat, and one synthetic summary or diagram | A curated Space with only synthetic sources; an issue, cloud-agent session, reviewed PR, and completed automation |
| VS Code tour | Inline/next-edit suggestions, inline chat or smart actions, Ask/Plan/Agent, context, model/Auto picker, test and diff | A small page change for built-in browser inspection; checkpoint/recovery example; Customizations editor |
| CLI tour | Interactive plan, bounded programmatic task, permission request, context/usage, stop/resume | Delegated task and installed plugin with a verified agent/skill invocation; no policy change or installation wait |
| Deployment lab handover | Branch, commit, PR/checks, workflow trigger, and where to find the resulting URL | A completed deployment run; review the actual diff before accepting a generated summary |

Use one synthetic app as the thread. Name the model, agent role, tools, context, and execution
environment as different choices. GitHub Copilot is the focus; Microsoft 365 Copilot and
Power Platform are related products, not interchangeable entitlements or tool surfaces.

Show how to stop or steer work as well as how to start it. Agent edits can be applied directly:
inspect the actual diff and restoration controls rather than promising a universal approval
dialog. Checkpoints are temporary workspace recovery, not Git history or an undo for external writes.

The [specialist topics](REFERENCES.md#optional-possibilities-and-specialist-topics) are a
reference shelf: SDK, other IDEs, migrations, BYOK, integrations, parallel execution, and
administration do not add prerequisites to Monday. Use the
[daily small tasks](REFERENCES.md#small-tasks-for-early-finishers) for early finishers.

## Organization setup

1. Confirm all items in [PREREQS.md](PREREQS.md).
2. Verify Copilot cloud-agent, automation, Codespaces, and remote GitHub MCP availability in the event organization.
3. Grant the required repository access. Test branch rules and use only the bypass permissions the cloud workflow actually requires.
4. Provision the shared Azure resources once: resource group, Container Apps environment, and container registry. See [PREREQS.md](PREREQS.md) for the provisioned names.
5. Configure Actions and Codespaces service access separately as listed in [PREREQS.md](PREREQS.md).
   `scripts/create_attendee_repos.py` creates repositories and team grants, not credentials.

## Governance repository

One repository, `agentic-dev-labs/.github-private`, does three jobs from three paths:

| Path | Job | Reaches |
|---|---|---|
| `agents/` | Organization-level custom agents | Eligible users in supported clients after the organization source is configured |
| `copilot/managed-settings.json` | Enterprise managed settings | Licensed users covered by the configured enterprise policy |
| `.github/plugin/marketplace.json` and `plugins/` | Plugin marketplace | Users whose clients can read the marketplace and plugin files |

Custom agents and plugins have different scope ladders. Agents have an organization level;
plugins do not use that same directory-based discovery mechanism.

- Organization agents must sit in a **root `agents/` directory**, not `.github/agents/`,
  which is the single-repository location. Members can use them without access to the
   repository under the supported organization-agent sharing model. Verify discovery in the actual client.
- Repository-level agents stay in `.github/agents` and apply only to that repository.
- Plugins have no organization scope. Distribute them per repository through
  `.github/copilot/settings.json`, or enterprise-wide through `managed-settings.json`.

Consult [custom-agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration),
[plugins](https://docs.github.com/en/copilot/concepts/agents/about-plugins), and
[enterprise-managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).
Supported components and policy keys vary by client; a marketplace does not itself grant access to private files.

## Plugin distribution

Check access and client behavior before relying on distribution. Do not alter global policies
mid-demonstration or assume repository agents and plugins are the same thing.

1. **Grant every attendee read access to the governance repository.** When `enabledPlugins`
   installs a plugin, the client fetches plugin files as the signed-in user. The repository
   is private, so users need access to fetch it. Inspect plugin diagnostics if it does not load.
2. Select the organization as the enterprise source of governance so
   `copilot/managed-settings.json` takes effect. Check the effective settings in the client;
   refresh or restart as its documentation requires rather than assuming immediate propagation.
3. Verify discovery and an actual invocation in the presenter client before delivery. When a manual
   rehearsal install is needed, use `copilot plugin marketplace add agentic-dev-labs/.github-private`,
   then `copilot plugin install vendor-assurance@agentic-dev-labs`. Do not present a manual install
   as proof that enterprise auto-install worked; inspect the effective settings and origin separately.
4. Optionally add `.github/copilot/settings.json` to this template so repositories generated
   from it enable the plugin without any enterprise change.
5. Never point the template at a marketplace repository that does not resolve; it fails for
   every team at once.
6. Leave `strictKnownMarketplaces` alone. It is enterprise-wide with no organization scope,
   and restricting it blocks plugins installed from every other marketplace.

For the presenter demo, use `copilot plugin install assurance-toolkit@agentic-dev-labs`
after confirming it appears in the marketplace. Inspect its agent, skills, and document-conversion
MCP configuration. Use a synthetic document and verify a quotation; do not promise that every
PDF failed before installation or that every converted file has reliable page provenance.
The toolkit is an optional presenter install, separate from the core labs. Verify its actual
tool permissions, runtime dependencies, and client support in the governance repository.
Introduce an already-installed capability on Day 1; inspect packaging and distribution in depth
on Day 5. Keep a verified transcript/result available if discovery is unavailable in the live client.

## Create team repositories

Repository secrets are **not** copied from a template. The script creates private repositories
and grants the configured attendee team write access:

```shell
python scripts/create_attendee_repos.py nn-na-2026-10-team-01 nn-na-2026-10-team-02
```

Re-running reuses existing repositories and reapplies the team grant. It does not create
identities, issue credentials, buy seats, or configure secret access. Template changes also do
not automatically update team repositories that already exist.

1. Confirm this repository is flagged as a template.
2. Run the script with the repository names you need.
3. Verify the team grant and assign one unique workshop label/app name per deployed repository.
4. Apply and test review rules. Configure Actions secret access and Day 2 Codespaces secrets separately.
5. Run CI once and create a Codespace in each repository.

## Dry run

Use the [full Codespaces rehearsal package](../rehearsal/README.md) and `/rehearse-workshop`
to execute the labs in a dedicated copy. It records live evidence separately from test results,
checks a fresh package install, and verifies the exact deployed commit. No attendee Azure login
is required; repository access to the prepared Actions identity must already exist.

- Create a Codespace from a test team repository on the corporate network.
- Confirm extensions install and `uv sync --locked --extra dev --extra web` succeeds.
- Inspect the devcontainer: Python version, dependency lock, minimum host requirements, shared editor settings, and forwarded port. Extension IDs are not version pins; CLI authentication is separate.
- Run tests and the sample CLI end to end.
- Use `--as-of 2026-10-26` to confirm sample scores 10, 8, and 2, plus exact source quotations.
- Rehearse inline assistance, context attachments, model/usage controls, and checkpoint recovery on a disposable change.
- Check the synthetic Space's sources and permissions; do not attach the whole repository or facilitator notes.
- Assign a test issue to Copilot and verify one reviewed result within the lab time-box. Check current limits instead of relying on a historical session cap.
- Create an automation triggered by issue creation, open a matching issue, and confirm exactly one session starts.
- Follow Lab 07's metadata-only hook example and harmless deny test. Local log files are not a durable compliance trail.
- Test remote GitHub MCP in read-only mode.
- Test Copilot built-in browser tools in the presenter client against a forwarded or deployed URL. If absent in an attendee client, use the presenter demo or manual page inspection; do not add another browser server.
- Exercise the Dataverse-backed training API using synthetic records.
- Set a name in `config.json`, dispatch **Deploy my app**, and confirm the app answers on its public URL.
- Run the Day 2 opt-in connection and confirm **Source: Dataverse**, not fallback samples.
- Follow Lab 01's JSON-generation step and Lab 06's separate baseline/report comparison with a fresh session.
- Verify the prepared plugin's agent/skill actually runs with its intended tools, not just that its manifest is listed.
- Disable test automations and stop unused Codespaces at the end of the rehearsal.

Unit tests, lint, JSON/YAML parsing, and a valid lockfile are offline checks, not evidence that
these live steps have passed. Record rehearsal results before promising end-to-end readiness.

**Regression coverage added for rehearsal:** the reproduced encryption-negation, planned-retention,
residency-contradiction, and unstated-SOC-2 cases are fixed and tested. Authenticated Dataverse and
token requests now reject redirects. This remains a small keyword-based teaching evaluator;
those counterexamples and the three sample scores do not establish general document correctness.
The live Codespaces, product-feature, Dataverse, and deployment gates must still be observed.

## Common failure modes

| Symptom | Check | Resolution |
|---|---|---|
| Codespace creation fails | Network and Codespaces policy | Allow required GitHub endpoints and enable Codespaces. |
| Copilot icon or agent missing | Seat and organization policy | Assign the seat, enable the feature, then reload the Codespace. |
| `copilot` command not found | Container setup step failed | The container installs it from `https://gh.io/copilot-install`. Re-run that command in the terminal, or use `npm install -g @github/copilot`, which needs Node 22 or later. |
| Organization agent missing from the list | Discovery setting | `github.copilot.chat.organizationCustomAgents.enabled` must be true; the devcontainer sets it. |
| Inline suggestion or model option missing | Client, language, seat, model and settings | Use a prepared example and the current support documentation; do not turn a missing preview into an installation task. |
| Browser tools missing | Presenter client and effective browser policy | Use the prepared demo or inspect the page manually; do not install another browser server. |
| Plugin listed but its task fails | Component discovery, tool access and runtime | Inspect the actual invoked component and tool error; manifest presence alone is not a successful test. |
| Cloud task cannot start | Access level or agent policy | Grant write access and enable the cloud agent at organization level. |
| Automations pane missing | Repository visibility or organization policy | Automations require a private or internal repository and an organization that allows them. |
| Hook appears to hang the agent | Hook runtime | Hooks block execution; keep them under five seconds and set `timeoutSec`. |
| Agent cannot update protected branch | Target branch and ruleset | Verify that the task uses its permitted branch. Have the owner approve only the documented exception needed; do not weaken protection during the session. |
| Dependency setup fails | Registry firewall path | Allowlist the approved registry endpoints and rebuild the container. |
| MCP authentication fails | Remote URL and browser auth | Use the documented remote URL and confirm the login flow is allowed. |
| Azure login fails | Actions secret and deployment identity | This workflow uses `AZURE_CREDENTIALS`, not OIDC. Verify its access and validity without printing its value. |
| App deploys but does not start | Container port or start command | The container listens on 8000; confirm `--target-port 8000` and check revision logs. |
| Deployment rejected on the name | `config.json` still says `Your Name`, or the derived name is invalid | Container App names are lowercase, alphanumeric with hyphens, and 32 characters at most. |

Do not disable certificate verification to work around corporate package restrictions. The
lockfile uses public PyPI URLs; a locally approved mirror belongs in local tooling configuration,
not the committed workshop lock. Check installation from the target Codespace network.

Never request attendee Azure access as a workaround. Escalate service configuration to the
event infrastructure owner. Do not change workshop clock times or invite participants during a code rehearsal.

## Official References

- [Coverage and reference guide](REFERENCES.md): all demonstrations, lab topics, and optional follow-ups.
- [Copilot administration](https://docs.github.com/en/copilot/how-tos/administer-copilot), [policy support](https://docs.github.com/en/copilot/reference/supported-surfaces-for-policies), and [managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings).
- [Codespaces overview](https://docs.github.com/en/codespaces/overview), [Copilot troubleshooting](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-common-issues), and [built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools).
- [Dataverse operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api), [Power Automate integration](https://learn.microsoft.com/power-automate/dataverse/overview), and [Container Apps deployment](https://learn.microsoft.com/azure/container-apps/github-actions).
- [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/) and [VS Code releases](https://code.visualstudio.com/updates): recheck before the event, especially preview demos.
