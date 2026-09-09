# Codespaces setup

The container requests at least 4 CPUs, 16 GB RAM, and 32 GB storage. These are
minimum requirements, not a fixed machine size. Larger machines consume more
billable compute, and organization policy can restrict available sizes.

Changing this file does not resize a running Codespace. On
[Your Codespaces](https://github.com/codespaces), open the Codespace's menu and
choose **Change machine type**. Expect a restart. For a new Codespace, use the
repository's **Code > Codespaces > ... > New with options** menu. New creations
use the configuration committed and pushed to the selected branch.

Tools run inside the container. Setup installs Python dependencies from the
checked-in lockfile with `uv sync --locked --extra dev --extra web` and finishes
before normal attachment. Day 2 service configuration is optional.

The image and feature tags can change; extension IDs and the Copilot CLI installer
do not pin versions. Record tool versions during rehearsal. Installed tools do
not prove successful authentication or organization-agent access.

Browser demonstrations use Copilot's built-in browser tools when available; no
separate browser automation server is installed. Port 8000 is forwarded, but the
application still needs to be started. Keep forwarded ports private by default.

Prebuilds must be configured in repository settings. Codespaces secrets and Actions
secrets are separate and must be configured separately for the relevant labs.

## Official references

- [Minimum machine specifications](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/setting-a-minimum-specification-for-codespace-machines)
- [Changing machine type](https://docs.github.com/en/codespaces/customizing-your-codespace/changing-the-machine-type-for-your-codespace)
- [Codespaces prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds)
- [Forwarding ports](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace)