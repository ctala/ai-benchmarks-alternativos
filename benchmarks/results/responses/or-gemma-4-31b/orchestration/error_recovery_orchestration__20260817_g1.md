# Gemma 4 31B — orchestration/error_recovery_orchestration

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 9.556s | tokens_per_second: 30.1
- input_tokens: 878 | output_tokens: 288

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

**Diagnóstico:** La herramienta `query_database` ha fallado porque la base de datos de producción está en mantenimiento programado y no estará disponible en las próximas 2 horas.

**Propuesta de alternativa:** 
Dado que necesitamos el reporte antes de las 5:00 PM, no podemos esperar a que el sistema vuelva a estar en línea. Propongo las siguientes alternativas en orden de prioridad:
1. **Buscar archivos de respaldo o caché:** Verificar si existen archivos `.csv` o `.json` con los cierres mensuales en el servidor local.
2. **Consultar una base de datos de lectura (Read-Replica):** Intentar acceder a una base de datos secundaria que no esté en mantenimiento.
3. **Solicitar el reporte al sistema de backups:** Ejecutar un script que extraiga la última copia de seguridad disponible.

**Ajuste del plan general:**
1. **Acción inmediata:** Intentaré buscar archivos de reportes ya generados en el servidor usando `run_script` o `read_file`.
2. **Si no hay archivos:** Intentaré una consulta a la base de datos de réplica (`production_replica`).
3. **Finalización:** Una vez obtenidos los datos, procesaré el resumen y enviaré el email al equipo.

¿Deseas que proceda buscando los archivos de respaldo en el servidor?