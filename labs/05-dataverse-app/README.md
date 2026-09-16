# Lab 05: Dataverse-backed app

**Objective:** Connect your deployed app to your own rows in Dataverse.

**Time-box:** 90 minutes

**Prerequisites:** An active browser-based Codespace and the facilitator's separately prepared
vendor app, seeded synthetic rows, and Dataverse connection. See [the prerequisites](../../docs/PREREQS.md).
Lab 08 published your website, not this app. The facilitator prepares the **vendor** target
independently before Day 2; your website and its browser storage remain separate.

Yesterday one browser remembered your information. Today a team needs shared, governed data.
The interface, data store, and automation are different parts. You describe and improve the
experience; the facilitator prepares the data model and access. All commands still run in the
**Codespaces Bash terminal**. No local VS Code, corporate-account switch, or Azure login is needed.

The presenter alternates demonstrations and practice: read (20 minutes), add (35), filter (20),
and verify (15). Use the built-in coding Agent on the vendor app. Advanced schema/authentication
details below are reference material, not a vocabulary test. Stay with one small change.

> **This is a to-do list.** The items happen to be vendors, and the to-dos are the gaps in their
> security controls. If you have ever kept a list of things with a status against each one, you have
> already used this pattern. The list now lives in Dataverse. The attendee label separates
> the exercise's rows for display; it is not a row-level authorization boundary.

## The training environment

The facilitator provisions the training environment and seeds the assigned label's rows before
the lab. Do not create tables or supply secrets yourself. Stop the Day 1 research MCP servers
when they are not needed; their processes can read files/environment available to their user.

|                                                   |                                                      |
| ------------------------------------------------- | ---------------------------------------------------- |
| Environment origin (`DATAVERSE_URL`)              | `https://org0ef69385.crm.dynamics.com`               |
| Web API base (derived by the code)                | `https://org0ef69385.crm.dynamics.com/api/data/v9.2` |
| Vendor reviews                                    | `cr522_vendorreviews`                                |
| Optional extension table (not seeded by this lab) | `cr522_controlfindings`                              |

Columns on a vendor review: `cr522_vendor`, `cr522_system`, `cr522_datatypes`,
`cr522_hostingregion`, `cr522_dataresidency`, `cr522_subprocessors`, `cr522_soc2type`,
`cr522_reportdate`, `cr522_score`, `cr522_sensitivity`, `cr522_gaps`, `cr522_attendee`.

Seed records come from the synthetic sample reports in `src/vendor_assurance/samples/`.
Any rows you add must also be fictional. Do not use real vendor, customer, or patient data.

The Power Platform session earlier this morning covered connectors, Dataverse and Power Automate.
This lab is the same data approached from the other side: a code app talking to the Web API directly.
The official [connector overview](https://learn.microsoft.com/power-automate/dataverse/overview)
and [Web API operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api)
are the two reference entrypoints. The entity set, authentication, and permissions still matter
whether a flow, an MCP tool, or your own code sends the request.

## Steps

### 1. Read your work queue (20 minutes)

Use your assigned, unique workshop label in `config.json`. The facilitator supplies all four
Dataverse environment variables as Codespaces secrets: `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`,
`DATAVERSE_CLIENT_SECRET`, and `DATAVERSE_TENANT_ID`. Never paste credentials into code or chat.
Rebuild or restart the Codespace after secrets are supplied, as directed by the facilitator.

The facilitator runs `uv run python scripts/dataverse_seed.py` with your label and prepared
environment credentials. It updates or creates the three sample vendors without deleting custom
rows. An empty queue goes to the helper; it is not a request to print secrets or grant new roles.

Stop your own Day 1 preview with **Ctrl+C** in its server terminal, then run:

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open **Ports > 8000 > Open in Browser**. Keep it private. Ask Copilot: "Explain this work queue
in plain English. Which records need follow-up, and what evidence supports that? Do not change
anything yet." Compare its answer with the page. The records are fictional, not customer data.

### Reference: where the data comes from

The starter already contains a read-only Dataverse path. Ask Copilot to explain
`app/main.py` and `src/vendor_assurance/dataverse.py`, then run the app locally and confirm
the source changes from local samples to **Dataverse**. The existing query filters by label:

```text
?$filter=cr522_attendee eq 'Your Workshop Label'
```

Codespaces secrets do not automatically reach your deployed app. Commit and push your
configuration, then run **Deploy my app** with **target: vendor** and **connect_dataverse** checked. This uses the
facilitator's Actions variables and secret to configure the Container App. Open your public
URL and confirm **Source: Dataverse**. A page showing fallback samples is not a successful connection.

### 2. Add a fictional item (35 minutes)

Watch the presenter add a small form, then ask:

> Let me add a fictional vendor and system to this work queue. Reject blank values, keep
> credentials on the server, and use the existing Dataverse client and configured workshop
> label. Show a useful error if saving fails. A new row must be Not assessed, not a made-up score.
> Add a mocked test, then let me try the form and reload the page.

Use Agent mode to add a small form and server-side POST handler for a fictional vendor and
system name. Reuse `DataverseClient`; validate input and set the attendee label on the server
from `config.json`, not from a browser-supplied identity. Keep credentials on the server.

Leave score and sensitivity unset: a new row is **Not assessed** until the evaluator runs.
Add a test with a mocked client, submit a fictional row, reload, and see it beside the seeded
three. Ask the prepared Playwright MCP to repeat that exact synthetic journey at Codespace
localhost, or verify manually and label the route. Commit, push, and redeploy the **vendor** target to
make the form available at your public URL.

### 3. Make it useful (20 minutes)

Choose your own wording and layout for a small follow-up filter, with the same data model.
For example: "Show only assessed records needing follow-up, with a count and a way to reset."

Add a filter for scored vendors needing follow-up, for example `cr522_score lt 5`, combined
with the existing attendee filter. Unassessed rows should remain distinguishable from a
calculated failure. This is a training work queue, not an automated risk-acceptance decision.

**Done when:** your deployed page shows Dataverse as its source, your new fictional row
survives a reload, your filter stays scoped to your label, and the mocked write test passes.

### 4. Verify and explain (15 minutes)

Repeat add -> reload -> filter -> reset at the **vendor** deployment URL. Ensure another
label was not substituted, and note that a display filter is not row-level authorization.
Show a neighbour the improvement and explain what a real business rollout would still need.
Use the 13:00 supported build block for further personalisation, not a new mandatory schema.

## When it does not work

| Response                                  | What it means                                                                                      |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `401` or sign-in failed                   | Check all four environment variables in the failing environment, without printing their values.    |
| `403`                                     | Check the Dataverse application user and its security role; either may be missing or insufficient. |
| `400`, syntax error at position           | An apostrophe in a name broke the filter. Escape it by doubling it.                                |
| Empty list, no error                      | The filter matched nothing. Check the name in `config.json` against what the seed script wrote.    |
| Local app works, public app shows samples | Configure Actions variables/secrets and rerun deployment with **connect_dataverse** checked.       |

## What you just learned

A code app can read _and_ write governed Dataverse data through the Web API, while Power Automate
and connectors coordinate the low-code side of the same tables. Neither one replaces the other.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Let the evaluator fill the row (10 min).** Run a sample through the evaluator and persist
   its calculated score and gaps, without asking the model to invent them.
2. **Count your rows (5 min).** Add visible totals for assessed and unassessed rows without changing the shared table schema.
3. **Explain your own diff.** Open a pull request for today's change and have Copilot write the
   summary, then check whether it describes what you actually did.
4. **Check an apostrophe (5 min).** Add a mocked test using `Synthetic O'Brien` and confirm
   query escaping works. Do not deliberately break the shared environment.

## Official References

- [Dataverse Web API operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api) and [types and operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/web-api-types-operations).
- [Query data](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query/overview), [select columns](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query/select-columns), and [create a row](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/create-entity-web-api).
- [Power Automate and Dataverse](https://learn.microsoft.com/power-automate/dataverse/overview): connectors and event-driven flows, covered by the guest session.
- [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces) and [Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions): different execution environments, not automatic credential copying.
- [Container Apps deployment](https://learn.microsoft.com/azure/container-apps/github-actions) and [built-in browser verification](https://code.visualstudio.com/docs/agents/run/browser-tools).
- [Whole-week coverage and extras](../../docs/REFERENCES.md).
