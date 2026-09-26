# GPT-6 Luna Pro — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 7.6 | quality: 8.0
- latency_total: 16.624s | tokens_per_second: 101.2
- input_tokens: 3218 | output_tokens: 1683

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

**Conclusión: con estos datos no se puede saber si la secuencia de emails funcionó.** Sí sabemos que marzo fue mejor que febrero: hubo 14 altas de pago frente a 9, y el MRR subió de $4.100 a $5.300. Pero eso es una comparación antes/después, no prueba que los emails causaran la mejora.

La publicidad empezó el 3 de marzo y hubo una mención de un creador el 12 de marzo. Cualquiera de esas acciones —o ambas— pudo contribuir. Además, el cambio de MRR también puede depender de bajas, ampliaciones de plan u otros factores; las altas totales no indican qué hizo cada canal.

**Para evaluarlo con más seguridad:**

- Separaría al azar a los usuarios gratuitos elegibles: un grupo recibe la secuencia y otro no. Compararía sus tasas de conversión en el mismo plazo.
- Registraría cuántos usuarios fueron asignados y expuestos, cuándo recibieron cada email y cuándo pasaron a pago.
- Definiría de antemano el resultado a medir —por ejemplo, conversión a pago en 30 días— y también el MRR incremental y el coste por conversión.
- Mantendría identificadas por separado las exposiciones a anuncios y a la mención del creador. Las atribuciones por clic ayudan, pero por sí solas no demuestran causalidad.

Si no hubo grupo de control, los datos de apertura, clics y atribución pueden servir para explorar, pero la conclusión honesta seguiría siendo: **los resultados mejoraron en marzo; no sabemos cuánto, si acaso, se debió a la secuencia.**