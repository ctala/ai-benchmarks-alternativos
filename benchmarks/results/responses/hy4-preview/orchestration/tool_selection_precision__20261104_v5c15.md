# Tencent Hy4 preview — orchestration/tool_selection_precision

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 10.452s | tokens_per_second: 46.8
- input_tokens: 1053 | output_tokens: 489

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador. Elige SIEMPRE la herramienta mas apropiada.
No uses herramientas innecesarias. Si algo no requiere herramienta, no la uses.
Explica brevemente por que elegiste esa herramienta sobre las alternativas.

**user:**

Tengo que hacer estas 4 tareas. Para cada una, indica que herramienta usarias y por que. Luego ejecuta la tarea 1.

Tarea 1: Verificar si el servidor de produccion esta respondiendo (URL: https://api.example.com/health)
Tarea 2: Obtener el conteo de usuarios activos del ultimo mes
Tarea 3: Calcular el promedio de 3 numeros: 45, 67, 89
Tarea 4: Encontrar articulos recientes sobre competidores


## Respuesta completa

**Plan de herramientas**

| Tarea | Herramienta | Por qué sobre las alternativas |
|---|---|---|
| 1. Health check de producción | `http_request` (GET) | Es la única que hace peticiones HTTP a una URL arbitraria. `run_script` con curl añadiría una capa innecesaria; `search_web` no sirve para un endpoint específico. |
| 2. Conteo de usuarios activos | `query_database` | El dato vive en la BD. `run_script` requeriría credenciales/drivers manuales; `http_request` solo si existiera un endpoint de métricas (no indicado). |
| 3. Promedio de 45, 67, 89 | `run_script` (python) | Es la herramienta de cálculo, pero honestamente es innecesaria: es aritmética trivial → **67**. No gastaría una llamada en esto. |
| 4. Artículos recientes de competidores | `search_web` | Está diseñada para recuperar información web actualizada. `http_request` exigiría conocer dominios/medios concretos de antemano. |

Ejecuto la tarea 1: