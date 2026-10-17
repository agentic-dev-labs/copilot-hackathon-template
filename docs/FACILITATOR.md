# Facilitator runbook

Use the [agenda](AGENDA.md) for timing and the [coverage guide](REFERENCES.md) for official
links for the whole week, not a Monday feature checklist. The priority is confidence for
first-time GitHub/app users. Day 1 establishes foundations, Chat, a shared first website, manual
checks, and saved work; Day 2 applies that workflow to participants' own ideas. Since the
14 October refit, Days 3-5 stay just as simple for the same audience: a few more ways to use
Copilot on their own website and choosing an idea (Day 3), build day (Day 4), and presentations (Day 5).
All attendee steps use browser-based Codespaces and its Bash terminal, never a laptop runtime.
Start with 30 minutes of concepts only. After that, show one action for 3-5 minutes, let people
try it for 8-12, then check. Repeat within the published blocks. Do not fill their building
time with additional demonstrations when they are making progress.

## Demonstration preparation

Prepare these results before Day 1 so network waits and preview setup do not consume lab time:

| Block               | Live core                                                                                  | Prepared result or fallback                                                         |
| ------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Monday foundations  | Concepts, glossary, and labelled screenshots from [START-HERE](START-HERE.md); no commands | Point to the same controls in the actual browser-based client                       |
| Monday first work   | Files, Chat, one idea note, save/review/commit/push                                        | Assigned working branch and tested access; no JSON or CLI setup                     |
| Monday page         | /create-website asks only the category; tested blueprint copied and named; live preview panel; Copilot explains selected code and each learner edits the `<h1>` headline by hand | Helper checks the preview helper; no completed page in the source template |
| Monday verification | Check a button and the starter's count (or Weather against its raw data) yourself          | Optional single public figure, not a five-report assignment                         |
| Monday afternoon    | One interaction, personal improvements, a bold change undone with **Undo**, a Copilot-written commit message, a tour of commits and file **History** on GitHub, and the bronze/silver/gold challenge card | Optional sketch-to-design moment (demonstrate it once first); storage and publication only for ready learners with help |
| Tuesday overviews | David first, then Jackie: responsibilities, low-risk uses, approved tools, and shared-data possibilities | No attendee marketplace, database, or connector setup |
| Tuesday building | One own-idea prototype, manual checks, saved work, and questions for IT | `/create-website` own-idea route in `site/ideas/` with fictional local content; Monday's page for people without an idea |
| Wednesday tools | CLI question and one change, the repository's read-only GitHub MCP server, an instructions file and a small skill | Presenter's browser-tools demonstration from VS Code Desktop connected to their Codespace; attendees install nothing; a prepared fallback screen for blocked sign-in or policy |
| Wednesday close | Pick an idea and write its brief; cloud-agent demonstration | Start the demonstration issue early, or show a prepared pull request labelled as prepared |
| Thursday building | Supported building, a 10:45 check-in, own checks, and a written three-minute story | Optional cloud-agent try only where the feature is enabled; nobody blocked waiting for it |
| Friday showcase | Short presentations by table, then the wrap-up | Screen-sharing method, timer, running order, and screenshot backups agreed before 09:30 |

Keep public reports and HTML briefs on the optional [extension shelf](RESEARCH.md), separate
from synthetic vendor evidence. Name tools when they become useful, rather than explaining
models, roles, and execution environments all at once. GitHub Copilot is the focus; Microsoft
365 Copilot and Power Platform are related products, not interchangeable entitlements.

## Room and Novice Pilot

- Preflight the actual attendee account/browser/network path before the event, including the
  assigned repository, Chat, first push, and private preview. A presenter account is not a substitute.
- Avoid 40-45 first-time Codespace creations at 09:30 on Monday. Enable Codespaces prebuilds for
  the attendee repositories, or ask attendees to create their Codespace before 09:00 and leave the
  tab open. A first creation installs dependencies and the preview helper and can take minutes.
- Plan support for **roughly 40-45 attendees**, with the final roster still to be confirmed. Confirm simultaneous Codespace
  capacity, budget, and floor-helper coverage. Aim for one helper per 8-10 beginners in addition
  to the presenter; if staffing is lower, arrange pairs and reduce simultaneous troubleshooting.
- A pair uses one assigned project and rotates the driver. Never ask two people to edit the same
  files concurrently. Prepare unique labels in `config.json` and test branch permissions before class.
- Keep the current action and expected result visible while helping somebody. Use quiet checkpoints:
  found Chat; pushed a note; opened a page; checked a behaviour and number; saved an improvement.
- Provide the [printable quick reference](QUICK-REFERENCE.md). Demonstrate finding the instructions
  and **Open Preview** for Markdown before expecting anyone to read a lab. The guides support
  live instruction; they are not independent reading assignments.
- Confirm table power, screen visibility, and a layout allowing helpers to circulate. Round tables
  and a second instruction screen were discussed, not verified. Print the short sheet if needed.
- Confirm the planned helper coverage with David, Bill, and Jackie, and encourage experienced
  participants to help neighbours without taking over their keyboard. AI experience does not
  necessarily imply GitHub/VS Code experience, even on Days 3-5.
- Keep a labelled completed example in a separate approved rehearsal copy for rescue or demonstration.
  It is not a learner-authored outcome or a replacement for recording a blocked step.
- Pilot the new beginner route with David/Susan and a few genuine first-timers on the intended
  managed-browser path. Record anonymous pilot labels, elapsed time, help needed, and unfinished
  steps. Do not put employee details or screen credentials into evidence.
- The pilot passes only when participants can find Chat, make and inspect a change, open the
  preview, check it, and save/commit/push without the presenter taking over. Adjust instructions
  from observations; a passing automated suite does not establish beginner usability.
- The beginner guide's images are attributed official examples, not workshop captures. During
  preflight compare them with the actual Codespaces UI; capture reviewed training-only replacements
  if the control locations differ materially. Never label a mock-up as an observed interface.

## Current Delivery Checkpoints

Monday uses [START-HERE](START-HERE.md) as the chronological route. The note/Git block at
10:00 and manual verification at 11:45 are outside Labs 00 and 01. Preserve afternoon building
time; no storage or public URL is needed to finish. End with a neighbour seeing one working feature.
Use `/create-website` for the first guided choice: Project Planner, Calendar, Ideas Wall, or
Weather. Demonstrate the Project Planner. It asks only which one, then builds and opens it,
so attendees see how little they need to say. Keep
the sponsor welcome inside the first concepts-only block. Do not introduce a React migration
solely because a starter template was mentioned; framework changes need an explicit decision.

Fresh Codespaces prepare the repository-owned Website preview panel, plus Copilot CLI.
Monday uses that panel, not desktop Chromium, CLI, or any server or port. The learner runs
`/create-website`; after approval the skill copies the tested category blueprint and kit,
personalises it, and opens it beside Chat. Verify a change appears by itself and an added
entry survives it, then `/stop-website` closes the panel and `/start-website` reopens it.
The Python server on 8000 remains for technical examples and deployment.

Do not require diagram tools, paid image generation, or choosing a frontend framework.
The skill provides original CSS, original animated SVG art, a licensed font, and synthetic
starter data. It must preserve existing files and never claim a manual check was done
without the learner's result. Fast finishers build an own idea from one sentence after checking,
saving, and showing the first site, in a new subfolder; slower learners move on to the next lab.
The Weather starter calls Open-Meteo, approved by the owner; its free tier is non-commercial,
and the page shows sample weather if the network blocks it. Weather uses Fahrenheit and mph, and
the Calendar's weeks start on Sunday, for the US audience. In the 11:45 checking block a
facilitator may instead show one value from the official
[five-year overview](https://annualreport.novonordisk.com/2025/introducing-novo-nordisk/five-year-overview.html)
against the labeled [prepared facts](annual-report-facts.json), checking year, unit, and value.
That replaces the count check; it is not a PDF research assignment.

Tuesday gives David 09:00-09:30 for responsibilities and approved-tool context, then Jackie
09:30-10:30 for Power Platform/shared-data examples. Confirm speaker availability. Use
[DAY-2-BUILD](DAY-2-BUILD.md) at 10:45 and throughout the afternoon; no required integration lab
or tools hour. At 14:45, allow two short volunteer demonstrations plus wrap-up or pair sharing,
not five minutes for every attendee. Let people explain how their prototype might help their work.

**Roles (14 October 2026):** Ali presents Day 1, leads Days 3-4, and hosts Day 5. On Day 2, as
agreed with David, Ali does not present: David and Jackie give the overviews and Ali is table
support with the other helpers. Confirm who restarts the room at 10:45 on Day 2 and who hosts the 14:45 demonstrations.

Wednesday follows [the Day 3 guide](TOOLS-PRACTICE.md): CLI 09:00-09:45, [Lab 04](../labs/04-mcp/README.md)
09:45-10:30 (GitHub MCP hands-on, then the presenter's browser-tools demonstration), [Lab 06](../labs/06-teach-copilot/README.md)
10:45-11:30, picking an idea 11:30-12:15, and the [Lab 03](../labs/03-cloud-agent/README.md)
cloud-agent demonstration 12:15-12:30. Every exercise uses the attendee's own website; no vendor
app, database, or extra repository. Thursday follows [the build day guide](DAY-4-BUILD.md) with a
quick check-in at 10:45; protect the building time. Friday follows [the showcase guide](DAY-5-SHOWCASE.md):
about two minutes to show plus one for a question or change-over fits about 40 people across the
two rounds with a short buffer, so present in pairs or by table if the roster is larger. Hooks, automations, multi-agent handoffs,
saved browser tests, CI, and release verification are [post-workshop reference](../post-workshop/advanced/README.md).

## Day 3 Helper Preparation

- Before Day 3, confirm the training accounts may use Copilot CLI, the remote GitHub MCP server,
  and the cloud agent. Check one attendee sign-in path privately. Installed is not signed in.
- **This repository keeps attendees' Copilot to its own tools.** `.vscode/mcp.json` lists only the
  read-only GitHub server. `.vscode/settings.json` sets `chat.mcp.autostart` to `never` (nothing
  starts until an attendee selects **Start** in Lab 04), switches off `chat.mcp.discovery.enabled`
  for every other app (Copilot CLI, Claude, Cursor, Windsurf), and sets `chat.extensionTools.enabled`
  and `chat.plugins.enabled` to `false`, which hides other extensions' chat tools and any agent
  plugin. The devcontainer turns off organization custom agents. VS Code has no repository setting
  that allows only named servers; that allowlist is enterprise policy (`allowedMcpServers` in Copilot
  managed settings). Personal servers in your own VS Code profile are not affected, so before you
  present, run **MCP: List Servers**, pick each personal server, and choose **Disable** for this workspace.
- **Decision, 14 October 2026: the browser check in Lab 04 is a presenter demonstration.**
  Attendees install nothing for it. VS Code's integrated browser and its browser tools are a VS
  Code Desktop feature, so open your Codespace in VS Code Desktop for this demo, keep
  `workbench.browser.enableChatTools` on, and turn on `workbench.browser.enableRemoteProxy`
  (preview) so the browser can reach pages in the Codespace. Rehearse the exact page and steps
  there beforehand. Serve the page privately with
  `uv run uvicorn app.site:app --port 8000` if the tools need a web address, and never make the
  port public. Background: in the owner's Codespace the pinned Playwright browser installed in
  about 40 seconds (`bash .devcontainer/setup.sh browser`) but could not start, because the
  container's default seccomp filter blocks the user namespaces Chromium's sandbox needs. Keep
  that profile for a later owner-approved environment, such as a reviewed
  `"runArgs": ["--security-opt", "seccomp=unconfined"]` tested in a fresh Codespace. Never add
  `--no-sandbox`.
- Start the cloud-agent demonstration issue before 12:15 so its pull request is ready, or show a
  prepared one and say that it is prepared. See [Lab 03](../labs/03-cloud-agent/README.md).
- Never publish MCP or debugger ports, disable the browser sandbox or TLS checks, or print
  credentials. No Dataverse connection, vendor app, or research download is needed today.
- Deeper material lives in the [advanced reference](../post-workshop/advanced/README.md); do
  not add it to today's blocks.

## Helping With Optional Publication (Lab 08)

Learners see a short, optional publish route. Helpers own the checks behind it. Before a learner
dispatches **Actions > Deploy my app**, confirm the unique label in `config.json`, the reviewed
commit on `main`, and deployment access. The workflow keeps its tests, lint, asset validation,
and revision checks, and any required pull-request review still applies. Run these in the
learner's Codespace first:

```bash
uv run python app/config.py --target website
uv run python -m app.site --check
uv run pytest
uv run ruff check .
```

The website target publishes only allowed `site/` assets; Markdown is not served. Limits are
2 MiB per asset, 100 files, and 20 MiB in total. Asset validation is not a full security scan, so
look at JSON and images as well as code. The workflow checks the exact commit and the entry page's
bytes and fingerprint through `/healthz` and the page; a healthy older revision is not this
deployment. Keep the website and vendor targets separate and never select vendor as a workaround.
Publication is checked only when the run succeeded, its verified URL serves the reviewed page, and
the learner's chosen interaction works there. Agree how long it stays online and who removes it;
never delete shared resources.

| Symptom                               | Cause                                             | Fix                                                                                                    |
| ------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Stops on **Read config.json**         | The prepared workshop label is missing            | Check the unique label before retrying.                                                                |
| Deployment rejected on the name       | Derived name is invalid                           | Names are lowercase letters, digits and hyphens, 32 characters at most; `python app/config.py` shows it. |
| The run cannot sign in to Azure       | Organization secrets are missing                  | The owner checks secret access; nothing on the learner's side is wrong.                                |
| Stops on prepared access/commit check | Missing Actions configuration or the branch moved | Check the named settings and retest the exact branch. Never sign into Azure as a workaround.            |
| Page shows the vendor table           | Wrong deployment target or URL                    | Use the website target and its verified run-summary URL; do not overwrite the business app.            |
| Website validation fails              | Missing entry point, invalid asset, or too large  | Inspect `python -m app.site --check`; keep only intentional web assets under `site/`.                  |

## Idea Intake and Handover

Before Tuesday, ask for a short idea description, not a real spreadsheet or business dataset:
audience, task, smallest useful interaction, example fictional fields, and how success can be checked.
Offer project planner, calendar, ideas wall, reading list, or a simple follow-up list examples.
"I do not have an idea yet" is a valid response. Own ideas start with `/create-website` in their
own folder under `site/ideas/` in the same repository, so no extra repository is needed. People
without an idea continue the Monday page. Never overwrite their work.

Susan coordinates idea collection and the final attendee list; the meeting planned training
invitations for the week before the event, after policy approval. Use a small approved pilot group
for earlier testing. Do not bulk-invite or provision identities as part of content maintenance.
The next content review discussed was **Monday 28 September 2026**, with Susan sending the invite
and David bringing his overview material; this note does not assert a calendar invitation exists.

The reported 09:00-16:00 attendee invitation differs from the published 09:00-15:00 beginner
days. Confirm the finish time rather than silently extending the timetable. The proposed corporate
repository/desktop/AI-marketplace transition is not rehearsed or approved by these notes. Keep
attendee work Codespaces-only until an explicit change is approved and the target is tested.
Familiar menus do not imply identical runtimes, extensions, authentication, or policy coverage.

Never treat Codespaces as a policy bypass or a guarantee that actions cannot affect external
systems. Preserve work and confirm access for all remaining days before any approved membership
cleanup; never delete personal GitHub accounts. Use the
[post-workshop technical reference and prompts](../post-workshop/dataverse/README.md) to plan
the later real-work data/integration project with the technical owner, not during beginner building.

Show how to stop or steer work as well as how to start it. Agent edits can be applied directly:
inspect the actual diff and restoration controls rather than promising a universal approval
dialog. Checkpoints are temporary workspace recovery, not Git history or an undo for external writes.

The [specialist topics](REFERENCES.md#optional-possibilities-and-specialist-topics) are a
reference shelf: SDK, other IDEs, migrations, BYOK, integrations, parallel execution, and
administration do not add prerequisites to Monday. Use the
[daily small tasks](REFERENCES.md#small-tasks-for-early-finishers) for early finishers.

## Organization setup

1. Confirm all items in [PREREQS.md](PREREQS.md).
2. Verify Copilot CLI, cloud-agent, Codespaces, and remote GitHub MCP availability in the event organization.
3. Grant the required repository access. Test branch rules and use only the bypass permissions the cloud workflow actually requires.
4. Provision the shared Azure resources once: resource group, Container Apps environment, and container registry. See [PREREQS.md](PREREQS.md) for the provisioned names.
5. Configure Actions and Codespaces service access separately as listed in [PREREQS.md](PREREQS.md).
   `scripts/create_attendee_repos.py` creates repositories and team grants, not credentials.
6. Switch on [AI pictures and chat](#ai-pictures-and-chat) before Monday's Lab 02.

## AI pictures and chat

Lab 02's optional picture, the `/make-image` skill attendees write in Lab 06, and the prepared
`/add-chat` skill use the facilitator's Microsoft Foundry resource through one **workshop
identity**: an Entra ID app registration with only the **Cognitive Services OpenAI User** role on
that resource. It can draw and chat, but cannot read keys or change anything. No API key is used.

1. Store four **organization Codespaces secrets** with access for private repositories:
   `FOUNDRY_TENANT_ID`, `FOUNDRY_CLIENT_ID`, `FOUNDRY_CLIENT_SECRET`, and `FOUNDRY_RESOURCE` (the
   resource name only). Attendee repositories are private, so their Codespaces receive them. The
   public template does not: add the same four as your own personal Codespaces secrets for it.
2. Secrets arrive when a Codespace starts, so stop and restart it after any change. The restart
   also installs a newer Website preview; a window that is already open needs one
   **Developer: Reload Window** for that.
3. In the terminal, `python3 scripts/workshop_ai.py status` reports `"ok": true`. Then add
   `/add-chat` to a practice page and get one answer from **Ask**.

For a picture, Copilot runs `scripts/workshop_ai.py`, which signs in as the workshop identity,
draws with the first model that has capacity, and saves the file under `site/`. For the chat, the
page's **Ask** button hands the question and the page's visible text to the Website preview,
which asks the chat model and shows the answer. The page holds no credential and makes no network
call, and a published copy says the chat is switched off. Page text is treated as data, not
instructions, and attendees still check every answer.

Capacity tested on 17 October 2026 for about 45 people:

| Feature          | Models, in order                                            | Speed                                          |
| ---------------- | ----------------------------------------------------------- | ---------------------------------------------- |
| New picture      | FLUX-1.1-pro and FLUX.1-Kontext-pro, then gpt-image backups | 2-4 seconds; about 60 a minute before backups  |
| Change a picture | FLUX.1-Kontext-pro, then gpt-image-1.5                      | A few seconds                                  |
| Ask my page      | gpt-5.6-luna, then gpt-5.5                                  | 1-2 seconds; 20 questions a minute per page    |

When everyone draws at once, the helper retries once and then says "busy": wait a minute.
Content filters block unsuitable requests with a plain message.

After the workshop, and before the client secret expires on 1 November 2026, delete the four
organization secrets, your personal copies, and the app registration.

## Governance repository

The private repository `agentic-dev-labs/.github-private` now supplies managed settings and
the plugin marketplace. The outdated organization vendor-analyst was removed with owner
approval on 2026-09-09. Keep the correct local analyst/writer/reviewer for the
[advanced post-workshop reference](../post-workshop/advanced/agent-authoring-handoffs.md).

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

**Optional later specialist:** [attractions plugin](https://github.com/agentic-dev-labs/.github-private/tree/main/plugins/attractions).
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

For an optional later document-tool demo, use `copilot plugin install assurance-toolkit@agentic-dev-labs`
after confirming it appears in the marketplace. Inspect its agent, skills, and document-conversion
MCP configuration. Use a synthetic document and verify a quotation; do not promise that every
PDF failed before installation or that every converted file has reliable page provenance.
The toolkit is an optional presenter install, separate from the core labs. Verify its actual
tool permissions, runtime dependencies, and client support in the governance repository.
Keep this optional toolkit separate from Wednesday's prepared browser connection. A verified transcript
is a presenter fallback, not evidence that the attendee's plugin actually worked.

## Create team repositories

Repository secrets are **not** copied from a template. The script creates private repositories
and grants the configured attendee team write access. It first inspects the selected template
and stops if facilitator preparation files are present or the inspection fails.

The template no longer tracks `.facilitator/`: the notes stay in the owner's Codespace and are
git-ignored, though earlier commits still contain them. The template also ships no finished
website or learner-made skills, so every attendee starts from the same empty `site/`. CI fails
on the template repository if learner work is committed there. A demo website you build in the
template's own Codespace stays out of Source Control automatically (a local Git exclude, not
`.gitignore`, which attendee copies inherit); clear it with `/workshop-reset`. The script's own
check confirms the template is clean before it copies anything:

```shell
python scripts/create_attendee_repos.py nn-na-2026-10-team-01 nn-na-2026-10-team-02
```

Re-running reuses existing repositories and reapplies the team grant. It does not create
identities, issue credentials, buy seats, or configure secret access. Template changes also do
not automatically update team repositories that already exist.

1. Confirm the approved, note-free source is flagged as a template.
2. Run the script with the repository names you need.
3. Verify the team grant and set one unique workshop label/app name in each repository's config
   before the novice session. Have the owner commit/push that preparation through normal review.
4. Apply and test review rules. Configure Actions access for approved publication, not Dataverse
  secrets for beginner repositories. Database credentials are separate post-workshop preparation.
5. Run CI once and create a Codespace in each repository.

## Dry run

Use the [full Codespaces rehearsal package](../rehearsal/README.md) and `/rehearse-workshop`
to execute the labs in a dedicated copy. It records live evidence separately from test results,
checks a fresh package install, and verifies the exact deployed commit. No attendee Azure login
is required; repository access to the prepared Actions identity must already exist.

- Create a Codespace from a test team repository on the corporate network.
- Confirm extensions install and `uv sync --locked --extra dev --extra web` succeeds.
- Confirm the workshop preview helper is active and `copilot --version` responds without
  requiring a learner installation. CLI sign-in is separate; check it before Day 3.
- Inspect the devcontainer: Python version, dependency lock, minimum host requirements, shared editor settings, and forwarded port. Extension IDs are not version pins; CLI authentication is separate.
- Run tests and the sample CLI end to end.
- Use `--as-of 2026-10-26` to confirm sample scores 10, 8, and 2, plus exact source quotations.
- Complete the first-note save/review/commit/push journey through the browser UI and read back
  the changed file on GitHub. Check the current screenshots and labels against that client.
- Invoke `/create-website` in a new session; verify it asks only which of the four websites,
  builds straight away with the repository name, and preserves an existing page.
  Let creation open the Website preview automatically; change a heading and CSS, and observe
  both update with an added entry kept. Do not substitute an HTTP check
  for actual panel rendering or slash-command discovery.
- Verify `/stop-website` closes only the Website preview panel and `/start-website`
  reopens the same saved page automatically. Check a missing file, an already-running preview, an already-stopped
  server, and a separate own-idea page; no recreation, deletion, or unrelated process termination.
- In Lab 02, choose the learner's existing category, ask for one appearance change and one
  feature change, and verify the matching manual example. Do not repeat the creation interview.
- Manually check an interaction and a source figure, record honest results, save/push, and show
  a helper. Test an own-idea extension without losing the first page. Do not ship the finished
  rehearsal website in the source template.
- Rehearse stop/steer and inspection on a disposable small change. Keep Monday to these essentials.
- In VS Code in the browser (Codespaces), rehearse the four Monday additions: Chat explains
  selected lines in `site/index.html` and a hand edit of the `<h1>` headline updates the preview;
  **Keep** and **Undo** appear after a Copilot change and **Undo** restores the page; the
  **sparkle icon** in Source Control writes a commit message; and the commit list, a commit's
  changes, and the file **History** are easy to find on GitHub.
- Rehearse the optional sketch moment: drag `docs/images/sketch-example.png` from the Explorer
  into Chat with the model attendees will use. Image input depends on the model and policy; if
  Copilot cannot see pictures, keep it as a presenter demonstration or skip it.
- Before Day 3, verify the preinstalled CLI and its authentication separately; rerun
  `bash .devcontainer/setup.sh cli` only if repair/reinstall is needed.
- Only if selected, follow [the optional research guide](RESEARCH.md), prepare its separate
  profile, and record live downloads/conversion versus labelled prepared facts. Test visual-brief
  and any selected community skill in Linux without overwriting the learner's existing page.
- Check CLI sandbox/local-network support in the exact Codespace. Current Linux versions may
  require networking helpers and `/dev/net/tun`; inspect effective `/sandbox` settings and the
  official CLI release notes. Package downloads alone do not prove agent access. Do not bypass policy.
- Check the synthetic Space's sources and permissions; do not attach the whole repository or facilitator notes.
- Rehearse the Day 3 CLI block in a fresh attendee-style Codespace: sign in to Copilot CLI with
  `/login` and the device code, ask about the page, and watch one approved change appear in the
  preview.
- Assign the Lab 03 demonstration issue to Copilot and verify one reviewed, merged, pulled, and
  previewed result. Note how long the session takes so the 12:15 demonstration can start early.
  Check current limits instead of relying on a historical session cap. If attendees will try it on
  Day 4, confirm the **Website change for Copilot** issue template and Copilot assignment in their repositories.
- In a fresh attendee-style Codespace, confirm no MCP server runs on Day 1 and that the Agent's
  **Configure Tools** list shows no Python, pull-request, Pylance, Azure, or plugin tools. Then
  select **Start** on the `github` server in `.vscode/mcp.json`
  (`https://api.githubcopilot.com/mcp/readonly`), sign in, and confirm no write tools appear.
  Attendees get only this server from the repository. If an enterprise-managed plugin or tool still
  appears, an organization policy is overriding the workspace settings; check it with the owner.
- Rehearse the presenter's Lab 04 browser demonstration with VS Code's built-in browser tools,
  from VS Code Desktop connected to the presenter's Codespace (the integrated browser is a desktop
  feature): open a page, read its title, add an item, and report the count. Disable personal MCP
  servers in that workspace so the room sees the same tool list as attendees.
  Attendees run no browser setup. Playwright MCP stays for a later owner-approved environment,
  because Chromium's sandbox could not start in a default Codespace on 14 October 2026; see the
  [Day 3 helper notes](#day-3-helper-preparation).
- Run Lab 06 in a private copy that receives the FOUNDRY_* secrets: an instructions file under
  `.github/instructions/` applied to `site/`, a learner-written `make-image` skill that runs
  `scripts/workshop_ai.py` and puts the picture in the page, and the ready-made `/add-chat` with one
  answer checked against the page. See [AI pictures and chat](#ai-pictures-and-chat).
- Rehearse Tuesday's own-idea brief, bounded prototype, manual journey, save/push, and handover
  questions using fictional app-local content. Do not substitute a database exercise or tool call.
  Confirm `/create-website` offers the own-idea route when a page already exists.
- For optional publication (Lab 08), dispatch the intended **website** target with
  **connect_dataverse** unchecked. Verify the exact commit, URL, and interaction, plus website
  bytes/fingerprint. A healthy container alone is not a checked feature. Preserve all deployment
  guards and human approvals.
- Rehearse Friday's logistics: screen sharing in the room, the timer, the running order, and a
  pair or table fallback if the roster is larger than about 40.
- Stop unused Codespaces at the end of the rehearsal.

Unit tests, lint, JSON/YAML parsing, and a valid lockfile are offline checks, not evidence that
these live steps have passed. Record rehearsal results before promising end-to-end readiness.

**Regression coverage added for rehearsal:** the reproduced encryption/disposal/rights negations,
planned retention, unresolved sub-processor/residency metadata, residency contradiction, unstated
SOC 2 type, and twelve-calendar-month date boundary are tested. Authenticated Dataverse and
token requests reject redirects. This remains a small keyword-based teaching evaluator;
those counterexamples and the three sample scores do not establish general document correctness.
The live Codespaces, product-feature, and selected deployment gates must still be observed.
Live Dataverse checks are tracked separately if the post-workshop reference session is approved.

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
| `copilot` command not found | CLI profile not prepared | Before Day 3, the helper runs `bash .devcontainer/setup.sh cli` and verifies sign-in. This is not a Monday/Tuesday blocker. |
| Old duplicate vendor-analyst still appears     | Cached organization discovery                                            | The shared copy is retired; refresh/reload the client. Keep the local analyst used by the advanced reference.                                                                      |
| Learner agent or skill missing                 | File location, frontmatter, client                                       | Inspect discovery diagnostics; use skills for Agent Host, not unsupported prompt files.                                                                                     |
| Inline suggestion or model option missing      | Client, language, seat, model and settings                               | Use a prepared example and the current support documentation; do not turn a missing preview into an installation task.                                                      |
| Browser tools missing in the presenter demo    | Client support and effective policy                                      | Use the rehearsed fallback screen. Record a blocker if unavailable; never expose an MCP port or disable sandbox/TLS.                                                       |
| Browser profile: Chromium sandbox cannot start | Container seccomp blocks user namespaces                                 | Expected in a default Codespace; attendees do not run this profile. Never add `--no-sandbox`; see the Day 3 helper notes.                                                   |
| Setup did not add `playwright` to `.vscode/mcp.json` | The file had comments, another shape, or a different playwright entry | Read the message; nothing was overwritten. Add only the entry from `.devcontainer/mcp.example.json` and keep the others. |
| Copilot missing from an issue's Assignees | Cloud agent not enabled for that repository or account | Enable it for the demonstration repository; attendees skip the optional Day 4 try rather than wait. |
| Plugin listed but its task fails               | Component discovery, tool access and runtime                             | Inspect the actual invoked component and tool error; manifest presence alone is not a successful test.                                                                      |
| AttractionsAgent absent or not Managed         | Entitlement, private-source read access, policy refresh, local shadowing | Inspect source and the actual agent ID. Do not copy it into the learner repo or change enterprise settings live.                                                            |
| Travel site blocks the agent                   | Site access or bot controls                                              | Use another permitted source or clearly labelled fixture; never call the fallback live browsing.                                                                            |
| Packages work but agent cannot reach localhost | Sandbox and runtime prerequisites                                        | Inspect local-network controls and CLI release notes; do not disable enforced boundaries.                                                                                   |
| Cloud task cannot start                        | Access level or agent policy                                             | Grant write access and enable the cloud agent at organization level.                                                                                                        |
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
- [Copilot administration](https://docs.github.com/en/copilot/how-tos/administer-copilot), [policy support](https://docs.github.com/en/copilot/reference/supported-surfaces-for-policies), and [managed settings](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started).
- [Codespaces overview](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces), [Copilot troubleshooting](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-common-issues), and [built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools).
- [Dataverse operations](https://learn.microsoft.com/power-apps/developer/data-platform/webapi/perform-operations-web-api), [Power Automate integration](https://learn.microsoft.com/power-automate/dataverse/overview), and [Container Apps deployment](https://learn.microsoft.com/azure/container-apps/github-actions).
- [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/) and [VS Code releases](https://code.visualstudio.com/updates): recheck before the event, especially preview demos.
