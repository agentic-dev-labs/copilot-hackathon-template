# Neutral Website Kit

Original workshop CSS and fictional briefs, not a finished learner website or a corporate
design system. No Novo name, logo, proprietary imagery, corporate stylesheet, or corporate
font is included. The skill copies only the reusable dependencies after the learner approves
their small plan; it generates their own HTML and JavaScript.

## File Contract

| Kit file | Learner destination | Purpose |
| --- | --- | --- |
| [css/workshop.css](css/workshop.css) | `site/css/workshop.css` | Shared layout, controls, themes, responsive rules |
| [fonts/source-sans-3-latin.woff2](fonts/source-sans-3-latin.woff2) | `site/fonts/source-sans-3-latin.woff2` | Local, open-source variable font, Latin subset (28,740 bytes) |
| [fonts/OFL.txt](fonts/OFL.txt) | `site/FONT-LICENSE.md` | Retained font license; Markdown is not published by the static app |
| Selected SVG from `icons/` | `site/assets/` | Optional calendar, checklist, or wallet for a fictional project mark |
| [icons/LICENSE](icons/LICENSE) | `site/ICON-LICENSE.md` | Retained icon license when a symbol is used |
| [starters.json](starters.json) | Selected values in the learner's page/brief | Synthetic data and independently checkable figures |

The CSS expects its font at `../fonts/source-sans-3-latin.woff2`. It makes no external requests.
Load it before personal `styles.css`. All palettes default to light: Fresh mint (`green`),
Sky blue (`blue`), or Soft coral (`coral`). Use the matching body `data-theme` value; the editor's
dark theme does not change the website. Preserve dark readable text and restrained accent colors.
Keep content sections unframed; `.card` is for individual repeated items, not nested page sections.

The font is [Source Sans 3 from Google Fonts](https://github.com/google/fonts/tree/main/ofl/sourcesans3),
downloaded unchanged on 2026-09-22 as [the official Latin WOFF2 subset](https://fonts.gstatic.com/s/sourcesans3/v19/nwpStKy2OAdR1K-IwhWudF-R3w8aZQ.woff2)
and distributed under the included SIL Open Font License. SHA-256:
`7a19a7027e125257d310c6dbd78ae3a30b5ea1e3794d60b12bb28227a003bfda`.
The variable file supports weights 200-900; characters outside its Latin coverage use the
browser's local sans-serif fallback. Do not silently download more fonts during a learner session.
It is not a customer font or logo. Retain its license when copying it. No frontend framework,
CDN, tracking script, image service, or runtime download is needed.

The shared CSS stays below 12 KiB; the font stays below 40 KiB; the three icons together stay
below 4 KiB. No JavaScript library is bundled. The learner's first HTML/CSS/JavaScript version
has a suggested 100 KiB budget before these assets. Keep the code readable, not minified.
Live Preview serves the files directly: no compilation, service worker, or cache-busting pipeline.

Design references are [Fluent 2](https://fluent2.microsoft.design/) for clear, accessible product
interfaces and [Primer](https://primer.style/) for restrained controls and consistent spacing.
The kit is original CSS, not an implementation or install of either library.
[Material 3](https://m3.material.io/) remains a design system; its separate
[Material Web package](https://github.com/material-components/material-web) reports maintenance
mode. None of these packages is needed for a polished starter.

The unmodified [calendar](icons/calendar-days.svg), [checklist](icons/clipboard-check.svg), and
[wallet](icons/wallet.svg) are from [Lucide](https://github.com/lucide-icons/lucide/tree/main/icons),
downloaded on 2026-09-22 with the included ISC/MIT notices. Retain the complete license.
These are generic symbols, not exclusive or trademark-cleared logo designs. A name-only logo
or CSS initials needs no symbol. Use only fictional project identities, never Novo branding.

## Presenter Check

Run `/create-website` in a fresh Codespace. Verify it asks a single starter question and waits,
then asks for a title, audience, logo, colors, and category-specific features, requests approval,
and creates only the agreed learner files. "Not sure" should get a recommended default.
Open the generated page with Live Preview, save a changed heading, and verify the embedded
page updates. Check all three themes at narrow and desktop widths. The corresponding manual
totals in the fixture must be reproducible; recorded observations must not be invented.

Test existing work, a missing slash command, a blocked embedded preview, and an own-idea request.
Check that the first website is preserved. Unit tests validate file contracts, not actual skill
discovery, question-tool behavior, extension activation, or GitHub preview authentication.