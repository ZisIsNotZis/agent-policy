#!/bin/sh
# One link, one source: point the harness's agent directory at this checkout.
#
# A child resolves agents from a project and from ~/.pi/agent/agents. The law lives
# in one checkout, so the whole directory is a link to it instead of a copy of each
# role file. The manager is also the default agent, so its body is rendered as
# AGENTS.md at the root and linked as the agent directory's context file.
#
#     sh tools/install-agents.sh            install or refresh the link
#     sh tools/install-agents.sh --check    fail if the link is missing or points elsewhere
set -e
root=$(cd "$(dirname "$0")/.." && pwd)
target="$HOME/.pi/agent/agents"
want="$root/agents"

if [ "$1" = "--check" ]; then
    fail=0
    if [ ! -L "$target" ] || [ "$(readlink -f "$target")" != "$(readlink -f "$want")" ]; then
        echo "missing: $target -> $want"
        fail=1
    fi
    if [ ! -L "$HOME/.pi/agent/AGENTS.md" ] || [ "$(readlink -f "$HOME/.pi/agent/AGENTS.md")" != "$(readlink -f "$root/AGENTS.md")" ]; then
        echo "missing: $HOME/.pi/agent/AGENTS.md -> $root/AGENTS.md"
        fail=1
    fi
    if [ "$(git -C "$root" config core.hooksPath)" != ".githooks" ]; then
        echo "missing: core.hooksPath is not .githooks"
        fail=1
    fi
    [ "$fail" = 0 ] && echo "ok: $target -> $want, AGENTS.md linked, core.hooksPath = .githooks"
    exit "$fail"
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
if [ -e "$HOME/.pi/agent/AGENTS.md" ] && [ ! -L "$HOME/.pi/agent/AGENTS.md" ]; then
    mv "$HOME/.pi/agent/AGENTS.md" "$HOME/.pi/agent/AGENTS.md.local"
    echo "moved the stray context file to ~/.pi/agent/AGENTS.md.local"
fi
ln -sfn "$root/AGENTS.md" "$HOME/.pi/agent/AGENTS.md"
git -C "$root" config core.hooksPath .githooks
echo "ok: $target -> $want, core.hooksPath = .githooks"
