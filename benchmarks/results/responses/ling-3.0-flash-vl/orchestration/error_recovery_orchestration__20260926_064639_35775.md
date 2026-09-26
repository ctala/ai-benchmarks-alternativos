# Ling 3.0 Flash VL — orchestration/error_recovery_orchestration

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 4.3 | quality: 2.5
- latency_total: 3.263s | tokens_per_second: 105.4
- input_tokens: 1296 | output_tokens: 344

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

Entiendo la urgencia. La base de datos de producción está en mantenimiento, pero tenemos otras opciones. Voy a explorar alternativas para obtener los datos de ventas.


