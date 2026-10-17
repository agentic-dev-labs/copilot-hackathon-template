# Five-day agenda

**Location:** Princeton, New Jersey  
**Dates:** Monday 26 October-Friday 30 October 2026

**Post-meeting revision: 18 September 2026. Days 3-5 simplified: 14 October 2026.** The whole
week is for the same audience: business colleagues who have never used GitHub or code before.
Plan support for roughly 40-45 people; confirm the final roster before delivery.
All attendee work remains in browser-based Codespaces. No laptop installation or Azure login.

- **Day 1:** build and check your first website, and save it on GitHub.
- **Day 2:** build your own idea with help at the tables, after the business/IT and Power Platform overviews.
- **Day 3:** see a few more ways to use Copilot on your own website, then pick the idea you will build.
- **Day 4:** build day.
- **Day 5:** show what you built or learned in a round of short presentations.

The habit is **show -> try -> personalize -> verify -> share**. After the first concepts-only
block, show one action for 3-5 minutes, allow 8-12 minutes to try it, then check progress.
Repeat within the existing blocks. Keep day boundaries, breaks, and active lab durations unchanged.
The former Dataverse Lab 05 is a post-workshop technical reference, not a scheduled lab. Hooks,
automations, multi-agent handoffs, saved browser tests, CI, and the vendor app are no longer
workshop topics; they are kept as [advanced post-workshop reference](../post-workshop/advanced/README.md).
Dependencies and sign-in preflight are facilitator preparation, not room-wide install exercises.

Official starting points: [Copilot features](https://docs.github.com/en/copilot/get-started/about-github-copilot),
[VS Code agents](https://code.visualstudio.com/docs/agents/overview),
[customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet),
and [current release notes](https://github.blog/changelog/label/copilot/).
Feature availability depends on client, model, license, and policy; previews are not lab prerequisites.
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
| 10:45-11:45 | Lab 01: Use /create-website to pick a Project Planner, Calendar, Ideas Wall, or Weather page; it builds and opens the live preview |
| 11:45-12:15 | Trust but verify: manually check a button and a figure against its source; describe a real issue, improve, and recheck                              |
| 12:15-13:00 | Lunch                                                                                                                                               |
| 13:00-14:00 | Lab 02: Make your website useful; add one interaction, personalize, and check it yourself                                                           |
| 14:00-14:45 | Lab 08: Save, share, and keep building; supported publication is optional, not the core finish                                                      |
| 14:45-15:00 | Pair sharing and selected volunteer demonstrations: what worked, what you checked, and a possible work use |

**Finish:** a personalized page with one useful interaction, a headline changed by hand after
reading the code with Copilot, one change undone on purpose, manual behavior and source checks,
and reviewed work visible in GitHub, including its history. A private preview is enough. Remembering browser data and
publication are optional extensions. No CLI, MCP, PDF download, presentation, or skill installation
gates Monday's finish. The [beginner guide](START-HERE.md) is the chronological route.
The 10:00 note block and 11:45 verification block are separate from Labs 00 and 01.
The presenter uses the Project Planner; Calendar, Ideas Wall and Weather follow the same guided
steps. Complete, check, save, and show that page before an own-idea page, preserving
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

## Day 3 - Wednesday, half-day - More Ways to Use Copilot

| Time        | Activity                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 09:00-09:45 | Copilot in the terminal (CLI): watch, then ask one question about your own website                                |
| 09:45-10:30 | Lab 04: Copilot uses tools (MCP): read your GitHub history, then watch Copilot check a page in a browser           |
| 10:30-10:45 | Break                                                                                                             |
| 10:45-11:30 | Lab 06: Teach Copilot about your project with one instructions file and one small skill                           |
| 11:30-12:15 | Pick your idea: continue Tuesday's or start a new one; write a short brief and begin                              |
| 12:15-12:30 | Lab 03: Watch the cloud agent take a task from an issue (demonstration), then tomorrow's plan                     |

**Finish:** one CLI question about your own page, a GitHub answer you checked yourself, the
presenter's browser check compared with your own, your own instructions file and skill, and a
chosen idea with a short brief. Attendees install nothing on Day 3. Follow the
[Day 3 guide](TOOLS-PRACTICE.md). Everything works on the website you already built; no new app
or database is needed.

## Day 4 - Thursday, half-day - Build Day

| Time        | Activity                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 09:00-09:15 | Recap and goal: one working thing to show tomorrow; optional: hand one small change to the cloud agent            |
| 09:15-10:30 | Build your idea with help at the tables                                                                           |
| 10:30-10:45 | Break                                                                                                             |
| 10:45-11:45 | Quick check-in, then keep building                                                                                |
| 11:45-12:15 | Check it yourself; review the cloud agent's pull request if you tried it                                          |
| 12:15-12:30 | Save to GitHub and prepare your 3-minute story                                                                    |

**Finish:** a working first version of your idea, or a clear improvement, checked yourself and
saved on GitHub, plus a 3-minute story ready for Friday. Use the [build day guide](DAY-4-BUILD.md).
The cloud-agent try in [Lab 03](../labs/03-cloud-agent/README.md) is optional and happens inside
the building time. No publication, automated test, or new tool is required.

## Day 5 - Friday, half-day - Show What You Built

| Time        | Activity                                                                                                          |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| 09:00-09:30 | Final polish and practice your 3-minute story                                                                     |
| 09:30-10:30 | Presentations, round 1                                                                                            |
| 10:30-10:45 | Break                                                                                                             |
| 10:45-12:00 | Presentations, round 2                                                                                            |
| 12:00-12:30 | Wrap-up: approved tools, who to ask, keeping your work, and next steps                                            |

**Finish:** each attendee has shown what they built or learned: a website, a skill, a CLI or
MCP trick, or a better way of working with AI. Use the [showcase guide](DAY-5-SHOWCASE.md).
About 2 minutes to show plus 1 minute for a question or change-over fits about 40 people with a
short buffer; with more, present in pairs or by table. A private preview is enough; nothing has to
be published.

## Optional Extension Shelf

[Public research, MarkItDown, HTML presentations, and business-skill examples](RESEARCH.md)
remain available for supported exploration or later practice. They replace another extension
when chosen; they do not add hidden minutes to a core lab. The [coverage guide](REFERENCES.md)
distinguishes core work, demonstrations, and optional material. Deeper technical topics live in
the [advanced post-workshop reference](../post-workshop/advanced/README.md), not in this week.

## Scheduling and Handover

The repository remains 09:00-15:00 on Days 1-2 and 09:00-12:30 on Days 3-5. The reported
09:00-16:00 invitation window is not an approved extension of this timetable. Confirm speaker
availability and any change with the organizers. Preserve learner work and confirm access for
all remaining sessions before considering training-membership cleanup.
