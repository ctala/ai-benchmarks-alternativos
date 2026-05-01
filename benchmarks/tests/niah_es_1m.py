"""
Suite niah_es_1m — NIAH-ES con contexto 1,000,000 tokens.

Variante específica para validar el effective context window real de modelos
que declaran 1M+ tokens (Gemini 3.x Pro/Flash, GPT-4.1, DeepSeek V4 Flash NIM,
Llama 4 Scout Groq preview).

Por qué módulo separado:
- niah_es.py corre el grid v2 (4K-256K) sin tocar 1M (caro, lento)
- niah_es_1m.py es opcional, lo corremos solo cuando queremos validar
  modelos premium long-context

Reusa needles, corpus, scoring del módulo niah_es. Solo cambia el contexto.

# Diseño v3

- 5 needles × 1 contexto (1M) × 3 posiciones = 15 tests por modelo
- Modelos elegibles: Gemini 3.1 Pro, GPT-4.1, DeepSeek V4 Flash NIM,
  Llama 4 Scout 17B Groq (probable cap)
- Costo estimado: ~$0.5-2.5 por test (1M tokens input). Total $50-60 para
  3-4 modelos × 15 tests.

# Hipótesis a validar

1. Effective context << declared context. Hipótesis: solo 1-2 modelos
   procesarán 1M sin error 400.
2. Score degrada >50% vs 256K. Hipótesis: scores 3-4 promedio en 1M.
3. Lost-in-the-middle reaparece a 1M (lo que NO vimos en 4K-64K).
"""

from benchmarks.tests.niah_es import (
    NEEDLES,
    POSITIONS,
    _build_test,
    _CORPUS,  # noqa: F401 — para asegurar que el corpus está cargado
)

# Solo contexto 1M en este módulo
CONTEXT_SIZES = [1_000_000]

# Genera 15 tests: 5 needles × 1 ctx × 3 pos
TESTS = []
for needle_idx in range(len(NEEDLES)):
    for ctx in CONTEXT_SIZES:
        for pos in POSITIONS:
            TESTS.append(_build_test(needle_idx, ctx, pos))
