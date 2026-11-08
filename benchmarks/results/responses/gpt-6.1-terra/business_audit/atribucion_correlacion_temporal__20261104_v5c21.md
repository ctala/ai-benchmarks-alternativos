# GPT-6.1 Terra — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 8.293s | tokens_per_second: 59.4
- input_tokens: 224 | output_tokens: 493

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

**Conclusión: no se puede saber si la secuencia de emails funcionó.** Marzo fue mejor que febrero: el MRR subió de $4.100 a $5.300 (+29%) y las altas de pago pasaron de 9 a 14 (+56%). Pero también comenzaron la publicidad y la mención del creador, así que no podemos atribuir esas mejoras a los emails. Ni siquiera sabemos cuántas altas vinieron de usuarios que recibieron la secuencia.

Además, el cambio de MRR no refleja solo las altas: también puede incluir cancelaciones, cambios de plan u otros movimientos.

**Para estimar el efecto de los emails**, haría una prueba con nuevos usuarios elegibles del plan gratuito:

1. Asignarlos aleatoriamente a dos grupos: uno recibe la secuencia y otro no. Mantener el resto de las condiciones lo más similares posible.
2. Comparar qué porcentaje de cada grupo pasa a pago dentro de un plazo definido, no solo el número de altas. También medir el MRR incremental y las cancelaciones.
3. Definir de antemano el tamaño de muestra y la duración. Con volúmenes como 9–14 altas al mes, podría hacer falta bastante tiempo para detectar un efecto con confianza.

Mientras tanto, revisaría qué altas recibieron los emails y sus fuentes de adquisición. Eso puede dar pistas, pero por sí solo no demostraría que los emails causaron las conversiones.