# Claude Opus 4.8 (suscripción) — business_audit/roadmap_restriccion_capacidad

- model_id: `claude-opus-4-8`
- success: True  | final: 5.01 | quality: 5.74
- latency_total: 67.953s | tokens_per_second: 53.8
- input_tokens: 4 | output_tokens: 3658

## Respuesta completa

## Primero, la aritmética que cambia toda la conversación

Tus estimaciones están en semanas *a tiempo completo*. Tu calendario no lo está. Traducido a tu capacidad real (4h/día × 5 días = **20h/semana**, ~**150h** en las 8 semanas descontando fricción):

| | Estimado (FT) | Horas reales | Semanas **tuyas** |
|---|---|---|---|
| A) Reescritura | 3 meses | ~480h | **24 semanas** |
| B) Flujo de alta | 1 semana | ~40h | **2 semanas** |
| C) Panel métricas | 3 semanas | ~120h | **6 semanas** (+ bloqueada) |
| D) 10 videos | 2 semanas | ~80h | **4 semanas** |

Estás pidiendo **36 semanas de trabajo en un trimestre de 8**. Cuatro veces y media tu capacidad. No hay orden posible que haga caber esto. La decisión no es priorizar: es **matar cosas**.

---

## Veredicto por iniciativa

**A) Reescritura — NO. No este trimestre, probablemente no este año.**
480h son 24 semanas tuyas. Las reescrituras se pasan de largo ~2x en la práctica, así que estás mirando **~un año de calendario** manteniendo dos sistemas en paralelo, sin enviar valor nuevo. Y ojo con el impacto que le pusiste: "velocidad y todo lo futuro" no es impacto, es una promesa de impacto. Ningún cliente te paga por el framework. Si el problema real es que algo va lento, mide los 3 endpoints más lentos y arréglalos: perfilado, índice, caché. Eso son **días, no meses**.

**B) Flujo de alta — SÍ. Es la única obvia.**
Pierdes 60% en el paso 2. Es el agujero por el que se va todo lo demás. Y es lo más barato de la lista. Esta va primero, sin discusión.

**C) Panel de métricas — Muerta por transitividad.**
Depende de A, y A no ocurre. Pero desafía esa dependencia: **¿de verdad el panel necesita la reescritura, o es una regla que te inventaste?** Casi nunca lo es. Si hay clientes pidiéndolo, saca un v0 esta semana: una página de solo lectura, o directamente un email semanal con sus números. Horas, no semanas. Valida que lo usen antes de invertir 120h.

**D) 10 videos — Sí, pero después de B.**
Grabarlos antes de arreglar el alta es echar agua en un balde agujereado: traes gente y se te cae el 60% en el paso 2. El orden aquí no es preferencia, es física.

---

## El trimestre

| Semanas | Qué | Entregable |
|---|---|---|
| **1–2** | **B: flujo de alta.** Días 1–2 solo diagnóstico (instrumenta el paso 2, mira 5 sesiones, llama a 3 que se cayeron). Recién ahí tocas código. | Fix en producción + métrica base y post-fix |
| **3** | **Medir e iterar B.** Un fix de conversión rara vez sale a la primera. Esta semana ya está presupuestada, no es un fracaso usarla. | Caída del 60% → objetivo declarado |
| **4–7** | **D: 10 videos.** En lotes (3–4 por sesión de grabación), no de a uno. Ya tienen a dónde mandar a la gente. | 10 videos publicados |
| **8** | **Colchón.** Se va a llenar sola. | Cierre + decisión del próximo trimestre con datos |

Eso son 6 semanas de trabajo comprometido y 2 de holgura sobre 8. Si tu plan no tiene holgura, no es un plan, es un deseo.

---

## El único cambio que vale la pena considerar

Gastas **2 de 6 horas diarias en soporte y operación**. Es un tercio de tu capacidad, todos los días, para siempre. Si sacrificas D y usas las semanas 4–7 en atacar los 3 tickets más repetidos (documentarlos, arreglarlos, automatizarlos), y recuperas aunque sea 1h/día, eso son **+25% de capacidad para construir** de aquí en adelante. Compuesta cada trimestre. Los videos no compuestan.

Mi recomendación se queda con D porque necesitas entrada de gente y ya arreglaste el balde. Pero si el soporte te está ahogando, ese es el swap legítimo. Cualquier otro no lo es.

**No hagas ambos. Es exactamente así como llegas a la semana 8 con las dos a medias.**