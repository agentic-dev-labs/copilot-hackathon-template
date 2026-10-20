# Five-day agenda

**Location:** Princeton, New Jersey; Days 1-2 in rooms MKC 1D412 and 1D413  
**Dates:** Monday 26 October-Friday 30 October 2026

**Post-meeting revision: 18 September 2026. Days 3-5 follow David's final slides: 20 October 2026.**
The whole week is for the same audience: business colleagues who have never used GitHub or code
before. Plan support for roughly 40-45 people; confirm the final roster before delivery.
All attendee work remains in browser-based Codespaces. No laptop installation or Azure login.

- **Day 1:** build and check your first website, and save it on GitHub.
- **Day 2:** build your own idea with help at the tables, after the business/IT and Power Platform overviews.
- **Day 3:** write your own User Requirements agent with Copilot CLI, turn your idea into checkable user stories, build one, and test it.
- **Day 4:** practise branches and pull requests, hand an approved story to the cloud agent, and review it with your own Code Review agent.
- **Day 5:** CI/CD with GitHub Actions: check every change, approve each release, roll back a bad one, then demos and handoff.

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

Timings and wording follow David's latest slide (18 October 2026). Ali presents every block after
the opening welcome and teaser. The labs are interactive: Ali shows one step on his own
repository, attendees do it on theirs alongside him or straight after, then the next step.

| Time        | Activity                                                                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 09:00-09:30 | Sponsor welcome (SEFR video), ASTER Overview teaser (HZRW), glossary and GitHub basics (concepts only): Ali shows GitHub and a repository, then everyone makes their own private copy of the template in agentic-dev-labs with Use this template and looks around it; no commands |
| 09:30-10:00 | Lab, from the README: find files and Copilot Chat; ask and refine a question                                                                       |
| 10:00-10:30 | Create an idea note; save, review, commit, push, and verify it on GitHub (README)                                                                   |
| 10:30-10:45 | Break                                                                                                                                               |
| 10:45-11:45 | Lab 01: Ali shows /create-website, then attendees create a Project Planner, Calendar, Ideas Wall, Weather, Princeton Map, Photo Studio, or own-idea website and preview it |
| 11:45-12:15 | Trust but verify: check a button and a figure, fix, and recheck                                                                                     |
| 12:15-13:00 | Lunch                                                                                                                                               |
| 13:00-14:00 | Lab 02: Add a useful interaction, personalize, and check                                                                                            |
| 14:00-14:45 | Lab 08: Save, share, and keep building (publication optional)                                                                                       |
| 14:45-15:00 | Pair sharing and selected volunteer demonstrations                                                                                                  |

**Finish:** a personalized page with one useful interaction, a headline changed by hand after
reading the code with Copilot, one change undone on purpose, manual behavior and source checks,
and reviewed work visible in GitHub, including its history. A private preview is enough. Remembering browser data and
publication are optional extensions. No CLI, MCP, PDF download, presentation, or skill installation
gates Monday's finish. Until 10:30 the [README](../README.md#monday-morning-follow-along) is the
attendees' only page, so they see it on their repository's GitHub page without finding a file;
from 10:45 the [beginner guide](START-HERE.md) is the chronological route. At 09:00 every
attendee (or the driver of a pair) makes one private copy of the template in agentic-dev-labs,
so nobody pushes to a shared repository.
The 11:45 verification block is separate from Lab 01.
The presenter uses the Project Planner; Calendar, Ideas Wall, Weather (with a 3D climate chart),
Princeton Map (2D and 3D) and Photo Studio follow the same guided steps, and My own idea builds a
first page from one sentence. `/add-chart` is an optional Lab 02 wow. Complete, check, save, and show that page before an own-idea page, preserving
the first page. Fast finishers may start their own idea on Monday; it is Tuesday's main focus.

## Day 2 - Tuesday, 6 hours - Line of Business

| Time        | Activity                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------- |
| 09:00-09:30 | David: business/IT responsibilities, low-risk use cases, approved tools, and the internal AI marketplace overview |
| 09:30-10:30 | Jackie: Power Platform, Dataverse, and connectors explained through examples; no attendee integration setup |
| 10:30-10:45 | Break                                                                                                               |
| 10:45-12:15 | Supported own-idea build: agree one outcome, start it in its own folder with /create-website, and build the first version with fictional local data |
| 12:15-13:00 | Lunch                                                                                                               |
| 13:00-14:00 | Open build: improve one interaction, compare expected and actual behavior, and get help at the table |
| 14:00-14:45 | Supported personal building, fixes, and optional assisted publication                                               |
| 14:45-15:00 | Selected volunteer demonstrations and a clear next step with the technical owner |

**Finish:** an own-idea prototype or improved default app, one checked user journey, reviewed
work saved in GitHub, and a short list of data/access questions for the technical owner.
Use [the own-idea build guide](DAY-2-BUILD.md). No Dataverse connection, CLI turn, MCP invocation,
automated test, or public deployment is required. After the two overviews there are no more
room-wide presentations: helpers work at the tables. Keep this idea; you can continue it on Days 3-4.

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

**Finish:** a User Requirements agent the attendee wrote, a validated requirements file with one
approved story, that story working on their own website, and green `pytest checks`. Follow the
[Day 3 guide](TOOLS-PRACTICE.md). Attendees describe the agent in plain words and Copilot CLI
writes `.github/agents/user-requirements.agent.md`; the same file works in VS Code Chat. The
template ships the `checks/` helper, not a finished agent, story, or test. Lab 04 and Lab 06 are
optional extras.

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

**Finish:** a merged practice pull request, a cloud-agent pull request built from an approved
story (**User story for Copilot** issue template), a Code Review agent the attendee wrote, a
findings report with every finding verified by hand, and a merge-or-close decision with a reason.
Follow the [Day 4 guide](DAY-4-BUILD.md) and [Lab 03](../labs/03-cloud-agent/README.md).

## Day 5 - Friday, 4 hours - CI/CD with GitHub Actions

Ali. Times count from the start of the session.

| Elapsed     | Activity                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 00:00-00:20 | CI/CD concepts: continuous integration, delivery, and deployment                                                  |
| 00:20-00:50 | Workflow lab: edit a starter YAML file, triggers and permissions                                                  |
| 00:50-01:30 | CI lab: build and test a pull request, inspect logs, and fix failures                                             |
| 01:30-01:45 | Break                                                                                                             |
| 01:45-02:30 | CD lab: approve and deploy a build to the training environment                                                    |
| 02:30-03:15 | Recovery lab: smoke-test the app and redeploy a known-good build                                                  |
| 03:15-03:45 | Team demos: show requirements, review report, and CI/CD evidence                                                  |
| 03:45-04:00 | Handoff: share agent profiles, pipeline steps, and release ownership                                              |

**Finish:** the attendee's own check workflow running on pull requests, a red check fixed from
its log, publishing gated by their own approval in the `training` environment, a bad release
rolled back and proven by `scripts/smoke_test.py`, and a HANDOFF.md. Follow the
[Day 5 guide](DAY-5-SHOWCASE.md). Starters live in `.github/workflow-starters/`; publishing still
uses the template's OIDC publisher, so nobody needs a secret or an Azure sign-in.

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
