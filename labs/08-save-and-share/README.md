# Lab 08: Save, Share, and Keep Building

**Objective:** Save your work on GitHub, show one feature you checked, and keep improving it.

**Time-box:** 45 minutes

**Prerequisites:** Your page and checks from Labs 00-02, in the same Codespace.

This lab runs on **Day 1**, right after Lab 02; the lab numbers are just names. At 14:45 everyone
moves to pair sharing. The presenter shows each step, then pauses for your turn.

## Steps

### 1. Let Copilot Write the Message (10 minutes)

1. Save your files. Open **Source Control** and read what actually changed, not only what Chat
   said. You should see only your website files and your note, with no real or private information.
2. Select **+** next to each file you checked.
3. In the message box, select the **sparkle icon**. Copilot reads your changes and writes the
   message for you. Read it and fix anything that is not true. No sparkle? Type a short message yourself.
4. Select **Commit**, then **... > Push**. If a push is rejected or mentions a conflict, ask a
   helper. Never force a push.

### 2. Explore Your Work on GitHub (10 minutes)

GitHub keeps every snapshot you pushed today, like a time machine for your work.

5. Open your repository on GitHub and select **Commits** (next to the clock icon; a narrow window
   shows only the clock). These are the snapshots of your project, newest first. Yours from
   today are at the top: how many did you make?
6. Select one of your own snapshots, for example **Add my first website**. GitHub shows exactly
   what changed: green lines were added, red lines were removed.
7. Go back to your repository, open **site > index.html**, and select **History**. Each entry is
   one version of your page. Find the change you made in Lab 02 by its message.

**Check:** you found your first commit and your page's history on GitHub.

### 3. Take a Challenge (15 minutes)

Pick one level, ask Copilot, and check the result yourself:

| Level      | Challenge                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| **Bronze** | Ask for one idea from the "later ideas" list in your brief.                                                        |
| **Silver** | Make your page phone-friendly: drag the preview narrower, tell Copilot what looks wrong, and check again.          |
| **Gold**   | Give your idea's page a chart or a chat too: `/add-chart lunch-map` or `/add-chat lunch-map`, with your own folder's name. |
| **Bonus**  | Add the feature you did not pick in Lab 02: a chart, a chat, or a picture. Check it against your page. |

Done, and time left? Take the next level. Then save, commit, and push again.

### 4. Show It (10 minutes)

8. Show one feature to a neighbor. Explain what you expected, what you saw, and anything that
   does not work yet. Write your next idea in your brief instead of starting something big.

**Done when:** your work is on GitHub, you found your own history there, your page still works
in the preview, and you can explain one real check. A deployment or saved browser state is not required.

## What you just learned

Pushing keeps your work safe on GitHub, and GitHub remembers every version, so you can always
look back. Publishing, which is optional, puts a page on the internet. Neither one proves the page
works: you check that yourself.

## Optional extras

### Publish Your Page

If your page is ready, you can put it on the internet so others can open it with a link, even
on a phone. This is optional, and you can also do it on Tuesday or Thursday.

1. In Chat, type `/publish-website`. Accept the suggested name or type your own; Copilot writes it
   into `config.json` and tells you your address.
2. Save, commit and push as in step 1. Publishing starts by itself.
3. Wait about three minutes. On GitHub, **Actions > Publish my website** shows progress; when it
   is green, select the link under **Deployments** on your repository page. If nobody has opened
   it for a while, the first visit can take half a minute while it wakes up.
4. Try your main feature on the published page. It starts with the example entries, because your
   preview entries stay in your preview. **Ask** and photo editing work only in the preview.
5. From now on, every push updates your published page by itself.

Published pages stay online until the workshop owner removes them after the workshop.

When you finish for the day, stop your Codespace at [github.com/codespaces](https://github.com/codespaces)
(**...** > **Stop codespace**). Closing the browser tab does not stop it, and stopping it does
not take down a published page.

## Official References

- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): save, share, and review.
- [Source control in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Commit messages with Copilot](https://code.visualstudio.com/docs/editing/copilot-smart-actions): the sparkle icon.
- [Commit history on GitHub](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/viewing-and-comparing-commits/differences-between-commit-views): commits and file history.
- [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart): what runs when you publish.
