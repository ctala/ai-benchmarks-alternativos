# Tencent Hy3 — orchestration/tool_selection_precision

- model_id: `tencent/hy3`
- success: True  | final: 7.09 | quality: 7.5
- latency_total: 17.316s | tokens_per_second: 45.3
- input_tokens: 1143 | output_tokens: 785

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

## Herramientas para cada tarea

| Tarea | Herramienta | Por qué |
|-------|-------------|---------|
| **1. Verificar servidor de producción** | `http_request` (GET) | Es la herramienta diseñada para hacer peticiones HTTP a una API y comprobar si responde (status, latencia, cuerpo). |
| **2. Conteo de usuarios activos del último mes** | `query_database` | El dato vive en una base de datos, así que una consulta SQL (`COUNT` con filtro de fecha) es lo directo y exacto. |
| **3. Promedio de 45, 67, 89** | **Ninguna** | Es aritmética trivial: (45+67+89)/3 = 201/3 = **67**. Usar `run_script` sería innecesario. |
| **4. Artículos recientes de competidores** | `search_web` | Está hecha para buscar información actual en la web y devolver artículos recientes. |

Ahora ejecuto la **Tarea 1**:

