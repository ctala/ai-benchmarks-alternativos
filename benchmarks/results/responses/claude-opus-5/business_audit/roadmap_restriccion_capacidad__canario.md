# Claude Opus 5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.7 | quality: 8.0
- latency_total: 32.943s | tokens_per_second: 62.2
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

## Primero, la aritmética de capacidad

Tus estimaciones están en "semanas a tiempo completo" (40h). Tu semana real son 20h. El factor de conversión es 2x, y para fundador solo (sin revisión de código, con interrupciones de soporte) es más honesto 2.2x.

| | Estimado | Real en tu calendario | Cabe en 8 semanas |
|---|---|---|---|
| A) Reescritura | 3 meses FT (~480h) | ~24 semanas | No |
| B) Alta | 1 semana (40h) | ~2 semanas | Sí |
| C) Panel | 3 semanas (120h) | ~6 semanas + bloqueado por A | No |
| D) 10 videos | 2 semanas (80h) | ~4 semanas | Sí, pero se come la mitad del trimestre |

Capacidad total: 8 × 20h = **160h**. Planificable de verdad: **~128h** (20% de reserva para picos de soporte, un día malo, un cliente enojado). Lo que pides suma ~680h. Sobras 5x.

## El orden

**Semanas 1–2 — B, el flujo de alta (30h)**

No es negociable y va primero. Perder 60% en el paso 2 significa que todo lo demás que hagas rinde 40%. Hacer D antes que B es meter agua en un balde agujereado: pagás por tráfico que se cae solo.

Medio día antes de tocar código: instrumentá el paso 2 para saber *dónde* se van (¿campo específico? ¿validación? ¿pide tarjeta? ¿tiempo de carga?). Arreglar a ciegas es el error clásico acá.

**Semanas 3–4 — B, segunda pasada (20h)**

Esto es lo que casi nadie reserva. Un primer arreglo raramente lleva 60% a 20%; lleva 60% a 40%. Dejá espacio explícito para leer los datos de dos semanas e iterar. Si a la semana 3 el número ya bajó lo suficiente, liberás estas horas y las mandás abajo. Pero reservalas.

**Semanas 5–6 — D recortado: 5 videos, no 10 (30h)**

Dos ajustes. Uno: la mitad del alcance. 5 videos publicados enseñan lo mismo sobre si el canal funciona que 10, y con datos decidís en el próximo trimestre si vale escalar. Dos: grab