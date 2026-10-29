# Website hosting

One shared [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview)
environment hosts every attendee website. Attendees publish by pushing: they choose a name with
`/publish-website`, which sets `websiteName` in `config.json`, and
[publish-website.yml](../../.github/workflows/publish-website.yml) does the rest. Nobody signs in to
Azure and no secret exists anywhere.

## How the trust works

[website-hosting.bicep](../../infra/website-hosting.bicep) creates a deploy identity with a
[flexible federated identity credential](https://learn.microsoft.com/entra/workload-id/workload-identities-flexible-federated-identity-credentials)
(preview). Azure accepts a GitHub
[OpenID Connect token](https://docs.github.com/en/actions/reference/security/oidc) only when all
three hold:

| Claim                 | Must be                                                                                   | Why                                                    |
| --------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `sub`                 | `repo:agentic-dev-labs@323143564/*:ref:refs/heads/main`                                   | Any repository of the organisation, on `main` only     |
| `repository_owner_id` | `323143564`                                                                                | Immutable organisation ID; a recycled name cannot match |
| `job_workflow_ref`    | `agentic-dev-labs/copilot-hackathon-template/.github/workflows/website-publisher.yml@refs/heads/main` | Only the template's publisher, which attendees cannot edit |

The `sub` pattern uses GitHub's
[immutable subject format](https://github.blog/changelog/2026-04-23-immutable-subject-claims-for-github-actions-oidc-tokens/),
which every repository created after 15 July 2026 uses, so attendee copies match. The template
itself keeps the older format and never publishes. Anyone who can push to the template's `main`
controls the publisher, so keep that list to the workshop owners.

The [publisher](../../.github/workflows/website-publisher.yml) reads the attendee repository in a job
with no Azure access and passes on only `site/`. The signed-in job runs the template's own
Dockerfile and code, tags each website with its repository ID, refuses a name another repository
owns, and removes the repository's older names in the same slot. The deploy identity holds only:

| Role                       | Scope                  |
| -------------------------- | ---------------------- |
| AcrPush                    | The registry           |
| Container Apps Contributor | The resource group     |
| Reader                     | The resource group     |
| Managed Identity Operator  | The pull identity only |

Websites pull their image with a separate identity that can only pull. The registry has no admin
user. The separate **Deploy my app** workflow (vendor app and rehearsals) still uses the
`AZURE_CREDENTIALS` secret and is unaffected.

## Two slots on Day 5

On Day 5 each attendee website gets a second app: the **feature slot**, `<name>-feature` (the
first 24 characters of the name), which shows a pull request before it is merged. The attendee's
copy of
[deploy-feature-slot.yml](../../.github/workflow-starters/deploy-feature-slot.yml) starts from
[`workflow_run`](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_run)
when **Check my website** passes on a pull request. GitHub runs that event from the workflow file
on `main`, with `main` as its ref, so the token's `sub` still ends in `ref:refs/heads/main` and
the trust above needs no change. A pull request cannot alter how it is deployed. The publisher
builds the pull request's head commit, tags the app `website-slot: feature`, and its server adds
a yellow strip with the pull request, version, and build. The production slot is the website's
own address, published from `main` after the attendee's approval in their `production`
environment. Both slots serve the same files, so their content fingerprints match.

## Deploy

```bash
SUB=4bf7667a-1e78-40f4-b84b-08bed8e94602   # ME-MngEnvMCAP566671-alfarahn-2
az group create -n rg-nn-hackathon-2026-10 -l eastus --subscription $SUB \
  --tags workshop=nn-hackathon-2026-10 purpose=attendee-websites
az deployment group create -g rg-nn-hackathon-2026-10 --subscription $SUB \
  --name website-hosting --template-file infra/website-hosting.bicep
```

It takes about three minutes and is safe to repeat. Ali deployed it on 19 October 2026. If you
deploy elsewhere, copy the outputs into the publisher's `env` block (`deployClientId`, tenant and
subscription) and `environmentDefaultDomain` into the publisher and the
[publish-website skill](../../.github/skills/publish-website/SKILL.md). A test keeps those two in step.

## Run it

List the published websites and their repositories:

```bash
az containerapp list -g rg-nn-hackathon-2026-10 --subscription $SUB \
  --query '[].{name:name, repository:tags."github-repository", url:properties.configuration.ingress.fqdn}' -o table
```

Remove one website (its owner can publish again later):

```bash
az containerapp delete -g rg-nn-hackathon-2026-10 --subscription $SUB --name <website-name> --yes
```

## Cost and teardown

Websites sleep when nobody visits (0.25 vCPU, 0.5 GiB, at most one replica), so idle sites cost
nothing beyond the monthly free grant, but the first visit after a quiet spell takes about 30
seconds while Azure finds a node (measured on 19 October 2026; the 45 MB image pulls in 3 s). The
registry is **Standard** since 25 October 2026 (about USD 20 a month, 100 GiB), upgraded from Basic
so 80 attendees can publish at once; the log workspace keeps 30 days and stops at 1 GB a day.

**Capacity for 80 attendees** (checked 25 October 2026): 80 production websites plus 80 Day 5
feature slots are 160 container apps and at most 40 cores, against the environment's
consumption-core quota of 500 (`az containerapp env list-usages -g rg-nn-hackathon-2026-10 -n
cae-hackathon`). There is no per-environment app limit in that list. The registry's request limits
(2,000 writes and 10,000 reads a minute) cover every attendee pushing in the same minute, and the
organisation's Enterprise plan runs hundreds of Actions jobs at once.

**Keep the environment awake.** On 25 October 2026, with no apps left after the dry-run cleanup,
the environment's compute was suspended (`ManagedClusterSuspended`) and the first publish took
about 13 minutes to wake it. The always-on `keep-warm` app (0.25 CPU, no ingress, about USD 0.20 a
day, defined in `infra/website-hosting.bicep`) prevents that; never delete it during the week.
The publisher now waits up to 12.5 minutes and tells attendees to re-run after 10 minutes.

To keep every website awake during workshop days, at about USD 0.19 per website per day idle
(about USD 15 a day for 80, or 30 with Friday's feature slots), set `MIN_REPLICAS: 1` in the
[publisher](../../.github/workflows/website-publisher.yml), push it to `main`, and wake the websites
that already exist. Reverse both steps with `0` afterwards.

```bash
for app in $(az containerapp list -g rg-nn-hackathon-2026-10 --subscription $SUB --query '[].name' -o tsv); do
  az containerapp update -g rg-nn-hackathon-2026-10 --subscription $SUB -n "$app" --min-replicas 1 --output none
done
```

After the agreed end date, remove everything:

```bash
az group delete -n rg-nn-hackathon-2026-10 --subscription $SUB --yes
```

Pages are public to anyone with the link. They hold fictional content only.
