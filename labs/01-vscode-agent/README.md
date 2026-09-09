# Lab 01: Create your TravelPlannerAgent

**Objective:** Create your own coordinator agent and reusable FindFlight and FindHotel skills,
then research travel options for a fictional traveler. Activities are added in Lab 02 using
the facilitator's shared AttractionsAgent, not an agent you recreate locally.

**Time-box:** 60 minutes

**Prerequisites:** Completed Lab 00, an active Codespace, and the built-in Copilot browser
tools available in the client used for browser work. Otherwise follow the presenter browser
demonstration and record your own browser stage as unverified.

## Presenter Demonstration

The presenter introduces the same workflow in VS Code and Copilot CLI, then creates a small
instruction, custom agent, and skill. Inspect the generated files and actual discovery before
invoking them. Use Ask/Plan/Agent, context, models/Auto, and stop/review/recovery while building.
Inline chat and next-edit suggestions are lighter-weight assistance, not different agent roles.

The first exercise is about Copilot customizations, not building a website or integrating an SDK.
The enterprise plugin reveal follows this lab. Keep attractions unallocated until then.

## Steps

### 1. Set the trip and rules (10 minutes)

Create a working branch. Read the existing repository instructions without replacing their
synthetic-data or evidence rules. Use [the fictional trip brief](../../travel/trip-brief.json)
and keep generated plans under ignored `travel/output/`. Author the customization files under
`.github/` as described below. Never enter a real person's booking or payment details.

Use Copilot to help you author `.github/instructions/travel.instructions.md`. Give it a
meaningful `description` and set `applyTo` to `"travel/**"`. Write and review your own guidance
covering these requirements:

- Use the fictional brief and ask for missing dates or an ambiguous destination.
- Keep currencies, local times, and per-person/per-night price units explicit.
- Link sources and distinguish live observations from supplied synthetic examples.
- Preserve unknown prices as `null`, not zero.
- Permit public search/filter forms, but prohibit purchases, reservations, booking/passenger
  forms, sign-in, and real personal details.

Review its content. Path-scoped guidance is loaded by the applicable client/context; it is
not an access-control rule. Include the essential travel rules in the agent too.

### 2. Create the coordinator (10 minutes)

Ask Copilot to create `.github/agents/TravelPlannerAgent.agent.md`, with display name
`TravelPlannerAgent` and a description that explains when to use it. Start with the supported
`read`, `search`, `web`, and `browser` tool sets. Do not grant shell or booking tools. The
`browser` set is client-specific; verify it rather than assuming it exists in a terminal session.

Give the coordinator three responsibilities: clarify the trip, use your flight/hotel workflows,
and summarize choices without inventing availability. It returns results in chat; use the
built-in editing agent only when deliberately saving reviewed output. Select your new role
and inspect its source. An ordinary Agent-mode answer is not proof your custom agent loaded.

### 3. Create FindFlight and FindHotel (20 minutes)

Create `.github/skills/find-flight/SKILL.md` and `.github/skills/find-hotel/SKILL.md`.
Author each skill with Copilot, then inspect and revise it yourself. Set the frontmatter `name`
to match its folder (`find-flight` or `find-hotel`) and write a `description` that makes the
FindFlight or FindHotel task discoverable. Use the linked official documentation for syntax.

| Skill      | Inputs to request or validate                                | Details its workflow must preserve                                                                                     |
| ---------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| FindFlight | Departure/arrival airports, outbound/return dates, travelers | Up to three options, local dates/times, price, currency, fare conditions, and baggage/fee unknowns                     |
| FindHotel  | Destination, check-in/check-out dates, adults, rooms         | Up to three suitable options, total nights, room type, per-night versus stay total, taxes/fees, and cancellation terms |

Decide how each skill asks for missing input and returns results. Require it to open a source
page before calling a detail observed, include its link and checked date, and preserve unknown
prices as `null`. Supplied fixtures must be labelled `provided_only`, not live inventory.
Both workflows must prohibit bookings, sign-in, personal details, and bypassing site blocks.

The example trip has **two hotel nights**, not three. A skill guides work; it does not
automatically create a booking tool or grant permissions. This lab supplies requirements and
test inputs, not completed skill files or a finished itinerary.

Inspect skill discovery and invoke both by name. Use the [synthetic practice sources](../../travel/practice-sources.md)
for repeatable checks, then try the public search links below where access is permitted.
Do not commit collected real listings or personal data. No CAPTCHA bypass or bulk scraping.

#### Public search starting points

Use **KAYAK UK for flights** and **Booking.com for hotels** first. These links are prefilled
for the fictional trip: Copenhagen CPH to London Heathrow LHR, **26-28 October 2026**,
one adult, one room, and two hotel nights. Confirm the rendered search fields before using
any result; a URL parameter does not prove the site applied it.

| Task       | Start here                                                                                                                                                                                                                              | What to inspect                                                                                                                                                    |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| FindFlight | [KAYAK UK: CPH-LHR return search](https://www.kayak.co.uk/flights/CPH-LHR/2026-10-26/2026-10-28?sort=bestflight_a)                                                                                                                      | Dates, airports, outbound/return times, GBP, per-person return fare, baggage and fees. Distinguish adverts from ordinary results.                                  |
| FindHotel  | [Booking.com: London hotel search](https://www.booking.com/searchresults.html?ss=London%2C%20United%20Kingdom&checkin=2026-10-26&checkout=2026-10-28&group_adults=1&no_rooms=1&group_children=0&selected_currency=GBP&nflt=ht_id%3D204) | One adult/room, two-night stay total in GBP, room type, taxes/fees and cancellation. Exclude dormitory beds and sign-in-only rates from a private-room comparison. |

Add your chosen starting link to the corresponding skill. Ask it to open the result page,
read at most three suitable options, cite the page and checked date, and keep unstated fare
or cancellation terms unknown. Displayed prices are observations, not confirmed offers.
Do not follow a booking, checkout, reservation, or sign-in flow. Keep any collected listings
under ignored `travel/output/`, separate from the synthetic practice sources.

**Browser check, 9 September 2026:** Copilot's built-in browser in Windows VS Code returned
dated flight results with GBP prices from KAYAK UK and hotel results with two-night GBP totals
from Booking.com. No account or CAPTCHA solving was used. KAYAK's `.com` page displayed
dollars despite a GBP query hint, so use the UK link and still inspect the currency.

Other well-known options were less suitable in this session: [Google Flights](https://www.google.com/travel/flights)
stopped at a consent-button interaction timeout, and [Expedia](https://www.expedia.com/Hotels)
showed only partial listings while reporting HTTP 429 rate-limit errors. Some cookie/filter
clicks also timed out on the tested pages. These are **result-reading checks**, not proof of
reliable form automation, detail-page access, or workshop-wide availability.

Recheck the two starting links in the actual workshop client/network. If results are blocked,
record the limitation and use the supplied sources as `provided_only`; that fallback is not
a successful live browser test. Never bypass a CAPTCHA, login, or enforced browser policy.

### 4. Run and verify (15 minutes)

Use your TravelPlannerAgent with the brief and ask it to apply `find-flight` and `find-hotel`.
Compare the returned details with the pages or supplied excerpts. Choose one flight option
and one hotel; keep activities explicitly pending for the shared specialist.

| Check                           | Expected result                                                     |
| ------------------------------- | ------------------------------------------------------------------- |
| Missing dates or ambiguous city | Ask for clarification, not an invented itinerary                    |
| Unknown price                   | `null`/unknown and no unsupported within-budget claim               |
| Synthetic source only           | `provided_only`; no claimed browsing or current inventory           |
| Public page blocked             | Visible limitation; a fixture fallback is not a passed browser test |
| Reservation request             | Research/draft only; nothing bought, held, or reserved              |

Capture a real browser observation when those tools are available. Keep source labels in the
result. Use the built-in editing agent to save reviewed choices and limitations under
`travel/output/` for Lab 02; these generated files stay out of Git. Do not create AttractionsAgent.

### 5. Review and commit (5 minutes)

Inspect the diff and commit the instruction, your coordinator, and both skills on your branch.
Run `uv run pytest` and `uv run ruff check .` to catch unintended repository changes.
Those checks do not prove the new agent or skills were actually invoked; retain session evidence too.

**Done when:** your agent and both skills are discoverable and invoked, your flight/hotel
choices are source-backed with truthful live/fixture labels, missing-input checks behave
correctly, and the four customization files are reviewed and committed. No activities agent
has been copied into the project and no reservation has been made.

## What you just learned

Instructions supply shared guidance; skills supply reusable tasks; a custom agent supplies a
role and selected tools. Built-in browser tools retrieve and inspect pages. None of these is
an MCP server or an automatically deployed application.

## Optional extras

1. **Add a prompt entry point (5 min).** In the local VS Code agent, create
   `.github/prompts/plan-trip.prompt.md` with a description, `agent: TravelPlannerAgent`, and
   a request to apply your two skills to an attached brief. Prompt files are not loaded in
   Agent Host; the skills are the core cross-client task definitions.
2. **Inspect context (5 min).** Start a fresh session with only the brief and supplied sources.
   Identify which instructions and skill bodies loaded and what remains unknown.
3. **Practise recovery (5 min).** Inspect and restore a disposable text change with the client's
   supported checkpoint controls. Do not restore over other work; checkpoints are not Git history.

## Official References

- [Custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents) and [tool/frontmatter reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration).
- [Agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), [instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions), and [prompt files and Agent Host support](https://code.visualstudio.com/docs/agent-customization/prompt-files).
- [Official customization exercise](https://github.com/skills/customize-your-github-copilot-experience).
- [Built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools), [context](https://code.visualstudio.com/docs/agents/concepts/context), and [models](https://code.visualstudio.com/docs/agents/concepts/language-models).
- [Inline suggestions](https://code.visualstudio.com/docs/editing/ai-powered-suggestions), [inline chat](https://code.visualstudio.com/docs/chat/inline-chat), and [review/recovery](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Whole-week coverage and extras](../../docs/REFERENCES.md).
