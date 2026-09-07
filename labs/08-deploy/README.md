# Lab 08: Name it and ship it

**Objective:** Put your name in one file and get your own application running on a public URL.

**Time-box:** 45 minutes, plus optional extras if you finish early

**Prerequisites:** Completed Lab 00, and something of your own in the app from Lab 01.

> This lab runs on **Day 1**, after Lab 02. Lab numbers group topics; they are not the order
> of the week. See [the agenda](../../docs/AGENDA.md).

The facilitator prepares deployment access. You change the app's label and trigger a workflow;
you do not copy credentials into code or need an Azure portal login.

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

3. Commit and push your change, using a pull request if the repository requires it. Merge before deployment.
4. Go to **Actions**, select **Deploy my app**, and choose **Run workflow** on `main`. Leave **connect_dataverse** unchecked for Day 1.
5. The workflow runs tests and lint, then **Read config.json**. If your label is still `Your Name`, it stops there
   with a message telling you to edit the file. That is the guard working, not a failure.
6. The **Build the image** step builds your container remotely. Nothing is built on your laptop.
7. When the run finishes, open the **run summary**. Your URL is printed there.
8. Open it. The page title is your name, and the table lists the synthetic vendor reviews.

**Done when:** the workflow passes, its summary contains your URL, and that URL shows the three
synthetic samples. The health endpoint alone does not prove the page or Dataverse connection works.

## What you just learned

A configuration value drives naming and display filters, not user identity. The workflow uses
preconfigured credentials. Deployment is a deliberate action you trigger, not
something that happens on every push.

## If something goes wrong

| Symptom | Cause | Fix |
|---|---|---|
| Stops on **Read config.json** | Name is still `Your Name`, or it has no letters or digits | Edit `config.json` and push again |
| Deployment rejected on the name | Derived name is invalid | Names are lowercase, letters, digits and hyphens, 32 characters at most. Run `python app/config.py` to see yours |
| The run cannot sign in to Azure | Organization secrets are missing | Tell the facilitator; nothing on your side is wrong |
| Page loads but shows no rows | Not the expected Day 1 result | Confirm the local samples are present and inspect the source label. Dataverse with no matching rows is different from the local-sample path. |

**Stretch goal:** Change something visible in `app/main.py`, push, and run the workflow again.
Watch the same URL update rather than a new app appearing.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Get reviewed.** Open a pull request for your change and request a Copilot code review. Run it
   once at Lite and once at Balanced, and compare what each one caught.
2. **Let it write the summary.** Have Copilot generate the pull request description, then check it
   against your actual diff.
3. **Read the run log (5 min).** Identify the triggering user, commit, image tag, and time. Discuss
   retention requirements before treating it as a long-term record.
4. **Test the guard locally (5 min).** Run `python -m pytest tests/test_app_config.py -q` to see
   placeholder validation tested without changing the shared app or triggering a failed deployment.
