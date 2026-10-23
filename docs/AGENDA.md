# Five-day agenda

**Location:** Princeton, New Jersey; Days 1-2 in rooms MKC 1D412 and 1D413  
**Dates:** Monday 26 October-Friday 30 October 2026

**Post-meeting revision: 18 September 2026. Days 3-5 follow David's final slides: 20 October 2026.**
The whole week is for the same audience: business colleagues who have never used GitHub or code
before. Plan support for roughly 40-45 people; confirm the final roster before delivery.
All attendee work remains in browser-based Codespaces. No laptop installation or Azure login.

- **Day 1:** build and check your first website, and save it on GitHub.
- **Day 2:** build your own idea with help at the tables, around the business/IT, Power Platform, and Project Brain talks.
- **Day 3:** turn your idea into tickets on a project board, write your own User Requirements agent with Copilot CLI that adds checkable acceptance criteria to each ticket, build one, and test it.
- **Day 4:** practice branches and pull requests, hand an approved ticket to the cloud agent, and review it with your own Code Review agent.
- **Day 5:** CI/CD with GitHub Actions: check every change, try each pull request in a feature slot, approve each release to production, roll back a bad one, then demos and handoff.

The habit is **show -> try -> personalize -> verify -> share**. After the first concepts-only
block, show one action for 3-5 minutes, allow 8-12 minutes to try it, then check progress.
Repeat within the existing blocks. Keep day boundaries, breaks, and active lab durations unchanged.
The former Dataverse Lab 05 is a post-workshop technical reference, not a scheduled lab. Hooks,
automations, multi-agent handoffs, saved browser tests, and the vendor app are not workshop
topics; they are kept as [advanced post-workshop reference](../post-workshop/advanced/README.md).
Days 3-5 always work on the attendee's own website, with agents the attendee writes in plain words.
Dependencies and sign-in preflight are facilitator preparation, not room-wide install exercises.

Official starting points: [Copilot features](https://docs.github.com/en/copilot/get-started/about-github-copilot),
[VS Code agents](https://code.visualstudio.com/docs/agents/overview),
[customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet),
and [current release notes](https://github.blog/changelog/label/copilot/).
Feature availability depends on client, model, license, and policy; previews are not lab prerequisites.
Use the [coverage and official reference guide](REFERENCES.md) for topic-level links and short
optional tasks for every day. Monday's guides support live demonstrations, not independent
self-study. Monday morning runs from the repository [README](../README.md#monday-morning-follow-along);
from 10:45 use [START-HERE](START-HERE.md) and the [printable quick reference](QUICK-REFERENCE.md).

## Day 1 - Monday, 6 hours - GitHub and your first app (Line of Business)

Timings and wording follow David's final slide (20 October 2026); the order inside the blocks was
agreed with Ali on 21 October 2026. Ali presents every block after the opening welcome and
teaser. The labs are interactive: Ali shows one step on his own repository, attendees do it on
theirs alongside him or straight after, then the next step.

| Time        | Activity                                                                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 09:00-09:30 | Sponsor welcome (SEFR video), ASTER Overview teaser (HZRW), glossary and GitHub basics (concepts only): Ali shows GitHub and a repository on the template; attendees watch, no commands |
| 09:30-10:00 | Lab, from the README: everyone makes their own private copy of the template in agentic-dev-labs with Use this template, opens its Codespace, finds files and Copilot Chat, sees the same question give different answers (a fun table name, compared with a neighbour), and asks and refines a question |
| 10:00-10:30 | Create the first website with /create-website, which writes its idea note (site/brief.md); save, review, commit, push, and verify it on GitHub (README) |
| 10:30-10:45 | Break                                                                                                                                               |
| 10:45-11:45 | Lab 01: Ali shows more websites (Weather in 3D, Princeton Map, Photo Studio, Lab Chase, a tracker from one sentence); attendees read the code, change the headline by hand, and build one idea of their own in its own folder |
| 11:45-12:15 | Trust but verify: check a button and a figure, fix, and recheck                                                                                     |
| 12:15-13:00 | Lunch                                                                                                                                               |
| 13:00-14:00 | Lab 02: Add a useful interaction (a chart with /add-chart, a chat, or a picture), personalize, and check                                           |
| 14:00-14:45 | Lab 08: Save, share, and keep building (publication optional)                                                                                       |
| 14:45-15:00 | Pair sharing and selected volunteer demonstrations                                                                                                  |

**Finish:** a first page with a chart or chat checked by hand, one idea of their own in its own
folder, a headline changed by hand after reading the code with Copilot, one change undone on
purpose, manual behavior and source checks, and reviewed work visible in GitHub, including its
history. A private preview is enough. Remembering browser data and
publication are optional extensions. No CLI, MCP, PDF download, presentation, or skill installation
gates Monday's finish. Until 10:30 the [README](../README.md#monday-morning-follow-along) is the
attendees' only page, so they see it on their repository's GitHub page without finding a file;
from 10:45 the [beginner guide](START-HERE.md) is the chronological route. At 09:30 every
attendee (or the driver of a pair) makes one private copy of the template in agentic-dev-labs,
so nobody pushes to a shared repository.
The 11:45 verification block is separate from Lab 01.
The presenter uses the Project Planner; Calendar, Ideas Wall, Weather (with a 3D climate chart),
Princeton Map (2D and 3D) and Photo Studio follow the same guided steps, and My own idea builds a
first page from one sentence. The first page is saved on GitHub before anyone builds an own idea,
which always gets its own folder, so the first page is preserved. `/add-chart` is Lab 02's main
interaction; `/add-chat` and a picture are alternatives. Tuesday continues the own ideas.

## Day 2 - Tuesday, 6 hours - Line of Business

Timings follow David's final slide (20 October 2026). David, Jackie, and Bill Leeson present;
Ali supports the tables with the other helpers.

| Time        | Activity                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------- |
| 09:00-09:30 | David: business/IT responsibilities, low-risk use cases, approved tools, and the internal AI marketplace overview |
| 09:30-10:30 | Jackie: Power Platform, Dataverse, and connectors explained through examples; no attendee integration setup |
| 10:30-10:45 | Break                                                                                                               |
| 10:45-11:45 | Supported own-idea build: agree one outcome, start it in its own folder with /create-website, and build and save the first version with fictional local data |
| 11:45-12:15 | Bill Leeson: Building a Project Brain                                                                               |
| 12:15-13:00 | Lunch                                                                                                               |
| 13:00-14:00 | Open build: improve one interaction, compare expected and actual behavior, and get help at the table |
| 14:00-14:45 | Supported personal building, fixes, and optional assisted publication                                               |
| 14:45-15:00 | Selected volunteer demonstrations and a clear next step with the technical owner |

**Finish:** an own-idea prototype or improved default app, one checked user journey, reviewed
work saved in GitHub, a short list of data/access questions for the technical owner, and two or
three **Next** wishes in the brief, which become Wednesday's tickets.
Use [the own-idea build guide](DAY-2-BUILD.md). No Dataverse connection, CLI turn, MCP invocation,
automated test, or public deployment is required. Apart from the three talks, helpers work at the
tables; attendees save their first version before Bill's talk. Keep this idea; Days 3-5 continue it.

Participants work through familiar Chat with fictional content stored in the app. David's team
owns later data modeling and integrations. The [preserved Dataverse reference](../post-workshop/dataverse/README.md)
and its prompts are for that later technical session, not Day 2. A switch to corporate tooling,
AI marketplace configuration, or removal of training access requires a separately approved,
tested handover. The workshop remains Codespaces-only; there is no account-deletion exercise.

## Day 3 - Wednesday, 4 hours - VS Code and a Requirements Agent

MUKQ opening session, then Ali. Times count from the start of the session (owner-approved
slides, 20 October 2026).

| Elapsed     | Activity                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 00:00-00:20 | MUKQ: global and Microsoft perspectives on AI development                                                         |
| 00:20-00:50 | Ali: workspace setup, repository walkthrough, and agent roles and tools (Copilot CLI sign-in)                      |
| 00:50-01:30 | Build a User Requirements agent: instructions and output format                                                   |
| 01:30-01:45 | Break                                                                                                             |
| 01:45-02:30 | Agent lab: draft user stories and acceptance criteria, then validate                                              |
| 02:30-03:15 | Build lab: implement an approved story, debug, and verify the fix                                                 |
| 03:15-03:45 | Team build: add tests and document build and run commands                                                         |
| 03:45-04:00 | Checkpoint: show the agent, requirements, and working feature                                                     |

**Finish:** the attendee's own idea as tickets (issues from the **Requirement** template) on a
project board; a **user-stories** skill and a User Requirements agent the attendee wrote, which
add a user story and checkable acceptance criteria to each ticket; a brief that lists those
requirements and how to run the page; and one approved ticket built in the Codespace, checked
against its criteria, tested with green `pytest checks`, and closed by a `Closes #N` commit, so
the board shows it **Done**. Follow the [Day 3 guide](TOOLS-PRACTICE.md). In every block Ali
shows the step on a demo website, then attendees do the same on their own idea. The 00:20 block
uses a GitHub tool through MCP, and the 00:50 block opens with the building blocks
(instructions, skills, agents, and tools), the topics of Labs 04 and 06. Attendees describe the
skill and the agent in plain words and Copilot CLI writes `.github/skills/user-stories/` and
`.github/agents/user-requirements.agent.md`; the agent reads a ticket with the GitHub tools,
updates it with `gh` once the attendee agrees, and also works in VS Code Chat. The template ships
the **Requirement** issue template and the `checks/` helper, not a finished agent, skill, ticket,
or test. Lab 04 and Lab 06 remain optional extras.

## Day 4 - Thursday, 4 hours - GitHub Copilot Cloud Agents

Ali. Times count from the start of the session.

| Elapsed     | Activity                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 00:00-00:20 | Cloud-agent overview: delegation, safeguards, and human review                                                    |
| 00:20-00:50 | GitHub lab: practice branches and pull requests with a small change                                               |
| 00:50-01:30 | Lab 03: Delegation lab: assign an approved requirement to Copilot                                                 |
| 01:30-01:45 | Break                                                                                                             |
| 01:45-02:30 | Build a Code Review agent: review rules and report format                                                         |
| 02:30-03:15 | Report lab: run the agent on a diff and verify its findings                                                       |
| 03:15-03:45 | Iteration lab: request fixes with @copilot, retest, and peer-review                                               |
| 03:45-04:00 | Checkpoint: review the report and decide whether to merge                                                         |

**Finish:** a `Protect main` ruleset (changes reach `main` only through pull requests), a
pipeline that writes its build number into the live website as the
version, a cloud-agent pull request built from an approved ticket on the attendee's board,
review rules and a Code Review agent the attendee wrote, a findings report with
every finding verified by hand, and a decision: merged and deployed with the next version
number, with the ticket **Done** on the board, or closed with a reason. Copilot code review stays
switched off: the attendee's own Code Review agent does the reviewing. Attendees who join on
Day 4 or Day 5 start from the short catch-up at the top of that day's guide. Follow the
[Day 4 guide](DAY-4-BUILD.md) and [Lab 03](../labs/03-cloud-agent/README.md).

## Day 5 - Friday, 4 hours - CI/CD with GitHub Actions

Ali. Times count from the start of the session.

| Elapsed     | Activity                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 00:00-00:20 | CI/CD concepts: continuous integration, delivery, and deployment                                                  |
| 00:20-00:50 | Workflow lab: edit a starter YAML file, triggers and permissions                                                  |
| 00:50-01:30 | CI lab: build and test a pull request, inspect logs, and fix failures                                             |
| 01:30-01:45 | Break                                                                                                             |
| 01:45-02:30 | CD lab: approve and deploy a build to a training environment                                                      |
| 02:30-03:15 | Recovery lab: smoke-test the app and redeploy a known-good build                                                  |
| 03:15-03:45 | Team demos: show requirements, review report, and CI/CD evidence                                                  |
| 03:45-04:00 | Handoff: share agent profiles, pipeline steps, and release ownership                                              |

**Finish:** the attendee's own checks required on every pull request (their tests, plus a UI
check that opens their pages on a desktop and a phone and keeps the screenshots), a red UI check
fixed from its log and screenshot, a feature slot that shows every checked pull request with its
pull request, version, and build in a strip at the top, Copilot's ticket tried there, then
released to the production slot only after their own approval in the `production` environment,
a bad release rolled back with GitHub's **Revert** and proven by
`scripts/smoke_test.py`, team demos, and a HANDOFF.md. Follow the
[Day 5 guide](DAY-5-SHOWCASE.md). Starters live in `.github/workflow-starters/`; both slots still
use the template's OIDC publisher, so nobody needs a secret or an Azure sign-in.

## Optional Extension Shelf

[Public research, MarkItDown, HTML presentations, and business-skill examples](RESEARCH.md)
remain available for supported exploration or later practice. They replace another extension
when chosen; they do not add hidden minutes to a core lab. The [coverage guide](REFERENCES.md)
distinguishes core work, demonstrations, and optional material. Deeper technical topics live in
the [advanced post-workshop reference](../post-workshop/advanced/README.md), not in this week.

## Scheduling and Handover

The repository remains 09:00-15:00 on Days 1-2. Days 3-5 are four hours each, written as
elapsed times exactly as on David's slides; confirm each day's start time with the organizers.
The reported 09:00-16:00 invitation window is not an approved extension of Days 1-2. Confirm
speaker availability and any change with the organizers. Preserve learner work and confirm access for
all remaining sessions before considering training-membership cleanup.
