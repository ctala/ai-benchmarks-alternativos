# Gemini 3.1 Flash Lite — orchestration/tool_selection_precision

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 6.02 | quality: 5.0
- latency_total: 1.624s | tokens_per_second: 131.1
- input_tokens: 836 | output_tokens: 213
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena planificación y profundidad al explicar por qué se eligieron las herramientas específicas.

## Respuesta completa

Aquí tienes el plan de herramientas para tus tareas:

*   **Tarea 1 (Verificar servidor):** Usaría `http_request`. Es la herramienta diseñada para realizar peticiones a APIs externas y verificar su estado.
*   **Tarea 2 (Conteo de usuarios):** Usaría `query_database`. Es la herramienta específica para extraer información estructurada (como conteos) de una base de datos.
*   **Tarea 3 (Promedio):** Usaría `run_script` (Python). Es la forma más eficiente y precisa de realizar cálculos matemáticos mediante código.
*   **Tarea 4 (Artículos sobre competidores):** Usaría `search_web`. Es la herramienta adecuada para realizar búsquedas de información actualizada en internet.

---

### Ejecución de la Tarea 1

Procedo a verificar el estado del servidor:

