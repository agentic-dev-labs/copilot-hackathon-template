# Day 1 Travel Planner

This is the practice context, not a prebuilt agent solution. In [Lab 01](../labs/01-vscode-agent/README.md)
you create TravelPlannerAgent and the FindFlight/FindHotel skills. In [Lab 02](../labs/02-copilot-cli/README.md)
you consume the facilitator's managed AttractionsAgent and finish the trip. Do not add a
same-named local copy of that shared agent.

- [trip-brief.json](trip-brief.json): one fictional traveler, two hotel nights, dates, and budget.
- [practice-sources.md](practice-sources.md): fictional listings/events for repeatable checks.
- `output/`: your generated choices and itinerary, ignored by Git. Retain live/fixture labels.

Use permitted public pages for a separate live browser observation. Never submit a booking,
payment, passenger information, or a real employee's travel details. The fixture domains do
not resolve; they identify supplied text rather than sources you visited.

After trip completion, [Lab 08](../labs/08-deploy/README.md) introduces an Awesome Copilot example
and deploys the already-provided vendor-review app. That app is the bridge to Day 2's business
case; it does not host your Copilot agent or your generated travel research.

Official help: [custom agents](https://docs.github.com/en/copilot/reference/custom-agents-configuration),
[skills](https://code.visualstudio.com/docs/agent-customization/agent-skills),
[plugins](https://docs.github.com/en/copilot/concepts/agents/about-plugins), and
[built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools).
