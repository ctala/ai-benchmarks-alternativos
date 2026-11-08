# Kimi K3 — orchestration/error_recovery_orchestration

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.39 | quality: 7.5
- latency_total: 17.841s | tokens_per_second: 27.3
- input_tokens: 988 | output_tokens: 487

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

Entendido. Voy a buscar alternativas para obtener los datos sin esperar las 2 horas de mantenimiento.

**Diagnóstico:** La base de datos `production` rechaza conexiones por mantenimiento programado (recuperación estimada: 2 horas).

**Plan alternativo:** Intentaré dos vías en paralelo:
1. Consultar una réplica de solo lectura o base de analytics
2. Buscar archivos locales (exports, CSVs, backups) con datos de ventas