# GPT-OSS 120B — orchestration/error_recovery_orchestration

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 5.53 | quality: 5.0
- latency_total: 16.522s | tokens_per_second: 36.3
- input_tokens: 602 | output_tokens: 600

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

**Diagnóstico del fallo**  
El intento de consultar la base de datos *production* falló porque el servidor está en mantenimiento y no está disponible (error *Connection refused*). Por lo tanto, no podemos obtener los datos de ventas directamente mediante la consulta SQL.

**Alternativa propuesta**  
1. **Buscar un respaldo reciente**: normalmente, los datos de ventas se exportan diariamente a un archivo CSV que se guarda en el servidor de archivos. Intentaremos leer ese archivo (por ejemplo, `/data/exports/sales_2026-03.csv`).  
2. **Si el archivo no existe o está incompleto**, consultaremos la API interna de reporting (si está disponible) mediante una petición HTTP para obtener el mismo conjunto de datos.  
3. **Si tampoco hay API disponible**, haremos una búsqueda rápida en la web para localizar un informe público o un dashboard que contenga los números de ventas del mes pasado y extraeremos la información relevante.

**Plan ajustado**  

| Paso | Acción | Herramienta | Resultado esperado |
|------|--------|------------|--------------------|
| 1 | Intentar leer el archivo CSV de exportación de ventas del mes pasado. | `read_file` | Obtener los datos en formato texto/CSV. |
| 2 | Si el archivo no está disponible, hacer una petición HTTP a la API interna de reporting (`GET https://reporting.internal/api/v1/sales?month=2026-03`). | `http_request` | Recibir JSON con los datos de ventas. |
| 3 | Procesar los datos (agrupar por categoría, total, etc.) mediante un script Python. | `run_script` (Python) | Generar un resumen estructurado (texto). |
| 4 | Redactar el cuerpo del email con el resumen y adjuntar el CSV (si lo tenemos). | — | Texto listo para enviar. |
| 5 | Enviar el email al equipo antes de las 5 pm. | `send_email` | Email entregado a los destinatarios. |

Procederé con el **primer paso**: intentar leer el archivo CSV de exportación. Si falla, pasaré al segundo paso (API).  

---  

**Ejecutando paso 1** (lectura del archivo).