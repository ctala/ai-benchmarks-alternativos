# Qwen 3.7 Flash — orchestration/error_recovery_orchestration

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.58 | quality: 7.5
- latency_total: 10.091s | tokens_per_second: 117.3
- input_tokens: 1202 | output_tokens: 1184

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

Entendido. La base de datos principal está caída y el tiempo estimado de recuperación es de 2 horas. Para cumplir con la meta de las 5pm, necesitamos encontrar una alternativa inmediatamente.

Propongo intentar consultar una base de datos de respaldo o buscar un archivo local que contenga los datos exportados recientemente. Voy a probar primero si existe una instancia de respaldo disponible.

