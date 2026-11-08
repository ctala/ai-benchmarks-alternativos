# GPT-6 Astra — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-6-astra`
- success: True  | final: 4.76 | quality: 5.0
- latency_total: 5.539s | tokens_per_second: 37.0
- input_tokens: 532 | output_tokens: 205

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

La conexión falló porque la base `production` está en mantenimiento; la recuperación estimada es de 2 horas. **No conviene depender de que vuelva a tiempo para el envío de las 17:00.**

Propongo ajustar el plan:
1. **Buscar una fuente alternativa:** un CSV/Excel reciente, una exportación del CRM o una réplica de lectura disponible.
2. Preparar el resumen con ventas totales, número de operaciones y desglose por producto o región, según los datos disponibles. Indicaré la fuente, la fecha de corte y cualquier limitación.
3. Si no conseguimos datos completos a tiempo, enviar un **reporte provisional claramente identificado**, sin inventar cifras, y actualizarlo cuando vuelva la base.

¿Tienes un archivo o acceso a alguna fuente alternativa? Confírmame también los destinatarios, tu zona horaria y el mes que debemos reportar: la consulta anterior usó marzo de 2026 sin haberlo verificado.