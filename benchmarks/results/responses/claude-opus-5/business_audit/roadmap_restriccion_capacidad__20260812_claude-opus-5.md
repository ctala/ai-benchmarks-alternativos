# Claude Opus 5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 3.9 | quality: 4.0
- latency_total: 32.631s | tokens_per_second: 62.8
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

## Primero, tu presupuesto real (no el ideal)

| Concepto | Horas |
|---|---|
| Capacidad bruta: 8 sem × 5 días × 4h | 160h |
| Reserva por incidentes, soporte que se desborda, semanas malas (15%) | −25h |
| **Presupuesto construible** | **~135h** |

Tus estimaciones están en "semanas a tiempo completo" (40h). Traducidas a tu moneda real, y con el multiplicador honesto de fundador solo (×1.5, porque no hay nadie que absorba lo imprevisto):

| | Estimado | En horas reales | ¿Cabe en 135h? |
|---|---|---|---|
| A) Reescritura | 3 meses FT | ~480h → 720h | No. Es 4–5× tu trimestre |
| B) Alta / paso 2 | 1 sem FT | 40h → 60h | Sí |
| C) Panel métricas | 3 sem FT | 120h → 180h + bloqueada por A | No |
| D) 10 videos | 2 sem FT | 80h → 120h | Sí, pero se come todo lo demás |

B + D completos = 180h. No cabe. Algo se