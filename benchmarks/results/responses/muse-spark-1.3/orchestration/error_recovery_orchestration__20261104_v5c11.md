# Muse Spark 1.3 — orchestration/error_recovery_orchestration

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.77 | quality: 10.0
- latency_total: 6.917s | tokens_per_second: 119.8
- input_tokens: 1462 | output_tokens: 829

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

Entendido — la base de datos `production` está en mantenimiento (conexión rechazada, vuelve en ~2 horas) y tienes deadline a las 5pm, así que no podemos esperar.

**Diagnóstico:** fallo temporal de infraestructura, no de tu consulta.
**Alternativa:** buscar una fuente secundaria de ventas — archivo local de respaldo, export CSV, o API.
**Plan ajustado:** voy a explorar el servidor en busca de archivos de ventas y/o API alternativa mientras tanto.