# Facilitator runbook

Use the [agenda](AGENDA.md) for timing and the [coverage guide](REFERENCES.md) for official
links for the whole week, not a Monday feature checklist. The priority is confidence for
first-time GitHub/app users. Day 1 establishes foundations, Chat, a shared first website, manual
checks, and saved work; Day 2 applies that workflow to participants' own ideas. Days 3-5 follow
David's final slides (20 October 2026): attendees turn their idea into tickets on a project board,
write a User Requirements agent that adds acceptance criteria, and build and test one ticket
(Day 3), delegate the next ticket to the cloud agent and review it with their own Code Review
agent (Day 4), and run CI/CD with an approval gate and a rollback (Day 5). Every step is a plain
sentence typed to Copilot CLI or a click, on the attendee's own website.
All attendee steps use browser-based Codespaces and its Bash terminal, never a laptop runtime.
Start with the 09:00-09:30 block: the sponsor welcome (SEFR video) and the ASTER Overview teaser
(HZRW), then your GitHub tour, concepts only. After that, show one action for 3-5 minutes, let people
try it for 8-12, then check. Repeat within the published blocks. Do not fill their building
time with additional demonstrations when they are making progress.

## Demonstration preparation

Prepare these results before Day 1 so network waits and preview setup do not consume lab time:

| Block               | Live core                                                                                  | Prepared result or fallback                                                         |
| ------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Monday foundations  | Welcome, SEFR video and ASTER teaser; then on github.com: GitHub, a repository, and the README's five words, shown on the template while attendees watch; no commands | Org settings that let attendees create private repositories, tested with an attendee-like account; `scripts/create_attendee_repos.py` for anyone who cannot |
| Monday first work   | From the README at 09:30: everyone's own private copy via **Use this template**, Codespace, Chat; at 10:00 the first website, whose idea note is `site/brief.md`, then save/review/commit/push | Assigned working branch and tested access; no JSON or CLI setup                     |
| Monday page         | 10:00: /create-website asks only the category; tested blueprint copied and named; live preview panel. 10:45: more websites shown; Copilot explains selected code; each learner edits the `<h1>` headline by hand and builds one own idea in its own folder | Show the extra websites from a separate demo repository, built beforehand and labelled as prepared; build one live. Helper checks the preview helper; no completed page in the source template |
| Monday verification | Check a button and the starter's count (or Weather against its raw data) yourself          | Optional single public figure, not a five-report assignment                         |
| Monday afternoon    | A chart with `/add-chart` (or `/add-chat` or a picture) checked against the entries, personal improvements, a bold change undone with **Undo**, a Copilot-written commit message, a tour of commits and file **History** on GitHub, and the bronze/silver/gold challenge card | Optional sketch-to-design moment (demonstrate it once first); storage and publication only for ready learners with help |
| Tuesday overviews | David first, then Jackie: responsibilities, low-risk uses, approved tools, and shared-data possibilities; Bill Leeson's Building a Project Brain talk at 11:45-12:15 | No attendee marketplace, database, or connector setup |
| Tuesday building | One own-idea prototype, manual checks, saved work, and questions for IT | `/create-website` own-idea route in `site/ideas/` with fictional local content; Monday's page for people without an idea |
| Wednesday agents | Two or three **Requirement** tickets (from Tuesday's **Next** wishes) and a Board project named after the attendee that imports the repository; Copilot CLI `/login`; a GitHub tool lists the tickets (MCP); at 00:50 the four building blocks, then the **user-stories** skill and the User Requirements agent written from the guide's prompts; criteria added to each ticket with `gh` and validated; approved tickets dragged to **Todo**; one built in the Codespace; `pytest checks` green; the brief lists the requirements; a `Closes #N` commit moves it to **Done** | A demo website with its tickets and board ready, and a rehearsal copy with the skill and agent, labelled as prepared, for anyone whose CLI sign-in is blocked; pasting the agent's draft into the ticket when `gh` may not update it |
| Thursday cloud agents | A 5-minute presenter demo: an automation adds criteria to a new demo ticket by itself; the `Protect main` ruleset (pull requests only); the `version:` line switched on and shown in the footer; an approved ticket from the board assigned to Copilot; review rules and the Code Review agent; `@copilot` iteration; merge and deploy with the next version, the ticket **Done** | The criteria automation set up on the demo repository the day before (it runs as you, on your allowance); assign the demonstration ticket before the session so a pull request is ready; Copilot assignable in attendee repositories. Copilot code review stays off: no Copilot review appears on attendee pull requests |
| Friday CI/CD | Starter checks (tests and the UI check) with edited triggers and permissions, then required; a red UI check with its phone screenshot, then green; `training` approval; smoke test and **Revert**; demos; HANDOFF.md | A rehearsal copy with each step done, for showing a blocked step; the template CI's `ui-check` job green on `main` |

Keep public reports and HTML briefs on the optional [extension shelf](RESEARCH.md), separate
from synthetic vendor evidence. Name tools when they become useful, rather than explaining
models, roles, and execution environments all at once. GitHub Copilot is the focus; Microsoft
365 Copilot and Power Platform are related products, not interchangeable entitlements.

## Room and Novice Pilot

- Preflight the actual attendee account/browser/network path before the event, including
  creating a private repository from the template in agentic-dev-labs, Chat, first push, and
  private preview. A presenter account is not a substitute.
- Repositories made at 09:30 start their Codespaces from the ready-made image (see the
  [Codespaces setup](../.devcontainer/README.md#ready-made-image)), not from prebuilds, which
  belong to one repository. Measured on 19 October 2026, a fresh Codespace was ready in about
  50 seconds. Attendees click **Create codespace** right after making their repository, so it loads
  while you explain the repository. VS Code then asks **Do you trust the authors of the files in this folder?**;
  attendees choose **Trust Folder & Continue**, or the Website preview helper is not installed.
  Confirm concurrent capacity, and have helpers watch for stuck creations.
- Plan support for **roughly 40-45 attendees**, with the final roster still to be confirmed. Confirm simultaneous Codespace
  capacity, budget, and floor-helper coverage. Aim for one helper per 8-10 beginners in addition
  to the presenter; if staffing is lower, arrange pairs and reduce simultaneous troubleshooting.
- A pair uses one project, the driver's repository, and rotates the driver; a helper adds the
  partner under **Settings > Collaborators and teams**. Never ask two people to edit the same
  files concurrently. A website name in `config.json` is needed only for optional publication.
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

Monday morning runs from the repository [README](../README.md#monday-morning-follow-along): it is
the first thing attendees see on their repository's GitHub page, so nobody has to find a guide
before 10:30. Create your own copy live alongside the room, so your screen matches
theirs. Each block is interactive: show one step, attendees do it on their own repository
alongside you or straight after, then the next step.

| Time        | You show                                                                                       | Attendees do                                               |
| ----------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 09:00-09:30 | After the welcome, SEFR video and ASTER teaser: this is GitHub; this is a repository (the template's files, README, Commits, History, Search, Issues); the five words and save -> review -> commit -> push | Watch; no commands |
| 09:30-10:00 | **Use this template > Create a new repository** with owner agentic-dev-labs, your username as the name, and **Private**; your new copy (files, README, one commit); **Code > Codespaces > Create codespace on main**; **Trust Folder & Continue**; README with **Open Preview**; Chat in **Ask**; `/next-word` with "What a nice day, let's go to the", then "What a nice day here in Princeton, New Jersey, let's go to the", the room guessing first (its percentages are Copilot's own estimate); one question and one refinement | Make their own private copy with you, check the owner and **Private** label, open its Codespace, try `/next-word` on the first sentence, then each step straight after you |
| 10:00-10:30 | Chat in **Agent**; `/create-website` with the Project Planner; the preview beside Chat; `site/brief.md`, the idea note it wrote; **File > Save All**; Source Control with every file staged; commit; push; find it on GitHub | The same, then helpers check every page is on GitHub       |
| 10:45       | More websites from your prepared demo repository, one built live; then [START-HERE](START-HERE.md) is the route | Lab 01 step by step: headline by hand, one own idea in its own folder |

The sponsor welcome, SEFR video and ASTER teaser share the 09:00-09:30 block, so confirm their
running time with David and use the rest for the tour. If the 09:30 block runs over, finish the
first website in the break with helpers rather than shortening Lab 01. The 11:45 manual
verification is outside Lab 01. Preserve afternoon building
time; no storage or public URL is needed to finish. End with a neighbour seeing one working feature.
Use `/create-website` for the first guided choice: Project Planner, Calendar, Ideas Wall,
Weather, Princeton Map, Photo Studio, or My own idea. Demonstrate the Project Planner. It asks
only which one, then builds and opens it,
so attendees see how little they need to say. Do not introduce a React migration
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
without the learner's result. At 10:45 everyone builds one own idea from one sentence, in a
new subfolder, after the first site is saved on GitHub; the first site stays in place.
The Weather starter calls Open-Meteo, approved by the owner; its free tier is non-commercial,
and the page shows sample weather if the network blocks it. Weather uses Fahrenheit and mph, and
the Calendar's weeks start on Sunday, for the US audience. In the 11:45 checking block a
facilitator may instead show one value from the official
[five-year overview](https://annualreport.novonordisk.com/2025/introducing-novo-nordisk/five-year-overview.html)
against the labeled [prepared facts](annual-report-facts.json), checking year, unit, and value.
That replaces the count check; it is not a PDF research assignment.

Tuesday gives David 09:00-09:30 for responsibilities and approved-tool context, then Jackie
09:30-10:30 for Power Platform/shared-data examples, and Bill Leeson 11:45-12:15 for Building a
Project Brain, as on David's slide. Confirm speaker availability. Use
[DAY-2-BUILD](DAY-2-BUILD.md) at 10:45 and throughout the afternoon; no required integration lab
or tools hour. The morning build is one hour, so everyone saves a first version before Bill's
talk. At 14:45, allow two short volunteer demonstrations plus wrap-up or pair sharing,
not five minutes for every attendee. Let people explain how their prototype might help their work,
and make sure everyone writes two or three **Next** wishes in their brief: Wednesday's tickets.

**Roles (20 October 2026):** Ali presents Day 1. On Day 2, as agreed with David, Ali does not
present: David, Jackie, and Bill Leeson give the talks and Ali is table support with the other
helpers. Day 3 opens with MUKQ, then Ali; Ali leads Days 4 and 5. Confirm who restarts the room
at 10:45 on Day 2 and who hosts the 14:45 demonstrations.

Days 3-5 are four hours each, written as elapsed times exactly as on David's slides; confirm each
start time with the organizers. Wednesday follows [the Day 3 guide](TOOLS-PRACTICE.md): tickets,
the board, and agent roles 00:20, the User Requirements agent 00:50, criteria on the tickets
01:45, the build lab 02:30, tests 03:15, and the checkpoint 03:45. In every block show the step
on your demo website, then attendees do the same on their own idea. Thursday follows [the Day 4 guide](DAY-4-BUILD.md), with the
delegation lab in [Lab 03](../labs/03-cloud-agent/README.md). Friday follows [the Day 5 guide](DAY-5-SHOWCASE.md);
team demos run by table, about three minutes each. Every exercise uses the attendee's own website;
no vendor app, database, or extra repository. Hooks, automations, multi-agent handoffs, saved
browser tests, and the vendor app's release verification are [post-workshop reference](../post-workshop/advanced/README.md).

## Day 3 Helper Preparation

- Before Day 3, confirm the training accounts may use Copilot CLI, custom agents, and the cloud
  agent. Check one attendee sign-in path privately. Installed is not signed in.
- **Tickets and the board are plain GitHub.** Attendees write two or three tickets with the
  **Requirement** issue template, starting from the **Next** wishes they wrote in their brief on
  Tuesday, then create an organization project: the organization's name, **Projects > New
  project > Board**, named after themselves (`<username> website`, because all boards share the
  organization's Projects list), **Import items from repository**. Importing makes the repository
  the board's default, so it also appears in the repository's **Projects** tab, and adds the
  existing tickets and every new one; the board's default workflows set closed tickets and merged
  pull requests to **Done**. Todo means approved. Only people with access to a private repository
  can read its tickets on any board. Before Wednesday, create one board this way with
  an attendee-style account: confirm the members may create projects, where new tickets land, and
  that a `Closes #N` commit pushed to `main` moves its card to **Done**. If importing is missing,
  add cards with **+ Add item** and `#`.
- **The agent updates tickets with `gh`.** Copilot CLI's built-in GitHub tools read by default and
  do not write, so the User Requirements agent runs `gh issue edit` in the Codespace, with the
  Codespace's own token, after the attendee agrees. Confirm in an attendee-style Codespace that
  `gh issue edit` may change a ticket; if it is refused, attendees paste the agent's draft into
  the ticket themselves (**...** > **Edit**). Never ask anyone for a personal token.
- **Days 3-5 run on Copilot CLI and files the attendee writes.** The guides give plain-English
  prompts; Copilot writes the `.github/skills/user-stories/` skill and
  `.github/agents/user-requirements.agent.md` (Day 3), then `.github/instructions/review.instructions.md`
  and `code-review.agent.md` (Day 4). Copilot CLI reads agents and skills when it starts, so after
  creating one the attendee types `/exit` and `copilot`. The agent also appears in VS Code Chat's
  agent picker. The template ships only the `checks/` test helper, the **Requirement** and
  **Website change for Copilot** issue templates, the Day 5 starters in `.github/workflow-starters/`,
  `scripts/ui_check.py`, and `scripts/smoke_test.py`; CI keeps learner agents, skills,
  instructions, tests, reviews and HANDOFF.md out of the template.
- **Day 4 changes how everyone saves.** The `Protect main` ruleset makes every later change a
  branch and a pull request, including `/publish-website`, which therefore runs first if a
  website has no address yet. Copilot code review stays switched off (decided 21 October 2026):
  attendees review with their own Code Review agent and their own eyes. Required approvals stay
  at 0: attendees are alone in their repositories. Attendees are admins of their own copies, so
  they can create rulesets; leave the bypass list empty so the rules apply to them too.
- **People join partway through.** Days 3-5 continue with the people from Days 1-2 who want to
  take their own idea further (owner's call, 21 October 2026), so expect a smaller group, and some
  will skip a day.
  The top of the Day 4 and Day 5 guides has a 5-minute catch-up: on Day 4 one ticket written by
  hand with Chat's help, on Day 5 an address with `/publish-website` and the ruleset. Helpers do
  the catch-up with newcomers during the 00:00-00:20 talk.
- **The "agent that starts by itself" demo (Day 4, 00:00-00:20).** The day before, set up the
  automation from Lab 03's optional extras on your demo repository, after its user-stories skill
  is on `main`. At about 00:05 open a new **Requirement** ticket; by 00:15 the story and criteria
  are on it, or waiting as a suggested change. It runs as you and uses your Copilot allowance;
  switch it off after the session.
- **The version on the page comes from the publisher.** Switching on `version:` in the caller
  passes `1.0.<run number>`; the template's publisher writes `version.json` into the site before
  building the image, and the content fingerprint ignores that file, so a Day 5 rollback shows the
  known-good fingerprint with a higher version. Both changes take effect only from the template's
  `main`: after pushing them, publish one practice website with the version switched on and check
  its footer and `/healthz` before Thursday.
- **Days 4-5 need workflow-file pushes.** Attendees edit `publish-website.yml` on Day 4 and copy
  starters into `.github/workflows/` on Day 5, always on a branch. Confirm in an attendee-style
  Codespace that the push is accepted; if the Codespace token refuses workflow files, the fallback
  is GitHub's web editor (the pencil icon, or **Add file > Create new file**) committing to a new
  branch. The approval step uses the attendee's own `training` environment; required reviewers
  in private repositories need the organization's GitHub plan, which agentic-dev-labs has.
- **The UI check runs in GitHub Actions only.** Chromium cannot start in a default Codespace, so
  `scripts/ui_check.py` runs on the runner with `playwright==1.64.0` from PyPI, software graphics
  for 3D pages, and the browser sandbox on: one step lets the throwaway runner use the user
  namespaces Ubuntu 24.04 blocks by default. It checks the first page and up to five idea pages on
  a desktop and a 390-pixel phone, and keeps `home-desktop.png` and `home-phone.png` as single,
  unzipped artifacts. The template CI's `ui-check` job runs the same steps on the Project Planner
  starter; on 21 October every starter and own-idea pattern passed it locally.
- **This repository keeps attendees' Copilot to its own tools.** `.vscode/mcp.json` lists only the
  read-only GitHub server. `.vscode/settings.json` sets `chat.mcp.autostart` to `never` (nothing
  starts until an attendee selects **Start** in Lab 04), switches off `chat.mcp.discovery.enabled`
  for every other app (Copilot CLI, Claude, Cursor, Windsurf), and sets `chat.extensionTools.enabled`
  and `chat.plugins.enabled` to `false`, which hides other extensions' chat tools and any agent
  plugin. The devcontainer turns off organization custom agents. VS Code has no repository setting
  that allows only named servers; that allowlist is enterprise policy (`allowedMcpServers` in Copilot
  managed settings). Personal servers in your own VS Code profile are not affected, so before you
  present, run **MCP: List Servers**, pick each personal server, and choose **Disable** for this workspace.
- **Decision, 14 October 2026: the browser check in Lab 04 is a presenter demonstration**, now an
  optional extra. Attendees install nothing for it. VS Code's integrated browser and its browser
  tools are a VS Code Desktop feature, so open your Codespace in VS Code Desktop for this demo, keep
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
- On Day 4, assign the demonstration ticket before the session so its pull request is ready, or
  show a prepared one and say that it is prepared. See [Lab 03](../labs/03-cloud-agent/README.md).
- Never publish MCP or debugger ports, disable the browser sandbox or TLS checks, or print
  credentials. No Dataverse connection, vendor app, or research download is needed today.
- Deeper material lives in the [advanced reference](../post-workshop/advanced/README.md); do
  not add it to today's blocks.

## Helping With Optional Publication (Lab 08)

Learners type `/publish-website`, accept or type a name, and push. That push runs **Actions >
Publish my website**, which calls the template's
[publisher](../.github/workflows/website-publisher.yml) and puts `site/` on the shared Container
Apps environment in about three minutes. Every later push of `site/` updates it. Nobody signs in
to Azure and no secret exists: Azure trusts only the template's publisher on `main`, through
GitHub's signed token. [infra/README.md](../infra/README.md) explains the trust, lists the
websites, and tears them down. Facilitators can preset a name for a repository with the Actions
variable `WEBSITE_NAME`; `websiteName` in `config.json` wins when both are set.

The publisher takes only allowed `site/` assets; Markdown is not served. Limits are 2 MiB per
asset, 100 files, and 20 MiB in total. Asset validation is not a full security scan, so look at
JSON and images as well as code. The run checks the exact commit, the site fingerprint, and the
entry page's bytes through `/healthz` and the page; a healthy older revision is not this
publication. Each website is tagged with its repository ID: a repository can update or remove only
its own, and choosing a new name removes its old address. Publication counts only when the run
succeeded, the link serves the reviewed page, and the learner's chosen interaction works there.
Pages are public to anyone with the link and stay online until the agreed teardown.

| Symptom                                   | Cause                                                  | Fix                                                                                                    |
| ----------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| Green run with **Not published yet**      | No `websiteName` in `config.json` and no variable      | Run `/publish-website`, then push.                                                                     |
| Green run with **Nothing to publish yet** | `site/index.html` does not exist                       | Create the website first with `/create-website`.                                                       |
| **That name is taken**                    | Another repository owns the name                       | Run `/publish-website` again and choose another name.                                                  |
| Stops on the website name                 | Not 2-32 lowercase letters, digits and hyphens         | Run `/publish-website`; it writes a valid name.                                                        |
| **Sign in to Azure** fails                | Not on `main`, a copy outside the organisation, or the hosting was removed | Publish from `main` in the organisation's repository. The owner checks the federated credential in infra/README.md. Never add a secret as a workaround. |
| Website validation fails                  | Missing entry point, invalid asset, or too large       | Inspect `uv run python -m app.site --check`; keep only intentional web assets under `site/`.           |
| Times out on **Check the live website**   | Slow first start                                       | Re-run the failed jobs once; if it fails twice, read the revision logs in the Azure portal.            |

The separate **Actions > Deploy my app** workflow is for the post-workshop vendor app and
rehearsals. It still uses the `AZURE_CREDENTIALS` secret; never point learners at it.

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
instructions, and attendees still check every answer. The **Photo Studio** works the same way:
the page posts the photo to the Website preview, which first checks it with the chat model
(things, places and animals only; people, documents, screens, badges and number plates are
refused), repaints it, checks the result again, and saves only pictures it made into the page's
`gallery/`. Uploaded originals are never saved. A published copy shows the gallery only.

Capacity tested on 17 and 19 October 2026 for about 45 people:

| Feature          | Models, in order                                            | Speed                                          |
| ---------------- | ----------------------------------------------------------- | ---------------------------------------------- |
| New picture      | FLUX-1.1-pro and FLUX.1-Kontext-pro, then gpt-image backups | 2-4 seconds; about 60 a minute before backups  |
| Change a picture | FLUX.1-Kontext-pro, then gpt-image-1.5                      | A few seconds                                  |
| Ask my page      | gpt-5.6-luna, then gpt-5.5                                  | 1-2 seconds; 20 questions a minute per page    |
| Photo Studio     | Check: gpt-5.6-luna, then gpt-5.5. Repaint: gpt-image-2, then FLUX.1-Kontext-pro, then gpt-image-1.5 | Check 2-3 seconds; gpt-image-2 about 20 seconds (quota 2), Kontext about 7; 6 a minute per Codespace |

When everyone draws at once, the helper retries once and then says "busy": wait a minute.
Content filters block unsuitable requests with a plain message. gpt-image-2's quota is tiny, so
in a full room most Photo Studio edits come from FLUX.1-Kontext-pro; that is expected.

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

Attendees normally make their own private copy at 09:30 with **Use this template**. Use the
script below beforehand or as a fallback, for example for anyone whose account cannot create
repositories. Repository secrets are **not** copied from a template. The script creates private repositories
and grants the configured attendee team write access. It first inspects the selected template
and stops if facilitator preparation files are present or the inspection fails.

The template no longer tracks `.facilitator/`: the notes stay in the owner's Codespace and are
git-ignored, though earlier commits still contain them. The template also ships no finished
website or learner-made skills, so every attendee starts from the same empty `site/`. CI runs
only on the template repository, so attendee copies never show a red cross they did not cause,
and it fails there if learner work or a `websiteName` is committed. A demo website you build in the
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
- Complete the first website's save/review/commit/push journey (about 30 new files, all staged
  at once) through the browser UI and read back `site/brief.md` on GitHub. Check the current
  screenshots and labels against that client.
- Invoke `/create-website` in a new session; verify it asks only which website (the six
  starters or My own idea), builds straight away with the repository name, and preserves an
  existing page. Run it again after that page is pushed: it must offer an own idea in its own
  folder at once, without asking for checks first.
  Let creation open the Website preview automatically; change a heading and CSS, and observe
  both update with an added entry kept. Do not substitute an HTTP check
  for actual panel rendering or slash-command discovery.
- Verify `/stop-website` closes only the Website preview panel and `/start-website`
  reopens the same saved page automatically. Check a missing file, an already-running preview, an already-stopped
  server, and a separate own-idea page; no recreation, deletion, or unrelated process termination.
- In Lab 02, add a chart with `/add-chart` and check that it follows the entries, add `/add-chat`
  once and check an answer against the page, then one appearance change and an **Undo**. Do
  not repeat the creation interview.
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
- Rehearse Day 3 in a fresh attendee-style Codespace: write two **Requirement** tickets and
  create a Board project named after the account that imports the repository; sign in to Copilot CLI with `/login` and
  the device code, list the tickets with a GitHub tool, create the **user-stories** skill and the
  User Requirements agent from the guide's prompts, restart the CLI and find the agent with
  `/agent`, let it add criteria to a ticket with `gh issue edit`, drag the ticket to **Todo**,
  build it, run `pytest checks` green then red then green, and push a `Closes #N` commit: the
  card moves to **Done**.
- Rehearse Day 4: the criteria automation on a new demo ticket; run `/publish-website` first if
  needed; create the `Protect main` ruleset and confirm a direct push to `main` is refused;
  switch on `version:` on a feature branch, show it in the footer, merge, and see
  **Version 1.0.N** live; assign an approved ticket from the board to Copilot (note the session's
  length); merge the review rules and Code Review agent through a pull request and check the
  agent's report on Copilot's pull request; an `@copilot` fix; merge, see the feature live with
  the next version, and the ticket **Done** on the board. Then try the Day 4 catch-up from the
  guide's top as a newcomer would.
- Rehearse Day 5: copy the check starter on a branch, edit its trigger and permissions, merge it,
  and make **Check the website** and **UI check** required; add a 900-pixel banner and see the UI
  check go red with the banner in `home-phone.png`, then green; copy the approval starter, add
  yourself as a required reviewer of `training`, approve one release; run `scripts/smoke_test.py`,
  ship a bad sentence, roll it back with **Revert**, and confirm the content fingerprint returns
  while the version goes up.
- In a fresh attendee-style Codespace, confirm no MCP server runs on Day 1 and that the Agent's
  **Configure Tools** list shows no Python, pull-request, Pylance, Azure, or plugin tools. Then
  select **Start** on the `github` server in `.vscode/mcp.json`
  (`https://api.githubcopilot.com/mcp/readonly`), sign in, and confirm no write tools appear.
  Attendees get only this server from the repository. If an enterprise-managed plugin or tool still
  appears, an organization policy is overriding the workspace settings; check it with the owner.
- Optionally rehearse the presenter's Lab 04 browser demonstration with VS Code's built-in browser tools,
  from VS Code Desktop connected to the presenter's Codespace (the integrated browser is a desktop
  feature): open a page, read its title, add an item, and report the count. Disable personal MCP
  servers in that workspace so the room sees the same tool list as attendees.
  Attendees run no browser setup. Playwright MCP stays for a later owner-approved environment,
  because Chromium's sandbox could not start in a default Codespace on 14 October 2026; see the
  [Day 3 helper notes](#day-3-helper-preparation).
- Optionally run Lab 06 in a private copy that receives the FOUNDRY_* secrets: an instructions file under
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
| Copilot missing from an issue's Assignees | Cloud agent not enabled for that repository or account | Enable it for attendee repositories before Day 4; meanwhile the attendee follows the presenter's pull request rather than wait. |
| Pushing `.github/workflows/...` is refused | The Codespace token may lack workflow permission | Make the same change on GitHub with the pencil icon or **Add file > Create new file**, committing to a new branch; never add a personal token. |
| A push to `main` is refused from Day 4 on | The `Protect main` ruleset requires a pull request | Expected: create a branch, **Publish Branch**, a pull request, and merge. Never add the attendee to the bypass list. |
| The live footer shows **Preview**, not a version | `version:` still has its `#`, or no release ran since | Merge the uncommented line together with a `site/` change; `/healthz` and `version.json` on the live site show what was published. |
| A required check never reports | The ruleset names a check the workflow does not have | The job names are **Check the website** and **UI check**; add exactly those, after the starter has run once. |
| The UI check is red on a page nobody changed | A real problem on a desktop or phone, or a slow first load | Open the log's table and `home-phone.png`; re-run once for a timeout. Never add `--no-sandbox`. |
| The CI lab's banner leaves the UI check green | The banner went inside the page's header, which cuts it off | Ask Copilot to move it to the very top of the first page, above its header; the check compares the page's width with the phone's. |
| The live footer shows the version on the wrong page | The footer change went into an idea page | Ask for it in the first page, `site/index.html`: the website's address opens that page, and `/version.json` sits beside it. |
| A Day 3 agent is missing from `/agent` | Copilot CLI read agents when it started | Type `/exit`, then `copilot`; check the file is in `.github/agents/` and ends in `.agent.md`. |
| **New project** is missing, or a ticket is not on the board | Organization project settings, or the repository was not imported | Check that organization members may create projects; on the board add the card with **+ Add item** and `#`, choosing the repository. |
| The agent may not update a ticket | The Codespace token is refused for issues | The attendee pastes the agent's draft into the ticket (**...** > **Edit**); never add a personal token. |
| A ticket stays open after its commit | `Closes #N` missing, or the commit is not on `main` | Close it with **Close issue**; the board still moves it to **Done**. |
| Plugin listed but its task fails               | Component discovery, tool access and runtime                             | Inspect the actual invoked component and tool error; manifest presence alone is not a successful test.                                                                      |
| AttractionsAgent absent or not Managed         | Entitlement, private-source read access, policy refresh, local shadowing | Inspect source and the actual agent ID. Do not copy it into the learner repo or change enterprise settings live.                                                            |
| Travel site blocks the agent                   | Site access or bot controls                                              | Use another permitted source or clearly labelled fixture; never call the fallback live browsing.                                                                            |
| Packages work but agent cannot reach localhost | Sandbox and runtime prerequisites                                        | Inspect local-network controls and CLI release notes; do not disable enforced boundaries.                                                                                   |
| Cloud task cannot start                        | Access level or agent policy                                             | Grant write access and enable the cloud agent at organization level.                                                                                                        |
| Agent cannot update protected branch           | Target branch and ruleset                                                | Verify that the task uses its permitted branch. Have the owner approve only the documented exception needed; do not weaken protection during the session.                   |
| Dependency setup fails                         | Registry firewall path                                                   | Allowlist the approved registry endpoints and rebuild the container.                                                                                                        |
| MCP authentication fails                       | Remote URL and browser auth                                              | Use the documented remote URL and confirm the login flow is allowed.                                                                                                        |
| Azure login fails                              | Which workflow, and its identity                                         | **Publish my website** uses GitHub's signed token, no secret: see [infra/README.md](../infra/README.md). **Deploy my app** uses `AZURE_CREDENTIALS`; verify its access and validity without printing its value. |
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
