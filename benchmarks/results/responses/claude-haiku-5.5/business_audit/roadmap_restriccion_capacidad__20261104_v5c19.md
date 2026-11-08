# Claude Haiku 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 12.079s | tokens_per_second: 183.0
- input_tokens: 420 | output_tokens: 2211

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

## Orden del trimestre

1. **B: arreglar el alta** (semanas 1-2)
2. **D: grabar los videos** (semanas 3-4)
3. **Semanas 5-8: spike de A, no la reescritura.** Decidir si la reescritura hace falta y planificarla para el siguiente trimestre.
4. **C: fuera de este trimestre.**

## Por qué

**Capacidad.** Con ~4h/día reales y 5 días a la semana, tienes unas 160h en 8 semanas. Descontando un 20% de colchón para imprevistos, quedan unas 128h útiles.

- **B (~1 semana ≈ 20h):** cabe de sobra, y es el mayor impacto por hora. Perder al 60% en el paso 2 significa que cada visitante que consigues vale la mitad. Arreglarlo amplifica todo lo demás.
- **D (~2 semanas ≈ 40h):** cabe. Hazlo después de B, para que los videos lleven a un flujo que ya funciona.
- **A (~3 meses a tiempo completo):** no cabe. Aunque "tiempo completo" signifique 6h/día, son unas 13 semanas, más del doble del trimestre. A tu ritmo real serían unos 6 meses. Reescribir la plataforma en un trimestre no es una opción.
- **C (~3 semanas) depende de A:** como A no termina, C tampoco. Intentar hacerlo antes de A sería construir sobre algo que vas a cambiar.

**Sobre las semanas 5-8.** Tienes unas 80-100h. Úsalas así:

- **Spike de A (~2 semanas, ~40h):** ¿qué te frena realmente? Si la respuesta es "la velocidad de desarrollo en el stack actual", identifica los 2-3 cuellos de botella concretos (despliegues, tests, una parte del código) y arréglalos. Quizá eso dé el 70% del beneficio por el 10% del coste. Si tras el spike sigue haciendo falta la reescritura, planifícala con una estimación real para el próximo trimestre.
- **Reducir el soporte (~2h/día que no puedes delegar hoy):** si el soporte consume la mitad de tu capacidad, cualquier plan se retrasa. Dedica parte de estas semanas a documentar las preguntas frecuentes, automatizar respuestas o cerrar fuentes recurrentes de tickets. Cada hora que liberes multiplica tu capacidad para el próximo trimestre.

## Preguntas que te haría antes de cerrar el plan

- **¿C depende de verdad de A?** Si el panel solo necesita leer datos que ya tienes, quizá puedes hacer una versión mínima (una página con exportación o métricas básicas) en el stack actual en 1-2 semanas. Si tus clientes lo están pidiendo, esa es la validación que necesitas. Si la dependencia es real, dejalo para el próximo trimestre.
- **¿Qué métrica de B vas a mirar?** Antes de tocar nada, anota la tasa actual de paso 2. Después del arreglo, compara al menos 2 semanas de datos antes de decidir si D sigue siendo prioritario o si conviene invertir más en el funnel.