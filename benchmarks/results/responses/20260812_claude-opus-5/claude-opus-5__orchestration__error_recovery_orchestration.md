# Claude Opus 5 — orchestration/error_recovery_orchestration

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 2.97 | quality: 2.5
- latency_total: 12.137s | tokens_per_second: 68.0
- input_tokens: 1658 | output_tokens: 825

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

Entendido. Antes de nada, el diagnóstico y luego pruebo rutas alternativas.

**Diagnóstico:** no es un error de sintaxis ni de permisos — el motor rechazó la conexión (`Connection refused`) por una ventana de mantenimiento programada de ~2h. Reintentar la misma consulta contra `production` no va a funcionar hasta que termine. Necesitamos otra fuente de los mismos datos.

Voy a probar tres vías alternativas en paralelo: