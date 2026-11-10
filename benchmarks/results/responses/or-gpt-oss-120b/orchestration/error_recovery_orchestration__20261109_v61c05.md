# GPT-OSS 120B — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.35 | quality: 7.5
- latency_total: 5.512s | tokens_per_second: 35.6
- input_tokens: 613 | output_tokens: 196

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

We need to handle failure. Diagnose: DB under maintenance, cannot query. Alternatives: maybe there's a backup or a reporting API, or could retrieve from cached file, or use a different DB (like a replica). We could request from an alternative source, maybe a CSV export stored on server. Could also generate placeholder report indicating data unavailable then send with note. We need to send before 5pm. Could ask user for alternative source, but we can try to check for a recent sales report file, maybe /reports/sales_last_month.csv. Use read_file. Then generate summary. Then send email.

Plan: try read_file for that path. If fails, then maybe fallback to calling an external API endpoint for sales data. Or if that fails, we can send email notifying of unavailability.

We'll attempt read_file.