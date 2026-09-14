# Muse Glimmer 30B — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 34.054s | tokens_per_second: 46.4
- input_tokens: 237 | output_tokens: 1579

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

No, con esos números no se puede saber si la secuencia de emails funcionó.

Tienes un resultado positivo — MRR +29% y +5 altas al pago vs febrero — pero tienes **tres intervenciones simultáneas en el mismo mes** y sin grupo de control:

* 1 de marzo: secuencia de 5 emails a gratis
* 3 de marzo: empiezas publicidad por $400/mes
* 12 de marzo: mención de un creador con audiencia grande

Con eso es imposible separar qué parte del +$1.200 de MRR y de las 14 altas viene de los emails y qué parte de la publicidad o del creador. Es correlación, no causalidad.

Además con lo que pasaste no se puede ni siquiera estimar un efecto parcial:
* No sabemos cuántos usuarios gratuitos había el 1 de marzo y cuántos recibieron realmente la secuencia.
* No sabemos la tasa de conversión gratis → pago de ese grupo, ni opens/clicks/conversiones de los emails.
* El MRR puede subir por nuevas altas, por upsells o por menor churn, y no sabemos de dónde vino ese +29%.
* Febrero a Marzo es una comparación de 1 mes vs 1 mes. No sabemos cuál es la variabilidad normal.

Para poder decir si la secuencia funcionó haría falta aislar el efecto:

1. **Un experimento limpio.** Randomizar usuarios gratuitos en dos grupos iguales: Grupo A recibe la secuencia, Grupo B no la recibe. Comparar tasa de conversión a pago y MRR generado por ambos grupos en el mismo periodo. Sin holdout no hay contra-factual.

2. **Atribución por canal.** UTM / source en el signup para saber si la conversión vino de email, ads o referral del creador. Y métricas de la secuencia: entregados, abiertos, clics, conversiones atribuidas y revenue atribuido.

3. **Cohortes y ventana temporal.** Ver conversión de usuarios que entraron a gratis antes del 1 de marzo y fueron expuestos a la secuencia vs los que no. Y mirar el efecto día a día: la secuencia empieza 1/3, la publicidad 3/3 y el creador 12/3. Si el salto ocurre justo el 12/3 es más probable que sea el creador.

4. **Estadística básica.** Con 9 vs 14 altas estás hablando de 5 eventos. Eso está dentro del ruido normal de una comunidad pequeña. Necesitarías varias semanas de datos y una prueba de significancia.

Conclusión honesta hoy: **No se puede saber.** El mes fue bueno, pero no puedes atribuirlo a los emails con seguridad. Lo más responsable es no vender internamente que la secuencia funcionó y diseñar un test A/B controlado para la próxima iteración.

Si quieres, te ayudo a armar el diseño del experimento y el mínimo de métricas a recoger para la próxima vez.