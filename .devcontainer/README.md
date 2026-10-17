# Codespaces setup

The container requests at least 4 CPUs, 16 GB RAM, and 32 GB storage. These are
minimum requirements, not a fixed machine size. Larger machines consume more
billable compute, and organization policy can restrict available sizes.

Changing this file does not resize a running Codespace. On
[Your Codespaces](https://github.com/codespaces), open the Codespace's menu and
choose **Change machine type**. Expect a restart. For a new Codespace, use the
repository's **Code > Codespaces > ... > New with options** menu. New creations
use the configuration committed and pushed to the selected branch.

All attendee tools run inside this Linux container. The repository ships its own MCP tool list:
`.vscode/mcp.json` holds only the read-only GitHub server for Lab 04, and `.vscode/settings.json`
sets `chat.mcp.autostart` to `never`, so no tool server starts until a learner selects **Start**.
The same settings turn off MCP discovery from other apps (`chat.mcp.discovery.enabled`), chat tools
from other extensions such as Python and Pull Requests (`chat.extensionTools.enabled`), and agent
plugins (`chat.plugins.enabled`); this file's settings turn off organization custom agents.
Copilot Chat's own built-in tools are unaffected. Pylance's MCP server never starts by itself.
An exact server allowlist is enterprise policy only (`allowedMcpServers`), not a repository setting.
The Azure Container Apps extension was removed from the editor extensions on 14 October 2026: it
brought an Azure MCP server and Azure sign-in prompts that attendees cannot use. Facilitators who
need it can install it in their own Codespace. Creation installs **uv and Copilot CLI**
automatically; the CLI profile also checks `copilot --version`. Installation does not authenticate
the attendee. The container requests the Python, Python Environments, and Ruff editor extensions so
Ruff can use the project environment. Content setup runs `uv sync --locked --extra dev --extra web`
and installs the pinned extension packager before normal attachment. The post-attach preview profile
repairs any missing Python editor extensions and installs the repository-owned editor helper. When it
repairs an older Codespace, run **Developer: Reload Window** once at its prompt. Chromium and research
packages remain later preparation. Do not ignore a failed creation or core install. CLI teaching and
sign-in checks remain in Day 3.

## Same-Window Website Preview

The [preview helper](website-preview/package.json) is a small repository-owned VS Code
extension, packaged locally rather than downloaded from a marketplace. It opens a **Website
preview** panel that reads `site/index.html` directly and redraws it whenever a site file
changes. There is **no server, no port, and no sign-in**. The panel allows only the page's own
local files (CSS, JS, fonts, art, `data/*.json`) plus Open-Meteo for the approved Weather page;
other internet requests are blocked. Its script channel
is a user-only Unix socket in ignored `.workshop-preview/`, not an HTTP service.

At Lab 01, run `/create-website` in the built-in coding Agent. It asks only which website to
make (Project Planner, Calendar, Ideas Wall, or Weather), then copies that tested blueprint,
the local design kit and animated art into `site/`, names it after the repository, and opens
it. The source template never ships a finished `site/`. The learner installs nothing.

The skill opens the panel beside Chat automatically. `/start-website` reopens it and
`/stop-website` closes only that panel. Entries the learner adds are remembered in the
panel's browser storage and survive edits. HTML files under `site/` also show an
**Open Preview** button in the editor title bar.

**Ask my page.** `/add-chat` adds `Workshop.addChat` to a page. Its **Ask** button posts the
question and the page's visible text to this panel through the webview message channel. The
panel signs in as the workshop identity from the `FOUNDRY_*` Codespaces secrets and asks the chat
model, one question at a time and at most 20 a minute. The page never holds a credential, and its
own network rules are unchanged. Without the secrets it answers that it is not switched on. See
[AI pictures and chat](../docs/FACILITATOR.md#ai-pictures-and-chat).

For facilitator diagnosis only:

```bash
python3 scripts/website_preview.py status
python3 scripts/website_preview.py start
python3 scripts/website_preview.py stop
```

The Command Palette also has **Workshop Website: Open Preview** and **Close Preview**.
A newly installed helper activates without reloading; an upgrade of an already loaded
version needs one **Developer: Reload Window**. The attach profile skips a matching version.
For a fresh Codespace, commit and push the reviewed changes and create it from that branch.
Verify skill discovery, first build, automatic open, one observed live update, stop, reopen,
and saved entries after an edit. Tests are not a live attendee pilot. No Chromium, CLI
sign-in, or browser MCP is needed. The Python static server on 8000 can serve a page for the
presenter's Day 3 browser demonstration and is used for deployment checks.

## Facilitator Preparation Profiles

Run the following separately in the Codespace's Bash terminal before the relevant session,
not as room-wide installation exercises. Attendees run none of them.

| Profile  | Command                                | When                                                      |
| -------- | -------------------------------------- | --------------------------------------------------------- |
| Core     | `bash .devcontainer/setup.sh`          | Automatic startup; Monday's required environment. In the template's own Codespace only, it also keeps a demo `site/` out of Source Control. |
| Preview  | `bash .devcontainer/setup.sh preview`  | Automatic after editor attachment; facilitator repair command. |
| CLI      | `bash .devcontainer/setup.sh cli`      | Automatic on creation; facilitator repair/reinstall command. Sign-in stays separate. |
| Browser  | `bash .devcontainer/setup.sh browser`  | Not run by attendees: since 14 October the Day 3 browser check is a presenter demonstration. For a later owner-approved environment it sets aside the unused Yarn apt source, installs and launches sandboxed Chromium, then adds the reviewed `playwright` entry to `.vscode/mcp.json`. |
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

When it succeeds, the browser profile runs `scripts/enable_playwright_mcp.py`, which copies only
the `playwright` entry from [mcp.example.json](mcp.example.json) into `.vscode/mcp.json`. It keeps
existing entries, such as Lab 04's GitHub server, and leaves alone a file it cannot safely merge.
Because that file is tracked, the added entry then shows as a change; do not commit it to the template.
The user then starts and trusts the server. MarkItDown is optional and never added
automatically; the example file itself is not an automatically loaded configuration. It uses workspace stdio servers launched by
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

Two findings from a 14 October 2026 dry run in the owner's Codespace. First, the base image's
Yarn apt source (`dl.yarnpkg.com`) failed its signature check (`NO_PUBKEY 62D54FD4003F6525`) and
stopped Playwright's dependency install. The repository does not use Yarn, so the browser profile
renames that source to `yarn.list.disabled` before apt runs; no key is trusted and no check is
skipped. Second, Chromium still could not start: the container's default seccomp filter blocks
the user namespaces its sandbox needs (`unshare --user` fails), and the container lacks
`CAP_SYS_ADMIN`, so the setuid sandbox cannot help either. Enabling it needs an owner-approved
container change, such as `"runArgs": ["--security-opt", "seccomp=unconfined"]`, tested in a
fresh Codespace. The owner chose the alternative for this workshop: a presenter demonstration
with VS Code's built-in browser tools; see the [Day 3 helper notes](../docs/TOOLS-PRACTICE.md#helper-preparation).

In Copilot CLI, use `/mcp` and configure command `bash` with the **absolute Codespace path** to
the launcher and the desired server name. Derive the path with `pwd` in Bash. Do not copy
`${workspaceFolder}` into CLI configuration or assume the editor's chat/auth/browser session is shared.
Never expose MCP or debugger ports. No Dataverse credentials are needed for the workshop;
stop unused servers before any separately approved post-workshop service configuration.

Port 8000 is forwarded silently, without a pop-up, for the Day 3 browser check, technical
examples, and static build checks. Use `app.site:app` for the
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
- [VS Code webviews](https://code.visualstudio.com/api/extension-guides/webview): the server-free website preview panel.
- [VS Code API](https://code.visualstudio.com/api/references/vscode-api): editor-owned tabs and native tools.
- [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills): explicit invocation and discovery.
