# Lab 02: Make Your Website Useful

**Objective:** Make your website look like yours, add one useful feature, and check it yourself.

**Time-box:** 60 minutes

**Prerequisites:** Your checked page from Lab 01, in the same Codespace. Copilot CLI comes later, on **Day 3**.

The presenter shows one change, then you try it on your own page. Keep talking to Copilot in
normal Chat. This is not a new creation interview, so do not run `/create-website` again.

### 1. Choose Two Changes (10 minutes)

Pick **one appearance change** and **one feature change** for your website. These are ideas, not
a list to finish. If a feature already works, improve it or pick another one.

| Your Website | Appearance Ideas | Feature Ideas |
| --- | --- | --- |
| Project Planner | A sky blue or soft coral look, bigger cards, a calmer header | Owner name on each card, due dates, hide finished tasks |
| Calendar | Color notes by type, larger day numbers, a softer today highlight | Start times, a "this week" count, your country's public holidays |
| Ideas Wall | Larger notes, different sticky-note colors, a bolder headline | A vote button with a count, themes, a search box |
| Weather | A different color theme, a larger temperature, a friendlier headline | A Fahrenheit/Celsius switch, a "what to wear" tip, sunrise and sunset |

Ask: "Read my brief and my page. I want to improve [appearance] and [feature]. Suggest two small
changes, but do not build them yet. Keep the rest working."

### 2. Make the Design Yours (15 minutes)

Describe what you want in ordinary words. For example:

> Keep the page light. Try a sky blue look. Keep the text easy to read and leave the content
> and features unchanged.

> Give the cards more space and make the + buttons easier to see. Keep my colors.

Look at the change in **Source Control**, save, and watch the preview update. You do not need
any design words or codes. If the preview is closed, type `/start-website`.

**Be brave once, then undo it.** Ask for something wild, such as "Make the whole page bright
purple with giant text." Look at the preview. Then, in Chat, select **Undo** for that change:
Copilot shows **Keep** and **Undo** after each change it makes, and **Undo** puts your files back
the way they were. Your page returns to normal. Now you know you can always go back.

**Two optional wows, if you have time:**

- **Let Copilot draw a picture.** Ask: "Draw a friendly rocket for the top of my page, in my
  colors." It appears in a few seconds. Not right? Ask again, or select **Undo**. Made-up
  pictures only: no real people, logos, or company names.
- **Show Copilot a sketch.** Drag **docs > images > sketch-example.png** from the Explorer into the
  chat box and ask: "Make my page look more like this sketch. Keep all my entries and features."

![A hand-drawn page sketch: a wide header with a sun doodle, a big centered title, a short welcome line, and a small "3 of 5 done" badge; three rounded cards with an orange stripe on top; a big round + button at the bottom right. Orange notes say warm sunset colors, rounded cards with lots of space, and big round + button.](../../docs/images/sketch-example.png)

If Copilot says it cannot see pictures, skip the sketch. A photo of your own sketch works too,
but never a picture with real work information in it.

### 3. Add One Feature (15 minutes)

Use one of these, changed to fit your page:

| Category | Ask Copilot |
| --- | --- |
| Project Planner | "Add an owner name to each task card, shown small under the title, and let me type it when I add a task. Keep the design unchanged." |
| Calendar | "Let me give each note a type: meeting, personal, or deadline, each with its own color. Keep the design unchanged." |
| Ideas Wall | "Add a thumbs-up button with a count to each idea, and a button to sort by most votes. Keep the design unchanged." |
| Weather | "Add a switch between Fahrenheit and Celsius that remembers my choice. Keep the design unchanged." |

Ask for a short plan first, say yes, and let Copilot make the change. Save and watch the preview.

### 4. Check It Yourself (15 minutes)

Start from the example entries for your page:

| Your Website | One Example Check |
| --- | --- |
| Project Planner | 1 of 4 done. Tick a second task: 2 of 4, and the bar grows. Untick it: 1 of 4 again. |
| Calendar | 3 notes planned. Add one on Friday: 4. Drag it to Monday: still 4, now on Monday. |
| Ideas Wall | 3 ideas. Add one: 4. Drag it to the front, then remove it: 3 again. |
| Weather | Pick another city and compare today's temperature with **the raw forecast data** link. |

If you changed the entries, write down what you expect first. Also try an empty entry, the
keyboard (Tab and Enter), and a narrow window. Do the older features still work?

If something is wrong, say: "I expected [this]. I saw [that]. Fix only that, and keep [the part
that works] unchanged." Then check again. Copilot saying it works is not a check.

### 5. Write It Down (5 minutes)

Show a neighbor your new look and your new feature. In **site/brief.md**, write what you tried,
what happened, and what you would improve next. Save. The next block saves it to GitHub.

**Done when:** your page has one design change, one working new feature, and an honest check
written in your brief. Entries that stay after a refresh are a bonus, not a requirement.

## When It Does Not Work

| What you see                        | What to do                                                        |
| ----------------------------------- | ----------------------------------------------------------------- |
| A blank page or no preview          | Type `/start-website`. If it is still blank, show a helper.       |
| Entries disappear after a refresh   | Show a helper; the page should remember them in this browser.     |
| A number looks wrong                | Count it yourself and tell Copilot what you expected.             |

## Optional extras

1. **Your own idea (fast finishers).** Only after your page is checked, saved on GitHub, and
   shown to a neighbor: run `/create-website`, choose your own idea, and describe it in one
   sentence. Copilot builds it as an own-idea extension in a separate folder under `site/ideas/`,
   and your first page stays unchanged. If time runs out, stop; Tuesday has more time.
2. Add sorting, a theme switch, or favorites, then repeat your checks. Or take a challenge from
   [Lab 08's challenge card](../08-deploy/README.md#3-take-a-challenge-15-minutes).
3. Ask for a smaller or clearer version of one button.
4. Your entries are remembered with localStorage, in this browser only. It is not a shared
   database: another browser, or a published page, starts with the examples again.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Reviewing and undoing changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Adding a picture to Chat](https://code.visualstudio.com/docs/chat/copilot-chat-context).
- [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) and the [whole-week topic map](../../docs/REFERENCES.md).
