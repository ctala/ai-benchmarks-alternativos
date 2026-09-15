#!/bin/bash
# Estudio de effort por tarea (14-sep-2026) — FUERA del índice.
# 4 modelos de 4 laboratorios con niveles de effort declarados × {low, high} × suites del índice.
# El default de cada modelo ya está medido en el histórico: es la línea base, no se re-corre.
# Idempotente: cada combinación tiene su resume de nombre FIJO; relanzar retoma sin re-pagar.
cd /Users/cristiantala/Playground/Estrategias/benchmarks || exit 1
DIR=benchmarks/results/_experimentos/effort_por_tarea_202609
LOG="${LOG:-${TMPDIR:-/tmp}/estudio_effort_202609}"   # los logs no van al repo
mkdir -p "$DIR" "$LOG"
SUITES=$(.venv/bin/python -c "import sys; sys.path.insert(0,'benchmarks'); from suites import del_indice; print(' '.join(sorted(del_indice())))")
MODELOS="gpt-5.6-luna glm-5.3-flash deepseek-v4-flash-0731 muse-glimmer-30b"

for m in $MODELOS; do
  for lvl in low high; do
    f="$DIR/${m}__${lvl}.json"
    if [ ! -f "$f" ]; then
      .venv/bin/python -c "import json; json.dump({'metadata': {'timestamp': 'estudio_effort_${lvl}', 'partial': True, 'experimento': 'effort por tarea (14-sep-2026), fuera del indice', 'effort_pedido': '${lvl}'}, 'results': []}, open('$f', 'w'))"
    fi
    (
      for intento in 1 2 3 4 5 6; do
        BENCH_REASONING_EFFORT=$lvl .venv/bin/python benchmarks/runner.py --quick --judge --judge-model phi4-or \
          --models "$m" --tests $SUITES --resume "$f" >> "$LOG/${m}__${lvl}.log" 2>&1 && break
        echo "[$(date '+%H:%M:%S')] intento $intento terminó con error, reintento en 20 s" >> "$LOG/${m}__${lvl}.log"
        sleep 20
      done
    ) &
  done
done
wait
echo "ESTUDIO TERMINADO $(date)" >> "$LOG/fin.txt"
