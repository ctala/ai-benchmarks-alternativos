# Claude Opus 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.76 | quality: 8.0
- latency_total: 21.962s | tokens_per_second: 85.5
- input_tokens: 420 | output_tokens: 1878

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

## Capacidad real

- **4 h/día × 5 días × 8 semanas = 160 h** para construir.
- Tus estimaciones están en tiempo completo. Si eso equivale a unas 30-40 h/semana y tú tienes 20 h, cada estimación se multiplica por **1,5-2×**.

| Iniciativa | Estimación | En tu capacidad real | ¿Cabe? |
|---|---|---|---|
| A) Reescritura | 3 meses | ~390-520 h (6-8 meses a tu ritmo) | **No, ni de lejos** |
| B) Flujo de alta | 1 semana | ~30-40 h (1,5-2 semanas) | Sí |
| C) Panel de métricas | 3 semanas | Depende de A | **No es posible este trimestre** |
| D) 10 videos | 2 semanas | ~60-80 h (3-4 semanas) | Sí |

B + D suman ~90-120 h, lo que te deja **40-70 h de margen**. Necesitas ese margen, porque como fundador solo siempre surge algo.

## El orden

**Semanas 1-2: B (flujo de alta)**
- Es lo de mayor impacto por hora, con mucha diferencia. Perder al 60% en el paso 2 es una fuga en todo lo que hagas después.
- Mide antes y después: conversión del paso 2 y altas completadas por semana.

**Semanas 3-6: D (videos)**
- Van después de B a propósito. Si grabas antes de arreglar el alta, el tráfico que generen los videos cae en un embudo que pierde a 6 de cada 10.
- Si vas lento, recorta a 6-8 videos antes que alargar el plazo.

**Semanas 7-8: margen + preparación**
- Itera sobre B según los datos. El primer arreglo rara vez es el definitivo.
- Prepara un plan para A, sin empezarla (lo explico abajo).
- Si sobra tiempo, invierte en **reducir tus 2 h diarias de soporte** (documentación, respuestas guardadas, automatizar lo repetitivo). Cada hora diaria que recuperes son ~40 h más el próximo trimestre.

## Qué no hacer

**No empieces A este trimestre.** Una reescritura a medias es el peor estado posible: mantienes dos bases de código, no entregas nada y bloqueas todo lo demás. Además, las reescrituras casi siempre se subestiman, así que tus 3 meses probablemente sean más.

En las semanas 7-8, dedica 8-10 h a responder estas preguntas:
- ¿Qué problema concreto te resuelve el nuevo framework? ¿Es velocidad tuya o del producto?
- ¿Se puede migrar por partes en vez de reescribir todo de golpe?
- ¿Hay mejoras dentro del stack actual que te den el 50% del beneficio con el 10% del esfuerzo?

**Cuestiona la dependencia de C con A.** ¿Necesitas de verdad el nuevo framework para un panel de métricas? Quizá una versión mínima (un reporte por email, una página simple) entrega parte del valor en el stack actual. Si es así, puede ser candidata para el próximo trimestre sin esperar a A.

## Un aviso

Si B funciona, tendrás más altas, y más altas suelen traer más soporte. Vigila si tus 2 h diarias suben a 2,5-3 h. Si pasa, recorta D, no B.

**Resumen:** B → D → margen y preparación de A. C y A quedan fuera de este trimestre.