# Quick Commands

Short commands and prompts to type or paste during the week. In Chat choose **Agent**; from
Wednesday you can also paste them into Copilot CLI. Read permission requests before allowing
them; actions already allowed for the session may not ask again. Do not approve every tool.
None of these ever force-push or delete your saved history.

## Fetch Updates From the Main Workshop Repository

Your repository is a copy of the main workshop repository (the template,
`agentic-dev-labs/copilot-hackathon-template`), often called **upstream**. When the presenter
says the main repository was updated, paste this to fetch those updates into your own copy:

```text
Fetch the latest updates from the main workshop repository.
```

Copilot runs the workshop's own update script, `scripts/update_from_template.py`, for you; you
never type it, you only select **Allow**. It downloads the main repository's newest version and
copies in only the workshop's own files:
the guides, the ready-made skills, and the helper scripts. Your website, `config.json`, and your
own agents, skills, tests, and workflows stay exactly as they are. Then save, review the files in
**Source Control**, commit with the message `Fetch workshop updates`, and push.

A plain `git pull` from upstream does not work here: your copy started with its own history, so
Git would report conflicts in almost every file. The script is the safe way to do it.

**From Thursday on**, once you protect `main`, it takes changes only through pull requests, so
paste this instead:

```text
On a new branch, fetch the latest workshop updates.
```

Commit, select **Publish Branch**, create the pull request, and merge it on GitHub. Then switch
back to `main` and **Pull**.

## Thursday: Day 4 Prompts

The same prompts as in [the Day 4 guide](DAY-4.md), in the order you use them.

| Where                                                         | Type or paste                                                |
| ------------------------------------------------------------- | ------------------------------------------------------------ |
| Codespace, Chat with **Agent**                                | `Fetch the latest updates from the main workshop repository.` |
| The same Chat, then commit and push                           | `/publish-website`                                           |
| GitHub Copilot app, **Projects > +**, with your ticket number | `Build ticket #1 in the cloud as a pull request.`            |
| GitHub, **Agents > Automations > Create automation**          | `Review this pull request against its ticket. Only comment.` |
| A comment on a pull request that **has conflicts**            | `@copilot Fix the merge conflicts with main.`                |

## Friday: Day 5 Prompts

The same prompts as in [the Day 5 guide](DAY-5.md), all in Chat with **Agent**. You never type a
command: Copilot runs what is needed, and you select **Allow**.

| Lab                         | Type or paste                                                  |
| --------------------------- | -------------------------------------------------------------- |
| Workflow lab                | `Explain my Check my website workflow. Change nothing.`        |
| CI lab: break it on purpose | `Add a Sale banner above my header, min-width 900px.`          |
| CI lab: why is it red?      | `Why did my pull request's UI check fail?`                     |
| CI lab: fix it              | `Remove the banner you just added.`                            |
| CD lab: the two slots       | `Switch on the two Day 5 workflow starters.`                   |
| CD lab: the test copy       | `Smoke-test my feature slot.`                                  |
| CD lab: production          | `Smoke-test my website.`                                       |
| Recovery lab: the good page | `Smoke-test my website. It must show: <your sentence>`         |
| Recovery lab: a bad release | `Change the sentence under my headline to: Oops, wrong words.` |
| Handoff                     | `Write HANDOFF.md as section 7 of docs/DAY-5.md describes.`    |

## Every Day

| I want to...         | Type or paste                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| Build a website      | `/create-website`                                                                                       |
| Open my website      | `/start-website`, or for a second website its folder: `/start-website lunch-map`                        |
| Close my website     | `/stop-website` (your files stay)                                                                       |
| Add a chart          | `/add-chart`, or `/add-chart lunch-map`                                                                 |
| Add a chat           | `/add-chat`, or `/add-chat lunch-map`                                                                   |
| Teach my chat a fact | "Add to my page's knowledge.md: [your fact]." Then ask the chat about it.                               |
| Publish (optional)   | `/publish-website`, then save, commit, and push                                                         |
| Ask for one change   | "Change [this one thing]. Keep everything else the same. Tell me how to check it."                      |
| Report a problem     | "I expected [this]. I saw [that]. Fix only that, and keep everything else unchanged."                   |
| Get ideas            | "Suggest three small ideas for my page."                                                                |
| Understand some code | Select a few lines, then: "Explain the lines I selected in plain English, one short sentence per line." |

## Something Went Wrong

| When                                       | Paste this                                                                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Is my work safe?                           | "Is all my work committed and pushed to GitHub, and which branch am I on? Answer in plain words and change nothing."                                                                                         |
| I want to see what I changed               | "List the files I changed since my last commit, with one plain sentence for each. Change nothing."                                                                                                           |
| I made a mess and want my last commit back | "Undo every change since my last commit. First list each file that would change, including new files that would be deleted, and wait for my yes."                                                            |
| One file is broken                         | "Put site/index.html back the way it was in my last commit. Change no other file." Use your own file's name.                                                                                                 |
| It worked yesterday                        | "Show my last 5 commits in plain words. After I pick one, put site/index.html back the way it was in that commit, as a new change I can review. Never rewrite my history."                                   |
| My push was refused                        | "My push was refused. Explain why in one sentence, then fix it safely: pull first, and never force-push. If main takes only pull requests, move my commits to a new branch and help me open a pull request." |
| I am on the wrong branch                   | "Take me back to main with the newest version from GitHub. Keep any unfinished work safe first, and tell me where it is."                                                                                    |
| Git says there is a conflict               | "There is a merge conflict. For each file, show me both versions in plain words and ask me which to keep, one file at a time."                                                                               |

## Copilot in the Terminal (Wednesday only)

From Thursday everything happens in Chat; you do not need the terminal.

| Type            | What it does                                                          |
| --------------- | --------------------------------------------------------------------- |
| `copilot`       | Starts Copilot CLI in the terminal.                                   |
| `/login`        | Signs in, if the bottom line shows no model name.                     |
| `/agent`        | Picks one of your own agents.                                         |
| `/exit`         | Leaves Copilot CLI. Type `copilot` again to see a new agent or skill. |
| `pytest checks` | Runs your tests (type it in the terminal, outside Copilot CLI).       |

## One Good Request

"Change **this one thing** for **this audience**. Keep **these things** unchanged. Explain the
small plan first. I will check it by **this action and expected result**."

Back to the [Quick Reference](QUICK-REFERENCE.md) or [your week](../README.md#your-week).
