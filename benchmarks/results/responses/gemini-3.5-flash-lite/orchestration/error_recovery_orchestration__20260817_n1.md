# Gemini 3.5 Flash Lite — orchestration/error_recovery_orchestration

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 2.68 | quality: 0.0
- latency_total: 0.874s | tokens_per_second: 119.0
- input_tokens: 851 | output_tokens: 104

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

[tool_call] run_script({"language":"python","code":"import os\nprint(\"Archivos disponibles en el directorio actual:\", os.listdir('.'))\nfor root, dirs, files in os.walk('.'):\n    for f in files:\n        if 'sale' in f.lower() or 'ventas' in f.lower() or 'report' in f.lower():\n            print(os.path.join(root, f))\n"})