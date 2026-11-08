# GPT-6.1 Sol — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 5.04 | quality: 5.0
- latency_total: 6.218s | tokens_per_second: 43.7
- input_tokens: 532 | output_tokens: 272

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

La conexión fue rechazada porque la base de datos está en mantenimiento; la recuperación estimada es de dos horas, así que **no conviene depender de ella para cumplir el plazo**.

Propongo ajustar el plan:
1. **Buscar una fuente alternativa:** una exportación reciente en CSV/Excel, una réplica de lectura o el panel de ventas.
2. **Preparar el resumen** con el total vendido, número de operaciones, comparación con el mes anterior y principales productos o clientes, según los datos disponibles.
3. **Validar la cobertura:** si la fuente está incompleta, indicar claramente la fecha de actualización y qué falta.
4. Si no conseguimos datos a tiempo, enviar antes de las 5 un aviso del incidente y del plazo previsto del reporte, **sin presentar cifras no verificadas**.

¿Tienes una exportación o acceso a un panel alternativo? Confírmame también qué mes debe cubrir el reporte, la zona horaria de las 5 p. m. y los destinatarios del equipo.