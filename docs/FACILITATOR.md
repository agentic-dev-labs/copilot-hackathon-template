# Facilitator runbook

## Organization setup

1. Confirm all items in [PREREQS.md](PREREQS.md).
2. Enable Copilot policies, Copilot coding agent, Codespaces, and required MCP access for the event organization.
3. Grant attendees write access and add Copilot as a bypass actor on applicable rulesets.
4. Configure organization-level Actions values for Azure OIDC: `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`, and team-specific `AZURE_APP_SERVICE_NAME`.
5. Pre-provision Azure App Services and federated identity credentials. Attendees must not need an Azure portal login or guest account.

## Create team repositories

1. Mark this private repository as a template after the owner pushes it.
2. Create ten private repositories from the template on the default branch.
3. Replace `<TEAM_NAME>` only where a team identifier is required.
4. Add the corresponding team with write access.
5. Apply branch rules and confirm the Copilot bypass actor.
6. Run CI once and create a Codespace in each repository.

## Dry run

- Create a Codespace from a test team repository on the corporate network.
- Confirm extensions install and `uv sync --extra dev` succeeds.
- Run tests and the sample CLI end to end.
- Confirm the synthetic report produces multiple chunks and a completed privacy review.
- Assign a test issue to Copilot and verify one draft pull request appears before the 59-minute cap.
- Test remote GitHub MCP in read-only mode.
- Exercise the Dataverse-backed training API using synthetic records.
- Dispatch deployment and confirm GitHub OIDC reaches the pre-provisioned App Service.

## Common failure modes

| Symptom | Check | Resolution |
|---|---|---|
| Codespace creation fails | Network and Codespaces policy | Allow required GitHub endpoints and enable Codespaces. |
| Copilot icon or agent missing | Seat and organization policy | Assign the seat, enable the feature, then reload the Codespace. |
| Cloud task cannot start | Access level or agent policy | Grant write access and enable the cloud agent at organization level. |
| Agent cannot update protected branch | Ruleset bypass list | Add Copilot as a bypass actor; do not weaken protection globally. |
| Dependency setup fails | Registry firewall path | Allowlist the approved registry endpoints and rebuild the container. |
| MCP authentication fails | Remote URL and browser auth | Use the documented remote URL and confirm the login flow is allowed. |
| Azure login fails | OIDC subject and Actions configuration | Compare the federated subject with repository/environment scope and confirm organization values. |
| App deploys but does not start | App Service runtime/start command | Inspect deployment logs and align the Python runtime with the package. |

Never request attendee Azure access as a workaround. Escalate pre-provisioning or OIDC configuration to the event infrastructure owner.
