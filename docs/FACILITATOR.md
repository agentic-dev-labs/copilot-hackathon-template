# Facilitator runbook

Use the [agenda](AGENDA.md) for timing and the [coverage guide](REFERENCES.md) for official
links to every feature family. The priority is business-user AI enablement. Day 1 establishes
a useful research/presentation/site loop; Day 2 connects it to shared data; Days 3-5 add depth.
All attendee steps use browser-based Codespaces and its Bash terminal, never a laptop runtime.
Use 8-minute demonstrations followed by practice and personalisation, not long feature tours.

## Demonstration preparation

Prepare these results before Day 1 so network waits and preview setup do not consume lab time:

| Block                  | Live core                                                                                  | Prepared result or fallback                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Opening | A useful visual brief, a small interactive site, and a short CLI turn | Prepared advanced results; no mandatory feature-by-feature tour |
| Tool connection | Learners add/trust Playwright and MarkItDown MCP in the Codespace | Prepared dependencies; actual invocation still required |
| Research | One report first, verified facts, then bounded five-year collection | [Prepared public facts](annual-report-facts.json), labelled as prepared |
| Skill discovery | Awesome Copilot shortlist and the prepared visual-brief skill | Complete folders, attribution, dependencies, and client checks |
| Personal build | One interaction, localStorage, and browser verification | Extend the morning HTML instead of starting another project |
| Deployment | Website target, reviewed assets, exact commit, actual URL | Vendor target prepared separately before Day 2 |

Use public reports for Day 1 research and the synthetic vendor app for the later business case.
Name the model, agent role, tools, context, and execution
environment as different choices. GitHub Copilot is the focus; Microsoft 365 Copilot and
Power Platform are related products, not interchangeable entitlements or tool surfaces.

Show how to stop or steer work as well as how to start it. Agent edits can be applied directly:
inspect the actual diff and restoration controls rather than promising a universal approval
dialog. Checkpoints are temporary workspace recovery, not Git history or an undo for external writes.

The [specialist topics](REFERENCES.md#optional-possibilities-and-specialist-topics) are a
reference shelf: SDK, other IDEs, migrations, BYOK, integrations, parallel execution, and
administration do not add prerequisites to Monday. Use the
[daily small tasks](REFERENCES.md#small-tasks-for-early-finishers) for early finishers.

## Organization setup

1. Confirm all items in [PREREQS.md](PREREQS.md).
2. Verify Copilot cloud-agent, automation, Codespaces, and remote GitHub MCP availability in the event organization.
3. Grant the required repository access. Test branch rules and use only the bypass permissions the cloud workflow actually requires.
4. Provision the shared Azure resources once: resource group, Container Apps environment, and container registry. See [PREREQS.md](PREREQS.md) for the provisioned names.
5. Configure Actions and Codespaces service access separately as listed in [PREREQS.md](PREREQS.md).
   `scripts/create_attendee_repos.py` creates repositories and team grants, not credentials.

## Governance repository

The private repository `agentic-dev-labs/.github-private` now supplies managed settings and
the plugin marketplace. The outdated organization vendor-analyst was removed with owner
approval on 2026-09-09. Keep the correct local analyst/writer/reviewer for Friday's Lab 06.

| Path                                             | Job                         | Reaches                                                       |
| ------------------------------------------------ | --------------------------- | ------------------------------------------------------------- |
| `copilot/managed-settings.json`                  | Enterprise managed settings | Licensed users covered by the configured enterprise policy    |
| `.github/plugin/marketplace.json` and `plugins/` | Plugin marketplace          | Users whose clients can read the marketplace and plugin files |

Custom agents and plugins have different scope ladders. Agents have an organization level;
plugins do not use that same directory-based discovery mechanism.

- If organization agents are added later, their location is root `agents/`, not workspace
  `.github/agents/`. This is a reference concept, not an active second vendor analyst here.
- Repository-level agents stay in `.github/agents` and apply only to that repository.
- Plugins have no organization scope. Distribute them per repository through
  `.github/copilot/settings.json`, or enterprise-wide through `managed-settings.json`.

Consult [custom-agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration),
[plugins](https://docs.github.com/en/copilot/concepts/agents/about-plugins), and
[enterprise-managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).
Supported components and policy keys vary by client; a marketplace does not itself grant access to private files.

## Optional Later Plugin Distribution

Check access and client behavior before relying on distribution. Do not alter global policies
mid-demonstration or assume repository agents and plugins are the same thing.

1. **For participants in this optional demo, verify read access to the governance repository.** When `enabledPlugins`
   installs a plugin, the client fetches plugin files as the signed-in user. The repository
   is private, so users need access to fetch it. Inspect plugin diagnostics if it does not load.
2. Select the organization as the enterprise source of governance so
   `copilot/managed-settings.json` takes effect. Check the effective settings in the client;
   refresh or restart as its documentation requires rather than assuming immediate propagation.
3. Verify discovery and a real invocation in both target clients. For an approved presenter install,
   use `copilot plugin marketplace add agentic-dev-labs/.github-private`, refresh the catalog,
   then `copilot plugin install attractions@agentic-dev-labs`. Do not present a manual install
   as proof that enterprise auto-install worked; inspect the effective settings and origin separately.
4. Verify the effective Managed entry for `attractions@agentic-dev-labs`. Do not copy a local
   AttractionsAgent or silently substitute repository-level installation. Missing managed access
   is a blocker for that learning outcome, even if a presenter fallback can be shown.
5. Never point the template at a marketplace repository that does not resolve; it fails for
   every team at once.
6. Leave `strictKnownMarketplaces` alone. It is enterprise-wide with no organization scope,
   and restricting it blocks plugins installed from every other marketplace.

**Optional Day 5 specialist:** [attractions plugin](https://github.com/agentic-dev-labs/.github-private/tree/main/plugins/attractions).
The tested CLI ID is `attractions:AttractionsAgent`. Inspect the current identifier in each
client. The plugin installs neither an MCP server nor a browser package. It returns dated
activity suggestions and never makes reservations. The owner approved adding it to the
existing managed-plugin list; other enterprise settings stay unchanged.

**Optional later design-review example:** open [Awesome Copilot](https://github.com/github/awesome-copilot/)
and [web-design-reviewer](https://github.com/github/awesome-copilot/tree/main/skills/web-design-reviewer).
Prepare an adaptation before the workshop, retaining attribution and references. Reuse the
prepared Playwright MCP; do not install unreviewed browser servers. Demonstrate
one small visual check/fix on the provided app without changing the heading, source indicator,
or health contract. This is optional later material, not part of Lab 08's deployment time.

Use this prepared request after opening the collection and explaining its provenance. This is
our bounded adaptation of that review workflow, not an unmodified installed upstream skill:

```text
Review the provided workshop vendor app at the presenter-supplied URL using the prepared
Playwright MCP in Codespaces. Inspect its rendered layout and accessible controls at desktop and
narrow widths where supported. Report at most one concrete problem with an element reference
and a screenshot or page observation. If there is no supported finding, say so.

Propose the smallest fix, then implement it only after presenter review. Keep the page heading,
source indicator, sample rows, escaping, and health/deployment contracts unchanged. Use the
existing app styles and tests, with no framework, browser server, or package installation.
Re-run the relevant tests and inspect the changed element with the same browser tools.
Separate actual observations from assumptions; do not invent a defect to make the demo work.
```

Optional time budget: two minutes for the source distinction, five for the prepared
before/after observation, and three for verification. If live generation would
overrun, show the already verified result and label it prepared. Do not ship the presenter's
demo customization as a learner-authored skill or imply the community item is managed.

For an optional Day 5 document-tool demo, use `copilot plugin install assurance-toolkit@agentic-dev-labs`
after confirming it appears in the marketplace. Inspect its agent, skills, and document-conversion
MCP configuration. Use a synthetic document and verify a quotation; do not promise that every
PDF failed before installation or that every converted file has reliable page provenance.
The toolkit is an optional presenter install, separate from the core labs. Verify its actual
tool permissions, runtime dependencies, and client support in the governance repository.
Keep this optional toolkit separate from Monday's core tools and visual-brief skill. A verified transcript
is a presenter fallback, not evidence that the attendee's plugin actually worked.

## Create team repositories

Repository secrets are **not** copied from a template. The script creates private repositories
and grants the configured attendee team write access. It first inspects the selected template
and stops if facilitator preparation files are present or the inspection fails.

The current source temporarily tracks `.facilitator/`. Its disclosure approval applies only
to this repository, so the owner must prepare an approved template snapshot excluding that
folder before making attendee copies. Do not copy the notes and remove them afterward.
Pass the approved template's actual `owner/repository` to `--template`:

```shell
python scripts/create_attendee_repos.py nn-na-2026-10-team-01 nn-na-2026-10-team-02 --template OWNER/APPROVED-TEMPLATE
```

Re-running reuses existing repositories and reapplies the team grant. It does not create
identities, issue credentials, buy seats, or configure secret access. Template changes also do
not automatically update team repositories that already exist.

1. Confirm the approved, note-free source is flagged as a template.
2. Run the script with the repository names you need.
3. Verify the team grant and assign one unique workshop label/app name per deployed repository.
4. Apply and test review rules. Configure Actions secret access and Day 2 Codespaces secrets separately.
5. Run CI once and create a Codespace in each repository.

## Dry run

Use the [full Codespaces rehearsal package](../rehearsal/README.md) and `/rehearse-workshop`
to execute the labs in a dedicated copy. It records live evidence separately from test results,
checks a fresh package install, and verifies the exact deployed commit. No attendee Azure login
is required; repository access to the prepared Actions identity must already exist.

- Create a Codespace from a test team repository on the corporate network.
- Confirm extensions install and `uv sync --locked --extra dev --extra web` succeeds.
- Inspect the devcontainer: Python version, dependency lock, minimum host requirements, shared editor settings, and forwarded port. Extension IDs are not version pins; CLI authentication is separate.
- Run tests and the sample CLI end to end.
- Use `--as-of 2026-10-26` to confirm sample scores 10, 8, and 2, plus exact source quotations.
- Rehearse inline assistance, context attachments, model/usage controls, and checkpoint recovery on a disposable change.
- Add/trust the workspace MCP connections from Lab 01 using an attendee identity. Test a real
  browser navigation/download and a MarkItDown conversion. Install presence is not tool invocation.
- Follow [the research guide](RESEARCH.md): inspect one official PDF first, then collect the
  five-year window. Keep downloads ignored and separate from synthetic fixtures. Record blocked
  downloads or truncated conversion; use labelled prepared facts without claiming a live pass.
- Invoke the portable visual-brief skill, review source values, and create a learner-style HTML
  presentation in the rehearsal copy, not the source template. Test the chosen community skill
  in Linux; local presenter skills and desktop canvas features are not automatically available.
- Check CLI sandbox/local-network support in the exact Codespace. Current Linux versions may
  require networking helpers and `/dev/net/tun`; inspect effective `/sandbox` settings and the
  official CLI release notes. Package downloads alone do not prove agent access. Do not bypass policy.
- Check the synthetic Space's sources and permissions; do not attach the whole repository or facilitator notes.
- Assign a test issue to Copilot and verify one reviewed result within the lab time-box. Check current limits instead of relying on a historical session cap.
- Create an automation triggered by issue creation, open a matching issue, and confirm exactly one session starts.
- Follow Lab 07's metadata-only hook example and harmless deny test. Local log files are not a durable compliance trail.
- Test remote GitHub MCP in read-only mode.
- Test Playwright MCP against Codespace localhost, and manually open the private forwarded preview.
  Add/refresh/remove in the same browser context; repeat independently at the deployed origin.
- Exercise the Dataverse-backed training API using synthetic records.
- Set the unique label, dispatch **Deploy my app / website**, and verify the current site bytes,
  commit, URL, and interaction. A healthy endpoint is not a checked chart or storage journey.
- Independently prepare **Deploy my app / vendor** with Dataverse and seeded rows before Day 2.
  Confirm **Source: Dataverse**, not samples. Stop unneeded research tools before service access.
- Optional Day 5 only: invoke the managed specialist and verify origin. No local duplicate.
- Follow Lab 06's JSON generation and separate baseline/report comparison with a fresh session.
- Disable test automations and stop unused Codespaces at the end of the rehearsal.

Unit tests, lint, JSON/YAML parsing, and a valid lockfile are offline checks, not evidence that
these live steps have passed. Record rehearsal results before promising end-to-end readiness.

**Regression coverage added for rehearsal:** the reproduced encryption/disposal/rights negations,
planned retention, unresolved sub-processor/residency metadata, residency contradiction, unstated
SOC 2 type, and twelve-calendar-month date boundary are tested. Authenticated Dataverse and
token requests reject redirects. This remains a small keyword-based teaching evaluator;
those counterexamples and the three sample scores do not establish general document correctness.
The live Codespaces, product-feature, Dataverse, and deployment gates must still be observed.

## Container Image Readiness

The new website target uses `python:3.12-alpine` and a non-root runtime user. The editor's
base-image check on 16 September reported four High findings and no Critical findings for that
tag. This is not a scan of the finished image or proof of exploitability. Re-scan both final
images by digest and triage findings before live delivery. The vendor image is unchanged.

A read-only Trivy 0.74.0 scan on 2026-09-09 of the Linux AMD64 base in
[Dockerfile](../Dockerfile), `python:3.12-slim`, reported 51 High and 3 Critical package
findings across 18 CVEs, with no fixed versions listed. The compatible Bookworm variant
reported 55 High and 5 Critical findings and did not resolve this issue; the base was not changed.

These are scanner-reported dependency findings, not proof that this application exposes every
vulnerability. The owner must triage them and approve the final image. Record the image digest,
scan date, and results under ignored `rehearsal/results/`; recheck the final built app image,
including its installed dependencies. Passing Python tests or a base-only scan is not a full
container build, application security review, or live deployment check.

## Common failure modes

| Symptom                                        | Check                                                                    | Resolution                                                                                                                                                                  |
| ---------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Codespace creation fails                       | Network and Codespaces policy                                            | Allow required GitHub endpoints and enable Codespaces.                                                                                                                      |
| Copilot icon or agent missing                  | Seat and organization policy                                             | Assign the seat, enable the feature, then reload the Codespace.                                                                                                             |
| `copilot` command not found                    | Container setup step failed                                              | The container installs it from `https://gh.io/copilot-install`. Re-run that command in the terminal, or use `npm install -g @github/copilot`, which needs Node 22 or later. |
| Old duplicate vendor-analyst still appears     | Cached organization discovery                                            | The shared copy is retired; refresh/reload the client. Keep the local workshop analyst used by Lab 06.                                                                      |
| Learner agent or skill missing                 | File location, frontmatter, client                                       | Inspect discovery diagnostics; use skills for Agent Host, not unsupported prompt files.                                                                                     |
| Inline suggestion or model option missing      | Client, language, seat, model and settings                               | Use a prepared example and the current support documentation; do not turn a missing preview into an installation task.                                                      |
| Browser tools missing | Workspace MCP configuration, Linux setup, and effective policy | Use MCP logs and the prepared launcher. Record a blocker if unavailable; never expose an MCP port or disable sandbox/TLS. |
| Plugin listed but its task fails               | Component discovery, tool access and runtime                             | Inspect the actual invoked component and tool error; manifest presence alone is not a successful test.                                                                      |
| AttractionsAgent absent or not Managed         | Entitlement, private-source read access, policy refresh, local shadowing | Inspect source and the actual agent ID. Do not copy it into the learner repo or change enterprise settings live.                                                            |
| Travel site blocks the agent                   | Site access or bot controls                                              | Use another permitted source or clearly labelled fixture; never call the fallback live browsing.                                                                            |
| Packages work but agent cannot reach localhost | Sandbox and runtime prerequisites                                        | Inspect local-network controls and CLI release notes; do not disable enforced boundaries.                                                                                   |
| Cloud task cannot start                        | Access level or agent policy                                             | Grant write access and enable the cloud agent at organization level.                                                                                                        |
| Automations pane missing                       | Repository visibility or organization policy                             | Automations require a private or internal repository and an organization that allows them.                                                                                  |
| Hook appears to hang the agent                 | Hook runtime                                                             | Hooks block execution; keep them under five seconds and set `timeoutSec`.                                                                                                   |
| Agent cannot update protected branch           | Target branch and ruleset                                                | Verify that the task uses its permitted branch. Have the owner approve only the documented exception needed; do not weaken protection during the session.                   |
| Dependency setup fails                         | Registry firewall path                                                   | Allowlist the approved registry endpoints and rebuild the container.                                                                                                        |
| MCP authentication fails                       | Remote URL and browser auth                                              | Use the documented remote URL and confirm the login flow is allowed.                                                                                                        |
| Azure login fails                              | Actions secret and deployment identity                                   | This workflow uses `AZURE_CREDENTIALS`, not OIDC. Verify its access and validity without printing its value.                                                                |
| App deploys but does not start                 | Container port or start command                                          | The container listens on 8000; confirm `--target-port 8000` and check revision logs.                                                                                        |
| Deployment rejected on the name                | `config.json` still says `Your Name`, or the derived name is invalid     | Container App names are lowercase, alphanumeric with hyphens, and 32 characters at most.                                                                                    |

Do not disable certificate verification to work around corporate package restrictions. The
lockfile uses public PyPI URLs; a locally approved mirror belongs in local tooling configuration,
not the committed workshop lock. Check installation from the target Codespace network.

Never request attendee Azure access as a workaround. Escalate service configuration to the
event infrastructure owner. Do not change workshop clock times or invite participants during a code rehearsal.

## Official References

- [Coverage and reference guide](REFERENCES.md): all demonstrations, lab topics, and optional follow-ups.
- [Copilot administration](https://docs.github.com/en/copilot/how-tos/administer-copilot), [policy support](https://docs.github.com/en/copilot/reference/supported-surfaces-for-policies), and [managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings).
- [Codespaces overview](https://docs.github.com/en/codespaces/overview), [Copilot troubleshooting](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-common-issues), and [built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools).
- [Dataverse operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api), [Power Automate integration](https://learn.microsoft.com/power-automate/dataverse/overview), and [Container Apps deployment](https://learn.microsoft.com/azure/container-apps/github-actions).
- [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/) and [VS Code releases](https://code.visualstudio.com/updates): recheck before the event, especially preview demos.
