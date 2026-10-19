# Full Workshop Rehearsal

This folder is for the facilitator's completed-example and live-validation run, not an extra
attendee lab. Use a dedicated private/internal copy in Codespaces. The source template remains
a starter: the agent completes the exercises in the rehearsal copy so attendees still have work to do.

Run **`/rehearse-workshop`** in Copilot Chat's local VS Code Agent mode. The
[prompt](../.github/prompts/rehearse-workshop.prompt.md) drives seven active labs and the supported
daily sessions in timetable order: **00, 01, 02, 08, day-2, day-3, 04, 06, 03, day-4, day-5**, including adjacent coached blocks, actual
implementation, tests, later deployment, and evidence. Keep the [official reference map](../docs/REFERENCES.md) and
[prerequisites](../docs/PREREQS.md) available. Preview-only extras are tracked separately.

Agent Host sessions do not use prompt files. In those clients, invoke the companion
**`/workshop-rehearsal`** [skill](../.github/skills/workshop-rehearsal/SKILL.md), which reads the
same task. Inspect discovery rather than assuming it. Use browser-based Codespaces and its Bash
terminal. A CLI-only session cannot prove the learner's editor interactions or the Website preview.

Day 1 is foundations, Chat, a first website, manual behaviour/source checks, and saved work.
Storage, research, HTML presentations, and early publication are optional. Day 2 is supported
own-idea building with fictional app-local content. Day 3 shows CLI, GitHub MCP, an instructions
file, and a small skill on the learner's own page, plus presenter browser and cloud-agent demonstrations;
Day 4 is build day and Day 5 is presentations. The post-workshop vendor reader uses local
synthetic samples and stays read-only publicly. Dataverse is not a workshop prerequisite.
Do not prebuild a completed learner site in the source template or copy a managed specialist.

The manifest keeps seven numbered lab IDs and `day-2` to `day-5` sessions. Lab 00 records the
README's Monday morning: the GitHub tour, files and Chat, and the first note (its old lab page is
a signpost); Lab 01 records manual verification; `day-3` records the CLI block
and picking an idea; Lab 03 records the cloud-agent demonstration and the
optional Day 4 try. These do not enlarge the individual active lab time-boxes. The former Lab 07
is a signpost to the [advanced post-workshop reference](../post-workshop/advanced/README.md).
The retired Lab 05 is a signpost to the [post-workshop reference](../post-workshop/dataverse/README.md),
not a live-service gate. Preserve its existing implementation and offline regression tests.

These changes must exist in the rehearsal repository before its Codespace can use them.
Copy the updated template through your normal reviewed Git workflow, then create a dedicated
private/internal rehearsal repository. Updating this template does not update existing copies.

Before creating a copy, run `git ls-files -- .facilitator`. If it lists files, have the owner
prepare an approved snapshot excluding that folder before using template generation. Temporary
disclosure approval for this repository is not permission to copy the notes elsewhere. Do not
automatically delete/untrack them or change the owner's retention policy as part of rehearsal.

## Quick Start in Codespaces

The prompt/skill performs these steps for you. These Bash commands also let you run and inspect
the automation directly from the repository root. Python 3.12 is supplied by the devcontainer;
the network helper itself uses only the standard library and can run before dependency setup succeeds.

```bash
RUN="rehearsal/results/$(date -u +%Y%m%dT%H%M%SZ)"
REPOSITORY="$(gh repo view --json nameWithOwner --jq .nameWithOwner)"
python -m rehearsal.evidence --output "$RUN" init --repository "$REPOSITORY"
python -m rehearsal.network --fresh-install --output "$RUN/network.json"
uv sync --locked --extra dev --extra web
bash .devcontainer/setup.sh
python -m rehearsal.evidence --output "$RUN" checks
```

Inspect the exit status of each command. A failing network check is not permission to skip a
fresh install. Complete independent work while investigating the failing stage. Reuse the same
`RUN` directory after an interruption; `init` refuses to overwrite its ledger. Do not rerun `init`
to clear failures. Use a new directory for an intentionally new rehearsal.

## What Is Automated

| Component                      | What it proves                                                                                                         | What it does not prove                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Network doctor](network.py)   | Real PyPI/NuGet downloads, locked wheel hash, fresh temporary environment and cache                                    | All hosts/packages, a full .NET restore, or private-feed authentication         |
| [Evidence runner](evidence.py) | Actual pytest/Ruff exits, revision, timestamp, and explicit status for every required condition                        | That an agent's recorded observation is independently correct                   |
| [Lab manifest](labs.json) | Core conditions and optional extensions remain visible across active labs and supported sessions | That an unavailable feature was exercised |
| [Deployment helper](deploy.py) | Clean pushed commit, confirmed rehearsal repository, unique Actions run, matching artifact and fresh endpoint requests | Form submission, browser layout, or human PR review                             |
| Prompt and skill               | Drive implementation, real product calls, browser journeys, reviews, and fixes in the rehearsal copy                   | Bypass of missing seats, tools, service credentials, or required human approval |

## Python, NuGet, and TLS

The devcontainer uses `UV_NATIVE_TLS=true`, supported by the pinned **uv 0.9.7**, to load the
system's trusted certificates. Current uv documentation calls the newer option `UV_SYSTEM_CERTS`;
that option was added after this repository's pinned version. Certificate and hostname verification
remain enabled. Approved `SSL_CERT_FILE` configuration is retained when supplied by the environment.
Do not install an unverified root certificate, set insecure hosts, or disable TLS verification.

The fresh-install check deliberately uses new temporary `venv` and `cache` directories, public
PyPI, and `--no-config`. It does not reuse or delete the workspace virtual environment. Native trust
addresses trusted corporate CAs, not firewall denial. Windows cleanup is best-effort for transient
locked files; the actual install exit remains the pass/fail condition.

```bash
python -m rehearsal.network --fresh-install --nuget --output "$RUN/network-system.json"
python -m rehearsal.network --fresh-install --bundled-tls --output "$RUN/network-bundled.json"
```

The second command is an optional trust comparison, not a mandatory retry. `pypi-metadata` and
`pythonhosted-artifact` are separate checks; the latter downloads a real wheel from the lockfile
and verifies its SHA-256. NuGet checks download its service index and one real `.nupkg`; they are
diagnostic only because these labs are Python. A NuGet-only failure does not fail the Python gate.

Check the actual **Codespace** network and Linux trust store. A successful Windows check does not
transfer certificates or prove Codespaces reachability. Container/CLI bootstrap access to GitHub,
`ghcr.io`, `mcr.microsoft.com`, and installer endpoints must also work before this Python check can run.

| Failure                                  | Next action                                                                                        |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------- |
| DNS                                      | Check host resolution in the Codespace and its permitted network path                              |
| TLS trust/handshake                      | Check approved proxy/CA configuration in that environment; keep verification on                    |
| Index works, artifact fails              | Check the separate artifact host, not just the package index                                       |
| Fresh install fails, existing tests pass | Inspect install/build/network diagnostics; `--no-sync` is not an installation test                 |
| Missing uv or container build failure    | Inspect Codespaces creation logs and bootstrap endpoint policy                                     |
| Private feed is required                 | Have its owner supply approved configuration separately; do not rewrite the shared public lockfile |

### When Locked Sync Requests a New Lock

If `--locked` asks for a new lock despite unchanged project metadata, check inherited uv
configuration before regenerating anything. Compare this explicit public-index command:

```bash
uv --no-config sync --locked --extra dev --extra web --default-index https://pypi.org/simple
```

If it succeeds while ordinary locked sync fails, investigate the inherited configuration
without printing credential-bearing settings or replacing the shared lock with a private mirror.
Keep approved proxy and certificate trust in place. This checks the existing environment/lock;
use the fresh-install helper above to test new downloads and an empty cache.

## What Must Already Be Prepared

- GitHub repository access, Copilot entitlement, and an authenticated GitHub/Copilot session.
- Codespaces and network access; a preinstalled environment is not a successful fresh install.
- A successful **core-only** startup. Before Day 3, observe actual Copilot CLI authentication in
  VS Code Web, and rehearse the presenter's browser-tools demonstration. The `browser` profile in
  [the setup guide](../.devcontainer/README.md) is only for an owner-approved environment where
  Chromium's sandbox starts. Never bypass sandbox/TLS.
- Only for selected research, run the `research` profile and `check-research`. The app's lock
  does not cover `.venv-research/`, npm, or Chromium; record those preparations separately.
  A full optional-tool smoke can invoke both servers through `scripts/check_workshop_mcp.py`.
- If research is selected, use [official reports and labelled prepared facts](../docs/RESEARCH.md)
  with real download paths, complete conversions and checked values. A visual brief must not
  overwrite the existing page. Review any community skill before suggesting it.
  No inherited workstation paths or desktop-only canvas assumptions.
- The existing training Azure resources and the `AZURE_CREDENTIALS` **Actions secret**, accessible
  to the rehearsal repository. Template copies do not automatically receive secret access.
- The `/create-website` own-idea route in `site/ideas/`, or a continuation of the default app, for Tuesday.
  Use the [build guide](../docs/DAY-2-BUILD.md) and fictional data, without database provisioning.
- The vendor reader is a post-workshop example and is not needed for this run. Do not supply
  Dataverse credentials or enable its training form. Separate later setup needs explicit
  approval through the post-workshop reference and is not part of this run.
- Available Copilot CLI, remote GitHub MCP, Playwright MCP, skill discovery, and cloud-agent
  surfaces in Codespaces. One client may not expose them all; missing access is a recorded
  blocker, not a passed fallback.

**No attendee Azure sign-in.** [The deployment workflow](../.github/workflows/deploy.yml)
authenticates on the GitHub runner using the prepared identity and publishes the application URL.
GitHub/Copilot sign-in and service-owner prework are still required. Credentials must never appear
in chat, source, screenshots, evidence, or downloaded artifacts.

## Execution Rules

1. Confirm a disposable rehearsal repository, unique synthetic label, branch, and derived app name.
2. Confirm permission once for the run's pushes, issues, PRs, and any optional
   deployment cost in the existing training resource group. Normal tool approvals still apply.
3. Test clean installation and artifact connectivity before completing labs. Keep TLS verification
   enabled. A NuGet probe diagnoses optional .NET access; it does not make .NET a Python-lab dependency.
4. Complete and test each exercise rather than merely reading its instructions. Keep source
   observations, current-date limits, and unknowns truthful. Preserve later business CLI
   baselines, original sources, and the deterministic scoring contract.
5. If publication is selected, deploy the exact tested commit through Actions and verify the
   actual endpoint and page behavior.
6. Report every lab, including failures and blocked live features. Unit tests cannot stand in for
   a browser journey, MCP call, skill invocation, or cloud session. Manual beginner checks and the human novice pilot are also
   distinct from automated browser observations; do not invent either.

## Deploy and Retrieve the Endpoint

The `website` target publishes the reviewed `site/` assets with a distinct derived name.
The `vendor` target preserves the business app and existing name. Research downloads, extracted
reports, Markdown notes, and developer tools are not website assets. No hosted Copilot runtime
is deployed. Generated public research stays under ignored `research/` and out of both images.

Publication is optional (Lab 08, with a helper on Days 1, 2, or 4). Use the **website** target and
keep Dataverse disabled. The vendor command is kept for the post-workshop reference only; do not
create an unnecessary second site. No service connection is needed for the local-sample vendor reader.

Use a label such as **Synthetic Rehearsal 9f72a1** in the rehearsal copy. Put the unique suffix
early enough that the derived 32-character app name remains unique. Never reuse an attendee's label.
After the prompt finishes the relevant code changes, review, commit, and push them on the selected
branch. The helper refuses dirty/unpushed changes, a template repository, and a mismatched target.
It dispatches the existing workflow; it does not create Azure resources beyond the app in the
already-prepared training resource group or create credentials.

```bash
BRANCH="$(git branch --show-current)"
python -m rehearsal.deploy dispatch --repository "$REPOSITORY" --ref "$BRANCH" \
  --target website --request "$RUN/deploy-website.json" --approve-deploy
python -m rehearsal.deploy collect --request "$RUN/deploy-website.json" --wait
```

For a separately approved post-workshop run only, the read-only local-sample vendor target uses
the same helper. No seed operation, Dataverse credentials, or write-enable flag is required:

```bash
python -m rehearsal.deploy dispatch --repository "$REPOSITORY" --ref "$BRANCH" \
  --target vendor --request "$RUN/deploy-vendor.json" --approve-deploy
python -m rehearsal.deploy collect --request "$RUN/deploy-vendor.json" --wait
```

`--approve-deploy` records your approval to deploy this confirmed training app; it does not bypass
GitHub policy or client tool permissions. The request is saved **before** dispatch, so a lost response
can be recovered without issuing another deployment. `collect` returns **2** while no matching run
is visible or the run remains pending. Retry collection after GitHub reports the run, not dispatch.
`gh run watch` is subject to GitHub token support; if it is unavailable, follow the run in Actions
and call `collect` without `--wait` after completion. Do not broaden token permissions automatically.

The workflow validates prepared secret presence and the requested SHA before Azure operations.
It uses the Actions identity, selects the requested data source, and sets `WORKSHOP_COMMIT`.
The helper rejects a healthy **old** revision, wrong target/label, wrong website fingerprints,
or unexpected source. Local samples are the intended source for this vendor release, not a
fallback masquerading as live Dataverse. The optional Dataverse validator remains available for
an explicitly approved post-workshop run. It stores the expected website fingerprint at dispatch, so a later
local edit cannot silently change the requested result. Reverting
to sample mode removes active Dataverse environment variables; it does not delete stored secrets
or service rows. Each successful run publishes an artifact named
`deployment-result-<run-id>-<attempt>` containing the verified URL, SHA, label, source, and run URL.
No Azure secret is included. Ordinary attendees also get the HTTPS URL in the workflow summary.

Keep the final endpoint running for inspection. Do not delete the shared resource group, registry,
Container Apps environment, credentials, or other teams' rows. Record cleanup ownership and ongoing cost.

## Record, Resume, and Finish

The agent records checks from [labs.json](labs.json). For example, after observing a source
comparison, attach credential-free screenshots or a transcript under this run directory:

```bash
python -m rehearsal.evidence --output "$RUN" record --lab 01 --check source-check \
  --status passed --observed --evidence "$RUN/lab-01-source.md" \
  --note "Pressed Start again with the examples and counted 1 of 4 done, matching the starter."
python -m rehearsal.evidence --output "$RUN" record --lab 03 --check human-review \
  --status blocked --note "PR checks pass; the repository still requires an independent reviewer."
python -m rehearsal.evidence --output "$RUN" summary --require-complete
```

Evidence files must already exist; do not manufacture them to satisfy the command. Use stable
HTTPS URLs for issues, sessions, PRs, and workflow runs, without credentials or query tokens.
Record expected versus observed behavior in the note. `SUMMARY.md` and `ledger.json` are generated
under the ignored run directory. The summary fails while any core condition is pending, failed,
or blocked. These are **attested observations**, not a tamper-proof audit or independent evaluator.
The agent still must inspect their substance and verify the final deployed commit.

The revised curriculum has new check IDs. Old travel/research evidence cannot complete the new
first-page path; record actual observations rather than renaming passes. `checks` in the manifest
gate core completion; `optional_checks` are displayed in a separate summary table. Use the same
`record` command for either. An optional pass still requires `--observed` and evidence, but an
unselected or blocked extension does not fail `summary --require-complete`. It never fills a
missing core check. Prepared facts cannot pass an optional live download or conversion check.

Record Tuesday's own-idea brief, prototype, manual journey, saved work, and handover under `day-2`.
Record Wednesday's `cli-turn` and `idea-brief` under `day-3`, the GitHub MCP checks and the
presenter's `browser-demo` under Lab 04, the instructions file and skill under Lab 06, and
the cloud-agent demonstration under Lab 03. Record Thursday under `day-4`, with publication as an
optional check, and Friday's logistics and presentation under `day-5`. Report core completion and
extension statuses separately.

Existing ledgers retain retired `05` observations unchanged. They do not satisfy any `day-2`
condition or automatically transfer to Wednesday. Record new observations; missing new checks
remain pending. The runner can add new session entries while preserving the old ledger evidence.

Run session checks with `checks --lab day-2`, an active lab such as `checks --lab 04`, or omit
`--lab` for the full suite, including the maintained Dataverse regression tests.
The test runner never updates live statuses automatically. The known encryption, retention,
residency, SOC 2 metadata, and authenticated-redirect counterexamples have regression tests now;
rerun them, and investigate further counterexamples rather than treating them as a complete language model.

## Official References

- [Complete workshop map](../docs/REFERENCES.md) and the direct reference list in each lab.
- [VS Code prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files).
- [Agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills): the Agent Host-compatible entry point.
- [uv TLS trust](https://docs.astral.sh/uv/concepts/authentication/certificates/) and [uv environment variables](https://docs.astral.sh/uv/reference/environment/).
- [PyPI JSON API](https://docs.pypi.org/api/json/) and [NuGet API](https://learn.microsoft.com/nuget/api/overview), including [package downloads](https://learn.microsoft.com/nuget/api/package-base-address-resource).
- [Codespaces](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces) and [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces).
- [GitHub Actions secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) and [workflow dispatch](https://cli.github.com/manual/gh_workflow_run).
- [Workflow artifacts](https://docs.github.com/en/actions/tutorials/store-and-share-data), [exact-run listing](https://cli.github.com/manual/gh_run_list), [watching a run](https://cli.github.com/manual/gh_run_watch), and [artifact downloads](https://cli.github.com/manual/gh_run_download).
- [Azure Container Apps deployment from GitHub](https://learn.microsoft.com/azure/container-apps/github-actions).
- [Dataverse Web API operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api).
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) and [MarkItDown MCP](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp); private Codespaces stdio connections.
