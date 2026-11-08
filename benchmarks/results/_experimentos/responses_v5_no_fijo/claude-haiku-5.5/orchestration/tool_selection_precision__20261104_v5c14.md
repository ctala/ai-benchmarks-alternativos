# Claude Haiku 5.5 — orchestration/tool_selection_precision

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.42 | quality: 10.0
- latency_total: 2.708s | tokens_per_second: 193.2
- input_tokens: 1611 | output_tokens: 523

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

Para cada tarea, la herramienta que usaría:

1. **Verificar el servidor de producción:** `http_request` (GET a la URL de health). Es la forma directa de comprobar si responde. `search_web` no serviría, porque no consulta servidores en vivo.
2. **Conteo de usuarios activos del último mes:** `query_database`. Los datos de usuarios están en la base de datos, así que una consulta SQL es la fuente correcta. Me faltaría el nombre de la base de datos, que tendrías que indicarme.
3. **Promedio de 45, 67 y 89:** ninguna herramienta. Es un cálculo sencillo: (45 + 67 + 89) / 3 = 201 / 3 = **67**. Usar `run_script` sería innecesario.
4. **Artículos recientes sobre competidores:** `search_web`. Es la única opción que busca información pública y actual en internet.

Ahora ejecuto la tarea 1.