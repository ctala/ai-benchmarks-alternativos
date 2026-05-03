#!/usr/bin/env bash
# commit_model_results.sh — commit incremental de resultados de un modelo terminado.
#
# Uso:
#   bash benchmarks/commit_model_results.sh <timestamp> <model_slug> [<msg>]
#
# Ejemplo:
#   bash benchmarks/commit_model_results.sh 20260503_074942 devstral-2 \
#       "Devstral 2 cerro NIAH-ES lite (45/45)"
#
# Qué hace:
# - Adds JSON principal del bench (benchmark_<timestamp>.json) si tiene cambios
# - Adds responses del modelo (responses/<timestamp>/<slug>__*.md)
# - Commit con mensaje + Co-Authored-By
# - Pull --no-rebase + push
#
# Por qué existe (politica del proyecto, 3 mayo 2026):
# Resultados deben ser publicos lo antes posible. En lugar de esperar a que
# termine todo el lote (~3-5h), commiteamos cada vez que un modelo termina
# sus tests para que esten disponibles en GitHub asap.

set -euo pipefail

if [ $# -lt 2 ]; then
    echo "Uso: $0 <timestamp> <model_slug> [<mensaje>]"
    echo "Ejemplo: $0 20260503_074942 devstral-2 'Devstral 2 cerro NIAH-ES (45/45)'"
    exit 1
fi

TS="$1"
SLUG="$2"
MSG="${3:-data: $SLUG resultados ($TS)}"

cd "$(dirname "$0")/.."

JSON="benchmarks/results/benchmark_${TS}.json"
RESP_DIR="benchmarks/results/responses/${TS}"
RESP_PATTERN="${RESP_DIR}/${SLUG}__*.md"

# Validar que existen
if [ ! -f "$JSON" ]; then
    echo "WARN: $JSON no existe (puede que aun no se haya creado)"
fi

# Add JSON
[ -f "$JSON" ] && git add "$JSON"

# Add responses del modelo (si hay)
ls -1 $RESP_PATTERN 2>/dev/null | head -100 | xargs -I {} git add {}

# Verificar si hay algo staged
if git diff --staged --quiet; then
    echo "Sin cambios staged para $SLUG ($TS). Nada que commitear."
    exit 0
fi

# Commit
git commit -m "$(cat <<EOF
$MSG

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)" >/dev/null 2>&1

echo "OK commit: $MSG"

# Pull-merge (no rebase, preferencia del usuario)
if ! git pull --no-rebase origin main >/dev/null 2>&1; then
    echo "WARN: pull falló (verificar conflictos)"
fi

# Push
if git push origin main >/dev/null 2>&1; then
    echo "OK pushed a origin/main"
else
    echo "WARN: push falló"
fi
