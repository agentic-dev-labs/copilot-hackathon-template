# Lab 08: Name it and ship it

**Objective:** Put your name in one file and get your own application running on a public URL.

**Time-box:** 75 minutes

**Prerequisites:** Completed Lab 00, and something of your own in the app from Lab 01.

> This lab runs on **Day 1**, after Lab 02. Lab numbers group topics; they are not the order
> of the week. See [the agenda](../../docs/AGENDA.md).

You never handle a secret and never open the Azure portal. One file decides everything.

## Steps

1. Open `config.json`. It should look like this, with your own name:

   ```json
   {
     "displayName": "Ada Lovelace"
   }
   ```

2. Check what will be derived from it:

   ```shell
   python app/config.py
   ```

   It prints your `displayName` and the `appName` derived from it, for example `ada-lovelace`.
   That derived name becomes your Container App and your public address.

3. Commit and push your change to `main`.
4. Go to the **Actions** tab, select **Deploy my app**, and choose **Run workflow**.
5. Watch the **Read config.json** step first. If your name is still `Your Name`, it stops here
   with a message telling you to edit the file. That is the guard working, not a failure.
6. The **Build the image** step builds your container remotely. Nothing is built on your laptop.
7. When the run finishes, open the **run summary**. Your URL is printed there.
8. Open it. The page title is your name, and the table lists the synthetic vendor reviews.

## What you just learned

A single configuration value can drive naming, deployment, and identity. The pipeline holds the
credentials, so contributors never do. Deployment is a deliberate action you trigger, not
something that happens on every push.

## If something goes wrong

| Symptom | Cause | Fix |
|---|---|---|
| Stops on **Read config.json** | Name is still `Your Name`, or it has no letters or digits | Edit `config.json` and push again |
| Deployment rejected on the name | Derived name is invalid | Names are lowercase, letters, digits and hyphens, 32 characters at most. Run `python app/config.py` to see yours |
| The run cannot sign in to Azure | Organization secrets are missing | Tell the facilitator; nothing on your side is wrong |
| Page loads but shows no rows | Expected on Day 1 | The app reads the local synthetic samples until you connect Dataverse in Lab 05 |

**Stretch goal:** Change something visible in `app/main.py`, push, and run the workflow again.
Watch the same URL update rather than a new app appearing.
