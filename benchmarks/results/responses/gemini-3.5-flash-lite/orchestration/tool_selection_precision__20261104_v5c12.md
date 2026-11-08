# Gemini 3.5 Flash Lite — orchestration/tool_selection_precision

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 2.156s | tokens_per_second: 169.7
- input_tokens: 500 | output_tokens: 366

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

Para cada una de las tareas propuestas, indico la herramienta adecuada y el motivo:

*   **Tarea 1: Verificar si el servidor de producción está respondiendo (`https://api.example.com/health`)**
    *   **Herramienta:** `http_request`
    *   **Por qué:** Es la herramienta diseñada específicamente para realizar llamadas HTTP (como un GET) a una URL externa y comprobar el estado o la respuesta de una API o servidor.
*   **Tarea 2: Obtener el conteo de usuarios activos del último mes**
    *   **Herramienta:** `query_database`
    *   **Por qué:** Los datos estructurados de usuarios y su actividad suelen encontrarse almacenados en bases de datos relacionales o analíticas, por lo que una consulta SQL es la vía directa para extraer esta métrica.
*   **Tarea 3: Calcular el promedio de 3 números: 45, 67, 89**
    *   **Herramienta:** Ninguna (o `run_script` si se requiere ejecución automática)
    *   **Por qué:** Se trata de una operación matemática básica que se puede resolver directamente de forma lógica sin necesidad de llamadas externas ni herramientas pesadas.
*   **Tarea 4: Encontrar artículos recientes sobre competidores**
    *   **Herramienta:** `search_web`
    *   **Por qué:** Permite buscar información actualizada y reciente en la web abierta sobre cualquier temática o competidores específicos.

---

### Ejecución de la Tarea 1:

A continuación, ejecuto la **Tarea 1** utilizando la herramienta `http_request` para verificar el estado de la API de producción.