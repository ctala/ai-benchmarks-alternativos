# Claude Opus 5 Fast — orchestration/tool_selection_precision

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 6.893s | tokens_per_second: 97.2
- input_tokens: 1609 | output_tokens: 670

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

## Plan de herramientas

| Tarea | Herramienta | Por qué esa y no otra |
|---|---|---|
| 1. Health check de producción | `http_request` (GET) | Es una petición HTTP directa a un endpoint. `run_script` con curl haría lo mismo pero añade una capa innecesaria y riesgo de ejecución arbitraria; `search_web` no sirve para consultar un endpoint privado. |
| 2. Usuarios activos del último mes | `query_database` | El dato vive en la BD y es una agregación (`COUNT` + filtro de fecha). Una API HTTP solo serviría si existiera un endpoint de métricas; el SQL es la fuente directa. **Necesito de ti**: nombre de la base de datos y el esquema/tabla (p. ej. `users`, campo `last_active_at`) antes de lanzarla. |
| 3. Promedio de 45, 67, 89 | **Ninguna** | Aritmética trivial: (45+67+89)/3 = 201/3 = **67**. Invocar `run_script` para esto sería gasto puro. |
| 4. Artículos recientes sobre competidores | `search_web` | Requiere información pública y actual de fuentes externas. La BD no la tiene y `http_request` exigiría conocer de antemano las URLs. **Necesito de ti**: qué competidores concretos y qué ventana temporal. |

Ejecuto ahora la tarea 1: