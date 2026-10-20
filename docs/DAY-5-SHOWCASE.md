# Day 5: CI/CD with GitHub Actions

Today GitHub checks every change for you (**CI**) and publishes only what you approve (**CD**).
You break a release on purpose and bring the good one back. Then teams show their work and hand
it over. Same Codespace, same website, everything made up. No password, key, or Azure sign-in.

## Today's Route

Times count from the start of the session.

| Elapsed     | What happens                                                         | You are finished when                                              |
| ----------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 00:00-00:20 | [CI/CD concepts](#1-cicd-in-plain-words)                             | You found Monday's publishing workflow and read its trigger.       |
| 00:20-00:50 | [Workflow lab: edit a starter YAML file, triggers and permissions](#2-workflow-lab) | Your check workflow is on GitHub with your two edits.              |
| 00:50-01:30 | [CI lab: build and test a pull request, inspect logs, fix failures](#3-ci-lab) | Your pull request's check went red, then green, and you merged.    |
| 01:30-01:45 | Break                                                                |                                                                    |
| 01:45-02:30 | [CD lab: approve and deploy a build to the training environment](#4-cd-lab) | Your website was published only after you approved it.             |
| 02:30-03:15 | [Recovery lab: smoke-test and redeploy a known-good build](#5-recovery-lab) | The smoke test is green again after your rollback.                 |
| 03:15-03:45 | [Team demos: requirements, review report, and CI/CD evidence](#6-team-demos) | Your table showed its work.                                        |
| 03:45-04:00 | [Handoff: agent profiles, pipeline steps, and release ownership](#7-handoff) | Your HANDOFF.md is on GitHub.                                      |

| Word        | Plain meaning                                                                              |
| ----------- | ------------------------------------------------------------------------------------------ |
| Workflow    | A YAML file in `.github/workflows/` that tells GitHub what to do and when.                 |
| Trigger     | The `on:` part: what starts the workflow, such as a push or a pull request.                |
| Permissions | What the workflow may do with your repository. Give it only what it needs.                 |
| CI          | Continuous integration: every change is built and tested automatically.                   |
| CD          | Continuous delivery: a checked change is published, here only after a person approves.    |
| Smoke test  | A quick check that the published website is alive and shows the right thing.             |
| Rollback    | Going back to the last known-good version.                                                 |

## 1. CI/CD in Plain Words

**00:00-00:20.** Since Monday, every push of `site/` to `main` has published your website by
itself: that is already continuous delivery. Open **.github > workflows > publish-website.yml**.
Find `on:` (when it runs: a push to `main` that changes `site/`) and `permissions:` (it may only
read your files and prove who it is). Today you add the missing half: checks before publishing.

## 2. Workflow Lab

**00:20-00:50.**

1. Ask Copilot CLI (type `copilot` in the terminal): "Copy .github/workflow-starters/check-my-website.yml
   to .github/workflows/check-my-website.yml. Then explain each step in one plain sentence. Do
   not change anything else."
2. Open the new file. Make the two edits its comments ask for, by hand or by asking Copilot:
   - **Trigger:** under `on:`, keep `workflow_dispatch:` and add `pull_request:` and a push to
     `main`, so every change is checked.
   - **Permissions:** this check only reads your files, so change `contents: write` to
     `contents: read`.
3. Save, commit, and push. On GitHub open **Actions > Check my website** and watch it run.

**Check:** the run is green, and its log shows **Run my tests** with your Day 3 tests passing.

## 3. CI Lab

**00:50-01:30.**

1. Create a branch named `try-ci` (select `main` at the bottom left, then **Create new
   branch...**).
2. Break a test on purpose: change one word that a test in `checks/` looks for. Commit, select
   **Publish Branch**, and create a pull request.
3. On the pull request, the check **Check my website** turns red. Select **Details** and find
   the failing step and the line that says what was expected.
4. Ask Copilot CLI: "Why did the check on my pull request fail? Read its log and explain in two
   sentences." Compare its answer with what you read.
5. Fix it on the same branch, commit, and push. The check runs again and turns green. Merge the
   pull request, delete the branch, then switch to `main` in the Codespace and **Pull**.

**Check:** you saw red, read the log, fixed it, saw green, and merged.

## 4. CD Lab

**01:45-02:30.** Your website is your **training environment**. Now publishing waits for you.

1. If your website has no name yet, run `/publish-website` in Chat first and push.
2. Ask Copilot CLI: "Copy .github/workflow-starters/publish-website-with-approval.yml over
   .github/workflows/publish-website.yml. Show me what changed." Read the new **Wait for
   approval** job. Commit and push.
3. On GitHub open **Settings > Environments > training** (if it is missing, select **New
   environment** and name it `training`). Tick **Required reviewers**, add yourself, and select
   **Save protection rules**.
4. Make one small visible change to your page, commit, and push. Open **Actions > Publish my
   website**: it says **Waiting**. Select **Review deployments**, tick **training**, and select
   **Approve and deploy**.
5. When it is green, open your website's address. Your change is there.

**Check:** nothing was published until you approved it.

## 5. Recovery Lab

**02:30-03:15.**

1. **Smoke-test** your website, using your own address and your own headline:

   ```bash
   python3 scripts/smoke_test.py https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io --expect-text "<my headline>"
   ```

   Every line says **PASS**. Write down the **content** number on the first line: it is the
   fingerprint of your good version.
2. **Ship a bad build on purpose:** ask Copilot to change your headline to "Oops, wrong
   headline", then commit, push, and approve it. Run the smoke test again: **FAIL** on your
   headline.
3. **Roll back:** ask Copilot CLI: "Revert my last commit and push it." Approve the deployment.
4. Run the smoke test again: all **PASS**, and the **content** number is the same as in step 1.

**Check:** you saw a failed smoke test, rolled back, and the known-good version is live again.

## 6. Team Demos

**03:15-03:45.** About three minutes each, by table. Show:

1. Your **requirements**: one approved story and how you checked it.
2. Your **review report**: one finding you confirmed, and one you rejected.
3. Your **CI/CD evidence**: a red then green check, an approval, and a rollback.

An honest "this part does not work yet" is better than a polished claim nobody checked.

## 7. Handoff

**03:45-04:00.** Ask Copilot CLI: "Write HANDOFF.md in plain words: my two agents (file, job,
and how to run them), my pipeline (Check my website and Publish my website with approval, and
what starts each), how to release and how to roll back, who owns releases (me), and open
questions for IT." Read it, correct one sentence, then commit and push.

**Done when:** your check workflow runs on every pull request, you fixed a red check, publishing
waits for your approval, you rolled back a bad release and the smoke test proved it, and your
HANDOFF.md is on GitHub. Stop your Codespace at the end: closing the browser tab does not stop it.

## Optional extras

1. Add a **Smoke test** step to the publishing workflow that runs `scripts/smoke_test.py` after
   each release.
2. Ask your Code Review agent to review the pull request from the CI lab.
3. Write a five-line summary of what you built and learned this week for your manager.

## Official References

- [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart) and
  [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
- [Permissions for the GITHUB_TOKEN](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token).
- [Deployment environments and required reviewers](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments).
- [Reverting changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/reverting-a-pull-request)
  and [stopping a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace).
- [Topic map (for presenters)](REFERENCES.md).
