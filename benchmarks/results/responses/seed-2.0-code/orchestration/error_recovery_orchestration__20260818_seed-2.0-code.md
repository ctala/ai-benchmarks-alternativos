# Seed 2.0 Code — orchestration/error_recovery_orchestration

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.89 | quality: 7.5
- latency_total: 16.742s | tokens_per_second: 53.5
- input_tokens: 1285 | output_tokens: 895

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

La base de datos 'production' está en mantenimiento, pero hay varias alternativas que podemos explorar:

1. **Probar con una base de datos secundaria/réplica**: Muchas empresas tienen una base de datos de reporting o réplica para consultas sin afectar la producción.
2. **Buscar informes exportados recientemente**: A menudo se generan exports automáticos (CSV/Excel) en unidades de red.
3. **Consultar dashboards de BI**: Herramientas como Tableau, Power BI o Looker pueden tener los datos cacheados.

Primero, voy a intentar consultar una posible base de datos de reporting que comúnmente se usa como respaldo:
