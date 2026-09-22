# Everyday AI With GitHub Copilot

Describe an idea, build something small with AI, check it yourself, and learn how to improve it.
Days 1-2 start from no GitHub or app-building experience. Days 3-5 add technical depth for
low-coders and pro-coders. Every activity follows **show -> try -> personalise -> verify -> share**.

**Day 1:** understand the workspace, use Chat, build your first website, manually check a
feature and a figure, and save your work in GitHub. Use the guided `/create-website` starter
menu; the presenter demonstrates the fictional weekend planner. **Day 2:** David and Jackie explain the business/IT model and
shared-data possibilities; you build your own idea with fictional content and table-side help.
**Days 3-5:** use CLI and MCP/Playwright, delegate work, make checks repeatable, deploy, author
skills, and evaluate results. No Dataverse integration is required for the workshop.

All attendee work uses **browser-based GitHub Codespaces and its Linux terminal**. Nothing
needs installing on your laptop. See the [agenda](docs/AGENDA.md) and
[topic map and official references](docs/REFERENCES.md).

## Start here

1. Join the first concepts-only block with the [glossary and labelled screenshots](docs/START-HERE.md).
2. Open the repository assigned by the facilitator, then follow [Lab 00](labs/00-setup/README.md).
3. Follow [today's chronological route](docs/START-HERE.md#todays-route), one step at a time.

You start with files and Chat, not commands or configuration. In Lab 01, `/create-website`
guides you through a weekend, project, or budget planner. Microsoft Live Preview opens your
page inside the same Codespaces window and refreshes after saved edits. Copilot CLI is installed
from creation but introduced on Day 3; browser automation is prepared separately for that track.
optional research tools do not block Monday's workspace. The facilitator assigns your label and access.

Open `site/index.html`, then **Live Preview: Show Preview (Internal Browser)** from the Command
Palette. If authentication blocks it, open the private forwarded links once through Ports and
retry. See [Lab 01](labs/01-vscode-agent/README.md) for the fallback. A private preview is
enough for Monday; public deployment is not part of the guided skill.

The prepared commands keep the same website: **`/create-website`** asks the questions, builds
after approval, and opens the first preview; **`/start-website`** reopens it;
**`/stop-website`** stops preview without deleting files. Where Chat cannot run editor commands,
the skill gives the single matching UI action instead. Continue colors, layout, and features
in normal Chat using [Lab 02's category-specific examples](labs/02-copilot-cli/README.md).
The frontend is build-free HTML/CSS/JavaScript with light palettes, local assets, and no CDN.

## What This Repository Provides

- A prepared environment and lab guidance, not a completed learner website.
- A [guided creation skill](.github/skills/create-website/SKILL.md) with neutral styling and three fictional starter briefs; no learner installation or skill authoring.
- Plain-language choices for audience, fictional logo, colors, and useful features before building; no paid image service or diagram tool.
- Eight active labs, a [supported Tuesday build](docs/DAY-2-BUILD.md), official references, tests, and a [rehearsal package](rehearsal/README.md).
- A [printable quick reference](docs/QUICK-REFERENCE.md) for the live demonstrations.
- A synthetic vendor reader for the technical track; it runs without Dataverse credentials.
- [Post-workshop Dataverse setup knowledge and prompts](post-workshop/dataverse/README.md), retained for the later technical-owner session.
- [Optional public research and visual briefs](docs/RESEARCH.md), not Monday prerequisites.
- [Optional travel practice](travel/README.md) for later agent/skill exploration.

[Awesome Copilot](https://awesome-copilot.github.com/) skill discovery is part of Day 5 and
available as an extension. The collection is not an enterprise approval policy; complete
folders, dependencies, and permissions need review before use.

## Rehearse the Complete Workshop

In a dedicated Codespaces rehearsal copy, run **`/rehearse-workshop`** in Copilot's local Agent
mode, or **`/workshop-rehearsal`** through the companion skill in Agent Host. The
[rehearsal package](rehearsal/README.md) drives the eight active labs and own-idea build, diagnoses fresh
package installs, runs tests, tracks live evidence, and retrieves verified deployment endpoints.
Attendees do not sign into Azure: the existing Actions workflow uses the prepared deployment identity.
Missing access or required human review stays a blocker, not a simulated pass.

## Technical Reference: Run the Vendor Example

This is the separate Days 3-5 example, not the beginner website. Its prepared label is facilitator work.

```shell
uv sync --locked --extra dev --extra web
uv run uvicorn app.main:app --reload
```

With no Dataverse configured the app evaluates the synthetic samples directly, so it works in a
fresh Codespace with no credentials.

The devcontainer uses the checked-in `uv.lock`. Run `uv run pytest` and `uv run ruff check .`
from the repository root to check your work. Prepared headless Playwright MCP and MarkItDown MCP
run privately inside Codespaces. Built-in desktop browser tools are not an attendee prerequisite.

## Deploy it

For supported publication, run **Deploy my app** from Actions. Select **website** for your
page and **vendor** for the separate business app. The workflow uses the prepared Actions identity; no attendee Azure login is needed.
The run summary prints the verified URL and commit. Follow [Lab 08](labs/08-deploy/README.md)
before publishing. Only the intended site assets are published, not source reports or notes.

If you chose remembering as an extension, `localStorage` belongs to one browser context and
origin. Your preview, deployed site, and Playwright browser have separate data. Repeat your
actual checks at a new URL. Browser storage is not a shared team database.

Vendor writes are disabled by default. The preserved post-workshop reference explains the private
training switch and production gaps. It is not authentication and must never be enabled on the
public deployment. Beginner work does not need this form or service credentials.

## Labs

Lab numbers group topics; the **Day** column is the order of the week.

| Lab                                       | Topic                                                         | Day |
| ----------------------------------------- | ------------------------------------------------------------- | --- |
| [00](labs/00-setup/README.md)             | Find your files and Copilot Chat                              | 1   |
| [01](labs/01-vscode-agent/README.md)      | Build your first page; manually verify behaviour and a figure | 1   |
| [02](labs/02-copilot-cli/README.md)       | One useful interaction and your own improvements              | 1   |
| [08](labs/08-deploy/README.md)            | Save, share, keep building; optional publication              | 1   |
| [Own-idea build](docs/DAY-2-BUILD.md)     | Supported prototype building with fictional local data | 2 |
| [03](labs/03-cloud-agent/README.md)       | Copilot cloud agent                                           | 3   |
| [04](labs/04-mcp/README.md)               | Remote GitHub MCP server                                      | 3   |
| [07](labs/07-automations-hooks/README.md) | Automations and hooks                                         | 4   |
| [06](labs/06-multi-agent/README.md)       | Deeper agent/skill authoring and evidence handoffs            | 5   |

See the [prerequisites](docs/PREREQS.md), [agenda](docs/AGENDA.md), and [facilitator runbook](docs/FACILITATOR.md).

Every lab ends with official references and optional tasks. Use the
[daily early-finisher list](docs/REFERENCES.md#small-tasks-for-early-finishers) while the group catches up.
The former Lab 05 link is retained as a signpost, not a ninth scheduled lab. Technical setup,
data integration, and an approved real-work reference project live in the post-workshop folder.

## Sample reports

Three synthetic vendor reports are provided so you can compare outcomes from the same
checklist. All are fabricated and describe no real organization.

| Sample                                  | Outcome                                                    |
| --------------------------------------- | ---------------------------------------------------------- |
| `synthetic_soc2_harborline_congress.md` | Strong report, scores 10/10                                |
| `synthetic_soc2_report.md`              | Mixed report, 8/10 with one failure and one unclear result |
| `synthetic_soc2_meridian_outreach.md`   | Weak report, scores 2/10 despite strong encryption         |

They live in `src/vendor_assurance/samples/`. These outcomes use review date **2026-10-26**;
date-sensitive results change as reports age. Use a fixed date for repeatable demonstrations:

```bash
vendor-assurance src/vendor_assurance/samples/synthetic_soc2_report.md --as-of 2026-10-26 --output-directory reports/
```

The CLI writes JSON to stdout and the output path to stderr. Scores come from deterministic
Python, not the model. Evidence remains source text; the report renderer encodes table characters.

## Training scope

The evaluator recognizes ten controls in the supplied UTF-8 Markdown/text format using simple
rules. It is not a general SOC 2 assessor, an OCR pipeline, or a production compliance opinion.
Chunking uses whitespace-delimited words, not a model tokenizer; it helps demonstrate bounded
processing but does not guarantee complete evidence at every chunk size. Use synthetic data only.

The vendor starter reads synthetic samples without service access and retains a separately
documented opt-in private training form. Technical attendees author customizations in Labs 06
and 07; beginners do not configure data connections. Optional public research
is an explicit exception to the synthetic-only business fixtures: download into ignored
`research/`, verify facts, and publish original summaries only.
Never mix annual-report content into the vendor evaluator or confidential material into the lab.
Local tests do not prove live Codespaces, MCP, deployment, or Dataverse availability. Rehearse
the actual learner journey and keep prepared results visibly distinct from live observations.

## Official References

- [Copilot features](https://docs.github.com/en/copilot/get-started/features): the overall capability map.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): branch, commit, PR, review, and merge.
- [VS Code agents](https://code.visualstudio.com/docs/agents/overview): how context, models, tools, and sessions work together.
- [Workshop coverage and references](docs/REFERENCES.md): topic-by-topic official links, later-day practice, and optional extensions.
