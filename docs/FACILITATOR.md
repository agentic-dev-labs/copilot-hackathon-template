# Facilitator runbook

## Organization setup

1. Confirm all items in [PREREQS.md](PREREQS.md).
2. Enable Copilot policies, Copilot coding agent, Codespaces, and required MCP access for the event organization.
3. Grant attendees write access and add Copilot as a bypass actor on applicable rulesets.
4. Provision the shared Azure resources once: resource group, Container Apps environment, and container registry. See [PREREQS.md](PREREQS.md) for the provisioned names.
5. Apply `AZURE_CREDENTIALS` to each attendee repository using `scripts/create_attendee_repos.py`. Attendees must not need an Azure portal login or guest account.

## Governance repository

One repository, `agentic-dev-labs/.github-private`, does three jobs from three paths:

| Path | Job | Reaches |
|---|---|---|
| `agents/` | Organization-level custom agents | Every repository in the organization |
| `copilot/managed-settings.json` | Enterprise managed settings | Everyone on the enterprise Copilot plan |
| `.github/plugin/marketplace.json` and `plugins/` | Plugin marketplace | Anyone who adds the marketplace |

Custom agents and plugins have different scope ladders. Agents have an organization level;
plugins do not.

- Organization agents must sit in a **root `agents/` directory**, not `.github/agents/`,
  which is the single-repository location. Members can use them without access to the
  repository.
- Repository-level agents stay in `.github/agents` and apply only to that repository.
- Plugins have no organization scope. Distribute them per repository through
  `.github/copilot/settings.json`, or enterprise-wide through `managed-settings.json`.

## Plugin distribution

Order matters, and one prerequisite fails silently.

1. **Grant every attendee read access to the governance repository.** When `enabledPlugins`
   installs a plugin, the client fetches plugin files as the signed-in user. The repository
   is private, so without read access the install fails with no error.
2. Select the organization as the enterprise source of governance so
   `copilot/managed-settings.json` takes effect. Changes apply within about an hour, or
   immediately after a client restart or new sign-in.
3. Verify from the CLI before relying on it: `copilot plugin marketplace add agentic-dev-labs/.github-private`, then `copilot plugin install vendor-assurance@agentic-dev-labs`.
4. Optionally add `.github/copilot/settings.json` to this template so repositories generated
   from it enable the plugin without any enterprise change.
5. Never point the template at a marketplace repository that does not resolve; it fails for
   every team at once.
6. Leave `strictKnownMarketplaces` alone. It is enterprise-wide with no organization scope,
   and restricting it blocks plugins installed from every other marketplace.

## Create team repositories

Repository secrets are **not** copied when a repository is created from a template, and
setting organization secrets requires the `admin:org` scope. `scripts/create_attendee_repos.py`
solves both by creating each repository and applying its secrets in the same pass:

```shell
python scripts/create_attendee_repos.py nn-na-2026-10-team-01 nn-na-2026-10-team-02
```

It creates one deployment credential and one Dataverse secret per run, applies them to every
repository named, and never prints either value. Re-running skips repositories that exist.

1. Confirm this repository is flagged as a template.
2. Run the script with the repository names you need.
3. Add the corresponding team with write access.
4. Apply branch rules and confirm the Copilot bypass actor.
5. Run CI once and create a Codespace in each repository.

## Dry run

- Create a Codespace from a test team repository on the corporate network.
- Confirm extensions install and `uv sync --extra dev --extra web` succeeds.
- Run tests and the sample CLI end to end.
- Confirm the synthetic report produces multiple chunks and a completed privacy review.
- Assign a test issue to Copilot and verify one draft pull request appears before the 59-minute cap.
- Create an automation triggered by issue creation, open a matching issue, and confirm exactly one session starts.
- Add `.github/hooks/audit.json`, run one agent task, and confirm the audit log records tool use.
- Test remote GitHub MCP in read-only mode.
- Exercise the Dataverse-backed training API using synthetic records.
- Set a name in `config.json`, dispatch **Deploy my app**, and confirm the app answers on its public URL.

## Common failure modes

| Symptom | Check | Resolution |
|---|---|---|
| Codespace creation fails | Network and Codespaces policy | Allow required GitHub endpoints and enable Codespaces. |
| Copilot icon or agent missing | Seat and organization policy | Assign the seat, enable the feature, then reload the Codespace. |
| Cloud task cannot start | Access level or agent policy | Grant write access and enable the cloud agent at organization level. |
| Automations pane missing | Repository visibility or organization policy | Automations require a private or internal repository and an organization that allows them. |
| Hook appears to hang the agent | Hook runtime | Hooks block execution; keep them under five seconds and set `timeoutSec`. |
| Agent cannot update protected branch | Ruleset bypass list | Add Copilot as a bypass actor; do not weaken protection globally. |
| Dependency setup fails | Registry firewall path | Allowlist the approved registry endpoints and rebuild the container. |
| MCP authentication fails | Remote URL and browser auth | Use the documented remote URL and confirm the login flow is allowed. |
| Azure login fails | OIDC subject and Actions configuration | Compare the federated subject with repository/environment scope and confirm organization values. |
| App deploys but does not start | Container port or start command | The container listens on 8000; confirm `--target-port 8000` and check revision logs. |
| Deployment rejected on the name | `config.json` still says `Your Name`, or the derived name is invalid | Container App names are lowercase, alphanumeric with hyphens, and 32 characters at most. |

Never request attendee Azure access as a workaround. Escalate pre-provisioning or OIDC configuration to the event infrastructure owner.
