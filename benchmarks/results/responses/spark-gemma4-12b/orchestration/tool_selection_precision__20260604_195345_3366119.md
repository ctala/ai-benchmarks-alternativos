# Gemma 4 12B (Spark llama-server Q4_K_M) — orchestration/tool_selection_precision

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.05 | quality: 7.42
- latency_total: 9.713s | tokens_per_second: 22.9
- input_tokens: 855 | output_tokens: 222
- judge_score: 4.2 | justificación: 

## Respuesta completa

Aquí tienes el plan de acción para las tareas solicitadas:

### Análisis de herramientas:

*   **Tarea 1:** Usaría `http_request`. Es la herramienta adecuada para verificar la disponibilidad de un endpoint de API y obtener su estado de respuesta (status code).
*   **Tarea 2:** Usaría `query_database`. Es la forma más directa y eficiente de extraer datos estructurados y realizar agregaciones (como un conteo) sobre una base de datos de usuarios.
*   **Tarea 3:** No usaría ninguna herramienta. Es una operación aritmética simple que puedo realizar directamente como modelo de lenguaje.
*   **Tarea 4:** Usaría `search_web`. Es la herramienta diseñada para navegar por internet y extraer información actualizada sobre temas externos como la competencia.

---

### Ejecución de la Tarea 1:

Procedo a verificar el estado del servidor de producción.

