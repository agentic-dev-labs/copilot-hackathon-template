# Lab 03: Hand a Task to the Cloud Agent

**Objective:** See Copilot take a task from a GitHub issue, work on it by itself in the cloud,
and return a pull request for a person to review.

**Time-box:** 15 minutes

**Prerequisites:** On Day 3 you only watch. For the optional try on Day 4: your Day 1 website
saved on GitHub, and a helper's confirmation that the cloud agent is switched on for your repository.

This is a **12:15-12:30 demonstration on Day 3**. On **Day 4** you can try it yourself inside
the building time; it adds no extra block. Everything happens on the GitHub website and in your
browser-based Codespace.

| Word         | Plain meaning                                                                         |
| ------------ | ------------------------------------------------------------------------------------- |
| Issue        | A to-do note on GitHub that describes what you want.                                  |
| Cloud agent  | Copilot working by itself in the cloud, on its own copy of your project.              |
| Pull request | Its proposed change. Nothing in your project changes until a person accepts it.       |
| Merge        | Accept the pull request into your project.                                            |

## Watch the Demonstration (Day 3, 15 minutes)

On a practice repository, the presenter shows:

1. An issue asking for one small change, what must stay the same, and how to check it.
2. Assigning the issue to **Copilot**, then its progress log while it works.
3. The pull request: which file changed, and the change explained in plain words.
4. Merging it, bringing the change into the Codespace, and checking it in the preview.

Notice the pattern: you describe the outcome, Copilot does the work in the background, and a
person reviews before anything is accepted. It also follows the rules in your instructions file
from [Lab 06](../06-teach-copilot/README.md).

**Done when:** you have seen an issue become a pull request, and the presenter's own check of
the change before merging.

## Optional Try on Day 4

Ask for a change to your **Day 1 page** while you build your idea in its own folder, so you and
Copilot are not editing the same file at once. If your Day 4 idea is the Day 1 page itself, skip
this try.

1. **Write the issue (09:00-09:15).** On GitHub open your repository, then **Issues > New issue**
   and choose **Website change for Copilot**. Fill in what to change, what must stay the same,
   and how you will check it. For example: "Show today's date under the page title. Change only
   site/index.html. I will check that today's date appears and my entries still work."
2. **Assign it.** In the issue, select **Assignees > Copilot**. If a small window opens, check that
   the branch is the one your work is on (normally `main`; a helper confirms), then confirm. If
   Copilot is not listed, it is not switched on for you: skip this try and tell a helper. Check that
   the issue shows Copilot has started, then go back to building.
3. **Review it (11:45-12:00).** Open **Pull requests** and select Copilot's pull request, then
   **Files changed**. Does it change only what you asked for? If not, leave a comment starting
   with `@copilot` that says exactly what to fix, or close it. Nothing changes until you merge.
4. **Accept it with a helper.** First save, commit, and push your own work in the Codespace. If the
   pull request is still a draft, select **Ready for review**. Then select **Merge pull request**.
   If GitHub asks you to approve workflows, ask the helper first.
5. **Bring it into your Codespace.** In **Source Control** select **... > Pull**. Run
   `/start-website` and check the change yourself.

**Try finished when:** your merged change works in your own preview after you pulled it, and
your entries still work.

## What you just learned

An issue is a clear request, the cloud agent works on it without you watching, and a pull
request lets a person check the result before accepting it. Delegating work does not delegate
the checking.

## When It Does Not Work

| What you see                              | Next action                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------- |
| Copilot is not in the Assignees list      | The feature is not switched on for this repository. Skip the try.             |
| The pull request changed too much         | Comment with `@copilot` asking for the smaller change, or close it unmerged.   |
| Pull reports a conflict                   | Stop and show a helper. Never force a push.                                   |

## Optional extras

1. Ask Chat to write your issue from one sentence, then edit it into your own words.
2. Open the agent's progress log and find one step where it checked its own work.

## Official References

- [About the cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) and [start a task](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task).
- [Review Copilot's output](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output).
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): issues, pull requests, and merging.
- [Topic map (for presenters)](../../docs/REFERENCES.md).
