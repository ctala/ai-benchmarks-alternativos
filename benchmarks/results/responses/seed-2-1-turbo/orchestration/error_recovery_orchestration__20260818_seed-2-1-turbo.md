# Seed 2.1 Turbo — orchestration/error_recovery_orchestration

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 5.23 | quality: 5.0
- latency_total: 8.333s | tokens_per_second: 39.5
- input_tokens: 1285 | output_tokens: 329

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

Entiendo la urgencia. La base de datos principal estará en mantenimiento por 2 horas, así que vamos a intentar alternativas:

**Plan de contingencia:**
1. Consultar la base de datos de respaldo/staging (suele tener datos casi actualizados)
2. Buscar archivos de respaldo/exportaciones recientes de ventas
3. Si no encontramos datos completos, enviaremos un aviso al equipo con la información disponible

Vamos a intentar primero con la base de datos de staging:
