# GPT-6 Luna — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.21 | quality: 10.0
- latency_total: 6.835s | tokens_per_second: 70.1
- input_tokens: 224 | output_tokens: 479

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

**Conclusión: no se puede saber con estos datos si la secuencia funcionó.** Las cifras mejoraron en marzo —el MRR subió $1.200 (+29%) y las altas pasaron de 9 a 14 (+56%)—, pero eso no demuestra que los emails causaran la mejora.

En marzo también empezaste a pagar $400 en publicidad y un creador mencionó la comunidad. Cualquiera de esas acciones, o una combinación, pudo influir. Además, el MRR puede cambiar por renovaciones, cancelaciones o cambios de plan, no solo por nuevas altas.

**Para medir el efecto con más seguridad:**

- En un próximo envío, asigna aleatoriamente usuarios gratuitos comparables a dos grupos: uno recibe la secuencia y otro no.
- Compara la conversión a pago en un plazo definido —por ejemplo, 30 días— y también los ingresos generados por usuario.
- Mantén iguales, en lo posible, las demás acciones comerciales durante la prueba.
- Reúne suficientes usuarios para que la diferencia no dependa de unos pocos casos; el tamaño necesario depende de la conversión habitual y del efecto que quieras detectar.

Para analizar lo que ya ocurrió, harían falta datos por usuario: quién recibió cada email y cuándo, quién se convirtió y cuándo, y qué exposición tuvo a la publicidad o al video. Eso ayudaría a reconstruir el resultado, pero sin un grupo de comparación fiable seguiría siendo difícil separar el efecto de la secuencia del de las otras acciones.