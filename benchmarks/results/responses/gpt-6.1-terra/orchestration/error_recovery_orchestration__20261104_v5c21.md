# GPT-6.1 Terra — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 7.23 | quality: 7.5
- latency_total: 4.723s | tokens_per_second: 55.9
- input_tokens: 532 | output_tokens: 264

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

La conexión falló porque la base de datos de producción está en mantenimiento; la recuperación estimada es de **2 horas**, pero podría no llegar a tiempo.

Para cumplir el plazo, propongo:

1. Buscar los datos en una réplica de lectura, un panel de BI o una exportación reciente.
2. Preparar el resumen y enviarlo al equipo, indicando la fecha de actualización de los datos.
3. Si no hay una fuente alternativa, enviar antes de las 5 un aviso de retraso, sin inventar cifras, y completar el reporte cuando vuelva la base de datos.

¿Tienen alguna de esas fuentes alternativas? Indícame también los destinatarios y la zona horaria del plazo.