# Lab 03: Copilot cloud agent

**Objective:** Assign a focused issue and review the cloud agent's draft pull request.

**Time-box:** 60 minutes

**Prerequisites:** Codespaces access, repository write access, cloud agent enabled by the
organization, and the prepared vendor reader using local synthetic samples. No Dataverse access,
retired Lab 05, or travel customizations are required.

The preceding 09:00 block has a [15-minute CLI introduction](../../docs/TOOLS-PRACTICE.md), then
a 15-minute cloud-agent demonstration. Those are separate from this lab's 60 minutes.

Here you run an issue-to-PR workflow and distinguish the issue specification, agent session,
code changes, review, and merge. No Monday feature tour or personal website is a prerequisite.
New technical attendees use the facilitator's prepared synthetic app. Model choice is separate
from choosing the agent or its execution environment. Official procedures are linked below.

Earlier beginner work used interactive Chat. Here a remote development agent changes the business
app in a branch and proposes a PR. Your browser-based Codespace is still where you inspect and
test it. Keep any learner website and optional research unchanged. Follow the presenter's first small
example, then choose your own bounded improvement to the vendor interface.

## Steps

1. Create an issue using **Copilot agent task**.
2. Set one goal, measurable acceptance criteria, and explicit files in scope.
   A suggested task is adding an escaped **Gaps** column to the local synthetic vendor-review
   table. Reuse the evaluator's gaps, do not recompute risk with a model, and add focused tests.
   Keep the optional Dataverse path compatible using mocked tests, without calling a service.
   Scope app changes to `app/` and its existing tests;
   the source reports, evaluator rules, and travel customizations remain unchanged.
3. Assign the issue to Copilot and watch the cloud session log.
4. Open the draft pull request and review code, tests, and the agent summary.
5. Leave a precise pull request comment mentioning `@copilot` and requesting one correction.
6. Review the new diff. Check out the agent's PR branch in the Codespace before running its tests; tests on `main` do not validate the PR. Approve pending workflows only after inspecting the changes.
7. Merge only when acceptance criteria are met and facilitator branch rules allow it.

The cloud agent can also research a repository, propose a plan, and iterate on a branch
_before_ any pull request exists. Start that from the agents panel on GitHub when you want to
agree an approach first, and mention `@copilot` on an existing pull request to request changes.

Keep this exercise to one repository and one small PR. Session limits and supported entrypoints
can change; inspect the current session UI and [cloud-agent documentation](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent).

**Done when:** the PR meets the issue's acceptance criteria, has passing checks, and has received human review. A draft PR by itself is not a mandatory human-approval rule.

## What you just learned

Issues provide durable specifications, draft pull requests expose agent work for review, and comments create an auditable iteration loop.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Plan before any pull request exists.** Start a session from the agents panel and have it
   research and propose an approach on a branch first.
2. **Compare prepared results (5-10 min).** Inspect two results from the same bounded task with
   different models or reasoning settings. Compare evidence, tests, and usage. A new run is optional
   and requires the normal permission and budget checks.
3. **Let Copilot write the issue.** Describe the problem in prose and let it produce the structured
   issue, then judge whether its acceptance criteria are testable.
4. **Inspect another entrypoint (5 min).** Find an existing session through GitHub or the CLI.
   Mobile is an optional presenter tour, not an attendee installation requirement.
5. **Narrow a bad result.** Take an issue whose first attempt was too broad and tighten it without
   adding scope.

## Official References

- [About the cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) and [kick off a task](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task).
- [Research, plan, and iterate](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/research-plan-iterate) and [manage sessions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/manage-and-track-agents).
- [Review Copilot output](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output) and [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
- [Configure the agent environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment): distinct from an attendee's Codespace.
- [Third-party agents](https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents): optional later comparison, with its own support and access requirements.
- [Whole-week coverage and extras](../../docs/REFERENCES.md).
