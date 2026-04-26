# Gemini 3.1 Flash Lite — orchestration/tool_selection_precision

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 8.14 | quality: 6.97
- latency_total: 1.549s | tokens_per_second: 140.1
- input_tokens: 836 | output_tokens: 217
- judge_score: 4.2 | justificación: 

## Respuesta completa

Aquí tienes la selección de herramientas para cada tarea y la ejecución de la primera:

### Selección de herramientas

*   **Tarea 1 (Verificar servidor):** Usaría `http_request`. Es la herramienta diseñada específicamente para interactuar con APIs y verificar estados de respuesta HTTP.
*   **Tarea 2 (Conteo de usuarios):** Usaría `query_database`. Es la herramienta adecuada para consultar datos estructurados almacenados en una base de datos.
*   **Tarea 3 (Calcular promedio):** Usaría `run_script` (Python). Es la opción más eficiente para realizar cálculos matemáticos precisos mediante código.
*   **Tarea 4 (Buscar artículos):** Usaría `search_web`. Es la herramienta necesaria para consultar información actualizada en internet.

---

### Ejecución de la Tarea 1

Procedo a verificar el estado del servidor:

