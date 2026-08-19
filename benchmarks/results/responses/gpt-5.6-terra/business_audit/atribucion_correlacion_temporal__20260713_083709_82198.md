# GPT-5.6 Terra — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 5.53 | quality: 6.0
- latency_total: 11.314s | tokens_per_second: 94.2
- input_tokens: 224 | output_tokens: 1066

## Respuesta completa

**Conclusión:** con estos datos **no se puede saber si la secuencia de emails funcionó** en el sentido causal.

Sí se observa una mejora durante marzo:

- MRR: de **$4.100 a $5.300** (**+$1.200; +29%**).
- Altas de pago: de **9 a 14** (**+5; +56%**).

Pero esa mejora coincide con al menos dos intervenciones relevantes:

1. Publicidad pagada desde el 3 de marzo ($400).
2. Mención de un creador grande el 12 de marzo.

Por tanto, atribuir el aumento a los emails sería confundir correlación temporal con impacto causado. Además:

- El MRR no mide solo nuevas altas: puede incluir upgrades, bajas, reactivaciones, descuentos o cambios de precio.
- Pasar de 9 a 14 altas es una diferencia de solo 5 personas; podría deberse parcialmente a variación normal de un mes a otro.
- La publicidad y la mención probablemente trajeron usuarios nuevos, mientras que la secuencia se envió a usuarios gratuitos existentes. Sin saber de dónde proceden las conversiones, no podemos separar efectos.

## Lo que sí se puede afirmar

La secuencia **estuvo activa durante un mes en el que crecieron las altas y el MRR**, pero **no hay evidencia suficiente para afirmar que produjo ese crecimiento**.

## Qué haría falta para evaluarla mejor

### Opción ideal: experimento con grupo de control

Dividir aleatoriamente a los usuarios gratuitos elegibles en dos grupos:

- **Tratamiento:** recibe la secuencia de 5 emails.
- **Control:** no la recibe, o recibe la comunicación habitual.

Después comparar, durante una ventana definida —por ejemplo, 30 días desde que cada usuario entra al experimento—:

- Tasa de conversión a pago.
- MRR nuevo por usuario elegible.
- Tiempo hasta conversión.
- Bajas o reembolsos posteriores, si aplica.

Ejemplo: si convierte el 6% del grupo con emails y el 3% del grupo control, y la diferencia es suficientemente grande para el tamaño de muestra, habría evidencia de impacto incremental.

Importante: analizar por **asignación inicial** (quién fue incluido en cada grupo), no solo por quién abrió o hizo clic. Quienes abren emails suelen ser ya más activos; comparar abiertos vs. no abiertos no demuestra que el email causó la compra.

### Datos útiles para un análisis retrospectivo

Aunque no permitirían certeza total, ayudarían a estimar mejor:

1. **Usuarios elegibles para la secuencia**
   - Cuántos usuarios gratuitos había el 1 de marzo.
   - Cuántos recibieron cada email.
   - Fechas exactas de entrada de cada usuario a la secuencia.

2. **Conversiones por usuario**
   - Fecha de alta al plan pago.
   - Si ya era usuario antes de marzo o llegó durante marzo.
   - Qué emails recibió antes de convertir.

3. **Origen de adquisición**
   - UTM, códigos, landing pages o encuesta de “¿cómo nos conociste?”.
   - Altas atribuibles a publicidad.
   - Altas atribuibles al creador.
   - Altas orgánicas/directas.

4. **Descomposición del cambio de MRR**
   - MRR nuevo por nuevas altas.
   - Expansiones o upgrades.
   - Churn y contracciones.
   - Reactivaciones.
   - Descuentos o cambios de precio.

5. **Comparación histórica**
   - Altas semanales o diarias de varios meses previos, no solo febrero.
   - Estacionalidad y tendencias previas.
   - Conversión histórica de usuarios gratuitos a pago.

Con esos datos se podría hacer un análisis aproximado —por ejemplo, comparar conversiones de usuarios gratuitos existentes antes del 1 de marzo contra cohortes similares anteriores—, pero seguirían existiendo sesgos por la publicidad y la mención del creador.

**Recomendación práctica:** mantener la secuencia, pero implementar desde ahora un holdout aleatorio, por ejemplo del 10–20% de usuarios gratuitos. Es la forma más fiable de saber si los emails generan conversiones adicionales y no solo coinciden con ellas.