# Day 3: More Ways to Use Copilot

Today you keep the same Codespace and the website you already built. You will see three more
ways to work with Copilot, then pick the idea you will build tomorrow. Nothing is installed on
your laptop, and everything uses made-up content. The presenter shows each step first, then
pauses for your turn. You do not need to read ahead.

**Missed a day, or no website yet?** In Chat choose **Agent**, run `/create-website`, and pick
the Project Planner. A helper can get you started while the room continues.

## Today's Route

| When        | Open                                              | You are finished when                                                       |
| ----------- | ------------------------------------------------- | --------------------------------------------------------------------------- |
| 09:00-09:45 | [Copilot in the terminal](#copilot-in-the-terminal) | You asked Copilot CLI about your website and saw one change appear.        |
| 09:45-10:30 | [Lab 04](../labs/04-mcp/README.md)                | Copilot read your GitHub history, and you compared a browser check.         |
| 10:45-11:30 | [Lab 06](../labs/06-multi-agent/README.md)        | Your rules work, your own `/make-image` skill drew a picture, and your page has a chat. |
| 11:30-12:15 | [Pick your idea](#pick-your-idea)                 | Your idea has a short brief, a first step, and is saved on GitHub.          |
| 12:15-12:30 | [Lab 03](../labs/03-cloud-agent/README.md)        | You watched the cloud agent turn an issue into a pull request.              |

The [agenda](AGENDA.md) includes the break and the rest of the week. Lab numbers are just
names, so follow this table from top to bottom.

## New Words for Today

| Word              | Plain meaning                                                                         |
| ----------------- | ------------------------------------------------------------------------------------- |
| Terminal          | The panel below the editor where you type commands.                                   |
| CLI               | Copilot inside the terminal. The same assistant as Chat, through a different door.     |
| MCP               | A standard plug for adding tools to Copilot, such as reading GitHub or using a browser. |
| Browser tools     | Copilot opening a web page, clicking, and reporting what it sees. The presenter shows this. |
| Instructions file | A short note of rules Copilot reads before every request about your project.          |
| Skill             | A reusable recipe you run with a slash command, like `/create-website` on Monday.      |
| Issue             | A to-do note on GitHub that describes what you want.                                  |
| Pull request      | A proposed change that you review before accepting it into your project.              |

## Copilot in the Terminal

**09:00-09:45.** The presenter shows each step, then you try it.

1. Open the menu (the three lines at the top left), then **Terminal > New Terminal**. A panel
   opens at the bottom of the screen. Type `copilot` and press Enter.
2. If it asks whether you trust this folder, choose yes: it is your own project.
3. Sign in once: type `/login` and press Enter, then choose the first option. Copilot shows a
   short code. Open [github.com/login/device](https://github.com/login/device) in a new browser
   tab, type the code, and select **Authorize**. Never paste a password or token into Copilot.
4. Ask:

   > Read site/brief.md and site/index.html. In three short bullet points, explain what my
   > website does. Do not change any files.

   If it asks permission to read files, allow it. Say no to anything you do not understand.
   **Check:** compare its answer with your page. Is anything wrong or missing?
5. Ask: "Suggest one small improvement for someone who opens my page for the first time."
6. Ask: "Make that one change in site/index.html only. Keep everything else the same."
   Read what it wants to change before you allow it. In Chat, run `/start-website` if the
   preview is closed, and watch the change appear. **Check:** does the page still work?
7. Open **Source Control** to see the change. Keep it, or ask a helper to undo it. Type `/exit`
   to leave Copilot; the terminal stays open.

**Done when:** you asked Copilot CLI about your own website, compared its answer with the page,
and saw one change appear in your preview. If sign-in is blocked, follow the presenter's screen
and tell a helper; it is not a reason to install anything.

**What you just learned:** Chat and the terminal are two doors to the same assistant. Both work
on the same files, and you check the result the same way.

## Pick Your Idea

**11:30-12:15.** Tomorrow is build day, so choose one idea now. Pick one:

- **Keep going with Tuesday's idea.** Most people will choose this.
- **Start a new idea.** In Agent Chat run `/create-website`, choose to build your own idea, and
  describe it in one sentence. It gets its own folder under `site/ideas/` and never replaces your
  first page.
- **Make a helper for a routine task.** Write a skill like the one in Lab 06, and test it with
  made-up examples, never real work records.

1. **Answer four questions (10 minutes).** Who is it for? What should they be able to do? What
   is the smallest first version? How will I check it myself? Tell a neighbor or a helper.
2. **Write a short brief (10 minutes).** Ask Chat: "Write a short brief for my idea in its
   folder's brief.md using my four answers. Keep it under 15 lines and end with one check I
   will do myself." Read it and correct one sentence in your own words.
3. **Take the first step (20 minutes).** Ask for the smallest first version, or one improvement
   to Tuesday's idea. Watch the preview and do your check.
4. **Save (5 minutes).** Save, review, commit, and push. Open GitHub and confirm the brief is there.

**Done when:** your idea has a brief with a check you will do yourself, a first step started,
and your work is visible on GitHub. Tomorrow, follow the [build day guide](DAY-4-BUILD.md).

## Helper Preparation

- Before Day 3, confirm the training accounts may use Copilot CLI, the remote GitHub MCP server,
  and the cloud agent. Check one attendee sign-in path privately. Installed is not signed in.
- **This repository keeps attendees' Copilot to its own tools.** `.vscode/mcp.json` lists only the
  read-only GitHub server. `.vscode/settings.json` sets `chat.mcp.autostart` to `never` (nothing
  starts until an attendee selects **Start** in Lab 04), switches off `chat.mcp.discovery.enabled`
  for every other app (Copilot CLI, Claude, Cursor, Windsurf), and sets `chat.extensionTools.enabled`
  and `chat.plugins.enabled` to `false`, which hides other extensions' chat tools and any agent
  plugin. The devcontainer turns off organization custom agents. VS Code has no repository setting
  that allows only named servers; that allowlist is enterprise policy (`allowedMcpServers` in Copilot
  managed settings). Personal servers in your own VS Code profile are not affected, so before you
  present, run **MCP: List Servers**, pick each personal server, and choose **Disable** for this workspace.
- **Decision, 14 October 2026: the browser check in Lab 04 is a presenter demonstration.**
  Attendees install nothing for it. VS Code's integrated browser and its browser tools are a VS
  Code Desktop feature, so open your Codespace in VS Code Desktop for this demo, keep
  `workbench.browser.enableChatTools` on, and turn on `workbench.browser.enableRemoteProxy`
  (preview) so the browser can reach pages in the Codespace. Rehearse the exact page and steps
  there beforehand. Serve the page privately with
  `uv run uvicorn app.site:app --port 8000` if the tools need a web address, and never make the
  port public. Background: in the owner's Codespace the pinned Playwright browser installed in
  about 40 seconds (`bash .devcontainer/setup.sh browser`) but could not start, because the
  container's default seccomp filter blocks the user namespaces Chromium's sandbox needs. Keep
  that profile for a later owner-approved environment, such as a reviewed
  `"runArgs": ["--security-opt", "seccomp=unconfined"]` tested in a fresh Codespace. Never add
  `--no-sandbox`.
- Start the cloud-agent demonstration issue before 12:15 so its pull request is ready, or show a
  prepared one and say that it is prepared. See [Lab 03](../labs/03-cloud-agent/README.md).
- Never publish MCP or debugger ports, disable the browser sandbox or TLS checks, or print
  credentials. No Dataverse connection, vendor app, or research download is needed today.
- Deeper material lives in the [advanced reference](../post-workshop/advanced/README.md); do
  not add it to today's blocks.

## Optional extras

1. In Copilot CLI, type `/help` and find one command you would like to try later.
2. Ask the CLI the same question you asked Chat on Monday. Which answer was clearer?
3. Write down one routine task at work that a skill could help with, for Friday's story.

## Official References

- [Copilot CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart).
- [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).
- [MCP concepts](https://docs.github.com/en/copilot/concepts/context/mcp) and [MCP in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers).
- [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).
- [Whole-week topic map](REFERENCES.md).
