# Claude Haiku 5.5 — orchestration/error_recovery_orchestration

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 4.13 | quality: 2.5
- latency_total: 3.979s | tokens_per_second: 178.7
- input_tokens: 1662 | output_tokens: 711

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

La base principal no está disponible, así que voy a probar fuentes alternativas. Antes, una corrección: en la consulta anterior di por hecho que "el mes pasado" era marzo de 2026 y que el nombre de la base era `production`, sin confirmarlo. Esta vez uso un filtro relativo a la fecha actual, pero conviene que me confirme el periodo y la base correctos.