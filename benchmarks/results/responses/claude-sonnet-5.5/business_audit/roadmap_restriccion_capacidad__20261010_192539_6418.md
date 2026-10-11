# Claude Sonnet 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 4.19 | quality: 4.0
- latency_total: 22.635s | tokens_per_second: 108.8
- input_tokens: 420 | output_tokens: 2463

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
- 4h × 5 días × 8 semanas = **~160h**. Con ~20% de colchón para imprevistos de soporte y estimaciones optimistas, planifica con **~130h**.
- Asumo que tus estimaciones están en semanas a tiempo completo (~40h). A tu ritmo (~20h/semana), cada una dura el doble en calendario:
  - A: ~480h (no cabe ni de lejos)
  - B: ~40h (~2 semanas)
  - C: ~120h (~6 semanas), y está bloqueada por A
  - D: ~80h si son 2 semanas completas, aunque quizá puedas bajarlo con producción por lotes

## Orden

**1. B: Arreglar el alta (semanas 1-2)**
Perder al 60% en el paso 2 es la mayor palanca por hora invertida. Todo lo demás (videos, marketing, producto) alimenta ese embudo, así que arréglalo antes de meterle más tráfico.
- Días 1-2: diagnosticar antes de construir. Mira analíticas y grabaciones de sesión, y habla con 3-5 personas que abandonaron.
- Resto: arreglar, desplegar y medir.

**2. D: Videos (semanas 3-6)**
Con el embudo arreglado, cada visita vale más. Publica a medida que grabas, no al final, para que el efecto se acumule durante el trimestre. Si te retrasas, recorta a 6-7 videos en vez de empujar el plazo.

**3. Semanas 7-8: colchón e iteración**
- Itera sobre B con los datos reales de las semanas anteriores.
- Absorbe el desvío que haya habido en soporte o en los videos.
- Dedica medio día a decidir qué hacer con A (ver abajo).

## Lo que no entra este trimestre

**A (reescritura):** necesita ~12 semanas a tiempo completo y tú tienes la mitad de capacidad, así que son 5-6 meses. Tendrías el producto congelado durante todo ese tiempo, sin mejoras de conversión ni contenido, y con el riesgo de acabar con dos plataformas a medias. Antes de reabrirlo, respóndete: *¿qué cosa concreta me frena hoy que solo la reescritura resuelve?* Si la respuesta es vaga, probablemente no toca. Si es concreta, probablemente se puede atacar con una migración incremental.

**C (panel de métricas):** está bloqueada por A, y juntas serían ~8 meses. Si tus clientes lo piden de verdad, la alternativa es una versión mínima sobre la plataforma actual, como un email semanal con 3-4 números o un export CSV. Sería cuestión de días, no de semanas, y sirve para validar si de verdad lo usan.

## Riesgos
- **Soporte:** si crece más allá de 2h/día, sacrifica D, nunca B.
- **B más complejo de lo previsto:** el diagnóstico de los días 1-2 te lo dirá. Si es así, recorta D, no el arreglo.
- Si B reduce tickets de soporte (gente confundida en el paso 2), recuperas horas para el resto del trimestre.

¿Quieres que desglose las dos primeras semanas de B día a día?