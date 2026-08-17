# Gemini 3.1 Flash Lite — orchestration/tool_selection_precision

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 6.0 | quality: 5.0
- latency_total: 1.82s | tokens_per_second: 141.8
- input_tokens: 836 | output_tokens: 258
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena planificación y profundidad al explicar por qué se eligieron las herramientas específicas.

## Respuesta completa

Aquí tienes la selección de herramientas para cada tarea y la ejecución de la primera:

### Selección de herramientas

1.  **Tarea 1 (Verificar servidor):** Usaría `http_request`. Es la herramienta diseñada específicamente para realizar llamadas a endpoints de API y verificar su estado mediante métodos HTTP.
2.  **Tarea 2 (Conteo de usuarios):** Usaría `query_database`. Esta tarea implica consultar datos estructurados almacenados en una base de datos, lo cual es la función principal de esta herramienta.
3.  **Tarea 3 (Calcular promedio):** Usaría `run_script` (Python). Aunque es una operación simple, ejecutar un pequeño script de Python es la forma más precisa y eficiente de realizar cálculos matemáticos complejos o simples dentro de este entorno.
4.  **Tarea 4 (Artículos sobre competidores):** Usaría `search_web`. Esta herramienta está diseñada para realizar búsquedas en tiempo real en internet sobre temas específicos.

---

### Ejecución de la Tarea 1

Procedo a verificar el estado del servidor:

