#!/bin/sh
# One entry point: validate the corpus, then write the views.
set -e
cd "$(dirname "$0")/.."
exec python3 tools/schema.py
