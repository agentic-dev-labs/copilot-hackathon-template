# Advanced Copilot Reference

**Not part of the workshop.** On 14 October 2026 the owner simplified Days 3-5 for people who had
never used GitHub or code before. Wednesday now introduces a few tools on each attendee's own
website, Thursday is a build day, and Friday is a round of presentations. See the
[current agenda](../../AGENDA.md).

The deeper technical material below was removed from the schedule but kept so it is not lost.
Use it later with a technical owner, for a separate pro-coder session, or for self-study. It is
not homework, not an attendee prerequisite, and not authorization to change policy or connect
real data. Clock times, days, and lab numbers inside each page are historical.

| Page | What it covers |
| --- | --- |
| [CLI and prepared browser tools](cli-and-browser-tools.md) | The earlier technical-track CLI and Playwright introduction |
| [Cloud agent on the vendor app](cloud-agent-vendor-task.md) | Issue-to-PR work with tests on the synthetic vendor reader |
| [Remote GitHub MCP configuration](remote-github-mcp.md) | Toolsets, read-only mode, policy, and Spaces |
| [Automations, hooks, and release readiness](automations-hooks-readiness.md) | Event-triggered automations, audit/deny hooks, saved browser checks, CI, and verified deployment |
| [Agent authoring and evidence handoffs](agent-authoring-handoffs.md) | Custom agents, a source-evidence skill, and analyst/writer/reviewer handoffs |
| [The synthetic vendor reader](vendor-reader.md) | Running the vendor app, its three sample reports, publishing it, and its training scope |

The supporting code stays maintained and tested in its existing paths: the vendor reader under
`src/vendor_assurance/` and `app/`, the hook helper `scripts/audit_hook.py`, the agents in
`.github/agents/`, and the deployment workflow. The three vendor roles in `.github/agents/` carry
`user-invocable: false`, so beginners do not see them in the Chat agent picker. To pick them by
hand for the agent-handoff page, set it to `true` in your own copy. Its issue form is listed as
**Advanced: vendor app task (post-workshop)**. Business data remains synthetic. Scores still come
from the Python evaluator, never from a model's opinion.

Live Dataverse setup has its own [post-workshop reference](../dataverse/README.md).

## Official References

- [Customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).
- [About the cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent).
- [Hook reference](https://docs.github.com/en/copilot/reference/hooks-reference).
- [Whole-week topic map](../../REFERENCES.md).
