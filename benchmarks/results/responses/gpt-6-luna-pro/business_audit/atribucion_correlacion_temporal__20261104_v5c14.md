# GPT-6 Luna Pro — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 11.564s | tokens_per_second: 125.4
- input_tokens: 3280 | output_tokens: 1450

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

**Conclusión: no se puede saber con estos datos si funcionó la secuencia.** Los resultados son compatibles con que ayudara, pero no demuestran que causara el crecimiento.

En marzo, el MRR subió **$1.200 (29,3%)** y las altas al plan pago pasaron de **9 a 14** (**+5; +56%**). Pero en ese mismo mes empezaste a pagar publicidad y un creador mencionó la comunidad. Además, faltan el número de usuarios gratuitos expuestos y las tasas de conversión. El cambio de MRR también puede reflejar cancelaciones, mejoras de plan u otros movimientos, no solo nuevas altas.

**Qué haría falta para saberlo mejor:**

- Comparar usuarios gratuitos similares asignados al azar: un grupo recibe la secuencia y otro no.
- Medir la conversión a pago en un plazo definido —por ejemplo, 30 días— y el MRR generado por usuario elegible.
- Registrar quién recibió cada email, cuándo convirtió y cómo llegó a la comunidad; así se pueden analizar también la publicidad y la mención del creador.
- Revisar cuántos usuarios hay en cada grupo y la incertidumbre de la diferencia: con pocas conversiones, el resultado puede variar mucho.

Si la secuencia ya se envió a todos y no hubo grupo de control, puedes revisar cohortes y fuentes de adquisición para obtener indicios, pero **no separar con seguridad el efecto de los emails** del de la publicidad, la mención y otros factores.