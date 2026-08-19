# KAT Coder Air v2.5 — orchestration/error_recovery_orchestration

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.7 | quality: 7.5
- latency_total: 2.008s | tokens_per_second: 140.5
- input_tokens: 1280 | output_tokens: 282

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



Entiendo la urgencia. Voy a intentar alternativas:

1. **Buscar archivos locales** con datos de ventas
2. **Consultar una API** de reportes si existe
3. **Verificar si hay una base de datos de respaldo**

