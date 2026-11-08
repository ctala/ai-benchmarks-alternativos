# DeepSeek V4 Flash 0731 — orchestration/error_recovery_orchestration

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 7.8 | quality: 7.5
- latency_total: 3.231s | tokens_per_second: 166.5
- input_tokens: 1263 | output_tokens: 538

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

El mantenimiento impide acceder a `production` y tardará ~2 horas. Voy a diagnosticar buscando fuentes alternativas en paralelo: una base replica, archivos/cache en el servidor y una posible API interna.

