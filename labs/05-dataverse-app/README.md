# Lab 05: Dataverse-backed app

**Objective:** Connect your deployed app to your own rows in Dataverse.

**Time-box:** 2 hours, including the guest session

**Prerequisites:** Active Codespace, and the training Dataverse environment below.

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

## Guest Power Platform session - reserved 60 minutes

> **FACILITATOR/COLLEAGUE-LED SLOT:** Power Platform connectors, Dataverse, and Power Automate flows connected to code apps. Content is intentionally not included in this repository.

## Steps

1. Confirm `config.json` holds your name. Everything below filters on it.
2. Run `python scripts/dataverse_seed.py` to load your own three vendor rows. It only touches rows tagged with your name.
3. Open your deployed app and confirm the source line still says local samples.
4. Ask Copilot to make the app read from Dataverse instead, using `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`, `DATAVERSE_CLIENT_SECRET`, and `DATAVERSE_TENANT_ID` from the environment.
5. Query with a filter so you only see your rows: `?$filter=cr522_attendee eq 'Your Name'`.
6. Handle non-success responses explicitly. A 403 means the identity is not a user inside the Dataverse environment.
7. Add a filter for the vendors you would reject, for example `cr522_score lt 5`.

## What you just learned

A code app can use governed Dataverse data through the Web API while Power Automate and connectors coordinate low-code workflows.

**Stretch goal:** Write your own evaluation back as a new row, then confirm it appears alongside the seeded records.
