# Claude Sonnet 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.03 | quality: 8.0
- latency_total: 18.674s | tokens_per_second: 109.1
- input_tokens: 420 | output_tokens: 2037

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

## Cuentas de capacidad
- Capacidad real: 4h × 5 días × 8 semanas = **~160h**.
- Asumo que "1 semana a tiempo completo" son ~30h enfocadas (6h × 5). Si tus estimaciones eran de 40h/semana, el panorama es peor.
- Con las estimaciones: A ≈ 360h, C ≈ 90h, D ≈ 60h, B ≈ 30h.
- Las estimaciones suelen quedarse cortas, así que planifico con ~20-25% de colchón: **~125h útiles**.

**A no cabe ni de lejos** (más del doble de tu capacidad total). Y como C depende de A, **C tampoco cabe**.

## Plan

| Semanas | Qué | Horas |
|---|---|---|
| 1 – 2 | **B: arreglar el alta** (paso 2) | ~30h |
| 3 | Medir B, iterar sobre el embudo (pasos 2-3) | ~15h |
| 4 – 7 | **D: videos**, empezando por 5-6 y no por 10 | ~40-60h |
| 8 | Colchón, cierre, decidir el siguiente trimestre | ~15h |

## Por qué este orden
1. **B primero.** Es el mayor impacto por hora con diferencia: pierdes al 60% en el paso 2, y arreglarlo cuesta una semana. Cada usuario que consigas después vale más.
2. **B antes que D.** Los videos traen tráfico, y no quieres meterlo en un embudo que pierde al 60%. Si inviertes primero en D, pagas por adquirir gente que se va.
3. **D en lotes.** Con 5-6 videos ya ves si el canal funciona. Si funciona, haces los otros 4 el próximo trimestre; si no, te ahorraste 2 semanas.

## Qué NO haces
- **A (reescritura): no este trimestre.** Es 3 meses a tiempo completo para alguien con 4h/día, o sea, un proyecto de 5-6 meses durante los cuales no sacas nada nuevo, y con soporte encima. Reabre la conversación solo si puedes señalar un dolor concreto y medible que el framework actual te causa. Si lo hay, plantéalo como migración incremental, no como reescritura.
- **C (panel): no ahora.** Cuestiona la dependencia de A. Quizá una versión mínima (un email semanal con 3 métricas, o una vista simple) no necesite la reescritura. Si tus clientes lo piden, esa versión cabe en el colchón o en el próximo trimestre.

## La palanca que no estás mirando
Tus 2h de soporte/operación son el 33% de tu día. Si con B baja la fricción del alta, probablemente también baje el soporte. Y si dedicas unas horas a documentar respuestas frecuentes o a automatizar lo repetitivo, recuperas capacidad para todo lo demás. Considera meterlo en la semana 3 o 8.

## Riesgo principal
Que B salga en 2 semanas en vez de 1. Si pasa, recortas D a 4 videos. **Protege B y recorta D, nunca al revés.**