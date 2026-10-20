# Lab 03: Hand an Approved Story to the Cloud Agent

**Objective:** Give Copilot's cloud agent one approved user story in a GitHub issue, follow its
work, and get back a pull request that a person reviews before anything changes.

**Time-box:** 40 minutes

**Prerequisites:** Day 3's requirements file with an approved story, your website saved on
GitHub, and a helper's confirmation that the cloud agent is switched on for your repository.

This is Day 4's **delegation lab**, after you practised branches and pull requests yourself.
Everything happens on the GitHub website and in your browser-based Codespace.

| Word         | Plain meaning                                                                         |
| ------------ | ------------------------------------------------------------------------------------- |
| Issue        | A to-do note on GitHub that describes what you want.                                  |
| Cloud agent  | Copilot working by itself in the cloud, on its own copy of your project.              |
| Pull request | Its proposed change. Nothing in your project changes until a person accepts it.       |
| Merge        | Accept the pull request into your project.                                            |

## 1. Pick the Story (5 minutes)

Open your requirements file from Day 3 and choose one more story marked **Approved**, small enough
to check in a few minutes. If none is approved yet, approve one now: check that you could test
every acceptance criterion by clicking or counting.

## 2. Write the Issue (10 minutes)

1. On GitHub open your repository, then **Issues > New issue** and choose **User story for
   Copilot**.
2. Title it with the story's number and a few words, for example `US-2: show today's date`.
3. Paste the story and its acceptance criteria. Fill in what must stay the same and how you will
   check it. Keep **Only change** as it is (your page, its sample data, and tests) unless your
   story lives in an idea folder; then name that folder instead.

**Check:** someone who has never seen your page could tell when the story is done.

## 3. Assign It to Copilot (5 minutes)

1. In the issue, select **Assignees > Copilot**. If a small window opens, check that the branch is
   `main`, then confirm.
2. The issue shows that Copilot has started. Select the session link to see its progress log.

If Copilot is not listed, it is not switched on for you: tell a helper and follow the presenter's
pull request instead. Never wait idle for it.

## 4. Follow the Work (20 minutes)

Copilot usually needs a few minutes. While it works:

1. Read its progress log. Find one step where it read your files and one where it checked its work.
2. Open **Pull requests**: its pull request starts as a **draft**. Open **Files changed**. Does it
   change only your page, its sample data, and tests? Does every acceptance criterion appear to be covered?
3. Leave it open. On Day 4 you review it next with your own Code Review agent, ask for fixes
   with `@copilot`, and then decide whether to merge. Nothing changes until you merge.

**Done when:** your issue holds an approved story with acceptance criteria, Copilot is assigned
and working, and its draft pull request changes only what the story asked for.

## What you just learned

An issue with a clear story and checkable criteria is a good request. The cloud agent works on
its own branch, and a pull request lets a person check the result before accepting it.
Delegating work does not delegate the checking.

## When It Does Not Work

| What you see                              | Next action                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------- |
| Copilot is not in the Assignees list      | The feature is not switched on for this repository. Tell a helper.             |
| The pull request changed too much         | Comment with `@copilot` asking for the smaller change, or close it unmerged.   |
| GitHub asks you to approve workflows      | Ask a helper first. It is a safeguard: checks on Copilot's work wait for you.  |
| Pull reports a conflict                   | Stop and show a helper. Never force a push.                                   |

## Optional extras

1. Ask Chat to write your issue from one sentence, then edit it into your own words.
2. Use the simpler **Website change for Copilot** template for a small change that is not a story.

## Official References

- [About the cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) and [start a task](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task).
- [Review Copilot's output](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output).
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): issues, pull requests, and merging.
- [Topic map (for presenters)](../../docs/REFERENCES.md).
