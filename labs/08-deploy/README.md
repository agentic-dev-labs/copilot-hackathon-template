# Lab 08: Discover reusable skills and ship the starter

**Objective:** Inspect an Awesome Copilot example after completing the trip, then deploy the
provided training application through GitHub Actions without attendee Azure sign-in.

**Time-box:** 45 minutes

**Prerequisites:** Completed Labs 00-02, your reviewed travel plan, and the facilitator's
prepared Actions deployment access. The provided vendor-review app already runs; Lab 01
does not need to have modified it.

> This lab runs on **Day 1**, after Lab 02. Lab numbers group topics; they are not the order
> of the week. See [the agenda](../../docs/AGENDA.md).

The facilitator prepares deployment access. You change the app's label and trigger a workflow;
you do not copy credentials into code or need an Azure portal login.

## Presenter Demonstration (10 minutes within this lab)

Only after the trip is finalized, open [Awesome Copilot](https://github.com/github/awesome-copilot/).
Show the agents, instructions, skills, plugins, and Learning Hub. These are community-contributed
examples to inspect, adapt, and test, not automatically approved enterprise capabilities.

Use a prepared adaptation of [web-design-reviewer](https://github.com/github/awesome-copilot/tree/main/skills/web-design-reviewer)
on the provided training app. Inspect its skill file/references, then demonstrate one visual
check, a small source fix, and verification using **built-in browser tools only**. Do not copy
the upstream example's browser-server setup. A prepared result is labelled as such, not claimed
as a live run by every attendee. Installation is presenter prework, not an extra dependency.

Explain the three repositories: this workshop supplies exercises/tests/deployment; your
enterprise source distributes curated specialists; Awesome Copilot supplies examples to evaluate.
The remaining 35 minutes cover the deployment steps below, including handover and review.

The endpoint you publish is the **provided vendor-review training app**, used for Day 2's
Dataverse exercise. It does not host TravelPlannerAgent, perform bookings, or embed Copilot SDK.
The travel plan remains the completed customization exercise. Do not upload real research
results just to make a travel page. Building such a page is optional follow-up, not a hidden prerequisite.

## Steps

1. Open `config.json`. Use your assigned, unique workshop label, for example:

   ```json
   {
     "displayName": "Synthetic Team Seven"
   }
   ```

2. Check what will be derived from it:

   ```shell
   python app/config.py
   ```

   It prints your `displayName` and the `appName` derived from it, for example `synthetic-team-seven`.
   That name becomes your Container App. Two repositories with the same derived name would update
   the same app; the facilitator assigns unique labels. A shared team repo produces one shared app.

3. Review your configuration/customization diff and commit/push it, using a PR if required.
   An AI-generated summary is a draft to check against the diff. Merge before deployment.
4. Go to **Actions**, select **Deploy my app**, and choose **Run workflow** on `main`. Leave **connect_dataverse** unchecked for Day 1.
5. The workflow runs tests and lint, then **Read config.json**. If your label is still `Your Name`, it stops there
   with a message telling you to edit the file. That is the guard working, not a failure.
6. The **Build the image** step builds your container remotely. Nothing is built on your laptop.
7. When the run finishes, open the **run summary**. Your URL is printed there.
8. Open it. The page title is your name, and the table lists the synthetic vendor reviews.
9. Open `/healthz` at the same app origin. Confirm `status` is `ok` and `commit` matches
   the workflow's tested commit. A healthy response from an older revision is not this deployment.

**Done when:** you can explain the community-example versus managed-plugin distinction, the
workflow passes for your intended commit, and its summary/artifact URL shows your label and the
three synthetic samples. The health response must identify that commit. This deployment is
separate from executing the travel agent, and Dataverse is intentionally not connected yet.

## What you just learned

A configuration value drives naming and display filters, not user identity. The workflow uses
preconfigured credentials. Deployment is a deliberate action you trigger, not
something that happens on every push.

## If something goes wrong

| Symptom                               | Cause                                                     | Fix                                                                                                                                          |
| ------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Stops on **Read config.json**         | Name is still `Your Name`, or it has no letters or digits | Edit `config.json` and push again                                                                                                            |
| Deployment rejected on the name       | Derived name is invalid                                   | Names are lowercase, letters, digits and hyphens, 32 characters at most. Run `python app/config.py` to see yours                             |
| The run cannot sign in to Azure       | Organization secrets are missing                          | Tell the facilitator; nothing on your side is wrong                                                                                          |
| Stops on prepared access/commit check | Missing Actions configuration or the branch moved         | Ask the owner to check the named settings; retest the exact branch. Do not sign into Azure as a workaround.                                  |
| Page loads but shows no rows          | Not the expected Day 1 result                             | Confirm the local samples are present and inspect the source label. Dataverse with no matching rows is different from the local-sample path. |

**Stretch goal:** Change something visible in `app/main.py`, push, and run the workflow again.
Watch the same URL update rather than a new app appearing.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Get reviewed (5-10 min).** Open a PR for a small change and request Copilot code review if
   enabled. Inspect one finding against code and tests. If effort levels are offered, identify
   their purpose; a second review is optional and consumes additional usage.
2. **Let it write the summary.** Have Copilot generate the pull request description, then check it
   against your actual diff.
3. **Read the run log (5 min).** Identify the triggering user, commit, image tag, and time. Discuss
   retention requirements before treating it as a long-term record.
4. **Test the guard locally (5 min).** Run `python -m pytest tests/test_app_config.py -q` to see
   placeholder validation tested without changing the shared app or triggering a failed deployment.

## Official References

- [Awesome Copilot](https://github.com/github/awesome-copilot/) and [web-design-reviewer](https://github.com/github/awesome-copilot/tree/main/skills/web-design-reviewer): inspect provenance, dependencies, and source before reuse.
- [Built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools): the workshop's browser path, with no additional server installation.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): branch, commit, PR, review, and merge.
- [Commit and PR smart actions](https://code.visualstudio.com/docs/editing/copilot-smart-actions) and [PR summaries](https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/create-a-pr-summary).
- [GitHub Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) and [using Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
- [Container Apps with GitHub Actions](https://learn.microsoft.com/azure/container-apps/github-actions): deployment and registry authentication. The workshop uses its checked-in workflow, not every option in the guide.
- [Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) and [whole-week coverage](../../docs/REFERENCES.md).
