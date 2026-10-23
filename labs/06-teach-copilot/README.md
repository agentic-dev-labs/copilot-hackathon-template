# Lab 06: Teach Copilot About Your Project

**Objective:** Write one instructions file that Copilot follows for your website, write your own
`/make-image` skill that draws pictures for your page, and try a ready-made `/add-chat` skill.

**Time-box:** 45 minutes, as an **optional extra** for Day 3 or later. The scheduled Day 3 is
the [Requirements agent day](../../docs/TOOLS-PRACTICE.md).

**Prerequisites:** Your website and its `site/brief.md` from Days 1-2. Agent Chat in the same
browser-based Codespace. Nothing to install.

On Monday you used a skill someone else wrote: `/create-website`. Today you write your own, plus a
short instructions file that Copilot reads before every request about your website. Both are
ordinary text files that you can read, change, and save to GitHub.

|                | Instructions file                                          | Skill                                                |
| -------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| What it is     | Standing rules Copilot reads automatically                 | A recipe that runs when you ask for it                |
| Example        | "Write for busy managers. Keep my colors. Explain changes simply." | `/make-image a friendly rocket` draws a picture for your page |
| Where it lives | `.github/instructions/my-website.instructions.md`          | `.github/skills/make-image/SKILL.md`                 |

The presenter shows each part first, then pauses for your turn.

## 1. Write Your Instructions File (15 minutes)

1. In Agent Chat, ask:

   > Create .github/instructions/my-website.instructions.md that applies to every file under
   > site/. Use my site/brief.md. Include who my website is for, three short rules I want you to
   > keep (for example colors, tone, and keeping it simple), and a rule to explain every change
   > in one plain sentence. Keep it under 15 lines.

2. Open the new file. The first lines name `site/`: that is how Copilot knows when to use it.
   Change one rule into your own words and save.
3. Test it. Ask: "Add a short line at the bottom of my page saying who it is for."
   **Check:** did Copilot follow your rules, such as the one-sentence explanation?

## 2. Write Your Own Picture Skill (20 minutes)

Your Codespace can draw pictures with the workshop's AI picture models. A small helper does the
drawing; your skill is the recipe that tells Copilot when and how to use it.

4. In Agent Chat, ask:

   > Create a skill called make-image in .github/skills/make-image/SKILL.md. When I type
   > /make-image and describe a picture, run python3 scripts/workshop_ai.py image "my description",
   > put the new picture in my page (in the header if I do not say where), and ask me to check it.
   > Only friendly, made-up pictures: no real people, logos, or words in the picture.

5. Open `SKILL.md`. Read the `name` and `description` at the top: they tell Copilot what the skill
   is for. Read the steps below them and change anything that is not what you meant.
6. Start a new chat with **+**, type `/make-image a friendly rocket for my header`, and send it.
   For a page in its own folder, add where it goes, for example
   `/make-image a picnic table for my team-lunch page`.
   **Check:** a new picture file appears in **site > art**, and your page shows it in the preview.
   Do not like it? Run `/make-image` again with different words, or select **Undo** in Chat.

## 3. Try a Ready-Made Skill: Add a Chat (5 minutes)

7. Type `/add-chat` and send it. An **Ask** button appears at the bottom right of your page.
8. Select **Ask** and ask: "What is on this page?"
   **Check:** compare the answer with your page. The assistant reads only what your page shows,
   and it can be wrong, so you check.

## 4. Save Your Work (5 minutes)

9. Save. In **Source Control**, review the new files, commit with the message
   `Teach Copilot about my website`, and push. Confirm the files on GitHub.

**Done when:** Copilot followed a rule from your instructions file, your own `/make-image` skill put
a new picture on your page, you checked one answer from the chat, and your files are on GitHub.

## What you just learned

An instructions file holds rules Copilot always follows in your project. A skill is a recipe you
run when you need it, and it can use tools, such as the picture helper. Neither one is magic: they
are short files you wrote, and you still check what Copilot does with them.

## When It Does Not Work

| What you see                                 | Next action                                                              |
| -------------------------------------------- | ------------------------------------------------------------------------ |
| Your rules seem to be ignored                | Check the file is under `.github/instructions/` and names `site/`.       |
| `/make-image` does not appear                | Check the folder name matches the skill's `name`, then start a new chat. |
| "Busy"                                       | Wait a minute and try again.                                             |
| "Not switched on" (pictures or chat)         | Show a helper: your Codespace may need a restart.                        |

## Optional extras

1. **Change a picture:** write a second skill, `/edit-image`, that runs
   `python3 scripts/workshop_ai.py edit` on the picture I describe, with my change, and shows the
   new version. Try `/edit-image make my header picture a night scene`. The old picture stays, so
   you can always go back.
2. Write a skill for a routine task at work and test it with made-up content, for example turning
   fictional meeting notes into a short action list.
3. Open `.github/skills/add-chat/SKILL.md` and see how a ready-made skill is written. Read it; do
   not change it.

## Official References

- [Custom instructions in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions).
- [Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills) and [about agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).
- [Customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).
