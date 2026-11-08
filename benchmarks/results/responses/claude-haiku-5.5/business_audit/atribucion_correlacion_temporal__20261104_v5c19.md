# Claude Haiku 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.12 | quality: 10.0
- latency_total: 9.875s | tokens_per_second: 174.9
- input_tokens: 366 | output_tokens: 1727

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

**Conclusión: no se puede saber si la secuencia funcionó.** Con estos datos, la subida es compatible con que la secuencia haya ayudado, pero también con que lo hayan causado la publicidad o el video del creador, o con que sea variación normal.

**Por qué no se puede atribuir:**

- **Tres cambios coincidieron en marzo.** La secuencia (1 de marzo), los anuncios (3 de marzo) y la mención del creador (12 de marzo) empezaron casi a la vez. Con solo el total mensual no hay forma de separar sus efectos.
- **La muestra es muy pequeña.** Pasar de 9 a 14 altas son 5 usuarios. Ese salto puede aparecer por azar con facilidad. Con números así, un mes más o un mes menos cambia mucho la lectura.
- **El MRR mezcla más que altas nuevas.** El +$1.200 incluye altas, bajas (churn), cambios de plan y posibles pagos anuales. Un mes con menos cancelaciones también puede subir el MRR sin que la secuencia haga nada.
- **No sabemos cuántos usuarios recibieron la secuencia ni cuántos la abrieron o hicieron clic.** Sin esas métricas no podemos ver si el mecanismo de la secuencia funcionó siquiera.

**Qué haría falta para estar seguros:**

1. **Altas diarias por fuente.** Si las altas se concentran después del 1 de marzo, apuntan a la secuencia. Si suben tras el 12 de marzo, apuntan al video. Si llegan con UTM o código de anuncio, apuntan a la publicidad.
2. **Métricas de la secuencia.** Cuántos usuarios entraron, cuántos abrieron, cuántos hicieron clic y cuántos de ellos pasaron a pago. Así sabemos si el canal se usó de verdad.
3. **Grupo de control.** La prueba más sólida: asignar al azar a una parte de los usuarios gratuitos a no recibir la secuencia y comparar la tasa de conversión a pago entre ambos grupos. Es la única forma de aislar el efecto de los emails.
4. **Desglose del MRR.** Separar nuevo MRR, churn, expansión y contracción, para ver si la subida viene de altas o de menos bajas.
5. **Más tiempo.** Uno o dos meses más de datos con la secuencia activa y sin cambios grandes de canal daría una señal algo más fiable. Con estos volúmenes, incluso eso puede ser insuficiente.

**Lo que sí puedo decir hoy:** la secuencia podría haber contribuido, pero no hay evidencia suficiente para atribuirle el crecimiento. Yo no la daría por exitosa ni fallida todavía, y no tomaría decisiones de inversión (por ejemplo, escalar la secuencia o gastar más en anuncios) sin al menos la comparación por fuente.

Si me compartes las altas por día y las métricas de apertura y clic de la secuencia, puedo ayudarte a revisar qué parte del crecimiento encaja con cada canal.