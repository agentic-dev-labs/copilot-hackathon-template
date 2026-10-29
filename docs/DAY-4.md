# Day 4: GitHub Copilot Cloud Agents, Projects, and Automations

Today Copilot works for you in the cloud, the new way GitHub announced this week. First you save
your website on GitHub and publish it with a **version number**. Then you write one ticket, and a
**Copilot project** builds it for you as a **pull request**. GitHub checks every pull request by
itself and shows you the page on a desktop and a phone, right in the pull request. An
**automation** reviews it when you mark it ready, and only you decide to merge. After the merge
your live website shows where it runs and which version it is. Everything stays made up.

**Follow this guide in the workshop template on GitHub:** open
`github.com/agentic-dev-labs/copilot-hackathon-template`, then **docs > DAY-4.md**. Your own copy
receives it in section 1.

**Joining today, or no website yet?** A helper sits with you during section 1: on the workshop
template select **Use this template > Create a new repository**, owner **agentic-dev-labs**, a
name such as `<your username>-planner`, **Private**, then **Code > Codespaces > Create codespace
on main**. In Chat choose **Agent**, run `/create-website`, and pick the **Project Planner**. Then
continue with section 1, step 2.

## What You Saw on the Slides

Every part of today's lab puts one idea from the presentation into practice. Each section starts
with the **Slide** it belongs to.

| On the slides                                                                         | In your lab                                                                                   |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Evolving for the Agentic Era:** any event can trigger work                          | Your push publishes your website and starts its checks (section 1).                           |
| **The stages stay. The jobs change.** Plan becomes goals and acceptance criteria      | Your **Show my version** ticket says what done means (section 2).                             |
| **GitHub Copilot app** and **Copilot Projects:** mission control, one inbox for review | A Copilot project builds your ticket in the cloud; you follow it in **Overview** (section 2). |
| Build: "a pull request, with context". Verify: "auditable evidence"                    | Copilot's pull request, with checks and desktop and phone screenshots (section 2).            |
| **Copilot Automations:** work that starts by itself, with triggers, tools, and limits | Your **Reviewer**, started by your click on **Ready for review** (section 3).                 |
| **You decide · Agents do**                                                            | Only your merge releases the next version (section 4).                                        |

## Today's Route

Times count from the start of the session.

| Elapsed     | What happens                                                                                 | You use                         | You are finished when                                                          |
| ----------- | -------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------ |
| 00:00-00:15 | What's new: the GitHub Universe announcements                                                | The presenter's slides          | You can say what a Copilot project and an automation do.                       |
| 00:15-00:50 | [Save and publish your website, with checks and a version](#1-save-and-publish-your-website) | Your Codespace, then GitHub     | Your website is live, and its `version.json` shows version 1.0.0 and a build.  |
| 00:50-01:30 | [A Copilot project builds your ticket](#2-a-copilot-project-builds-your-ticket)              | GitHub and the Copilot app      | The pull request for your ticket shows its checks and your page's screenshots. |
| 01:30-01:45 | Break                                                                                        |                                 |                                                                                |
| 01:45-02:15 | [An automation reviews your pull request](#3-an-automation-reviews-your-pull-request)        | GitHub                          | Your Reviewer commented on your pull request by itself.                        |
| 02:15-02:45 | [Merge, release, and checkpoint](#4-merge-release-and-checkpoint)                            | GitHub, then your Codespace     | Your live website says **Production** and its version, and the ticket closed.  |

**Lost?** Find the row the room is on (the presenter names it at the start of every block),
select its link, and start there. Raise your hand: a helper catches you up on what you skipped.

## New Words for Today

| Word            | Plain meaning                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| Commit and push | Save a snapshot of your files, then send it to GitHub. Until you push, only your Codespace has it.     |
| Publish         | Put your website on the internet. From today every push to `main` does it by itself.                   |
| Version number  | The label of a release: 1.0.0 plus the build number, which goes up by one with every publish.          |
| Environment     | Where a copy of your website runs. Your website's own address is **Production**.                       |
| Ticket (issue)  | One thing you want, written on GitHub under **Issues**, with a number such as #1.                      |
| Copilot project | Copilot as a team lead for one goal: it starts work sessions, runs them, and keeps track of them.      |
| Session         | One piece of work Copilot does, here in the cloud, on its own branch.                                  |
| Pull request    | A proposed change. Nothing changes in `main` until you merge it. A **draft** is still being worked on. |
| Check           | A job GitHub runs by itself on every change: your tests, and a browser that takes screenshots.         |
| Automation      | Copilot starting by itself when something happens, such as a pull request marked ready for review.     |
| Trigger         | The event that starts an automation or a check.                                                        |
| Ruleset         | Rules GitHub applies to a branch, such as "changes arrive only through a pull request".                |

## 1. Save and Publish Your Website

**00:15-00:50.** **Slide: Evolving for the Agentic Era.** Your website from Monday and Tuesday is
probably still only in your Codespace: it reaches GitHub only when you push. Today one push saves
it, switches on GitHub's checks and your version number, and publishes your website: your push is
the event that starts the work. The presenter does each step on screen first, and you do it right
after.

1. **Open your Codespace.** Go to [github.com/codespaces](https://github.com/codespaces) and select
   the codespace of your workshop repository. It wakes up in about a minute, with all your
   files. Never create a second one: a new codespace does not have your unsaved work. Two listed?
   Open the one you used last, and ask a helper if you are not sure. Open Chat and choose
   **Agent**.
2. **Bring in today's updates.** Send this in Chat, then **Allow** the command:

   ```text
   Run python3 scripts/update_from_template.py
   ```

   It brings this guide into your copy, today's ticket template, the starter for your checks, and
   a newer `/publish-website`.

3. **Publish, with checks and a version.** Type `/publish-website` in Chat and answer its one
   question: keep its suggested name or type your own, such as `ali-planner`. It writes the name
   into `config.json`, shows your address, and switches on two things for GitHub: **checks** that
   test every change, and a **version number** for every release. **Check:** open **.github >
   workflows > publish-website.yml**. Its last line says `version: 1.0.0.${{ github.run_number }}`,
   lined up with `website-name:` above it.
4. **One push for everything.** Choose **File > Save All**. Open **Source Control**: it lists your
   website plus today's updates. Hover over **Changes** and select its **+** to include them all,
   type `Day 4: my website, checks and version`, select **Commit**, then **... > Push**.
5. **Watch GitHub work.** On your repository's page open **Actions**. Two runs start by
   themselves: **Publish my website** puts your website on the internet, and **Check my
   website** opens your pages in a browser on a desktop and a phone. Each takes about three
   minutes.
6. **Open your website.** Open the **Publish my website** run. Its summary says **Your website is
   live**, with your address and **Version 1.0.0.** plus the build number. Open the address. Then
   add `/version.json` to the end of the address: your website knows its version and its
   environment, **Production**. The page itself does not show them yet: that is your ticket.
7. **Look at your first check.** Open the **Check my website** run. Green or red, both are fine
   today: the **UI check** table says what to look at, and under **Artifacts** you find
   **home-desktop.png** and **home-phone.png**, your page as GitHub's browser saw it.

**Check:** your website opens at its own address, and its `version.json` shows a version that
starts with 1.0.0 and the environment Production.

| What you see                                           | Next action                                                                                                     |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **Source Control** lists only today's updates          | Your website is already on GitHub, or this is a new codespace. Check that **site > index.html** is on GitHub.   |
| No `site/index.html` anywhere                          | Build your website first with `/create-website` and a helper, as in **Joining today**, then continue at step 2. |
| The update stops: workshop files are not committed     | Show a helper. Usually you undo that one file in **Source Control**, then paste the prompt again.               |
| No `scripts/update_from_template.py`                   | Your repository is not a copy of the workshop template. A helper starts you with **Joining today**.             |
| The push is refused because it changes a workflow file | Show a helper: they make the two workflow changes on GitHub with the pencil icon, then you push again.          |
| The publish run says **That name is taken**            | Run `/publish-website` again with another name, then commit and push.                                           |
| The publish run is red for another reason              | Show its message to a helper. Never change the workflow to make it pass.                                        |
| The **UI check** is red                                | Fine today. Read its table: it says what to look at. On Friday you learn to fix and require these checks.       |

## 2. A Copilot Project Builds Your Ticket

**00:50-01:30.** **Slide: Copilot Projects.** You write one ticket. A Copilot project builds it in
the cloud while you watch, and GitHub checks the result. **From here you lead:** follow the steps
on your own; the presenter and helpers walk the room, so raise your hand when you are stuck.

1. **Write the ticket.** On GitHub open **Issues > New issue** and choose **Show my version**. Its
   user story and three acceptance criteria are already written, and they fit any website: read
   them, then select **Create**. Note its number, such as **#1**.
2. **Protect main.** From now on every change arrives through a pull request. Open **Settings >
   Rules > Rulesets**, then **New ruleset > New branch ruleset**. Name it `Protect main`, set
   **Enforcement status** to **Active**, and under **Target branches** select **Add target >
   Include default branch**. Under **Branch rules** keep **Restrict deletions** and **Block force
   pushes**, then tick **Require a pull request before merging**, with required approvals left
   at **0**: you are the only person in your repository, so you check each change yourself
   before you merge it.

   Leave the bypass list empty, so the rules apply to you too, and select **Create**. GitHub may
   ask you to **Confirm access** with GitHub Mobile or a code: keep your phone at hand, and never
   share that code.

3. **Start a Copilot project.** Open the **GitHub Copilot app** on your laptop, signed in with your
   workshop account as on Wednesday. In the sidebar, next to **Projects**, select **+**. Under
   **Which repositories should this Project use?**, search for your repository, select it, and
   select **Add repositories**.
4. **Give it the goal.** Send this in the prompt box, with your own ticket's number:

   ```text
   Build ticket #1 in the cloud as a pull request.
   ```

   Ten words are enough: your ticket already says what to change, which test to add, and that the
   pull request closes it. Copilot never merges; that decision stays yours.

5. **Follow it.** Select **Overview** at the top of the right-hand panel: your ticket's session is
   under **Working**. If something appears under **Needs input**, read it and answer: Copilot asks
   when it needs a decision or your permission. Select the session to see its plan and its
   changes; **Steer this session** sends it a message while it works. It usually takes 5 to 15
   minutes.
6. **Open the pull request.** When the session moves to **Open**, open **Pull requests** on GitHub
   and select it. It is a **draft**, linked to your ticket. Select **Files changed**: it should
   change only `site/index.html` and add a test in `checks/`.
7. **Let the checks run.** GitHub runs nothing on Copilot's code until a person allows it. If you
   see **Approve workflows to run** at the bottom of **Conversation**, select it. Wait until
   Copilot has finished first (the title no longer starts with **[WIP]**): each new commit asks
   again.
8. **See your page in the pull request.** About three minutes later the checks are done, and a
   comment from **github-actions** appears at the bottom of **Conversation**: **UI check**, with
   your first page on a desktop and on a phone. The new footer says **Preview**: checks run before
   any release, so there is no version yet. **Do not merge yet.**

**Check:** a draft pull request for your ticket is open, its checks are done, and a comment shows
your page on a desktop and a phone.

| What you see                                                     | Next action                                                                                                                  |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| No **Projects** in the app, or nothing starts after five minutes | On GitHub open your ticket and select **Assignees > Assign to Agent**, keep **main** and **Copilot**, and select **Assign**. |
| Under **Needs input** Copilot asks to run a command              | Read it. Allow what reads or edits your repository's files, runs its tests, or opens the pull request.                       |
| The session finished, but there is no pull request               | Open the session and select **Create PR**, or ask it: "Open the draft pull request now."                                     |
| No **Approve workflows to run** button                           | Copilot is still working, or your checks already run: look at the checks list in the merge box.                              |
| Checks done, but no comment with pictures                        | Open **Actions > Check my website**: its **Screenshots** job says why. Your pictures are also under **Artifacts**.           |
| The pictures in the comment do not load                          | They show only to people signed in who can open your repository. Reload the page.                                            |

## 3. An Automation Reviews Your Pull Request

**01:45-02:15.** **Slide: Copilot Automations.** Now you build an automation of your own. It
starts by itself whenever you mark a pull request **ready for review**, one of the new triggers:
no meeting and no reminder, just an event.

1. On GitHub, on your repository's page, select **Agents**, then **Automations** in the sidebar,
   then **Create automation** and **Create manually**.
2. **Name** it `Reviewer`. Under **Type** choose **Personal**: only you see it, and it acts as you.
3. Under **Triggers**, choose the pull request trigger **Ready for review**. Keep the other
   settings, except **Configured tools can change**: choose **Only this issue**, so it can touch
   only the pull request that started it.
4. **Prompt:** type this:

   ```text
   Review this pull request against its ticket. Only comment.
   ```

5. **Tools:** select **Suggest tools**. Keep the tools that read and the one that adds a comment;
   untick anything that pushes, merges, closes, or changes labels.
6. **AI credit limits:** set **Per run** to `100` and **Daily** to `300`. Every run uses AI
   credits; these limits cap what one run and one day can cost. Select **Create automation**.
7. **Fire it.** Open your draft pull request and select **Ready for review** at the bottom of
   **Conversation**. That click is the trigger. On your repository's **Agents** page a
   **Reviewer** session starts within a minute, and a few minutes later its comment appears on
   the pull request, with your name on it: a personal automation acts as you. **No Ready for review button?** Your pull request is not a draft: open
   **Agents > Automations > Reviewer**, select **Run**, choose the trigger **Ready for review**,
   paste your pull request's address under **Resource URL**, and select **Run now**.
8. **Check the reviewer.** For each point it makes, look at the screenshots and the ticket
   yourself. Do you agree? An automation's review can be wrong, like any answer: your own check
   decides.

**Check:** your Reviewer's comment is on your pull request, and you checked each of its points
yourself.

## 4. Merge, Release, and Checkpoint

**02:15-02:45.** **Slide: You decide · Agents do.** Your merge is the one step only you take.

1. **Merge.** On the pull request select **Merge pull request** and **Confirm merge**, then
   **Delete branch**. GitHub may then offer **Delete codespace**: never select it. That is your own
   Codespace, with your work in it.
2. **Released.** The merge starts **Actions > Publish my website** by itself. When it is green,
   about three minutes later, open your website and look at the bottom of the page: the footer
   says **Production · Version 1.0.0.** and the run's build number. Still **Preview**? Reload the
   page.
3. **Closed by itself.** Open your ticket: `Closes #1` in the pull request closed it when you
   merged. Still open? Select **Close issue**.
4. **Switch off your automation.** Open **Agents > Automations > Reviewer** and choose **Disable**:
   every run uses AI credits. You can switch it on again on Friday.
5. **Back in your Codespace,** open **Source Control** and select **... > Pull**, so your
   Codespace has Copilot's change too.
6. **Show a neighbour** four things: your Copilot project's **Overview**, the pull request with its
   screenshots and the Reviewer's comment, your merge, and the footer of your live website.

**Done when:** your website is live at its own address, a Copilot project built your ticket as a
pull request, GitHub checked it with desktop and phone screenshots, your Reviewer automation
reviewed it when you marked it ready, and after your merge the footer of your live website says
Production and its version number.

**What you just learned:** one push saved your work and published it with a version number. A
ticket said what done means, a Copilot project built it in the cloud, GitHub checked it in a
browser and showed you the screenshots, and an automation reviewed it. Every step started with an
event (a push, a new pull request, your click on **Ready for review**, your merge), not with a
meeting, and you made every decision. Tomorrow you make the checks required, try every pull
request on a test copy of your website, and approve each release: see the
[Day 5 guide](DAY-5.md).

## Optional extras

1. **Two tickets in parallel.** Write a second, small wish with **Issues > New issue >
   Requirement**, in plain words with two acceptance criteria you can check by clicking or
   counting. In your Copilot project send `Build ticket #2 in the cloud as a pull request.`
   Merge one pull request, then the other. If GitHub says the second **has conflicts**, comment
   `@copilot Fix the merge conflicts with main.` on it and wait.
2. **A project that keeps working.** In your Copilot project send
   `Every weekday at 9 AM, suggest my next ticket.` Select **Automations** at the top of the
   right-hand panel to see it, and choose **Pause** before you leave.
3. **Watch the version climb.** Any change you merge publishes again: the footer shows the next
   build number.

## Official References

- [Working with projects in the GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/working-with-projects)
  and [agent sessions](https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions).
- [Copilot automations](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automations)
  and [creating an automation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-automations).
- [About the cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
  and [reviewing its pull requests](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/review-copilot-output).
- [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
  and [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
- [The run number and other workflow values](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context).
- [Source control in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
