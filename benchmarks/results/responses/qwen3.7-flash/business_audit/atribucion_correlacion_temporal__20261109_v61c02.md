# Qwen 3.7 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 30.458s | tokens_per_second: 72.2
- input_tokens: 245 | output_tokens: 2198

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

Con la información que compartes, **no se puede saber** si la secuencia de emails funcionó. Lo que sí sabemos es que entre febrero y marzo hubo un aumento de MRR y de nuevas altas, pero ese cambio coincide con al menos dos estímulos externos simultáneos y no tenemos forma de aislar su efecto.

### 🔍 Por qué no podemos atribuir el crecimiento a la secuencia
1. **Variables de confusión no controladas**: 
   - Inversión publicitaria ($400) iniciada el 3 de marzo.
   - Mención orgánica de un creador con audiencia grande el 12 de marzo.
   Ambos son fuentes potenciales de tráfico y conversión que actúan en paralelo con los emails.

2. **Falta de métricas de ejecución de la secuencia**:
   - No sabemos cuántos usuarios del plan gratuito fueron alcanzados, cuántos abrieron los correos o hicieron clic en los enlaces de pago. Sin tasas de apertura, clics o conversiones directas desde la secuencia, no hay puente causal.

3. **Origen de las nuevas altas desconocido**:
   - Pasar de 9 a 14 altas mensuales es un salto, pero no sabemos si provienen de la secuencia, de la publicidad, del video, o de tráfico directo/orgánico. Además, el MRR subió $1.200, lo cual podría deberse a upgrades de usuarios existentes, menor churn, o cambios en precios, no necesariamente a las 14 nuevas altas.

4. **Ausencia de línea base y grupo de control**:
   - No hay datos históricos de meses anteriores para ver si marzo suele tener picos naturales.
   - No se aplicó la secuencia a un grupo comparable que sirva como contraparte (control), por lo que no podemos comparar `con secuencia` vs `sin secuencia`.

### 📊 Qué hace falta para estar seguros
- **Desagregación por canal de adquisición**: Implementa UTM, preguntas en el formulario de registro o integración con analytics para saber de dónde viene cada alta. Sin esto, cualquier atribución es suposición.
- **Métricas específicas de la secuencia**: Entregados, tasa de apertura, clics por email, y conversiones atribuibles (eventos de compra marcados con parámetros de la campaña).
- **Prueba controlada o A/B**: Lanza la misma secuencia a un 50% de tu base gratuita restante y compárala con el otro 50% que no la reciba. Mide conversiones a 7, 14 y 30 días.
- **Validación de sostenibilidad**: Revisa churn, cancelaciones y actividad post-conversión para descartar que el aumento sea un pico temporal o compensado por pérdida de usuarios después.
- **Cálculo de impacto económico**: Compara los ingresos atribuibles a la secuencia vs. costos de producción/distribución y vs. el rendimiento de la publicidad ($400 invertidos). Solo así sabrás si vale la pena escalarla o sustituirla.

### ✅ Recomendación inmediata
No tomes decisiones de inversión o escalado basadas en este mes hasta tener al menos dos cosas:
1. Tracking claro del origen de cada alta.
2. Una prueba A/B o un grupo de control que permita medir el efecto marginal de la secuencia.

Mientras tanto, trata el resultado como **una señal correlacional, no causal**. Si quieres, puedo ayudarte a diseñar el setup de medición o la estructura de la próxima prueba A/B para que tengas una respuesta robusta en 14-30 días.