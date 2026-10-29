# Advanced Reference: The Synthetic Vendor Reader

> **Post-workshop reference, not a workshop lab.** On 14 October 2026 the owner simplified
> Days 3-5 for first-time users, so this material left the schedule. Use it later with a
> technical owner; it does not change the [current agenda](../../AGENDA.md). See
> [the advanced index](README.md).

This separate business example reviews **synthetic** vendor reports. It is not the beginner
website. Scores come from deterministic Python in `src/vendor_assurance/evaluator.py`, never from
a model's opinion, and every finding quotes its source.

## Run It

```shell
uv sync --locked --extra dev --extra web
uv run uvicorn app.main:app --reload
```

With no Dataverse configured, the app evaluates the synthetic samples directly, so it works in a
fresh Codespace with no credentials. The devcontainer uses the checked-in `uv.lock`. Run
`uv run pytest` and `uv run ruff check .` from the repository root to check your work.

## Sample Reports

Three synthetic vendor reports compare outcomes from the same checklist. All are fabricated and
describe no real organization. They live in `src/vendor_assurance/samples/`.

| Sample                                  | Outcome                                                    |
| --------------------------------------- | ---------------------------------------------------------- |
| `synthetic_soc2_harborline_congress.md` | Strong report, scores 10/10                                |
| `synthetic_soc2_report.md`              | Mixed report, 8/10 with one failure and one unclear result |
| `synthetic_soc2_meridian_outreach.md`   | Weak report, scores 2/10 despite strong encryption         |

These outcomes use review date **2026-10-26**; date-sensitive results change as reports age.
Use a fixed date for repeatable demonstrations:

```bash
vendor-assurance src/vendor_assurance/samples/synthetic_soc2_report.md --as-of 2026-10-26 --output-directory reports/
```

The CLI writes JSON to stdout and the output path to stderr. Evidence remains source text; the
report renderer encodes table characters.

## Publishing the Vendor App

**Actions > Deploy my app** has a separate **vendor** target, using the prepared Actions
identity; no attendee Azure login is needed. The run summary prints the verified URL and commit.
Vendor writes are disabled by default. The [Dataverse reference](../dataverse/README.md) explains
the private training switch and production gaps. That switch is not authentication and must never
be enabled on a public deployment. Keep the website and vendor targets separate.

## Training Scope

The evaluator recognizes ten controls in the supplied UTF-8 Markdown/text format using simple
rules. It is not a general SOC 2 assessor, an OCR pipeline, or a production compliance opinion.
Chunking uses whitespace-delimited words, not a model tokenizer; it helps demonstrate bounded
processing but does not guarantee complete evidence at every chunk size. Use synthetic data only.

Optional public research is an explicit exception to the synthetic-only business fixtures:
download into ignored `research/`, verify facts, and publish original summaries only. Never mix
annual-report content into the vendor evaluator or confidential material into the lab. Local
tests do not prove live Codespaces, MCP, deployment, or Dataverse availability.

## Official References

- [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart).
- [Container Apps with GitHub Actions](https://learn.microsoft.com/azure/container-apps/github-actions).
- [Whole-week topic map](../../REFERENCES.md).
