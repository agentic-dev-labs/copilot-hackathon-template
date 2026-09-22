# Five-day agenda

**Location:** Princeton, New Jersey  
**Dates:** Monday 26 October-Friday 30 October 2026

**Post-meeting revision: 18 September 2026.** Days 1-2 are a complete introduction for
first-time GitHub and app-building users. Plan support for roughly 40-45 people; confirm the
final roster before delivery. Days 3-5 are
technical half-days for low-coders and pro-coders, not prerequisites for Monday's success.
All attendee work remains in browser-based Codespaces. No laptop installation or Azure login.

The habit is **show -> try -> personalise -> verify -> share**. After the first concepts-only
block, show one action for 3-5 minutes, allow 8-12 minutes to try it, then check progress.
Repeat within the existing blocks. Keep day boundaries, breaks, and active lab durations unchanged.
The former Dataverse Lab 05 is now a post-workshop technical reference, not a scheduled lab.
Tuesday's former tools hour is supported building; the final 15 minutes allow selected volunteers
to share. Day 2 is not a sequence of technical labs.
Dependencies and sign-in preflight are facilitator preparation, not room-wide install exercises.

Official starting points: [Copilot features](https://docs.github.com/en/copilot/get-started/features),
[VS Code agents](https://code.visualstudio.com/docs/agents/overview),
[customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet),
and [current release notes](https://github.blog/changelog/label/copilot/).
Feature availability depends on client, model, licence, and policy; previews are not lab prerequisites.
Use the [coverage and official reference guide](REFERENCES.md) for topic-level links and short
optional tasks for every day. Monday's guides support live demonstrations, not independent
self-study. Use [START-HERE](START-HERE.md) and the [printable quick reference](QUICK-REFERENCE.md).

## Day 1 - Monday, 6 hours - Line of Business

| Time        | Activity                                                                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 09:00-09:30 | Brief sponsor welcome within the concepts-only block; glossary, screenshots, GitHub/repository/Codespace, save -> commit -> push; no commands |
| 09:30-10:00 | Lab 00: Find your files and Copilot Chat; ask and refine one question                                                                               |
| 10:00-10:30 | Show and try: create a short idea note; save, review, commit, push, and confirm the file on GitHub                                                  |
| 10:30-10:45 | Break                                                                                                                                               |
| 10:45-11:45 | Lab 01: Use /create-website to choose a fictional starter, logo, colors, and features; build and open the embedded live preview |
| 11:45-12:15 | Trust but verify: manually check a button and a figure against its source; describe a real issue, improve, and recheck                              |
| 12:15-13:00 | Lunch                                                                                                                                               |
| 13:00-14:00 | Lab 02: Make your website useful; add one interaction, personalise, and check it yourself                                                           |
| 14:00-14:45 | Lab 08: Save, share, and keep building; supported publication is optional, not the core finish                                                      |
| 14:45-15:00 | Pair sharing and selected volunteer demonstrations: what worked, what you checked, and a possible work use |

**Finish:** a personalised page with one useful interaction, manual behaviour and source checks,
and reviewed work visible in GitHub. A private preview is enough. Remembering browser data and
publication are optional extensions. No CLI, MCP, PDF download, presentation, or skill installation
gates Monday's finish. The [beginner guide](START-HERE.md) is the chronological route.
The 10:00 note block and 11:45 verification block are separate from Labs 00 and 01.
The presenter uses the weekend planner; project and budget planners follow the same guided
steps. Complete, check, save, and show that starter before an own-idea extension, preserving
the first page. Their own business idea is Tuesday's main focus.

## Day 2 - Tuesday, 6 hours - Line of Business

| Time        | Activity                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------- |
| 09:00-09:30 | David: business/IT responsibilities, low-risk use cases, approved tools, and the internal AI marketplace overview |
| 09:30-10:30 | Jackie: Power Platform, Dataverse, and connectors explained through examples; no attendee integration setup |
| 10:30-10:45 | Break                                                                                                               |
| 10:45-12:15 | Supported own-idea build: agree one outcome, use the prepared repository, and build the first version with fictional local data |
| 12:15-13:00 | Lunch                                                                                                               |
| 13:00-14:00 | Open build: improve one interaction, compare expected and actual behaviour, and get help at the table |
| 14:00-14:45 | Supported personal building, fixes, and optional assisted publication                                               |
| 14:45-15:00 | Selected volunteer demonstrations and a clear next step with the technical owner |

**Finish:** an own-idea prototype or improved default app, one checked user journey, reviewed
work saved in GitHub, and a short list of data/access questions for the technical owner.
Use [the own-idea build guide](DAY-2-BUILD.md). No Dataverse connection, CLI turn, MCP invocation,
automated test, or public deployment is required. A prepared browser demonstration may help a
ready individual, but must not interrupt the group's protected building time.

Participants work through familiar Chat with fictional content stored in the app. David's team
owns later data modelling and integrations. The [preserved Dataverse reference](../post-workshop/dataverse/README.md)
and its prompts are for that later technical session, not Day 2. A switch to corporate tooling,
AI marketplace configuration, or removal of training access requires a separately approved,
tested handover. The workshop remains Codespaces-only; there is no account-deletion exercise.

## Day 3 - Wednesday, half-day - Low-coders and pro-coders

| Time        | Activity                                                                              |
| ----------- | ------------------------------------------------------------------------------------- |
| 09:00-09:30 | Show and try: one CLI task (15 minutes), then a bounded cloud-agent issue and its review workflow (15 minutes) |
| 09:30-10:30 | Lab 03: Cloud agent                                                                   |
| 10:30-10:45 | Break                                                                                 |
| 10:45-11:15 | Show and try: MCP explained through a prepared Playwright browser check and comparison with a manual observation |
| 11:15-12:15 | Lab 04: Remote GitHub MCP                                                             |
| 12:15-12:30 | Review the agent's pull request together                                              |

**Finish:** a real CLI turn, an observed prepared browser check, a human-reviewed agent contribution,
and a verified read-only GitHub MCP result. The introductions fit the two existing demonstration
blocks; they do not add an extra hour. Deeper configuration belongs in Lab 04. New technical
attendees can use the prepared local-sample vendor reader without Dataverse or Monday's website.

## Day 4 - Thursday, half-day - Low-coders and pro-coders

| Time        | Activity                                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------------------- |
| 09:00-09:30 | Demonstration: event-triggered automations and hooks that record or deny tool calls                            |
| 09:30-10:30 | Lab 07: Automations and hooks                                                                                  |
| 10:30-10:45 | Break                                                                                                          |
| 10:45-11:15 | Demonstration: turn a browser journey into a saved check; inspect code review and prepared deployment evidence |
| 11:15-12:30 | Readiness practice: run the saved browser check, inspect CI, verify a deployment, and record remaining gaps    |

**Finish:** repeatable verification and a checked release, not a claim of production certification.
A Playwright MCP observation is not a saved test. Use the repeatable-check exercise in Lab 07's
separate 11:15 block; it does not enlarge that lab's 60-minute automation/hook time-box.
Release one selected target: the learner website or the vendor reader with local synthetic
samples. A live Dataverse release is post-workshop work, not a required technical-track gate.

## Day 5 - Friday, half-day - Low-coders and pro-coders

| Time        | Activity                                                                                                           |
| ----------- | ------------------------------------------------------------------------------------------------------------------ |
| 09:00-09:30 | Discover a reviewed everyday-work skill on Awesome Copilot; compare using guidance with authoring a role and skill |
| 09:30-11:00 | Lab 06: Build your own agent and skill, then hand off work                                                         |
| 11:00-11:15 | Break                                                                                                              |
| 11:15-11:45 | Evaluations and evidence quality; optional second-model check                                                      |
| 11:45-12:30 | Final demonstrations and close                                                                                     |

**Finish:** a reusable workflow tested against correct, missing, and contradictory evidence.
Synthetic vendor scores still come from the evaluator, never a model's opinion. Managed plugins
and parallel-agent comparisons are optional, not extra required topics in the opening block.

## Optional Extension Shelf

[Public research, MarkItDown, HTML presentations, and business-skill examples](RESEARCH.md)
remain available for supported exploration or later practice. They replace another extension
when chosen; they do not add hidden minutes to a core lab. The [coverage guide](REFERENCES.md)
distinguishes core work, guided introductions, technical labs, and optional material.

## Scheduling and Handover

The repository remains 09:00-15:00 on Days 1-2 and 09:00-12:30 on Days 3-5. The reported
09:00-16:00 invitation window is not an approved extension of this timetable. Confirm speaker
availability and any change with the organisers. Preserve learner work and confirm access for
all remaining sessions before considering training-membership cleanup.
