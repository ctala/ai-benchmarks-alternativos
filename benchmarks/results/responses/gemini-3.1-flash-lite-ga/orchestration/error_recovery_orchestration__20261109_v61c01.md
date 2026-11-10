# Gemini 3.1 Flash Lite (GA) — orchestration/error_recovery_orchestration

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 9.54 | quality: 10.0
- latency_total: 1.898s | tokens_per_second: 129.6
- input_tokens: 498 | output_tokens: 246

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

Comprendo la urgencia. Dado que la base de datos `production` no estará disponible a tiempo, el plan es el siguiente:

1.  **Diagnóstico:** La base de datos está inaccesible por mantenimiento programado hasta dentro de 2 horas.
2.  **Alternativa:** Verificaremos si existe una **copia de seguridad diaria o una base de datos de réplica (staging/analytics)** a la que podamos acceder para extraer los mismos datos sin afectar el mantenimiento.
3.  **Ajuste del Plan:**
    *   Consultaré la lista de bases de datos disponibles para ver si hay una alternativa (como `analytics` o `backup`).
    *   Si no hay otra base de datos, buscaré en el sistema de archivos si existen reportes automáticos exportados recientemente (archivos `.csv` o `.json`) en alguna carpeta compartida.
    *   Una vez obtenidos los datos, procederé a redactar y enviar el resumen al equipo antes de las 5pm.

**¿Deseas que proceda buscando bases de datos alternativas o prefieres que revise el sistema de archivos en busca de reportes exportados?**