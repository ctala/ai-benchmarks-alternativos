# Qwen 3.6 35B base (OpenRouter FP8) — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 5.93 | quality: 6.0
- latency_total: 22.665s | tokens_per_second: 90.4
- input_tokens: 245 | output_tokens: 2048

## Respuesta completa

**Conclusión directa:** No se puede saber. Los datos que me compartes muestran un crecimiento en marzo, pero no permiten atribuirlo a la secuencia de emails.

### Por qué los datos actuales no sostienen esa conclusión
1. **Confundidores temporales claros:** Lanzaste la secuencia el 1 de marzo, pero el 3 de marzo iniciaste publicidad paga y el 12 de marzo hubo una mención de un creador con audiencia grande. Todos estos factores pueden generar conversiones simultáneas o acumuladas. Sin atribución, no hay forma de separar su impacto.
2. **Correlación ≠ causalidad:** El salto de 9 a 14 conversiones y el +29% de MRR son indicadores positivos, pero son agregados. No sabemos si las conversiones vinieron de usuarios que recibieron los emails, de los que llegaron por ads, o de los que llegaron por el video.
3. **Falta de métricas de exposición y engagement:** No tengo tasa de entrega de emails, aperturas, clics, ni volumen real de la base gratuita expuesta. Sin saber cuántos usuarios vieron la secuencia y cómo interactuaron, no hay base para calcular su efectividad.
4. **Ausencia de línea base y grupo de control:** No conozco la tasa de conversión histórica free → paid antes del 1 de marzo, ni un grupo comparable que no recibiera la secuencia. Sin eso, cualquier cambio mensual puede deberse a estacionalidad, variación natural o factores externos.

### Qué haría falta para estar seguros
Para pasar de “parece que funcionó” a “la secuencia generó X impacto”, necesitarías:

1. **Atribución por canal:** Marcar en tu CRM/analytics la fuente de cada conversión (email, ads, orgánico, video, referral). Usa UTM, códigos de descuento exclusivos o landing pages diferenciadas para ads y el video.
2. **Segmentación de la secuencia:** Saber cuántos usuarios gratuitos recibieron los emails, cuántos abrieron/clickearon, y comparar su tasa de conversión vs. quienes no los recibieron.
3. **Prueba controlada (A/B o cuasi-experimento):** Enviar la secuencia solo a un 40-50% de la base gratuita durante el próximo ciclo, manteniendo ads y contenido orgánico estables. Compara la tasa de conversión entre el grupo expuesto y el grupo control.
4. **Métricas base y cohortes:** Registrar la conversión histórica free → paid, el volumen mensual de usuarios gratuitos, y analizar cohortes por fecha de registro para ver si la secuencia afecta a nuevos vs. antiguos usuarios.
5. **Medición de impacto de los otros factores:** Rastrear el ROI y la tasa de conversión de los ads ($400) y del video por separado. Si el video generó un pico puntual, puedes aislarlo temporalmente y ver si la secuencia mantiene su efecto después.

### Cierre analítico
Mientras no tengas atribución por canal, segmentación de exposición y un diseño que permita comparar grupos, cualquier afirmación de que “la secuencia funcionó” sería una suposición cómoda, no un hallazgo respaldado por datos. Lo correcto es seguir midiendo, registrar la exposición y