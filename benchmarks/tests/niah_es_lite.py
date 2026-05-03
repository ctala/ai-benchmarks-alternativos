"""
Suite niah_es_lite — NIAH-ES sin contexto 256K.

Variante "lite" para correr más modelos sin gastar en context 256K que es
el más caro (~30-50% del costo total del lote v2). En 4/2026 verificamos
que solo 3 modelos (GPT-4.1, Gemini 3.1 Pro, Claude Opus 4.7) procesan 256K
sin error 400 — el resto cap por su provider. Para modelos cheap/cap,
correr solo 4K-64K es suficiente para evaluar retrieval en español.

# Diseño

- 5 needles × 3 contextos (4K, 16K, 64K) × 3 posiciones (25%, 50%, 75%) = 45 tests

Reusa needles, corpus, scoring del módulo niah_es.
"""

from benchmarks.tests.niah_es import (
    NEEDLES,
    POSITIONS,
    _build_test,
    _CORPUS,  # noqa: F401
)

# Solo 4K-64K, sin 256K
CONTEXT_SIZES = [4000, 16000, 64000]

TESTS = []
for needle_idx in range(len(NEEDLES)):
    for ctx in CONTEXT_SIZES:
        for pos in POSITIONS:
            TESTS.append(_build_test(needle_idx, ctx, pos))
