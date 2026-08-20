# Gemini 3.7 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 11.382s | tokens_per_second: 99.0
- input_tokens: 221 | output_tokens: 1127

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

**Conclusión directa: No se puede saber.** 

Decir que la secuencia de emails funcionó basándonos en estos números sería engañarnos. Aunque el negocio creció en marzo, es imposible atribuirle ese éxito a los emails por tres razones críticas:

### Por qué los datos actuales no sostienen esa conclusión

1. **Factores de confusión graves (ruido externo):** Lanzaste anuncios de pago ($400) el 3 de marzo y recibiste la mención de un influencer el 12 de marzo. Ambos eventos inyectaron tráfico nuevo y con alta intención de compra en el mismo período. El aumento de ingresos y altas puede deberse 100% a la publicidad, 100% al influencer, o a una mezcla de todo.
2. **Volumen de muestra muy pequeño:** Pasaste de 9 a 14 altas. Una diferencia de **5 conversiones** en un mes es estadísticamente insignificante a este nivel; podría ser simple variabilidad natural del mes a mes.
3. **Cero datos de atribución:** No tenemos métricas intermedias de los emails (aperturas, clics, conversiones rastreadas desde los enlaces del correo). 

---

### Qué hace falta para estar seguros

Para evaluar el impacto real de la secuencia necesitas aislar su efecto. Esto es lo mínimo necesario:

1. **Atribución directa (Enlaces UTM):**
   * Configurar enlaces con parámetros UTM en los 5 emails para saber exactamente cuántas de esas 14 personas hicieron clic en un correo antes de pagar.
2. **Métricas de embudo del email:**
   * ¿Cuántos usuarios gratuitos entraron a la secuencia?
   * Tasa de apertura y tasa de clics (CTR) por correo. Si nadie hace clic en los correos, la secuencia no generó las ventas.
3. **Un grupo de control (Prueba A/B):**
   * Dividir a los nuevos usuarios gratuitos: al 50% le envías la secuencia y al otro 50% no (o les envías solo un correo de bienvenida). Si el grupo con la secuencia convierte a plan de pago a una tasa significativamente mayor, entonces sí funciona.
4. **Separación por canales de adquisición:**
   * Analizar la tasa de conversión histórica de los usuarios gratuitos *antes* de que existiera el tráfico del influencer y de los anuncios.