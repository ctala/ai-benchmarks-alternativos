# Nemotron 3.5 Lightning — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.16 | quality: 10.0
- latency_total: 14.761s | tokens_per_second: 131.6
- input_tokens: 243 | output_tokens: 1943

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

**Conclusión: No se puede saber si la secuencia de emails funcionó.**

Los datos que compartes muestran una correlación (el MRR subió y las conversiones aumentaron), pero **no demuestran causalidad**. Hay al menos tres factores concurrentes que podrían explicar todo o parte del crecimiento, y no hay en la información suficientes datos de atribución para aislar el efecto de la secuencia.

**Por qué los datos no sostienen la conclusión:**

1. **Factores externos que ocurrieron al mismo tiempo:**
   - Empezaste a pagar publicidad el 3 de marzo ($400 en el mes). Eso trae tráfico y conversiones, pero no tienes datos de cuántos registros o cuánto MRR generó ese tráfico.
   - El 12 de marzo un creador con audiencia grande mencionó la comunidad en un video. Un solo shoutout de ese tipo suele generar un pico de inscripciones que puede durar días o semanas. No hay forma de saber cuántos de los +5 nuevos pagantes llegaron por ese canal vs. los emails vs. el tráfico orgánico habitual.

2. **Falta de métricas de la propia secuencia:**
   - No tienes tasas de apertura, de clics, ni tasa de conversión de email a pago. Una secuencia de 5 emails puede tener un rendimiento excelente, mediocre o pésimo; los datos de MRR y altas totales no lo revelan.
   - No hay grupo de control (usuarios que no recibieron los emails) ni datos históricos de qué pasaba con las altas en semanas similares sin secuencia.

3. **El salto numérico no cierra el círculo:**
   - Pasaste de 9 a 14 altas pagas (+5). Si tu plan de pago tiene, por ejemplo, $20/mes, esos 5 nuevos usuarios representan $100 de MRR. Pero el MRR subió $1.200 (de $4.100 a $5.300). Eso significa que otros $1.100 provinieron de usuarios que ya estaban suscritos (renewals), upgrades, o bien de los anuncios y el mencio del creador. No hay datos para repartir ese crédito.

**Qué haría falta para estar seguros:**

Para atribuir el crecimiento a la secuencia de emails, necesitaría al menos uno de estos escenarios:

| Qué medir / tener | Por qué importa |
|-------------------|----------------|
| **Resultados A/B**: Un grupo que recibió los 5 emails y otro que no (o recibió una versión placeholder). | Es la única forma estadísticamente válida de aislar el efecto de los emails. |
| **Atribución de alta**: Tagging en el formulario de alta que pregunte "¿Cómo te enteraste?" o vincule la alta al origen (email, ad, redes sociales, referencia). | Permite contar cuántos de los +5 pagos vinieron específicamente de la secuencia. |
| **Tasas de engagement**: Apertura y clics de la secuencia. | Incluso sin A/B, unos buenos números de engagement harían más plausible que los emails contribuyeran. |
| **Precio promedio por usuario (ARPU) o plan desglosado**: Para verificar si los +5 nuevos pagos explican una parte lógica del +$1.200 MRR, o si el crecimiento viene de renovaciones/upsells. | Evita la ilusión de que los emails causaron todo el crecimiento. |
| **Lag temporal**: Registrar la fecha exacta de cada alta y compararla con los días 1–5 de la secuencia, el 3 de marzo (anuncios) y el 12 de marzo (creador). | Permite ver si las altas se concentran en la ventana de los emails o se dispersan por los otros hitos. |

**En resumen:** Con los datos actuales, la secuencia podría haber ayudado, podría haber sido irrelevante, o podría haber simplemente "atado" dos tendencias que venían de los anuncios y el mencio del creador. Para responder con certeza, se necesita datos de atribución y, idealmente, un diseño experimental controlado.