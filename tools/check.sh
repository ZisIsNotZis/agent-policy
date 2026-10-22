#!/bin/sh
# One entry point for every check this repository makes.
set -e
cd "$(dirname "$0")/.."
python3 tools/law.py --check
python3 tools/build.py --check
python3 tools/contract.py --self-test
python3 tools/cases.py
python3 tools/counts.py
python3 tools/dupes.py
