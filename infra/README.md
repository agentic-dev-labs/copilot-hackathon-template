# Website hosting

One shared [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview)
environment hosts every attendee website. Attendees publish by pushing: they choose a name with
`/publish-website`, which sets `websiteName` in `config.json`, and
[publish-website.yml](../.github/workflows/publish-website.yml) does the rest. Nobody signs in to
Azure and no secret exists anywhere.

## How the trust works

[website-hosting.bicep](website-hosting.bicep) creates a deploy identity with a
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

The [publisher](../.github/workflows/website-publisher.yml) reads the attendee repository in a job
with no Azure access and passes on only `site/`. The signed-in job runs the template's own
Dockerfile and code, tags each website with its repository ID, refuses a name another repository
owns, and removes the repository's older names. The deploy identity holds only:

| Role                       | Scope                  |
| -------------------------- | ---------------------- |
| AcrPush                    | The registry           |
| Container Apps Contributor | The resource group     |
| Reader                     | The resource group     |
| Managed Identity Operator  | The pull identity only |

Websites pull their image with a separate identity that can only pull. The registry has no admin
user. The separate **Deploy my app** workflow (vendor app and rehearsals) still uses the
`AZURE_CREDENTIALS` secret and is unaffected.

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
[publish-website skill](../.github/skills/publish-website/SKILL.md). A test keeps those two in step.

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

Websites scale to zero when nobody visits (0.25 vCPU, 0.5 GiB, at most one replica), so idle sites
cost nothing beyond the monthly free grant. The Basic registry costs about USD 5 a month; the log
workspace keeps 30 days and stops at 1 GB a day. After the agreed end date, remove everything:

```bash
az group delete -n rg-nn-hackathon-2026-10 --subscription $SUB --yes
```

Pages are public to anyone with the link. They hold fictional content only.
