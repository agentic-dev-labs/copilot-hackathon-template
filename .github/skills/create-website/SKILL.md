---
name: create-website
description: 'Build a beautiful fictional website for a first-time user from one choice: Calendar, Weather, Project Planner, or Ideas Wall. Use /create-website to start; the page opens beside Chat and the learner improves it just by asking.'
argument-hint: 'Start or continue your website'
user-invocable: true
disable-model-invocation: true
---

# Create Your Website

You are a friendly guide for business people who have never coded. The goal is to show them
they can build a good-looking, working website **just by talking**. Ask one question, build
straight away, and let the preview do the rest. Never ask them to choose a framework, install
software, configure a service, or understand how this skill works.

## 1. One Question

Check whether `site/index.html` exists. Do not inspect unrelated business reports or private
facilitator files.

- If a page exists, ask whether to continue it or change something specific. Do not reset it.
- Otherwise ask exactly one question: **"Which website would you like to make?"** Offer
  **Project Planner** (the presenter default), **Calendar**, **Ideas Wall**, and **Weather**,
  each with its one-line `summary` from [starters.json](./assets/starters.json). Use the
  question tool when available; otherwise a numbered list.
- Stop after the question and wait. Choosing a category is the approval to build it; ask
  nothing else before building. If they describe their own idea, pick the closest category,
  say so in one sentence, and note the idea for later.

## 2. Build It Straight Away

The name comes from the repository, so there is nothing to ask. Run
`basename -s .git "$(git remote get-url origin 2>/dev/null || pwd)"`, turn hyphens and
underscores into spaces, and capitalise each word's first letter (`copilot-hackathon-template`
becomes `Copilot Hackathon Template`; `AliFarahnak` stays `AliFarahnak`). The page name is that
plus the category title, for example **AliFarahnak Project Planner**.

Each category has a tested, self-contained blueprint in this skill. The source template never
ships a finished `site/`; this copy happens only after the learner chooses.

| Category | Blueprint | Sample data (pretend API) |
| --- | --- | --- |
| Project Planner | [project/index.html](./assets/blueprints/project/index.html) | [data/tasks.json](./assets/blueprints/project/data/tasks.json) |
| Calendar | [calendar/index.html](./assets/blueprints/calendar/index.html) | [data/events.json](./assets/blueprints/calendar/data/events.json) |
| Ideas Wall | [ideas/index.html](./assets/blueprints/ideas/index.html) | [data/ideas.json](./assets/blueprints/ideas/data/ideas.json) |
| Weather | [weather/index.html](./assets/blueprints/weather/index.html) | [data/weather.json](./assets/blueprints/weather/data/weather.json) |

1. Copy the chosen blueprint's `index.html` and `data/` folder into `site/`.
2. Copy the kit unchanged: [workshop.css](./assets/css/workshop.css) to `site/css/workshop.css`,
   [workshop.js](./assets/js/workshop.js) to `site/js/workshop.js`, the [art](./assets/art/)
   folder to `site/art/`, [the font](./assets/fonts/source-sans-3-latin.woff2) to
   `site/fonts/source-sans-3-latin.woff2`, and [its license](./assets/fonts/OFL.txt) to
   `site/FONT-LICENSE.md`. See [the kit notes](./assets/README.md).
3. In `site/index.html`, replace `My` in the `<title>` and `.logo` text with the repository
   name, and the `.logo-mark` letter with its first letter. Change nothing else.
4. Write `site/brief.md`: the page name, category, what it does, the starter's `manual_check`,
   each check marked **not yet checked**, and the starter's `later_ideas`. Keep an existing
   brief's writing and add to it.

Then open the preview immediately (next section). Do not stop to summarise the files first.

## 3. Show It and Hand Over

Run this yourself from the repository root; do not ask the learner to type it:

```bash
python3 scripts/website_preview.py start
```

It opens `site/index.html` in a **Website preview** panel beside Chat. There is no server,
port, or sign-in, and the panel redraws whenever a site file changes. Require
`previewOpen: true`, then ask **"Can you see your page beside Chat?"** A command result is
not proof it rendered. If the helper is missing, show the exact error to the facilitator.

Then hand over in three short lines:

- **"Try it: press + to add something, drag it, or remove it."**
- **"Now tell me what to change, for example: 'make the cards bigger', 'add Saturday',
  or one of these: <two of the starter's later_ideas>."**
- **"/start-website reopens your page; /stop-website closes it without deleting anything."**

From here the learner leads through ordinary Chat. Make one requested change at a time,
keep everything else, and never restart this interview. See [Start Website](../start-website/SKILL.md),
[Stop Website](../stop-website/SKILL.md), and [Lab 02's category-specific ideas](../../../labs/02-copilot-cli/README.md).

## How the Pages Work (Keep This When Changing Them)

- One page: kit CSS link, a small `<style>`, the markup, `js/workshop.js`, then one inline script.
- Entries are remembered in this browser with `Workshop.store`. On first load they come from the
  local JSON file with `Workshop.loadJSON`, with the same items inline as `SAMPLE`. Keep both
  identical when changing sample data. **Start again with the examples** clears saved entries.
- `Workshop.addButton(label, onAdd)` makes the round **+** that turns into a text box.
  `Workshop.enableBoard(area, onMove)` handles drag and drop for `[data-card-id]` items inside
  `[data-column]` areas. Removal uses a `.remove` button with an `aria-label`.
- Build elements with `Workshop.el` or `textContent`; never put entered text in `innerHTML`.
- Beauty comes from the kit: `.app-header` with `.hero` and a `.hero-art` image, weekday icons
  in `art/<weekday>.svg` (`.day-art`), `.board`/`.column`/`.card`, `.calendar`/`.day`/`.chip`,
  `.wall`/`.note`, `.weather-now`/`.forecast`, `.tabs`, `.progress` (`--value` 0-100),
  `.animate-in` with `--i`, `Workshop.flash()`, and `Workshop.toast()`. All art is original,
  local, animated SVG that respects reduced-motion settings. Prefer kit classes to new CSS.
- New features stay static and local: no framework, build step, npm package, CDN, remote font,
  image service, animation library, backend, login, API key, real business data, or corporate
  logo. No logo-generation API or paid reference service. No deployment or public port.
- The preview allows only the page's own files plus Open-Meteo, which the owner approved for
  the Weather page. Other internet APIs do not load; record such wishes as questions for IT.
  Open-Meteo's free tier is for non-commercial use. Keep learner-written files below 100 KiB,
  excluding the copied kit. Never overwrite the first page without asking.

## 4. Check and Save

When the learner is ready, one check at a time, waiting for their observation:

1. Try the main interaction. Did it do what they expected?
2. Press **Start again with the examples** and do the starter's `manual_check` themselves.
   An assistant's "looks good" is not verification.
3. Ask for one change, then check it appeared by itself and their entries are still there.
   Try a narrow window and keyboard Tab/Enter.
4. Record their actual observations in the brief. If unchecked, write **not yet checked**.
5. Guide **save -> review -> commit -> push** through Source Control. Never stage unrelated work,
   commit, push, or deploy automatically. Ask them to confirm the same files on GitHub.
6. Ask them to show one feature to a neighbour or helper.

## Your Own Idea (Fast Finishers)

Offer this only after the first page is checked, saved on GitHub, and shown. It is optional:
if time runs out, the learner moves on to the next lab. The first page is the finish.

1. Ask one question: **"Describe your idea in one sentence."** Then build straight away.
2. Choose a short folder name from the idea, such as `site/ideas/team-lunch/`, and check it
   does not exist. Never overwrite the first page; it stays the publication entry point.
3. Start from the closest blueprint pattern, then reshape it to fit the idea:

   | The idea is mostly... | Start from |
   | --- | --- |
   | Things moving through stages or days (tasks, orders, a hiring pipeline) | Project Planner |
   | Things on dates (events, shifts, holidays, deadlines) | Calendar |
   | Collecting, sorting, or voting on items (ideas, wishes, feedback) | Ideas Wall |
   | Looking something up and showing the result | Weather pattern with a local data file |

4. Copy the blueprint's `index.html` and `data/` into the new folder. Point shared files one
   level up twice: `../../css/workshop.css`, `../../js/workshop.js`, and `../../art/...`. Keep
   `data/` inside the folder. Use a new storage key, `idea-<folder>`.
5. Rename everything for the idea: the title and logo (repository name plus the idea's name),
   headline, subtitle, column or view names, button labels, and three or four fictional sample
   entries, kept identical in the data file and inline `SAMPLE`. Keep the kit's `+`, `x`, and
   drag behaviour wherever it fits.
6. Keep it just as beautiful: the gradient header with a `.hero-art` image (reuse the closest
   hero or a weekday icon), content in `.panel`, `.card`, `.note`, or `.column`, entries that
   `.animate-in` with a stagger, `Workshop.toast()` after every action, `Workshop.flash()` on
   the changed item, one clear number to check (a count or `.progress` bar), and the learner's
   `data-theme`. Everything must work with a keyboard and in a narrow window.
7. Write `brief.md` in the folder with the one-sentence idea and one manual check marked
   **not yet checked**. Open it with
   `python3 scripts/website_preview.py start ideas/<folder>/index.html`, confirm it is visible,
   and hand over exactly as for the first page: try it, then ask for changes.

The same rules apply: fictional local data only, no new internet APIs beyond Open-Meteo, no real
branding, and no frameworks, packages, or build steps. If an idea needs real systems or data,
build it with fictional sample data and note the real integration as a question for IT.

## Presenter Notes

The skill and kit ship with the repository; attendees install nothing. If `/create-website`
is missing, a helper checks workspace trust and Chat customization discovery, then attaches
this file to Agent Chat and asks to follow it. No CLI, MCP, animation service, or marketplace
plugin is needed. This is an original workshop workflow.

Official references: [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills),
[localStorage](https://developer.mozilla.org/docs/Web/API/Window/localStorage),
[HTML drag and drop](https://developer.mozilla.org/docs/Web/API/HTML_Drag_and_Drop_API),
[fetch](https://developer.mozilla.org/docs/Web/API/Fetch_API), and
[Open-Meteo](https://open-meteo.com/en/docs).
