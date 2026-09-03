# Tencent Hy4 preview — orchestration/tool_selection_precision

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 8.829s | tokens_per_second: 46.0
- input_tokens: 1053 | output_tokens: 406

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

## Selección de herramientas

| Tarea | Herramienta | Por qué |
|---|---|---|
| 1. Health check | `http_request` | Es una petición GET puntual a un endpoint. `run_script` también podría hacerlo, pero sería excesivo levantar un runtime para un solo request. |
| 2. Usuarios activos | `query_database` | Es una consulta directa sobre la base de datos (COUNT + filtro por fecha). Ninguna otra herramienta accede a datos estructurados. |
| 3. Promedio de 45, 67, 89 | **Ninguna** | Es aritmética trivial: (45+67+89)/3 = 201/3 = **67**. Usar `run_script` sería gastar recursos innecesariamente. |
| 4. Artículos recientes | `search_web` | Es una búsqueda de información pública y actualizada. `http_request` requeriría saber el endpoint exacto de un buscador. |

Ahora ejecuto la tarea 1: