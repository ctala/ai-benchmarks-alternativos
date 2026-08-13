# Tencent Hy3 — orchestration/error_recovery_orchestration

- model_id: `tencent/hy3`
- success: True  | final: 7.22 | quality: 7.5
- latency_total: 16.337s | tokens_per_second: 54.4
- input_tokens: 1154 | output_tokens: 889

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

## Diagnóstico del fallo

**Causa:** La base de datos `production` está en mantenimiento programado y rechaza conexiones. La recuperación estimada es de 2 horas, lo que probablemente nos deje fuera del límite de las 5:00 pm.

## Alternativas propuestas

Para cumplir con el plazo, no podemos esperar a que `production` vuelva. Voy a intentar fuentes alternativas de los mismos datos:
1. **Réplica de solo lectura / data warehouse** (suele estar fuera del mantenimiento de producción).
2. **Archivo de exportación** reciente (CSV/JSON) si el equipo genera volcados periódicos.
3. **API interna** de reportes de ventas.

Voy a probar estas opciones en paralelo, ya que son independientes: