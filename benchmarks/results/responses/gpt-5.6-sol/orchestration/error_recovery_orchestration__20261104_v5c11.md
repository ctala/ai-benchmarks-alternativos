# GPT-5.6 Sol — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 5.28 | quality: 5.0
- latency_total: 4.948s | tokens_per_second: 83.1
- input_tokens: 532 | output_tokens: 411

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

El fallo está diagnosticado: **la base `production` rechaza conexiones por mantenimiento** y su recuperación estimada es de 2 horas. No conviene esperar si el reporte debe salir antes de las 17:00.

### Plan alternativo

1. **Buscar una fuente secundaria inmediata**, en este orden:
   - Réplica de lectura o data warehouse.
   - Exportación CSV/Excel del cierre de marzo.
   - API del CRM, ERP o plataforma de pagos.
   - Último reporte automático disponible.

2. **Preparar el resumen** con:
   - Ventas totales.
   - Número de operaciones.
   - Ticket promedio.
   - Comparación con febrero y, si existe, marzo del año anterior.
   - Productos, regiones o comerciales destacados.

3. **Validar y enviar**:
   - Si los datos son definitivos, enviar el informe normal.
   - Si proceden de una copia parcial, marcarlo como **preliminar** y programar una versión validada cuando vuelva la base.

Para continuar ahora, necesito que me indiques **dónde está la fuente alternativa** —archivo, API o nombre de la réplica/data warehouse— y **los correos del equipo**. Si tienes un CSV o Excel, dame la ruta y lo proceso directamente.