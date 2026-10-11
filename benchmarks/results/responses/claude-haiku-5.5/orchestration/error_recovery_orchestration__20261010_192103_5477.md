# Claude Haiku 5.5 — orchestration/error_recovery_orchestration

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 5.91 | quality: 5.0
- latency_total: 3.516s | tokens_per_second: 151.6
- input_tokens: 1662 | output_tokens: 533

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

La base `production` está caída por mantenimiento, con recuperación estimada en 2 horas. Antes de buscar alternativas, tengo que corregir algo: en la consulta anterior puse `'2026-03'` como mes sin confirmarlo. No sé la fecha actual ni cuál es el "mes pasado" para ti, así que esa consulta podría haber apuntado al periodo equivocado.

Voy a probar una réplica de solo lectura, si existe, y ver si hay un reporte ya generado.