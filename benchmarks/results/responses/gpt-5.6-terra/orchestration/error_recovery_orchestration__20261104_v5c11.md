# GPT-5.6 Terra — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 5.432s | tokens_per_second: 74.2
- input_tokens: 532 | output_tokens: 403

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

La consulta falló porque la base de datos de producción está en mantenimiento y no acepta conexiones; la recuperación estimada es de unas 2 horas. Como el informe debe salir antes de las 17:00, no conviene depender de que vuelva a tiempo.

**Plan alternativo, en este orden:**

1. **Usar una réplica de solo lectura o el data warehouse**  
   Consultar las ventas de marzo de 2026 allí. Normalmente estas fuentes siguen disponibles durante el mantenimiento de producción.

2. **Revisar el dashboard de BI con datos cacheados**  
   Si el dashboard muestra una actualización reciente y su fecha de corte, podemos elaborar un reporte preliminar, indicando claramente esa fecha.

3. **Reconstruir el total desde fuentes operativas**  
   Exportar transacciones de la pasarela de pagos / facturación y conciliar con pedidos enviados o cancelados. Es más lento, pero permite entregar una cifra verificable.

4. **Plan de contingencia de comunicación**  
   Si ninguna fuente está disponible antes de una hora de la hora límite, enviar al equipo una nota breve explicando que el reporte final se retrasa por mantenimiento, junto con los últimos indicadores confirmados disponibles, sin inventar cifras.

Para avanzar, necesito saber qué fuentes tenemos disponibles: ¿hay réplica, warehouse, herramienta de BI (por ejemplo, Power BI/Tableau/Looker) o acceso a la pasarela de pagos? Si me indicas cuál, preparo la consulta y el resumen para el equipo.