# DeepSeek V4 Pro — orchestration/error_recovery_orchestration

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 5.18 | quality: 5.0
- latency_total: 9.266s | tokens_per_second: 72.6
- input_tokens: 1183 | output_tokens: 673

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

Buen diagnóstico. La base `production` está en mantenimiento (~2h), pero tenemos deadline a las 5pm. Vamos a buscar alternativas en paralelo: réplicas, backups recientes y APIs secundarias.

