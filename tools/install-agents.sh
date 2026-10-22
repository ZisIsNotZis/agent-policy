#!/bin/sh
# Link the role definitions where a child resolves them.
#
# A child launched with cwd inside a project resolves agents from that project and
# from ~/.pi/agent/agents. The law lives in one checkout, so link it there instead
# of copying it. Idempotent.
#
#     sh tools/install-agents.sh            install or refresh the links
#     sh tools/install-agents.sh --check    fail if a link is missing or points elsewhere
set -e
root=$(cd "$(dirname "$0")/.." && pwd)
target="$HOME/.pi/agent/agents"
roles="manager worker researcher reviewer policy_worker"

if [ "$1" = "--check" ]; then
    fail=0
    for role in $roles; do
        link="$target/$role.md"
        want="$root/agents/$role.md"
        if [ ! -L "$link" ] || [ "$(readlink -f "$link")" != "$(readlink -f "$want")" ]; then
            echo "missing: $link -> $want"
            fail=1
        fi
    done
    [ "$fail" = 0 ] && echo "ok: $target"
    exit "$fail"
fi

mkdir -p "$target"
for role in $roles; do
    ln -sfn "$root/agents/$role.md" "$target/$role.md"
done
echo "ok: $target -> $root/agents"
