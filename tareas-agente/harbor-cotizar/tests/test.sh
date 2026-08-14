#!/bin/bash
set -e
pip install -q pytest 2>/dev/null || true
python -m pytest /app/tests/test_outputs.py -rA --tb=short
