# Llama 4 Maverick — orchestration/tool_selection_precision

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 4.082s | tokens_per_second: 76.2
- input_tokens: 1320 | output_tokens: 311

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

**Tarea 1: Verificar si el servidor de produccion esta respondiendo**

* Herramienta: `http_request`
* Razón: La tarea requiere hacer una petición HTTP a una URL específica para verificar si el servidor está respondiendo. La herramienta `http_request` es la más adecuada para esta tarea ya que permite hacer peticiones HTTP con diferentes métodos (GET, POST, PUT, DELETE, etc.).

**Tarea 2: Obtener el conteo de usuarios activos del ultimo mes**

* Herramienta: `query_database`
* Razón: La tarea requiere obtener información de la base de datos, específicamente el conteo de usuarios activos del último mes. La herramienta `query_database` es la más adecuada para esta tarea ya que permite ejecutar consultas SQL en la base de datos.

**Tarea 3: Calcular el promedio de 3 numeros: 45, 67, 89**

* Herramienta: Ninguna
* Razón: La tarea es un cálculo simple que no requiere ninguna herramienta específica. Se puede realizar directamente.

**Tarea 4: Encontrar articulos recientes sobre competidores**

* Herramienta: `search_web`
* Razón: La tarea requiere buscar información en la web sobre competidores. La herramienta `search_web` es la más adecuada para esta tarea ya que permite buscar información en la web con una consulta específica.

Ahora, ejecutaré la Tarea 1:

[http_request(method='GET', url='https://api.example.com/health')]