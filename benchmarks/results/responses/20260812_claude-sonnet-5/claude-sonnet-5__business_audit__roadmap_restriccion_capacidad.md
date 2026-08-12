# Claude Sonnet 5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 4.08 | quality: 4.0
- latency_total: 26.31s | tokens_per_second: 77.8
- input_tokens: 418 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

# Orden del trimestre

**Capacidad real disponible: 160 horas** (4h/día × 5 días × 8 semanas). Ese es tu presupuesto real, no las 8 semanas en abstracto.

## Traduciendo los esfuerzos a tu realidad

Las estimaciones están dadas en "tiempo completo" (40h/semana). Convertidas a horas absolutas de trabajo:

| Iniciativa | Esfuerzo nominal | Horas reales | % del presupuesto trimestral |
|---|---|---|---|
| B | 1 semana FT | 40h | 25% |
| D | 2 semanas FT | 80h | 50% |
| C | 3 semanas FT | 120h | 75% (pero bloqueada) |
| A | 3 meses FT | 480h | **300%** |

**A no cabe en el trimestre bajo ning