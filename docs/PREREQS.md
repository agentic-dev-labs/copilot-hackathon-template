# Customer access checklist

Complete and dry-run these items before Monday 26 October 2026.

- [ ] Collect attendee GitHub usernames: `[Confirm with facilitator]`.
- [ ] Confirm those accounts may join an external GitHub organization.
- [ ] Assign a GitHub Copilot seat to every attendee.
- [ ] Grant every attendee **write** access to the team repository; write access is required to trigger the cloud agent.
- [ ] Enable the Copilot cloud agent at organization level; it is off by default for Business and Enterprise organizations.
- [ ] Keep every team repository **private or internal**; Copilot automations are unavailable in public repositories.
- [ ] Confirm the organization allows Copilot automations as well as the cloud agent.
- [ ] Confirm the remote GitHub MCP server is permitted by any enterprise MCP allowlist.
- [ ] Add Copilot as a bypass actor for applicable branch protection or rulesets.
- [ ] Allowlist required corporate/internal package registries through the firewall.
- [ ] Confirm `github.com` is reachable from the corporate network.
- [ ] Confirm GitHub Codespaces is reachable and can create a container from the template.
- [ ] Confirm browser authentication flows for GitHub CLI and remote MCP are allowed.
- [ ] Assign ten team names and memberships: `[Confirm with facilitator]`.
- [ ] Provide organization-level Azure OIDC configuration and App Service names without exposing values in repositories.
