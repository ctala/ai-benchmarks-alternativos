"""
Suite noticias_pauta — Redactar con la pauta editorial de Eco.

PENDIENTE DE IMPLEMENTACIÓN: requiere fichas de hechos y licencia CC BY 4.0.

Diseño:
- 12 tests: 3 rondas LATAM, 3 producto IA, 3 regional, 3 comunicados
- Entrada: pauta (~2.500 chars) + ficha de hechos (hasta 3.000 chars)
- Salida: nota 600-900 palabras + título
- Tokens por test: ~1.600

Puntuación (pesos ajustables con validate_suite):
- Forma 40%: sin voseo, título ≤60 chars, sin chino, sin cierres prohibidos
- Fidelidad 30%: cada cifra de la nota está en la ficha
- Utilidad 30%: 3 preguntas al verificador Phi-4
  (a) ¿Nombra decisión/acción concreta para founder?
  (b) ¿Cierre trae dato específico, no consejo genérico?
  (c) ¿Título nombra al protagonista?

Pauta: español neutro, utilidad concreta, sin "¿Qué significa esto para tu startup?",
título ≤60 chars con protagonista.

FUENTE: /workspace/uploads/benchmark-pack-noticias_e470.md § 4.3
BLOQUEANTE: fichas de hechos (12) + aprobación de licencia CC BY
"""

TESTS = [
    # Placeholder - requiere fichas de hechos reales
]
