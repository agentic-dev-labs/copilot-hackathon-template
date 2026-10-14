# Lab 04: Copilot Uses Tools (MCP)

**Objective:** Plug a tool into Copilot so it can read your GitHub repository, check what it
reports, and watch Copilot use a browser.

**Time-box:** 45 minutes

**Prerequisites:** Your website from Days 1-2 and Agent Chat, in the same browser-based
Codespace. Nothing to install.

**MCP** is a standard plug for tools. With a tool, Copilot can do something it cannot do by
talking alone, such as looking things up on GitHub or clicking through a web page. You choose
which tools to plug in, and you still check what they report. The presenter shows each part first.

## 1. Plug In GitHub (25 minutes)

1. Open the Command Palette: press **F1**, or open the menu (three lines, top left) and choose
   **View > Command Palette**. Type **MCP: Add Server** and select it.
2. Choose **HTTP**. Paste `https://api.githubcopilot.com/mcp/readonly` and press Enter.
   `readonly` means Copilot can look at your repository but cannot change anything on GitHub.
3. Name it `github`. When asked where to save it, choose **Workspace**. VS Code opens
   `.vscode/mcp.json`, the list of tools plugged into this project. It stays in your Codespace
   and is not saved to GitHub.
4. Sign in with GitHub when asked and allow access. If sign-in is blocked, show a helper and
   follow the presenter's screen instead.
5. In Chat choose **Agent**, then ask:

   > Use the GitHub tools to list the last three commits in my repository. For each one, tell me
   > its message and which files it changed. Do not change anything.

   If Copilot asks to use a tool, read the tool's name and allow it.
   **Check:** open your repository on GitHub in another tab and select **Commits**. Do the
   messages and files match what Copilot said?

## 2. Watch Copilot Use a Browser (20 minutes)

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

## What you just learned

MCP plugs tools into Copilot. Read-only GitHub tools can look but not change. A browser tool can
click through a page, but its report is still something you compare with what you expected.

## When It Does Not Work

| What you see                        | Next action                                                                   |
| ----------------------------------- | ----------------------------------------------------------------------------- |
| GitHub sign-in fails                | It may be blocked by policy. Tell a helper and follow the presenter's screen. |
| **MCP: Add Server** is not listed   | Check the spelling in the Command Palette, then ask a helper.                 |
| Copilot does not use the GitHub tool | Say "Use the GitHub tools" in your question, and allow the tool when asked.   |

## Optional extras

1. Ask the GitHub tools which file in your repository has changed most often. Compare with GitHub.
2. Ask for the message of your very first commit, then find it on GitHub yourself.
3. Open the tools button in the chat box and turn off one tool you do not need.

## Official References

- [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp) and [MCP in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
- [Set up the GitHub MCP server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server) and [use it in your editor](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server).
- [Browser tools in VS Code](https://code.visualstudio.com/docs/agents/run/browser-tools): what the presenter uses.
- [Whole-week topic map](../../docs/REFERENCES.md).
