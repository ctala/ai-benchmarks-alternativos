# GLM 5.2 — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 31.588s | tokens_per_second: 48.9
- input_tokens: 235 | output_tokens: 1544

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

**Conclusión: No se puede saber si la secuencia de emails funcionó.**

Los datos muestran un crecimiento real y positivo (el MRR subió un 29% y las altas pasaron de 9 a 14), pero es imposible atribuir ese éxito a la secuencia de emails con la información actual. 

El motivo principal es que tienes tres variables que ocurrieron al mismo tiempo (la secuencia de emails, la inversión en publicidad y el video del creador). Cualquiera de las tres —o la combinación de ellas— podría explicar las 5 altas adicionales. Es muy probable que las altas vengan de los nuevos usuarios que atrajo el creador o la publicidad, y no de los usuarios gratuitos que recibieron los correos.

Para poder afirmar con seguridad que la secuencia de emails funcionó (y para saber si merece la pena mantenerla o mejorarla), haría falta lo siguiente:

1. **Atribución por canal (Lo más urgente):** Necesitamos saber de dónde vienen exactamente esas 14 altas de marzo. ¿Cuántas vinieron de la publicidad? ¿Cuántas del video del creador? ¿Cuántas de los usuarios gratuitos existentes? Si de las 14 altas, 10 vinieron del video y 4 de la publicidad, y 0 vinieron de usuarios que ya estaban en el plan gratuito, la secuencia de emails no funcionó.
2. **Métricas de la secuencia de emails:** ¿Cuántos usuarios gratuitos recibieron los correos? ¿Cuántos los abrieron? ¿Cuántos hicieron clic en el enlace de upgrade? Necesitamos ver el embudo de conversión específico de esa secuencia.
3. **Seguimiento con UTM o etiquetas:** Los enlaces dentro de los emails deben tener etiquetas de seguimiento específicas para saber si un usuario que se dio de alta al plan pago lo hizo después de hacer clic en uno de esos 5 correos.
4. **Análisis temporal:** Necesitamos las fechas exactas de las 14 altas. Si la mayoría de las altas ocurrieron entre el 12 y el 15 de marzo, el impulso fue del creador. Si ocurrieron escalonadamente justo después de que saliera cada email, hay un mejor indicio de que la secuencia ayudó.
5. **Un grupo de control (Para el futuro):** Para medir esto correctamente la próxima vez, habría que dividir a los usuarios gratuitos en dos grupos. Al Grupo A se le envía la secuencia y al Grupo B no. Si el Grupo A se convierte al plan pago a una tasa significativamente mayor que el Grupo B, entonces sabremos con certeza que los emails funcionan.

En resumen: los negocios van bien, pero no podemos darle el mérito a los emails sin aislar el ruido que generaron la publicidad y el creador. Si me consigues el desglose de origen de esas 14 altas, te puedo dar una respuesta definitiva.