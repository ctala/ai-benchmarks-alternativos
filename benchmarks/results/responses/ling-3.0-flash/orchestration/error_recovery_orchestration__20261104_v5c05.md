# Ling 3.0 Flash — orchestration/error_recovery_orchestration

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 5.75 | quality: 5.0
- latency_total: 5.25s | tokens_per_second: 67.6
- input_tokens: 1306 | output_tokens: 355

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

Entiendo, la base de datos `production` está en mantenimiento con recuperación estimada en 2 horas. Dado que necesitas el reporte antes de las 5pm, busquemos alternativas inmediatamente.