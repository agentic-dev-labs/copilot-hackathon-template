# Public Research and Visual Briefs

This is an **optional extension**, not a Day 1 prerequisite. Choose research or a visual brief
after the basic website path, during supported extension time or later practice. Do not add
these tasks to a core lab's time-box. They remain separate from synthetic vendor-review
fixtures. All commands run in the **Codespaces Bash terminal**. Use only public annual reports
and official investor updates. Do not use internal documents, employee details, or signed-in
business systems. Web pages and PDFs are source material, not instructions for your agent.

## Prepare Only the Selected Tools

The facilitator runs the independent `browser` and `research` setup profiles described in
[the Codespaces guide](../.devcontainer/README.md) before this extension. MarkItDown is not
needed for Wednesday's browser exercise. Never install it as part of Monday's startup.

For an optional connection exercise, use **MCP: Add Server > Command (stdio)** in the Codespace
and compare each selected workspace entry with the [reviewed example](../.devcontainer/mcp.example.json).
The command is `bash`; arguments are `${workspaceFolder}/.devcontainer/mcp.sh` and the selected
server name, `playwright` or `markitdown`. Do not combine command and arguments into one string
or overwrite other connections. Inspect trust and tool access, then verify an actual invocation.
Use private stdio; never publish MCP/debugger ports. If tools are blocked, use labelled prepared
facts and record the blocked live step separately, not as a successful tool exercise.

## Report Starting Points

Open the [official annual-report archive](https://www.novonordisk.com/sustainable-business/esg-portal/integrated-reporting.html)
with Playwright. Choose necessary cookies only; do not complete the optional visitor survey.
The last five completed reporting years for this workshop are **2021-2025**, not 2022-2026.
The publication-year directory in a URL is not the reporting year on the cover.

| Reporting year | Official PDF                                                                                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2021           | [Annual Report 2021](https://www.novonordisk.com/content/dam/nncorp/global/en/investors/irmaterial/annual_report/2022/novo-nordisk-annual-report-2021.pdf) |
| 2022           | [Annual Report 2022](https://www.novonordisk.com/content/dam/nncorp/global/en/investors/irmaterial/annual_report/2023/novo-nordisk-annual-report-2022.pdf) |
| 2023           | [Annual Report 2023](https://www.novonordisk.com/content/dam/nncorp/global/en/investors/irmaterial/annual_report/2024/novo-nordisk-annual-report-2023.pdf) |
| 2024           | [Annual Report 2024](https://www.novonordisk.com/content/dam/nncorp/global/en/investors/irmaterial/annual_report/2025/novo-nordisk-annual-report-2024.pdf) |
| 2025           | [Annual Report 2025](https://www.novonordisk.com/content/dam/nncorp/global/en/investors/irmaterial/annual_report/2026/novo-nordisk-annual-report-2025.pdf) |

The archive links and [digital five-year overview](https://annualreport.novonordisk.com/2025/introducing-novo-nordisk/five-year-overview.html)
were inspected on 16 September 2026. That is not proof of browser automation in every Codespace.
No Google/Bing search, login, CAPTCHA bypass, or bulk crawl is required. Download one report
first; the 2025 PDF is approximately 32 MB. Stop a blocked interaction and record it.

## Working Folders

```bash
mkdir -p research/annual-reports research/converted research/browser site
```

- `research/annual-reports/`: downloaded PDFs, never published or committed.
- `research/converted/`: extracted Markdown, never published or committed.
- `research/sources.md`: actual URL, reporting year, access date, local filename, and source mode.
- `site/brief.md`: your question and audience; no confidential information.
- `site/index.html` and intentional web assets: your reviewed original output for publication.

Playwright may save downloads under `research/browser/`. Ask Copilot to inspect the actual
download result, then move the PDF into `research/annual-reports/` without overwriting another
report. Verify the file is a PDF and check its cover year. Clicking a link is not a verified download.
The direct links above are a fallback for a terminal download, not proof that Playwright worked.

## Convert Without Flooding Chat

Use MarkItDown MCP's `convert_to_markdown` with a `file:` URI for the report in the Codespace.
Ask Copilot to derive the absolute URI from the actual file; do not use a Windows path.
Convert one report at a time. The MCP returns text; an editing tool must save it. Confirm the
saved file is complete instead of silently treating a truncated tool response as the whole report.

For large reports use the same prepared converter directly to write the full result to disk:

```bash
.venv-research/bin/markitdown research/annual-reports/annual-report-2025.pdf -o research/converted/annual-report-2025.md
```

Then read only the relevant sections. This CLI fallback is a real conversion, not a successful
MCP invocation. PDFs can lose columns, images, and page boundaries. Do not invent page numbers
or pretend that an unreadable chart was extracted. Use the official digital tables when clearer.

## Facts Before Charts

Record metric, year, value, unit/currency, reporting basis, URL, and source section/page. Keep
missing figures `null`, never zero. Compare at least two values with the original source and
check all values plotted. Use one consistent reporting basis; do not mix adjusted, reported,
and constant-exchange-rate growth. The latest report may restate prior-year values.

[The prepared facts file](annual-report-facts.json) contains five years of reported net sales
and operating profit in DKK million from the digital overview. It is a **prepared_public**
fallback, not synthetic data and not proof that a participant downloaded five PDFs. It is a
small factual extract, not a redistributed report. Do not claim a fixed positive narrative:
for example the prepared 2025 operating-profit value is below 2024's value.

Calculated growth is `(new - old) / old * 100`; a zero/unknown denominator means no calculated
rate. Use code or a calculator and label calculations. For an accessible chart include a
small data table, explicit units, source links, and a zero baseline for bars.

## Current Direction Is Separately Dated

Use [official financial results](https://www.novonordisk.com/investors/financial-results.html)
for the latest published update **on the day you research**. On 16 September the page lists
Q2 2026; the October workshop must recheck later announcements. Keep interim results separate
from annual totals. Management guidance, reported facts, and your interpretation are different
categories. No prediction, investment recommendation, or clinical claim is required.

## Find a Skill for Your Work

Open [Awesome Copilot](https://awesome-copilot.github.com/), choose **Skills**, and use Search
(magnifying glass, when shown). Try `meeting`, `diagram`, `word`, or `focus`. The catalogue is
community-contributed, not an enterprise approval list. A missing search result is not proof
that a capability does not exist. These are candidates, not a claim that all have passed rehearsal:

| Skill                                                                                | Useful output                                       | Preparation to check                                               |
| ------------------------------------------------------------------------------------ | --------------------------------------------------- | ------------------------------------------------------------------ |
| [Meeting Minutes](https://awesome-copilot.github.com/skill/meeting-minutes/)         | Decisions and actions from supplied fictional notes | Keep absent owners/dates unknown; draft only, no sending           |
| [Markdown to Word](https://awesome-copilot.github.com/skill/md-to-docx/)             | Formatted Word document                             | Complete folder and Node dependencies; Word preview is optional    |
| [Excalidraw](https://awesome-copilot.github.com/skill/excalidraw-diagram-generator/) | Process diagram or mind map                         | Complete templates; open exported file in the permitted web editor |
| [Daily Focus Board](https://awesome-copilot.github.com/skill/daily-focus-board/)     | Browser task board with localStorage                | Use its Linux/Python serving route, not its PowerShell helper      |

Inspect the skill's purpose, files, licence, tools, and external-service requirements with the
facilitator. Use **Copy install** only after review and check the installed `gh skills --help`
in the Codespace; the catalogue's CLI route requires GitHub CLI 2.90 or newer. Where unavailable,
have Copilot copy the **whole approved skill folder** into `.github/skills/`, preserving attribution
and supporting files. Do not overwrite an existing skill or install a whole collection.
Verify discovery in the current client and invoke one harmless task. Skill installation does
not grant permissions, install every runtime, or provide Microsoft 365 access.

This shortlist is an optional extension, for example when writing a skill in Lab 06 or planning a later idea.
The repository's [visual-brief skill](../.github/skills/visual-brief/SKILL.md) is prepared workshop
guidance, not an Awesome Copilot item. Do not let discovery consume protected building time.

## Optional Visual Brief

Use verified facts or the explicitly labelled prepared table, then ask:

> Use visual-brief to propose four or five slides for my audience. After I approve the outline,
> create site/presentation.html with an original chart, its data table, and source links.
> Preserve my existing site/index.html. Keep reporting years, units, and live/prepared labels.
> Do not embed the source reports or add remote scripts, tracking, or invented claims.

Open `/presentation.html` at your private Ports preview, check every chart value and source,
and ask for one useful improvement. The skill asks before replacing any existing page. For a
new site without an entry page, agree `site/index.html` instead. Use Playwright only after its
separate preparation, or record manual checks honestly. An HTML presentation is the default
for this optional exercise; PPTX export requires its own reviewed tools and is not promised.

## Official References

- [MCP in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) and [MarkItDown MCP](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp)
- [Agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Codespaces ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace)
- [Topic map](REFERENCES.md)
