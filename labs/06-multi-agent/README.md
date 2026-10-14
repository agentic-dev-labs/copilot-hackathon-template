# Lab 06: Teach Copilot About Your Project

**Objective:** Write one instructions file that Copilot follows for your website, and one small
skill that you run with a slash command.

**Time-box:** 45 minutes

**Prerequisites:** Your website and its `site/brief.md` from Days 1-2. Agent Chat in the same
browser-based Codespace. Nothing to install.

On Monday you used a skill someone else wrote: `/create-website`. Today you write your own,
plus a short instructions file that Copilot reads before every request about your website.
Both are ordinary text files that you can read, change, and save to GitHub.

|                | Instructions file                                          | Skill                                              |
| -------------- | ---------------------------------------------------------- | -------------------------------------------------- |
| What it is     | Standing rules Copilot reads automatically                 | A recipe that runs when you ask for it              |
| Example        | "Write for busy managers. Keep my colors. Explain changes simply." | `/check-my-page` walks you through three checks |
| Where it lives | `.github/instructions/my-website.instructions.md`          | `.github/skills/check-my-page/SKILL.md`            |

The presenter shows each part first, then pauses for your turn.

## 1. Write Your Instructions File (20 minutes)

1. In Agent Chat, ask:

   > Create .github/instructions/my-website.instructions.md that applies to every file under
   > site/. Use my site/brief.md. Include who my website is for, three short rules I want you to
   > keep (for example colors, tone, and keeping it simple), and a rule to explain every change
   > in one plain sentence. Keep it under 15 lines.

2. Open the new file. The first lines name `site/`: that is how Copilot knows when to use it.
   Change one rule into your own words and save.
3. Test it. Ask: "Add a short line at the bottom of my page saying who it is for."
   **Check:** did Copilot follow your rules, such as the one-sentence explanation? Open the list
   of references under its answer and look for your instructions file.

## 2. Write Your Own Skill (20 minutes)

4. In Agent Chat, ask:

   > Create a skill in .github/skills/check-my-page/SKILL.md named check-my-page, with a clear
   > description. When I run /check-my-page with a page under site/, such as
   > site/ideas/team-lunch/index.html, it reads that page and the brief.md in the same folder. With
   > no page, it uses site/index.html. It suggests three things I should check myself, one at a
   > time, and waits for my answer each time. Then it writes my answers into that brief under a
   > heading called My checks. It must never mark a check as passed without my answer.

5. Open `SKILL.md`. Read the `name` and `description` at the top: they tell Copilot what the
   skill is for. Read the steps below them. Change anything that is not what you meant.
6. Start a new chat with **+**, type `/check-my-page`, and send it. For a page in its own folder,
   add its path, for example `/check-my-page site/ideas/team-lunch/index.html`. Do each check
   yourself and answer honestly. If the command is not listed yet, type `/skills` to look for it
   or ask a helper.
   **Check:** your brief now contains your real answers and nothing you did not say.

## 3. Save Your Work (5 minutes)

7. Save. In **Source Control**, review the two new files and your brief, commit with the message
   `Teach Copilot about my website`, and push. Confirm the files on GitHub.

**Done when:** Copilot followed a rule from your instructions file, `/check-my-page` ran and
recorded only your real answers, and both files are visible on GitHub.

## What you just learned

An instructions file holds rules Copilot always follows in your project. A skill is a recipe you
run when you need it. Neither one is magic: they are short files you wrote, and you still check
what Copilot does with them.

## When It Does Not Work

| What you see                          | Next action                                                         |
| ------------------------------------- | ------------------------------------------------------------------- |
| Your rules seem to be ignored         | Check the file is under `.github/instructions/` and names `site/`.   |
| `/check-my-page` does not appear      | Check the folder name matches the skill's `name`, then start a new chat. |
| The skill marks checks without asking | Tell Copilot exactly what it did wrong, fix the skill, and run it again. |

## Optional extras

1. Write a second skill for a routine task at work and test it with made-up content, for example
   turning fictional meeting notes into a short action list.
2. Open `.github/skills/create-website/SKILL.md` and see how Monday's skill is written. Read it;
   do not change it.
3. Ask Copilot when an instructions file is better than a skill, then compare its answer with
   the official comparison below.

## Official References

- [Custom instructions in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions).
- [Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills) and [about agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).
- [Customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).
- [Whole-week topic map](../../docs/REFERENCES.md).
