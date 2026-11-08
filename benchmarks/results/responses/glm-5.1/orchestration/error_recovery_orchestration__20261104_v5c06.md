# GLM-5.1 — orchestration/error_recovery_orchestration

- model_id: `z-ai/glm-5.1`
- success: True  | final: 5.3 | quality: 5.0
- latency_total: 7.484s | tokens_per_second: 51.3
- input_tokens: 990 | output_tokens: 384

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

La base de datos principal está en mantenimiento, pero no nos quedemos con los brazos cruzados. Voy a buscar alternativas en paralelo:

1. **Probar una réplica de la base de datos** (staging/replica)
2. **Buscar archivos exportados** de ventas recientes en el servidor
3. **Consultar una API de reportes** si existe