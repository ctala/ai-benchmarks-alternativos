# Fugu Max — orchestration/error_recovery_orchestration

- model_id: `sakana/fugu-max`
- success: True  | final: 7.1 | quality: 7.5
- latency_total: 4.798s | tokens_per_second: 85.7
- input_tokens: 605 | output_tokens: 411

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

La consulta falló porque la base de datos `production` está en mantenimiento y se estima una recuperación en unas 2 horas, así que no conviene esperar.

Plan alternativo inmediato:
1. Buscar una exportación reciente de ventas (CSV/XLSX/JSON) en los archivos disponibles.
2. Si existe, calcular el resumen del mes pasado y dejarlo listo.
3. Para enviarlo, necesitaré la lista o alias del equipo y, si aplica, el formato deseado.