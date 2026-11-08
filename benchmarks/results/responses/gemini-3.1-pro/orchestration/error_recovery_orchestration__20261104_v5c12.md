# Gemini 3.1 Pro — orchestration/error_recovery_orchestration

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.62 | quality: 7.5
- latency_total: 14.236s | tokens_per_second: 73.7
- input_tokens: 498 | output_tokens: 1049

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

**1. Diagnóstico del fallo:**
La consulta falló porque la base de datos principal (`production`) está actualmente en mantenimiento y rechaza las conexiones. El tiempo estimado de recuperación es de 2 horas, lo cual podría poner en riesgo tu límite de las 5 PM si esperamos.

**2. Propuesta de alternativa:**
Dado que no podemos acceder a la base de datos principal, podemos intentar obtener los datos de fuentes secundarias:
*   Buscar si hay algún archivo de respaldo o reporte automático generado recientemente (archivos `.csv` o `.xlsx` en el servidor).
*   Consultar una base de datos de réplica o de análisis (ej. `analytics` o `reporting`) si está configurada.

**3. Ajuste del plan general:**
1. Buscar archivos locales de exportación de ventas en el servidor.
2. Si encontramos un archivo válido, leeremos sus datos para generar el resumen.
3. Si no hay archivos, intentaré consultar una base de datos de réplica.
4. Redactar y enviar el correo al equipo de inmediato con los datos obtenidos.

Voy a ejecutar una búsqueda rápida en el servidor para ver si tenemos algún archivo de ventas disponible.