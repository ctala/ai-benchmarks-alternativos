# MiniMax M3 — orchestration/error_recovery_orchestration

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.03 | quality: 7.5
- latency_total: 11.298s | tokens_per_second: 89.7
- input_tokens: 1296 | output_tokens: 1014

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

El fallo es de conexión a `production` por mantenimiento previsto (~2 h), no un error en la consulta. Ajusto el plan para no depender de esa instancia:

1. Buscar una réplica, respaldo o exportación reciente de ventas.
2. Validar que incluya todo el mes pasado.
3. Calcular el resumen y enviarlo al equipo antes de las 5 p. m.
4. Si los datos son parciales, indicarlo explícitamente en el reporte para no tomar decisiones sobre cifras incompletas.

Voy a localizar fuentes alternativas y comprobar también la fecha actual del servidor.