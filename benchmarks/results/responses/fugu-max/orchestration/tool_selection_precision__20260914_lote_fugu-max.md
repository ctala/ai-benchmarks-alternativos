# Fugu Max — orchestration/tool_selection_precision

- model_id: `sakana/fugu-max`
- success: True  | final: 7.15 | quality: 7.5
- latency_total: 4.242s | tokens_per_second: 61.1
- input_tokens: 584 | output_tokens: 259

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

Usaría estas herramientas:

1. **Tarea 1 — `http_request` (GET):** es la opción adecuada para comprobar directamente si la URL de salud responde y observar su código HTTP y contenido. No usaría búsqueda web ni un script, porque no hace falta localizar otra URL ni ejecutar lógica adicional.
2. **Tarea 2 — `query_database`:** permite consultar directamente el conteo de usuarios activos del último mes en la base de datos, en lugar de hacer una búsqueda web.
3. **Tarea 3 — `run_script`:** sirve para calcular de forma exacta el promedio; es más apropiado que consultar una base de datos o buscar en la web.
4. **Tarea 4 — `search_web`:** está diseñada para encontrar artículos recientes sobre competidores y sus publicaciones actuales.

Ejecuto ahora la **tarea 1** con una petición GET a la URL indicada.