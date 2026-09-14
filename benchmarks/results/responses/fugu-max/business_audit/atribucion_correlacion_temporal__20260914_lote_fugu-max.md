# Fugu Max — business_audit/atribucion_correlacion_temporal

- model_id: `sakana/fugu-max`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 16.59s | tokens_per_second: 80.5
- input_tokens: 297 | output_tokens: 1336

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

## Conclusión

**No se puede saber si la secuencia de emails funcionó a partir de estos datos.**

Los resultados de marzo son positivos:

- MRR: de **$4.100 a $5.300**, un aumento de **$1.200 (+29%)**.
- Altas al plan pago: de **9 a 14**, un aumento de **5 altas (+56%)**.

Pero el mismo mes ocurrieron dos acciones relevantes:

- Publicidad desde el 3 de marzo, con un gasto de $400.
- Mención de un creador con una audiencia grande el 12 de marzo.

Por tanto, las 14 altas y el aumento de MRR pueden deberse a los emails, a la publicidad, a la mención del creador, a una combinación de ellos o a otros factores. Los datos agregados mensuales no permiten atribuir el resultado a la secuencia.

La conclusión correcta sería:

> **Marzo tuvo mejor desempeño, pero no hay evidencia suficiente para afirmar que la secuencia de emails causó la mejora.**

Además, el MRR no necesariamente proviene solo de nuevas altas: puede incluir churn, upgrades, downgrades, reactivaciones o cambios de precio.

## Qué haría falta para estar seguros

### 1. Un grupo de control

La mejor opción sería haber dividido aleatoriamente a los usuarios gratuitos elegibles:

- **Grupo tratamiento:** recibió la secuencia.
- **Grupo control:** no recibió la secuencia durante el período de evaluación.

Luego comparar entre ambos:

- Tasa de conversión a pago.
- Ingreso incremental o MRR por usuario.
- Tiempo hasta la conversión.
- Retención después de 30, 60 o 90 días.
- Bajas y reembolsos.

La comparación relevante sería algo como:

> Conversión del grupo con emails menos conversión del grupo sin emails.

Comparar simplemente “quienes abrieron el email” contra “quienes no lo abrieron” no es suficiente, porque los usuarios más interesados probablemente también sean más propensos a abrir y comprar.

### 2. Atribución separada de cada canal

Habría que registrar, para cada alta:

- Si recibió la secuencia.
- Si abrió o hizo clic en algún email.
- Si visitó desde un anuncio.
- Si llegó mediante la mención del creador.
- UTM o códigos específicos por canal.
- Fecha y hora de la conversión.

También convendría analizar las altas por día. Si hubo un pico inmediatamente después del video, eso sería compatible con un efecto importante del creador, aunque tampoco lo demostraría por sí solo.

### 3. La base de comparación correcta

Para calcular una tasa de conversión hacen falta al menos:

- Número de usuarios gratuitos elegibles al inicio.
- Cuántos recibieron efectivamente cada email.
- Entregabilidad, aperturas y clics.
- Conversiones de esos usuarios.
- Precio del plan y MRR generado por cada alta.
- Churn durante el período.
- Historial de conversión de meses anteriores.

Las 9 altas de febrero sirven como referencia descriptiva, pero no como un control sólido: puede haber estacionalidad, cambios en el volumen de usuarios gratuitos o variaciones en el tráfico.

### 4. Un experimento futuro

Mantendría, por ejemplo, un **10–20% de usuarios como grupo de control**, asignado aleatoriamente, y mediría durante una ventana definida —por ejemplo, 30 días—:

- Conversión incremental.
- MRR incremental.
- Retención.
- Coste de la secuencia.
- Valor generado por usuario.

Así se podría estimar el retorno real de los emails, separado tanto de la publicidad como de las menciones externas.

En resumen: **los números justifican investigar la secuencia, pero no atribuirle el crecimiento**. Hay señales positivas a nivel global, no una prueba de causalidad.