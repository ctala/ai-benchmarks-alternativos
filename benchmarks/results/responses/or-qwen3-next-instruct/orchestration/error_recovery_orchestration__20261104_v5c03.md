# Qwen 3-Next 80B Instruct — orchestration/error_recovery_orchestration

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 6.2 | quality: 5.0
- latency_total: 0.843s | tokens_per_second: 95.0
- input_tokens: 1085 | output_tokens: 80

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

Entiendo la urgencia. Como la base de datos principal está en mantenimiento, voy a buscar alternativas para obtener los datos de ventas del mes pasado.

Primero, voy a verificar si hay algún archivo de respaldo o registro de ventas que podamos usar:

