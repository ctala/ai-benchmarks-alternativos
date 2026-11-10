# Claude Fable 5.2 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 21.812s | tokens_per_second: 85.5
- input_tokens: 420 | output_tokens: 1866

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

**Orden: B primero, luego D. A y C quedan fuera de este trimestre.**

## La capacidad real

Tienes 4 h/día × 5 días × 8 semanas = **160 horas** para construir. Asumo que tus estimaciones son en semanas a tiempo completo (~40 h), así que cada "semana" de esfuerzo te cuesta 2 semanas de calendario.

| Iniciativa | Esfuerzo | En horas | En tu calendario | ¿Cabe? |
|---|---|---|---|---|
| A) Reescritura | ~3 meses | ~520 h | ~26 semanas | No, es más de 3 veces tu trimestre |
| B) Flujo de alta | 1 semana | ~40 h | 2 semanas | Sí |
| C) Panel de métricas | 3 semanas | ~120 h | 6 semanas | Bloqueada por A |
| D) 10 videos | 2 semanas | ~80 h | 4 semanas | Sí |

## El plan

- **Semanas 1–2: B.** Tiene impacto alto y el menor esfuerzo. Además, todo lo que hagas después rinde más si el alta no pierde al 60% de la gente.
- **Semanas 3–6: D.** Va después de B a propósito: los videos traen tráfico, y mandarlo a un alta rota es desperdiciarlo. Mientras grabas, mides cómo responde el arreglo de B.
- **Semanas 7–8: colchón de ~40 h.** Las estimaciones se pasan casi siempre, así que no lo llenes de antemano. Si sobra, úsalo en este orden:
  1. Una segunda iteración de B con los datos reales.
  2. Reducir las 2 h diarias de soporte (respuestas tipo, automatizaciones, documentación). Cada media hora que recuperes ahí te da un 12% más de capacidad para construir.

## Por qué A y C no entran

- **A:** aunque le dedicaras el trimestre entero, llegarías al cierre con ~30% de la reescritura hecha, nada entregado y el alta todavía rota. Si la quieres hacer, es un proyecto de dos trimestres completos, o hay que partirla en migraciones incrementales.
- **C:** depende de A, así que no puede empezar. Lo que sí revisaría es si esa dependencia es real, o si una versión mínima del panel puede hacerse sobre la plataforma actual. Si se puede, es candidata para el próximo trimestre sin esperar a A.

Si tus estimaciones eran en semanas de tus 6 h enfocadas y no de 40 h, B y D ocupan ~4,5 semanas en vez de 6 y el colchón crece, pero el orden y los descartes no cambian.