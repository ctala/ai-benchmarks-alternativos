# GLM 5.3 — orchestration/error_recovery_orchestration

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.7 | quality: 7.5
- latency_total: 18.462s | tokens_per_second: 32.8
- input_tokens: 990 | output_tokens: 606

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

No hay problema, tengo varias alternativas para probar. Voy a intentar:
1. Consultar una réplica o base de datos analítica (si existe)
2. Buscar archivos locales con exportaciones o backups de datos de ventas