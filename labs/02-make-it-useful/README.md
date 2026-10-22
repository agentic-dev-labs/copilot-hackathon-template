# Lab 02: Make Your Website Useful

**Objective:** Add a chart or a chat to your page, give it your own look, and check it yourself.

**Time-box:** 60 minutes

**Prerequisites:** Your pages from Lab 01, in the same Codespace. Copilot CLI comes later, on **Day 3**.

The presenter shows one change, then you try it on your own page. You add **one feature**, a
chart or a chat, and make **one appearance change**. Keep talking to Copilot in normal Chat.
This is not a new creation interview, so do not run `/create-website` again.

### 1. Choose Your Feature (5 minutes)

Pick one. It goes on your first page; for your idea's page, add its folder name, for example
`/add-chart lunch-map`. If a feature already works on your page, pick another one.

| Feature   | How to start                                                        | What you get                                                                   |
| --------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| A chart   | Type **`/add-chart`**                                               | A chart drawn from your own entries, even a 3D one, that follows every change. |
| A chat    | Type **`/add-chat`**                                                | An **Ask** button on your page that answers questions about it.                |
| A picture | Ask: "Draw a friendly rocket for the top of my page, in my colors." | A new picture for your page, drawn by the workshop AI in a few seconds.        |

### 2. Add It (15 minutes)

1. In Chat, with **Agent** chosen, start your feature. For a chart, Copilot asks one question:
   which chart? Choose one, such as the Project Planner's **Progress gauge** or its 3D
   **Week skyline**.
2. Watch it appear on your page by itself. Drag a 3D chart to turn it.
3. For a chat, select **Ask** at the bottom right of your page and ask: "What is on this page?"

Not right? Ask again, or select **Undo** in Chat. Pictures stay made up: no real people, logos,
or company names.

### 3. Check It Yourself (15 minutes)

Start from the example entries for your page. For your idea's page, use the check in its
**brief.md**.

| Your Website | One Example Check |
| --- | --- |
| Project Planner | 1 of 4 done. Tick a second task: 2 of 4, and the bar grows. Untick it: 1 of 4 again. |
| Calendar | 3 notes planned. Add one on Friday: 4. Drag it to Monday: still 4, now on Monday. |
| Ideas Wall | 3 ideas. Add one: 4. Drag it to the front, then remove it: 3 again. |
| Weather | Pick another city and compare today's temperature with **the raw forecast data** link. |
| Princeton Map | 18 places. Choose History: 6. Press **+**, name a place and click the map: 19 places. |
| Photo Studio | 6 pictures. Make one into a watercolor and save it: the gallery shows 7. |

- **A chart:** do the check above and watch the chart follow. Does it agree with your own count?
- **A chat:** ask something you can count yourself, such as "How many tasks are done?", and
  compare. The chat can be wrong too.
- **A picture:** is it what you asked for, and is everything in it made up?

If you changed the entries, write down what you expect first. Also try the keyboard (Tab and
Enter) and a narrow window. Do the older features still work?

If something is wrong, say: "I expected [this]. I saw [that]. Fix only that, and keep [the part
that works] unchanged." Then check again. Copilot saying it works is not a check.

### 4. Make the Design Yours (15 minutes)

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

**Optional: show Copilot a sketch.** Drag **docs > images > sketch-example.png** from the
Explorer into the chat box and ask: "Make my page look more like this sketch. Keep all my
entries and features."

![A hand-drawn page sketch: a wide header with a sun doodle, a big centered title, a short welcome line, and a small "3 of 5 done" badge; three rounded cards with an orange stripe on top; a big round + button at the bottom right. Orange notes say warm sunset colors, rounded cards with lots of space, and big round + button.](../../docs/images/sketch-example.png)

If Copilot says it cannot see pictures, skip the sketch. A photo of your own sketch works too,
but never a picture with real work information in it.

### 5. Write It Down (10 minutes)

Show a neighbor your new feature and your new look. In **site/brief.md**, write what you tried,
what happened, and what you would improve next. Save. The next block saves it to GitHub.

**Done when:** your page has a chart or a chat (or a new picture) that you checked yourself,
one design change, and an honest check written in your brief. Entries that stay after a refresh
are a bonus, not a requirement.

## When It Does Not Work

| What you see                                   | What to do                                                    |
| ---------------------------------------------- | ------------------------------------------------------------- |
| A blank page or no preview                     | Type `/start-website`. If it is still blank, show a helper.   |
| The chat says the assistant is not switched on | Show a helper the exact message, and add a chart meanwhile.   |
| Entries disappear after a refresh              | Show a helper; the page should remember them in this browser. |
| A number looks wrong                           | Count it yourself and tell Copilot what you expected.         |

## Optional extras

1. **One more feature.** Ask for one of these, changed to fit your page. Ask for a short plan
   first, say yes, then check it.

   | Category | Ask Copilot |
   | --- | --- |
   | Project Planner | "Add an owner name to each task card, shown small under the title, and let me type it when I add a task. Keep the design unchanged." |
   | Calendar | "Let me give each note a type: meeting, personal, or deadline, each with its own color. Keep the design unchanged." |
   | Ideas Wall | "Add a thumbs-up button with a count to each idea, and a button to sort by most votes. Keep the design unchanged." |
   | Weather | "Add a switch between Fahrenheit and Celsius that remembers my choice. Keep the design unchanged." |
   | Princeton Map | "Add a search box above the list that shows only the places whose name matches. Keep the design unchanged." |
   | Photo Studio | "Add a title box so I can name a picture before I save it to the gallery. Keep the design unchanged." |

2. Add sorting, a theme switch, or favorites, then repeat your checks. Or take a challenge from
   [Lab 08's challenge card](../08-save-and-share/README.md#3-take-a-challenge-15-minutes).
3. Ask for a smaller or clearer version of one button.
4. Your entries are remembered with localStorage, in this browser only. It is not a shared
   database: another browser, or a published page, starts with the examples again.

## Official References

- [Copilot prompting](https://docs.github.com/en/copilot/get-started/best-practices).
- [Reviewing and undoing changes](https://code.visualstudio.com/docs/agents/run/review-code-edits).
- [Adding a picture to Chat](https://code.visualstudio.com/docs/chat/copilot-chat-context).
- [Apache ECharts](https://echarts.apache.org/en/index.html): the chart library behind `/add-chart`.
- [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage): how your page remembers entries.
- [Topic map (for presenters)](../../docs/REFERENCES.md).
