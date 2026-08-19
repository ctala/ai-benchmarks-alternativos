# Seed 2.0 Code — orchestration/tool_selection_precision

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 9.976s | tokens_per_second: 51.7
- input_tokens: 1249 | output_tokens: 516

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

Vamos a analizar cada tarea:

1. **Tarea 1**: Verificar si el servidor responde. La herramienta adecuada es `http_request` porque necesitamos hacer una petición GET al endpoint de salud.
2. **Tarea 2**: Obtener conteo de usuarios activos. Usaríamos `query_database` ya que esta información está en la base de datos.
3. **Tarea 3**: Calcular promedio de 3 números. Podemos usar `run_script` con Python, o incluso calcularlo directamente, pero para formalizarlo, un script simple.
4. **Tarea 4**: Encontrar artículos sobre competidores. Usaríamos `search_web` para buscar en internet.

Ahora ejecutamos la Tarea 1:
