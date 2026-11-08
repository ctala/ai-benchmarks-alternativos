# Muse Glimmer 30B — orchestration/tool_selection_precision

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.27 | quality: 7.5
- latency_total: 5.492s | tokens_per_second: 128.0
- input_tokens: 1293 | output_tokens: 703

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

Para cada tarea la herramienta más apropiada sería:

**Tarea 1: Verificar si el servidor de producción está respondiendo**
Herramienta: **http_request**
Por qué: Necesitas hacer una petición HTTP real a `https://api.example.com/health` y comprobar el código de estado / respuesta. No es una búsqueda web ni una consulta a base de datos. `http_request` con GET es la herramienta específica para comprobar la salud de un endpoint.

**Tarea 2: Obtener el conteo de usuarios activos del último mes**
Herramienta: **query_database**
Por qué: El conteo de usuarios activos es un dato transaccional interno. Se obtiene con SQL sobre la base de datos donde se almacenan los usuarios y sus fechas de última actividad. No es información web pública ni un cálculo simple.

**Tarea 3: Calcular el promedio de 3 números: 45, 67, 89**
Herramienta: **run_script**
Por qué: Es un cálculo determinista simple. Con `run_script` en python puedes calcularlo de forma reproducible. No requiere web, archivo ni base de datos. Se podría hacer mentalmente, pero usar script garantiza trazabilidad.

**Tarea 4: Encontrar artículos recientes sobre competidores**
Herramienta: **search_web**
Por qué: Necesitas información actual publicada en internet sobre competidores. `search_web` está diseñado para búsquedas web con resultados recientes. No es un dato interno de la empresa.

Ahora ejecuto la Tarea 1:
