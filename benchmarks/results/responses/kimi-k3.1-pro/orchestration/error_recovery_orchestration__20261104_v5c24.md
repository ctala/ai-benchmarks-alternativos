# Kimi K3.1 Pro — orchestration/error_recovery_orchestration

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 6.36 | quality: 7.5
- latency_total: 35.469s | tokens_per_second: 25.0
- input_tokens: 988 | output_tokens: 885

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

El fallo es de **conexión**, no de la consulta: `production` rechaza accesos por mantenimiento y no volvería hasta dentro de unas 2 horas. Para no arriesgar la entrega de las 5 p. m., descartemos esperar como opción principal.

**Plan alternativo:** buscar una réplica de solo lectura y, en paralelo, una exportación reciente de ventas. Si ninguna está disponible, necesitaré que me proporciones el CSV/Excel o acceso a la fuente alternativa; no conviene enviar cifras sin verificar.