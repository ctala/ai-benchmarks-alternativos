# Mistral Large 4.0 — orchestration/error_recovery_orchestration

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 5.22 | quality: 5.0
- latency_total: 12.009s | tokens_per_second: 59.9
- input_tokens: 960 | output_tokens: 719

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

El usuario tiene una urgencia: necesita enviar el reporte antes de las 5pm, pero la base de datos de producción está en mantenimiento. Como agente orquestador, debo diagnosticar, proponer alternativas y ajustar el plan.

Diagnostico: La conexión fue rechazada porque la base 'production' está en mantenimiento (recuperación estimada en 2 horas).

Alternativas que puedo explorar:
1. Verificar si hay una base de datos réplica/backup/staging con los datos de ventas
2. Buscar los datos en otra fuente (archivos CSV exportados, data warehouse, API de reportes, etc.)
3. Buscar emails previos con reportes o archivos adjuntos
4. Verificar si hay un script o job que genere el reporte

Voy a explorar en paralelo:
- Listar bases de datos disponibles o probar con otras bases comunes (staging, replica, analytics, warehouse, reporting)
- Buscar en la web? No, mejor buscar archivos locales o usar run_script para ver archivos disponibles
- Hacer consultas a otras bases de datos

Voy a intentar varias cosas en paralelo:
1. Probar query en 'analytics' o 'reporting' o 'replica' o 'staging'
2. Ejecutar un script para listar archivos que puedan contener datos de ventas (CSV, exports)
3. Buscar info sobre el mantenimiento

Empecemos con consultas a otras bases y listar archivos.