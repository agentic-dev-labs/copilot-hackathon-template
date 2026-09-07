# Lab 00: Browser-only setup

**Objective:** Open your repository in a Codespace and confirm Copilot and GitHub access.

**Time-box:** 30 minutes

**Prerequisites:** A browser, assigned GitHub account, Copilot seat, and write access to your repository.

## Steps

1. Open your repository, select **Code > Codespaces > Create codespace on main**, and wait for setup.
2. Confirm the Copilot icon is visible in VS Code and open Copilot Chat.
3. In the Codespace terminal, run `python --version`, `node --version`, `gh --version`, and `copilot --version`. All four are installed by the container.
4. Run `gh auth status`. If prompted, follow the browser sign-in flow using the assigned account.
5. Run `python -m pytest` and confirm the starter tests pass.
6. Open Copilot Chat and check the agents list. A `vendor-analyst` agent is already there, shared from the organization; nobody installed it.
7. Ask Copilot Chat to explain `src/vendor_assurance/chunker.py`.
8. Open `config.json` and replace `Your Name` with your own name. Everything you deploy later is named from this.

No local Node.js is required or permitted as a prerequisite; Node runs inside the Codespace.
As an optional local alternative for an approved developer workstation, install the CLI with
`winget install GitHub.Copilot`. All labs remain supported in the browser.

## What you just learned

You can use a consistent development environment and Copilot without installing a runtime on the laptop.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Read the recipe.** Open `.devcontainer/devcontainer.json` and work out which tools it installed
   for you, which extensions you did not choose, and where the `vendor-analyst` agent came from.
   Everyone in the room is running what that one file says.
2. **Ask the same question twice.** Ask Copilot Chat on github.com what this repository does, then
   ask the agent in your Codespace. Notice which one can actually open the files.
3. **Skim the commands.** Run `copilot`, type `/help`, and note three slash commands you want to come
   back to later in the week.
