#!/bin/bash
set +e
mkdir -p /logs/verifier
pip install -q pytest==8.4.1 pytest-json-ctrf==0.3.5 2>/dev/null
python -m pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py -rA
RC=$?
if [ -f /logs/verifier/ctrf.json ]; then
  python - <<'PY'
import json
s = json.load(open("/logs/verifier/ctrf.json"))["results"]["summary"]
t = s.get("tests", 0) or 1
open("/logs/verifier/reward.txt", "w").write(str(round(s.get("passed", 0) / t, 4)))
PY
else
  echo "$([ $RC -eq 0 ] && echo 1 || echo 0)" > /logs/verifier/reward.txt
fi
