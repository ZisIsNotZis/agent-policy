#!/bin/sh
# One entry point: fail if a view on disk differs from what the law renders.
set -e
cd "$(dirname "$0")/.."
exec python3 tools/render.py --check
