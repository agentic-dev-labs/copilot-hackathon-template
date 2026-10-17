# Workshop Website Kit

Original workshop CSS, a small helper script, original animated artwork, four tested category
blueprints, and fictional sample data. No Novo name, logo, proprietary imagery, corporate
stylesheet, or corporate font is included. The skill copies the chosen blueprint and kit into
`site/` only after the learner picks a category; the source template never ships a finished site.

## File Contract

| Kit file | Learner destination | Purpose |
| --- | --- | --- |
| [css/workshop.css](css/workshop.css) | `site/css/workshop.css` | Themes, header, board, cards, calendar, sticky notes, weather, tabs, progress, toast, motion |
| [js/workshop.js](js/workshop.js) | `site/js/workshop.js` | `store`, `getJSON`, `loadJSON`, `useColumns`, safe `el`, `addButton`, `enableBoard`, `toast`, `flash`, `newId` |
| [js/workshop-chat.js](js/workshop-chat.js) | `site/js/workshop-chat.js`, only when `/add-chat` runs | `Workshop.addChat()`: an "Ask my page" bubble that asks the Website preview, never the network |
| [art/](art/) | `site/art/` | Original animated SVGs: four header illustrations and one icon per weekday |
| `blueprints/<category>/index.html` | `site/index.html` | Tested self-contained page for the chosen category |
| `blueprints/<category>/data/*.json` | `site/data/*.json` | Fictional sample entries; the page's pretend API |
| [fonts/source-sans-3-latin.woff2](fonts/source-sans-3-latin.woff2) | `site/fonts/source-sans-3-latin.woff2` | Local, open-source variable font, Latin subset (28,740 bytes) |
| [fonts/OFL.txt](fonts/OFL.txt) | `site/FONT-LICENSE.md` | Retained font license; Markdown is not published by the static app |
| [starters.json](starters.json) | Summaries, checks, and idea menus | The category list, manual checks, per-category `later_ideas`, and the shared `any_page_ideas` offered at hand-over |

Neither the CSS, the scripts, nor the art makes external requests; the chat bubble only posts questions to the Website preview. The only internet access is
the Weather blueprint's calls to Open-Meteo, which the owner approved; its free tier is for
non-commercial use, and the page falls back to local sample weather when blocked. All palettes
are light: Fresh mint (`green`, default), Sky blue (`blue`), or Soft coral (`coral`) via the
body's `data-theme`. The editor's dark theme does not change the website.

The artwork is original to this workshop: hand-written SVG shapes with CSS animation inside
each file, no scripts or external links, and no third-party license. Every file stops moving
when the visitor asks for reduced motion. Together they stay below 24 KiB.

The font is [Source Sans 3 from Google Fonts](https://github.com/google/fonts/tree/main/ofl/sourcesans3),
downloaded unchanged on 2026-09-22 as [the official Latin WOFF2 subset](https://fonts.gstatic.com/s/sourcesans3/v19/nwpStKy2OAdR1K-IwhWudF-R3w8aZQ.woff2)
and distributed under the included SIL Open Font License. SHA-256:
`7a19a7027e125257d310c6dbd78ae3a30b5ea1e3794d60b12bb28227a003bfda`.
Retain its license when copying it. Do not silently download more fonts during a session.

The shared CSS stays below 12 KiB and the font below 40 KiB. No third-party JavaScript library,
framework, CDN, tracking script, image service, or animation service is bundled. The
learner-written page has a suggested 100 KiB budget before these assets. Keep code readable,
not minified. The Website preview panel reads the files directly; no build or server is needed.

## Presenter Check

Run `/create-website` in a fresh Codespace. Verify it asks only which website to make, then
builds immediately with the repository name, opens the preview, and hands over. Press + to add,
drag, and remove in each category; switch the calendar views; add a city on the Weather page.
Ask for a changed heading and verify the panel updates by itself with added entries kept.
Rename a Project Planner column and verify the board follows without losing saved cards.
Remove every entry and reload: each starter's examples must come back by themselves and
reproduce its `manual_check`. Check narrow and
desktop widths. Recorded observations must not be invented.
