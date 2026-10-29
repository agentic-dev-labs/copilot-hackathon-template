# Table support: attendee ideas and where to start

Private facilitator note (git-ignored; real names from the roster). Source: the roster sheet's
"idea" column as of 20 Oct 2026. Ideas are the attendees' own words, shortened. Build everything
with **fictional** sample data; real systems become a question for IT.

How it is used (at the tables all week; on Day 2 David, Jackie and Bill Leeson present and Ali is
table support, so this sheet is busiest then): on **Day 1** an attendee who
picks **My own idea** in `/create-website`, or a fast finisher building a second idea, describes
it in one sentence; on **Day 2** they build that idea at their table; on **Days 3-5** they write
stories for, build, test and publish that same page. The skill starts from the closest tested
pattern. For timings, always look in `final-workshop-david/WEEK.md`.
The two new patterns (20 Oct) are the **Request Tracker** (form, stages, overdue flags, counts)
and the **Team Dashboard** (headline numbers, monthly bars with a what-if forecast, share ring,
editable table). Helpers can nudge: "Describe it as a tracker of ... with stages ..." or
"a dashboard of ... by ... per month".

## People who wrote an idea

| Who | Team | Their idea | Start from | Say this to Copilot (example) | Question for IT later |
|---|---|---|---|---|---|
| JFZK Joohee Kim | CMR, USO PS Qua & GxP | Solution request tool: automation, analytics, reporting and dashboard requests, assignment, approvals, inventory of solutions | **Tracker** | "A request tracker for automation and dashboard requests with stages Submitted, Assessed, Approved, Built, and an owner for each" | Where requests live today (SharePoint/Forms?), approval routing |
| AYTY Amy Taylor | CMR, PT&D | More sophisticated project tracker (status of each project, effectiveness of the new process); later Access database migration | **Tracker**, then a chart | "A project tracker with stages and a chart of projects per stage" | Access migration target and data owner |
| KLUP Kari Belson | Market Access, Patient Support | Master roster of vendor employees, start and training dates for safety compliance | **Tracker** (people as rows, training due date, overdue) | "A roster of vendor staff with start date, training due date and an overdue flag" | Source of the real roster; personal data rules |
| IBGZ Bella Guzzi | P&O, Academy & Franchise | Training incompletion notifications; interactive dashboards | **Tracker** (overdue = incomplete) + **Dashboard** | "A training completion tracker that flags overdue people" | LMS export, email sending |
| BQMC Brian McCluskey (remote, NC) | Legal | Intake many PDF contracts, find signing parties, study numbers, dates, itemized financials | **Tracker** as a contract register | "A contract register with parties, study number, contract date and amount" | PDF extraction service, document storage |
| QZRO Ashley Rose | Market Access, Public Affairs Policy | Workflow engine: legislative/regulatory inputs mapped to brands, risks and opportunities | **Tracker** (policy items with impact and brand) | "A policy radar: each item has a brand, impact High/Medium/Low, and a stage" | Live policy feeds, agents |
| KPVK Kiran Kaur | Market Access, Patient Support Solutions | PSS operations: contracting, program launches, cost savings | **Tracker** or **Dashboard** | "A launch tracker with stages and cost per launch" | Contract systems, cost data |
| MPCA Michele Petracca | P&O, HR | Automate or streamline several processes | **Tracker** | "A tracker of HR process requests with stages" | Which HR system |
| XACL Adrienne Long | Market Access, Public Affairs/Executive | Team information sharing, something usable | **Ideas Wall** or **Tracker** | "An updates board where the team pins news by topic" | Teams/SharePoint instead? |
| ACDF Allie Cohen Dolloff | Legal, CMR | To-do app with Outlook: colour priorities, day/week/month views, meetings and flagged emails as tick boxes | **Calendar** (views) or **Project Planner** (priority chips) | "A to-do list with High/Medium/Low colours and Day, Week and Month tabs" | Outlook integration (Graph) is IT |
| ORDH Rick Hansen | CMR, Clinical data science / Data & Insights | Clinically oriented dashboards for medical affairs, cheaper than vendor builds | **Dashboard** | "A dashboard of (fictional) programme numbers by therapy area per month" | Real-world data sources, validation |
| ZRAR Myriam Asmar | CMR, Medical Affairs | Content/image generator for medical; automate reporting from static Excel sheets | **Dashboard** (report) + **Photo Studio** / picture helper | "A dashboard that replaces my monthly Excel report" | Medical content review rules; Excel source |
| CNVJ Christian Skov Jensen | Finance & Operations, Strategic Finance | The US long-term forecast | **Dashboard** (what-if slider) | "A forecast dashboard by region with a growth slider" | Real forecast model and data |
| SAUB Anubhav Srivastava | Finance & Operations, EDAA | Several agents collaborating as an engineering team | Days 3-4 content (custom agents, cloud agent) | Use the User Requirements and Code Review agents | - |
| AIPH Anil Kumar Pathipati | Marketing & Patient Solutions, Enterprise Insights | "Yes" (no detail) | Ask: probably **Dashboard** | - | - |
| WJED Bill Day | Legal Operations | Will have a concept by then | Ask on the day | - | - |
| HZRW Hannah Walker | CMR, Process Transformation | Not yet | Ask on the day; Tracker suits process work | - | - |
| KSZV Karan Sharma | Finance & Operations, Forecasting | "na" | Suggest **Dashboard** (forecast) | - | - |

## No idea written (suggest by team)

| Team | People | Suggest |
|---|---|---|
| Finance & Operations (Tax, ED&AA) | IGQQ Igor Gryniv (out until 26 Oct), RYRL Ryan Lillie, WSIH Shihan He | Dashboard (deadlines, filings per month) or Tracker (filings with due dates) |
| Market Access (PSS Enablement, PAP Affordability, Public Affairs) | YMPK Malay Parekh, UJIY Jinny Yun, YJPZ Jon Pena, ZMMI Michele Mizrahi, KIFL Karis Felthouse | Tracker (cases or applications by stage) or Dashboard |
| Marketing & Patient Solutions | VSKK Sai Rithvik Kanakamedala | Dashboard |
| CMR USO PS Qua & GxP | UOKL Sonali Kulkarni, WXZP Jacika Patel | Tracker (same team as JFZK: compare designs) |
| Legal Strategy & Operations | CFMC Charles McGovern | Tracker (matters or contracts) |
| DD&IT Data & Insights | VUGN Vivek Gangaramani, BGYM Bigyan Swarup Mishra, TLKS Tamal Santra, PNC Praveen Chand | Dashboard; can help business people at their table |
| DD&IT Global Security | RQLB Racquel Balaoas, MUQD Mehul Doshi, GTMU Geeta Madhuri Adusumilli, KWUC Keith Wunsch, ZDNK DK Kanyangarara | Tracker (findings or access reviews by stage, overdue) |
| DD&IT HCP Engagement | OXQO Omkar Oka, RJLS Jerald Selvaraj, MGRB Marc Greenbaum | Tracker or Dashboard (engagements per month) |
| DD&IT P&O Enablement | MPAZ Maria Pazos, JPIA Jean-Pierre Pereira, AZKQ Azeem Khan | Tracker (onboarding steps) |
| DD&IT GITO, Enterprise Enablement, EDT | IBSR Isabel Struckmeier, HMAM Hamsa Ambarish, POZM Patrick Melo | Tracker (requests) or Dashboard |

## Rules at the table

- Fictional data only: no real names, contracts, patient, vendor or employee data in pages or
  prompts. Say "made-up examples" out loud.
- Integration wishes (Outlook, PDFs, Access, live feeds, SharePoint) go on the IT question list,
  not into the page.
- Pair a DD&IT person with a business table where possible (18 DD&IT, 30 business).
