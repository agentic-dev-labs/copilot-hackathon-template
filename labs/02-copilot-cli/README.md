# Lab 02: Complete the trip with a shared agent

**Objective:** Use your travel customizations from Copilot CLI, consume the enterprise-managed
AttractionsAgent, and finish the trip without recreating the shared specialist.

**Time-box:** 60 minutes

**Prerequisites:** Completed Lab 01, Copilot CLI sign-in, and the facilitator's prepared
`attractions@agentic-dev-labs` plugin. Plugin access and enterprise configuration are prework,
not attendee setup. The actual client still needs permitted research tools.

## Presenter Demonstration

After you have planned flights and a hotel, the presenter reveals **AttractionsAgent** from
the managed `attractions` plugin. Inspect its source, version, Managed entry, and tools; then
invoke it with the destination and exact travel dates. A same-named repository agent would
not prove central distribution. Do not create or copy one into your project.

The presenter also shows CLI context/model/usage, stop/resume, and a prepared cloud delegation.
MCP is a separate tools/data connection. This plugin uses the client's research tools and does
not install an MCP server or host your planner. Deeper cloud work is in Lab 03.

## Steps

### 1. Continue in the CLI (15 minutes)

Run `copilot` from the repository root. Select your `TravelPlannerAgent` using the actual
agent picker and inspect `/skills`, `/instructions`, `/model`, and `/context` where available.
Attach [the trip brief](../../travel/trip-brief.json) and your saved flight/hotel choices.
Shared files do not imply the CLI has the VS Code conversation or browser session.

Invoke one of your travel skills and verify its source-labelled result. Approve only the
task's required tools. Practise stopping a response and finding the same session again.
Try this bounded programmatic task after exiting the interactive session:

```shell
copilot -p "For a fictional trip with hotel check-in 2026-10-26 and check-out 2026-10-28, state the number of hotel nights and explain the date arithmetic. Do not use tools."
```

Expect two nights. This proves a real CLI turn, not live hotel availability. `--allow-all`
is not a prerequisite. Inspect the effective sandbox if localhost or web access fails;
never bypass an enforced policy or install an alternative browser server.

### 2. Use the centrally supplied specialist (20 minutes)

Find `AttractionsAgent` in the plugin's actual discovered agent list. Select it directly,
or let your planner delegate where supported. For delegation, explicitly enable the supported
agent tool and allow the discovered specialist identifier in your planner. Do not guess a
namespace or assume that a VS Code handoff button works identically in the CLI.

Supply the city/country, inclusive ISO dates, interests, selected travel times, activity budget,
and free-time windows. For the fixture trip, preserve Flight F1 and Hotel H1. You can use:

> Find things to do in London, United Kingdom, during 2026-10-26 through 2026-10-28.
> Interests: history, museums, walking. Keep the supplied flights and hotel unchanged.
> Do not schedule anything before arrival or after departure. Distinguish event occurrence
> dates from attraction opening hours. Return sourced options and JSON; do not reserve anything.

Use permitted official pages for live research. For a repeatable supplied-source check, attach
[the synthetic sources](../../travel/practice-sources.md) and explicitly prohibit browsing.
The latter must return `provided_only` evidence, not pretend its fictional URLs are live sites.

### 3. Finalize and verify the trip (20 minutes)

Return the specialist's summary/JSON to your TravelPlannerAgent. Explicit selection and
context transfer are valid when automatic delegation is unavailable. Ask it to combine
transport, hotel, and chosen activities into a day-by-day plan, with costs and open questions.

| Check                     | Expected result                                                                |
| ------------------------- | ------------------------------------------------------------------------------ |
| Flight and hotel choice   | Preserved unless you explicitly request a change                               |
| Event E1                  | 27 October fits the supplied trip; availability remains unconfirmed            |
| Event E2                  | 30 October is excluded, not moved to make it fit                               |
| Museum A1                 | Not scheduled on Monday when its supplied schedule says closed                 |
| Unknown museum/hotel cost | Still unknown; no invented zero or final guaranteed total                      |
| Source mode               | Live sources have real links/check dates; fixture sources remain provided_only |
| Booking state             | Nothing purchased, reserved, or submitted                                      |

Save the reviewed itinerary and source limitations under `travel/output/` using the built-in
editing agent when needed. Commit changes to your own coordinator/skills, not generated listings
or the shared agent. The trip is the completed artifact; a website is not required to finish it.

### 4. Explain the boundary (5 minutes)

Show your own agent/skill files and the separately installed AttractionsAgent's source.
Identify the plugin's version and the observed distribution path. If enterprise access is
missing, follow the presenter result but record **managed-plugin consumption blocked**.
A manually copied agent or synthetic response does not pass that check.

**Done when:** your own customizations run in the CLI, a real invocation of the managed
AttractionsAgent supplies date-relevant options, and your verified itinerary preserves the
chosen flights/hotel with sources, costs, and limitations. Missing client features or live
research access must stay visible rather than becoming a claimed success.

## What you just learned

You authored a role and workflows, then reused a centrally distributed specialist. Plugin
installation, agent invocation, web/MCP access, and response correctness are separate checks.
The next segment introduces Awesome Copilot only after this trip-completion stage.

## Optional extras

1. **Independent checks (5-10 min).** Use available subagents for separate date and budget
   reviews of the supplied plan, without competing file edits or real bookings.
2. **Cloud preview (5 min).** Inspect the presenter's delegated task. `/delegate` starts remote
   development work; it is not required to invoke the locally installed AttractionsAgent.
3. **Session hygiene (5 min).** Compare new, resume, and compaction controls. Explain what
   context must be supplied again; compaction does not preserve every detail.
4. **Research/automation preview (5 min).** Inspect `/research`, `/after`, and `/every` help.
   Any test schedule must be read-only and removed before leaving the lab.

## Official References

- [CLI overview](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli) and [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).
- [CLI for Beginners](https://github.com/github/copilot-cli-for-beginners): context, custom agents, skills, and MCP.
- [Plugins and discovery](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) and [enterprise-managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings).
- [Custom-agent tool controls](https://docs.github.com/en/copilot/reference/custom-agents-configuration), [built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools), and [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp).
- [CLI release notes and sandbox prerequisites](https://github.com/github/copilot-cli/blob/main/changelog.md).
- [Whole-week coverage and extras](../../docs/REFERENCES.md).
