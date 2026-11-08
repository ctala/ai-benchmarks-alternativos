# Kimi K2 — orchestration/error_recovery_orchestration

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.07 | quality: 7.5
- latency_total: 5.747s | tokens_per_second: 40.5
- input_tokens: 657 | output_tokens: 233

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

Entiendo la urgencia. Como la base de datos está en mantenimiento, aquí tienes alternativas:

## Opciones disponibles:

### Opción 1: Usar datos de respaldo/caché
Si tienes un archivo CSV o Excel con los datos de ventas del mes pasado, puedo leerlo y generar el resumen.

### Opción 2: API alternativa
Si tu sistema de ventas tiene una API REST que pueda consultar, podemos usarla.

### Opción 3: Reporte pre-generado
Si ya existe un reporte anterior que podamos usar como base.

---

**¿Tienes alguno de estos recursos disponibles?** Por favor indícame:
- Ruta de algún archivo con datos de ventas
- URL de una API alternativa
- O si prefieres que busque información sobre cómo acceder a datos de respaldo

Con la hora límite de las 5pm, necesitamos actuar rápido. ¿Qué opción prefieres explorar?