# Qwen 3.6 27B base (OpenRouter FP8) — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.39 | quality: 8.4
- latency_total: 25.365s | tokens_per_second: 80.7
- input_tokens: 245 | output_tokens: 2048

## Respuesta completa

**Conclusión directa:** Con los datos que compartes, **no se puede saber** si la secuencia de emails fue la causa del aumento. Hay correlación temporal, pero no evidencia de causalidad.

### 🔍 Por qué no se puede atribuir con seguridad
1. **Variables simultáneas no aisladas:** En las mismas dos semanas se lanzaron tres iniciativas con potencial de conversión: emails (1 mar), publicidad pagada (3 mar) y mención de un creador (12 mar). Sin tracking de atribución, es imposible separar qué porcentaje del aumento corresponde a cada una.
2. **Tamaño muestral pequeño:** Pasaste de 9 a 14 altas. Son solo **5 usuarios adicionales**. Con volúmenes bajos, la variación natural, un día pico de tráfico orgánico o incluso un solo usuario que compró en un momento diferente al habitual pueden explicar el cambio sin necesidad de invocar el email.
3. **El MRR no dice de dónde viene:** Un aumento de $1.200 puede provenir de nuevas altas, de usuarios existentes que cambiaron de plan, de una reducción en el churn, o incluso de un ajuste de precios. Sin desglose, no se puede vincular al flujo de emails.
4. **Falta de métricas de la secuencia:** No compartes aperturas, clics, tasa de conversión desde el email, ni si hay tracking de eventos. Sin eso, no sabes si la secuencia siquiera fue vista o si generó intención de compra.

### 📊 Qué haría falta para estar seguros
- **Atribución por fuente:** UTM en cada enlace de los emails, parámetros de campaña en tu plataforma de pagos, o códigos únicos por canal. Así podrías ver cuántas de las 14 altas llegaron específicamente desde el email.
- **Desglose del MRR:** Separar nuevas altas vs. upgrades de usuarios existentes vs. churn reducido. Idealmente, con fecha y plan asociado.
- **Métricas de la secuencia:** Aperturas, clics, y conversión rastreada (ej. evento `upgrade_from_email` en tu analítica).
- **Línea base o grupo de control:** Comparar marzo con meses anteriores en condiciones similares, o mantener un % de usuarios gratuitos que no reciban la secuencia para medir el lift real.
- **Datos de tráfico y conversión por canal:** Cuántas visitas y altas vinieron de orgánico, ads, influencer y email en marzo.

### ✅ Qué te recomiendo hacer ahora
1. **No asumas causalidad.** Escalar presupuesto o rediseñar la funnel bas