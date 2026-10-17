# Day 2: Build Your Own Idea

Today you build your own idea, with help at your table. After the two talks in the morning there
are no more presentations: helpers work with you at the tables. Use the same habits as Monday:
ask in Chat, watch the preview, check it yourself, and save. Use made-up content only, never
real work data.

## Today's Route

| When        | What happens                                                            |
| ----------- | ----------------------------------------------------------------------- |
| 09:00-09:30 | David: how business and IT work together, and which tools are approved. |
| 09:30-10:30 | Jackie: how shared data and the Power Platform work, through examples.  |
| 10:30-10:45 | Break.                                                                  |
| 10:45-12:15 | Morning build, with help at your table.                                 |
| 12:15-13:00 | Lunch.                                                                  |
| 13:00-14:45 | Afternoon build, at your own pace.                                      |
| 14:45-15:00 | Show a neighbor and plan your next step.                                |

You do not set up anything from the morning talks today.

## Choose One Useful Outcome

Pick the idea you sent in. If you do not have one yet, keep improving Monday's page; that is
fine. You never need a real spreadsheet or customer list to show an idea.

Before building, tell your helper:

| Question                            | Example                                                  |
| ----------------------------------- | -------------------------------------------------------- |
| Who is this for?                    | Someone organizing a made-up team event.                 |
| What should they be able to do?     | Add an event and filter by day.                          |
| What is the smallest first version? | One page with a list, a form, and a filter.              |
| How will I check it?                | Add a made-up event, filter, and see the right entries.  |

Everything stays in your own repository. Your idea gets its own folder under `site/ideas/`, so
Monday's page is never replaced. You can keep working on this idea on Days 3 and 4.

## Morning Build: 10:45-12:15

1. **Agree the first version (15 minutes).** Tell your helper your four answers and agree the
   smallest first version. Do not create any files yet.
2. **Build one page (30 minutes).** Run `/create-website` once, choose your own idea, and
   describe it in one sentence. Copilot builds it in its own folder, such as
   `site/ideas/team-lunch/`, with its own `brief.md`, and opens it beside Chat. Add your four
   answers to that brief. To open it again later, type `/start-website team-lunch`, using your
   folder's name.
3. **Add one useful thing (25 minutes).** Ask for a form, a filter, or a choice. Keep everything
   else the same. Compare what you expected with what you see.
4. **Save (20 minutes).** Save, review, commit, and push, then find your folder on GitHub. In your
   brief, write one thing that works, one thing that does not work yet, and your next step.

If you are not sure what to ask, try:

> Read the brief.md in my idea's folder. Suggest the smallest first version of this page using
> made-up sample data in the page. No database, login, API keys, integrations, or publishing.
> Ask before replacing a file. After I say yes, build one feature and tell me how to check it myself.

## Afternoon Build: 13:00-14:45

Keep going at your own pace. Pick one improvement at a time and check it:

- **Clearer words:** ask a neighbor to try the page without your help.
- **Empty entries:** an empty box should not add an empty item.
- **A filter, sort, or count:** compare the result with your made-up entries.
- **Keyboard and narrow window:** buttons are still easy to read and to reach.

Expect -> try -> compare -> improve -> repeat. After each change, check that the older features
still work, and save before you try something big. The terminal (CLI), MCP, and browser tools
come on Wednesday, not today.

From 14:00, helpers can help you publish if you want to, using
[Lab 08's optional route](../labs/08-save-and-share/README.md#publish-with-a-helper). Your preview is
enough to finish.

## Show and Plan the Next Step: 14:45-15:00

Show a neighbor one feature, how you checked it, and how it might help your work. A few
volunteers show the room; everyone gets a turn on Friday.

Then write down your questions for IT: what real data it would need, who should have access,
which systems it would connect to, and what approval it needs to become a real app.

**Done when:** you have a checked first version of your idea (or a better Monday page), your work
is on GitHub, and you wrote your next step. Database connections, automated browser checks, and
public deployment are not completion gates. On Wednesday you will learn a few more ways to use
Copilot on this same work: see the [Day 3 guide](TOOLS-PRACTICE.md).

Keep working in this Codespace. Moving an idea to company tools later needs your technical
owner's approval, so save your work and ask first. Never remove training access or delete an
account yourself. Technical owners use the [Dataverse reference](../post-workshop/dataverse/README.md)
for that later step.

## Optional extras

1. Ask for two other versions of one confusing button, pick one, and check it again.
2. Write a short, plain note for IT that keeps "works today" and "ideas for later" apart.
3. Write down one check you would like to see Copilot's browser try on Wednesday.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Review AI-generated edits](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Source control in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Topic map (for presenters)](REFERENCES.md).
