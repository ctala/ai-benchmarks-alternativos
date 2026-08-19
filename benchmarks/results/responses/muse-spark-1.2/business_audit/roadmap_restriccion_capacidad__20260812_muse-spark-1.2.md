# Muse Spark 1.2 — business_audit/roadmap_restriccion_capacidad

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 22.037s | tokens_per_second: 121.5
- input_tokens: 250 | output_tokens: 2677

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

Como fundador solo, tu capacidad no es 8 semanas. Es **160 horas.**

4h/día x 5 días x 8 semanas = 160h. Y eso sin contar que tus estimaciones están hechas para tiempo completo y sin interrupciones. En la vida real multiplícalas x1.5.

Con esa matemática, tu trimestre se ordena solo:

### La tabla fría

| Iniciativa | Impacto | Esfuerzo estimado | Esfuerzo REAL para ti | ¿Cabe? | Veredicto |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A) Reescribir plataforma** | Alto | 3 meses full-time = ~360h a 6h/día | ~540h con tu ritmo de 4h/día | NO. Te consume 2 trimestres enteros sin entregar nada | **NO HACER** |
| **B) Arreglar alta - pierde 60%** | Alto | 1 semana = ~20h | ~30h | SÍ | **P0 - HACER YA** |
| **C) Panel de métricas** | Medio | 3 semanas | ~60h | NO, depende de A. Si A no se hace, C está bloqueado | **NO HACER** |
| **D) 10 videos** | Medio | 2 semanas = ~40h | ~60h | SÍ | **P1 - HACER DESPUÉS** |

> Regla de fundador solo: Si no lo puedes terminar y poner en producción este trimestre, no lo empiezas.

Si haces A, llegas al cierre del trimestre con 0 ingresos nuevos, 0 usuarios nuevos y una reescritura a medias que no puedes lanzar. Es suicidio.

### Tu orden para las próximas 8 semanas

**Semana 1 - 1.5: SOLO B. Nada más.**
Arreglar el flujo de alta que pierde al 60% en el paso 2. Es lo único con impacto alto que cabe en tu capacidad.
Objetivo: Pasar de perder 60% a perder 30% o menos. Eso duplica tus altas sin gastar un euro en adquisición. Todo lo demás es secundario.

**Semana 2 - 4: D. Los 10 videos.**
Ya tienes un alta que convierte. Ahora sí tiene sentido traer gente. Grábalos en lote: 2 días guión, 5 días grabación, 3 días edición. 1 video cada 1-2 días a 4h/día.

**Semana 5 - 8: NO EMPIECES A NI C. Itera y mide.**
Te sobran ~4 semanas. No las llenes con una reescritura. Úsalas para:
1.  Medir B: ¿Realmente mejoró la conversión? Entrevista a 5 usuarios que pasaron el nuevo flujo.
2.  Iterar B: Pulir el paso 2 con lo que aprendiste. Un 5% extra ahí vale más que cualquier panel.
3.  Buffer: Soporte siempre se come más de 2h. Deja 30% de colchón.
4.  Discovery de A: Máximo 30 min/día para documentar qué duele del framework actual y qué harías distinto. Cero código.

### Resumen para tu trimestre

**HACER:** B -> D
**NO HACER:** A y C

B y D juntos te consumen ~90h reales. Te dejan 70h de colchón para imprevistos, iterar y no quemarte. A sola te pide 540h. No es priorización, es física.

¿Quieres velocidad futura? No la consigues reescribiendo 3 meses solo. La consigues reteniendo a los usuarios que hoy se te van en el paso 2.

Empieza B mañana. Hasta que no esté en producción y medido, D no existe y A es tabú.