"""
Suite noticias_verificacion — Verificar datos contra fuente.

PENDIENTE DE IMPLEMENTACIÓN: requiere notas de Eco y afirmaciones, licencia CC BY 4.0.

Diseño:
- 8 tests con 12 afirmaciones cada uno (96 total)
- Entrada: prompt verificación + nota fuente (~7.400 chars) + 12 afirmaciones
- Salida: JSON {id, veredicto: RESPALDA|CONTRADICE|SIN_RESPALDO, razon}
- Tokens por test: ~4.000

Composición de las 12 afirmaciones por test:
- 4 copiadas literalmente de la nota
- 3 parafraseadas
- 3 con cifra alterada sutilmente ("más de mil millones" → "935 millones")
- 2 inventadas pero verosímiles (empresas/episodios no en fuente)

Métrica: veredictos correctos / afirmaciones. Sin veredicto = error.
Reportar aparte: "dejó pasar inventado" vs "bloqueó respaldado".

Prompt: reutiliza verificar_claims_lote.py (4.218 chars, ya público).
Razón: verificar_claims_lote tiene 53% de runs perfectos (cerca de saturación).
Si esta suite también satura en validate_suite, se descarta.

FUENTE: /workspace/uploads/benchmark-pack-noticias_e470.md § 4.4
BLOQUEANTE: 8 notas + 96 afirmaciones construidas + aprobación licencia CC BY
"""

TESTS = [
    # Placeholder - requiere notas y afirmaciones construidas
]
