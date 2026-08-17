# GPT-5.6 Luna Pro — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 5.54 | quality: 5.0
- latency_total: 7.982s | tokens_per_second: 188.0
- input_tokens: 4567 | output_tokens: 1501

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador. Tienes acceso a herramientas pero algunas pueden fallar.
Cuando una herramienta falla, debes:
1. Diagnosticar por que fallo
2. Proponer una alternativa
3. Ajustar el plan general

**user:**

Necesito obtener los datos de ventas del mes pasado y enviar un resumen al equipo.

**assistant:**

Voy a consultar la base de datos para obtener los datos de ventas.

**tool:**

ERROR: Connection refused - database 'production' is currently under maintenance. Expected recovery: 2 hours.

**user:**

La base de datos esta en mantenimiento. Que hacemos? Necesito enviar el reporte antes de las 5pm.


## Respuesta completa

La consulta falló porque la base de datos `production` está en mantenimiento, con una recuperación estimada de 2 horas. Como el plazo es antes de las 17:00, propongo este plan:

1. **Usar una fuente alternativa inmediata**: réplica de solo lectura, almacén analítico, dashboard de BI o último archivo CSV/Excel exportado.
2. **Confirmar el período**: la consulta anterior asumía marzo de 2026 como “mes pasado”.
3. **Preparar el resumen** con ventas totales, número de pedidos, ticket promedio y comparación con el mes anterior.
4. **Enviar una versión preliminar** antes de las 17:00, indicando la fuente alternativa y que se validará contra producción cuando vuelva a estar disponible.
5. **Actualizar el reporte** después de la recuperación si hubiera discrepancias.

Necesito que me indiques una de estas alternativas para continuar:

- Nombre de la base de datos réplica o analítica.
- Ruta del último archivo exportado.
- URL del dashboard o API de ventas.
- Si no existe ninguna, los destinatarios del equipo y autorización para enviar un aviso de retraso con la hora estimada de recuperación.