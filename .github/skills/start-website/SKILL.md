---
name: start-website
description: 'Start or reopen an existing learner website in the same-window Live Preview in Codespaces. Use /start-website when the preview is closed or stopped. Reuse the saved HTML/CSS/JavaScript without recreating the page or starting a second server.'
argument-hint: 'Optional HTML file under site/'
user-invocable: true
disable-model-invocation: true
---

# Start My Website

Help a business learner see their existing page beside Copilot Chat. Do not repeat the
creation questions or edit website files. This workflow may also be followed immediately
after an approved build in [create-website](../create-website/SKILL.md).

## Choose the Existing Page

1. Use the explicitly requested HTML file under `site/`, or the confirmed active HTML file
   there; otherwise use `site/index.html`. If several pages exist and the intended one is
   unclear, ask which page in one short question. Preserve the first page and all extensions.
2. Confirm the file exists and resolves inside `site/`; do not serve a symlink or path outside
   it. If no page exists, explain **"Let's create your website first with /create-website."**
   Do not create a placeholder or silently regenerate their work.
3. Check the workspace's Live Preview settings. The prepared server root is `site`, the preview
   target is **Embedded Preview**, and saved changes refresh the page. No build step is needed.

## Open or Reuse Live Preview

Use an available VS Code command tool only when its supported scope permits this existing
workspace. Otherwise guide the learner through the single UI action below. Never claim an
editor command ran when no suitable tool is available; don't install an automation bridge.

- With a permitted command tool, call `livePreview.start.preview.atFileString` with the HTML
  path **relative to the configured server root**, for example `index.html` or
  `ideas/my-list/index.html`, not `site/index.html`. The configured target opens it embedded.
  This extension command reuses an existing server or starts its managed server if stopped.
- UI fallback: open the chosen HTML file, then **View > Command Palette > Live Preview: Show
  Preview (Internal Browser)**. Keep Chat beside the preview in the same Codespaces browser tab.
- No repeated installer, terminal command, bundler, npm project, or duplicate Python server.
  Keep files unchanged. If the extension is missing, explain the fresh-Codespace/rebuild
  requirement to the helper; installation is facilitator preparation, not the learner's task.

## Check the Preview

The usual private ports are 3000 for the page and 3001 for updates. The extension's status
indicator shows actual ports when defaults were busy. If embedding shows a blank/access page,
open those private forwarded URLs once through **Ports > Open in Browser**, allow the normal
GitHub redirects, then reopen the embedded preview. Never change visibility to Public.

Ask **"Can you see your page beside Chat?"** unless an actual UI observation already proves it.
A successful command or HTTP response alone does not prove embedded rendering. State a blocked
step honestly. When corporate browser policy blocks embedding, use the private external tab;
[Lab 01](../../../labs/01-vscode-agent/README.md), under "Python Fallback With a Helper", documents the
manual-refresh Python fallback. Do not switch to it silently or stop another process.

Once visible, say **"Your files are ready to improve. Tell Copilot one change, then save and
check the result. Use /stop-website to stop this preview."** If already visible, leave the
server alone. Reloads may reset temporary form entries. No sign-in for the app, Dataverse,
publication, or separate frontend runtime is required. Do not commit, push, or deploy.

Official reference: [Microsoft Live Preview](https://github.com/microsoft/vscode-livepreview).