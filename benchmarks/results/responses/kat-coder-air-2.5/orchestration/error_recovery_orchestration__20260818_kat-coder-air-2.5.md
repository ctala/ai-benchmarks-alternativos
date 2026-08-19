# KAT Coder Air v2.5 — orchestration/error_recovery_orchestration

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 6.11 | quality: 5.0
- latency_total: 1.893s | tokens_per_second: 136.8
- input_tokens: 1280 | output_tokens: 259

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



La base de datos principal está en mantenimiento. Voy a proponer alternativas:

1. **Buscar archivos de respaldo** en el sistema de archivos
2. **Consultar otras fuentes** (web, APIs alternativas)

