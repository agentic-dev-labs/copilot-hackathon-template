# Technical Track: CLI and Prepared Browser Tools

These introductions belong to **Day 3**, not the beginner days. They fit the existing
demonstration blocks: CLI at **09:00-09:15**, followed by the cloud-agent introduction;
MCP/Playwright at **10:45-11:15**, followed by Lab 04's full configuration exercise.
There is no additional tools hour. The [agenda](AGENDA.md) remains the timing authority.

The facilitator prepares `cli` and `browser` profiles and checks sign-in before the technical
session. Use browser-based Codespaces throughout. Missing access remains a blocker, not a
reason to install tools on laptops or disable permissions. MarkItDown is not needed here.

## CLI: One Request and Refinement (15 minutes)

Copilot CLI is another interface to the assistant, inside the terminal. It is not the terminal
itself and does not automatically inherit editor chat or authentication.

1. Open a second Codespaces Bash terminal with the terminal **+**. Keep any preview server
   running in its original terminal. Run `copilot` in the second terminal.
2. Ask: "Read site/brief.md and suggest one clearer label for my page. Do not change files or
   run commands." If you did not build a site, ask it to read app/main.py and suggest one clearer
   label for the synthetic vendor reader instead. Approve only understood, scoped file access.
3. Follow up: "Make the suggestion shorter and explain who it helps."
   Compare the answer with the actual page/file, not a different editor conversation.
4. Use `/exit` before typing Bash commands. If sign-in is missing, use the official flow with
   a helper; never paste a password or token into Chat. Installation alone is not authentication.

The remaining 15 minutes of the 09:00 block introduce one bounded issue and the cloud-agent
review workflow. Continue with [Lab 03](../labs/03-cloud-agent/README.md) at 09:30.

## MCP and Playwright: Observe a Browser Check (30 minutes)

### Inspect the Connection (10 minutes)

**MCP connects Copilot to tools; Playwright supplies browser tools.** CLI is not a prerequisite.
Return to editor Chat. Inspect the prepared `playwright` connection, launcher, and available
tools. Review trust and enable only the intended tools. Use **MCP: List Servers** with the
presenter; do not enable every server to fix a missing one.

The browser is headless inside the Codespace. Results and screenshots appear in Chat; it does
not control your laptop browser. Its data and cookies are separate from your private preview.
Configuration of another connection, remote GitHub MCP, is the next lab.

### Check One Existing Feature (15 minutes)

Use your own working website or the prepared local-sample vendor reader. No Dataverse connection
or write form is required. For the reader, the helper starts `app.main:app` with no Dataverse
configuration, then you can ask:

> Use Playwright to open http://localhost:8000. Confirm the page identifies local synthetic
> samples. Apply the assessed-below-five filter, inspect the remaining scores, then reset.
> Check a narrow-screen layout. Report actual observations; do not change files. Save any
> screenshots under research/browser/, not the published site.

Use the actual port. For a personal page, substitute its real existing interaction, such as
adding and removing a fictional item. Do not ask the browser to prove a feature not implemented.

Inspect the tool calls and compare with your own manual check through the private Ports preview.
If a genuine problem appears, propose a small correction and repeat the failed check after any
approved fix. Do not invent a defect for the demonstration. If you selected remembering as an
extension, create and refresh the fictional entry within the same automation browser context;
your own preview's entries do not transfer to it.

### Record the Observation (5 minutes)

Record expected versus actual, the real tool call, any failure, and what you checked manually.
A screenshot or install check is not an observed interaction. This is not yet a saved test or
CI coverage; Day 4 makes the journey repeatable. Keep unavailable live tools explicitly blocked.

**Done when:** the CLI request/refinement and prepared browser journey were actually observed
and checked against the source or manual result. These are technical-track outcomes, not
requirements for completing Monday or Tuesday.

## Helper Preparation

Use [the independent setup profiles](../.devcontainer/README.md). Verify CLI access with the
intended identity privately. Prepare only the selected workspace `playwright` entry from the
reviewed example, preserving existing entries. Learners still inspect trust and tool access.
Test an actual invocation in VS Code Web. Never publish MCP/debugger ports, disable TLS or
sandboxing, print credentials, or assume desktop and Codespaces tool discovery are identical.

## Optional extras

1. Inspect one additional page state or repeat a manual keyboard check.
2. Compare a repository fact from GitHub MCP with the source page during Lab 04.
3. Bookmark a reviewed everyday-work skill for Friday; do not add document conversion now.

## Official References

- [Copilot CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart).
- [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).
- [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp).
- [MCP in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
- [Playwright MCP](https://github.com/microsoft/playwright-mcp).
- [Whole-week topic map](REFERENCES.md).