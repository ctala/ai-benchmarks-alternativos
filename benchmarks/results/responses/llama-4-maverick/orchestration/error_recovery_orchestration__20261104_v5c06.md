# Llama 4 Maverick — orchestration/error_recovery_orchestration

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 4.22 | quality: 2.5
- latency_total: 1.32s | tokens_per_second: 70.5
- input_tokens: 1325 | output_tokens: 93

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

La base de datos está en mantenimiento y no estará disponible por 2 horas. Eso significa que no podré obtener los datos de ventas a tiempo para enviar el reporte antes de las 5pm.

Voy a intentar obtener los datos de ventas de una fuente alternativa. Puedo buscar en la web si hay alguna API o fuente de datos pública que proporcione información de ventas históricas.

[search_web(query="API de ventas históricas", max_results=5)]