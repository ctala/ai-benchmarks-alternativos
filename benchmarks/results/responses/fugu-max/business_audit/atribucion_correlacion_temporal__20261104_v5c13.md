# Fugu Max — business_audit/atribucion_correlacion_temporal

- model_id: `sakana/fugu-max`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 7.863s | tokens_per_second: 80.3
- input_tokens: 315 | output_tokens: 631

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

**Conclusión:** no se puede saber si la secuencia funcionó a partir de estos datos. Los resultados de marzo mejoraron —el MRR subió $1.200 (+29%) y las altas al plan pago pasaron de 9 a 14 (+56%)—, pero eso no demuestra que los emails causaran la mejora. La publicidad y la mención del creador ocurrieron durante el mismo mes y son explicaciones alternativas.

Además, el MRR puede cambiar por factores distintos de las nuevas altas, como bajas, cambios de plan o ajustes de precios. Y con solo 9 y 14 altas, la diferencia podría ser variable.

**Para medirlo con más seguridad:**

- Asigna al azar a usuarios gratuitos elegibles a dos grupos: secuencia de emails y grupo de control sin secuencia.
- Compara la **tasa de conversión a pago** durante el mismo plazo, no solo el total de altas.
- Registra quién recibió los emails y sus conversiones; mide también entregas, clics y bajas, aunque estos datos por sí solos no prueban causalidad.
- Sigue el MRR generado por cada grupo y considera bajas o cambios de plan.
- Procura que ambos grupos tengan una exposición comparable a publicidad y otras promociones.

Si no puedes hacer una prueba controlada, los datos por fuente y por cohorte pueden ayudar, pero con estos acontecimientos simultáneos no darían una atribución segura.