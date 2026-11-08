# GLM 5.2 — orchestration/error_recovery_orchestration

- model_id: `z-ai/glm-5.2`
- success: True  | final: 5.51 | quality: 5.0
- latency_total: 4.767s | tokens_per_second: 91.3
- input_tokens: 990 | output_tokens: 435

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

## ⚠️ Diagnóstico del problema

La base de datos `production` está en mantenimiento y no estará disponible por ~2 horas. Esto pone en riesgo el plazo de las 5pm. 

## 🔄 Plan alternativo

Voy a intentar varias opciones en paralelo:

1. **Consultar una base de datos réplica** (`production_replica`) que podría tener los datos sincronizados.
2. **Consultar una base de datos de staging** que podría tener una copia reciente.
3. **Buscar en el sistema de archivos** si existe algún export o snapshot reciente de ventas.

Lanzo las tres búsquedas simultáneamente: