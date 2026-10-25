# Lab 01: Make It Yours and Try More Ideas

**Objective:** Read your page's code, change it by hand, and build one more idea of your own
just by describing it.

**Time-box:** 60 minutes

**Prerequisites:** The morning steps in the [README](../../README.md#monday-morning-follow-along),
including [your first website](../../README.md#your-first-website), in the same Codespace.
Nothing to install.

At 10:45 the presenter shows more websites you can build, then each later step, and you try
each one straight after. Everything you add stays made up.

## 1. See What Else You Can Build (10 minutes)

The presenter shows websites made the same way as yours, just by describing them:

| Website         | What it does                                                            |
| --------------- | ----------------------------------------------------------------------- |
| Weather         | Your cities' forecast, and a 3D chart of their year that you can turn. |
| Princeton Map   | Sights you can filter, add to, and see in 3D.                          |
| Photo Studio    | The workshop AI repaints photos of things, places and pets.            |
| Lab Chase       | A funny 3D maze game: a scientist chases escaped molecules.            |
| Request Tracker | Requests with stages, owners and overdue flags.                        |
| Team Dashboard  | Monthly numbers with a what-if forecast.                               |

Pick one you would like to try, or think of your own.

## 2. Peek Inside the Code (15 minutes)

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
   they are. Choose **File > Save** and watch the preview update by itself. If the preview is
   closed, type `/start-website` first.

**Check:** your new words appear on your page. You just changed code with your own hands.
If the page looks broken, press **Ctrl+Z** (**Cmd+Z** on a Mac) until your typing is undone,
save again, and ask a helper if it still looks wrong.

## 3. Build One More Idea (20 minutes)

1. In Chat, with **Agent** chosen, type **`/create-website`** again. Copilot sees that you
   already have a page and asks what you would like: answer **build my own idea**.
2. Describe it in one sentence, for example one from the table below. Something from your own
   work is welcome too, as long as every entry is made up.
3. Copilot builds it in its own folder, such as `site/ideas/lunch-map/`, and opens it beside
   Chat. Your first page stays exactly as it is.
4. Ask for one change in ordinary words, and add "Leave the rest alone." For example: "Make the
   headline friendlier. Leave the rest alone." Watch the change appear by itself. Like it?
   Select **Keep**.

| You would like... | Say                                                                  |
| ----------------- | -------------------------------------------------------------------- |
| A weather page    | "A weather page for my three favorite holiday cities."              |
| A map             | "A map of my favorite lunch spots in Princeton."                    |
| A game            | "A funny 3D game where a scientist chases escaped molecules."        |
| A tracker         | "A tracker for team requests with stages Submitted, Doing and Done." |
| A dashboard       | "A dashboard of made-up monthly sales by region."                    |

**Check:** a new folder appears in **Explorer > site > ideas**. `/start-website` still opens
your first page; add the folder's name to open your idea, for example `/start-website lunch-map`.
If Copilot changed too much, select **Stop**, then **Undo** in Chat, and ask for something smaller.

Rather improve your first page? Ask for one change to it instead:

| Your website    | Try asking                                 |
| --------------- | ------------------------------------------ |
| Project Planner | "Add a Saturday column."                   |
| Calendar        | "Make today's date stand out more."        |
| Ideas Wall      | "Make the notes bigger."                   |
| Weather         | "Add Paris as a city."                     |
| Princeton Map   | "Add a pin for my favorite coffee place." |
| Photo Studio    | "Make the gallery pictures bigger."        |

## 4. Save and Show (15 minutes)

Show a neighbor your pages and let them try one. Then save, review, commit, and push, just like
this morning: **File > Save All**, then **Source Control**. This time it lists only what
changed: your headline and your idea's folder. Type a short message, select **Commit**, then
**... > Push**, and find your idea's folder on GitHub.

**Done when:** you changed your headline yourself, your own idea opens beside Chat in its own
folder, your first page still works, and both are on GitHub.

## Coached Verification Block

**11:45-12:15**, right after this lab: **trust, but verify.** Copilot can be wrong, so you check.
Use your first page: type `/start-website` to open it beside Chat.

1. **Check a button (10 minutes).** Ask for one new button, such as "hide finished tasks",
   "show only this week", or "shuffle the ideas". Say what you expect, click it twice, and
   compare. If it is wrong, tell Copilot: "I expected ..., but I saw ...". Check again after the fix.
2. **Check a number (10 minutes).** On your first page, count it yourself, using the table
   below. The table counts the example entries, so add the ones you made: with the task you
   added at 10:00, the planner shows **1 of 5 done**. If your first page is your own idea, use
   the check in its **brief.md**. Do not trust a number you have not checked.
3. **Write it down (10 minutes).** In **site/brief.md**, write what you tried and what happened,
   including anything that does not work yet. Then save, review, commit, and push.

| Your website    | Check it yourself                                                                    |
| --------------- | ------------------------------------------------------------------------------------ |
| Project Planner | 4 tasks and 1 ticked, so the bar reads **1 of 4 done**. Tick one more: 2 of 4.       |
| Calendar        | **3 notes planned**: today, tomorrow, and in three days. Add one: 4 notes planned.   |
| Ideas Wall      | **3 ideas**. Add one: 4 ideas. Remove one: back to 3.                                |
| Weather         | Select **the raw forecast data** link and compare today's temperature with the page. |
| Princeton Map   | **18 places**. Choose History: 6. Press **+**, name a place and click the map: 19.   |
| Photo Studio    | **6 pictures**. Make the sleepy cat into a watercolor and save it: the gallery shows 7. |

Weather is the only page with live data. If the internet is blocked, it says it is showing sample weather.

## When It Does Not Work

| What you see                             | What to do                                                             |
| ---------------------------------------- | ---------------------------------------------------------------------- |
| A blank page or no preview               | Show a helper the exact message.                                       |
| Copilot changed your first page instead of making a new folder | Select **Stop**, then **Undo** in Chat, and say "Build my own idea in its own folder." |
| Copilot changed other files              | Select **Stop**, then **Undo** in Chat, and ask for less.              |
| A button or a number is wrong            | Tell Copilot what you expected and what you saw, then check again.     |
| Something asks you to install            | Say no and ask a helper.                                               |

**If the preview does not open,** show a helper the exact message and do not install anything.
A helper can run `python3 scripts/website_preview.py status` to see what is wrong.

## Optional extras

1. **One more idea.** Run `/create-website` again and describe another idea in one sentence. It
   gets its own folder too. If time runs out, stop; Tuesday has more time for your ideas.
2. Make a page easy to read in a narrow window.
3. Try one of the later ideas listed in your brief, or a challenge from
   [Lab 08's Take a Challenge section](../08-save-and-share/README.md#3-take-a-challenge-15-minutes).

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Review and undo AI changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Chat context](https://code.visualstudio.com/docs/agents/concepts/context): how Copilot reads your selected lines.
- [Source control](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace).
- [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills): how `/create-website` works.
