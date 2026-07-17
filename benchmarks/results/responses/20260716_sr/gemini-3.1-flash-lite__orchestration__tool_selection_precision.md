# Gemini 3.1 Flash Lite — orchestration/tool_selection_precision

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 6.0 | quality: 5.0
- latency_total: 1.727s | tokens_per_second: 148.8
- input_tokens: 836 | output_tokens: 257
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena planificación y profundidad al explicar por qué se eligieron las herramientas específicas.

## Respuesta completa

Aquí tienes las herramientas seleccionadas para cada tarea y la ejecución de la primera:

### Selección de herramientas

*   **Tarea 1 (Verificar servidor):** Usaría `http_request`. Es la herramienta diseñada para realizar peticiones HTTP (GET, POST, etc.) a URLs específicas, siendo ideal para comprobar el estado de un servicio.
*   **Tarea 2 (Conteo de usuarios):** Usaría `query_database`. Esta función está diseñada específicamente para interactuar con bases de datos mediante consultas SQL, lo cual es necesario para extraer métricas de usuarios.
*   **Tarea 3 (Calcular promedio):** Usaría `run_script` (con Python). Aunque es un cálculo simple, ejecutar un pequeño script es la forma más precisa y estructurada de procesar datos numéricos.
*   **Tarea 4 (Buscar artículos):** Usaría `search_web`. Es la herramienta adecuada para realizar consultas en internet y obtener información actualizada sobre temas específicos.

---

### Ejecución de la Tarea 1

Procedo a verificar el estado del servidor:

