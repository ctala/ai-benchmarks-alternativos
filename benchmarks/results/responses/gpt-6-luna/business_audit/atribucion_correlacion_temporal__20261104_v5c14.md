# GPT-6 Luna — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.13 | quality: 10.0
- latency_total: 8.795s | tokens_per_second: 87.2
- input_tokens: 224 | output_tokens: 767

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

**Conclusión:** los resultados mejoraron en marzo, pero no se puede saber si la secuencia de emails causó esa mejora.

El MRR subió **$1.200** (de $4.100 a $5.300) y las altas al plan pago pasaron de **9 a 14**. Eso es compatible con que los emails hayan ayudado, pero en el mismo mes empezaste a pagar publicidad y un creador mencionó la comunidad. Sin un grupo de comparación, no podemos separar el efecto de cada cosa —ni descartar otros cambios, como cancelaciones o ampliaciones de planes.

**Qué haría para estimarlo con más seguridad:**

- Asignar aleatoriamente a los usuarios gratuitos elegibles a dos grupos: uno recibe la secuencia y otro no.
- Comparar la conversión a pago en el mismo plazo para ambos grupos —por ejemplo, dentro de los 30 días— y también el MRR neto generado.
- Registrar qué usuarios recibieron los emails y de dónde llegaron; si es posible, equilibrar la asignación por canal de adquisición.
- Repetirlo con suficiente volumen. Con pocos usuarios, la diferencia puede deberse al azar, así que conviene informar el tamaño de la muestra y la incertidumbre.

Los clics o las conversiones atribuidas a los emails ayudan a entender el recorrido, pero por sí solos no demuestran que la secuencia generara conversiones adicionales.