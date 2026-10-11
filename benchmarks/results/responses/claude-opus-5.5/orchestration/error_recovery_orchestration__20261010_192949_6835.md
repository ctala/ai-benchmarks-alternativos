# Claude Opus 5.5 — orchestration/error_recovery_orchestration

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 3.14 | quality: 2.5
- latency_total: 6.524s | tokens_per_second: 80.3
- input_tokens: 1662 | output_tokens: 524

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

Producción no responde por mantenimiento (unas 2 horas más), así que voy a buscar otras fuentes con los mismos datos. Pruebo varias a la vez: