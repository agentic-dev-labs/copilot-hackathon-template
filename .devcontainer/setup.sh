#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"
export UV_NATIVE_TLS="${UV_NATIVE_TLS:-true}"
if ! uv sync --locked --extra dev --extra web; then
	printf '\nDependency setup failed; TLS verification remains enabled.\n' >&2
	printf 'Run: python -m rehearsal.network --fresh-install --nuget\n' >&2
	printf 'See rehearsal/README.md for package-host and approved certificate guidance.\n' >&2
	exit 1
fi