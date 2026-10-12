#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"
export UV_NATIVE_TLS="${UV_NATIVE_TLS:-true}"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

EDITOR_RELOAD_REQUIRED=false

ensure_editor_extension() {
	local extension="$1"
	if code --list-extensions | grep -Fxiq "$extension"; then
		return
	fi
	code --install-extension "$extension"
	EDITOR_RELOAD_REQUIRED=true
	printf 'Installed editor extension %s.\n' "$extension"
}

case "${1:-core}" in
	core)
		if ! uv sync --locked --extra dev --extra web; then
			printf '\nDependency setup failed; TLS verification remains enabled.\n' >&2
			printf 'Facilitator: run python -m rehearsal.network --fresh-install\n' >&2
			printf 'See rehearsal/README.md for package-host and approved certificate guidance.\n' >&2
			exit 1
		fi
		npm ci --prefix .devcontainer/website-preview --ignore-scripts --no-audit --no-fund
		;;
	preview)
		if ! command -v code >/dev/null 2>&1; then
			printf 'Preview helper installation needs an attached Codespaces editor.\n' >&2
			exit 1
		fi
		ensure_editor_extension "ms-python.python"
		ensure_editor_extension "ms-python.vscode-python-envs"
		ensure_editor_extension "charliermarsh.ruff"
		VERSION="$(node -p 'require("./.devcontainer/website-preview/package.json").version')"
		if code --list-extensions --show-versions | grep -Fxq "workshop-local.workshop-site-preview@$VERSION"; then
			printf 'Workshop preview helper %s is already prepared.\n' "$VERSION"
		else
			mkdir -p .workshop-preview
			pushd .devcontainer/website-preview >/dev/null
			node_modules/.bin/vsce package --no-dependencies --allow-missing-repository --skip-license --out "$ROOT/.workshop-preview/workshop-site-preview.vsix"
			popd >/dev/null
			code --install-extension "$ROOT/.workshop-preview/workshop-site-preview.vsix" --force
			printf 'Preview helper installed. Existing editor sessions may need one Reload Window.\n'
		fi
		if "$EDITOR_RELOAD_REQUIRED"; then
			printf 'Run Developer: Reload Window once so Ruff can use the project environment.\n'
		fi
		;;
	cli)
		curl -fsSL https://gh.io/copilot-install | bash
		copilot --version
		;;
	browser)
		npm ci --prefix .devcontainer/browser --ignore-scripts --no-audit --no-fund
		node .devcontainer/browser/node_modules/playwright/cli.js install --with-deps chromium
		bash .devcontainer/mcp.sh check-browser
		;;
	research)
		uv venv --allow-existing .venv-research --python 3.12
		uv pip install --python .venv-research/bin/python --requirement .devcontainer/research-requirements.txt
		bash .devcontainer/mcp.sh check-research
		;;
	*)
		printf 'Usage: bash .devcontainer/setup.sh [core|preview|cli|browser|research]\n' >&2
		exit 2
		;;
esac