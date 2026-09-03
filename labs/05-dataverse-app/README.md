# Lab 05: Dataverse-backed app

**Objective:** Connect a small code application to a facilitator-provided Dataverse-backed API.

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

1. Read the environment values above. Set `DATAVERSE_API_URL` in your Codespace rather than hard-coding the host.
2. Get an access token for the environment. In the Codespace terminal, `az account get-access-token --resource https://org0ef69385.crm.dynamics.com/` returns one; the facilitator will confirm how you sign in.
3. Ask Copilot to write a small client that reads the base URL from the environment and lists vendor reviews.
4. Query the three seeded rows and sort them by `cr522_score`. Expect scores of 10, 8, and 2.
5. Handle non-success responses explicitly. A 403 almost always means the signed-in identity is not a user in the Dataverse environment.
6. Add a filter, for example `?$filter=cr522_score lt 5`, to list only the vendors you would reject.
7. Add a test with a mocked API response and review the diff.

## What you just learned

A code app can use governed Dataverse data through the Web API while Power Automate and connectors coordinate low-code workflows.

**Stretch goal:** Write your own evaluation back as a new row, then confirm it appears alongside the seeded records.
