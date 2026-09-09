# Novo Nordisk North America — GitHub Copilot Hackathon
## Engagement Brief & Decision Log - historical snapshot, engineering notes updated 7 September 2026

> **Classification: MICROSOFT INTERNAL — CONFIDENTIAL.**
> Contains commercial terms, dispatch references, compete positioning and candid internal discussion.
> The repository owner explicitly approved temporary versioning in this shared repository on
> 2026-09-09, after acknowledging that all repository readers can access the file and its history.
> This dot-folder is organizational, not an access restriction. Do not redistribute the material
> outside that approved audience. See [README.md](README.md) for the 2026-10-12 cleanup reminder;
> untracking later does not remove existing history or copies. Repository paths below start at the root.

**Prepared for:** Ali Reza Farahnak (delivery lead)
**Compiled from:** Teams (1:1s, group chats, meeting chats), Outlook mail + calendar, OneDrive (Mike Podolski's *2026-10 Hackathon* folder; Ali's *GitHub CoPilot Novo Nordisk* folder), the Novo account channel, the Copilot CLI build log (2 Sep), and web research on GitHub's agentic stack (31 Aug 2026).
**On transcripts:** no meeting transcripts exist for this engagement. The first prep calls are 14 and 18 Sep. Every "discussion" below comes from Teams chat logs and email, quoted verbatim where it matters.

**Reading this record:** quoted discussions and proposed decisions below are historical, not a
live access, billing, calendar, or product-support check. Current implementation instructions are
in `README.md`, `docs/FACILITATOR.md`, and the labs. The working agenda is unchanged; invitations
and time changes are outside the current repository cleanup. Preserve customer quotations rather
than treating the training implementation as a complete delivery of every requested feature.

---

## Contents

1. One-page summary & purpose
2. People
3. Timeline (Dec 2024 → 2 Sep 2026)
4. The proposal (v3) and deck lineage
5. Agenda changes since v3
6. Customer background & the real use case
7. Constraints
8. Technical research — GitHub agentic stack
9. Delivery environment & identity — decision log
10. PoCs proposed
11. Repo plan & build status
12. Commercials & logistics
13. Calendar
14. Open items (prioritised)
15. Risks
16. Where everything lives
- Appendix A — David Santos's SOC 2 agent spec (full)
- Appendix B — 20 July alignment (verbatim)
- Appendix C — Source prompts for the deck
- Appendix D — Access questions to send David & Jackie (paste-ready)
- Appendix E — Commands

---

## 1. One-page summary

| | |
|---|---|
| **Event** | GitHub Copilot Hackathon — Novo Nordisk North America (Novo Nordisk Inc.) |
| **Where** | Princeton, New Jersey — venue address requested 6 Aug, **not yet received** |
| **When** | Mon 26 – Fri 30 October 2026 |
| **Shape** | Days 1–2: hackathon for Line-of-Business teams (**6-hour days**). Days 3–5: deep dives for low-coders + pro-coders (**half-days**). |
| **Customer sponsor** | David Santos (DVSO) — Senior Manager, Digital Solutions, NN NA |
| **Customer PM** | Susan Ames (SUAS) — program manager for the site; internal promotion & recruitment |
| **Microsoft** | Ali Farahnak (delivery, all content) · Mike Podolski (account, Senior CSAM) · Jackie Kelly (Power Platform, Q&A, ~1h on Day 2) |
| **Commercial** | Onsite delivery **non-billable** (Microsoft Denmark investment). Prep **billable** via Ali's self-dispatch ROSS2026072005388609 on agreement 185945054 / package 189101145. |
| **Status** | v3 proposal accepted 20 Jul; Jackie updated the shape 28 Aug. The template was committed and pushed from 2 Sep onward. Code, lab instructions, and tests have since been expanded; current verification belongs to the latest test run, not the original scaffold count. Live access and full lab rehearsal remain separate checks. |
| **Hard constraints** | Node.js blocked on all non-IT laptops · restrictive GitHub permissions · post-incident GitHub estate (new instance since 1 Jul 2026) · GxP-regulated pharma |
| **Biggest open question** | Can Novo attendees join an **external** GitHub org (EMU vs SSO)? This decides the delivery-environment plan. |

### Purpose — why this exists

- **Customer's why** (David, via Mike, 23 Apr): "enable regular Devs and citizen developers from their business teams to handle their own app and UI design and development, while his team concentrates more on data model governance." Scale: "we have up to 1000 people in this building alone who could end up benefiting from a GitHub Copilot license." Gains Mike listed: more apps on Power Platform (idea-to-app time down, backlog cleared), more Copilot licences in use, downstream ACR/AI revenue, repeatable across business teams globally. David "expressed a strong preference for an on-site delivery over remote."
- **Ali's why** (20 Jul): "prior to this most of these people are not even pro code developers any of them, my aim is to enable/adopt Github Copilot for these people so they can start coding and consume AI through Github."
- **Microsoft's why** (Mike, 20 Jul): "this is like a trojan horse to win their AI business more broadly." Ali: "Specially in NN we have tough compete with AWS… if [we] dont show them our agents and how to code with our stack I am sure AWS and competitors happily will take the fruit instead."
- **Account context:** Novo removed GitHub/ADO access for all employees in May 2026 after a security incident, then reopened on a **new GitHub instance on 1 Jul 2026** — 1,100 developers onboarded in 24 hours, ambition **8,000 developers in 4–5 months** with GitHub + Copilot + GitHub Advanced Security as the single developer platform. Novo has publicly named AWS its preferred cloud and strategic AI partner.
- **The promised outcome** (v3 deck): "confidence to build pro-code apps with AI, hands-on not slideware, idea-to-deployed-app in one week."

---

## 2. People

### Microsoft

| Name | Role here | Notes |
|---|---|---|
| **Ali Farahnak** | Delivery lead, builds all content | CSA, Microsoft Denmark. Delivered the Novo DPSE GitHub Copilot workshop at Microsoft Lyngby, Dec 2024. Not permitted to deliver billable onsite in the US (legal/visa) → prep billable, delivery free. |
| **Mike Podolski** | Account lead — Senior Customer Success Account Manager | Moved to Industry team Jul 2026; Novo moved with him ("still SMB, was hoping they might get moved up to SMC"). Owns customer cadence, dispatches, deck versions. May attend onsite "for a couple of days". |
| **Jackie Kelly** | Power Platform / Q&A support | Runs the TUBs with Novo NA; built Power Automate workarounds for David; delivering ~1h on Day 2 (connectors, Dataverse, Power Automate flows → code apps). |
| Martin Nielsen | Novo account team (DK) | Drove the GitHub re-onboarding engagement; posts account updates; in brainstorm chat. |
| Lukkas Hamann | In brainstorm chat | — |
| Mark Bisbjerg | Ali's manager | Weekly 1:1s; **Connect FY27 H1 on 8 Sep** — confirm prep days + travel week. Ali (20 Jul): "I need to justify with my local manager as I have a lot of requests locally I am declining." |
| Rafia Floyd, Corey Satnick | April thread + TUB chat | Corey leaving the account for the next Unified agreement year (Mike, 22 Jun). |
| Katrina Fugl → Katrine Garde, Rebecca Jensen | CSAMs on Novo (DK) | Katrina rotated off; Katrine & Rebecca new (Jul 2026). |
| Hossein Zahed | AI Open Office speaker | AI Gateway session, 30+ attendees; compiled FinOps answers for Novo. |
| Simona Toader | — | Ali forwarded the ACR thread 23 Apr suggesting joint delivery. |
| Christian Presley | — | Referenced the internal trial-org process: "gh-msft-innersource/GitHubWorkshops has instructions to join the security group to get a trial organization… (i.e. golden ticket)". |
| Anders Ravnholt, Klaus | DK colleagues | Asked Ali to join the Global Hackathon 14–17 Sep — **unresolved, clashes** (§13). |

### Novo Nordisk

| Name | Role | Notes |
|---|---|---|
| **David Santos (DVSO)** | Senior Manager, Digital Solutions, NN NA — sponsor | dvso@novonordisk.com. Authored the two-stage SOC 2 agent spec (Appendix A). "keen on anything agentic, but stressed that anything AI related will be welcome." Ordered a loaner Windows laptop to test Ali's instructions. Wants to review the training with a participant before the event. |
| **Susan Ames (SUAS)** | Program manager for the Princeton site | suas@novonordisk.com. Internal advertising/recruitment; "not super technical" — wanted PPTX/PDF, not HTML. |
| **Bill Leeson (WPLJ)** | Digital Solutions team | Owns the 200-page-document / 5 MB problem. Wants to "inject autonomous agents into some highly manual work processes." Debugged Work IQ MCP tool descriptions himself. |
| Karis Felthouse (KIFL) | TUB participant | Shared "Using AI to surface unreported GLP-1 side effects in Reddit posts". |
| Anja Letz Imner (AJE) | GVP Enterprise AI; **interim CISO from 1 Sep 2026** | Reorg (announced 21 Aug): Infrastructure & Information Security split into two orgs; Mark Navas (MNV) leaving; Shafik Tawadros (SSL0) interim IT Infrastructure. *An "Anja Leth Zimmer (AJZE)" was cc'd on Ali's Dec 2024 workshop thread — likely the same person (spelling differs across sources); **verify**. If so, a warm contact for the security questions this hackathon will raise.* |
| John F. Kuckelman | Group General Counsel | Met Antony Cook (CVP, Deputy GC) 1 Sep on AI Governance & the Future of Legal. |

---

## 3. Timeline

Teams timestamps are UTC; calendar times CET.

| Date | What happened | Source |
|---|---|---|
| **Nov–Dec 2024** | Ali delivers **GitHub Copilot — Developer Productivity Workshop** for Novo DPSE (Denmark), in person at Microsoft Lyngby. Requirements mail 21 Nov ("Ability to code and understand…"); thank-you thread 13/17 Dec with OHNE, CLUB, AJZE, MDHF; Ali shared slides + videos; demoed Semantic Kernel + local OpenAI-compatible Docker server for "offline mode" questions. | Email |
| **3 Apr 2026** | Mike: *"Low Code / Pro Code / GitHub Copilot @ Novo Nordisk NA"* to Ali, Jackie, Rafia, Corey (cc Martin, Katrina, Kirstine Hvid). Ali: "we could schedule an intense onsite one-week hackathon so they can feel confident about GitHub Copilot, and in parallel make sure both options are crystal clear to them (Pro Code vs. Low Code)… the local CSAs should be the first priority for the long-term relationship." | Email |
| 8 Apr | RMOT2026040305179382 (Visual Studio (P), Novo Nordisk Inc., Princeton) — "already delivered". | Email |
| 15–16 Apr | TUB chat: Jackie helps David surface the Cowork (Frontier) agent in M365 Copilot; shares Work IQ SharePoint reference; builds a Power Automate flow ("when an agent calls a flow") to write to SharePoint because the SharePoint tool was flaky. | TUB chat |
| **23 Apr** | Mike: *"Estimating potential ACR and AI gains with GitHub Copilot services at Novo Nordisk NA"* (to Ali, Martin, Mark Bisbjerg; cc Joseph Mayo) — David's vision, 1,000 people, strong onsite preference; "Ali has done a great job at cutting through David's initial questions and getting to the real business value." Ali forwards to Simona Toader. | Email |
| 28–30 Apr | Request 5613042 (CSA) accepted; dispatch RMOT2026041705206557 confirmed; RMOT2026042905229375 accepted (Ali later billed 15 min to it). | Email |
| **30 Apr** | TUB chat: David posts the **full two-stage SOC 2 agent spec** (Appendix A). Bill: Work IQ Word MCP "create file" writes to OneDrive by design → added OneDrive MCP + updated agent instructions. Jackie asks David for TUB attendance export. | TUB chat |
| 6–7 May | Bill: Cowork Frontier not visible for all Novo users; Mike posts an enablement checklist. Bill brings a new colleague: "ways to inject autonomous agents into some highly manual work processes." | TUB chat |
| **15 May** | **The wall.** Bill: "reliably read a 200-page document and compare its content against a set of predefined criteria, using AI… The 5MB limit for files/data in Copilot Studio is giving us trouble… We'll likely need to mimic the P2P approach with AI Builder… using Copilot Studio alone isn't cutting it." Mike: "for such a large document, chunking is recommended, and Studio/P2P with AI Builder are not robust enough for the task." Jackie: could try Power Automate to chunk. Ali: "You have to use structured output for this... it is straight forward with a api call." | TUB chat |
| 21 May | Ali/Mike: revisit "when we get closer to October if still relevant." Mike: David "would sign up for regular updates like a TUB but tailored and in more technical depth." | 1:1 |
| **27–28 May** | Mike: "will you be able to put together an agenda for the hackathon? Susan… is starting work on the planning so she's looking for materials to start advertising and promoting it internally." Ali builds an HTML deck via Cowork; Mike needs PPTX/PDF for Susan; Ali supplies the source prompt (Appendix C); Mike re-runs it with the date changed to Oct 2026 → **v1 PDF** (28 May 14:00). TUB that day skipped — nobody could join. | 1:1, OneDrive, TUB |
| **10 Jun** | Mike meets David & Susan; October date being set. David's requested shape: Day 1 basics for everyone (Ali's intro), Day 2 hackathon for everyone, Days 3–5 for experienced/advanced with ≤4h classroom/day. Mike: "these engagements usually take MORE time because when lightbulbs go off, people start asking what if…"; "you'll have Jackie to help." Mike creates **"NN NA Hackathon October 26 Brainstorm"** (Ali, Mike, Jackie, Martin, Lukkas): "3-5 is a goldmine for us"; "David is keen on anything agentic"; in-person possible "if there is budget for anyone to join Ali on the trip." Ali proposes **AI evaluations** breakout: "how do you measure and monitor the success of your AI solutions upfront and continuously." | Brainstorm chat |
| 12 Jun | Mike doing Planner training with Susan, "hoping she can finalize some hackathon dates real soon." A DK-STU-delivered US workshop (Christian, Frederik; possibly Power BI) — Mike curious about tie-in. | 1:1 |
| **16 Jun** | Mike asks Ali to take David's **SOC 2 agent PoC** as a remote "AI proof of concept dispatch": "An agent that can automatically run (e.g. SharePoint), read a SOC 2 report, and populate a vendor output report… They've tried this with Copilot Studio but it's hitting the bounds of that platform." Ali: "Should be possible to build with Pro Code"; "Copilot Studio is limited"; declines new work this FY; Mike to try RCs / a local CSA. *Whether anyone picked it up since: unknown.* | 1:1 |
| **22 Jun** | Mike: **"NN firmed up 10/26 as the week for delivery Ali and Jackie."** Also: losing Corey next Unified year — "would it make more sense to have a PBI EDE? Could we work in PBI topics to pair well with the hackathon and breakout sessions?" (unanswered). | Brainstorm chat |
| 26 Jun | Separate Novo thread *"Help regarding GitHub"* — after "the recent attack on Novo Nordisk, we are taking a critical look at our GitHub setup." | Email |
| **1–2 Jul** | Martin: Novo reopens developer access on a **new GitHub instance**; 1,100 developers in 24h; ambition 8,000; GitHub + Copilot + GHAS single platform; Open Office sessions planned. | Account channel |
| **14 Jul** | Mike shares **v2** (*Novo-Nordisk-GitHub-Copilot-Hackathon v2.pptx/pdf*): "days 1 and 2 being learn and build, then 3 to 5 being advanced topics." Ali: "This is a good draft and proposal then we can refine it one more time in september… day 1 and 2 is more intro and get started." Mike: moved to Industry; Novo came with him. | 1:1 |
| **20 Jul** | **Alignment session** (Appendix B): audience + why per track; days 3–5 = 4h, 10am–3pm ET; topic list; Ali builds all content + review calls with David; commercials; 9 prep days; agreement/package IDs; **v3** deck + `prompt.txt`; folder shared. | Brainstorm + 1:1 |
| **6 Aug** | Cadence with David agreed (9–10am ET / 4–5pm CET; 2–3× in September; Ali on vacation the following week). Ali self-dispatched **ROSS2026072005388609** — Mike: "dispatch looks good, drawn on correct package and line item." Internal blocking invites sent ("week of 10.26.26"). Mike creates **"[EXTERNAL] Novo Nordisk NA Hackathon 20261026 Planning"** (Mike, Susan, Jackie, Ali, David) and shares *Novo Nordisk 20261026 Hackathon Planning.docx* — single open question from David: "we really need to test and understand what software they need to have on the laptop and permission. I ordered a loaner windows machine to test out Ali instructions." First call set for 14 Sep. Ali asks "Where I have to be onsite? I have to plan and reserve the logistics" → Mike to send address. | 1:1, External chat, Planning.docx |
| 12 Aug | Anders Ravnholt: "har du lyst til at arbejde med Klaus og mig på et hackathon 14-17 sep?" Ali: "Ja kan vi godt" → Anders to talk to Klaus — **never closed.** | 1:1 |
| 21 Aug | Novo reorg announced (effective 1 Sep). Martin's coffee update: AI Open Office momentum (next: Agent 365 Security & Governance, ~80 invited); **Novo-exclusive Ignite Keynote at Microsoft Lyngby, 17 Nov**; first FY27 Unified add-on (~$100K, Sheng Zhu half-time to Clinical Development); Mission Critical Support positioned vs AWS. | Account channel |
| **27–28 Aug** | **Jackie 1:1.** Jackie: David "wants to make sure we have a clear agenda and he is able to test access for users with enough time beforehand since their policies are so restrictive." Ali: "I will start building the content from September 9. Do we have the number of users and their email addresses, and do they have access to GitHub Copilot?" Jackie: no total yet — "I can get that from David and Susan"; "they are getting everyone access to GitHub Copilot"; **"they cannot use Node.js because it's blocked for all non-IT laptops"**; David "wants to review the training with us and a participant since some other GitHub activities/permissions may prevent advanced GitHub actions"; **"day 1 and day 2 will be 6-hour days with them, and the rest we'll plan for half-days"**; on Day 2 Jackie gives "an overview of Power Platform connectors, Datavers, Power Automate flows, etc. connected to code apps… about an hour." | Jackie chat |
| 31 Aug | Full discovery across M365; GitHub agentic research; environment/identity decisions (§9); build prompt authored. | This work |
| **2 Sep** | Org **`agentic-dev-labs`** and the initially private template repo created. Corrected scaffold record: commit `d83f28c`, 31 files, committed and pushed (§11). | Terminal log and Git history |

---

## 4. The proposal (v3, 20 July 2026)

**Deck:** *Novo-Nordisk-GitHub-Copilot-Hackathon v3.pdf / .pptx* (8 pages). Cover: "MICROSOFT × GITHUB — GitHub Copilot Hackathon — Princeton, New Jersey · October 26, 2026 — Prepared for Novo Nordisk — North America — A hands-on workshop — five days from idea to a deployed app."

**Prep list** (from `prompt.txt`): GitHub starter repo, Azure playground subscription, Dataverse template, prompt templates, custom agents, MCP connections.

| Day | v3 content | Audience | Why (as written) |
|---|---|---|---|
| **Mon 26 — Hackathon Start** | Fusion Team rollout — "Business and technical people team up on GitHub and Copilot — one shared way of working." Vibe Coding Training — "Build by describing what you want in plain language and letting Copilot draft the working code." | Line of Business | "Line of Business teams learn to turn their application ideas into reality — fast." |
| **Tue 27 — Hackathon Build** | Morning — Build ("Copilot as your pair"). Afternoon — Showcase ("Demo your app to the group"). | Line of Business | same |
| **Wed 28 – Fri 30 — Deep dives** | "focused four-hour deep dives… 10am to 3pm ET, with an hour for lunch" | Low-coders + pro-coders | "Build real depth in the skills that take an app from prototype to production." |

**Days 3–5 topics:** Advanced Copilot patterns — custom agents, MCP, cloud agent, PowerApp-to-pro-code patterns · Production readiness — CI/CD pipelines, deployment to Azure App Service · Production polish — AI code review, security review · AI evaluations — "Continuously measure and monitor how well your AI solutions perform." "AND MORE — We'll shape the agenda around what your teams want to learn — bring your ideas."

**Outcome slide:** "01 Confidence to build pro-code apps with AI. 02 Hands-on the whole way — not slideware. 03 Idea to a deployed app, in one week."

**Deck lineage:** v1 (28 May; generated from Ali's prompt — originally "Princeton, July 2026", re-run to October) → v2 (14 Jul; LOB / advanced split) → v3 (20 Jul; audience + why per track; 10–3 ET). All in Mike's OneDrive: `Documents/Customers/Novo Nordisk/2026-10 Hackathon/` — Planning.docx (6 Aug), v1.pdf, v2.pdf + .pptx, v3.pdf + .pptx, prompt.txt.

**Ali's earlier Novo assets** (own OneDrive, folder *GitHub CoPilot Novo Nordisk*): *GitHub CoPilot Novo Nordisk.pptx*, *Semantic Kernel Novo Nordisk.pptx*, demo videos 1–4.mp4, and `gh.txt` — the Dec 2024 run-sheet: show enterprise → VS settings for Copilot → **"Open Codespaces for cities and devcontainer.json, explain benefit of branching and its policies"** → indexing & semantic ranking (Copilot Enterprise) → videos → WhatsApp Copilot + GitHub automation → models → extensions → Cities CRUD API demo (record struct, list of 10 biggest cities, CRUD, README, tests) → WhatsApp/ACS 4096-character chunking fix.

---

## 5. Agenda changes since v3 (not yet in any deck)

| Item | v3 says | Now (Jackie, 28 Aug) |
|---|---|---|
| Days 1–2 length | not specified | **6-hour days** |
| Days 3–5 length | 4h, 10am–3pm ET | **half-days** |
| Day 2 | build + showcase | **+ ~1h Jackie** — Power Platform connectors, Dataverse, Power Automate flows → code apps |
| Internal blocking invite | — | 14:00–22:00 CET (08:00–16:00 ET) all five days — matches neither |
| GitHub Spark | not mentioned | make sure it stays out — **retired** (no new users/apps from 4 Aug 2026) |

→ **Produce v4 before the 14 Sep call.** Ali promised a September refinement on 14 Jul.

---

## 6. Customer background & the real use case

### Who they are
Digital Solutions, Novo Nordisk Inc. (North America), Princeton. A Power Platform / Dataverse shop moving toward fusion teams. In active use: M365 Copilot, Cowork (Frontier), Copilot Studio, AI Builder, Power Automate, **Work IQ MCP** (Word / SharePoint / OneDrive). They are **not** MCP novices — Bill found and fixed an MCP tool-description problem himself. Pitch MCP as "the same MCP, now with real code around it."

### The live problem — third-party vendor privacy assurance
David has written a complete two-stage agent (Appendix A, verbatim):

1. **Analyse** a SOC 2 report → extract vendor/system, data types (only PII / PHI / payment / employee / none), hosting region, data residency, sub-processors, SOC 2 type & date → evaluate **10 controls**, each returning **Pass / Fail / Unclear + a direct quote as evidence + one plain-language sentence of reasoning** → score /10 → sensitivity High (PII/PHI) / Medium (employee/payment) / Low → 2–3 sentence factual executive summary → structured JSON with fixed keys → GapsList (Fail/Unclear only, each with a recommended next step).
2. **Report** — fill `Privacy_Review_Report_Template.docx` `{{PLACEHOLDERS}}` from the JSON; auto-clear when score ≥ 9; validate that no placeholder remains; save `PrivacyReview_VendorName_YYYY_MM_DD_RunID.docx` to the **ReviewReports** SharePoint library; never overwrite the template.

**The 10 controls (David's exact criteria):** 1 MFA enforced for privileged/user access · 2 TLS 1.2+ in transit · 3 AES-256 (or equivalent) at rest · 4 Retention schedule with a defined period · 5 Documented deletion/disposal process · **6 Incident-response SLA ≤ 72 hours · 7 Sub-processor list provided · 8 SOC 2 Type II report dated within the last 12 months · 9 Hosting region/residency explicitly stated and consistent** · 10 DSAR / data-subject-rights handling referenced.

**Where it broke:** 200-page documents vs Copilot Studio's 5 MB limit; Studio / AI Builder "not robust enough"; needs chunking + structured output → **pro-code.** This is the hackathon's hero PoC and the whole "why GitHub Copilot" narrative — supplied by the customer.

**Governance caveat:** real SOC 2 reports are confidential third-party documents. The template ships
fictional text reports explicitly labelled synthetic. Do not describe that label as a technical
watermark or imply real vendor material has been tested here. Real reports require an approved environment.

---

## 7. Constraints

| Constraint | Detail | Implication |
|---|---|---|
| **Node.js blocked** | "blocked for all non-IT laptops" (David via Jackie). IT-issued laptops probably have it — **confirm for Days 3–5**. | No local `npm`. Node runs only in the Codespaces container / Actions runner. LOB days = zero local install. |
| **Restrictive GitHub permissions** | "some other GitHub activities/permissions may prevent advanced GitHub actions." | Cloud agent needs: enabled at org (off by default), **write** access, Copilot as ruleset bypass actor. |
| **Post-incident estate** | All GitHub/ADO access removed May 2026; new instance since 1 Jul; security org being re-founded 1 Sep. | Verify the account and repository ownership model, access policy, and current cloud-agent support. Do not infer organization-repository support from restrictions on managed users' personal repositories. |
| **Regulated (GxP) pharma** | Feature enforcement and document-handling rules differ by client and environment. | Use synthetic data, approved access, and the current supported-surfaces reference. Instruction files, hooks, or a template alone do not establish compliance. |
| **Ali can't deliver billable onsite** | Legal/visa (Microsoft Denmark). | Delivery free; prep billable; DK covers Ali's time. |
| **Time** | 8 weeks; content from 9 Sep; ~11 prep days dispatched. | No identity-infrastructure projects (EMU etc.). |

---

## 8. Historical technical research - GitHub agentic stack (31 Aug snapshot)

Do not use historical version, billing, or support claims below as current prerequisites.
Recheck product documentation and the actual presenter client during rehearsal.

| Capability | Status | Node on laptop? | Key facts |
|---|---|---|---|
| **Copilot cloud agent** (docs renamed from "coding agent") — issue → draft PR | GA. **Off by default** on Business/Enterprise (admin enables). **Unavailable on repos owned by managed user accounts (EMU)** — verify scope for org-owned repos inside EMU. | **No** — browser/mobile only | Ephemeral GitHub Actions environment, customised via `.github/workflows/copilot-setup-steps.yml` (job must be named exactly `copilot-setup-steps`; only honoured on the default branch; keys: steps, permissions, runs-on, services, snapshot, timeout-minutes ≤59). Limits: one repo, one branch, **exactly one PR per task**, **59-minute hard cap**. Only **write-access** users can trigger; pushes only to `copilot/` branches; draft PRs must be human-reviewed; workflows need "Approve and run". Incompatible rulesets **block it** → add Copilot as **bypass actor**. Firewall on by default (recommended allowlist) but **does not cover MCP servers or setup steps**; not compatible with self-hosted/Windows runners. Built-in first-line code review. |
| **Copilot CLI** | GA | **No** — `winget install GitHub.Copilot` (Windows; needs PowerShell 6+), `brew install --cask copilot-cli`, `curl -fsSL https://gh.io/copilot-install \| bash`, or direct binary. Only `npm install -g @github/copilot` needs Node 22+. | `copilot -p "…"` non-interactive; `-s` silent; `--no-ask-user`; `--allow-tool` / `--deny-tool`; `/delegate` to cloud agent; `/review`; `/fleet`; custom agents/skills/MCP; admins can block `--allow-all` / `--yolo` on Business/Enterprise. Auth via `/login` or PAT with "Copilot Requests" permission. |
| **VS Code Copilot** | GA | No (bundled runtime) | Agent mode; **custom agents** = `.agent.md` in `.github/agents` (frontmatter: `tools`, `model`, `mcp-servers`, **`handoffs`**, subagents) → Planning → Implement → Review chains; instruction files (`.github/copilot-instructions.md` + path-scoped) and prompt files; `.vscode/mcp.json` (`http` remote or `stdio` local); MCP gallery; parallel sessions; delegate to cloud agent; per-agent model choice. |
| **Mission control / Agent HQ** | Public preview | No | "a single command center to assign, steer, and track the work of multiple agents." **Claude and Codex** assignable to issues/PRs (public preview; one premium request per session). Jules / Devin / xAI announced, not shipped. "Agents working in parallel can create merge conflicts if they touch the same files. Be thoughtful about partitioning work." |
| **GitHub MCP server** | GA | **No** — remote `https://api.githubcopilot.com/mcp/` ("no local setup or runtime required") or local Go binary / Docker | `/readonly` suffix or `--read-only`; lockdown mode; ~20 toolsets via `/x/{toolset}`; default = context, repos, issues, pull_requests, users; org policy can centrally manage MCP. Remote server includes `create_pull_request_with_copilot`. **Workshop browser automation uses Copilot's built-in browser tools, separately from GitHub MCP; no extra browser server or package is required.** |
| **Spec Kit** | GA v1.0.0 | No — Python / `uv` | `uv tool install specify-cli`; `specify init --integration copilot`; `/speckit.constitution → specify → plan → tasks → implement`; "Works offline, behind firewalls"; regulatory-traceability presets. |
| **GitHub Spark** | **Retired** | — | "Beginning August 4, 2026, GitHub Spark no longer accepts new users or allows the creation of new apps." Remove from any material. |

> **Refreshed 2 Sep 2026.** This table was verified 31 Aug and already had gaps. Missing entirely:
> **Copilot automations** (scheduled / event-triggered cloud agent — David's original ask),
> **hooks** (`.github/hooks/*.json`, `preToolUse` can deny a tool call), **Copilot code review
> approving PRs** (1 Sep), **Agent Plugins 1.0** (GA 12 Aug), **MCP allowlists in enterprise
> managed settings** (6 Aug), and **Copilot in Microsoft Teams** (public preview, 21 Aug).
> The cloud agent also researches/plans/iterates *before* a PR. **Workshop browser choice updated
> 7 Sep:** use Copilot's built-in browser tools rather than installing a browser MCP server.
> Verify availability in the presenter client; do not assume the same tools exist on every surface.
> Several models were deprecated 31 Aug — do not pin a model name. Full write-up in section 15 of `.facilitator/RUN-OF-SHOW.md`.

**Primary sources:** docs.github.com — About cloud agent; Enable coding agent (access management); Customize the agent environment; Firewall; Risks & mitigations; Install Copilot CLI; Configure Copilot CLI; Run CLI programmatically; Content exclusion; About third-party coding agents · code.visualstudio.com — Custom agents; MCP servers; Chat overview · github.blog — "Welcome home, agents" (Agent HQ); "Pick your agent" (Claude/Codex, 4 Feb 2026); Mission control how-to (1 Dec 2025); Spark deprecation changelog (4 Aug 2026) · github.com/github/github-mcp-server (README, docs/remote-server.md) · github.com/github/spec-kit. Full 25-source report: *github-agentic-coding-2026-report.md* (available from the 31 Aug session).

### Node.js vs frontend frameworks — clarified
Node is a **runtime** for developer tooling (`npm install`, Vite dev server, bundlers). Vue / React / Angular are **frameworks**; their built output is HTML/CSS/JS the browser runs with its own engine — no Node. "No Node on the laptop" means **no local build loop**, not "no frontend." Routes: (1) Node in Codespaces or the Actions runner; (2) **buildless** frontends — Vue, Alpine.js, htmx, Tailwind via CDN `<script>`; (3) non-JS stacks — Python (Streamlit, Gradio, FastAPI), Blazor (.NET → WebAssembly), Power Apps. Mapping: Days 1–2 (non-IT laptops) → zero local install; Days 3–5 (likely IT laptops) → full toolchain, **confirm first**.

### Codespaces — **NOT yet verified** (research was cut off)
The devcontainer specifies Python 3.12, Node 22, a locked Python dependency set, tools and editor
settings. Extension IDs do not pin versions, and host requirements are minimums rather than a fixed
machine size. The setup script installs Copilot CLI explicitly. Verify actual build, authentication,
network access, concurrency, prebuild behavior, and costs in a fresh Codespace before delivery.

---

## 9. Delivery environment & identity — decision log

| # | Option | Decision | Reasoning |
|---|---|---|---|
| 1 | Deliver in **Novo's own GitHub org** | **Preferred for Days 3–5** | Real identity, licences already assigned, code stays in their tenant, and it's the estate scaling to 8,000 developers — "the friction *is* the content." Cost: David's admin pre-work (a checklist, not a project). |
| 2 | **Ali's paid GitHub Enterprise** (billed via Azure subscription) → org **`agentic-dev-labs`** — standard, **not EMU** | **Chosen for building now + Days 1–2** | Ali controls every switch: cloud agent on, CLI on, Claude/Codex previews on, bypass actor, firewall, Codespaces policy. Fund ~50 Copilot seats + Codespaces. Dependency: attendees can sign in to github.com with a non-Novo-managed account from a Novo laptop. |
| 3 | Microsoft **trial org / "golden ticket"** (gh-msft-innersource/GitHubWorkshops) | **Chase in parallel** | Sanctioned; defensible to Novo security; likely carries entitlements; lead time. |
| 4 | **EMU** stood up from Ali's playground tenant | **Rejected** | Cloud agent unavailable on EMU-owned repos; needs a separate GHEC enterprise + SCIM/SSO (weeks); playground tenant not for customer identities; EMU is the *most* locked-down model — recreates the walls. |
| 5 | Mass-create "demo/PoC" GitHub accounts | **Rejected** | One account per real person (ToS); Ali would hold Novo staff credentials; probably blocked on managed laptops anyway. |
| 6 | Azure **B2B guest** accounts for attendees | **Rejected** | Azure identity ≠ GitHub identity; cross-tenant / conditional-access fights; 50× RBAC. |
| 7 | Deployment approach | **Implemented differently from the original OIDC proposal** | Current workflow uses the `AZURE_CREDENTIALS` Actions secret and Container Apps in one shared training resource group. Unique app names separate deployments. OIDC and one resource group per team are not implemented. |
| 8 | **Template repo** (not clone / fork) → ~10 **team repos** `nn-na-2026-10-team-01…10` | **Chosen** | Independent histories; cloud agent needs write + opens one PR per task; prebuilds, secrets and rulesets amortise at org level. |
| 9 | Invite by **GitHub username** (collected via Jackie → David/Susan), not email | **Chosen** | An email routes to whichever account already holds it (possibly EMU); collecting usernames surfaces problems in September, not at 09:00 on the 26th. |
| 10 | Naming | Org name neutral (no customer name public); `nn-na` only in private repo names | Trademark/impersonation optics; org reusable for Ferring, LEGO, GN, Energinet work. |
| 11 | Org hygiene **before inviting anyone**: base permission → **No permission**; org rulesets with Copilot bypass; org secrets; Codespaces spending limit; cloud agent enabled; members may create repos | **Do first** | GitHub's default base permission is *Read* → every member could read every private repo, including this brief. |
| 12 | Data | **Synthetic SOC 2 only** in template and Azure; real vendor docs stay in Novo's tenant | Confidential third-party documents; GxP. |

**Recommended arc:** Days 1–2 in `agentic-dev-labs` (Codespaces in the browser, everything enabled, zero friction — the lightbulb). Days 3–5 in Novo's org with David's admin pre-work — the transferable win. Fallback if external-org access is blocked: deliver everything in Novo's org.

---

## 10. PoCs proposed

1. **Vendor assurance teaching workflow** - UTF-8 Markdown/text input, whitespace-word chunks,
   ten rule-based controls, evaluator JSON, and a Markdown report. The three agents verify and
   present calculated results. PDF OCR, 200-page throughput, Word output, SharePoint delivery,
   executive-summary generation, and automatic risk clearance are not implemented by this template.
2. **Dataverse-backed app, agent-built** — file an issue → assign to Copilot → review the draft PR live. Serves David's "business owns apps / my team owns the data model" split; hooks into Jackie's Day 2 hour.
3. **Copilot CLI on a locked-down laptop** — `winget`, no admin, no Node. The trust-builder.
4. **Multi-agent split** — one issue to Copilot and Claude in parallel, compare the PRs; teaches partitioning.

---

## 11. Repo plan & build status

**Org:** `agentic-dev-labs` · **Template:** `agentic-dev-labs/copilot-hackathon-template`
(last observed internal) · **Governance:** `agentic-dev-labs/.github-private` · **Planned team
names:** `nn-na-2026-10-team-01…10` · **Rehearsal repo:** `nn-na-2026-10-team-00`.
This list is not a fresh inventory or permission check.

**`.github-private` — one repo, three jobs** (created 3 Sep, commit `ab756f2`): `agents/vendor-analyst.agent.md` gives an **org-level** agent to every repo in the org without repo access; `copilot/managed-settings.json` is what the **enterprise** points at once the org is selected as source of governance (additive only — registers the marketplace and auto-installs the plugin; deliberately no `strictKnownMarketplaces`, which is enterprise-wide and would block the `ali/*` and `work-iq/*` plugins); `.github/plugin/marketplace.json` + `plugins/vendor-assurance/` is the **marketplace**. **Gotcha:** `enabledPlugins` fetches plugin files as the signed-in user, so every attendee needs **read access** to this private repo or the install fails silently.

```
.devcontainer/devcontainer.json + setup.sh  Python 3.12 + Node 22 + CLI tools; uv.lock; shared extension IDs
.github/copilot-instructions.md          training repo · Python · synthetic only · quote evidence · no secrets
.github/ISSUE_TEMPLATE/agent-task.md     issue shape for the cloud agent
.github/agents/vendor-analyst.agent.md · report-writer.agent.md · reviewer.agent.md
.github/workflows/copilot-setup-steps.yml · deploy.yml (Actions credentials → Container Apps) · ci.yml
labs/00-setup … 08-deploy               (09 labs; Jackie's hour is separate from Lab 05)
src/vendor_assurance/chunker.py · evaluator.py · report_writer.py · cli.py · templates/ · samples/synthetic_soc2_report.md
tests/test_chunker.py · test_evaluator.py
docs/PREREQS.md · AGENDA.md · FACILITATOR.md · README.md · pyproject.toml · .gitignore
```

**Built 2 Sep 2026 via Copilot CLI** (resume: `copilot --resume=98337cac-2ce4-46d4-9be1-972e22e2705d`). **Corrected 2 Sep from git:** the scaffold commit is **31 files, +934 / −1** (not the 71 files / +980 / −16 first recorded), and it is **committed and pushed** — `d83f28c` on `origin/main`. `BUILD_PROMPT.md` was already deleted. Verification passed: pytest; CLI ran end-to-end with a placeholder-free report; YAML, JSON and agent frontmatter valid; ruff clean; no `npm install` in required steps. Intentional placeholders: `<TEAM_NAME>`, `<DATAVERSE_API_URL>`, `[Confirm with facilitator]`, `${{ secrets.* }}`.

**Fixed 2 Sep.** Controls 6–9 now match David's checklist exactly (incident-response SLA ≤72h, sub-processor disclosure, SOC 2 Type II within 12 months, data-residency consistency) across `evaluator.py`, `vendor-analyst.agent.md` and the synthetic sample. Two further defects found and fixed in the same pass: the **data-sensitivity mapping was inverted** (PII was scored Medium and payment High; David's spec is High = PII/PHI, Medium = employee/payment), and the spec's **GapsList** was missing entirely — now generated with a recommended next step per non-Pass control. Synthetic sample scores 8/10, sensitivity High.

**Added 2 Sep — `labs/07-automations-hooks`.** Research on 2 Sep found two capabilities the 31 Aug snapshot missed. **Copilot automations** run the cloud agent on a schedule or on issue/PR events — this *is* David's original 16 Jun ask ("an agent that can automatically run"). **Hooks** (`.github/hooks/*.json`) log or *deny* tool calls, which is the GxP audit answer. Day 4 is now the governance/production day and Day 5 is multi-agent + evaluations.

**Verification boundary:** the template flag, sample team repos, and some service tests were
reported in earlier sessions. Do not repeat the initial "not done" list as current fact. A complete
fresh-Codespace rehearsal and current seats, service access, budgets, and policy state still require
live checks. No invitations, purchases, or enterprise policy changes are performed by this code audit.

**Day mapping:** D1 = labs 00-02 and 08; D2 = Jackie's hour, Lab 05, team build and showcase;
D3 = labs 03-04; D4 = Lab 07, code review and Container Apps; D5 = author agents and skills in
Lab 06, evaluations and final demos. `docs/AGENDA.md` is the working timetable.

---

## 12. Commercials & logistics

- **Model:** onsite delivery non-billable; prep billable. Ali (20 Jul): "Yeah I am not allowed to deliver on billable onsite… if [I] go there for free then its purely a Microsoft Denmark investement… the only way for me to get hours then is the hours and days I spend to prepare for this remotely." Mike: "as you say, we can certainly bill everything for discussions and prep."
- **Agreement 185945054 / package 189101145** (Mike, 20 Jul). "~680 hours total" in the bucket at FY start. Fixed bucket vs case labor left to Ali: "entirely your choice Ali, we have plenty of resources to use, and the customer wants this, so have at it."
- **Dispatch:** Ali self-dispatched **ROSS2026072005388609** (6 Aug) — confirmed on the correct package and line item. Earlier references: RMOT2026042905229375 (15 min billed), RMOT2026041705206557 (dispatch confirmation), RMOT2026040305179382 (already delivered), Request 5613042 (CSA).
- **Prep days proposed (20 Jul):** 19–21 Aug, 9–11 Sep, 23–25 Sep = 9 days ("should I book 3 days more for safety?" — "entirely your choice"). **Actual GRM dispatches:** 5796995 (9–11 Sep), 5797029 (16–18 Sep), 5820109 (21–23 Sep), 5797009 (23–25 Sep) → ~11 days; the August block never happened (vacation); **23 Sep overlaps**.
- **Delivery dispatch anomaly:** **5855920 — "Novo Nordisk A/S | GitHub - Copilot", 19–23 Oct 15:00–23:00 CET** — the week *before* the event and the Danish entity (all prep dispatches say "Novo Nordisk Inc."). **Confirm with Mike.**
- **Travel:** approved 25 Oct – 1 Nov. Venue address requested 6 Aug — not received. Flights/hotel status unknown. Mike may attend two days.
- **Manager alignment:** Mark Bisbjerg — Connect FY27 H1 on 8 Sep; confirm prep days + travel week.
- **Open commercial idea:** PBI EDE / PBI topics paired with the hackathon (Mike, 22 Jun) — unanswered.

---

## 13. Calendar

| When (CET) | What |
|---|---|
| Tue 8 Sep 09:00–10:00 | Connect FY27 H1 — Ali/Mark Bisbjerg |
| 9–11 Sep | Prep dispatch 5796995 — **content build starts 9 Sep** |
| **Mon 14 Sep 15:00–16:00** | **Microsoft Hackathon @ Novo Nordisk — Preparation** (Mike; Susan, David, Ali accepted; Jackie tentative) |
| 14–17 Sep | ⚠ Global Hackathon ask from Anders/Klaus — unresolved clash |
| 16–18 Sep | Prep dispatch 5797029 |
| **Fri 18 Sep 15:00–16:00** | **Preparation — Session 2** |
| 21–23 Sep / 23–25 Sep | Prep dispatches 5820109 / 5797009 (overlap 23 Sep) |
| 19–31 Oct | "Novo Nordisk GitHub" — Ali's own block |
| 19–23 Oct 15:00–23:00 | ⚠ Resource Assigned 5855920 (Novo Nordisk **A/S**) — verify entity and week |
| 25 Oct – 1 Nov | Travel approved |
| **Mon 26 – Fri 30 Oct 14:00–22:00** | Novo Nordisk North America — Hackathon [Internal Blocking] (Mike; Jackie) — no location on invite |
| Tue 17 Nov | Novo-exclusive Ignite Keynote, Microsoft Lyngby — natural follow-on |

Recurring: *Microsoft x Novo Nordisk — AI Open Office* (Ali declined 7 & 17 Aug).

---

## 14. Open items (prioritised)

| # | Item | Owner | By |
|---|---|---|---|
| 1 | Answer David's laptop / software / permissions question (**open since 6 Aug**) — send `docs/PREREQS.md` + Appendix D | Ali | this week |
| 2 | Confirm with Novo: EMU or SSO? Can accounts join an external org? Copilot entitlement outside Novo's enterprise? github.com + Codespaces reachable from Novo network? Node on IT laptops for Days 3–5? | David via Jackie | before 14 Sep |
| 3 | Attendee count per track + **GitHub usernames** | Jackie → David/Susan | before 14 Sep |
| 4 | Deck **v4**: 6h Days 1–2, half-day Days 3–5, Jackie's hour, no Spark; fix internal-invite hours | Ali / Mike | 14 Sep |
| 5 | ~~Align evaluator/agent controls 6–9~~ **DONE 2 Sep** (plus inverted sensitivity + missing GapsList) | Ali | ✓ |
| 6 | ~~Delete `BUILD_PROMPT.md`; commit + push template~~ **DONE**. Remaining: flag as template; org settings (§9 #11); team-00 dry run | Ali | this week |
| 7 | Chase the golden-ticket trial org in parallel | Ali | this week |
| 8 | Close the 14–17 Sep Global Hackathon ask with Anders/Klaus | Ali | now |
| 9 | Dispatch tidy: 23 Sep overlap; 11 vs 9 days; **5855920 entity (A/S) and week (19–23 Oct)** | Ali + Mike | Sep |
| 10 | Venue address; flights/hotel | Mike → Ali | Sep |
| 11 | Codespaces verification — cost, region, concurrency; set org spending limit | Ali | before buying seats |
| 12 | Copilot seats (~50) + Codespaces budget in `agentic-dev-labs` | Ali | Oct |
| 13 | Dry run with David + one participant on the loaner laptop (his request) | Ali / David | late Sep |
| 14 | Re-verify preview features (Claude/Codex, mission control) | Ali | week of 19 Oct |
| 15 | Align with Mark Bisbjerg on prep days + travel | Ali | 8 Sep |
| 16 | Decide on PBI EDE pairing (Mike's 22 Jun idea) | Mike | — |
| 17 | Follow-on: connect to Novo's GitHub/GHAS onboarding workstream and the 17 Nov Ignite Lyngby session | Ali / Martin | Nov |

---

## 15. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Novo accounts can't join an external org (EMU) | Days 1–2 plan in own org fails | Ask now; fallback = deliver all in Novo's org with admin pre-work; golden ticket |
| Cloud agent silently blocked (disabled / no write / ruleset) | Flagship demo fails | Org settings checklist; bypass actor; team-00 dry run |
| Copilot seats missing on Day 1 | "A Copilot hackathon without Copilot" | Fund seats in own org; confirm Novo entitlement scope |
| Node blocked **and** Codespaces blocked | No build loop at all | Buildless / Python path decided in September, not in the room |
| Real vendor documents land in Ali's Azure | Data-governance breach | Synthetic only; state it to David in writing |
| Preview churn (Claude/Codex, mission control) | Demo changes under you | Re-verify 19 Oct; keep Copilot-only fallbacks |
| Hours mismatch (deck vs invite vs Jackie) | Confusion on site | v4 + corrected invites |
| Ali double-booked 14–17 Sep | Prep time and scoping call lost | Close the Anders/Klaus ask |
| Delivery dispatch on wrong entity/week | Utilisation not recorded | Fix 5855920 with Mike |

---

## 16. Where everything lives

- **Teams — 1:1 *Chat with Mike Podolski*:** all commercials and agenda history (21 May → 6 Aug).
- **Teams — group *NN NA Hackathon October 26 Brainstorm*:** Ali, Mike, Jackie, Martin Nielsen, Lukkas Hamann (10 Jun → 20 Jul; v3 + prompt.txt links).
- **Teams — group *[EXTERNAL] Novo Nordisk NA Hackathon 20261026 Planning*:** Mike, Susan, Jackie, Ali, David (from 6 Aug; Planning.docx).
- **Teams — 1:1 *Chat with Jackie Kelly*:** 27–28 Aug updates.
- **Teams — TUB meeting chat** (Bill, David, Rafia, Corey, Jackie, Mike, Karis): SOC 2 spec (30 Apr), the 5 MB wall (15 May), Work IQ MCP notes.
- **Teams — *Team Novo Nordisk Ext – Coffee Update Chat*:** account news (GitHub reopening, reorg, Ignite, AWS).
- **OneDrive (Mike):** `Documents/Customers/Novo Nordisk/2026-10 Hackathon/` — Planning.docx, v1/v2/v3 decks, prompt.txt.
- **OneDrive (Ali):** `GitHub CoPilot Novo Nordisk/` — decks, videos, gh.txt.
- **Email:** meeting receipts only, plus the April 2026 threads (Low Code/Pro Code; ACR gains; dispatch confirmations) and the Dec 2024 DPSE workshop threads.
- **GitHub:** `agentic-dev-labs/copilot-hackathon-template` (last observed internal).
- **Research:** *github-agentic-coding-2026-report.md* (31 Aug session).
- **Transcripts:** none exist for this engagement.

---

## Appendix A — David Santos's SOC 2 agent spec (TUB chat, 30 Apr 2026 — verbatim, lightly formatted)

### Stage 1 — Analyse

**Step 1** — Extract the following high level details from the document: Vendor or system name · System or product name if different · Data types processed. Use only these values: PII, PHI, payment, employee, none · Hosting region · Data residency statement · List of sub processors if stated · SOC 2 report type. Type I, Type II, or None · SOC 2 report date if present.

**Step 2** — Evaluate each SOC 2 checklist item below. For each item return three values: **Result** (Pass, Fail, or Unclear) · **Evidence** (Direct quote from the document) · **Reasoning** (One short plain language sentence explaining why the result was given).

| # | Control | Pass if… |
|---|---|---|
| 1 | Logical access controls | the document explicitly states MFA is enforced for privileged or user access |
| 2 | Encryption in transit | TLS 1.2 or higher is explicitly stated |
| 3 | Encryption at rest | AES 256 or equivalent encryption is explicitly stated |
| 4 | Data retention | a retention schedule with a defined time period is stated |
| 5 | Data disposal | a documented deletion or disposal process is stated |
| 6 | Incident response | an incident response SLA of 72 hours or less is stated |
| 7 | Sub processor disclosure | a list of sub processors is provided |
| 8 | SOC 2 currency | a SOC 2 Type II report dated within the last 12 months is stated |
| 9 | Data residency | a hosting region or residency is explicitly stated and consistent |
| 10 | Data subject rights | DSAR or data subject rights handling is referenced |

**Step 3** — Score is the count of Pass results out of 10.
**Step 4** — Data sensitivity: High if PII or PHI is present · Medium if employee or payment data · Low if none.
**Step 5** — Executive summary: 2 to 3 sentences summarising overall posture, key strengths, any major gaps. Tone must be factual and neutral.
**Step 6** — Structured output. Return JSON with keys: VendorName, VendorSystem, DataTypes, HostingRegion, DataResidency, SubProcessors, SOC2Type, SOC2Date, Score, DataSensitivity, C1_Result, C1_Evidence … C10_Result, C10_Evidence, ExecutiveSummary, GapsList (short bulleted list; only items marked Fail or Unclear; each bullet must include a recommended next step).

### Stage 2 — Report ("You are an internal IT Privacy document generation agent")

Input: the Stage 1 JSON + read-only access to `Privacy_Review_Report_Template.docx`. Task: replace every placeholder with values from the JSON. Do not add new content. Do not rewrite text in the template. Do not leave any placeholder unfilled.

**Step 1** — Open the Word template in read only mode.
**Step 2** — Mapping: `{{VENDOR_NAME}}`←VendorName · `{{VENDOR_SYSTEM}}`←VendorSystem · `{{DATA_TYPES}}`←DataTypes · `{{HOSTING_REGION}}`←HostingRegion · `{{DATA_RESIDENCY}}`←DataResidency · `{{SUB_PROCESSORS}}`←SubProcessors · `{{SOC2_TYPE}}`←SOC2Type · `{{SOC2_DATE}}`←SOC2Date · `{{SCORE}}`←Score · `{{DATA_SENSITIVITY}}`←DataSensitivity · `{{Cn_RESULT}}` / `{{Cn_EVIDENCE}}`←Cn_Result / Cn_Evidence for n = 1..10 · `{{EXECUTIVE_SUMMARY}}`←ExecutiveSummary exactly as provided · `{{GAPS_LIST}}`←GapsList as a Word-formatted bullet list; do not add or remove bullets; if no gaps exist insert "No gaps identified".
**Step 3** — Auto-populated: `{{REVIEW_DATE}}` = current run date · `{{AGENT_RUN_ID}}` = agent run identifier · `{{REVIEWER_NAME}}` = "Auto Cleared by Agent" if score ≥ 9, otherwise leave blank for human completion · if auto cleared: `{{REVIEWER_ROLE}}` = N A, `{{REVIEWER_DECISION}}` = Auto Cleared, `{{FINAL_DECISION}}` = Auto Cleared, `{{FINAL_DECISION_DATE}}` = current date.
**Step 4** — Validation before saving: no `{{ }}` placeholders remain · all checklist rows contain a Result and Evidence · Executive Summary is populated · Score is numeric · Data Sensitivity is High, Medium, or Low. If validation fails: do not save; return an error describing which placeholder is missing.
**Step 5** — Save as a new Word file; do not overwrite the template. File name `PrivacyReview_VendorName_YYYY_MM_DD_RunID.docx`. Save location: **ReviewReports SharePoint library**.

---

## Appendix B — 20 July alignment (key verbatim, Brainstorm chat + 1:1)

- Mike: "updating the agenda again. For days 1&2, and 3 through 5, they want to include a target audience and a why for each. Your original prompt for the agenda set the outcome as 'confidence to build pro-code apps with AI, hands-on not slideware, idea-to-deployed-app in one week'. What would you suggest for each target audience and why?"
- Ali: "My aim was… to have the same group of people following but where we start from a intermediate level to get everyone aligned… Because prior to this most of these people are not even pro code developers any of them, my aim is to enable/adopt Github Copilot for these people so they can start coding and consume AI through Github."
- Mike: "like every customer, and I do mean every customer, they were concerned about having a 5 day commitment, so they wanted to concentrate on the first 2 days for the actual hackathon, and then more technical deep dives 3-5 that attendees can choose from… I think everyone will take days 1 and 2, but the less technical will graze content 3-5."
- Mike: "so David was seeing day 1 as basics, day 2 as hackathon, then 3-5 more technical Q&A and deep dive… it needs to make sense and be a good ROI for them, the struggle is getting teams to commit for 5 days."
- Ali: "day 3-5 is more where they build a simple pro code app on top of dataverse." Mike: "I think labs yes, but in the context of building on dataverse… David's idea was the advanced labs, but maybe you could run a new app through each of the labs as demonstration?"
- Mike (prompt text): "Days 3 through 5 will be for a smaller audience, each day being a tight 4 hours between 10am and 3pm ET (with an hour for lunch), with advanced topics covered… advanced Copilot patterns — custom agents, MCP, cloud agent, PowerApp-to-pro-code patterns; production readiness - CI/CD, App Service deployment; production polish — AI code review, security review; AI evaluations - how to continuously measure and monitor the success of your AI solutions."
- Ali: "Then I will build workshop content for all the days and do calls with David to get his feedback on what I put together."
- Mike: "for now I will update the target audience to LOB teams for 1 and 2, and more targeted audience for 3-5. The why for 1 and 2 can be to learn and build an app quickly with AI, why for 3-5 can be deeper dives into more technical subject matter for both low and pro coders… I think it will be good… to have a call with David and just make sure I am not mis-translating between us." Ali: "Yes for sure lets have continuous meeting with him on this… Lets do it in August where I start."
- Mike: "I was surprised it took that long to get a decision, this is like a trojan horse to win their AI business more broadly." Ali: "I was actually surprised they still wanted to do it, I was already considering this opportunity to be lost."
- Ali: "reason why they approve is because we see this as an enabler and if dont show them our agents and how to code with our stack I am sure AWS and competitors happily will take the fruit instead." Mike: "and if takes off they will need more guidance and spend more on AI."

---

## Appendix C — Source prompts for the deck

**Ali's prompt (28 May 2026):**
> Create a customer-facing PowerPoint/PDF for Novo Nordisk NA's GitHub Copilot Hackathon. Theme: GitHub dark design with Microsoft + GitHub branding. Purpose: sell the workshop, not internal Microsoft value. Include: Title: GitHub Copilot Hackathon — Princeton, July 2026. Prep: GitHub starter repo, Azure playground subscription, Dataverse template, prompt templates, custom agents, MCP connections. Day 1: enterprise GitHub intro, Copilot in VS Code, Copilot CLI, agents/skills/plugins/MCP, repo + Azure handoff, build first app. Day 2: teams propose apps/API/frontend on shared Dataverse foundation, spec-first planning, build kickoff. Day 3: advanced Copilot patterns — custom agents, MCP, cloud agent, PowerApp-to-pro-code patterns. Day 4: production polish — AI code review, security review, CI/CD, App Service deployment. Day 5: final sprint, demos, retro, handoff to Novo environments. Outcome: confidence to build pro-code apps with AI, hands-on not slideware, idea-to-deployed-app in one week. Tone: concise, executive-friendly, customer-facing. Avoid ACR, Microsoft revenue, internal names, or "low-code is dead." Emphasize hands-on learning, GitHub Copilot, Dataverse, Azure App Service, and real deployed apps.

**`prompt.txt` (Mike, 20 Jul 2026)** — same, with: Title "October 26, 2026"; Day 1 "Hackathon Start - Fusion Team rollout with GitHub and Copilot, and Vibe Coding Training"; Day 2 "Hackathon Build - Build an app based on learnings in the morning, showcase apps in the afternoon"; LOB audience/why for Days 1–2; low-coders + pro-coders for Days 3–5, "a tight 4 hours between 10am and 3pm ET (with an hour for lunch)"; topics incl. AI evaluations; footnotes "Monday, October 26th — LEARN / Tuesday, October 27th — BUILD then SHOW".

---

## Appendix D — Access questions to send David & Jackie (paste-ready)

1. Is Novo's new GitHub instance **Enterprise Managed Users** or a standard organisation with SSO? Can attendee accounts accept an invitation to an **external** GitHub organisation?
2. Does the Copilot licence you're assigning work **outside** Novo's enterprise (in an external org)? If not, we'll fund seats for the week.
3. From a Novo laptop on the Novo network, can attendees reach **github.com** and open **GitHub Codespaces** in the browser? Any proxy / TLS inspection we should know about?
4. Do the Day 3–5 participants (pro-coders) have **Node.js** on IT-issued laptops? Days 1–2 will assume zero local install.
5. Please send the **GitHub usernames** and attendee count per track (Days 1–2 vs Days 3–5).
6. If we run Days 3–5 inside Novo's GitHub, an org admin needs to: (a) enable the Copilot **cloud agent** at org level (it is off by default), (b) grant attendees **write** on the workshop repositories, (c) add **Copilot as a bypass actor** on branch protection / rulesets, (d) enable the **Copilot CLI** policy, (e) allow-list internal package registries in the agent firewall.
7. Loaner-laptop core test: open the assigned repository in a browser, create a Codespace,
   sign in with the approved account, run tests, then start `copilot` inside the Codespace.
   No laptop runtime installation is required for the workshop path.

---

## Appendix E — Commands

**Push the template (from `C:\Users\alfarahn\Downloads\copilot-hackathon-template`):**
```powershell
Remove-Item BUILD_PROMPT.md
git add -A
git commit -m "Scaffold hackathon template"
git push
gh repo edit agentic-dev-labs/copilot-hackathon-template --template
```
(UI fallback for the last step: repo **Settings → General → Template repository**.)

**Lock the org down before inviting anyone** (needs `admin:org` scope):
```powershell
gh auth refresh -h github.com -s admin:org
gh api -X PATCH /orgs/agentic-dev-labs -f default_repository_permission=none
```
(UI: **Org Settings → Member privileges → Base permissions → No permission**.) Then enable the Copilot cloud agent and CLI policies, set the Codespaces spending limit, and add org secrets — all in the org's Settings.

**Historical alternative: separate private repository (superseded 2026-09-09).**
The commands below use the original filenames and are retained as planning history, not
current instructions. Current storage and cleanup are described in `.facilitator/README.md`.
```powershell
cd C:\Users\alfarahn\Downloads
gh repo create agentic-dev-labs/nn-na-2026-10-engagement --private --add-readme --clone
Move-Item .\NN-NA-Hackathon-2026-10-Engagement-Brief.md .\nn-na-2026-10-engagement\
cd nn-na-2026-10-engagement
git add -A
git commit -m "Add engagement brief"
git push
```

**Create the team repos later:**
```powershell
foreach ($i in 0..10) {
  $n = $i.ToString("00")
  gh repo create "agentic-dev-labs/nn-na-2026-10-team-$n" --template agentic-dev-labs/copilot-hackathon-template --private
}
```
