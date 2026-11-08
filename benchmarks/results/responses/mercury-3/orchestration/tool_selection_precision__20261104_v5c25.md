# Mercury 3 — orchestration/tool_selection_precision

- model_id: `inception/mercury-3`
- success: True  | final: 9.59 | quality: 10.0
- latency_total: 1.616s | tokens_per_second: 482.2
- input_tokens: 1110 | output_tokens: 779

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

Aquí está mi análisis de las 4 tareas:

**Tarea 1: Verificar salud del servidor de producción**
- **Herramienta:** `http_request` (GET)
- **Por qué:** Es una comprobación de estado HTTP directa contra un endpoint de API. `http_request` está diseñada exactamente para esto. Alternativas como `search_web` no sirven, ya que busca información en la web, no hace peticiones a una API específica.

**Tarea 2: Conteo de usuarios activos del último mes**
- **Herramienta:** `query_database` (SQL)
- **Por qué:** Esta es una consulta de datos estructurados almacenados en una base de datos. La herramienta `query_database` permite ejecutar una consulta SQL para agregar y filtrar los datos (por ejemplo, `SELECT COUNT(*) ... WHERE fecha >= ...`).

**Tarea 3: Promedio de 3 números (45, 67, 89)**
- **Herramienta:** Ninguna (cálculo directo)
- **Por qué:** (45 + 67 + 89) / 3 = 201 / 3 = 67. Es aritmética simple que se resuelve mentalmente; no necesita ninguna herramienta.

**Tarea 4: Artículos recientes sobre competidores**
- **Herramienta:** `search_web`
- **Por qué:** Para encontrar contenido actualizado publicado en la web sobre competidores, la búsqueda web es la herramienta adecuada.

---

Ahora ejecuto la **Tarea 1**: verificar si el servidor de producción está respondiendo.

