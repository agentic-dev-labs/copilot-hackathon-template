# Day 4: Build Day

Today you build the idea you picked yesterday. Helpers work at the tables; there are short
check-ins, not long demonstrations. Use the same Codespace, the same Chat, and fictional content
only. The goal is **one working thing you can show tomorrow in three minutes**.

## Today's Route

| When        | What you do                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------- |
| 09:00-09:15 | Recap and goal. Optional: hand one small change to the cloud agent ([Lab 03](../labs/03-cloud-agent/README.md#optional-try-on-day-4)). |
| 09:15-10:30 | Build your idea with help at the tables.                                                           |
| 10:45-11:45 | Quick check-in, then keep building.                                                                |
| 11:45-12:15 | Check it yourself; review the cloud agent's pull request if you tried it.                          |
| 12:15-12:30 | Save to GitHub and prepare your three-minute story.                                                |

The [agenda](AGENDA.md) includes the break. If you have no idea yet, keep improving Monday's page;
that is a good thing to show.

## Build in Small Steps

Use the loop you already know: **ask for one change -> watch the preview -> check it -> save.**

- Describe one change at a time: "Change **this one thing** for **this audience**. Keep
  **these things** unchanged. I will check it by **this action**."
- Your idea's page lives in its own folder under `site/ideas/`. Type `/start-website` and your
  folder's name, for example `/start-website team-lunch`, to open it beside Chat.
- Use whichever tool helps: Chat, Copilot CLI in the terminal, the GitHub tools from
  [Lab 04](../labs/04-mcp/README.md), and your instructions file and `/check-my-page` skill from
  [Lab 06](../labs/06-multi-agent/README.md).
- When something is wrong, say: "I expected [result]. I actually saw [result]. Fix only that."
  If Copilot changes more than you asked, select **Stop** and ask a helper.
- Save a checkpoint about every 30-45 minutes: save, review, commit, and push.
- If your idea is a skill rather than a page, use the same loop: run it with made-up input,
  compare the result with what you expected, improve its `SKILL.md`, and save.

No database, login, API keys, integrations, or real work data. If your idea needs a real
system, build it with made-up sample data and write the real connection down as a question for IT.

## Check-In at 10:45 (5 minutes)

Tell your table or helper three things: what works, what you will do next, and what is blocking
you. If you are stuck for more than ten minutes at any time, raise your hand.

## Check It Yourself (11:45-12:15)

1. Run `/check-my-page` with your page's path, such as `/check-my-page site/ideas/team-lunch/index.html`,
   or do the check written in your brief by hand.
2. Try an empty input, the keyboard (Tab and Enter), and a narrow window. For a skill, run it on
   three made-up examples, including one with missing information, and check it does not guess.
3. Write what actually happened in your brief, including anything that does not work yet.
4. If you tried the cloud agent, review its pull request first, by 12:00, with a helper using
   [Lab 03's steps](../labs/03-cloud-agent/README.md#optional-try-on-day-4).

"Copilot says it works" is not a check. Your own click and your own count are.

## Prepare Your Three-Minute Story (12:15-12:30)

Write these four short answers in your brief under a heading called **My story**:

1. **What I built:** who it is for and the problem it helps with.
2. **Show it:** the one thing you will click through live.
3. **How I checked it:** one check and what you found.
4. **How I would use it at work:** the next step, or a question for IT.

Then save, review, commit, and push. You can keep improving your work before Friday in the same
Codespace. Stop your Codespace when you finish for the day; closing the browser tab does not stop it.

**Done when:** you have a working first version of your idea, or a clear improvement, that you
checked yourself, your work is visible on GitHub, and your story is written in your brief.

## Optional extras

1. Publish your page with a helper using [Lab 08's optional route](../labs/08-deploy/README.md#publish-with-a-helper).
2. Ask a neighbor to try your page without help, and write down where they got stuck.
3. Add one plain sentence at the top of your page telling a first-time visitor what to do.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Review AI-generated edits](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Source control in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Whole-week topic map](REFERENCES.md).
