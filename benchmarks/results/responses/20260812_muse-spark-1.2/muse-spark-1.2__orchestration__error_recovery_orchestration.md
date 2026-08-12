# Muse Spark 1.2 — orchestration/error_recovery_orchestration

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 1.97 | quality: 0.0
- latency_total: 3.034s | tokens_per_second: 175.7
- input_tokens: 1460 | output_tokens: 533

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

[tool_call] run_script({"language":"bash","code":"find . -type f -name \"*.csv\" -o -name \"*.xlsx\" -o -name \"*sales*\" -o -name \"*ventas*\" 2>/dev/null | head -n 50; echo \"---LIST ROOT---\"; ls -R 2>/dev/null | head -n 100"})