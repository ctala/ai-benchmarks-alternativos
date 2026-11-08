# Muse Spark 1.3 — orchestration/tool_selection_precision

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 11.202s | tokens_per_second: 136.8
- input_tokens: 1392 | output_tokens: 1533

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

Estas son las herramientas ideales para cada tarea:

**Tarea 1: Verificar servidor https://api.example.com/health → `http_request`**
Porque necesitas comprobar en vivo el código de estado HTTP. La descarto frente a `search_web` (solo trae info indexada, no estado en vivo) y frente a `run_script` (innecesariamente complejo para un simple GET).

**Tarea 2: Conteo de usuarios activos del último mes → `query_database`**
Porque es un dato estructurado interno que requiere SQL (ej. `SELECT COUNT(*)...`). La elijo sobre `read_file` (no está en archivo) o `http_request` (no es una API externa).

**Tarea 3: Promedio de 45, 67, 89 → Ninguna herramienta**
Es (45+67+89)/3 = 67, cálculo mental directo. Uso innecesario de `run_script` o cualquier otra herramienta violaría el principio de no usar herramientas innecesarias.

**Tarea 4: Artículos recientes sobre competidores → `search_web`**
Porque es información pública externa y actualizada. La elijo sobre `query_database` (no tenemos eso en BD interna) o `http_request` (no conocemos una API específica).

Ejecuto ahora la Tarea 1: