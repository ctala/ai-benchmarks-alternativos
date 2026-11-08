# Gemini 3.5 Flash Lite — orchestration/error_recovery_orchestration

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.44 | quality: 10.0
- latency_total: 1.869s | tokens_per_second: 143.9
- input_tokens: 498 | output_tokens: 269

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

El intento de consultar la base de datos `production` ha fallado debido a que se encuentra en mantenimiento (con un tiempo estimado de recuperación de 2 horas). 

Como necesitamos enviar el resumen antes de las 5:00 p.m. y no podemos esperar 2 horas, propongo las siguientes alternativas:

1. **Buscar archivos locales o reportes previos**: Verificar si en el servidor o en archivos locales existe un respaldo, un archivo CSV, Excel o un reporte generado previamente correspondiente al mes pasado.
2. **Consultar una base de datos de réplica o staging**: Si existe un entorno secundario (staging o backup) que no esté en mantenimiento, podríamos intentar consultar los datos desde allí.

Permíteme verificar si tenemos archivos locales con los datos de ventas. Voy a listar los archivos disponibles en el servidor.