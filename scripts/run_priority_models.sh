#!/usr/bin/env bash
# scripts/run_priority_models.sh
# Corre los modelos prioritarios para la siguiente versión del benchmark.
# Uso: ./scripts/run_priority_models.sh
set -euo pipefail
cd "$(dirname "$0")/.."

PYTHON=".venv/bin/python"
RUNNER="benchmarks/runner.py"

# 1) Grok 4.3 — OpenRouter (~$70 con NIAH, ~$2 sin NIAH)
echo "▶ Corriendo Grok 4.3 completo..."
$PYTHON $RUNNER --models grok-4.3

# 2) Nemotron 3 Ultra 550B — NVIDIA NIM (gratis con rate limit)
# Requiere NVIDIA_NIM_API_KEY en .env
echo "▶ Corriendo Nemotron 3 Ultra 550B completo..."
$PYTHON $RUNNER --models nim-nemotron-3-ultra-550b

echo "✅ Benchmarks prioritarios completados."
