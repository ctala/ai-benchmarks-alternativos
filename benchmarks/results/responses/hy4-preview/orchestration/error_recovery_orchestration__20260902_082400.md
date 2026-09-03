# Tencent Hy4 preview — orchestration/error_recovery_orchestration

- model_id: `tencent/hy4-preview`
- success: True  | final: 3.42 | quality: 2.5
- latency_total: 9.914s | tokens_per_second: 43.2
- input_tokens: 1062 | output_tokens: 428

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

La base de datos principal no está disponible. Voy a probar rutas alternativas en paralelo antes de decidir.