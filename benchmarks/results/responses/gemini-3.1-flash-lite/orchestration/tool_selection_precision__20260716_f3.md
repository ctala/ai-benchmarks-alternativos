# Gemini 3.1 Flash Lite — orchestration/tool_selection_precision

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 9.33 | quality: 10.0
- latency_total: 2.029s | tokens_per_second: 150.3
- input_tokens: 836 | output_tokens: 305
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con una planificación óptima de las herramientas, aunque la profundidad es solo aceptable ya que no ofrece insights adicionales más allá de la elección de herramientas.

## Respuesta completa

Aquí tienes la planificación de las herramientas y la ejecución de la primera tarea:

### Planificación de herramientas

*   **Tarea 1: Verificar servidor de producción.**
    *   **Herramienta:** `http_request`.
    *   **Por qué:** Es la forma directa de realizar una petición GET a una URL específica para comprobar su estado.
*   **Tarea 2: Obtener conteo de usuarios activos.**
    *   **Herramienta:** `query_database`.
    *   **Por qué:** La información sobre usuarios reside normalmente en tablas de bases de datos, por lo que una consulta SQL es el método adecuado.
*   **Tarea 3: Calcular promedio de 3 números.**
    *   **Herramienta:** `run_script` (Python).
    *   **Por qué:** Es una operación lógica simple que se puede resolver rápidamente mediante un script sin necesidad de consultar fuentes externas.
*   **Tarea 4: Encontrar artículos sobre competidores.**
    *   **Herramienta:** `search_web`.
    *   **Por qué:** Esta herramienta permite buscar información actualizada y pública en internet.

---

### Ejecución de la Tarea 1

Voy a realizar la petición a `https://api.example.com/health`.

