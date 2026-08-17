# GPT-5.6 Terra — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 7.55 | quality: 8.57
- latency_total: 5.404s | tokens_per_second: 81.1
- input_tokens: 532 | output_tokens: 438
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece un plan detallado y bien estructurado para manejar la indisponibilidad de datos, proporcionando alternativas prácticas y pasos claros para la recuperación y validación de datos.

## Respuesta completa

La consulta falló porque la base `production` está en mantenimiento y no aceptará conexiones hasta dentro de unas 2 horas. Reintentar ahora no resolvería el problema.

**Plan ajustado para llegar antes de las 5pm:**

1. **Usar una fuente alternativa**, en este orden:
   - Réplica de solo lectura / *data warehouse* (por ejemplo, `analytics`, `reporting` o `sales_replica`).
   - Dashboard de BI con exportación de ventas de marzo.
   - Exportación diaria/cierre mensual almacenado en Drive, S3 o un sistema de facturación/CRM.
2. **Validar el corte:** confirmar que la fuente incluye del **1 al 31 de marzo** y comparar al menos el total con el último cierre disponible.
3. **Enviar un resumen provisional antes de las 5pm**, indicando la fuente y, si hiciera falta, que los datos se confirmarán cuando vuelva la base.
4. **Conciliar después del mantenimiento**; si hay diferencias, enviar una corrección puntual.

Necesito saber cuál de estas fuentes alternativas tienen disponible —réplica, warehouse, dashboard o archivo de cierre— para extraer los datos. Si no hay ninguna, la opción más segura es enviar al equipo una nota antes de las 5pm explicando la indisponibilidad y comprometiendo el reporte validado apenas se recupere el acceso.