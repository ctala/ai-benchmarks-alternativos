# DeepSeek V4.1 Flash — orchestration/error_recovery_orchestration

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 7.66 | quality: 7.5
- latency_total: 4.211s | tokens_per_second: 100.4
- input_tokens: 1191 | output_tokens: 423

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

Diagnóstico y alternativas. Antes de decirte que no hay nada que hacer, voy a probar tres vías independientes: una réplica de lectura, un export local, y una API de reporting.