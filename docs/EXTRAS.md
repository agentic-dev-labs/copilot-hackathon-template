# Optional Extras

Two extras for Day 3 or later, when you finish early. Neither is needed to complete a day. The
presenter shows each part first. Everything stays made up, and nothing is installed on your laptop.

| Extra                                                              | Time       | What you do                                                    |
| ------------------------------------------------------------------ | ---------- | -------------------------------------------------------------- |
| [1. Copilot uses tools (MCP)](#1-copilot-uses-tools-mcp)           | 45 minutes | Plug in GitHub tools, check what they report, watch a browser tool. |
| [2. Teach Copilot about your project](#2-teach-copilot-about-your-project) | 45 minutes | Write an instructions file and your own `/make-image` skill, and try `/add-chat`. |

## 1. Copilot Uses Tools (MCP)

**An optional extra, 45 minutes.** You need your website from Days 1-2 and Agent Chat, in the
same browser-based Codespace.

**MCP** is a standard plug for tools. With a tool, Copilot can do something it cannot do by
talking alone, such as looking things up on GitHub or clicking through a web page. You choose
which tools to plug in, and you still check what they report.

### Plug In GitHub (25 minutes)

This project comes with its own short list of tools, so you do not have to find or type anything.

1. In the **Explorer**, open the **.vscode** folder and select **mcp.json**. It lists one tool
   server, `github`, at `https://api.githubcopilot.com/mcp/readonly`. `readonly` means Copilot
   can look at your repository but cannot change anything on GitHub.
2. Select **Start**, the small link just above `"github"`. If VS Code asks you to sign in to
   GitHub or to allow access, choose **Allow**. If sign-in is blocked, show a helper and follow
   the presenter's screen instead.
3. In Chat choose **Agent**, then ask:

   > Use the GitHub tools to list the last three commits in my repository. For each one, tell me
   > its message and which files it changed. Do not change anything.

   If Copilot asks to use a tool, read the tool's name and allow it.
   **Check:** open your repository on GitHub in another tab and select **Commits**. Do the
   messages and files match what Copilot said?

### Watch Copilot Use a Browser (20 minutes)

Tools can also click through a web page. The presenter shows this on their own screen with
VS Code's browser tools, so you have nothing to set up.

1. Watch the presenter ask Copilot to open a page, read its title, add an item, and report the
   new count.
2. Do the same check by hand on your own page: open it with `/start-website`, read the title,
   add one made-up item, and count.
3. Compare. Did Copilot's report match what the presenter's page showed? Is your own count one
   more than before? A tool's report is something you check, just like any other answer.

**Done when:** Copilot listed your own recent commits and they match GitHub, and you compared
the presenter's browser check with your own check of your page.

| What you see                         | Next action                                                                   |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| GitHub sign-in fails                 | It may be blocked by policy. Tell a helper and follow the presenter's screen. |
| No **Start** link above `"github"`   | Make sure you opened `.vscode/mcp.json`, then ask a helper.                   |
| Copilot does not use the GitHub tool | Select **Start** first, say "Use the GitHub tools", and allow the tool.       |

More to try: ask the GitHub tools which file has changed most often, or for the message of your
very first commit, and compare with GitHub. To see where new tools come from, press **F1**, type
**MCP: Add Server**, look at the choices, then press **Esc** to close it without adding anything.

## 2. Teach Copilot About Your Project

**An optional extra, 45 minutes.** You need your website from Days 1-2, and Agent Chat in the
same browser-based Codespace.

On Monday you used a skill someone else wrote: `/create-website`. Here you write your own, plus a
short instructions file that Copilot reads before every request about your website. Both are
ordinary text files that you can read, change, and save to GitHub.

|                | Instructions file                                          | Skill                                                |
| -------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| What it is     | Standing rules Copilot reads automatically                 | A recipe that runs when you ask for it                |
| Example        | "Write for busy managers. Keep my colors. Explain changes simply." | `/make-image a friendly rocket` draws a picture for your page |
| Where it lives | `.github/instructions/my-website.instructions.md`          | `.github/skills/make-image/SKILL.md`                 |

### Write Your Instructions File (15 minutes)

1. In Agent Chat, ask:

   > Create .github/instructions/my-website.instructions.md that applies to every file under
   > site/. Read my site/index.html to see what my website does. Include who it is for, three
   > short rules I want you to keep (for example colors, tone, and keeping it simple), and a rule
   > to explain every change in one plain sentence. Keep it under 15 lines.

2. Open the new file. The first lines name `site/`: that is how Copilot knows when to use it.
   Change one rule into your own words and save.
3. Test it. Ask: "Add a short line at the bottom of my page saying who it is for."
   **Check:** did Copilot follow your rules, such as the one-sentence explanation?

### Write Your Own Picture Skill (20 minutes)

Your Codespace can draw pictures with the workshop's AI picture models. A small helper does the
drawing; your skill is the recipe that tells Copilot when and how to use it.

4. In Agent Chat, ask:

   > Create a skill called make-image in .github/skills/make-image/SKILL.md. When I type
   > /make-image and describe a picture, run python3 scripts/workshop_ai.py image "my description",
   > put the new picture in my page (in the header if I do not say where), and ask me to check it.
   > Only friendly, made-up pictures: no real people, logos, or words in the picture.

5. Open `SKILL.md`. Read the `name` and `description` at the top: they tell Copilot what the skill
   is for. Read the steps below them and change anything that is not what you meant.
6. Start a new chat with **+**. Before typing, check the button under the chat box: if it says
   **Copilot**, select it and choose **Local**, so **Keep** and **Undo** still appear. Type
   `/make-image a friendly rocket for my header` and send it.
   For a page in its own folder, add where it goes, for example
   `/make-image a picnic table for my team-lunch page`.
   **Check:** a new picture file appears in **site > art**, and your page shows it in the preview.
   Do not like it? Run `/make-image` again with different words, or select **Undo** in Chat.

### Try a Ready-Made Skill: Add a Chat (5 minutes)

7. Type `/add-chat` and send it. An **Ask** button appears at the bottom right of your page.
8. Select **Ask** and ask: "What is on this page?"
   **Check:** compare the answer with your page. The assistant reads only what your page shows,
   and it can be wrong, so you check.

### Save Your Work (5 minutes)

9. Save. In **Source Control**, review the new files, commit with the message
   `Teach Copilot about my website`, and push (from Day 4 on, through a pull request). Confirm
   the files on GitHub.

**Done when:** Copilot followed a rule from your instructions file, your own `/make-image` skill put
a new picture on your page, you checked one answer from the chat, and your files are on GitHub.

| What you see                         | Next action                                                              |
| ------------------------------------ | ------------------------------------------------------------------------ |
| Your rules seem to be ignored        | Check the file is under `.github/instructions/` and names `site/`.       |
| `/make-image` does not appear        | Check the folder name matches the skill's `name`, then start a new chat. |
| "Busy"                               | Wait a minute and try again.                                             |
| "Not switched on" (pictures or chat) | Show a helper: your Codespace may need a restart.                        |

More to try: write a second skill, `/edit-image`, that runs `python3 scripts/workshop_ai.py edit`
on the picture you describe, with your change; the old picture stays, so you can always go back.
Or write a skill for a routine task at work and test it with made-up content. To see how a
ready-made skill is written, read `.github/skills/add-chat/SKILL.md` without changing it.

## Official References

- [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp) and [MCP in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
- [Set up the GitHub MCP server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server) and [use it in your editor](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server).
- [Browser tools in VS Code](https://code.visualstudio.com/docs/agents/run/browser-tools): what the presenter uses.
- [Custom instructions in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions).
- [Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills) and [about agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).
- [Customization comparison](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).
