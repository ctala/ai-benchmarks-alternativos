# Gemini 3.1 Flash Lite — orchestration/tool_selection_precision

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 6.01 | quality: 5.0
- latency_total: 1.684s | tokens_per_second: 147.3
- input_tokens: 836 | output_tokens: 248
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena planificación y profundidad al justificar la selección de herramientas.

## Respuesta completa

Aquí tienes la selección de herramientas para cada tarea y la ejecución de la primera:

### Selección de herramientas

*   **Tarea 1 (Verificar servidor):** Usaría `http_request`. Es la herramienta diseñada específicamente para realizar peticiones a endpoints de APIs y verificar su estado.
*   **Tarea 2 (Conteo de usuarios):** Usaría `query_database`. Es la forma correcta de extraer métricas estructuradas directamente de los datos almacenados en la base de datos de la empresa.
*   **Tarea 3 (Calcular promedio):** Usaría `run_script` (Python). Aunque es una operación simple, un script es la forma más precisa y eficiente de realizar cálculos matemáticos complejos o repetitivos.
*   **Tarea 4 (Artículos sobre competidores):** Usaría `search_web`. Es la herramienta adecuada para realizar búsquedas de información actualizada y externa en tiempo real.

---

### Ejecución de la Tarea 1

Procedo a verificar el estado del servidor de producción:

