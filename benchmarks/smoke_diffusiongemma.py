#!/usr/bin/env python3
"""
Smoke test para DiffusionGemma via DiffusionGemmaProvider.

Uso:
    python benchmarks/smoke_diffusiongemma.py

Lee la config del modelo `local-diffusiongemma-26b` desde benchmarks.config
y corre un par de prompts de prueba.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.config import OLLAMA_MODELS
from providers.adapters import DiffusionGemmaProvider


def main():
    cfg = OLLAMA_MODELS["local-diffusiongemma-26b"]
    provider = DiffusionGemmaProvider(
        "diffusion_cli",
        bin_path=cfg["bin_path"],
        gguf_path=cfg["gguf_path"],
        ngl=cfg.get("ngl", 99),
        ctx_size=cfg.get("ctx_size", 8192),
        seed=cfg.get("seed", 42),
    )

    tests = [
        {
            "name": "smoke_coding",
            "messages": [
                {"role": "system", "content": "Sos un experto en Python. Respondé solo con el código."},
                {"role": "user", "content": "Escribí una función en Python que reciba una lista de números y devuelva la mediana."},
            ],
        },
        {
            "name": "smoke_razonamiento",
            "messages": [
                {"role": "user", "content": "Un tren sale de Santiago a 100 km/h y otro sale de Valparaíso a 80 km/h. La distancia es 120 km. ¿Dónde se cruzan?"},
            ],
        },
    ]

    for test in tests:
        print(f"\n{'='*70}")
        print(f"Test: {test['name']}")
        print(f"{'='*70}")
        result = provider.chat(
            model=cfg["id"],
            messages=test["messages"],
            max_tokens=1024,
            timeout=300,
        )
        print(f"success: {result.success}")
        print(f"latency_total: {result.latency_total:.2f}s")
        print(f"tokens_per_second: {result.tokens_per_second:.2f}")
        print(f"output_tokens: {result.output_tokens}")
        if result.error:
            print(f"error: {result.error}")
        print(f"response:\n{result.response[:1000]}")


if __name__ == "__main__":
    main()
