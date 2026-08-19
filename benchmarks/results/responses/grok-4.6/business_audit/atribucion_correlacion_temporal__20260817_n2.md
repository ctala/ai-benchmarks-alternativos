# Grok 4.6 — business_audit/atribucion_correlacion_temporal

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 17.317s | tokens_per_second: 62.8
- input_tokens: 422 | output_tokens: 1088

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

**No se puede saber si la secuencia de emails funcionó.** El aumento de MRR (+$1.200 / +29 %) y de altas (de 9 a 14) coincide en el tiempo con **dos cambios más** que empezaron casi al mismo tiempo: publicidad pagada desde el 3 de marzo y una mención de un creador con audiencia grande el 12 de marzo. Con los números que das no hay forma de separar los efectos.

Otros problemas que impiden atribuir el resultado a los emails:
- No hay datos de conversión específica de la secuencia (aperturas, clics, altas atribuidas a esos emails, o siquiera cuántos usuarios gratuitos la recibieron).
- No hay grupo de control ni comparación limpia (periodo anterior sin publicidad ni mención, o holdout).
- El MRR sube por altas nuevas, pero también podría incluir upgrades, menor churn u otras cosas que no se desglosan. 5 altas extra no explican por sí solas +$1.200 sin saber precios, timing de cobro o retención.
- Febrero y marzo no son periodos equivalentes (estacionalidad, días del mes, etc.).

### Qué haría falta para estar más seguros
- Atribución directa: UTM o tracking en los emails (altas que vinieron de esos enlaces vs. resto de canales).
- Tasas de conversión free→pago **antes vs. después**, segmentadas por cohorte de usuarios que recibieron la secuencia vs. los que no.
- Desglose de las 14 altas de marzo por fuente (emails / ads / mención / orgánico / otros) y del incremento de MRR.
- Idealmente un test (A/B o holdout de parte de la lista gratuita) o al menos un periodo de comparación sin las otras dos intervenciones.
- Datos de funnel (cuántos gratuitos había, tasa histórica de conversión, LTV o retención de las nuevas altas).

Sin eso, cualquier afirmación de que “los emails funcionaron” (o de que no) es especulación. El crecimiento es real; la causa no se puede aislar con lo que hay. Si tienes más métricas (conversiones por email, fuentes de las altas, etc.) se puede revisar de nuevo.