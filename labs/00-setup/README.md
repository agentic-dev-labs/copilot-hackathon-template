# Lab 00: Browser-only setup

**Objective:** Open your repository in a Codespace and confirm Copilot and GitHub access.

**Time-box:** 30 minutes

**Prerequisites:** A browser, assigned GitHub account, Copilot seat, and write access to your repository.

The opening [possibilities tour](../../docs/REFERENCES.md#day-1-see-the-possibilities) shows
the same project in GitHub Chat/Spaces, VS Code, CLI, and a prepared cloud-agent PR. Codespaces
supplies the development environment; Copilot supplies assistance. This lab only sets up the
core environment, not every feature shown in the tour.

## Steps

1. Open your repository, select **Code > Codespaces > Create codespace on main**, and wait for setup.
2. Confirm the Copilot icon is visible in VS Code and open Copilot Chat.
3. In the Codespace terminal, run `python --version`, `node --version`, `gh --version`, and `copilot --version`. All four are installed by the container.
4. Run `gh auth status`. Start `copilot` separately and follow its sign-in flow if requested. Installation does not guarantee authentication; use the assigned account for both.
5. Run `python -m pytest` and confirm the starter tests pass.
6. Open Copilot Chat and select `vendor-analyst`. Inspect its definition in `.github/agents/vendor-analyst.agent.md`. This copy comes from the template; its presence alone does not prove organization sharing or plugin installation.
7. Switch back to the built-in **Ask** or **Agent** role and ask it to explain `src/vendor_assurance/chunker.py`. The specialist `vendor-analyst` expects a report and evaluator JSON, not a general coding question.
8. Open `config.json` and replace `Your Name` with your assigned unique workshop label, such as `Workshop Team 01`. One repository has one configuration and one deployed app, even when two people share it.

**Done when:** the tools run, tests pass, the selected agent's source is identified, and your label is set.

No local Node.js is required as a prerequisite; Node runs inside the Codespace.
As an optional local alternative for an approved developer workstation, install the CLI with
`winget install GitHub.Copilot`. All labs remain supported in the browser.

## What you just learned

You can use a consistent development environment and Copilot without installing a runtime on the laptop.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Read the recipe.** Open `.devcontainer/devcontainer.json` and work out which tools it installed
   for you, which extensions you did not choose, and where the `vendor-analyst` agent came from.
   Identify what is pinned, what is a minimum, and what depends on account or client settings.
2. **Ask the same question twice (5 min).** Ask Copilot Chat on github.com what this repository does,
   then ask in your Codespace. Both can use repository context; compare the cited files and available tools.
3. **Skim the commands.** Run `copilot`, type `/help`, and note three slash commands you want to come
   back to later in the week.

Stop your Codespace when finished for the day. Closing the browser tab does not immediately stop compute billing.

## Official References

- [Codespaces overview](https://docs.github.com/en/codespaces/overview): where the environment runs and how access/billing work.
- [Devcontainers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers): shared tools, settings, lifecycle, and rebuilding.
- [Codespaces quickstart](https://docs.github.com/en/codespaces/quickstart): creating and using the environment.
- [Copilot getting started](https://docs.github.com/en/copilot/get-started/quickstart) and [CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart): installation, sign-in, and first use.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): the branch/commit/PR workflow used in later labs.
- [Whole-week coverage and extras](../../docs/REFERENCES.md): official links for the opening tour and optional work.
