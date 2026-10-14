# Advanced Reference: Remote GitHub MCP Configuration

> **Post-workshop reference, not a workshop lab.** On 14 October 2026 the owner simplified
> Days 3-5 for first-time users, so this material left the schedule. Days, clock times, lab
> numbers, and time-boxes below are historical. Use it later with a technical owner; it does
> not change the [current agenda](../../docs/AGENDA.md). See [the advanced index](README.md).

**Objective:** Connect the remote GitHub MCP server and perform a read-only repository query.

**Original time-box:** 60 minutes

**Prerequisites:** Active Codespace, Copilot access, and permission to read your repository.

Today's separate 10:45-11:15 [tools introduction](cli-and-browser-tools.md) used a prepared
Playwright connection. This lab makes the
connection explicit: discover a tool, inspect what it can do, authenticate, call it, and verify
the result. MCP configuration, a skill's instructions, and the built-in browser tools are different things.

Playwright supplied browser tools; MarkItDown is an optional document-conversion extension,
not prior required work. This is another connection: GitHub MCP exposes repository data and actions. The learning goal is the
same: inspect permissions, call the intended tool, and verify its result. All local configuration
and terminal work remains inside Codespaces; the GitHub service itself is remote.

## Steps

1. Open the Command Palette in the Codespace and choose **MCP: Add Server**, then **HTTP**.
2. Enter `https://api.githubcopilot.com/mcp/`, save the GitHub server in the workspace's `.vscode/mcp.json`, and follow the GitHub authentication flow.
3. Follow the [GitHub MCP toolset guide](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/configure-toolsets) to configure read-only mode. Inspect the tool list before approving access; requesting read-only behavior in a prompt is not the same as removing write tools.
4. Ask Copilot to list open issues through the GitHub MCP server.
5. Ask it to read one issue and summarize acceptance criteria without changing the issue.
6. Inspect the listed MCP tools and verify write tools are unavailable or disabled.
7. Remove or disable the connection after the exercise if required by facilitator policy.

The remote GitHub server needs no local runtime. Browser automation uses the prepared headless
Playwright MCP inside the Codespace. GitHub tools and browser tools are different capabilities.
Cloud-agent MCP configuration is separate from `.vscode/mcp.json`; do not assume local servers
or authentication carry over.

Enterprise controls can restrict MCP servers in supported clients. Check the current supported
properties and effective policy. Matching a user-assigned server name alone is not a strong
security boundary; URL/command controls and service authorization are separate concerns.

**Done when:** a tool call retrieves a real issue from your training repository, its answer matches GitHub, and write tools are unavailable in the selected configuration.

## What you just learned

MCP gives agents governed access to external capabilities, and read-only mode reduces risk during exploration.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Trim the tool list (5 min).** Configure toolsets so only the tools you need are loaded, then notice the
   effect on how the agent behaves.
2. **Drive a browser (5-10 min).** Ask the prepared Playwright MCP to open the app at Codespace localhost or its deployment URL, inspect the table, and capture a screenshot. Its context is separate from the learner preview; otherwise inspect manually and record the limitation.
3. **Ground it deliberately (5-10 min).** Query the prepared training Space with the ten controls
   and synthetic samples. Compare the answer with a normal chat and identify its sources. If you
   create your own Space, include only synthetic files; do not attach the whole repository or `.facilitator/`.
4. **Two routes, one fact.** Ask for the same repository fact through MCP and through `gh`, and
   compare how each answer is grounded.

## Official References

- [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp) and [MCP in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
- [Set up GitHub MCP](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server), [configure toolsets](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/configure-toolsets), and [use it in an IDE](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server).
- [Repository MCP for cloud agent and review](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers).
- [Playwright MCP](https://github.com/microsoft/playwright-mcp): the prepared Codespaces browser path. [Built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools) are optional where supported.
- [Copilot Spaces](https://docs.github.com/en/copilot/concepts/context/spaces) and [enterprise-managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).
- [Whole-week coverage and extras](../../docs/REFERENCES.md).
