# GPT-6 Luna — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-6-luna`
- success: True  | final: 6.09 | quality: 6.0
- latency_total: 18.784s | tokens_per_second: 97.5
- input_tokens: 241 | output_tokens: 1832

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

Tienes **~20 horas de construcción por semana** y **~160 horas en las 8 semanas**. No planificaría como si pudieras avanzar en todo a la vez.

| Prioridad | Decisión para este trimestre |
|---|---|
| **B. Arreglar el alta** | **Primero.** Dedica la primera semana a corregir el paso 2 y medir el embudo. El 60% de abandono es una pérdida concreta y el esfuerzo es pequeño. |
| **D. Videos** | **Después, con una condición.** Hazlos en las semanas 3–4 solo si ya tienes claro dónde se publicarán y cómo medirás si funcionan. Si no, prueba primero con 2–3 videos y decide según la respuesta; no des por hecho que hacer 10 equivale a obtener impacto. |
| **A. Reescritura** | **No la acometas este trimestre.** Tres meses a tiempo completo son unas 480 horas; a tus 20 horas semanales, serían aproximadamente **24 semanas**. Empezarla ahora probablemente dejaría una reescritura incompleta. |
| **C. Panel de métricas** | **Aplázalo.** Depende de A, así que no es un objetivo viable para estas 8 semanas. |

**Calendario propuesto**

- **Semana 1:** implementar B.
- **Semana 2:** revisar datos, resolver problemas del cambio y confirmar si mejora el alta.
- **Semanas 3–4:** D si hay un plan de distribución y una métrica de éxito; si no, piloto de 2–3 videos.
- **Semanas 5–8:** invertir el tiempo según lo aprendido: seguir mejorando el alta si sigue perdiendo usuarios, o ampliar contenido si el piloto demuestra tracción. Mantén margen para operación e imprevistos.

No llenaría el resto del trimestre con tareas solo para ocupar horas. Si quieres evaluar A, limita esa evaluación a unas pocas horas para identificar qué problema resolvería la reescritura y si existe una alternativa más pequeña; **no conviertas la evaluación en empezar el proyecto**.