# Lab 05: Dataverse-backed app

**Objective:** Connect your deployed app to your own rows in Dataverse.

**Time-box:** 90 minutes

**Prerequisites:** Active Codespace, your app deployed in Lab 08, and the facilitator's prepared Dataverse connection. See [the prerequisites](../../docs/PREREQS.md).

> **This is a to-do list.** The items happen to be vendors, and the to-dos are the gaps in their
> security controls. If you have ever kept a list of things with a status against each one, you have
> already used this pattern. The list now lives in Dataverse. The attendee label separates
> the exercise's rows for display; it is not a row-level authorization boundary.

## The training environment

The facilitator provisions the training environment; you seed your own sample rows below.

| | |
|---|---|
| Environment origin (`DATAVERSE_URL`) | `https://org0ef69385.crm.dynamics.com` |
| Web API base (derived by the code) | `https://org0ef69385.crm.dynamics.com/api/data/v9.2` |
| Vendor reviews | `cr522_vendorreviews` |
| Optional extension table (not seeded by this lab) | `cr522_controlfindings` |

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

### 1. Claim your rows

Use your assigned, unique workshop label in `config.json`. The facilitator supplies all four
Dataverse environment variables as Codespaces secrets: `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`,
`DATAVERSE_CLIENT_SECRET`, and `DATAVERSE_TENANT_ID`. Never paste credentials into code or chat.
Rebuild or restart the Codespace after secrets are supplied, as directed by the facilitator.

Run `python scripts/dataverse_seed.py`. It updates or creates the three sample vendors tagged
with your label, without deleting custom rows or modifying another label's rows. The optional
Azure CLI authentication fallback is for facilitator scripts; the web app uses environment credentials.

### 2. Read them from your app

The starter already contains a read-only Dataverse path. Ask Copilot to explain
`app/main.py` and `src/vendor_assurance/dataverse.py`, then run the app locally and confirm
the source changes from local samples to **Dataverse**. The existing query filters by label:

```text
?$filter=cr522_attendee eq 'Your Workshop Label'
```

Codespaces secrets do not automatically reach your deployed app. Commit and push your
configuration, then run **Deploy my app** with **connect_dataverse** checked. This uses the
facilitator's Actions variables and secret to configure the Container App. Open your public
URL and confirm **Source: Dataverse**. A page showing fallback samples is not a successful connection.

### 3. Add a row

Use Agent mode to add a small form and server-side POST handler for a fictional vendor and
system name. Reuse `DataverseClient`; validate input and set the attendee label on the server
from `config.json`, not from a browser-supplied identity. Keep credentials on the server.

Leave score and sensitivity unset: a new row is **Not assessed** until the evaluator runs.
Add a test with a mocked client, submit a fictional row, reload, and see it beside the seeded
three. If built-in browser tools are available, ask Copilot to repeat that exact journey and
report the observed result; manual verification remains valid. Commit, push, and redeploy to
make the form available at your public URL.

### 4. Filter to the ones you would reject

Add a filter for scored vendors needing follow-up, for example `cr522_score lt 5`, combined
with the existing attendee filter. Unassessed rows should remain distinguishable from a
calculated failure. This is a training work queue, not an automated risk-acceptance decision.

**Done when:** your deployed page shows Dataverse as its source, your new fictional row
survives a reload, your filter stays scoped to your label, and the mocked write test passes.

## When it does not work

| Response | What it means |
|---|---|
| `401` or sign-in failed | Check all four environment variables in the failing environment, without printing their values. |
| `403` | Check the Dataverse application user and its security role; either may be missing or insufficient. |
| `400`, syntax error at position | An apostrophe in a name broke the filter. Escape it by doubling it. |
| Empty list, no error | The filter matched nothing. Check the name in `config.json` against what the seed script wrote. |
| Local app works, public app shows samples | Configure Actions variables/secrets and rerun deployment with **connect_dataverse** checked. |

## What you just learned

A code app can read *and* write governed Dataverse data through the Web API, while Power Automate
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
