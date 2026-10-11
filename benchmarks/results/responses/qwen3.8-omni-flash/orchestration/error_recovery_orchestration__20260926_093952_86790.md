# Qwen 3.8 Omni Flash — orchestration/error_recovery_orchestration

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 7.07 | quality: 7.5
- latency_total: 24.486s | tokens_per_second: 38.2
- input_tokens: 1240 | output_tokens: 935

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

Entendido. Diagnóstico rápido y plan B:

**Diagnóstico:** `production` está caída por mantenimiento (~2h de recuperación). Si ahora son más de las 15:00, esperar no es viable. Hay que buscar una fuente alternativa de los mismos datos.

**Alternativas, de mejor a peor:**
1. Réplica de solo lectura / Data Warehouse (`analytics`, `reporting`, `staging`) — misma data, sin tocar producción.
2. Exportaciones recientes en disco (CSV/Parquet generados por jobs nocturnos).
3. API de reporting del sistema de ventas.
4. Pedir el dato a Finanzas/BI como último recurso.

Voy a explorar las tres primeras en paralelo y confirmar la fecha real para calcular bien "mes pasado".

