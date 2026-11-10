# GPT-OSS 20B — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.65 | quality: 7.5
- latency_total: 2.402s | tokens_per_second: 74.9
- input_tokens: 612 | output_tokens: 180

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

We have tool failure: database unavailable. Need alternative. Could fetch from backup, use a cached copy, or logic: use earlier month. Provide plan.

We can also search web for a backup dataset? maybe not possible. Could query a REST API that provides sales data? Or call "run_script" to run Python to query via an API gateway. For now I'll propose to fetch from a backup database named 'sales_backup' if exists.

We need to send email. So write or read file maybe use a template. Determine best approach: Use backup DB. Alternatively, if no backup, maybe fallback to a flat file stored in repository (sales_mar.csv). Use read_file to check.

Let's first search repository for file.