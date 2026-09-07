# Facilitator runbook

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

## Plugin distribution

Check access and client behavior before relying on distribution. Do not alter global policies
mid-demonstration or assume repository agents and plugins are the same thing.

1. **Grant every attendee read access to the governance repository.** When `enabledPlugins`
   installs a plugin, the client fetches plugin files as the signed-in user. The repository
   is private, so users need access to fetch it. Inspect plugin diagnostics if it does not load.
2. Select the organization as the enterprise source of governance so
   `copilot/managed-settings.json` takes effect. Check the effective settings in the client;
   refresh or restart as its documentation requires rather than assuming immediate propagation.
3. Verify from the CLI before relying on it: `copilot plugin marketplace add agentic-dev-labs/.github-private`, then `copilot plugin install vendor-assurance@agentic-dev-labs`.
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

- Create a Codespace from a test team repository on the corporate network.
- Confirm extensions install and `uv sync --locked --extra dev --extra web` succeeds.
- Inspect the devcontainer: Python version, dependency lock, minimum host requirements, shared editor settings, and forwarded port. Extension IDs are not version pins; CLI authentication is separate.
- Run tests and the sample CLI end to end.
- Use `--as-of 2026-10-26` to confirm sample scores 10, 8, and 2, plus exact source quotations.
- Assign a test issue to Copilot and verify one draft pull request appears before the 59-minute cap.
- Create an automation triggered by issue creation, open a matching issue, and confirm exactly one session starts.
- Follow Lab 07's metadata-only hook example and harmless deny test. Local log files are not a durable compliance trail.
- Test remote GitHub MCP in read-only mode.
- Test Copilot built-in browser tools in the presenter client against a forwarded or deployed URL. If absent in an attendee client, use the presenter demo or manual page inspection; do not add another browser server.
- Exercise the Dataverse-backed training API using synthetic records.
- Set a name in `config.json`, dispatch **Deploy my app**, and confirm the app answers on its public URL.
- Run the Day 2 opt-in connection and confirm **Source: Dataverse**, not fallback samples.
- Disable test automations and stop unused Codespaces at the end of the rehearsal.

Unit tests, lint, JSON/YAML parsing, and a valid lockfile are offline checks, not evidence that
these live steps have passed. Record rehearsal results before promising end-to-end readiness.

## Common failure modes

| Symptom | Check | Resolution |
|---|---|---|
| Codespace creation fails | Network and Codespaces policy | Allow required GitHub endpoints and enable Codespaces. |
| Copilot icon or agent missing | Seat and organization policy | Assign the seat, enable the feature, then reload the Codespace. |
| `copilot` command not found | Container setup step failed | The container installs it from `https://gh.io/copilot-install`. Re-run that command in the terminal, or use `npm install -g @github/copilot`, which needs Node 22 or later. |
| Organization agent missing from the list | Discovery setting | `github.copilot.chat.organizationCustomAgents.enabled` must be true; the devcontainer sets it. |
| Cloud task cannot start | Access level or agent policy | Grant write access and enable the cloud agent at organization level. |
| Automations pane missing | Repository visibility or organization policy | Automations require a private or internal repository and an organization that allows them. |
| Hook appears to hang the agent | Hook runtime | Hooks block execution; keep them under five seconds and set `timeoutSec`. |
| Agent cannot update protected branch | Ruleset bypass list | Add Copilot as a bypass actor; do not weaken protection globally. |
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
