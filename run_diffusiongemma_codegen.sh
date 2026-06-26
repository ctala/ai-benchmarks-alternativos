#!/usr/bin/env bash
# Script de una línea para correr DiffusionGemma en la suite code_generation.
# Uso: ./run_diffusiongemma_codegen.sh

cd "$(dirname "$0")" || exit 1
.venv/bin/python benchmarks/runner.py --models local-diffusiongemma-26b --tests code_generation --quick --judge "$@"
