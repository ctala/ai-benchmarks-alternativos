# Seed 2.1 Turbo — business_audit/atribucion_correlacion_temporal

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.37 | quality: 10.0
- latency_total: 69.831s | tokens_per_second: 74.9
- input_tokens: 275 | output_tokens: 5231

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de datos de una empresa pequeña. Tu trabajo es proteger al equipo de conclusiones que los datos no sostienen. Prefieres decir 'no se puede saber' antes que dar una respuesta cómoda pero falsa.

**user:**

Tengo una comunidad de pago online. Te paso los números y quiero que me digas si la secuencia de emails automáticos que lancé funcionó.

- El 1 de marzo activé una secuencia de 5 emails para los usuarios del plan gratuito.
- MRR al 28 de febrero: $4.100
- MRR al 31 de marzo: $5.300 (+29%)
- Altas al plan pago en febrero: 9
- Altas al plan pago en marzo: 14

Contexto adicional: también el 3 de marzo empecé a pagar publicidad ($400 en el mes), y el 12 de marzo un creador con audiencia grande mencionó la comunidad en un video.

¿La secuencia de emails funcionó? Dame tu conclusión y qué haría falta para estar seguros.


## Respuesta completa

### Conclusión clara: No se puede saber si la secuencia de emails funcionó.
El aumento de MRR y de altas que ves en marzo no se puede atribuir a la secuencia de emails, porque hay demasiadas variables que se superponen en el mismo período y no tienes forma de aislar el efecto de cada una. Incluso es posible que la secuencia no haya aportado nada al crecimiento, o que sí lo haya hecho, pero no tienes datos para confirmarlo.

---

### Por qué no se puede confirmar con los datos que tienes:
1. **Hay dos variables confundidoras muy fuertes en el mismo mes**
   Empezaste la secuencia el 1 de marzo, pero solo 2 días después lanzaste publicidad pagada ($400, un monto relevante para un MRR de ~$4k) y el 12 de marzo hubo una mención de un creador con audiencia grande (este tipo de acciones suelen generar picos de altas muy importantes). Todo el crecimiento de marzo se puede explicar por cualquiera de estas dos acciones, por una combinación de las tres, o incluso por factores que no mencionas.

2. **No sabes si las altas vienen de la población que recibió los emails**
   La secuencia era para usuarios del plan gratuito existentes al 1 de marzo, pero no tienes desglosado:
   - Cuántas de las 14 altas de marzo son de usuarios que ya eran gratuitos ANTES del 1 de marzo (o sea, que sí recibieron la secuencia completa).
   - Cuántas son de usuarios que se registraron como gratuitos DESPUÉS del 1 de marzo (que entraron por publicidad o la mención del creador, y tal vez recibieron parte de la secuencia, pero no son la población objetivo inicial).
   - Cuántas son altas directas al plan pago (sin pasar por el gratuito), que no habrían recibido los emails en absoluto.

3. **El tamaño de muestra es muy pequeño**
   Pasar de 9 a 14 altas es una diferencia de solo 5 usuarios. Incluso si no hubiera habido publicidad ni mención del creador, esta diferencia podría ser una fluctuación aleatoria normal (por ejemplo, un par de usuarios que iban a convertirse de todos modos lo hicieron en marzo en lugar de febrero).

4. **Faltan datos que explican el aumento de MRR**
   El MRR no solo depende de altas: también cambia por cancelaciones (churn), cambios de plan (subidas o bajadas) o pagos anuales que se contabilizan prorrateados. No sabes cuánto del aumento de $1.200 de MRR se debe a las 5 altas extra, y cuánto a otros factores.

---

### Qué puedes hacer para acercarte a una respuesta (sin certeza total):
Si quieres analizar lo que pasó en marzo con datos que probablemente ya tienes, puedes hacer estos pasos para tener indicios (pero no prueba definitiva):
1. **Desglosa las altas por cohorte de usuario gratuito**
   Separa las altas de marzo entre: usuarios que eran gratuitos antes del 1 de marzo, usuarios que se registraron entre el 1 y el 3 de marzo (antes de la publicidad), entre el 3 y el 12 de marzo (con publicidad pero sin la mención del creador) y después del 12 (con todas las acciones). Si la mayoría de las altas de la cohorte anterior al 1 de marzo se dieron antes del 3 de marzo, es un indicio leve de que los emails podrían haber ayudado.
2. **Compara la tasa de conversión histórica**
   Revisa qué porcentaje de la base gratuita se convertía a pago en meses anteriores a marzo. Si la tasa de conversión de los usuarios que eran gratuitos antes del 1 de marzo fue mucho más alta en marzo que en el promedio histórico, es otro indicio, pero sin certeza (podría ser que la mención del creador también motivara a usuarios que ya estaban en la base a convertirse).
3. **Desglosa el origen de las altas**
   Si usas parámetros UTM, códigos de descuento exclusivos para la publicidad y la mención del creador, o encuestas de "¿cómo te enteraste?", puedes saber cuántas altas vinieron directamente de esas dos acciones. Las que no tengan un origen claro podrían ser de los emails, pero también de boca en boca o tráfico orgánico.

---

### Qué necesitas para estar SEGURO de si la secuencia funciona:
La única forma de medir el impacto real de la secuencia de emails es hacer un **test A/B controlado**:
1. Toma a todos los usuarios del plan gratuito que cumplan los mismos criterios (por ejemplo, que se registraron hace menos de 30 días, que no han recibido emails de venta antes).
2. Divídelos en dos grupos **aleatorios**:
   - Grupo control: no recibe la secuencia de emails.
   - Grupo tratamiento: sí recibe la secuencia.
3. Asegúrate de que ambos grupos estén expuestos a las mismas condiciones externas (misma publicidad, mismas menciones de creadores, mismas promociones). La única diferencia entre los dos grupos tiene que ser la secuencia de emails.
4. Después del período de la secuencia (por ejemplo, 15 o 30 días), compara la tasa de conversión a plan pago entre ambos grupos. Si la diferencia es estadísticamente significativa (es decir, es muy poco probable que sea por azar), entonces puedes decir con seguridad si la secuencia funcionó, y incluso medir cuánto impacto tiene.

Hasta que no hagas esto, cualquier afirmación de que la secuencia fue la causa del crecimiento de marzo es una suposición, no una conclusión basada en datos.