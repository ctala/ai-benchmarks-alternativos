# Nex-N2-Mini — orchestration/error_recovery_orchestration

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 7.95 | quality: 7.5
- latency_total: 1.267s | tokens_per_second: 101.0
- input_tokens: 1231 | output_tokens: 128

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


Voy a intentar una alternativa: consultar si hay otra base de datos disponible o un almacén de reportes.
