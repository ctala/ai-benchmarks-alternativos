# DeepSeek V3 — orchestration/error_recovery_orchestration

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 5.34 | quality: 5.0
- latency_total: 5.097s | tokens_per_second: 18.4
- input_tokens: 1255 | output_tokens: 94

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

Voy a buscar alternativas para obtener los datos de ventas. Veamos si hay copias de seguridad o archivos de respaldo que contengan la información de ventas.