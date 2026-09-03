# Lab 04: Remote GitHub MCP

**Objective:** Connect the remote GitHub MCP server and perform a read-only repository query.

**Time-box:** 60 minutes

**Prerequisites:** Active Codespace, Copilot access, and permission to read the team repository.

## Steps

1. Open the Copilot MCP configuration from VS Code in the Codespace.
2. Add the remote server URL `https://api.githubcopilot.com/mcp/` using the GitHub authentication flow.
3. Configure or select read-only mode before enabling tools.
4. Ask Copilot to list open issues through the GitHub MCP server.
5. Ask it to read one issue and summarize acceptance criteria without changing the issue.
6. Inspect the listed MCP tools and verify write tools are unavailable or disabled.
7. Remove or disable the connection after the exercise if required by facilitator policy.

The remote server needs no local runtime. The GitHub MCP server and the Playwright MCP server
are enabled by default for Copilot cloud agent and Copilot code review, and repository MCP
settings apply to both. By contrast, `npx`-based community MCP servers would need Node.js;
they are not laptop prerequisites and should run only in an approved container.

Enterprises can approve or block individual MCP servers by URL, command, or name through
enterprise managed settings. Ask your administrator which servers are on the allowlist before
planning a dependency on one.

## What you just learned

MCP gives agents governed access to external capabilities, and read-only mode reduces risk during exploration.

**Stretch goal:** Ask for the same repository fact via MCP and `gh`, then compare the grounding.
