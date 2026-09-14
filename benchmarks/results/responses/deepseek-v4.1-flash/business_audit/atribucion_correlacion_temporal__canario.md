# DeepSeek V4.1 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 12.85s | tokens_per_second: 250.5
- input_tokens: 261 | output_tokens: 3219

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

**Conclusión: no se puede saber si la secuencia de emails funcionó.** Pudo haber ayudado, pudo no haber hecho nada, o el crecimiento pudo venir de la publicidad y/o de la mención del creador. Con estos datos, atribuir el +29% de MRR a la secuencia es una conclusión que los datos no sostienen.

Por qué:

- **Lanzaste tres cosas casi juntas:** secuencia el 1 de marzo, ads el 3 de marzo y mención de un creador el 12 de marzo. No hay forma de separar sus efectos.
- **El MRR no mide solo altas nuevas.** El +$1.200 puede incluir upgrades, downgrades, churn, cambios de precio, planes anuales, etc. No equivale a “14 altas nuevas”.
- **Las altas pasaron de 9 a 14: +5.** Sin saber cuántos usuarios free había en cada mes, no sabes si mejoró la tasa de conversión o si simplemente había más gente por los ads y el video.
- **Muestra pequeña:** 5 altas extra pueden ser ruido normal.
- **No hay grupo de control.** No sabes qué habría pasado sin la secuencia.

Qué miraría ya mismo para acotar:

1. **Altas por día:** si el salto fuerte es después del 12, probablemente pesó la mención; si es después del 3, los ads; si es gradual desde el 1, la secuencia.
2. **Fuente de cada alta:** email, video, ads, orgánico, referidos. Con UTM o encuesta post-compra.
3. **Tasa de conversión free→pago:** altas / usuarios free activos, no solo el número de altas.
4. **Churn y upgrades/downgrades:** para ver el MRR neto real.
5. **Métricas de la secuencia:** aperturas, clics, clics a checkout y upgrades atribuidos a cada email.

Para estar **seguros**, lo mínimo sería un experimento:

- Aleatorizar usuarios free: mitad recibe la secuencia, mitad no la recibe (o la recibe 30 días después).
- Medir conversión a pago en 30/60/90 días, MRR incremental y retención.
- Comparar el grupo con secuencia contra el grupo control. Eso te da el efecto causal real.

Si ya lanzaste todo y no puedes aleatorizar, se puede intentar un análisis cuasi-experimental: comparar expuestos vs no expuestos, cohortes antes/después y controlar por fuente, fecha de alta y engagement previo. Pero nunca será tan limpio como un holdout.

**Resumen:** la secuencia puede haber contribuido, pero no está probado. No la declares ganadora todavía. Necesitas un grupo control y datos de atribución por fuente para saber si realmente movió la aguja.