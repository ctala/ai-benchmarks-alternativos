# Qwen 3.7 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.27 | quality: 10.0
- latency_total: 20.481s | tokens_per_second: 103.5
- input_tokens: 245 | output_tokens: 2120

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

**Conclusión directa:** No se puede saber con los datos que me proporcionas. Lo que tienes es una coincidencia temporal, no evidencia de causalidad.

### Por qué los números actuales no sostienen esa afirmación
1. **Tres factores concurrentes generan ruido crítico:** 
   - Inicias publicidad paga el 3 de marzo ($400).
   - Un creador con audiencia grande menciona la comunidad el 12 de marzo.
   - Lanzas la secuencia de emails el 1 de marzo.
   Todos estos eventos suelen disparar tráfico, visibilidad y conversiones simultáneamente. Sin desagregar el origen de cada nuevo pago, cualquier atribución a los emails es especulativa.

2. **El MRR y las "altas al pago" no miden lo mismo:** 
   - El salto de $4.100 a $5.300 en MRR puede provenir casi totalmente de nuevos suscriptores captados por ads o el video, no de usuarios del plan gratuito que hicieron upgrade.
   - Las conversiones pasaron de 9 a 14, pero sin conocer el tamaño de tu cohorte gratuita, la tasa de conversión histórica ni el momento exacto en que cada usuario recibió/respondió los emails, ese delta no es estadísticamente significativo ni atribuible.

3. **Falta trazabilidad y diseño de prueba:** 
   - No hay grupo de control (usuarios expuestos vs. no expuestos a la secuencia).
   - No se reportan métricas intermedias clave (tasa de apertura, clics, tiempo entre último email y conversión).
   - No se indica cómo estás rastreando la fuente de cada conversión (UTMs, canal primario, evento de atribución). En entornos multi-canal, atribuir todo a un touchpoint automático es un error común de análisis.

### Qué haría falta para estar seguros
- **Desglose de adquisición por fuente:** cuántos nuevos pagos vinieron de orgánico/freemium, de ads, de referencia del creador, y de otros canales.
- **Cohorte de conversión controlada:** comparar la tasa de upgrade de quienes sí recibieron la secuencia contra una cohorte similar que no la recibió (o contra febrero ajustado por estacionalidad y crecimiento orgánico histórico).
- **Atribución clara:** implementar UTM consistentes + panel de analytics que registre el primer contacto y el canal primario antes de la compra. Sin esto, cualquier conclusión es ruido.
- **Métricas de engagement con la secuencia:** aperturas, clics en CTAs, caída por etapa, y distribución temporal de conversiones respecto al día/número de email recibido.
- **Control de contexto operativo:** ¿cambiaste precios, límites del plan gratuito, experiencia de onboarding o capacidad de soporte en marzo? Cualquier variación externa distorsiona la señal.

### Recomendación operativa
Por ahora, etiqueta este lanzamiento como **experimento en curso**. La próxima vez:
1. Separa claramente los canales (ads, referencias orgánicas, emails) desde el click hasta la conversión.
2. Mantén un grupo de control equivalente durante la prueba.
3. Espera al menos 2-4 semanas después del último email para cerrar el ciclo de atribución.
4. Compara tasas de conversión por cohorte, no solo deltas absolutos.

Si quieres, puedo ayudarte a estructurar el seguimiento, definir las variables mínimas viables y armar un dashboard simple para tomar la decisión correctamente.