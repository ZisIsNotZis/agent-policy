#!/bin/sh
# One link, one source: point the harness's agent directory at this checkout.
#
# A child resolves agents from a project and from ~/.pi/agent/agents. The law lives
# in one checkout, so the whole directory is a link to it instead of a copy of each
# role file. A file with no frontmatter is skipped by the loader, which is how the
# root_manager view stays an entrance and not an agent.
#
#     sh tools/install-agents.sh            install or refresh the link
#     sh tools/install-agents.sh --check    fail if the link is missing or points elsewhere
set -e
root=$(cd "$(dirname "$0")/.." && pwd)
target="$HOME/.pi/agent/agents"
want="$root/agents"

if [ "$1" = "--check" ]; then
    if [ -L "$target" ] && [ "$(readlink -f "$target")" = "$(readlink -f "$want")" ]; then
        echo "ok: $target -> $want"
        exit 0
    fi
    echo "missing: $target -> $want"
    exit 1
fi

if [ -e "$target" ] && [ ! -L "$target" ]; then
    if [ -f "$target/settings.json" ]; then
        mv "$target/settings.json" "$HOME/.pi/agent/agents-settings.json"
        echo "moved the stray settings file to ~/.pi/agent/agents-settings.json"
    fi
    rm -rf "$target"
fi
mkdir -p "$(dirname "$target")"
ln -sfn "$want" "$target"
echo "ok: $target -> $want"
