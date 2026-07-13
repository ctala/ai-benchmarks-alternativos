# Kimi K2 Thinking (NIM) — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2-thinking`
- success: True  | final: 5.25 | quality: 4.8
- latency_total: 5.603s | tokens_per_second: 195.1
- input_tokens: 269 | output_tokens: 1093

## Respuesta completa

**Conclusión: No se puede saber.** Los datos que presentas no permiten atribuir el aumento a los emails, y decir que "funcionó" sería una conclusión falsa y cómoda.

Aquí está el problema:

### Tres variables interfirieron simultáneamente
Tu secuencia no fue el único cambio en marzo. Tuviste **tres intervenciones** en 12 días:
1. Emails (1 de marzo)
2. Publicidad pagada (3 de marzo)
3. Mención de creador (12 de marzo)

Cualquiera de estas tres pudo haber causado las 5 altas extra. Es imposible desentrañar cuánto correspondió a cada una.

### Los números son demasiado pequeños para ser concluyentes
- 14 altas vs 9 es una diferencia de **solo 5 conversiones**
- Con un efecto tan pequeño, una o dos conversiones por cualquier otro motivo (referidos orgánicos, efecto mes a mes, etc.) ya distorsionan el resultado
- El error estándar es enorme: si las conversiones siguen una distribución aleatoria, esa variación podría ser pura fluctuación natural

### No tienes métricas de la base relevante
- ¿Cuántos usuarios gratuitos recibieron la secuencia?
- ¿Cuál era tu tasa de conversión histórica de gratuito a pago *antes* de la secuencia?
- ¿Cuántos de los 14 pagos en marzo provenían de usuarios antiguos vs nuevos?

Sin esto, no sabes si el 29% de crecimiento vino de activar usuarios dormidos o de nuevos usuarios que llegaron por la publicidad/mención.

---

## ¿Qué haría falta para estar seguros?

**Diseño experimental mínimo:**
1. **Grupo de control**: Usuarios gratuitos que *no* reciben la secuencia (aleatoriamente seleccionados)
2. **Métrica directa**: Conversiones específicas de la secuencia (usuarios que recibieron email -> pagaron)
3. **Tiempo de espera**: Al menos 2-3 meses sin otros cambios masivos (publicidad, menciones)
4. **Tamaño muestral**: Necesitas mínimo 50-100 conversiones por variante para reducir el ruido

**Alternativa retroactiva (menos robusta pero posible):**
- Segmentar los 14 pagos de marzo por fuente: ¿cuántos usaban la comunidad desde antes del 1 de marzo? ¿cuántos llegaron después de la mención?
- Analizar cohortes: comparar conversión de usuarios que llegaron en enero (solo recibieron email) vs usuarios que llegaron después del 12 de marzo (mención + email)

**Pregunta clave que no puedo responder con tus datos:** ¿Cuántos de esos 14 pagos eran usuarios que *ya estaban* en el plan gratuito antes del 1 de marzo?

Si no lo sabes, cualquier conclusión es especulación.