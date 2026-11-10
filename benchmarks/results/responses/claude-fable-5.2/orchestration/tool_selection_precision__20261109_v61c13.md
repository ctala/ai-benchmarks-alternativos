# Claude Fable 5.2 — orchestration/tool_selection_precision

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 7.676s | tokens_per_second: 78.2
- input_tokens: 1611 | output_tokens: 600

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

**Herramienta por tarea**

| Tarea | Herramienta | Por qué |
|---|---|---|
| 1. Verificar el servidor de producción | `http_request` (GET) | Es una llamada directa a un endpoint y devuelve el código de estado y la respuesta. `run_script` con curl sería un rodeo, y `search_web` no consulta endpoints en tiempo real. |
| 2. Conteo de usuarios activos del último mes | `query_database` | Los datos están en la base de datos y basta un `SELECT COUNT(*)` con filtro de fecha. Antes de ejecutarla necesitaría el nombre de la base de datos y de la tabla. |
| 3. Promedio de 45, 67 y 89 | Ninguna | Es aritmética simple: (45 + 67 + 89) / 3 = 201 / 3 = **67**. Usar `run_script` sería innecesario. |
| 4. Artículos recientes sobre competidores | `search_web` | Es información pública y actual de la web. `http_request` exigiría conocer una API concreta. Necesitaría los nombres de los competidores para la consulta. |

**Ejecución de la tarea 1**