# Claude Opus 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.75 | quality: 8.0
- latency_total: 21.246s | tokens_per_second: 89.9
- input_tokens: 420 | output_tokens: 1911

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

## Tu capacidad real

- **8 semanas × 5 días × 4 h = 160 h** de construcción.
- Supongo que tus estimaciones son "a tiempo completo" = tus 6 h enfocadas → **1 semana estimada ≈ 30 h**.
- Tu trimestre equivale a **~5 semanas de las que tú estimas**, no 8.

| Iniciativa | Esfuerzo estimado | Horas reales | Semanas de calendario (a 4 h/día) |
|---|---|---|---|
| A) Reescritura | ~3 meses | ~390 h | ~20 semanas |
| B) Flujo de alta | 1 semana | ~30 h | ~1,5 |
| C) Panel métricas | 3 semanas | ~90 h | ~4,5 (y bloqueada por A) |
| D) 10 videos | 2 semanas | ~60 h | ~3 |

**A no cabe.** Necesita ~2,5 trimestres de tu capacidad real. Y como **C depende de A, C tampoco cabe.** Eso simplifica la decisión.

## El orden

**Semanas 1–2 → B: arreglar el alta**
- Es lo de mayor impacto por hora con diferencia: ~30 h para atacar una fuga del 60%.
- Va **antes que D** por una razón concreta: los videos traen gente. Si los publicas antes de arreglar el alta, más de la mitad de esa gente se pierde en el paso 2.
- Deja medición puesta desde el día 1 para saber si el arreglo funcionó.

**Semanas 3–5 → D: los 10 videos**
- Ahora el tráfico que generes cae en un embudo que retiene.
- Si puedes, publica 2–3 primero y mira la respuesta antes de grabar los 10. Ajustas sin rehacer trabajo.

**Semanas 6–8 → colchón (~70 h), en este orden de prioridad:**
1. **Margen para retrasos.** Las estimaciones de una sola persona casi siempre se quedan cortas. Asume que B y D se comerán parte de esto.
2. **Iterar sobre B** con los datos reales. El primer arreglo rara vez es el definitivo.
3. **Reducir tus 2 h/día de soporte.** Documentación, respuestas plantilla, automatizar lo repetitivo. Recuperar aunque sea 1 h/día equivale a un 25% más de capacidad cada trimestre siguiente. Es la mejor inversión a largo plazo que tienes, mejor que A.
4. **Preparar la decisión sobre A** (como máximo 1–2 días). Escribe exactamente qué problema de velocidad resuelve y si se puede atacar con una migración incremental módulo a módulo en vez de una reescritura completa.

## Lo que no harías este trimestre

- **No empieces A "para ir avanzando".** Una reescritura a medias no aporta nada: mantienes dos sistemas, el producto no mejora y el trimestre se va. Para un fundador solo, la reescritura completa es una de las trampas más caras que hay.
- **Cuestiona la dependencia de C.** Si tus clientes necesitan el panel, comprueba si una versión mínima (incluso un export o un informe por email) puede hacerse sobre la plataforma actual. Si sí, es candidata para el colchón o el próximo trimestre. Si no, C espera a que A esté decidido.

**Resumen:** B → D → colchón (soporte + iterar B). A y C quedan fuera por capacidad.