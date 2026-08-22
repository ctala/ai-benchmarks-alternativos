# GLM 5.3 — orchestration/error_recovery_orchestration

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 10.768s | tokens_per_second: 47.5
- input_tokens: 990 | output_tokens: 511

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

El error indica que la base de datos `production` está bajo mantenimiento por 2 horas — no es un problema de credenciales sino de disponibilidad. Dado que la fecha límite es las 5pm, no podemos esperar la recuperación. Voy a intentar alternativas:

1. **Base de datos réplica/staging** — suele haber una copia con datos de ventas
2. **Archivos de reportes previos** — quizás exista un reporte cacheado en el servidor