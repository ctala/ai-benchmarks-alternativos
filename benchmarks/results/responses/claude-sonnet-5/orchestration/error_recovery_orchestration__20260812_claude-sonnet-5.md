# Claude Sonnet 5 — orchestration/error_recovery_orchestration

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 4.88 | quality: 5.0
- latency_total: 11.556s | tokens_per_second: 78.4
- input_tokens: 1726 | output_tokens: 906

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

Entiendo la urgencia. Mientras la base de datos principal está en mantenimiento (recuperación estimada en 2h, lo que no llega a tiempo para las 5pm), voy a intentar 3 alternativas en paralelo para conseguir los datos sin depender de esa instancia:

1. **Réplica/base de reporting** (si existe una base secundaria de solo lectura)
2. **API interna de ventas** (si el dashboard consume un endpoint distinto a la BD directa)
3. **Archivo de export** (si hay un backup/reporte generado automáticamente cada noche)