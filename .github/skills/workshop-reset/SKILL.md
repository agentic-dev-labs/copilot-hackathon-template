---
name: workshop-reset
description: 'End a rehearsal run: turn what this session actually proved into skill and lab improvements, then clear the generated attendee output so the next run starts from the template. Use /workshop-reset after debugging the guided sites or working through labs.'
argument-hint: 'Finish a rehearsal run and reset the repository'
user-invocable: true
disable-model-invocation: true
---

# Workshop Reset

A facilitator tool for the end of a rehearsal run, not an attendee lab. It has two halves and
the order matters: **harvest what the run proved, then clear what it generated.** Resetting
first destroys the evidence, because the built page, the preview output and the failing command
are the proof. Never start at section 5.

Everything here is a proposal until the facilitator says yes. Apply nothing silently, and never
commit, push, or deploy.

## 1. Collect the Evidence While It Still Exists

Re-read this session, then look at what is actually on disk:

```bash
git status --porcelain
git --no-pager diff
```

Each candidate learning needs three things. Drop it if any are missing:

1. **The request in the learner's own words** ("make the progress bar much bigger").
2. **What actually happened**, not what was intended.
3. **Proof**: a rendered observation the facilitator reported, a command or test with its real
   message, or a file and line you have read. Never invent one, and never promote a plausible
   guess. If nothing proves it, it is not a learning.

Sort what you find into three lists and keep them apart:

- **Proved** — a command, test, or a person's observation settled it.
- **Observed but unexplained** — the symptom is real, the cause is not established yet. Say so.
- **To watch** — a hunch. These never become skill wording; they go in the hand-back as
  questions for the next run.

Say plainly what this run did **not** exercise. A path that never ran is untested, however
confident the code looks.

## 2. Decide Where Each Learning Belongs

| What the run exposed | Where it belongs |
| --- | --- |
| A page-building or design-kit trap that looks right in code and wrong on screen | `How the Pages Work` in [Create Website](../create-website/SKILL.md) |
| Interview, build-order, or hand-over wording | The matching numbered section of Create Website |
| Preview opening, reopening, or closing behaviour | [Start Website](../start-website/SKILL.md), [Stop Website](../stop-website/SKILL.md) |
| A lab step that is wrong, missing, or out of order | That lab's `README.md` under `labs/` |
| A missing or moved official link | [docs/REFERENCES.md](../../../docs/REFERENCES.md) and the lab that needs it |
| A rule every agent in this repository must follow | `AGENTS.md` and `.github/copilot-instructions.md`, in the fewest words that carry it |
| Clock times, lab length, or day structure | **Proposal only.** Write the case; the owner decides. |

Write the **class of problem and the check that catches it**, not the anecdote. "The bar was
288px wide" helps nobody; "kit wrappers are flex items, so check the parent's width before
trusting a child's `100%`" is reusable. One learning belongs in one place: repeating it in three
files means three files drift apart.

## 3. Propose, Then Apply

Show a short numbered list: the learning, its evidence, the file it would change, and the
wording in one line. Ask which to apply. Then make only those edits, keeping each file's
existing voice, line width, and heading style.

Guardrails that outrank any learning from a single run:

- Published clock times, day boundaries, and active lab durations stay unchanged without the
  owner's explicit approval.
- Fixtures, samples, and tests stay synthetic. A rehearsal observation is never a reason to add
  real vendor, patient, customer, or employee data.
- The design kit is capped at **12 KiB** by `tests/test_lab_contracts.py`, and the art has its
  own budget. Anything added to `workshop.css` has to be paid for in bytes, so prefer a rule in
  the page's own `<style>` or a sentence of guidance.
- No product documentation prose in synthetic reports or the privacy review template.
- Attendee days stay free of laptop installs, ports, and public deployment.
- Preserve the owner's in-progress work: if a file you want to edit already has staged or
  unstaged changes you did not make, say so and ask before touching it.

## 4. Validate Before Resetting

```bash
uv run pytest
uv run ruff check .
```

A change to the kit, a blueprint, or a lab is not finished until these pass.
`tests/test_lab_contracts.py` enforces the size budgets, the offline rules, and the shape of the
guided starters, so it fails on exactly the kind of well-meant addition a rehearsal produces. A
green suite still proves only that the repository is consistent, never that a live Codespaces or
deployment path works.

## 5. Clear the Generated Output

Stop the preview first, so nothing is holding a file that is about to disappear:

```bash
python3 scripts/website_preview.py stop
```

List what you are about to delete, wait for a yes, then delete it. If a run produced nothing,
say that the repository is already clean and skip this section rather than hunting for something
to remove.

| Safe to clear after confirmation | Never clear here |
| --- | --- |
| Everything in `site/` **except `README.md`**: `index.html`, `brief.md`, `data/`, `css/`, `js/`, `art/`, `fonts/`, `FONT-LICENSE.md`, `ideas/` | `site/README.md`, which explains the empty folder |
| `.playwright-mcp/`, `rehearsal/results/`, `travel/output/` | `.workshop-preview/`: the preview extension and its live `site.sock`, which is prepared Codespace machinery, not run output. Deleting it breaks `/create-website` until a facilitator re-prepares the Codespace. |
| Files this run generated that nobody has edited by hand | `research/` downloads, `reports/`, and `dist/`: ask first, they can represent hours of work or a build nobody wants repeated |
| | `.facilitator/`, `.env*`, and anything tracked that the facilitator changed |

Being listed in `.gitignore` proves a path is untracked, never that this run created it. Check
before deleting, for example with `stat -c '%y %n'`, and leave anything older than the session
alone unless the facilitator says otherwise.

**Never run `git reset --hard`, `git checkout .`, or `git clean -fdx`.** They cannot tell the
run's leftovers from the facilitator's own uncommitted work, and this skill exists to keep that
distinction. Delete named paths only.

Finish with `git status --porcelain` and confirm `site/` holds nothing but `README.md`, matching
what the template ships. Skill and lab improvements stay in the working tree for review; leave
them uncommitted unless asked.

## 6. Hand Back

Six short lines:

1. Learnings applied, and where.
2. Learnings deferred, and why.
3. Anything observed but unexplained, plus the questions to watch next run.
4. What this run did not exercise.
5. Test and lint result.
6. What was cleared, what was deliberately left, and that the skill edits are uncommitted.

Then stop. The next `/create-website` should start from the template with nothing left over.

Official references: [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
and the [customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).
