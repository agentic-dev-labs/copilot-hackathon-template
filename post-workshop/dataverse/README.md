# Dataverse Reference for the Post-Workshop Technical Session

This folder preserves the technical material removed from the beginner workshop after the
18 September planning meeting. It is for the delivery lead and customer technical owner to
prepare a reference project **after the workshop**, not an attendee lab or a production-ready
solution. No live connection, permissions, deployment, or migration is implied by these notes.

The beginner path builds a prototype using fictional content in the app. The technical owner
then agrees the data model, approved environment, access rules, integrations, and release process.
Use [the reusable prompts](PROMPTS.md) to plan that work one reviewed step at a time.

## What Is Preserved

| Existing implementation | Purpose |
| --- | --- |
| [app/main.py](../../app/main.py) | Synthetic vendor reader, follow-up filter, and opt-in training write form. |
| [Dataverse client](../../src/vendor_assurance/dataverse.py) | Server-side authentication, requests, pagination, and redirect protection. |
| [Provisioning script](../../scripts/dataverse_provision.py) | Create the synthetic example schema, not an arbitrary production data model. |
| [Application-user helper](../../scripts/dataverse_app_user.py) | Explicitly approved Dataverse application user and role preparation. |
| [Attendee helper](../../scripts/dataverse_add_attendee.py) | Legacy helper adding the label column, not identities, access grants, or row authorization. |
| [Seed script](../../scripts/dataverse_seed.py) | Load synthetic example records without deleting unrelated rows. |
| [Deployment workflow](../../.github/workflows/deploy.yml) | Separate website/vendor targets using prepared Actions identity. |
| [Deployment evidence](../../scripts/deployment_result.py) | Exact revision/source checks; a healthy old endpoint is insufficient. |
| [App tests](../../tests/test_app_main.py) and [transport tests](../../tests/test_dataverse.py) | Validation, unassessed rows, failure paths, escaping, and redirect regressions. |
| [Evaluator](../../src/vendor_assurance/evaluator.py) | Deterministic teaching scores with source evidence; not a general assurance engine. |

Keep these maintained implementations in their existing paths. Do not create a second fork of
the code in this folder or delete them just because the beginner agenda no longer requires them.

## First Agree the Reference Project

1. Select one low-risk prototype and a technical owner. Describe its users, decisions, input
   fields, and expected behaviour. Do not start by granting access to a real business dataset.
2. Agree the customer's approved repository, runtime, identity, data classification, retention,
   region, service entitlements, cost owner, and security review. Workshop access is not approval.
3. Decide whether Dataverse is appropriate for the use case and existing governance. Have the
   data owner approve the schema and per-user/per-role authorization before implementation.
4. Work first in a separate non-production environment with synthetic records. Do not paste
   confidential reports, employee details, credentials, or customer data into this repository.
5. Agree a small acceptance checklist and the human approval needed for every live change.

The workshop's browser-based Codespaces route does not automatically transfer to a corporate
desktop or enterprise repository. Test the selected client, network, extensions, runtime, and
authentication separately. Do not remove training access or accounts before saving work and
verifying the approved handover route and any remaining technical sessions.

## Connection Knowledge

Credentials are read on the server through environment configuration:

| Setting | Meaning |
| --- | --- |
| `DATAVERSE_URL` | HTTPS environment origin only, without `/api/data/v9.2`. |
| `DATAVERSE_CLIENT_ID` | Approved application identity. |
| `DATAVERSE_CLIENT_SECRET` | Secret supplied through the approved secret store, never source or chat. |
| `DATAVERSE_TENANT_ID` | Tenant for that application identity. |
| `DATAVERSE_PREFIX` | Optional example schema prefix; current default is `cr522`. |

The sample Web API path is `<environment-origin>/api/data/v9.2`. Codespaces secrets and
Actions variables/secrets belong to different execution environments and are not automatically
copied. The website target does not receive Dataverse credentials. Provisioning and role grants
are technical-owner work; a failed connection is not permission to broaden access.

The example review table is `cr522_vendorreviews`. Its fields include vendor, system, data types,
hosting region, residency, subprocessors, report type/date, score, sensitivity, gaps, and attendee.
The optional `cr522_controlfindings` table is not populated by the standard seed exercise.
Inspect the provisioning script for exact logical names, types, and limits before any live use.

### Previous Training Target, Not a Production Default

These non-secret identifiers preserve the former facilitator checklist. They are historical
configuration, not a live health/access check or authorization to reuse the environment.

| Item | Previous training value |
| --- | --- |
| Environment | Hackathon Dataverse, Developer SKU. |
| Origin | `https://org0ef69385.crm.dynamics.com` |
| Web API | `https://org0ef69385.crm.dynamics.com/api/data/v9.2` |
| Application identity name | `nn-hackathon-dataverse`; verify actual application user and role. |
| Seed grouping | Three synthetic sample vendors per unique workshop label; no control-finding rows. |

For a new reference project, obtain the approved identifiers from its owner rather than copying
these values. Set `DATAVERSE_APP_ID` and an explicit approved `DATAVERSE_ROLE` before using the
application-user helper. Provisioning checks existence but does not repair arbitrary schema drift.
The runtime application role need not have schema-provisioning privileges; separate the actors.

The reader escapes the configured workshop label in its OData filter. **That label is display
grouping, not tenant isolation or authorization.** A shared application identity can have access
beyond the displayed rows. A real application must enforce its approved access model server-side.

## Reproduce the Synthetic Training Example

This remains a useful technical walkthrough, but it is not a beginner completion gate.
First inspect the scripts, confirm a disposable target and explicit permission for any writes,
and have the owner supply the four environment settings privately. Configure a unique synthetic
label in the reference copy, never an attendee's active repository.

Run the existing offline checks before touching a service:

```bash
uv sync --locked --extra dev --extra web
uv run pytest tests/test_app_main.py tests/test_dataverse.py tests/test_dataverse_scripts.py
uv run ruff check .
```

### Owner-Approved Script Sequence

The following scripts **can write immediately**; they do not implement a dry-run or `--help`
mode. Read them before running. Obtain approval for the exact target and each operation.

1. **Schema preparation, provisioning identity.** Supply the approved environment and complete
   identity settings through the owner's secret process, then run
   `uv run python scripts/dataverse_provision.py`. It checks for the two synthetic tables and
   individual columns before creating missing objects. It does not validate or migrate arbitrary
   existing field types. Stop on permission errors; do not auto-grant an administrator role.
2. **Application user and role, authorised administrator.** Set the target application's
   `DATAVERSE_APP_ID` and an explicit approved `DATAVERSE_ROLE`, then run
   `uv run python scripts/dataverse_app_user.py`. It finds/creates that application's Dataverse
   user, finds one role in its business unit, and assigns it only if absent. The target app ID
   may differ from the identity authorised to perform this administration. Review that distinction.
3. **Seed, runtime identity.** Switch to the intended runtime application's complete environment
   credentials and confirm the unique synthetic label in the reference copy's `config.json`.
   Run `uv run python scripts/dataverse_seed.py`. It evaluates the checked-in synthetic reports,
   updates matching vendor rows for that label, and creates missing ones without deleting custom
   rows. It uses the current evaluation date; the CLI's separate `--as-of` option is not a seed
   script argument. Do not assume a historical sample score without checking its date.
4. **Legacy column helper, only if needed.** `uv run python scripts/dataverse_add_attendee.py`
   adds the attendee label column to an older schema. Normal provisioning already includes it.
   It does not create an account, assign access, or provide user isolation.

The provisioning and application-user helpers permit an Azure CLI token fallback when no
application credentials are supplied. For the documented repeatable reference route, supply
the complete approved application settings first and do not rely on an ambient personal login.
Never request attendee Azure login as a workaround. The seed/runtime path disallows that fallback.

After seeding, keep runtime credentials least-privileged and separate from provisioning authority.
No command above should run merely because an assistant opened this Markdown file.

For an explicitly approved **private** training preview only:

```bash
WORKSHOP_ALLOW_WRITES=true uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open the private forwarded port through Codespaces **Ports > Open in Browser**. Check:

1. **Read:** the intended workshop label and `Source: Dataverse`, not local-sample fallback.
2. **Add:** one uniquely named fictional vendor and system. Reject blank or oversized input.
3. **Reload:** the row remains and displays **Not assessed**, never an invented score.
4. **Filter:** assessed scores below five appear; an unassessed row is not a failure.
5. **Reset:** the full label-scoped queue returns. Compare displayed counts with the rows.
6. **Failure:** a mocked service failure is not reported as saved. If a live response is lost,
   inspect for the row before retrying; do not repeatedly submit and create duplicates.

The POST handler accepts only bounded vendor/system names, rejects extra fields, assigns the
label from server configuration, and leaves score and sensitivity unset. Source text and entered
names must remain safely rendered. Preserve deterministic results and exact evidence quotations.

## Release and Production Gaps

The training flag is **not authentication**. Never enable `WORKSHOP_ALLOW_WRITES` on a public
deployment. The current workflow explicitly sets it false on both creation and update. This
public reader is suitable only for the approved synthetic example, not real confidential data.

For an approved reference release, use the existing `vendor` target and explicitly opt into
Dataverse with prepared Actions access. Keep `website` separate. Validate the exact tested commit,
source, deployment artifact, and endpoint. Repeat the read/filter journey there; the missing
public write form is intentional. Local tests and a successful health response do not prove a
live integration or authorization model.

The existing workflow reads `DATAVERSE_URL`, `DATAVERSE_CLIENT_ID`, and `DATAVERSE_TENANT_ID`
from **Actions variables**, and `DATAVERSE_CLIENT_SECRET` from an **Actions secret**. Azure
deployment uses the separately prepared `AZURE_CREDENTIALS` Actions secret. None is copied from
Codespaces automatically. Confirm the repository is allowed to use each secret without printing it.
The technical owner sets **target: vendor** and **connect_dataverse: true** only after approval.
The website target refuses this combination and must not receive service credentials.

Before real work, replace training assumptions with reviewed design for identity and row access,
CSRF/request-origin protection where applicable, rate limits and input boundaries, duplicate-safe
writes, secret lifecycle, audit/monitoring, backup/recovery, accessibility, and retention/deletion.
Require independent role-isolation and negative tests, approved deployment/rollback, and explicit
data-owner/security acceptance. Do not label the workshop prototype production-ready.

## Troubleshooting Without Exposing Secrets

| Observation | Technical-owner check |
| --- | --- |
| Sign-in fails | Check presence/validity of the three identity settings privately. |
| HTTP 403 | Verify application user and the approved least-privilege role; do not auto-grant. |
| HTTP 400 | Compare schema names, field types, and escaped filters with the actual environment. |
| Empty queue | Check seed target and configured label; an empty result is not service failure. |
| Local samples appear | Read the labelled fallback and investigate the connection; do not call it Dataverse success. |
| Preview works, deployment does not | Check the separate Actions configuration and exact deployment target. |
| Save cannot be confirmed | Inspect existing rows before retrying a possibly completed request. |

## Official References

- [Dataverse Web API operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api).
- [Query data](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/query/overview).
- [Create a row](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/create-entity-web-api).
- [Dataverse security](https://learn.microsoft.com/power-platform/admin/wp-security-cds).
- [Manage application users](https://learn.microsoft.com/power-platform/admin/manage-application-users).
- [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces).
- [Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
- [Workshop topic map](../../docs/REFERENCES.md).