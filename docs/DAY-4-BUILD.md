# Day 4: GitHub Copilot Cloud Agents

Today you hand an approved user story to Copilot's **cloud agent**, write your own **Code
Review agent**, and decide yourself whether Copilot's work is good enough to accept. You use the
same Codespace, your website, and the requirements file from Day 3. Everything stays made up.

## Today's Route

Times count from the start of the session.

| Elapsed     | What happens                                                           | You are finished when                                                 |
| ----------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 00:00-00:20 | [Cloud-agent overview: delegation, safeguards, and human review](#1-how-the-cloud-agent-works) | You can say who may change `main`.                                    |
| 00:20-00:50 | [Practice branches and pull requests with a small change](#2-branches-and-pull-requests) | Your own pull request is merged and pulled.                           |
| 00:50-01:30 | [Assign an approved requirement to Copilot](#3-delegate-an-approved-story) | Copilot is working on your story.                                     |
| 01:30-01:45 | Break                                                                  |                                                                       |
| 01:45-02:30 | [Build a Code Review agent: review rules and report format](#4-build-your-code-review-agent) | Your review agent file exists and Copilot CLI lists it.               |
| 02:30-03:15 | [Run the agent on a diff and verify its findings](#5-review-copilots-pull-request) | Every finding in the report is marked Confirmed or Not a problem.     |
| 03:15-03:45 | [Request fixes with @copilot, retest, and peer-review](#6-ask-for-fixes-and-retest) | Copilot pushed a fix and your checks pass again.                      |
| 03:45-04:00 | [Checkpoint: review the report and decide whether to merge](#7-checkpoint-merge-or-not) | You merged, or closed with a reason, and saved the report.            |

| Word         | Plain meaning                                                                         |
| ------------ | ------------------------------------------------------------------------------------- |
| Branch       | A separate line of work, so `main` stays safe while you try something.                |
| Pull request | A proposed change from a branch. Nothing changes in `main` until a person merges it. |
| Cloud agent  | Copilot working by itself on GitHub, on its own branch, from an issue you write.      |
| Diff         | The list of lines a change adds (green) and removes (red).                            |
| Finding      | One thing a reviewer noticed, with where it is and why it matters.                    |

## 1. How the Cloud Agent Works

**00:00-00:20.** The presenter explains, using a real pull request:

- **Delegation:** you write an issue with one clear outcome and assign it to **Copilot**.
- **Safeguards:** Copilot works on its own `copilot/...` branch. It cannot push to `main`, its
  pull request starts as a draft, and checks on its pull request wait until a person approves.
- **Human review:** you read the change, check it yourself, and only you decide to merge.

## 2. Branches and Pull Requests

**00:20-00:50.** One small change, the safe way.

1. In your Codespace, select the branch name `main` at the bottom left. Choose **Create new
   branch...**, type `my-first-branch`, and press Enter.
2. Make one small change, for example ask Chat: "Change the footer text to say who the page is
   for. Leave the rest alone." Save, then commit in **Source Control**.
3. Select **Publish Branch**. When a message offers **Create Pull Request**, choose it, or open
   your repository on GitHub and select **Compare & pull request**.
4. On GitHub, open the pull request's **Files changed**. Is it only your change? Select
   **Merge pull request**, then **Confirm merge**, then **Delete branch**.
5. Back in the Codespace, select the branch name again, choose `main`, then in **Source
   Control** select **... > Pull**.

**Check:** on GitHub, **Commits** on `main` shows your change.

## 3. Delegate an Approved Story

**00:50-01:30.**

1. On GitHub open **Issues > New issue** and choose **User story for Copilot**.
2. Paste one more **approved** story from your requirements file, with its acceptance criteria.
   Fill in what must stay the same and how you will check it.
3. Select **Assignees > Copilot**. If a small window opens, keep the branch `main` and confirm.
   If Copilot is not listed, tell a helper and follow the presenter's pull request instead.
4. Open the issue again: it shows that Copilot started. Select the session link to watch its
   progress log. It usually takes a few minutes, so go on to the next part.

**Check:** a draft pull request from Copilot appears under **Pull requests**. Step-by-step help
and what to do when something goes wrong: [Lab 03](../labs/03-cloud-agent/README.md).

## 4. Build Your Code Review Agent

**01:45-02:30.** In Copilot CLI (type `copilot` in the terminal), paste this and change the
bracketed part:

> Create a custom agent file at .github/agents/code-review.agent.md with `name: code-review`
> and a one-line description. It is a Code Review agent for my website. When I give it a pull
> request number, it reads that pull request's changes and the user story in its description.
> It checks: every acceptance criterion is met; nothing outside the story changed; typed text
> is shown safely (textContent, never innerHTML); no new internet addresses, packages, keys, or
> real data; the page still works with a keyboard and in a narrow window; [one rule of my own].
> It writes a report to reviews/pr-NUMBER.md as a table with the columns #, Severity (Must fix,
> Should fix, or Nice to have), File and line, What I found, Evidence (the exact line), and
> Suggested fix. Each finding is one or two plain sentences for a beginner. Problems that were
> already there before this pull request go in a separate table called "Already there before",
> so they do not block this change. If it cannot check something itself, it says what I should
> check by hand. It ends with "Verdict: Ready to merge" or "Verdict: Not yet". It never changes
> other files, comments on GitHub, or merges.

Open **.github > agents > code-review.agent.md**, read its rules, and change one into your own
words. Then type `/exit` and `copilot` again, and check that `/agent` lists **code-review**. It is
yours; the workshop's older **reviewer** agent is for a different example, so do not pick that one.

## 5. Review Copilot's Pull Request

**02:30-03:15.**

1. Note the number of Copilot's pull request, for example **#3**. Type `/agent`, choose
   **code-review**, and ask: "Review pull request #3."
2. Open **reviews/pr-3.md**. For every finding, find the line on GitHub under **Files changed**.
   Add a column called **My check** and write **Confirmed** or **Not a problem**, with one reason.
3. Check the change yourself, too: type `/exit` and `copilot` to leave the review agent, then
   ask "Check out pull request #3 so I can try it". In Chat run `/start-website` and try each
   acceptance criterion. Run `pytest checks` in the terminal.

An agent's report can be wrong, just like any other answer. Your checks decide.

## 6. Ask for Fixes and Retest

**03:15-03:45.**

1. On the pull request on GitHub, write a comment that starts with `@copilot` and names one
   confirmed finding: "@copilot Fix finding 1 from my review: [what is wrong]. Change nothing
   else." Copilot starts again and pushes a new commit.
2. When it is done, ask Copilot CLI: "Pull the latest changes of this branch." Check the
   criterion again in the preview, run `pytest checks`, and ask **code-review** to review the
   pull request again.
3. **Peer review:** show your neighbor the pull request and your report. Ask them to check one
   criterion on your screen and say whether they agree.

## 7. Checkpoint: Merge or Not

**03:45-04:00.**

1. Decide. **Merge** if every criterion passes and no **Must fix** is left: select **Ready for
   review**, then **Merge pull request**. If GitHub asks you to approve and run workflows, ask
   a helper first. Otherwise **Close pull request** with a comment saying why.
2. In the Codespace switch to `main` and **Pull**. Save your review agent and report: commit and
   push them.

**Done when:** your own pull request was merged, Copilot built an approved story in a pull
request, your Code Review agent wrote a report whose findings you verified yourself, and you
merged or closed with a reason.

**What you just learned:** branches keep `main` safe, the cloud agent works from a clear issue,
and a review agent helps you look, but a person still checks and decides. Tomorrow you make
GitHub check and publish every change for you: see the [Day 5 guide](DAY-5-SHOWCASE.md).

## Optional extras

1. Hand a second approved story to Copilot, and review it with your agent too.
2. Read Copilot's progress log and find one step where it checked its own work.
3. Ask your review agent to review your own pull request from section 2.

## Official References

- [About the cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
  and [review its output](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output).
- [Branches and pull requests in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview).
- [Custom agents in Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli).
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
- [Topic map (for presenters)](REFERENCES.md).
