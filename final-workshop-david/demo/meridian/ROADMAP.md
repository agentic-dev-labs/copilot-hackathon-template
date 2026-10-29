# Project Meridian Roadmap

## Brief
- Project Meridian is a wholly fictional injectable-medicine launch simulation in 12 invented markets, M01-M12.
- The 12-month horizon comprises Q1 (months 1-3), Q2 (months 4-6), Q3 (months 7-9), and Q4 (months 10-12).
- Launch waves activate M01-M04 in month 8, M05-M08 in month 10, and M09-M12 in month 12.
- Every market requires simulated regulatory, supply, packaging, education, access, support, safety, IT, and communications clearance.
- All products, entities, records, decisions, and role slots are invented; this is not clinical guidance or a real regulatory forecast.

## Planning assumptions and launch gates

"Launch" means activation in an isolated rehearsal environment, not medicine distribution or patient treatment. All quantities, budgets, cases, role rosters, and decisions are synthetic. Prices use invented simulation credits. Owners are roles, never named people. No dosing, administration instructions, treatment recommendations, or real product claims are in scope.

Milestone months are completion deadlines. Every listed dependency must finish before its consumer; same-quarter dependencies finish in earlier months. Gates at months 7, 9, and 11 cover the nine readiness domains for their respective waves. All applicable checks must pass, evidence must be re-attested within ten rehearsal business days, and zero critical blockers may remain. A critical blocker is any failed mandatory readiness control; it cannot be waived to meet the deadline. Failed gates stop affected-market activation and trigger corrective replanning. Activation-time checks revalidate clearance and evidence; continuing controls revoke eligibility when evidence expires or a critical defect emerges.

## E01: Regulatory submission

- **First quarter:** Q1

### E01-F01: Fictional market requirements baseline
- **User story:** As a regulatory planning lead, I want a fictional requirements baseline so that all teams share one submission scope.
- **Quarter:** Q1
- **Milestone:** Month 2
- **Owner role:** Regulatory planning lead
- **Dependencies:** E08-F01
- **Acceptance criteria:**
  1. Given the market registry, When requirements are baselined, Then all 12 markets have one versioned fictional requirements checklist.
  2. Given the checklists, When the planning review runs, Then every requirement has an evidence type, owner role, and simulated decision route.
  3. Given the baseline, When content review completes, Then zero real authorities, submission timelines, or regulatory claims appear.

### E01-F02: Simulated submission assembly
- **User story:** As a submission coordinator, I want traceable rehearsal dossiers so that simulated reviews use complete evidence.
- **Quarter:** Q2
- **Milestone:** Month 4
- **Owner role:** Submission coordinator
- **Dependencies:** E01-F01, E08-F02
- **Acceptance criteria:**
  1. Given the baseline, When dossiers are assembled, Then 12 of 12 markets have a uniquely identified simulated submission.
  2. Given each dossier, When completeness checks run, Then every required section contains synthetic evidence or an explicitly justified fictional exclusion.
  3. Given the repository, When traceability is tested, Then every dossier section resolves to a versioned source with zero broken links.

### E01-F03: Simulated authorisation decisions
- **User story:** As a simulated regulatory reviewer, I want explicit market decisions so that submission completion is never mistaken for permission.
- **Quarter:** Q2
- **Milestone:** Month 6
- **Owner role:** Simulated regulatory reviewer
- **Dependencies:** E01-F02, E03-F02, E07-F02
- **Acceptance criteria:**
  1. Given complete dossiers and label records, When simulated reviews conclude, Then all 12 markets have an explicit approved-or-blocked rehearsal decision.
  2. Given an approved decision, When its record is inspected, Then it identifies the market, approved label version, conditions, reviewer role, and review date.
  3. Given a blocked or conditional record, When eligibility is evaluated, Then the market remains ineligible until every blocking condition has documented simulated closure.

### E01-F04: Final-wave authorisation and readiness gate
- **User story:** As a launch governance lead, I want a final cross-functional gate so that M09-M12 activate only with current permissions and readiness.
- **Quarter:** Q4
- **Milestone:** Month 11
- **Owner role:** Launch governance lead
- **Dependencies:** E01-F03, E02-F04, E03-F04, E04-F04, E05-F04, E06-F04, E07-F04, E08-F04, E09-F03
- **Acceptance criteria:**
  1. Given final-wave evidence, When the month-11 gate runs, Then M09-M12 each have current simulated authorisation and 100% passing checks across all nine readiness domains.
  2. Given evidence and prior-wave findings, When final readiness is reviewed, Then all inputs were re-attested within ten rehearsal business days and all findings affecting M09-M12 are closed.
  3. Given any failed check or stale evidence, When the decision is recorded, Then activation is blocked with an owner role and corrective deadline; zero critical blockers are waived.

## E02: Manufacturing and supply

- **First quarter:** Q1

### E02-F01: Synthetic demand and supply assumptions
- **User story:** As a supply planning lead, I want a synthetic demand baseline so that rehearsal capacity matches the staged market scope.
- **Quarter:** Q1
- **Milestone:** Month 2
- **Owner role:** Supply planning lead
- **Dependencies:** E08-F01
- **Acceptance criteria:**
  1. Given the registry, When demand is modelled, Then 12 markets have synthetic monthly quantities through month 12.
  2. Given the wave schedule, When assumptions are reviewed, Then all three waves have capacity and buffer assumptions expressed in synthetic units.
  3. Given demand scenarios, When baseline and 20% uplift cases run, Then every capacity shortfall is quantified and assigned an owner role.

### E02-F02: Manufacturing and supply-control qualification
- **User story:** As a supply quality lead, I want a qualified manufacturing and supply simulation so that allocation cannot bypass capacity, release, or traceability controls.
- **Quarter:** Q2
- **Milestone:** Month 4
- **Owner role:** Supply quality lead
- **Dependencies:** E02-F01, E08-F02
- **Acceptance criteria:**
  1. Given synthetic production schedules and lots, When qualification runs, Then all 12 markets have capacity coverage and documented release, storage-control, and traceability checks.
  2. Given 12 deliberately failed synthetic lots, When release controls run, Then all 12 are blocked from allocation.
  3. Given a mock withdrawal request, When traceability is exercised, Then 100% of affected synthetic units are located within four rehearsal hours.

### E02-F03: First-two-wave inventory readiness
- **User story:** As an inventory coordinator, I want allocated rehearsal stock so that the first two waves have measurable supply coverage.
- **Quarter:** Q2
- **Milestone:** Month 6
- **Owner role:** Inventory coordinator
- **Dependencies:** E02-F02, E03-F02
- **Acceptance criteria:**
  1. Given the demand baseline, When inventory is allocated, Then M01-M08 each have released synthetic stock covering the first two simulated demand months.
  2. Given allocated stock, When packaging and release records are reconciled, Then every record matches its market and approved rehearsal version.
  3. Given demand and route disruptions, When recovery is rehearsed, Then all eight markets retain planned launch coverage or receive an explicit supply blocker.

### E02-F04: Final-wave supply resilience
- **User story:** As a supply resilience lead, I want final-wave stock and recovery evidence so that the last four markets can pass the launch gate.
- **Quarter:** Q4
- **Milestone:** Month 10
- **Owner role:** Supply resilience lead
- **Dependencies:** E02-F03, E03-F03, E08-F04
- **Acceptance criteria:**
  1. Given updated synthetic demand, When final-wave allocation completes, Then M09-M12 each have two simulated demand months of released stock.
  2. Given a 20% uplift and one failed fictional route, When the resilience exercise runs, Then all four markets have a documented executable recovery allocation.
  3. Given inventory evidence, When gate inputs are published, Then all 12 markets have reconciled balances and zero unresolved critical supply discrepancies.

## E03: Packaging and labelling

- **First quarter:** Q2

### E03-F01: Fictional artwork and language matrix
- **User story:** As a packaging lead, I want a market artwork matrix so that packaging variants are defined before simulated approval.
- **Quarter:** Q2
- **Milestone:** Month 4
- **Owner role:** Packaging lead
- **Dependencies:** E01-F01, E08-F02
- **Acceptance criteria:**
  1. Given the regulatory baseline, When the matrix is created, Then all 12 markets map to one controlled artwork variant and fictional language code.
  2. Given each variant, When content checks run, Then every variant displays "SIMULATION ONLY - NOT FOR USE" and a version identifier.
  3. Given the artwork set, When prohibited-content review runs, Then zero real claims, dosing details, or administration instructions appear.

### E03-F02: Controlled label review
- **User story:** As a labelling reviewer, I want approved rehearsal label masters so that submissions and supply use matching content.
- **Quarter:** Q2
- **Milestone:** Month 5
- **Owner role:** Labelling reviewer
- **Dependencies:** E03-F01, E01-F02
- **Acceptance criteria:**
  1. Given artwork and dossier versions, When simulated review completes, Then all 12 markets have an approved-or-blocked label record.
  2. Given an approved label, When traceability is checked, Then its market, dossier reference, version, and two reviewing roles are recorded.
  3. Given superseded artwork, When release is attempted, Then 100% of obsolete versions are rejected.

### E03-F03: First-two-wave packaging verification
- **User story:** As a packaging quality coordinator, I want verified sample packs so that the first two waves cannot use mismatched artwork.
- **Quarter:** Q2
- **Milestone:** Month 6
- **Owner role:** Packaging quality coordinator
- **Dependencies:** E03-F02, E02-F02
- **Acceptance criteria:**
  1. Given approved masters, When sample verification runs, Then M01-M08 each have a passing simulated pack record.
  2. Given eight seeded market-or-version mismatches, When verification runs, Then all eight are detected and blocked.
  3. Given packaging evidence, When gate records are published, Then all eight markets have complete artwork-to-lot traceability and zero unresolved critical defects.

### E03-F04: Final-wave packaging reconciliation
- **User story:** As a packaging operations lead, I want reconciled final-wave variants so that the last wave uses current controlled packaging.
- **Quarter:** Q4
- **Milestone:** Month 10
- **Owner role:** Packaging operations lead
- **Dependencies:** E03-F03, E01-F03, E08-F04
- **Acceptance criteria:**
  1. Given current simulated authorisations, When final-wave packs are checked, Then M09-M12 each match the currently approved label master.
  2. Given a superseded-version test for each final-wave market, When release is attempted, Then all four attempts are blocked.
  3. Given reconciliation results, When sign-off completes, Then all four markets have complete variant records and zero critical packaging defects.

## E04: Medical education

- **First quarter:** Q2

### E04-F01: Non-clinical education scope
- **User story:** As a medical education lead, I want a bounded education plan so that participants understand processes without receiving clinical guidance.
- **Quarter:** Q2
- **Milestone:** Month 4
- **Owner role:** Medical education lead
- **Dependencies:** E01-F01, E07-F01
- **Acceptance criteria:**
  1. Given market and safety requirements, When the curriculum is scoped, Then all 12 markets have role-based learning objectives.
  2. Given the curriculum, When content review runs, Then every module is limited to fictional programme, escalation, and launch-governance processes.
  3. Given draft materials, When prohibited-content checks complete, Then zero clinical instructions, treatment recommendations, or efficacy claims remain.

### E04-F02: First-wave learning readiness
- **User story:** As a learning coordinator, I want assessed first-wave participants so that process owners are ready before the gate.
- **Quarter:** Q2
- **Milestone:** Month 6
- **Owner role:** Learning coordinator
- **Dependencies:** E04-F01, E03-F02, E07-F02
- **Acceptance criteria:**
  1. Given the fictional role roster, When training completes, Then every required M01-M04 role slot has a completion record.
  2. Given completed learning, When assessments run, Then every required role slot scores at least 90% before being marked ready.
  3. Given a synthetic safety enquiry per market, When routing is rehearsed, Then all four reach the approved safety channel without clinical advice.

### E04-F03: Second-wave learning readiness
- **User story:** As a regional education coordinator, I want refreshed second-wave learning so that expansion reflects first-wave findings.
- **Quarter:** Q3
- **Milestone:** Month 8
- **Owner role:** Regional education coordinator
- **Dependencies:** E04-F02, E07-F03, E08-F03
- **Acceptance criteria:**
  1. Given first-wave gate findings, When materials are refreshed, Then every applicable learning action is incorporated or explicitly closed.
  2. Given the M05-M08 roster, When training and assessment complete, Then every required role slot is trained and scores at least 90%.
  3. Given four misrouting scenarios, When routing drills run, Then all four reach the correct fictional process owner within one rehearsal hour.

### E04-F04: Final-wave learning readiness
- **User story:** As an education assurance lead, I want verified final-wave learning so that all remaining role slots are prepared.
- **Quarter:** Q4
- **Milestone:** Month 10
- **Owner role:** Education assurance lead
- **Dependencies:** E04-F03, E08-F04
- **Acceptance criteria:**
  1. Given the M09-M12 roster, When final-wave learning completes, Then every required role slot has a current completion record.
  2. Given the final assessment, When results are evaluated, Then every required role slot scores at least 90%.
  3. Given the curriculum, When content audit runs, Then all four markets use controlled materials with zero prohibited clinical content.

## E05: Market access and pricing

- **First quarter:** Q1

### E05-F01: Fictional access and pricing assumptions
- **User story:** As an access strategy lead, I want transparent fictional assumptions so that affordability work starts from an agreed baseline.
- **Quarter:** Q1
- **Milestone:** Month 2
- **Owner role:** Access strategy lead
- **Dependencies:** E08-F01
- **Acceptance criteria:**
  1. Given the registry, When assumptions are recorded, Then all 12 markets have fictional access pathways and synthetic budget envelopes.
  2. Given pricing scenarios, When units are checked, Then every scenario uses invented simulation credits rather than real currencies or benchmarks.
  3. Given access barriers, When the baseline is reviewed, Then each market has at least one measurable barrier and an accountable owner role.

### E05-F02: Simulated access decision framework
- **User story:** As a pricing governance lead, I want consistent decision rules so that market access is assessed separately from authorisation.
- **Quarter:** Q2
- **Milestone:** Month 5
- **Owner role:** Pricing governance lead
- **Dependencies:** E05-F01, E01-F02, E08-F02
- **Acceptance criteria:**
  1. Given the baseline, When the framework is approved, Then 12 market templates define access eligibility, synthetic pricing, and budget checks.
  2. Given base and 20% uplift scenarios, When affordability is assessed, Then all 12 markets have quantified outcomes against their synthetic envelopes.
  3. Given a failed access condition, When eligibility is calculated, Then the market is blocked regardless of simulated authorisation status.

### E05-F03: First-two-wave access decisions
- **User story:** As an access operations lead, I want documented decisions so that the first two launch gates have explicit access evidence.
- **Quarter:** Q2
- **Milestone:** Month 6
- **Owner role:** Access operations lead
- **Dependencies:** E05-F02
- **Acceptance criteria:**
  1. Given the framework, When reviews complete, Then M01-M08 each have an explicit approved-or-blocked simulated access decision.
  2. Given an approved decision, When evidence is inspected, Then synthetic price, budget coverage, eligibility rules, and reviewing role are recorded.
  3. Given unresolved affordability or pathway conditions, When readiness is evaluated, Then every affected market is marked blocked.

### E05-F04: Final-wave access and budget confirmation
- **User story:** As an access assurance lead, I want final-wave confirmation so that the last four markets have funded fictional pathways.
- **Quarter:** Q4
- **Milestone:** Month 10
- **Owner role:** Access assurance lead
- **Dependencies:** E05-F03, E08-F04
- **Acceptance criteria:**
  1. Given updated assumptions, When final-wave reviews complete, Then M09-M12 each have an explicit access decision and budget record.
  2. Given the 20% uplift scenario, When budget checks run, Then all four markets fit approved synthetic envelopes or remain blocked.
  3. Given all access records, When reconciliation completes, Then 12 of 12 markets have current evidence and zero unexplained pricing-version differences.

## E06: Patient support programme

- **First quarter:** Q2

### E06-F01: Fictional support service design
- **User story:** As a support programme lead, I want a non-clinical support model so that fictional users can navigate access and escalation safely.
- **Quarter:** Q2
- **Milestone:** Month 4
- **Owner role:** Support programme lead
- **Dependencies:** E05-F01, E07-F01, E08-F02
- **Acceptance criteria:**
  1. Given market assumptions, When design completes, Then all 12 markets have access-navigation, enquiry, and escalation routes.
  2. Given support forms, When privacy review runs, Then every form requests synthetic identifiers only and no live personal data.
  3. Given support scripts, When scope review completes, Then zero dosing, administration, diagnosis, or treatment recommendations appear.

### E06-F02: First-wave support rehearsal
- **User story:** As a support operations coordinator, I want tested first-wave support so that fictional enquiries reach the correct service.
- **Quarter:** Q2
- **Milestone:** Month 6
- **Owner role:** Support operations coordinator
- **Dependencies:** E06-F01, E05-F02, E07-F02
- **Acceptance criteria:**
  1. Given M01-M04 routes, When 40 synthetic enquiries are submitted, Then all 40 receive a logged acknowledgement within one rehearsal business day.
  2. Given eight safety-related test enquiries, When routing runs, Then all eight reach the simulated safety queue within one rehearsal hour.
  3. Given one forbidden-read test per market, When permissions are checked, Then all four reads are denied and logged.

### E06-F03: Second-wave support readiness
- **User story:** As a support expansion lead, I want second-wave coverage so that all new fictional users have tested routes.
- **Quarter:** Q3
- **Milestone:** Month 8
- **Owner role:** Support expansion lead
- **Dependencies:** E06-F02, E05-F03, E07-F03, E08-F03
- **Acceptance criteria:**
  1. Given M05-M08 configurations, When 40 synthetic enquiries run, Then every enquiry routes to the correct market and role.
  2. Given two unavailable-channel scenarios per market, When fallback routing activates, Then all eight reach an alternate queue within one rehearsal hour.
  3. Given first-wave gate findings, When readiness is assessed, Then all applicable support actions are closed and zero critical blockers remain.

### E06-F04: Final-wave support readiness
- **User story:** As a support assurance lead, I want verified final-wave support so that all 12 markets have operational rehearsal coverage.
- **Quarter:** Q4
- **Milestone:** Month 10
- **Owner role:** Support assurance lead
- **Dependencies:** E06-F03, E08-F04
- **Acceptance criteria:**
  1. Given M09-M12 configurations, When 40 synthetic enquiries run, Then all 40 are acknowledged within one rehearsal business day.
  2. Given eight synthetic safety enquiries, When escalation is exercised, Then all eight reach the safety queue within one rehearsal hour.
  3. Given the service registry, When final readiness is reviewed, Then all 12 markets have an active primary route, fallback route, and accountable owner role.

## E07: Safety reporting

- **First quarter:** Q1

### E07-F01: Simulated safety governance baseline
- **User story:** As a safety governance lead, I want explicit rehearsal controls so that safety readiness is designed before launch activities.
- **Quarter:** Q1
- **Milestone:** Month 2
- **Owner role:** Safety governance lead
- **Dependencies:** E08-F01
- **Acceptance criteria:**
  1. Given the registry, When governance is defined, Then all 12 markets have a safety owner role, backup role, and escalation route.
  2. Given process definitions, When the baseline is reviewed, Then intake, triage, reconciliation, escalation, and simulated reporting each have an accountable role.
  3. Given timing targets, When documentation is checked, Then every target is labelled internal to the rehearsal and zero real reporting deadlines are asserted.

### E07-F02: Safety intake and reporting configuration
- **User story:** As a safety operations lead, I want controlled simulated intake so that fictional safety records cannot be lost or routed externally.
- **Quarter:** Q2
- **Milestone:** Month 4
- **Owner role:** Safety operations lead
- **Dependencies:** E07-F01, E08-F02
- **Acceptance criteria:**
  1. Given 24 synthetic safety records, When intake runs, Then all 24 receive unique identifiers, market tags, timestamps, and owner roles.
  2. Given external destination tests, When transmission is attempted, Then every attempt is blocked and reporting outputs remain in the simulation environment.
  3. Given one urgent synthetic record per market, When escalation runs, Then all 12 reach the designated safety role within one rehearsal hour.

### E07-F03: First-two-wave safety qualification
- **User story:** As a safety assurance lead, I want qualified workflows so that safety readiness is proven before the first two activations.
- **Quarter:** Q2
- **Milestone:** Month 6
- **Owner role:** Safety assurance lead
- **Dependencies:** E07-F02
- **Acceptance criteria:**
  1. Given ten synthetic cases per market, When end-to-end testing runs for M01-M08, Then all 80 have complete intake-to-simulated-report-to-closure traceability.
  2. Given seeded duplicate and missing-field cases, When validation runs, Then every seeded defect is detected and assigned a documented resolution.
  3. Given support and safety ledgers, When reconciliation completes, Then there are zero unexplained case-count differences and zero critical safety defects.

### E07-F04: Final-wave safety and stop-launch exercise
- **User story:** As a safety readiness lead, I want final-wave qualification and a stop-launch drill so that unsafe rehearsal states cannot proceed.
- **Quarter:** Q4
- **Milestone:** Month 10
- **Owner role:** Safety readiness lead
- **Dependencies:** E07-F03, E06-F03, E08-F04
- **Acceptance criteria:**
  1. Given ten synthetic cases per final-wave market, When qualification runs, Then all 40 complete intake, simulated reporting, and closure with full audit trails.
  2. Given a critical safety-control failure, When the stop-launch drill runs, Then activation is blocked within 15 rehearsal minutes until documented simulated clearance.
  3. Given all safety ledgers, When final reconciliation completes, Then all 12 markets have zero unexplained differences and zero unresolved critical safety defects.

## E08: IT systems and data

- **First quarter:** Q1

### E08-F01: Simulation registry and isolated workspace
- **User story:** As a simulation platform lead, I want an isolated foundation so that every workstream uses consistent fictional identities and boundaries.
- **Quarter:** Q1
- **Milestone:** Month 1
- **Owner role:** Simulation platform lead
- **Dependencies:** None
- **Acceptance criteria:**
  1. Given initial setup, When the registry is created, Then it contains exactly M01-M12, the three launch waves, and role-based ownership fields.
  2. Given the workspace, When boundary tests run, Then all outbound operational integrations are disabled and zero real personal records are present.
  3. Given roadmap identifiers, When the evidence schema is published, Then it supports feature IDs, market IDs, versions, timestamps, owner roles, and dependency references.

### E08-F02: Evidence repository and access controls
- **User story:** As a data governance lead, I want controlled evidence storage so that readiness decisions are traceable and reproducible.
- **Quarter:** Q1
- **Milestone:** Month 3
- **Owner role:** Data governance lead
- **Dependencies:** E08-F01, E01-F01, E02-F01, E05-F01, E07-F01
- **Acceptance criteria:**
  1. Given foundational baselines, When configuration completes, Then all four baseline sets are versioned and linked to originating feature IDs.
  2. Given permitted and forbidden role actions, When 24 access tests run, Then all 24 produce the expected allow-or-deny result with audit records.
  3. Given a backup snapshot, When restoration is rehearsed, Then every baseline record and version history is recovered and matches the snapshot.

### E08-F03: First-wave readiness gate
- **User story:** As a launch readiness analyst, I want an evidence-driven first gate so that activation cannot precede cross-functional readiness.
- **Quarter:** Q3
- **Milestone:** Month 7
- **Owner role:** Launch readiness analyst
- **Dependencies:** E01-F03, E02-F03, E03-F03, E04-F02, E05-F03, E06-F02, E07-F03, E08-F02, E09-F01
- **Acceptance criteria:**
  1. Given M01-M04 evidence, When the month-7 gate runs, Then every market requires passing checks in all nine readiness domains before clearance.
  2. Given gate inputs, When freshness validation runs, Then every input was re-attested within ten rehearsal business days and zero critical blockers remain.
  3. Given nine seeded failures, one per domain, When negative tests run, Then all nine block activation and produce owner-assigned corrective records.

### E08-F04: Second-wave gate and continuing control
- **User story:** As a launch controls lead, I want a second gate and continuing checks so that expansion reflects current evidence and first-wave findings.
- **Quarter:** Q3
- **Milestone:** Month 9
- **Owner role:** Launch controls lead
- **Dependencies:** E08-F03, E04-F03, E06-F03, E09-F02
- **Acceptance criteria:**
  1. Given M05-M08 evidence, When the month-9 gate runs, Then all four pass the same nine domains with evidence re-attested within ten rehearsal business days.
  2. Given first-wave findings and refreshed supply, access, authorisation, packaging, and safety records, When reconciliation runs, Then all applicable actions are closed and zero critical blockers remain.
  3. Given a revoked or expired record, When continuing checks run, Then the affected market loses activation eligibility within 15 rehearsal minutes and the final-gate checklist is updated.

## E09: Communications

- **First quarter:** Q2

### E09-F01: Controlled fictional communications pack
- **User story:** As a communications lead, I want a controlled rehearsal pack so that launch messages remain accurate, bounded, and non-clinical.
- **Quarter:** Q2
- **Milestone:** Month 6
- **Owner role:** Communications lead
- **Dependencies:** E03-F02, E04-F01, E06-F01, E07-F02
- **Acceptance criteria:**
  1. Given approved source materials, When the pack is assembled, Then all 12 markets have a fictional announcement, enquiry route, and escalation statement.
  2. Given the pack, When content review completes, Then every item is marked simulation-only and zero real product, clinical, or regulatory claims appear.
  3. Given distribution settings, When boundary tests run, Then every recipient is an internal fictional role alias and external sending is blocked.

### E09-F02: First-wave simulated activation
- **User story:** As a first-wave launch coordinator, I want gated activation so that M01-M04 launch only after readiness is confirmed.
- **Quarter:** Q3
- **Milestone:** Month 8
- **Owner role:** First-wave launch coordinator
- **Dependencies:** E09-F01, E08-F03
- **Acceptance criteria:**
  1. Given a passing month-7 gate and current activation-time checks, When month-8 activation runs, Then exactly M01-M04 receive simulated launch records.
  2. Given a revoked gate or critical blocker, When activation is attempted, Then the affected market receives no launch record or announcement.
  3. Given activation, When the initial review completes, Then all four markets have delivery receipts, readiness rechecks, and owner-assigned findings within five rehearsal business days.

### E09-F03: Second-wave simulated activation
- **User story:** As a second-wave launch coordinator, I want controlled expansion so that M05-M08 activate only with current gate clearance.
- **Quarter:** Q4
- **Milestone:** Month 10
- **Owner role:** Second-wave launch coordinator
- **Dependencies:** E09-F02, E08-F04
- **Acceptance criteria:**
  1. Given a passing month-9 gate, When month-10 activation runs, Then exactly M05-M08 receive new launch records and the cumulative total is eight markets.
  2. Given activation-time checks, When permissions are revalidated, Then all four markets have current gate clearance, fresh evidence, and zero critical blockers.
  3. Given second-wave results, When review completes within five rehearsal business days, Then all four markets have delivery receipts and all final-wave-relevant findings have owner roles and deadlines.

### E09-F04: Final-wave activation and programme closure
- **User story:** As a programme launch lead, I want final activation and reconciliation so that all 12 fictional markets finish within the planned year.
- **Quarter:** Q4
- **Milestone:** Month 12
- **Owner role:** Programme launch lead
- **Dependencies:** E09-F03, E01-F04
- **Acceptance criteria:**
  1. Given a passing month-11 gate and current activation-time checks, When final activation runs, Then exactly M09-M12 receive new simulated launch records by the end of month 12.
  2. Given the registry, When programme reconciliation runs, Then exactly 12 unique markets are launched with zero duplicate or ungated launch records.
  3. Given closure evidence, When final review completes, Then all 36 features have recorded outcomes and every residual noncritical action has an owner role and deadline.

## Top 5 risks

All likelihood and impact ratings are qualitative planning assumptions, not real-world estimates.

| Rank | Risk | Likelihood / impact | Trigger or indicator | Mitigation and response | Owner role |
|---|---|---|---|---|---|
| 1 | Simulated authorisation or label mismatch blocks activation | Medium / High | Missing decision, open condition, or mismatched label version | Reconcile controlled versions before every gate; block the affected market until simulated clearance | Regulatory planning lead |
| 2 | Safety intake, reporting, or escalation fails | Medium / High | Lost synthetic case, unexplained ledger difference, or missed internal routing target | Repeat qualification and fallback drills; prohibit activation while a critical defect remains | Safety readiness lead |
| 3 | Supply coverage or traceability becomes insufficient | Medium / High | Less than two simulated demand months of launch stock, failed release control, or unreconciled allocation | Reallocate synthetic stock and rehearse alternate routes; block activation without restored coverage | Supply resilience lead |
| 4 | Access assumptions fail under updated demand | Medium / High | Synthetic budget exceeded or access decision blocked, expired, or incomplete | Rework fictional scenarios and obtain a fresh simulated access decision before gate reconsideration | Access assurance lead |
| 5 | Stale evidence, dependency slippage, or boundary failure undermines the 12-month plan | Medium / High | Overdue prerequisite, stale gate evidence, attempted external transmission, or non-synthetic record | Enforce dependency and freshness checks, isolate affected workflows, and replan rather than bypass readiness | Programme launch lead |

## GitHub epic issues

Each issue contains four feature checklist items and the full feature stories, criteria, quarters, owner roles, and dependencies. Its quarter label is the earliest quarter in that epic.

| Epic | First-quarter label | Issue |
|---|---|---|
| E01: Regulatory submission | Q1 | [#1](https://github.com/agentic-dev-labs/meridian-demo/issues/1) |
| E02: Manufacturing and supply | Q1 | [#2](https://github.com/agentic-dev-labs/meridian-demo/issues/2) |
| E03: Packaging and labelling | Q2 | [#3](https://github.com/agentic-dev-labs/meridian-demo/issues/3) |
| E04: Medical education | Q2 | [#4](https://github.com/agentic-dev-labs/meridian-demo/issues/4) |
| E05: Market access and pricing | Q1 | [#5](https://github.com/agentic-dev-labs/meridian-demo/issues/5) |
| E06: Patient support programme | Q2 | [#6](https://github.com/agentic-dev-labs/meridian-demo/issues/6) |
| E07: Safety reporting | Q1 | [#7](https://github.com/agentic-dev-labs/meridian-demo/issues/7) |
| E08: IT systems and data | Q1 | [#8](https://github.com/agentic-dev-labs/meridian-demo/issues/8) |
| E09: Communications | Q2 | [#9](https://github.com/agentic-dev-labs/meridian-demo/issues/9) |
