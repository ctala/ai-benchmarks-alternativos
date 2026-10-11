# GPT-6 Luna Pro — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 9.04 | quality: 10.0
- latency_total: 10.649s | tokens_per_second: 108.3
- input_tokens: 3435 | output_tokens: 1153

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

La consulta no falló por el SQL: la base `production` está en mantenimiento y el aviso estima **2 horas** para recuperarse. Como el reporte debe salir antes de las 5, esperar sin más podría dejarnos sin margen.

Propongo este plan:
1. **Ahora:** buscar los datos en una fuente alternativa, como una réplica de lectura, un panel de BI o una exportación CSV del mes pasado.
2. **En paralelo:** volver a consultar `production` cuando termine el mantenimiento, si aún hay tiempo.
3. **Después:** preparar y enviar el resumen apenas tengamos los datos.

¿Tienes acceso a una réplica, un archivo exportado o algún panel con las ventas de marzo de 2026? También necesito la lista de destinatarios del equipo para poder enviarlo.