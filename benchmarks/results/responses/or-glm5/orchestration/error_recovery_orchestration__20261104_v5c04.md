# GLM 5 — orchestration/error_recovery_orchestration

- model_id: `z-ai/glm-5`
- success: True  | final: 7.0 | quality: 7.5
- latency_total: 9.594s | tokens_per_second: 37.2
- input_tokens: 990 | output_tokens: 357

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

¡No te preocupes! La base de datos `production` está en mantenimiento, pero tengo varias alternativas para intentar. Déjame probar múltiples opciones en paralelo:

1. **Consultar una base de datos réplica/warehouse** (suele haber una para reportes)
2. **Buscar un API interno** que pueda servir los datos de ventas
3. **Revisar si hay archivos locales** con reportes previos de ventas

Vamos a probar todo a la vez: