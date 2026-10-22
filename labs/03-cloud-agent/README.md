# Lab 03: Hand an Approved Ticket to the Cloud Agent

**Objective:** Give Copilot's cloud agent one approved ticket from your board, follow its work
online, and get back a pull request that is reviewed before anything changes.

**Time-box:** 40 minutes

**Prerequisites:** Day 3's board with an approved ticket in **Todo**, its user story and
acceptance criteria filled in; your `Protect main` ruleset from
[Day 4, section 2](../../docs/DAY-4-BUILD.md#2-protect-main-and-version-your-releases), so every
change reaches `main` through a pull request; and a helper's confirmation that the cloud agent is
switched on for your repository. Joining today without a board? Write one ticket as the
[Day 4 guide](../../docs/DAY-4-BUILD.md) shows at the top.

This is Day 4's **delegation lab**, after you practiced branches and pull requests yourself.
The presenter delegates a demo ticket first; then you delegate yours. Everything happens on the
GitHub website and in your browser-based Codespace.

| Word           | Plain meaning                                                                       |
| -------------- | ----------------------------------------------------------------------------------- |
| Ticket (issue) | One thing you want, with its user story and acceptance criteria, under **Issues**. |
| Board          | Your project's cards: Todo (approved), In Progress, and Done.                       |
| Cloud agent    | Copilot working by itself in the cloud, on its own copy of your project.            |
| Pull request   | Its proposed change. Nothing in your project changes until a person accepts it.     |
| Merge          | Accept the pull request into your project.                                          |

## 1. Pick the Ticket (5 minutes)

Open your board from your repository's **Projects** tab and choose one ticket in **Todo**, small
enough to check in a few minutes. None there yet? Run your User Requirements agent on a ticket, as
on Day 3, check that you could test every acceptance criterion by clicking or counting, and drag it
into **Todo**.

## 2. Check the Ticket (10 minutes)

1. Open the ticket. Read its **User story** and **Acceptance criteria** once more: could someone
   who has never seen your page tell when it is done?
2. **Which page** must name the right page: `site/index.html`, or your idea's folder, such as
   `site/ideas/team-lunch/`. Keep **Only change** as it is.
3. To change anything, select **...** and **Edit** on the ticket, then save.

**Check:** the ticket says what you want, where, and how you will know it is done.

## 3. Assign It to Copilot (5 minutes)

1. In the ticket, select **Assignees > Copilot**. If a small window opens, check that the branch
   is `main`, then confirm.
2. On your board, drag the ticket into **In Progress**.
3. The ticket shows that Copilot has started. Select the session link to see its progress log.

If Copilot is not listed, it is not switched on for you: tell a helper and follow the presenter's
pull request instead. Never wait idle for it.

## 4. Follow the Work (20 minutes)

Copilot usually needs a few minutes. While it works:

1. Read its progress log. Find one step where it read your files and one where it checked its work.
2. Open **Pull requests**: its pull request starts as a **draft** and is linked to your ticket.
3. Open **Files changed**. Does it change only your page, its sample data, and tests? Does every
   acceptance criterion appear to be covered?
4. Leave it open. Next you review it with your own Code Review agent, ask for fixes with
   `@copilot`, and then decide whether to merge. Nothing changes until you merge, and your
   pipeline deploys it only after that. The merge also closes the ticket, and your board moves
   it to **Done**.

**Done when:** your approved ticket is assigned to Copilot and **In Progress** on your board, and
Copilot's draft pull request changes only what the ticket asked for.

## What you just learned

A ticket with a clear story and checkable criteria is a good request. The cloud agent works on
its own branch, and a pull request lets a person, with their own review agent, check the result
before accepting it. Delegating work does not delegate the checking.

## When It Does Not Work

| What you see                              | Next action                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------- |
| Copilot is not in the Assignees list      | The feature is not switched on for this repository. Tell a helper.             |
| The pull request changed too much         | Comment with `@copilot` asking for the smaller change, or close it unmerged.   |
| GitHub asks you to approve workflows      | Ask a helper first. It is a safeguard: checks on Copilot's work wait for you.  |
| Pull reports a conflict                   | Stop and show a helper. Never force a push.                                   |

## Optional extras

1. Ask Chat to write a new ticket from one sentence, then edit it into your own words before you
   create it with the **Requirement** template.
2. Use the simpler **Website change for Copilot** template for a small change that is not a
   ticket from your board.
3. **An agent that starts by itself.** On GitHub open **Agents > Automations > Create new**. Name
   it `Criteria for new tickets`, choose the trigger **When an issue is created** with the filter
   `label:enhancement`, and use this prompt: "Read this new ticket. Use the user-stories skill to
   write its user story and acceptance criteria into the ticket's User story and Acceptance
   criteria sections, keeping the author's own words. Change nothing else." Select **Suggest
   tools** and keep only reading the ticket and updating it. Then open **Issues > New issue >
   Requirement**: nobody assigns it, yet a session starts, and the criteria arrive on the ticket
   or as a suggested change for you to approve. Turn the automation off afterwards under
   **Agents > Automations**, because each run uses your Copilot allowance.

## Official References

- [About the cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) and [start a task](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task).
- [Review Copilot's output](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output).
- [About projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) and [their built-in automations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations).
- [Copilot automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations) and [creating them](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations), for the optional extra.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): issues, pull requests, and merging.
- [Topic map (for presenters)](../../docs/REFERENCES.md).
