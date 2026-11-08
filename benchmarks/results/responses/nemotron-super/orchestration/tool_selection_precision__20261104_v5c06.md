# Nemotron 3 Super — orchestration/tool_selection_precision

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.9 | quality: 7.5
- latency_total: 1.291s | tokens_per_second: 326.1
- input_tokens: 1372 | output_tokens: 421

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

Aquí está el análisis de las herramientas para cada tarea:

**Tarea 1:** Usaría `http_request` porque es la herramienta diseñada específicamente para hacer peticiones HTTP a URLs y verificar si un servidor responde.

**Tarea 2:** Usaría `query_database` porque permite ejecutar consultas SQL para obtener datos como conteos de usuarios desde una base de datos.

**Tarea 3:** Usaría `run_script` porque permite ejecutar código (Python, Bash, Node) para realizar cálculos matemáticos.

**Tarea 4:** Usaría `search_web` porque está diseñada para buscar información en internet, ideal para encontrar artículos recientes.

---

Ahora ejecuto la Tarea 1:

