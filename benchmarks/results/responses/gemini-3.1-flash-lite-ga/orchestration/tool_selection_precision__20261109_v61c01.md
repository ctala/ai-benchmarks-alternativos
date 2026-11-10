# Gemini 3.1 Flash Lite (GA) — orchestration/tool_selection_precision

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 6.05 | quality: 5.0
- latency_total: 1.63s | tokens_per_second: 141.1
- input_tokens: 500 | output_tokens: 230

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

Aquí tienes la selección de herramientas para cada tarea y la ejecución de la primera:

### Selección de herramientas:

*   **Tarea 1 (Verificar servidor):** Usaría `http_request`. Es la herramienta diseñada específicamente para realizar llamadas HTTP a URLs externas y verificar su estado.
*   **Tarea 2 (Conteo de usuarios):** Usaría `query_database`. Es la herramienta adecuada para consultar información estructurada directamente desde la base de datos de la empresa.
*   **Tarea 3 (Promedio de números):** Usaría `run_script` (con Python). Es la forma más precisa y eficiente de realizar cálculos matemáticos mediante un pequeño script.
*   **Tarea 4 (Artículos sobre competidores):** Usaría `search_web`. Es la herramienta correcta para buscar información actualizada y pública en internet.

---

### Ejecución de la Tarea 1:

Voy a verificar el estado del servidor solicitado.

