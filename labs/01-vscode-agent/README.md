# Lab 01: Build Your First Page

**Objective:** Build a small website by talking to Copilot, see it beside Chat, and change it.

**Time-box:** 60 minutes

**Prerequisites:** Lab 00 and [your first note](../../docs/START-HERE.md#your-first-note), in the
same Codespace. Nothing to install.

You choose one of four starter websites: **Project Planner**, **Calendar**, **Ideas Wall**, or
**Weather**. The presenter builds the Project Planner; pick it if you are unsure. All four work
the same way, and everything on them is made up. The presenter shows each step, then you try it.

## 1. Pick Your Website (10 minutes)

1. In Chat, choose **Agent**. Type **`/create-website`**, pick it from the list, and press Enter.
2. Copilot asks one question: which website would you like to make? Choose one.
3. It builds the page straight away and names it after your repository, for example
   **AliFarahnak Project Planner**. You can change anything later just by asking.

**Check:** a new **index.html** appears in **Explorer > site**. Seeing the file is the proof,
not Copilot saying "done". If `/create-website` is not in the list, ask a helper.

## 2. Open Your Preview (15 minutes)

Copilot opens your page in a **Website preview** panel beside Chat.

1. Find your page beside Chat. Its title uses your repository's name.
2. Press **+** to add a made-up entry, then drag it somewhere else.
3. Ask Copilot for one small change, such as "Make the title bigger. Leave the rest alone."
   Watch the change appear by itself. Your entry is still there.
4. Type `/stop-website` to close the preview, then `/start-website` to open it again. The same
   page comes back.

The page remembers your entries in this browser. If you remove them all, the examples come back.

**If the preview does not open,** show a helper the exact message and do not install anything.
A helper can run `python3 scripts/website_preview.py status` to see what is wrong.

## 3. Peek Inside the Code (15 minutes)

Your page is made of code: plain text that tells the browser what to show. You do not need to
learn it. Just take a look, with Copilot as your guide.

1. In the **Explorer**, open **site > index.html**. This is the code behind your page. Scroll
   through it. It is only text.
2. Select about five lines near the top: click at the start of the first line, then hold
   **Shift** and click at the end of the fifth. In Chat, ask: "Explain the lines I selected in
   plain English, one short sentence per line. I have never seen code before." Copilot reads
   your selected lines automatically.
3. Find your page's big headline: click anywhere inside index.html, press **Ctrl+F** (**Cmd+F**
   on a Mac), type `<h1>`, and press Enter. The words between `<h1>` and `</h1>` are the headline you see on
   your page, for example *Plan the week, one card at a time*.
4. Change one or two of those words yourself, by typing. Leave `<h1>` and `</h1>` exactly as
   they are. Choose **File > Save** and watch the preview update by itself.

**Check:** your new words appear on your page. You just changed code with your own hands.
If the page looks broken, press **Ctrl+Z** (**Cmd+Z** on a Mac) until your typing is undone,
save again, and ask a helper if it still looks wrong.

## 4. Make One Change (10 minutes)

Now let Copilot do the typing. Ask for one change in ordinary words, and add "Leave the rest
alone." For example:

| Your website    | Try asking                          |
| --------------- | ----------------------------------- |
| Project Planner | "Add a Saturday column."            |
| Calendar        | "Make today's date stand out more." |
| Ideas Wall      | "Make the notes bigger."            |
| Weather         | "Add Paris as a city."              |

Open **Source Control** to see what changed, then save. **Check:** your change is there and
everything else still works. If Copilot changed too much, select **Stop**, then **Undo** in Chat,
and ask for something smaller.

## 5. Show and Save (10 minutes)

Show a neighbor your page and the file behind it, **site/index.html**. Let them add and move an
entry. Then save, review, commit, and push, just like your note, and find it on GitHub.

**Done when:** your page opens beside Chat, you changed its headline yourself, one change you
asked Copilot for is visible, and your saved version is on GitHub.

## Coached Verification Block

**11:45-12:15**, right after this lab: **trust, but verify.** Copilot can be wrong, so you check.

1. **Check a button (10 minutes).** Ask for one new button, such as "hide finished tasks",
   "show only this week", or "shuffle the ideas". Say what you expect, click it twice, and
   compare. If it is wrong, tell Copilot: "I expected ..., but I saw ...". Check again after the fix.
2. **Check a number (10 minutes).** Count it yourself, using the table below. Do not trust a
   number you have not checked.
3. **Write it down (10 minutes).** In **site/brief.md**, write what you tried and what happened,
   including anything that does not work yet. Then save, review, commit, and push.

| Your website    | Check it yourself                                                                    |
| --------------- | ------------------------------------------------------------------------------------ |
| Project Planner | 4 tasks and 1 ticked, so the bar reads **1 of 4 done**. Tick one more: 2 of 4.       |
| Calendar        | **3 notes planned**: today, tomorrow, and in three days. Add one: 4 notes planned.   |
| Ideas Wall      | **3 ideas**. Add one: 4 ideas. Remove one: back to 3.                                |
| Weather         | Select **the raw forecast data** link and compare today's temperature with the page. |

Weather is the only page with live data. If the internet is blocked, it says it is showing sample weather.

## When It Does Not Work

| What you see                     | What to do                                                          |
| -------------------------------- | ------------------------------------------------------------------- |
| A blank page or no preview       | Show a helper the exact message.                                    |
| Copilot changed other files      | Select **Stop**, then **Undo** in Chat, and ask for less.           |
| A button or a number is wrong    | Tell Copilot what you expected and what you saw, then check again.  |
| Something asks you to install    | Say no and ask a helper.                                            |

## Optional extras

1. **Your own idea (fast finishers).** After your page is checked, saved, and shown to a
   neighbor, run `/create-website` again, choose to build your own idea, and describe it in one
   sentence. It gets its own folder under `site/ideas/`, and your first page stays as it is. If
   time runs out, stop; Tuesday has more time.
2. Make the page easy to read in a narrow window.
3. Try one of the later ideas listed in your brief, or a challenge from
   [Lab 08's challenge card](../08-deploy/README.md#3-take-a-challenge-15-minutes).

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Review and undo AI changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Chat context](https://code.visualstudio.com/docs/agents/concepts/context): how Copilot reads your selected lines.
- [Source control](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills): how `/create-website` works.
- [Whole-week topic map](../../docs/REFERENCES.md).
