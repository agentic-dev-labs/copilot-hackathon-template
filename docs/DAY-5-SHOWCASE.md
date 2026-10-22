# Day 5: CI/CD with GitHub Actions

Today GitHub checks every pull request for you (**CI**): your tests, and a browser that opens
your pages on a desktop and a phone and keeps screenshots. Then it publishes only what you
approve (**CD**). You break a release on purpose and bring the good one back, and then teams
present their work and hand it over. Same Codespace, same website, everything made up. No
password, key, or Azure sign-in. Since Day 4 every change reaches `main` through a pull request.
Stuck in the terminal? Paste the same sentence into Chat with **Agent** chosen; it does the same job.

**Joining today?** Before the workflow lab at 00:20, your website needs an address and a
protected `main`. If it has no address yet, type `/publish-website` in Chat, then save, commit,
and push. Then create the `Protect main` ruleset as in
[Day 4, section 2, step 1](DAY-4-BUILD.md#2-protect-main-and-version-your-releases). No tests from
Day 3? Your checks say so and stay green.

## Today's Route

Times count from the start of the session.

| Elapsed     | What happens                                                         | You are finished when                                              |
| ----------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 00:00-00:20 | [CI/CD concepts](#1-cicd-in-plain-words)                             | You can point to your pipeline's trigger, permissions, and version. |
| 00:20-00:50 | [Workflow lab: edit a starter YAML file, triggers and permissions](#2-workflow-lab) | Your checks are merged, and your ruleset requires them.            |
| 00:50-01:30 | [CI lab: build and test a pull request, inspect logs, fix failures](#3-ci-lab) | You saw red, read the log and a screenshot, fixed it, and merged on green. |
| 01:30-01:45 | Break                                                                |                                                                    |
| 01:45-02:30 | [CD lab: approve and deploy a build to the training environment](#4-cd-lab) | Your website was published only after you approved it.             |
| 02:30-03:15 | [Recovery lab: smoke-test and redeploy a known-good build](#5-recovery-lab) | The smoke test is green again after your rollback.                 |
| 03:15-03:45 | [Team demos: requirements, review report, and CI/CD evidence](#6-team-demos) | Your table showed its work.                                        |
| 03:45-04:00 | [Handoff: agent profiles, pipeline steps, and release ownership](#7-handoff) | Your HANDOFF.md is merged.                                         |

**Lost?** Find the row the room is on (the presenter names it at the start of every block),
select its link, and start there. Raise your hand: a helper catches you up on what you skipped.

| Word           | Plain meaning                                                                           |
| -------------- | --------------------------------------------------------------------------------------- |
| Workflow       | A YAML file in `.github/workflows/` that tells GitHub what to do and when.              |
| Trigger        | The `on:` part: what starts the workflow, such as a push or a pull request.             |
| Permissions    | What the workflow may do with your repository. Give it only what it needs.              |
| CI             | Continuous integration: every change is built and tested automatically.                |
| UI check       | A browser opens your pages, checks what a person would see, and takes screenshots.      |
| Required check | A check your ruleset insists on: a pull request cannot be merged while it is red.       |
| CD             | Continuous delivery: a checked change is published, here only after a person approves. |
| Smoke test     | A quick check that the published website is alive and shows the right thing.          |
| Rollback       | Going back to the last known-good version. GitHub's **Revert** button does it for you. |

## 1. CI/CD in Plain Words

**00:00-00:20.** Since Day 4, every change reaches `main` through a pull request that you check,
and each merge publishes a numbered version. Open **.github > workflows > publish-website.yml**.
Find `on:` (when it runs: a push to `main` that changes `site/`), `permissions:` (it may only read
your files and prove who it is), and `version:` (your build number). Today you add the missing
half: checks before every merge, and your approval before every release.

## 2. Workflow Lab

**00:20-00:50.**

1. Create a branch named `ci-checks` (select `main` at the bottom left, then **Create new
   branch...**).
2. Ask Copilot CLI (type `copilot` in the terminal): "Copy .github/workflow-starters/check-my-website.yml
   to .github/workflows/check-my-website.yml. Then explain each job and step in one plain
   sentence. Do not change anything else." It has two jobs: **Check the website** runs the build
   check and your Day 3 tests, and **UI check** opens your pages in a browser.
3. Open the new file. Make the two edits its comments ask for, by hand or by asking Copilot:
   - **Trigger:** under `on:`, keep `workflow_dispatch:` and add `pull_request:` and a push to
     `main`, so every change is checked.
   - **Permissions:** these checks only read your files, so change `contents: write` to
     `contents: read`.
4. Commit, select **Publish Branch**, and create a pull request. The pull request runs your new
   checks on itself. When both are green, merge it and delete the branch.
5. **Make the checks required.** On GitHub open **Settings > Rules > Rulesets > Protect main**.
   Tick **Require status checks to pass**, select **Add checks**, and add **Check the website**
   and **UI check**. Select **Save changes**.

**Check:** both checks were green on your pull request, and your ruleset lists them as required.

## 3. CI Lab

**00:50-01:30.**

1. Create a branch named `try-ci`.
2. Break your page on purpose, in a way only a browser notices. Ask Copilot CLI: "Add a banner
   900 pixels wide that says Sale at the very top of my first page, above its header. Change
   nothing else." Commit, select **Publish Branch**, and create a pull request.
3. On the pull request, **Check the website** stays green, but **UI check** turns red, and
   **Merge** is blocked: your ruleset requires it. Select **Details** and read the table at the
   end of the log: it says what is wrong, such as **Wider than a phone screen**.
4. Open the run's summary page (**Summary**, top left). Under **Artifacts**, open
   **home-phone.png**: the banner sticks out of the phone screen. **home-desktop.png** shows the
   desktop, and **all-screenshots** holds every page, idea pages too.
5. Ask Copilot CLI: "Why did the UI check on my pull request fail? Read its log and explain in
   two sentences." Compare its answer with what you read and saw.
6. Fix it on the same branch: "Remove the banner you just added." Commit and push. Both checks
   run again and turn green. Merge the pull request, delete the branch, then switch to `main` in
   the Codespace and **Pull**.

**Check:** you saw red, read the log, looked at a screenshot, fixed it, saw green, and merged.

## 4. CD Lab

**01:45-02:30.** Your website is your **training environment**. Now publishing waits for you.

1. Create a branch named `approval`. Ask Copilot CLI: "Copy
   .github/workflow-starters/publish-website-with-approval.yml over
   .github/workflows/publish-website.yml. Show me what changed." Read the new **Wait for
   approval** job, and see that your `version:` line is still there. Commit, publish the branch,
   create the pull request, and merge it when its checks are green.
2. On GitHub open **Settings > Environments > training** (if it is missing, select **New
   environment** and name it `training`). Tick **Required reviewers**, add yourself, and select
   **Save protection rules**.
3. On a new branch, make one small visible change to your page, then pull request, green checks,
   merge. Open **Actions > Publish my website**: it says **Waiting**. Select **Review
   deployments**, tick **training**, and select **Approve and deploy**.
4. When it is green, open your website's address. Your change is there, with a new version number.

**Check:** nothing was published until you approved it.

## 5. Recovery Lab

**02:30-03:15.**

1. **Smoke-test** your website, using your own address and the sentence under your headline:

   ```bash
   python3 scripts/smoke_test.py https://<name>.thankfulrock-bf005377.eastus.azurecontainerapps.io --expect-text "<the sentence under my headline>"
   ```

   Every line says **PASS**. Write down the **content** and **version** on the first line: the
   content number is the fingerprint of your good version.
2. **Ship a bad build on purpose:** on a new branch, ask Copilot to change the sentence under
   your headline to "Oops, wrong words". Pull request, merge, and approve the release. Your checks
   stay green, because no check knows your words. Run the smoke test again: **FAIL** on your
   sentence. That is why you test the live website after every release.
3. **Roll back:** on GitHub open the pull request you just merged and select **Revert**. GitHub
   opens a new pull request that undoes it. Merge it when its checks are green, then approve the
   release.
4. Run the smoke test again: all **PASS**. The **content** number is the same as in step 1, and
   the **version** is higher: a new build of your known-good page.

**Check:** you saw a failed smoke test, rolled back with **Revert**, and the known-good version is
live again.

## 6. Team Demos

**03:15-03:45.** About three minutes each, by table. Show:

1. Your **requirements**: your board, one ticket with its acceptance criteria, and how you
   checked it.
2. Your **review report**: one finding you confirmed, and one you rejected.
3. Your **CI/CD evidence**: a red then green check with its screenshot, an approval, your version
   number, and a rollback.

An honest "this part does not work yet" is better than a polished claim nobody checked.

## 7. Handoff

**03:45-04:00.** Ask Copilot CLI: "Write HANDOFF.md in plain words: my agent profiles
(user-requirements and code-review: file, job, and how to run them), my user-stories skill, my
board and how a ticket moves from Todo to Done, my review rules, my ruleset (what it requires
before a merge), my pipeline (Check my website with its tests and UI check, and Publish my
website with approval and a version number, and what starts each), how to release and how to
roll back with Revert, who owns releases (me), and open questions for IT. Add a short 'To make
it real' list: which parts are made up or only in my browser today, and the route for each from
the table in docs/DAY-5-SHOWCASE.md." Read it, correct one sentence, then save it the Day 4 way:
a branch, a pull request, and a merge. If you tried an automation, switch it off: on GitHub open
**Agents > Automations**, select it, and choose **Disable**.

Your website is a working prototype with made-up data, kept in one browser. That is the point
of this week: it shows exactly what you need. Making it real is a project with IT, usually:

| Your page needs...                                  | Usual route to ask IT about                 |
| --------------------------------------------------- | ------------------------------------------- |
| Shared data, several people, sign-in, approvals     | Power Apps with Dataverse; a Power Apps code app can keep your page's code |
| Reminders, emails, or Outlook and Teams steps       | Power Automate                              |
| Dashboards on real numbers                          | Power BI, on your team's approved data      |
| Reading PDFs or contracts                           | A document-reading AI service, reviewed by IT |
| An assistant that answers from company information  | Copilot Studio                              |
| To keep building with code, tickets, reviews, and pipelines | A repository in Novo's own GitHub Enterprise, through IT. Rulesets, boards, Actions, and Copilot work the same there; which agents are switched on is Novo's choice |
| To be used in GxP work, such as regulated processes or records | Novo's validation process, with your Quality team, before any real use. This week's website is a prototype, not a validated system |

**Done when:** your ruleset requires your two checks, you fixed a red check from its log and a
screenshot, publishing waits for your approval, you rolled back a bad release with **Revert** and
the smoke test proved it, and your HANDOFF.md is merged. Stop your Codespace at the end: closing
the browser tab does not stop it.

## Optional extras

1. Add a **Smoke test** step to the publishing workflow that runs `scripts/smoke_test.py` after
   each release.
2. Break a test word from Day 3 on a branch and watch **Check the website** turn red too: tests
   and the UI check catch different problems.
3. Ask your Code Review agent to review the pull request from the CI lab.
4. **Agentic Workflows (presenter demo, public preview):** an agent that runs inside GitHub
   Actions, for example when a check fails, and comments what went wrong. It is written in plain
   words like your agents, and the organization pays for it with no personal token.
5. Write a five-line summary of what you built and learned this week for your manager.

## Official References

- [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart) and
  [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
- [Permissions for the GITHUB_TOKEN](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token).
- [Deployment environments and required reviewers](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments).
- [Reverting changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/reverting-a-pull-request)
  and [stopping a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace).
- [Required status checks in rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-status-checks-to-pass-before-merging)
  and [workflow artifacts](https://docs.github.com/en/actions/tutorials/store-and-share-data): where your screenshots are kept.
- [Playwright for Python](https://playwright.dev/python/docs/intro): the browser behind the UI check.
- [Copilot automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations)
  and [GitHub Agentic Workflows](https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows)
  (public preview): agents that start by themselves.
- Routes to make a prototype real, to discuss with IT: [Power Apps](https://learn.microsoft.com/power-apps/)
  with [Dataverse](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro)
  and [code apps](https://learn.microsoft.com/power-apps/developer/code-apps/overview),
  [Power Automate](https://learn.microsoft.com/power-automate/), [Power BI](https://learn.microsoft.com/power-bi/),
  [Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/), and
  [Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/).
- [Topic map (for presenters)](REFERENCES.md).
