# Reviewed Prompts for the Reference-Project Session

Use these after the workshop with the technical owner and the
[reference guide](README.md). These are Markdown planning aids, not installed agents or grants
of tool permission. Run one at a time, inspect the result, and approve the next stage explicitly.
Replace placeholders with approved non-secret identifiers; never insert secrets or real records.

## 1. Scope and Readiness, Read Only

> Read the approved prototype and post-workshop/dataverse/README.md. Propose the smallest
> reference project for <business outcome>. Identify users, data fields, read/write operations,
> ownership, approval gates, and unresolved decisions. Distinguish existing working code from
> assumptions. Do not edit files, call live services, create resources, grant roles, or deploy.
> Keep sample information fictional and ask for missing decisions instead of guessing.

## 2. Data Model and Access, Plan Only

> For the approved scope, propose a Dataverse data model and permission matrix. Reuse suitable
> existing tables only after their owner approves them. Explain field types, required values,
> relationship choices, retention, and how each user/role is authorized to each operation.
> Do not treat the workshop label filter as security. Identify where application identity and
> user authorization differ. Return a design and test cases, not provisioning commands executed
> against an environment. Wait for data-owner and security review.

## 3. Inspect the Existing Implementation

> Inspect app/main.py, src/vendor_assurance/dataverse.py, the Dataverse scripts, related tests,
> and the deployment workflow. Map them to the approved design. Identify reusable pieces and
> training-only assumptions, especially the private write switch, shared identity, label filter,
> read-only public deployment, and sample fallback. Preserve redirect and credential protections.
> Propose small changes and a rollback plan. Do not rewrite the evaluator or change live settings.

## 4. Implement a Bounded Change

> Implement only <approved change> in <approved files> in the reference copy. Keep credentials
> on the server and preserve input validation, safe rendering, server-owned scope, and unassessed
> rows. Add focused mocked tests for success, blank/oversized input, unexpected identity/score
> fields, denied access, duplicate/ambiguous saves, and service failures as applicable. Explain
> which security requirements remain unimplemented. Do not use real data, enable public training
> writes, alter shared schema, commit, push, grant permissions, or deploy without separate approval.

## 5. Prepare an Approved Non-Production Connection

> Check configuration presence without printing values. Confirm <approved environment>, tenant,
> application identity, table prefix, and least-privilege role with the owner. Review the existing
> provisioning/application-user/seed scripts and list exactly which operations would write.
> Do not execute them until the target and each proposed change are explicitly approved. Do not
> use Azure CLI sign-in, disable TLS, follow credential-bearing redirects, or broaden roles as
> a workaround. Record a blocker when approval or service access is missing.

## 6. Validate the Live Reference

> In the approved private non-production preview, use a uniquely named synthetic record to
> verify read -> add -> reload -> filter -> reset. Check Not assessed before evaluation, server
> scope, and blank-input rejection. Compare the UI with observed service results. Test denied
> access using the approved role-isolation plan, not another person's identity. If a save result
> is ambiguous, read back before retrying. Record expected/actual behaviour and redact evidence.
> Do not delete all records or claim mocked results as live service verification.

## 7. Review a Release Before Dispatch

> Review the approved branch, exact tested commit, required human review, environment settings,
> build artifacts, rollback, and data-owner acceptance. Use the prepared deployment identity;
> never put a credential in a prompt. Keep the workshop public vendor target read-only. List
> unresolved production gaps and stop if a training flag is proposed as authorization. Ask for
> explicit approval of the target and cost before dispatch. After approval, verify the actual
> workflow result, commit, source, endpoint, and meaningful user journey. Do not substitute an old
> healthy revision, local samples, or a screenshot for that verification.

## 8. Handover and Retention

> Produce a short operational handover with owner, approved environments, support route,
> configuration names only, deployment/rollback procedure, tests, known limitations, monitoring,
> retention, and cleanup responsibilities. Separate verified observations from pending approvals.
> Preserve work and confirm approved access before requesting removal of temporary training
> membership. Do not delete personal accounts, resources, repositories, or service data.

## Original UI Improvement Prompt

This preserves the useful part of the retired beginner Dataverse exercise for a technical clinic:

> Make the form labels and table spacing clearer in app/main.py. Keep source information,
> escaping, input validation, the server-owned label, private-only write restrictions, and
> calculated scores unchanged. Change only the interface; show the small plan first. After
> approval, run focused mocked tests and repeat the synthetic private add/reload/filter/reset
> journey. Report what was actually observed and any remaining limitation.