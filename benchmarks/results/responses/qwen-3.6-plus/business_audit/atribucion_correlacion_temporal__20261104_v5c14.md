# Qwen 3.6 Plus — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 34.928s | tokens_per_second: 57.3
- input_tokens: 245 | output_tokens: 2002

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

**Conclusión directa:** Con los datos que me compartes, **no se puede saber** si la secuencia de emails funcionó.

**Por qué:**
1. **Múltiples intervenciones simultáneas:** En marzo lanzaste emails (1 mar), pagaste publicidad (3 mar) y recibiste una mención de un creador grande (12 mar). Los +$1.200 de MRR y los +5 nuevos pagos son el resultado combinado de estas tres acciones (más cualquier tendencia orgánica o estacional). Sin atribución, es matemáticamente imposible repartir el crédito.
2. **Falta de trazabilidad:** No hay forma de saber cuántos de los 14 nuevos pagos vinieron por clic en un email, por el anuncio, por el video o por búsqueda directa. Un solo pago puede venir de dos o tres canales distintos.
3. **Muestra muy pequeña:** Pasar de 9 a 14 altas es una variación absoluta de +5. Con volúmenes así, una sola decisión de compra (o una baja) distorsiona completamente el porcentaje. No hay base estadística para afirmar causalidad.
4. **Sin métricas de funnel ni grupo de control:** No sabemos cuántos usuarios vieron los emails, cuántos hicieron clic, cuántos llegaron a la pasarela de pago ni qué tasa de conversión tuvieron. Tampoco hay un grupo de referencia que no haya recibido la secuencia para comparar.

**Qué haría falta para estar seguros:**
- ✅ **Atribución por canal:** UTM en enlaces de emails, landing page o código de descuento exclusivo para la secuencia, y tracking de origen en el checkout.
- ✅ **Grupo de control (A/B test):** Retener aleatoriamente el 30-50% de los usuarios gratuitos sin enviarles la secuencia y comparar tasas de conversión a 30/60 días.
- ✅ **Métricas de engagement:** Apertura, CTR, clics únicos, rebotes y conversión post-clic. Sin ellas, solo medimos resultado final, no eficacia del canal.
- ✅ **Análisis de cohortes + tiempo:** Cruzar fecha de alta con fecha de envío de cada email y con picos de tráfico de ads/creator. Observar al menos 2 ciclos completos para descartar estacionalidad o efecto de novedad.
- ✅ **Cálculo de CAC/ROI por canal:** La publicidad tiene costo directo ($400), el email casi nulo. Saber cuántos pagos pagó cada canal permite priorizar con evidencia, no con intuición.

**Recomendación práctica ahora mismo:** 
No asumas que funcionó ni la desactives. Implementa tracking básico esta semana (UTM + campo "¿cómo nos conociste?" en el checkout o código exclusivo). En el próximo mes, compara conversión de usuarios expuestos vs. no expuestos. Hasta que tengas eso, cualquier afirmación sobre el impacto de la secuencia es especulación, y en datos pequeños la especulación suele costar decisiones equivocadas.