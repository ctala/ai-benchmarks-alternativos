# Claude Sonnet 5 — orchestration/error_recovery_orchestration

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 9.32s | tokens_per_second: 83.2
- input_tokens: 1726 | output_tokens: 775

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

Diagnóstico: la base de datos `production` está en mantenimiento (ventana de ~2h), por lo que la consulta directa no es viable ahora mismo. Como tenemos el límite de las 5pm, voy a intentar 3 alternativas en paralelo para no perder tiempo:

1. Consultar una réplica/base de reporting (si existe) que suele estar separada del mantenimiento.
2. Consultar si existe un endpoint de API que expone los datos de ventas (muchas empresas tienen un servicio intermedio que no depende directamente de la DB principal).
3. Revisar si hay un archivo de export/cache reciente con los datos del mes pasado.