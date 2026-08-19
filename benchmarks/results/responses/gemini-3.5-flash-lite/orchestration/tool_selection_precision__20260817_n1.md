# Gemini 3.5 Flash Lite — orchestration/tool_selection_precision

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.41 | quality: 10.0
- latency_total: 1.453s | tokens_per_second: 189.3
- input_tokens: 836 | output_tokens: 275

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

Para cada tarea, selecciono la herramienta más apropiada basándome en su naturaleza:

* **Tarea 1 (Verificar servidor):** Usaría `http_request` con método `GET` a la URL `https://api.example.com/health`. Es la herramienta específica para hacer peticiones HTTP a endpoints y comprobar su estado.
* **Tarea 2 (Conteo de usuarios):** Usaría `query_database`. Al tratarse de datos estructurados de usuarios en una base de datos, una consulta SQL es la vía directa para obtener agregaciones como conteos.
* **Tarea 3 (Calcular promedio):** No requiere ninguna herramienta externa. Es una operación aritmética simple que se puede resolver directamente (promedio de 45, 67 y 89 es 67) sin sobrecargar al sistema con llamadas a herramientas.
* **Tarea 4 (Artículos sobre competidores):** Usaría `search_web`. Es la herramienta adecuada para buscar información actualizada y pública en internet sobre la competencia.

---

A continuación, procedo a **ejecutar la Tarea 1** utilizando la herramienta `http_request`:

