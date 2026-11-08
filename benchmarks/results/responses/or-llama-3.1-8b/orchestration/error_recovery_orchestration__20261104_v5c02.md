# Llama 3.1 8B Instant — orchestration/error_recovery_orchestration

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 4.45 | quality: 2.5
- latency_total: 0.741s | tokens_per_second: 86.4
- input_tokens: 1371 | output_tokens: 64

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

En ese caso, podemos intentar utilizar la función `read_file` para leer el archivo de ventas del mes pasado desde un archivo de texto, en lugar de conectarnos a la base de datos.

{"name": "read_file", "parameters": {"path": "/ventas/2026-03.txt"}}