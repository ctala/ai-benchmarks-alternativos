# Claude Opus 5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 51.583s | tokens_per_second: 59.7
- input_tokens: 418 | output_tokens: 3081

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

## Primero, la matemática — porque tus estimaciones y tu capacidad están en unidades distintas

Tus esfuerzos están en "semanas/meses a tiempo completo". Tu capacidad es 4h/día. Eso es **media velocidad**. Todo se duplica en calendario:

| | Esfuerzo declarado | Horas | Semanas reales a tu ritmo | ¿Cabe en 8 semanas? |
|---|---|---|---|---|
| A) Reescritura | 3 meses FT | ~480h | **~24 semanas** | No (3x el trimestre) |
| B) Flujo de alta | 1 semana FT | ~40h | **2 semanas** | Sí |
| C) Panel métricas | 3 semanas FT | ~120h | **6 semanas** + bloqueado por A | No |
| D) 10 videos | 2 semanas FT | ~80h | **4 semanas** | Sí, apretado |

Tienes ~160 horas en el trimestre. A sola pide 480. La discusión sobre "priorizar A" no existe: no es una decisión, es una imposibilidad aritmética.

Y sé honesto contigo: esas estimaciones son tuyas y son optimistas. Aplica 1.5x mentalmente. Además, tus 2h/día de soporte no son fijas — crecen con clientes.

## Veredicto por iniciativa

**B — Hazlo ya, esta semana.** Perder 60% en un paso concreto es el mejor ROI que vas a ver en tu vida. Duplicar ese paso duplica todo lo que viene detrás sin tocar nada más. Es 2 semanas de las 8. No hay argumento en contra.

**A — Fuera del trimestre. No la empieces "un poquito en paralelo".** Esa es la forma más común en que un fundador solo pierde un trimestre entero: 6 semanas de rewrite a medias, plataforma vieja sin mantener, nueva sin terminar, cero valor entregado. Lo que sí haces: un spike de **8 horas máximo** al final del trimestre para escribir qué dolor concreto resuelve el rewrite. Casi siempre resulta que son 3 problemas puntuales que se arreglan en 2 semanas sin cambiar de framework. Si de verdad no, tendrás el documento para decidir con datos en el próximo trimestre.

**C — Muerta por dependencia.** Depende de A, y A no pasa. Punto. Pero ojo: si un cliente te está pagando o retenido por ese panel, la dependencia de A es sospechosa. Un panel de métricas casi nunca necesita un framework nuevo. Si es real, hay una versión de 3 días (una vista, 4 números, sin tiempo real) que probablemente cubre el 80% del valor. Eso sí lo consideraría en el próximo trimestre.

**D — Sí, pero recortada.** 10 videos es un número que te inventaste. Haz 4, grabados en dos sesiones batch. Es la iniciativa con scope más elástico, así que es tu amortiguador: si B se complica, D se encoge sin drama.

## El trimestre

| Semana | Foco |
|---|---|
| **1** | Instrumentar el paso 2 (¿dónde exactamente se caen y por qué?) + arreglo v1 |
| **2** | Cerrar B, deploy |
| **3** | Dejar correr y acumular datos. Guiones de D |
| **4–6** | D: batch de grabación (2 sesiones), edición, publicación |
| **7** | B v2, ahora con un mes de datos reales del funnel |
| **8** | Colchón + spike de A (8h) + plan del próximo trimestre |

Semanas 6 de trabajo, 2 de colchón. El colchón no es pereza: es lo que se come un pico de soporte, un cliente enojado o una gripe. Si planificas 8 de 8, entregas 5.

## Dos cosas que cambian este orden

**Si tienes poco tráfico:** arreglar un 60% de caída sobre 30 visitas al mes no mueve nada. Si es tu caso, D sube al primer lugar (generar demanda) y B baja a segundo. Mira tu volumen antes de aceptar este plan.

**Revisa de dónde vienen tus tickets de soporte.** Si una parte significativa es gente confundida en el alta, B te devuelve horas de tus 2h/día diarias además de arreglar el funnel. Eso lo convierte en la única iniciativa que te compra capacidad futura — y esa capacidad es lo que eventualmente hace viable un proyecto del tamaño de A.