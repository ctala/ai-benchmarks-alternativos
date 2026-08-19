# Claude Opus 5 Fast — orchestration/error_recovery_orchestration

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.55 | quality: 7.5
- latency_total: 5.501s | tokens_per_second: 158.5
- input_tokens: 1658 | output_tokens: 872

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

## Diagnóstico

El fallo no es de mi consulta (la sintaxis era válida), sino de **disponibilidad de infraestructura**: la instancia `production` rechaza conexiones por una ventana de mantenimiento con recuperación estimada en ~2 horas. No es un error reintentar-able de inmediato; reintentar la misma llamada dará el mismo resultado.

Tenemos margen, pero necesito rutas alternativas. Voy a probar dos en paralelo: una réplica de lectura y la búsqueda de exports/cachés locales. De paso verifico la fecha real del sistema, porque asumí que "el mes pasado" era 2026-03 y eso hay que confirmarlo.