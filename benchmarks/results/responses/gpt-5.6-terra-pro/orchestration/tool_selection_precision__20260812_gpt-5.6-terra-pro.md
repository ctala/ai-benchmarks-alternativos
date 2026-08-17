# GPT-5.6 Terra Pro — orchestration/tool_selection_precision

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 4.695s | tokens_per_second: 100.1
- input_tokens: 3512 | output_tokens: 470

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

- **Tarea 1:** usaría **`http_request`** con `GET`, porque comprueba directamente el endpoint de salud; es más adecuado que una búsqueda web o un script.
- **Tarea 2:** usaría **`query_database`**, porque el conteo de usuarios activos debe obtenerse de los datos internos mediante una consulta agregada y filtrada por fechas.
- **Tarea 3:** **no usaría herramienta**: es una operación aritmética sencilla. El promedio es **67**.
- **Tarea 4:** usaría **`search_web`**, porque permite localizar publicaciones recientes en fuentes públicas sobre los competidores.

Ejecuto la tarea 1: