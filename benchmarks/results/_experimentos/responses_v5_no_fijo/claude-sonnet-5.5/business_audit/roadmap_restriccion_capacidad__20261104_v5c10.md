# Claude Sonnet 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.05 | quality: 8.0
- latency_total: 15.867s | tokens_per_second: 111.7
- input_tokens: 420 | output_tokens: 1772

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

# Plan del trimestre

## La cuenta de capacidad
- 4h/día × 5 días × 8 semanas = **~160h construibles**
- Si "tiempo completo" son ~40h/semana, tus estimaciones en horas son:
  - **A:** ~480h. Es 3 veces todo tu trimestre.
  - **B:** ~40h
  - **C:** ~120h
  - **D:** ~80h

A no cabe, y C depende de A, así que tampoco. B + D suman ~120h, lo que deja ~40h (25%) de colchón. Con un solo humano, soporte incluido, ese colchón lo vas a necesitar.

## Orden

| Semanas | Qué | Por qué |
|---|---|---|
| 1-2 | **B: arreglar el alta** | Mayor impacto con menor esfuerzo. Perder al 60% en el paso 2 es una fuga que hace peor todo lo demás. |
| 3-6 | **D: videos** (ritmo ~2-3 por semana) | Va después de B, porque no tiene sentido llevar tráfico a un embudo que pierde al 60%. |
| 7-8 | **Colchón** + medir B + terminar lo que se haya retrasado | Aquí se te irán los imprevistos. Si no pasa nada, adelanta videos o ataca el soporte. |

**B va primero y sola.** Mide la conversión del paso 2 antes y después. Si sube de 40% a 60%, has mejorado el ROI de todo el resto.

## Lo que queda fuera
- **A (reescritura):** no este trimestre. Un fundador solo, con 2h diarias de soporte, reescribiendo durante ~6 meses reales sin lanzar nada, es un riesgo enorme. Antes de plantearla de nuevo, responde: *¿qué duele concretamente del stack actual?* Si es algo acotado, probablemente se resuelve con refactors incrementales sin parar el producto.
- **C (panel de métricas):** queda fuera por la dependencia con A. Pregúntate si esa dependencia es real o solo cómoda. Una versión mínima (un email semanal con 3-4 métricas, o una página simple) quizá no requiera A y cueste unas 10-15h. Si tus clientes lo piden, puede entrar en el colchón.

## Palanca extra: las 2h de soporte
Recuperar 30 minutos al día te da ~20h más en el trimestre. Un FAQ, respuestas guardadas o arreglar las 2-3 causas que generan más tickets rinde más que muchas features. Además, el arreglo de B probablemente reduzca preguntas de soporte.

## Riesgos
- **B se alarga:** si pasa de 2 semanas, recorta D a 6-7 videos, no a 10.
- **D se come el tiempo:** graba en lote (un día, varios videos) y fija un tope por video.

¿Quieres que desglosemos B en tareas concretas para la semana 1?