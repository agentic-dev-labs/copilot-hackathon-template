# Lab 05: Dataverse-backed app

**Objective:** Connect a small code application to a facilitator-provided Dataverse-backed API.

**Time-box:** 2 hours, including the guest session

**Prerequisites:** Active Codespace and a facilitator-provided API base URL named `<DATAVERSE_API_URL>` with synthetic training records.

## Guest Power Platform session - reserved 60 minutes

> **FACILITATOR/COLLEAGUE-LED SLOT:** Power Platform connectors, Dataverse, and Power Automate flows connected to code apps. Content is intentionally not included in this repository.

## Steps

1. After the guest session, copy `.env.example` to a Codespace-local `.env` if the facilitator provides one; never commit it.
2. Set `DATAVERSE_API_URL=<DATAVERSE_API_URL>` in the Codespace environment.
3. Ask Copilot to identify an API client pattern that reads configuration from the environment.
4. Implement a small endpoint or command that lists synthetic vendor-review records from the API.
5. Handle non-success responses explicitly and display a useful error.
6. Run the app in the Codespace and confirm only synthetic records appear.
7. Add a test with a mocked API response and review the diff.

## What you just learned

A code app can use governed Dataverse data through an API while Power Automate and connectors coordinate low-code workflows.

**Stretch goal:** Add a synthetic review-status filter without changing the upstream schema.
