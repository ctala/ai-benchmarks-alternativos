# Claude Opus 5 — orchestration/tool_selection_precision

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 12.833s | tokens_per_second: 62.7
- input_tokens: 1609 | output_tokens: 804

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

Primero el plan de herramientas, y al final ejecuto solo la Tarea 1.

**Tarea 1 — Verificar el servidor de producción** → `http_request` (GET)
Es una petición HTTP directa a un endpoint público de health. Alternativas descartadas: `run_script` con curl haría lo mismo pero ejecutando código arbitrario en el servidor (más privilegios de los necesarios); `search_web` no comprueba estado real, solo busca información sobre ello.

**Tarea 2 — Conteo de usuarios activos del último mes** → `query_database`
El dato vive en la base de datos interna; SQL con un `COUNT(DISTINCT ...)` y filtro de fecha es la vía precisa. Descartado `http_request` (solo si existiera una API de analytics documentada, que no me has indicado) y `run_script` (innecesario para una simple agregación). **Necesito dos datos antes de ejecutarla**: el nombre de la base de datos y cómo defines "usuario activo" (¿login? ¿evento? ¿tabla `sessions`/`events`?).

**Tarea 3 — Promedio de 45, 67, 89** → **ninguna herramienta**
Es aritmética trivial: (45 + 67 + 89) / 3 = 201 / 3 = **67**. Invocar `run_script` para esto sería gasto injustificado.

**Tarea 4 — Artículos recientes sobre competidores** → `search_web`
Requiere información pública y actualizada de fuera de mi conocimiento. Descartado `http_request` porque implicaría adivinar URLs concretas en vez de descubrir fuentes. **Necesito que me digas qué competidores** (nombres concretos) y el sector, si no la búsqueda sería demasiado vaga.

Ejecuto ahora la Tarea 1: