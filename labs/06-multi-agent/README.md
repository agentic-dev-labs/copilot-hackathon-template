# Lab 06: Build your own agents

**Objective:** Write a custom agent and a skill of your own, then hand work between agents without collisions.

**Time-box:** 90 minutes

**Prerequisites:** Completed Labs 01-03.

Until now you have used three agents somebody else wrote. This is the lab that matters on Monday
morning, because it is the one where you author your own.

## Part A: Write an agent (45 minutes)

A custom agent is one Markdown file with frontmatter. Four things define it, and they are the same
four things that define an automation: who it is, what it may touch, what it does, and where it
hands off.

1. Open `.github/agents/vendor-analyst.agent.md` and read the frontmatter before the prose.
2. Create `.github/agents/<your-agent>.agent.md`. A residency checker, a sub-processor auditor, a
   plain-English summariser for somebody who does not read SOC 2 reports - your choice.

   ```markdown
   ---
   name: residency-checker
   description: Checks whether a stated hosting region and data residency claim agree.
   tools:
     - read
     - search
   ---

   You check one thing only: whether hosting region and data residency contradict each other.

   Quote the exact sentence stating each. If either is absent, say so rather than inferring it.
   Return `region`, `residency`, `consistent` (true, false, or unknown) and `evidence`.
   ```

3. The `description` is not documentation. It is how Copilot decides when to reach for your agent,
   so write it as a trigger condition rather than a title.
4. `tools` is the scope control. Start with `read` and `search`. Do not grant `edit` unless the
   agent must write something - an agent that cannot edit cannot damage anything.
5. Select your agent in Copilot Chat and run it against
   `src/vendor_assurance/samples/synthetic_soc2_harborline_congress.md`.
6. Now make it fail on purpose. Run it against a sample where the fact is missing and confirm it
   says so instead of inventing an answer. An agent that never says "unknown" is not trustworthy.

### Turn a repeated instruction into a skill

When you find yourself pasting the same guidance into several agents, that guidance is a **skill**.
Create `.github/skills/<name>/SKILL.md` with a name and a description of when it applies, then let
your agents rely on it instead of repeating it. Skills load only when needed, so they cost nothing
until they are used.

## Part B: Hand off between agents (45 minutes)

1. Run the vendor analyst against `synthetic_soc2_meridian_outreach.md` and save its JSON. That
   sample scores 2 out of 10, so there is plenty for agents to disagree about.
2. Add a handoff to your own agent so it can pass work onwards:

   ```yaml
   handoffs:
     - label: Write privacy review
       agent: report-writer
       prompt: Render the analyst JSON into the privacy review template.
   ```

3. Give every agent its own output file. Never point two agents at one file - that is where merge
   conflicts come from, and partitioning is the real skill this lab is teaching.
4. Where two agents disagree, settle it against the direct quotation, never against the more
   confidently worded answer.
5. Hand the accepted JSON to the report writer, then the rendered report to the reviewer.
6. Run the CLI workflow and the tests, then check the final report for unfilled placeholders.

## What you just learned

A custom agent is a file, not a product feature. Because it is a file, it can be reviewed,
versioned and shared - repository first, then organization, then enterprise. Parallel agents help
only when the work is genuinely independent, and file ownership is what keeps it that way.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Share it upwards.** Ask the facilitator how the `vendor-analyst` agent reached your Codespace
   without you installing anything, then find that file in the organization's `.github-private`.
2. **Run subtasks in parallel.** In Copilot CLI, use `/fleet` to split a multi-step request into
   independent subtasks and watch them run at once.
3. **Build the strictest agent you can.** Give one agent no tools at all and see what it can still
   usefully do. This is the fastest way to understand what `tools` really controls.
4. **Write the schema checker.** A fourth agent that validates only the shape of the analyst's JSON
   and owns no file any other agent touches.

