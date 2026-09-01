# GLM 5.3 Flash — orchestration/error_recovery_orchestration

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 5.38 | quality: 5.0
- latency_total: 13.286s | tokens_per_second: 23.3
- input_tokens: 980 | output_tokens: 310

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

Entendido, actuemos con urgencia. Diagnóstico y plan:

**Diagnóstico:** La base de producción está en mantenimiento (~2 horas de espera). Si esperamos, probablemente lleguemos tarde a tu deadline de las 5pm.

**Plan alternativo:** Voy a intentar obtener los datos de fuentes secundarias: réplicas, entorno de staging y/o backups analíticos. Probaré varias en paralelo: