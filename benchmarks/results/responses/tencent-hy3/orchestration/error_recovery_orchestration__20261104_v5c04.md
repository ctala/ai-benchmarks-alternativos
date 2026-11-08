# Tencent Hy3 — orchestration/error_recovery_orchestration

- model_id: `tencent/hy3`
- success: True  | final: 5.28 | quality: 5.0
- latency_total: 30.126s | tokens_per_second: 38.6
- input_tokens: 1152 | output_tokens: 1163

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

Entiendo la urgencia. Vamos a diagnosticar y buscar alternativas de inmediato.

**Diagnóstico del fallo:**
- La base de datos `production` rechazó la conexión porque está en mantenimiento programado.
- Recuperación estimada: 2 horas. Si es ahora, eso probablemente nos pasaría de las 5pm.

**Plan de acción:** Necesito una fuente alternativa. Las opciones típicas son una réplica de solo lectura, un almacén de analítica, un API interna, o un archivo de respaldo reciente. Voy a verificar el tiempo disponible y sondear fuentes alternativas en paralelo.