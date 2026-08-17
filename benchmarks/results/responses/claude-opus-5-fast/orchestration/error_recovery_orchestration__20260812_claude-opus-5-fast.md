# Claude Opus 5 Fast — orchestration/error_recovery_orchestration

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 4.76 | quality: 5.0
- latency_total: 5.739s | tokens_per_second: 195.5
- input_tokens: 1658 | output_tokens: 1122

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

Entiendo la urgencia. Antes de improvisar, déjame diagnosticar y probar rutas alternativas en paralelo.

**Diagnóstico:** el fallo no es de sintaxis ni de permisos — es indisponibilidad del host (`Connection refused`, mantenimiento programado, ETA ~2h). Reintentar la misma consulta contra `production` no va a funcionar hasta que termine la ventana. Necesito una fuente de datos distinta, no un reintento.

Voy a probar tres vías alternativas a la vez: