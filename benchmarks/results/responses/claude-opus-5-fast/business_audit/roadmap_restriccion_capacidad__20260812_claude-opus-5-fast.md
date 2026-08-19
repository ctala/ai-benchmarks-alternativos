# Claude Opus 5 Fast — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 3.91 | quality: 4.0
- latency_total: 10.896s | tokens_per_second: 188.0
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

## Primero, la aritmética — porque decide casi todo

Tu presupuesto real del trimestre:

**4h/día × 5 días × 8 semanas = 160h brutas.** Descontando desbordes, contexto y el fuego imprevisto que siempre aparece, lo comprometible son **~120h**. Ese es el número con el que hay que planificar, no 160.

Ahora, una pregunta que cambia el plan: **cuando dijiste "1 semana", "3 semanas", "2 semanas", ¿eran semanas tuyas de 20h o semanas de 40h?** Casi todo el mundo estima en semanas ideales de tiempo completo. Voy a asumir eso (es lo conservador). Con esa lectura:

| | Estimado | Horas | Semanas tuyas reales |
|---|---|---|---|
| A | 3 meses FT | ~480h | **24 semanas** |
| B | 1 semana | 40h | 2 semanas |
| C | 3 semanas | 120h | 6 semanas (+ bloqueada por A) |
| D | 2 semanas | 80h | 4 semanas |

## Qué muere hoy, sin negociación

**A queda fuera.** No es una opinión de prioridades, es que no cabe: necesita tres trimestres como este. Empezarla significa llegar a la semana 8 con una plataforma a medio migrar, la vieja sin tocar y cero resultados. Es el peor estado posible.

**C queda fuera por arrast