# Bonsai 2 27B — orchestration/error_recovery_orchestration

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 6.95s | tokens_per_second: 32.7
- input_tokens: 1036 | output_tokens: 227

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



La BD principal está en mantenimiento, pero puedo probar alternativas antes de las 5pm. Déjame explorar opciones:


