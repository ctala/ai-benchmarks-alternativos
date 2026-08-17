# Sakana Namazu — business_audit/atribucion_correlacion_temporal

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 10.714s | tokens_per_second: 191.2
- input_tokens: 270 | output_tokens: 2048

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

**No se puede saber si la secuencia de emails funcionó.** Con los datos que tienes, atribuir el crecimiento de marzo a los emails sería una conjetura, no una conclusión.

### Por qué no hay evidencia suficiente

Tienes tres eventos simultáneos en marzo que pueden explicar el mismo resultado:

1. **Secuencia de emails** (1 marzo) → dirigida a usuarios gratuitos existentes.
2. **Publicidad pagada** (3 marzo) → puede traer nuevos usuarios gratuitos *y* pagos directos.
3. **Mención de creador grande** (12 marzo) → suele generar picos de tráfico cualificado y conversiones inmediatas.

Además, estás midiendo **altas totales**, pero tu objetivo era convertir la **base gratuita preexistente**. Si entre las 14 altas de marzo hay usuarios que llegaron por los anuncios o el influencer y pagaron al instante, esas conversiones no deben atribuirse a la secuencia de emails.

### Lo que los números SÍ dicen (y no dicen)

- El MRR subió $1,200 (29%) y las altas pasaron de 9 a 14. En volúmenes pequeños, una diferencia de 5 altas puede ser ruido o puede explicarse fácilmente por un solo evento externo (la mención del creador, por ejemplo).
- No sabes cuántas de esas 14 altas eran usuarios gratuitos que ya estaban antes del 1 de marzo.
- No sabes si el pico de conversiones ocurrió después del envío de los emails, después del día 12 (mención) o fue distribuido durante todo el mes.
- No tienes tasa de churn: parte del aumento de MRR podría deberse a menos cancelaciones, no a más altas.

### Qué haría falta para estar seguros

Para poder decir "la secuencia funcionó" necesitarías, como mínimo, una de estas cosas:

1. **Atribución directa de cada alta**
   - Taggear cada checkout con la fuente (email, ads, influencer, orgánico).
   - Ver cuántas altas vineron del funnel de emails vs. otros canales.

2. **Grupo de control (A/B test o cohorte)**
   - Comparar la tasa de conversión de los usuarios gratuitos que recibieron la secuencia contra un grupo igual que no la recibió. Sin esto, no hay contrafactual