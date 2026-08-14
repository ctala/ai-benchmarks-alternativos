#!/bin/bash
# Formato de Harbor: los tests corren y el resultado se escribe en
# /logs/verifier/reward.txt (1 = pasó todo, 0 = falló algo) + un CTRF con el detalle
# por test. Sin ese archivo, el job termina en RewardFileNotFoundError.
set +e
mkdir -p /logs/verifier

pip install -q pytest pytest-json-ctrf 2>/dev/null

python -m pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py -rA
RC=$?

# Puntaje PARCIAL, no binario: 8 criterios independientes. Un agente puede acertar el
# servicio y errar la banda. Reportar solo 0/1 tiraría el gradiente que hace útil esta
# tarea — es lo que Cristian pidió cuando dijo que una prueba binaria no sirve de mucho.
if [ -f /logs/verifier/ctrf.json ]; then
  python - <<'PY'
import json
d = json.load(open("/logs/verifier/ctrf.json"))
s = d["results"]["summary"]
total = s.get("tests", 0) or 1
passed = s.get("passed", 0)
open("/logs/verifier/reward.txt", "w").write(str(round(passed / total, 4)))
print(f"reward = {passed}/{total} = {passed/total:.3f}")
PY
else
  echo "$([ $RC -eq 0 ] && echo 1 || echo 0)" > /logs/verifier/reward.txt
fi
