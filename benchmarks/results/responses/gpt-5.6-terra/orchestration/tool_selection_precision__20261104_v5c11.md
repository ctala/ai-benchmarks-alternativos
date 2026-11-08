# GPT-5.6 Terra — orchestration/tool_selection_precision

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 2.9s | tokens_per_second: 90.7
- input_tokens: 511 | output_tokens: 263

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

1. **Verificar el servidor de producción:** usaría **`http_request`** con `GET`, porque permite consultar directamente el endpoint de salud. Es más apropiada que una búsqueda web, que no verifica la disponibilidad real del servicio.

2. **Conteo de usuarios activos del último mes:** usaría **`query_database`**, porque el dato debe obtenerse mediante una consulta agregada sobre la base de datos; habría que conocer el esquema exacto y qué define a un usuario “activo”.

3. **Promedio de 45, 67 y 89:** no usaría ninguna herramienta, ya que es un cálculo sencillo: \((45 + 67 + 89) / 3 = 67\).

4. **Artículos recientes sobre competidores:** usaría **`search_web`**, ya que busca fuentes y publicaciones recientes en la web. Haría falta especificar qué competidores o sector se deben cubrir.

Ahora ejecuto la tarea 1.