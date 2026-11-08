# Tencent Hy4 — orchestration/error_recovery_orchestration

- model_id: `tencent/hy4`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 23.203s | tokens_per_second: 64.8
- input_tokens: 1062 | output_tokens: 1503

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

**Diagnóstico:** el fallo no es de la consulta ni de credenciales, sino que `production` está en mantenimiento con recuperación estimada en ~2 h. Esperar a ciegas pone en riesgo el plazo de las 5 pm.

**Alternativas que voy a probar en paralelo (sin depender de `production`):**
1. Réplica / base de datos de analítica (`analytics` / `replica`) → probablemente fuera del mantenimiento.
2. Exportaciones locales (CSV/Excel/JSON) de ventas → permiten calcular el resumen con un script.
3. API interna de reporting o caché → última fuente alternativa.

**Plan ajustado:** obtener datos de la fuente alternativa → validar que el periodo y los importes estén completos → calcular el resumen → enviar antes de las 5 pm. Si la fuente alternativa está desactualizada, enviaré un informe **provisional marcado como tal** y lo completaré cuando `production` vuelva, en lugar de no enviar nada.