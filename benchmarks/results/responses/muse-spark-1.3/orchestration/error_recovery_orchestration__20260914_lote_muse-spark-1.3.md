# Muse Spark 1.3 — orchestration/error_recovery_orchestration

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 3.74 | quality: 2.5
- latency_total: 3.834s | tokens_per_second: 114.0
- input_tokens: 1473 | output_tokens: 437

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

[tool_call] run_script({"code":"ls -la && echo \"---\" && find . -maxdepth 3 -type f -name \"*.csv\" -o -name \"*sales*\" -o -name \"*.db\" 2>/dev/null | head -20","language":"bash"})