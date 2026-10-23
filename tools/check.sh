#!/bin/sh
# One entry point: check the law and write the views.
set -e
cd "$(dirname "$0")/.."
exec python3 tools/policy.py
