# Lab 06: Multi-agent assurance review

**Objective:** Partition a vendor review across agents, run independent work in parallel, and merge without conflicts.

**Time-box:** 90 minutes

**Prerequisites:** Completed Labs 01-03 and familiarity with the three agents in `.github/agents`.

## Steps

1. Run the vendor analyst against `src/vendor_assurance/samples/synthetic_soc2_meridian_outreach.md` and save its structured JSON. That sample scores 2 out of 10, so there is plenty for the agents to disagree about.
2. In parallel, assign one agent to validate metadata and another to inspect checklist evidence.
3. Give each agent separate output files; never assign two agents to edit the same file.
4. Compare results and resolve factual disagreement against direct source quotations.
5. Hand the accepted JSON to the report writer.
6. Hand the rendered report to the reviewer and address weak or absent evidence.
7. Run the CLI workflow and tests, then inspect the final report for placeholders.

Partition by separate concerns and file ownership. Small, explicit scopes avoid merge
conflicts and make it clear which agent produced each result.

## What you just learned

Parallel agents help when work is independent; deliberate partitioning, handoffs, and evidence review preserve quality.

**Stretch goal:** Design a fourth agent that checks only output schema without overlapping existing file ownership.
