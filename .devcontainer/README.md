# Codespaces setup

The container requests at least 4 CPUs, 16 GB RAM, and 32 GB storage. These are
minimum requirements, not a fixed machine size. Larger machines consume more
billable compute, and organization policy can restrict available sizes.

Changing this file does not resize a running Codespace. On
[Your Codespaces](https://github.com/codespaces), open the Codespace's menu and
choose **Change machine type**. Expect a restart. For a new Codespace, use the
repository's **Code > Codespaces > ... > New with options** menu. New creations
use the configuration committed and pushed to the selected branch.

All attendee tools run inside this Linux container. Creation installs **uv and Copilot CLI**
automatically; the CLI profile also checks `copilot --version`. Installation does not authenticate
the attendee. Content setup runs the **core** Python profile, `uv sync --locked --extra dev --extra web`,
before normal attachment. Chromium and research packages remain separate later preparation.
Do not ignore a failed creation or core install. CLI teaching and sign-in checks remain in Day 3.

## Same-Window Website Preview

Fresh Codespaces install **Microsoft Live Preview** (`ms-vscode.live-server`) through the
devcontainer extension list. Workspace settings scope its server to `site/`, use the embedded
webview instead of the desktop Integrated Browser, and refresh **on saved file changes**.
No Chromium, npm frontend build, CLI sign-in, or browser MCP is needed for this preview.

At Lab 01, select the built-in coding Agent and run `/create-website`. The prepared skill
asks for a starter, title, audience, logo style, colors, and a small feature set, then waits
for approval. It provides neutral CSS and
an open-source local font; it does not place a completed website in the template.
Open the resulting `site/index.html`, then run **Live Preview: Show Preview (Internal Browser)**
from the Command Palette. Keep Chat visible beside the preview. Save a changed heading to
test live refresh. This is a page reload, not state-preserving hot-module replacement.

Ports **3000** (page server) and **3001** (normally the refresh connection) are forwarded.
Keep both **Private**. For Codespaces authentication, the extension documents opening both
actual forwarded URLs once through Ports, allowing the normal redirects, then reopening the
embedded preview. Browser policy may still block embedding; use the private external tab
as the fallback. If a port is occupied, a helper chooses free ports and checks the extension's
status indicator; never stop another process or change visibility to Public.

After a pull, an existing Codespace may need a rebuild to install the new extension. New
Codespaces use the **committed and pushed branch**, not local uncommitted edits. The old
`app.site:app` preview on 8000 remains a manual-refresh fallback and the deployment server.
Extension installation and skill discovery still need a fresh attendee-account rehearsal.

The provided `/start-website` and `/stop-website` skills use the extension's commands where
editor tools permit, with the matching Command Palette action as a fallback. They do not
generate files or start duplicate Python servers. The default initial page is `site/index.html`
relative to the workspace, while the file-specific start command takes a path relative to the
server root. Stop Server can prompt for a workspace when several preview servers are running;
select only the workshop site. Stopping a preview does not stop Codespaces compute or billing.

## Facilitator Preparation Profiles

Run the following separately in the Codespace's Bash terminal before the relevant session,
not as a room-wide installation exercise:

| Profile  | Command                                | When                                                      |
| -------- | -------------------------------------- | --------------------------------------------------------- |
| Core     | `bash .devcontainer/setup.sh`          | Automatic startup; Monday's required environment.         |
| CLI      | `bash .devcontainer/setup.sh cli`      | Automatic on creation; facilitator repair/reinstall command. Sign-in stays separate. |
| Browser  | `bash .devcontainer/setup.sh browser`  | Before Day 3; installs and launches sandboxed Chromium. |
| Research | `bash .devcontainer/setup.sh research` | Optional later document-conversion exercise only.         |

Each profile fails visibly when its own preparation fails. Do not run the research profile as
a workaround for a browser failure. Rebuilding may remove CLI binaries outside the workspace;
recheck the selected profiles after a rebuild. Never change policy, disable TLS, or remove the
browser sandbox to get a green result.

Document tools live in separate `.venv-research/`, using [direct version pins](research-requirements.txt).
Their transitive Python dependencies are resolved at install time; record `uv pip freeze --python
.venv-research/bin/python` during rehearsal. Do not describe those as fully locked dependencies.
The optional MCP package is prerelease; validate compatibility before the event.
MarkItDown's `all` extra requires the prerelease `azure-ai-contentunderstanding` SDK. Its exact
version is explicitly pinned so uv permits that dependency without allowing every package's
prereleases. The workshop's local conversion does not call that Azure service or require its credentials.

Browser dependencies use [package.json](browser/package.json) and [package-lock.json](browser/package-lock.json)
with `npm ci --ignore-scripts`. Playwright MCP 0.0.81 pins Playwright 1.64.0-alpha-2026-09-14.
The installer downloads matching Chromium and Linux system dependencies; the container's existing
privilege configuration must permit the documented install. The launcher uses that exact executable,
headless and isolated, not the default installed Chrome channel. The `browser` profile's
`check-browser` launches that real binary without requiring the research environment.

The image and feature tags can change; extension IDs and the Copilot CLI installer
do not pin versions. Record tool versions during rehearsal. Installed tools do
not prove successful authentication or organization-agent access.

The facilitator prepares the Playwright workspace connection for Day 3. Technical attendees inspect
and trust it before actual use; deeper configuration belongs in Lab 04. MarkItDown is optional.
Use only the needed entry from [mcp.example.json](mcp.example.json); the example is not an
automatically loaded configuration. It uses workspace stdio servers launched by
`bash .devcontainer/mcp.sh playwright` and `bash .devcontainer/mcp.sh markitdown`.
The `check-browser` and `check-research` commands are independent. `check` runs both for a
full optional-tool rehearsal. These verify imports and a real Chromium launch, not VS Code/CLI discovery or
MCP protocol invocation. Headless automation provides results/screenshots, not a laptop browser.

After both optional profiles, `.venv-research/bin/python scripts/check_workshop_mcp.py` initializes each stdio
server, discovers its tools, and checks a synthetic conversion plus browser navigation and a
separate heading read. Playwright can return a saved snapshot path rather than inline content;
the checker verifies page text, not the presence of that path. CI runs this on
Linux. It is not a VS Code Web trust/discovery check, a corporate-network report download, or a
complete attendee rehearsal; those live checks remain in the rehearsal ledger.

The research-tools CI job uses Ubuntu 22.04: the default Ubuntu runner rejected Chromium's
sandbox startup during verification. Neither the test nor the launcher disables the sandbox;
the startup check explicitly matches MCP's sandboxed browser configuration. The actual Debian
Codespace must also pass this launch and the MCP smoke check. Escalate an unsupported host
configuration to the facilitator instead of adding `--no-sandbox` or disabling a host policy.

In Copilot CLI, use `/mcp` and configure command `bash` with the **absolute Codespace path** to
the launcher and the desired server name. Derive the path with `pwd` in Bash. Do not copy
`${workspaceFolder}` into CLI configuration or assume the editor's chat/auth/browser session is shared.
Never expose MCP or debugger ports. No Dataverse credentials are needed for the workshop;
stop unused servers before any separately approved post-workshop service configuration.

Port 8000 remains forwarded for the optional Python fallback and technical examples.
Use `app.site:app` for the
learner website or `app.main:app` for the vendor app, then **Ports > Open in Browser**. For a
second running server choose and forward another port, such as 8001. Keep previews private.
Neither a laptop's localhost nor its file system points into the Codespace.

Prebuilds must be configured in repository settings. Codespaces secrets and Actions
secrets are separate. Live Dataverse setup is preserved in the
[post-workshop reference](../post-workshop/dataverse/README.md), not a beginner prerequisite.

## Official references

- [Minimum machine specifications](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/setting-a-minimum-specification-for-codespace-machines)
- [Changing machine type](https://docs.github.com/en/codespaces/customizing-your-codespace/changing-the-machine-type-for-your-codespace)
- [Codespaces prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds)
- [Forwarding ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace)
- [Microsoft Live Preview](https://github.com/microsoft/vscode-livepreview): embedded preview, save-refresh, and Codespaces authentication.
- [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills): explicit invocation and discovery.
