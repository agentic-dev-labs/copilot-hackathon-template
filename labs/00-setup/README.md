# Lab 00: Browser-only setup

**Objective:** Open the team repository in a Codespace and confirm Copilot and GitHub access.

**Time-box:** 30 minutes

**Prerequisites:** A browser, assigned GitHub account, Copilot seat, and write access to the team repository.

## Steps

1. Open the team repository, select **Code > Codespaces > Create codespace on main**, and wait for setup.
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

**Stretch goal:** Inspect `.devcontainer/devcontainer.json` and identify which tools it supplies.
