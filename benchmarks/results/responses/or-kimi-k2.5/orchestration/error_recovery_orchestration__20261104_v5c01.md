# Kimi K2.5 — orchestration/error_recovery_orchestration

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 6.68 | quality: 7.5
- latency_total: 28.48s | tokens_per_second: 28.2
- input_tokens: 654 | output_tokens: 803

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

¡Entendido! La base de datos `production` está caída por mantenimiento y el tiempo corre. Te propongo un plan de contingencia activo:

**Diagnóstico:** Fallo por mantenimiento programado de la BD principal. Recuperación estimada: 2 horas (probablemente después de tu deadline de 5pm).

**Plan alternativo:**
1. Intentar con la base de datos de reportes/analytics o réplica.
2. Buscar archivos CSV o reportes previos del mes pasado en el servidor.
3. Si tenemos datos, generar el resumen y enviarlo.

Permíteme ejecutar estas opciones ahora: