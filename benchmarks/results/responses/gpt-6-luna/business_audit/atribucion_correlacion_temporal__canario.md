# GPT-6 Luna — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.21 | quality: 10.0
- latency_total: 6.891s | tokens_per_second: 70.5
- input_tokens: 224 | output_tokens: 486

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

**Conclusión:** en marzo hubo una mejora observada, pero no se puede saber si la causó la secuencia de emails.

El MRR subió de **$4.100 a $5.300** (+$1.200, aproximadamente **29%**) y las altas al plan pago pasaron de **9 a 14** (+5; aproximadamente **56%**). Pero durante el mismo mes empezaste a pagar publicidad y un creador mencionó la comunidad. Además, esos datos no dicen cuántas altas vinieron de usuarios que recibieron los emails ni cuánto MRR aportaron.

Para estar más seguros:

- **Haz un grupo de control aleatorio:** asigna usuarios gratuitos elegibles a recibir la secuencia o a no recibirla, manteniendo iguales las demás condiciones.
- **Compara la conversión a pago** en ambos grupos durante el mismo plazo, por ejemplo, 30 días desde que cada usuario entra en la secuencia.
- Mide también **ingreso incremental, cancelaciones y retención**, no solo altas. Define de antemano qué resultado consideras éxito.
- Reúne suficientes usuarios para que la diferencia no pueda explicarse fácilmente por azar; calcula el tamaño de muestra según tu conversión habitual.

Con los datos actuales, la respuesta honesta es: **los resultados de marzo mejoraron, pero no hay evidencia suficiente para atribuir esa mejora a los emails**.