# The ready-made Codespace image. Everything here used to be installed in every attendee's
# Codespace at start-up; now it is installed once, by .github/workflows/codespace-image.yml.
# Attendee copies of the template only download this image, so their Codespaces start faster.
# It contains public tools and package caches only: no secrets, no learner work.
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

LABEL org.opencontainers.image.source=https://github.com/agentic-dev-labs/copilot-hackathon-template
LABEL org.opencontainers.image.description="Ready-made Codespace for the Copilot hackathon template"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# GitHub CLI from GitHub's signed package source. The base image's unused Yarn source can fail
# its signature check and stop apt, so it is removed rather than trusted.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && mkdir -p -m 755 /etc/apt/keyrings \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        -o /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
        > /etc/apt/sources.list.d/github-cli.list \
    && apt-get update \
    && apt-get install --yes --no-install-recommends gh \
    && rm -rf /var/lib/apt/lists/* \
    && gh --version

# Node.js 22 for the Website preview helper.
COPY --from=node:22-bookworm-slim /usr/local/bin/node /usr/local/bin/node
COPY --from=node:22-bookworm-slim /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -s ../lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
    && ln -s ../lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx \
    && node --version && npm --version

# Package caches live outside the workspace, so the Codespace's own `uv sync` and `npm ci`
# copy from them instead of downloading. TLS verification stays on.
ENV UV_CACHE_DIR=/opt/workshop-cache/uv \
    UV_LINK_MODE=copy \
    UV_NATIVE_TLS=true \
    npm_config_cache=/opt/workshop-cache/npm \
    PATH=/home/vscode/.local/bin:$PATH
RUN mkdir -p /opt/workshop-cache && chown vscode:vscode /opt/workshop-cache

USER vscode
RUN curl -LsSf https://astral.sh/uv/0.9.7/install.sh | sh && uv --version
RUN curl -fsSL https://gh.io/copilot-install | bash && copilot --version

# Fill the caches from the locked dependency lists. The empty package lets uv also cache the
# project's build backend, so the Codespace's own sync needs no downloads at all.
COPY --chown=vscode:vscode pyproject.toml uv.lock /tmp/warm/
COPY --chown=vscode:vscode .devcontainer/website-preview/package.json .devcontainer/website-preview/package-lock.json /tmp/warm/website-preview/
RUN cd /tmp/warm \
    && mkdir -p src/vendor_assurance && touch src/vendor_assurance/__init__.py \
    && uv sync --locked --extra dev --extra web \
    && npm ci --prefix website-preview --ignore-scripts --no-audit --no-fund \
    && rm -rf /tmp/warm

USER root
