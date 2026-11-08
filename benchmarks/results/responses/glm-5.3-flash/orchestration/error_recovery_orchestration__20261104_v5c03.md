# GLM 5.3 Flash — orchestration/error_recovery_orchestration

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 5.39 | quality: 5.0
- latency_total: 15.138s | tokens_per_second: 38.4
- input_tokens: 990 | output_tokens: 581

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

Entiendo la urgencia. Diagnóstico y plan alternativo:

**Diagnóstico:** La BD de producción está en mantenimiento con recuperación estimada en 2 horas — esperar es demasiado arriesgado para el deadline de las 5pm.

**Plan B:** Voy a intentar fuentes alternativas en paralelo:
1. La base de datos de staging/replica (suele contener datos replicados de producción)
2. Un data warehouse de analítica (si existe)
3. Archivos exportados localmente (CSVs u snapshots)