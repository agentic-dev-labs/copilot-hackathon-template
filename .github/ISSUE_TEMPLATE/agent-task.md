---
name: Copilot agent task
about: Assign a focused implementation task to the Copilot cloud agent
title: "[Agent] "
labels: ["copilot"]
assignees: []
---

## Goal

<!-- State one measurable outcome. -->

## Acceptance criteria

- [ ] [Observable behavior]
- [ ] Tests cover the change.
- [ ] Tests and lint pass on the pull request branch.
- [ ] Synthetic data only; no credentials or private data.
- [ ] Documentation changes retain workshop timings and link the applicable official reference.

## Files in scope

<!-- List files or directories the agent may change. -->

## Agent boundary

Keep this task in one repository and one pull request. Ask before expanding the agreed scope.
For vendor-assurance tasks, use the Python evaluator for calculated findings; do not invent a
different score or source quote. For travel tasks, preserve source labels and unknowns, never
book or submit personal details, and keep generated research under ignored `travel/output/`.
Do not prebuild the learner's solution in the template or copy the managed AttractionsAgent locally.
Do not read or change facilitator preparation notes unless explicitly included in scope.

## Official References

- [Start a cloud-agent task](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task).
- [Review Copilot output](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output).
- Workshop topic map: `docs/REFERENCES.md` in the repository. Product documentation is not evidence from a vendor report.
