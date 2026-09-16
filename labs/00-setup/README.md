# Lab 00: Browser-only setup

**Objective:** Open your repository in a Codespace and confirm Copilot and GitHub access.

**Time-box:** 30 minutes

**Prerequisites:** A browser, assigned GitHub account, Copilot seat, and write access to your repository.

Codespaces is your remote working computer; Copilot is your assistant. A repository is a
project folder with recorded history. A terminal is where commands run. Here it is always the
**Bash terminal inside your Codespace**, never Windows PowerShell or a terminal on your laptop.
The [opening tour](../../docs/REFERENCES.md#day-1-see-the-possibilities) shows research,
presentations, planning, and small websites. The vendor app is for Day 2, not today's setup.

## Steps

### Show and try: open your workspace (10 minutes)

1. Open the **assigned learner repository**, then **Code > Codespaces > Create codespace on main**.
   The facilitator supplies a copy without private preparation notes. Do not create an attendee
   copy from an unapproved template. Wait for setup; report a failed setup rather than skipping it.
2. Open the left **Explorer** (files), then **View > Terminal**. Run:

   ```bash
   python --version
   node --version
   gh --version
   copilot --version
   gh auth status
   ```

3. Open Copilot Chat and use the built-in **Ask** or **Agent**, not a vendor-review custom role.
   Ask: "Explain the difference between my repository, Codespace, and Copilot in three sentences."
   Check the answer against what the presenter showed. Use the assigned GitHub identity.

### Show and try: one CLI task (10 minutes)

4. Run `copilot` in that same Codespace terminal and complete its sign-in if requested.
   GitHub CLI and Copilot CLI authentication are separate. Never paste tokens into chat.
5. Ask: "Suggest three questions a new colleague could answer from a public annual report.
   Use plain English. Do not download anything or change files."
6. Refine one question. Practise stopping with **Ctrl+C**, inspect `/help`, and exit the CLI
   before typing Bash commands. The chat history in VS Code does not transfer to the CLI.

### Make it yours: create a brief (10 minutes)

7. In VS Code Chat ask: "Create site/brief.md with my chosen question, audience, three things
   I want to show, and one fact I must verify. Use only public-source or fictional material."
   Open the file in Explorer and correct it. This is a plain Markdown note, not website code yet.
8. Edit `config.json` in Explorer. Replace `Your Name` with your assigned **unique workshop label**,
   for example `Workshop Team 01`. Save it. One repository has one label, even when a pair shares it.
9. Ask Copilot to explain the change. Look in **Source Control** to see the modified files.
   Saving a file is not a commit, and committing is not pushing to GitHub. You practise both later.

**Done when:** the tools are available, Chat and CLI each answer a real request using the right
account, `site/brief.md` contains your reviewed question, and your unique label is saved.

If sign-in, models, or setup are missing, ask the facilitator. Do not install tools on the laptop,
change organisation policy, or grant broad permissions to make a demonstration work.

## What you just learned

You can use a consistent development environment and Copilot without installing a runtime on the laptop.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Compare two requests (5 min).** Ask for a shorter outline or a different audience. Explain
   which result is more useful without treating confident wording as evidence.
2. **Read the recipe (5 min).** Inspect `.devcontainer/devcontainer.json` with Copilot. Identify
   one prepared dependency and one thing that still needs account permission.
3. **Run the starter checks (5 min).** Run `uv run pytest` in Bash. The facilitator runs these
   before delivery; a green suite is not proof that your MCP or live deployment works.

Stop your Codespace when finished for the day. Closing the browser tab does not immediately stop compute billing.

## Official References

- [Codespaces overview](https://docs.github.com/en/codespaces/overview): where the environment runs and how access/billing work.
- [Devcontainers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers): shared tools, settings, lifecycle, and rebuilding.
- [Codespaces quickstart](https://docs.github.com/en/codespaces/quickstart): creating and using the environment.
- [Copilot getting started](https://docs.github.com/en/copilot/get-started/quickstart) and [CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart): installation, sign-in, and first use.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): the branch/commit/PR workflow used in later labs.
- [Whole-week coverage and extras](../../docs/REFERENCES.md): official links for the opening tour and optional work.
