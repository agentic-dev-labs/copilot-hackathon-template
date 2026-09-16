# Codespaces setup

The container requests at least 4 CPUs, 16 GB RAM, and 32 GB storage. These are
minimum requirements, not a fixed machine size. Larger machines consume more
billable compute, and organization policy can restrict available sizes.

Changing this file does not resize a running Codespace. On
[Your Codespaces](https://github.com/codespaces), open the Codespace's menu and
choose **Change machine type**. Expect a restart. For a new Codespace, use the
repository's **Code > Codespaces > ... > New with options** menu. New creations
use the configuration committed and pushed to the selected branch.

All attendee tools run inside this Linux container. Setup installs app dependencies with
`uv sync --locked --extra dev --extra web` and finishes before normal attachment. Document tools
live in separate `.venv-research/`, using [direct version pins](research-requirements.txt).
Their transitive Python dependencies are resolved at install time; record `uv pip freeze --python
.venv-research/bin/python` during rehearsal. Do not describe those as fully locked dependencies.
The optional MCP package is prerelease; validate compatibility before the event.

Browser dependencies use [package.json](browser/package.json) and [package-lock.json](browser/package-lock.json)
with `npm ci --ignore-scripts`. Playwright MCP 0.0.81 pins Playwright 1.64.0-alpha-2026-09-14.
The installer downloads matching Chromium and Linux system dependencies; the container's existing
privilege configuration must permit the documented install. The launcher uses that exact executable,
headless and isolated, not the default installed Chrome channel. Never disable TLS or the browser
sandbox to work around a failing launch. Startup fails visibly when required setup fails.

The image and feature tags can change; extension IDs and the Copilot CLI installer
do not pin versions. Record tool versions during rehearsal. Installed tools do
not prove successful authentication or organization-agent access.

Learners add the connections from [mcp.example.json](mcp.example.json) during Lab 01. The example
is not an automatically loaded configuration. It uses workspace stdio servers launched by
`bash .devcontainer/mcp.sh playwright` and `bash .devcontainer/mcp.sh markitdown`.
The `check` command verifies imports and a real Chromium launch, not VS Code/CLI discovery or
MCP protocol invocation. Headless automation provides results/screenshots, not a laptop browser.

After setup, `.venv-research/bin/python scripts/check_workshop_mcp.py` initializes each stdio
server, discovers its tool, and checks a synthetic conversion/browser navigation. CI runs this on
Linux. It is not a VS Code Web trust/discovery check, a corporate-network report download, or a
complete attendee rehearsal; those live checks remain in the rehearsal ledger.

In Copilot CLI, use `/mcp` and configure command `bash` with the **absolute Codespace path** to
the launcher and the desired server name. Derive the path with `pwd` in Bash. Do not copy
`${workspaceFolder}` into CLI configuration or assume the editor's chat/auth/browser session is shared.
Never expose MCP or debugger ports. Stop unused servers before switching to Day 2 credentials.

Port 8000 is forwarded, but the application still needs starting. Use `app.site:app` for the
learner website or `app.main:app` for the vendor app, then **Ports > Open in Browser**. For a
second running server choose and forward another port, such as 8001. Keep previews private.
Neither a laptop's localhost nor its file system points into the Codespace.

Prebuilds must be configured in repository settings. Codespaces secrets and Actions
secrets are separate and must be configured separately for the relevant labs.

## Official references

- [Minimum machine specifications](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/setting-a-minimum-specification-for-codespace-machines)
- [Changing machine type](https://docs.github.com/en/codespaces/customizing-your-codespace/changing-the-machine-type-for-your-codespace)
- [Codespaces prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds)
- [Forwarding ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace)