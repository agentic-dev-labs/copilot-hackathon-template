# Lab 05: Dataverse-backed app

**Objective:** Connect your deployed app to your own rows in Dataverse.

**Time-box:** 90 minutes

**Prerequisites:** Active Codespace, your app deployed in Lab 08, and the training Dataverse environment below.

> **This is a to-do list.** The items happen to be vendors, and the to-dos are the gaps in their
> security controls. If you have ever kept a list of things with a status against each one, you have
> already built this. The only difference is where the list lives: in Dataverse, where your
> organisation decides who may read it and who may change it.

## The training environment

A Dataverse environment is already provisioned and seeded with synthetic vendor reviews.

| | |
|---|---|
| Web API base | `https://org0ef69385.crm.dynamics.com/api/data/v9.2` |
| Vendor reviews | `cr522_vendorreviews` |
| Control findings | `cr522_controlfindings` |

Columns on a vendor review: `cr522_vendor`, `cr522_system`, `cr522_datatypes`,
`cr522_hostingregion`, `cr522_dataresidency`, `cr522_subprocessors`, `cr522_soc2type`,
`cr522_reportdate`, `cr522_score`, `cr522_sensitivity`, `cr522_gaps`.

Every record is generated from the synthetic sample reports in
`src/vendor_assurance/samples/`. There is no real vendor, customer, or patient data here.

The Power Platform session earlier this morning covered connectors, Dataverse and Power Automate.
This lab is the same data approached from the other side: a code app talking to the Web API directly.

## Steps

### 1. Claim your rows

Put your name in `config.json`, then run `python scripts/dataverse_seed.py`. It loads three vendor
reviews tagged with your name and leaves everybody else's rows alone.

### 2. Read them from your app

Your deployed app still says it is reading local samples. Ask Copilot to read from Dataverse
instead, using `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`, `DATAVERSE_CLIENT_SECRET` and
`DATAVERSE_TENANT_ID` from the environment, filtered to your own rows:

```
?$filter=cr522_attendee eq 'Your Name'
```

Reload your public URL. Your rows, your name, your app. Stop and look at it before moving on.

### 3. Add a row

Add a form that writes a new vendor review back to Dataverse. Submit it, reload, and watch it appear
next to the seeded three. That is the whole trick: the list you read from is the list you write to.

### 4. Filter to the ones you would reject

Show only the vendors that failed, for example `cr522_score lt 5`. One line of OData turns a report
into a work queue.

## When it does not work

| Response | What it means |
|---|---|
| `401` | The token was rejected. Check all four environment variables are set in your Codespace. |
| `403` | Authentication worked, authorisation did not. The identity is not a user inside the Dataverse environment. |
| `400`, syntax error at position | An apostrophe in a name broke the filter. Escape it by doubling it. |
| Empty list, no error | The filter matched nothing. Check the name in `config.json` against what the seed script wrote. |

## What you just learned

A code app can read *and* write governed Dataverse data through the Web API, while Power Automate
and connectors coordinate the low-code side of the same tables. Neither one replaces the other.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Let the evaluator fill the row.** Run the evaluator over a sample report and write its real
   score and gaps back, instead of typing a row by hand.
2. **Make it a queue.** Add a status column to your rows and let the page mark a review as handled.
3. **Explain your own diff.** Open a pull request for today's change and have Copilot write the
   summary, then check whether it describes what you actually did.
4. **Break it deliberately.** Put an apostrophe in a vendor name and watch the OData filter fail,
   then fix the escaping.
