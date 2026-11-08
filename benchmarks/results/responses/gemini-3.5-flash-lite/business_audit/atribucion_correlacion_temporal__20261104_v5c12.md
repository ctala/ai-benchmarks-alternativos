# Gemini 3.5 Flash Lite — business_audit/atribucion_correlacion_temporal

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 3.079s | tokens_per_second: 188.4
- input_tokens: 221 | output_tokens: 580

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

Como analista de datos, mi respuesta directa y sin rodeos es: **No se puede saber.** 

Los datos que me das muestran que el negocio creció en marzo (más MRR y más altas), pero **es estadísticamente imposible aislar el impacto de los emails** a partir de esta información. 

### ¿Por qué los datos no sostienen que los emails funcionaron?

Tenemos un problema clásico de atribución. En marzo ocurrieron tres cosas al mismo tiempo (variables confusoras):
1. Lanzaste la secuencia de emails.
2. Empezaste a pagar publicidad ($400).
3. Un creador con audiencia grande mencionó la comunidad.

Cualquiera de estos tres factores —o una combinación de ellos— pudo haber traído a las 14 altas de marzo. 
* ¿Los nuevos usuarios compraron por leer el email 3, por hacer clic en el anuncio de pago, o porque llegaron desde el video del creador? Con estos datos, es adivinanza, no análisis.

Además, hay otra métrica invisible: **la correlación no es causalidad**. El hecho de que el MRR subiera un 29% después del 1 de marzo no prueba que el gatillo fuera la secuencia. Pudo haber sido estacionalidad del mercado, por ejemplo.

---

### ¿Qué haría falta para estar seguros de que la secuencia funcionó?

Para poder medir el éxito real de los emails y dejar de adivinar, necesitaríamos:

1. **Atribución por enlace (UTMs):** Que los botones de pago dentro de los emails hubieran tenido parámetros UTM únicos (ej. `?utm_source=email&utm_medium=secuencia_gratis`). Así podríamos ver exactamente cuántos clics y, sobre todo, cuántas *compras* vinieron directamente de ahí, diferenciándolas de los clics de la publicidad o del video del creador.
2. **Grupo de control (A/B testing):** Haber enviado la secuencia solo a un porcentaje aleatorio de los usuarios gratuitos (ej. 50%) y al otro 50% no enviarle nada (o un email genérico). Si el grupo con la secuencia convertía estadísticamente mucho más que el grupo de control, tendríamos prueba de causalidad.
3. **Datos de comportamiento:** Saber cuántos usuarios llegaron al final de la secuencia, qué tasa de apertura tuvieron y en qué email exacto se produjo la conversión.

**Conclusión:** Tu negocio fue mejor en marzo, felicidades por eso. Pero afirmar que la secuencia de emails fue la causa es una conclusión cómoda, no una conclusión basada en datos. Si repetimos esto el mes que viene sin medir mejor, estaremos tomando decisiones a ciegas.