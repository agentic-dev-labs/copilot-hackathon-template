# Lab 03: Copilot cloud agent

**Objective:** Assign a focused issue and review the cloud agent's draft pull request.

**Time-box:** 60 minutes

**Prerequisites:** Repository write access, cloud agent enabled by the organization, and completed Lab 02.

## Steps

1. Create an issue using **Copilot agent task**.
2. Set one goal, measurable acceptance criteria, and explicit files in scope.
3. Assign the issue to Copilot and watch the cloud session log.
4. Open the draft pull request and review code, tests, and the agent summary.
5. Leave a precise pull request comment mentioning `@copilot` and requesting one correction.
6. Review the new diff. Check out the agent's PR branch in the Codespace before running its tests; tests on `main` do not validate the PR. Approve pending workflows only after inspecting the changes.
7. Merge only when acceptance criteria are met and facilitator branch rules allow it.

The cloud agent can also research a repository, propose a plan, and iterate on a branch
*before* any pull request exists. Start that from the agents panel on GitHub when you want to
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
2. **Change the dial.** Rerun the same issue with a different model and reasoning level, then compare
   the diffs and what each one cost.
3. **Let Copilot write the issue.** Describe the problem in prose and let it produce the structured
   issue, then judge whether its acceptance criteria are testable.
4. **Start one from somewhere else.** Launch a task from the GitHub CLI, or from your phone, and
   watch it appear in the same session list.
5. **Narrow a bad result.** Take an issue whose first attempt was too broad and tighten it without
   adding scope.
