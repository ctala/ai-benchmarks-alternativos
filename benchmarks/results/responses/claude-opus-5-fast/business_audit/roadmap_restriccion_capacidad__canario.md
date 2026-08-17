# Claude Opus 5 Fast — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 2.51 | quality: 2.0
- latency_total: 11.161s | tokens_per_second: 183.5
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

## Primero, la aritmética que cambia la conversación

Tus estimaciones están en "semanas", pero casi seguro las pensaste en semanas de 40h. Tu semana real es de 20h — y planificar a 20h es planificar sin margen. Planifico a **16h/semana**, con 4h de colchón para incendios.

**Capacidad real del trimestre: ~128h.**

| Iniciativa | Tu estimación | En horas (FT) | En *tus* semanas |
|---|---|---|---|
| A) Reescritura | 3 meses | ~480h | 30 semanas (y con el impuesto de optimismo típico de reescrituras, ~50) |
| B) Alta | 1 semana | 40h | 2,5 semanas |
| C) Panel | 3 semanas | 120h | 7,5 semanas |
| D) Videos | 2 semanas | 80h | 5 semanas |

**B + C + D = 240h contra 128h disponibles.** Incluso eliminando A por completo, no entra. Así que el problema no es ordenar: es recortar alcance. Ordenar sin recortar te deja en la semana 8 con tres cosas al 60%.

## Las decisiones

**A se cae del trimestre. Explícitamente, no "más adelante".** 