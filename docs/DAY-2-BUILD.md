# Day 2: Build Your Own Idea

Today is supported building, not another sequence of technical labs. The presenter and helpers
will work with you at the table. Use the same Chat, preview, checking, and saving habits as Monday.
Your prototype uses fictional content in the app, not a live database or confidential work data.

David explains business/IT responsibilities and approved tools first; Jackie explains shared
data and Power Platform through examples. You are not expected to connect a database, install
tools, configure the internal marketplace, or implement authentication during this session.

## Choose One Useful Outcome

Use your submitted idea and assigned, prepared repository. If you have no idea yet, continue
the weekend planner or choose a fictional event calendar, reading list, or simple follow-up list.
A real spreadsheet, employee list, or customer report is not needed to show the idea.

Before building, tell your helper:

| Question | Example |
| --- | --- |
| Who is this for? | Someone organising a fictional internal event. |
| What should they be able to do? | Add an event and filter by day. |
| What is the smallest first version? | One page with a list, form, and filter. |
| How will I check it? | Add a fictional event, filter, reset, and confirm the right entries appear. |

If you need a separate project, the helper provides an approved prepared repository. Do not
overwrite Monday's page or create a new public repository to get started. If a separate project
is unavailable, keep improving your existing page and record the new idea in your brief.

## Morning Build: 10:45-12:15

The presenter demonstrates the next action only when needed, then gives you time to try it.

1. **Agree the first version (15 minutes).** Write the four answers above in your project brief.
   Ask Chat to propose a small plan using fictional examples and the existing project setup.
2. **Build one page (30 minutes).** Ask for that version, inspect the files, and open the private
   preview using the familiar prepared command and Ports link. Tell a helper if it does not open.
3. **Make one useful interaction (25 minutes).** Add a form, filter, or selection. Keep everything
   else unchanged. Compare your expected result with what you actually see.
4. **Save a checkpoint (20 minutes).** Review, save, commit, push, and read back the same branch
   on GitHub. Record one success, one limitation, and the next change. Do not force a rejected push.

Example request:

> Read my brief. Propose the smallest first version of this page using fictional sample data
> stored in the app. Keep the existing simple project setup. No database, login, API keys,
> integrations, or deployment. Ask before replacing an existing file. After I approve the plan,
> help me build one feature and describe a manual check I can perform myself.

## Afternoon Build: 13:00-14:45

Continue at your own pace. Choose one improvement at a time, then check it:

- Clearer labels or layout: ask a neighbour to try the page without explaining each button.
- Better input handling: empty values should not create an invalid item.
- A filter, sort, or count: compare the result with your known fictional entries.
- Narrow-screen and keyboard use: controls remain readable and reachable.
- Remembering entries: optional; test add -> refresh -> remove -> refresh in your own browser.

Expect -> try -> compare -> improve -> repeat. Record the actual result rather than relying on
Copilot saying it works. Recheck an existing feature after each change. Save reviewed progress
before starting a larger experiment. A helper may show a prepared tool when useful, but CLI,
MCP, and Playwright are not tasks everyone must complete today.

At 14:00, helpers also support optional publication through the existing workflow when the page
and prepared access are ready. Follow [Lab 08](../labs/08-deploy/README.md); a private preview is
enough to finish. Do not make a port public or switch to a different deployment target as a shortcut.

## Show and Plan the Next Step: 14:45-15:00

Everyone can share with a neighbour. A few volunteers can show the room their result; there
is not time for every attendee to give a five-minute stage demonstration.

Show one feature, one check, and one way it might help your work. Then record the questions
for the technical owner: what data would be needed, who should have access, what integrations
are missing, and what approval is needed before it becomes a real application.

**Done when:** you have a checked own-idea prototype or improved default app, reviewed work
visible in GitHub, and a short next-step note. Database connections, automated browser checks,
and public deployment are not completion gates.

## Before Any Corporate Handover

Stay in the approved browser-based Codespace. Your technical owner must separately confirm
repository/client access, approved AI services, runtime, permissions, data classification, and
support. Familiar VS Code menus do not guarantee identical extensions or authentication.
Do not remove training membership or delete accounts; save your work and ask the owner first.

The [post-workshop Dataverse reference](../post-workshop/dataverse/README.md) preserves technical
setup guidance and prompts for that later owner-led session. It is not additional homework.

## Optional extras

1. Ask for two alternatives to one confusing control, choose one, and retest it.
2. Write a short plain-language handover that accurately distinguishes working features from ideas.
3. Record an additional test case for the later technical track without installing a new tool now.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Review AI-generated edits](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Source control in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Ports and previews](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).
- [Whole-week topic map](REFERENCES.md).