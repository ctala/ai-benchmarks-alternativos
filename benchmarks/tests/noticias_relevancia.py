"""
Suite noticias_relevancia — Puntuar y filtrar notas según criterio editorial.

PENDIENTE DE IMPLEMENTACIÓN: requiere corpus de Eco y licencia CC BY 4.0.

Diseño:
- 6 tests, cada uno con 10 notas del 26-sep al 10-oct-2026
- Entrada: criterio editorial + título + primeros 1.500 caracteres por nota
- Salida: JSON {id, decision: KEEP|SKIP, categoria, puntaje 1-10}
- Métrica: decisiones correctas / notas enviadas (0-10)
- Tokens por test: ~5.800

Verdad objetiva: etiqueta humana (40 KEEP, 20 SKIP).
Referencia: GTA 6 (115391), Gears of War (114806), iPhone 17 Pro (114721) como
candidatos SKIP que se publicaron.

FUENTE: /workspace/uploads/benchmark-pack-noticias_e470.md § 4.1
BLOQUEANTE: corpus de Eco + aprobación de licencia CC BY
"""

TESTS = [
    # Placeholder - requiere datos reales de Eco
]
