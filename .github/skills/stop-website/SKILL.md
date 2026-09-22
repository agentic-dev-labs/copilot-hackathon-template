---
name: stop-website
description: 'Stop the learner website preview without deleting files, stopping the Codespace, or affecting unrelated processes. Use /stop-website when finished previewing; /start-website reopens the existing page later.'
user-invocable: true
disable-model-invocation: true
---

# Stop My Website

Stop only the requested preview. Do not edit, delete, reset, commit, or recreate website files.
Do not stop the Codespace, change port visibility, or remove a public deployment. Stopping
preview is separate from saving work and from stopping Codespaces billing.

## Stop the Managed Preview

1. Confirm this is the workshop's Live Preview, not an unrelated service or another workspace's
   server. If the learner used the Python fallback, follow the separate rule below.
2. When an available VS Code command tool permits this existing workspace, call
   `livePreview.end` with no arguments. Otherwise guide **View > Command Palette > Live Preview:
   Stop Server**. Do not say the server stopped just because you gave the instruction.
3. In a multi-root workspace, the extension can show a server picker. Select only the
   requested site's workspace, not every server. Ask if ownership is unclear. Within one
   workspace this stops its Live Preview page/update connections, including its other open
   page previews; do not pretend it can stop only one page while keeping that server alive.
4. Verify the extension's stopped status through an actual UI result, or ask the learner to
   confirm it. An open preview tab may remain showing stale content or an offline message.
   Closing the tab alone is not evidence that the server stopped. If it is already stopped,
   say so without starting a server just to stop it.

## If the Python Fallback Was Used

Use Ctrl+C only in the known terminal running the learner's `app.site:app` server, or stop
the exact execution previously started for it when ownership is recorded. If the terminal is
unknown, ask the helper to identify it. Do not use `pkill`, `killall`, a port-wide kill command,
or terminate every Python/Node process. Do not stop another learner's server.

## Finish

After confirmed stopping, say **"Preview stopped. Your files are unchanged. Use /start-website
to open them again."** Do not promise temporary form entries survive; that needs the optional
remembering feature. Remind the learner to save/review/push through their usual workflow when
appropriate, but do not perform Git operations. To stop Codespaces compute at the end of the day,
the learner uses the separate Codespaces menu after preserving their work.

Related workflow: [Start Website](../start-website/SKILL.md).
Official reference: [Microsoft Live Preview](https://github.com/microsoft/vscode-livepreview).