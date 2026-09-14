# Mercury 2.5 — orchestration/error_recovery_orchestration

- model_id: `inception/mercury-2.5`
- success: True  | final: 4.6 | quality: 2.5
- latency_total: 0.934s | tokens_per_second: 219.4
- input_tokens: 1297 | output_tokens: 205

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

[tool_call] search_web({"query": "sales data export backup files", "max_results": 5})
[tool_call] read_file({"path": "/data/sales/sales_data_2026_03.csv"})
[tool_call] read_file({"path": "/data/exports/sales_export_2026_03.csv"})