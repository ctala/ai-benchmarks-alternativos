# Qwen 3.8 Flash — orchestration/error_recovery_orchestration

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 7.47 | quality: 7.5
- latency_total: 6.511s | tokens_per_second: 111.5
- input_tokens: 1244 | output_tokens: 726

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

La base de datos `production` está caída ~2 horas, así que no podemos esperar a eso si el plazo es las 5pm. Voy a buscar rutas alternativas en paralelo: réplicas/otras bases, y exportaciones o cachés ya existentes en disco.

