# Nemotron 3 Super — orchestration/error_recovery_orchestration

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 6.0 | quality: 5.0
- latency_total: 2.343s | tokens_per_second: 163.0
- input_tokens: 1407 | output_tokens: 382

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

Entiendo, la base de datos está en mantenimiento. Vamos a buscar alternativas para obtener los datos de ventas. Voy a:

1. Buscar archivos locales que puedan contener datos de ventas
2. Intentar consultar otras bases de datos disponibles
3. Buscar en la web si hay alguna API o fuente alternativa


