# Lab 04: Remote GitHub MCP

**Objective:** Connect the remote GitHub MCP server and perform a read-only repository query.

**Time-box:** 60 minutes

**Prerequisites:** Active Codespace, Copilot access, and permission to read your repository.

Day 1 introduced MCP as one way to connect an agent to tools or data. This lab makes the
connection explicit: discover a tool, inspect what it can do, authenticate, call it, and verify
the result. MCP configuration, a skill's instructions, and the built-in browser tools are different things.

## Steps

1. Open the Command Palette in the Codespace and choose **MCP: Add Server**, then **HTTP**.
2. Enter `https://api.githubcopilot.com/mcp/`, save the GitHub server in the workspace's `.vscode/mcp.json`, and follow the GitHub authentication flow.
3. Follow the [GitHub MCP toolset guide](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/configure-toolsets) to configure read-only mode. Inspect the tool list before approving access; requesting read-only behavior in a prompt is not the same as removing write tools.
4. Ask Copilot to list open issues through the GitHub MCP server.
5. Ask it to read one issue and summarize acceptance criteria without changing the issue.
6. Inspect the listed MCP tools and verify write tools are unavailable or disabled.
7. Remove or disable the connection after the exercise if required by facilitator policy.

The remote GitHub server needs no local runtime. Browser automation is a separate demonstration
using **Copilot's built-in browser tools**, not an additional MCP server. Check which tools your
VS Code client exposes; follow the facilitator demo if they are unavailable in your Codespace.
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
2. **Drive a browser (5-10 min).** If your Copilot session exposes built-in browser tools, ask it to open your app's forwarded or deployed URL, inspect the table, and capture a screenshot. Verify the result against the page. No separate server installation is needed; otherwise inspect the page manually or follow the facilitator demo.
3. **Ground it deliberately (5-10 min).** Query the prepared training Space with the ten controls
   and synthetic samples. Compare the answer with a normal chat and identify its sources. If you
   create your own Space, include only synthetic files; do not attach the whole repository or `.facilitator/`.
4. **Two routes, one fact.** Ask for the same repository fact through MCP and through `gh`, and
   compare how each answer is grounded.

## Official References

- [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp) and [MCP in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
- [Set up GitHub MCP](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/set-up-the-github-mcp-server), [configure toolsets](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/configure-toolsets), and [use it in an IDE](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server).
- [Repository MCP for cloud agent and review](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers).
- [Built-in browser tools](https://code.visualstudio.com/docs/agents/run/browser-tools): no extra browser server is required.
- [Copilot Spaces](https://docs.github.com/en/copilot/concepts/context/spaces) and [enterprise-managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).
- [Whole-week coverage and extras](../../docs/REFERENCES.md).
