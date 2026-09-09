# Lab 00: Browser-only setup

**Objective:** Open your repository in a Codespace and confirm Copilot and GitHub access.

**Time-box:** 30 minutes

**Prerequisites:** A browser, assigned GitHub account, Copilot seat, and write access to your repository.

The opening [possibilities tour](../../docs/REFERENCES.md#day-1-see-the-possibilities) shows
the same project in GitHub Chat/Spaces, VS Code, CLI, and a prepared cloud-agent PR. Codespaces
supplies the development environment; Copilot supplies assistance. This lab only sets up the
core environment, not every feature shown in the tour.

The first build task is [TravelPlannerAgent](../01-vscode-agent/README.md): you create its
flight/hotel skills, then consume the facilitator's shared AttractionsAgent in Lab 02.
The vendor-review application is already provided for the later deployment and business labs.

## Steps

1. Open your repository, select **Code > Codespaces > Create codespace on main**, and wait for setup.
2. Confirm the Copilot icon is visible in VS Code and open Copilot Chat.
3. In the Codespace terminal, run `python --version`, `node --version`, `gh --version`, and `copilot --version`. All four are installed by the container.
4. Run `gh auth status`. Start `copilot` separately and follow its sign-in flow if requested. Installation does not guarantee authentication; use the assigned account for both.
5. Run `uv run pytest` and confirm the starter tests pass.
6. In the built-in **Ask** or **Agent** role, open [the fictional trip brief](../../travel/trip-brief.json)
   and ask what inputs a travel planner needs. Do not ask the vendor-analyst role to plan a trip.
7. Open the Customizations editor and identify repository-provided examples versus built-in
   roles. The three vendor-review agents are for the business case later in the week;
   their presence does not prove managed plugin delivery. You will create your own travel role.
8. Open `config.json` and replace `Your Name` with your assigned unique workshop label, such as `Workshop Team 01`. One repository has one configuration and one deployed app, even when two people share it.
9. Run `uv run uvicorn app.main:app --host 0.0.0.0 --port 8000` in a terminal. Open port 8000
   from the Codespaces **Ports** view and confirm your label and the three synthetic vendors.
   Keep that terminal running while using the app; use another terminal for lab commands.

**Done when:** the tools and sign-in work, starter tests pass, the fictional brief is understood,
you can identify a customization's source, and the provided app shows your unique label and
synthetic sample rows.

No local Node.js is required as a prerequisite; Node runs inside the Codespace.
As an optional local alternative for an approved developer workstation, install the CLI with
`winget install GitHub.Copilot`. Codespaces is the intended attendee environment; verify
the actual client features instead of assuming desktop and browser parity. Missing browser
tools or managed-plugin access go to the facilitator, not a new installation exercise.

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
