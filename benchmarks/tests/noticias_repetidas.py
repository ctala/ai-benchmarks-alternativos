"""
Suite noticias_repetidas — Detectar notas que cuentan el mismo hecho.

PENDIENTE DE IMPLEMENTACIÓN: requiere corpus de Eco y licencia CC BY 4.0.

Diseño:
- 6 tests con lotes de ~43 notas del 8-9-oct-2026
- Entrada: lista numerada (título + primeros 300 caracteres)
- Salida: JSON {grupos: [[id, id, ...], ...]}
- Métrica: F1 por pares (precisión + cobertura)
- Tokens por test: ~5.000

Verdad objetiva: backtest/gt_dedup_8_9oct.json (23 grupos, 36 sobrantes, 10 grises).
Baseline: regla léxica 13.9%, regla híbrida embeddings 88.9%.
Un modelo solo vale la pena si supera al baseline gratis.

FUENTE: /workspace/uploads/benchmark-pack-noticias_e470.md § 4.2
BLOQUEANTE: corpus de Eco + gt_dedup + aprobación de licencia CC BY
"""

TESTS = [
    # Placeholder - requiere datos reales de Eco
]
