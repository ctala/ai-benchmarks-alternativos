# Fugu Max — orchestration/error_recovery_orchestration

- model_id: `sakana/fugu-max`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 10.961s | tokens_per_second: 71.4
- input_tokens: 625 | output_tokens: 783

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

La conexión a `production` está rechazada por mantenimiento; la recuperación estimada es en **2 horas**. Para no arriesgar el plazo de las 5, haría esto:

1. Usar una réplica de solo lectura, un almacén de analítica o el último CSV/exportación de ventas disponible.
2. Comprobar que los datos cubran todo marzo y anotar la fecha de actualización.
3. Si no hay una fuente alternativa confiable, avisar al equipo del retraso en vez de enviar cifras incompletas.

¿Tienes una réplica o un archivo exportado que podamos usar? También necesito la dirección o lista del equipo para enviar el resumen.