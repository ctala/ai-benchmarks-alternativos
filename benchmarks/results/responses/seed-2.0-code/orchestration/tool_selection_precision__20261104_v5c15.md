# Seed 2.0 Code — orchestration/tool_selection_precision

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 9.737s | tokens_per_second: 69.0
- input_tokens: 1249 | output_tokens: 672

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

Voy a analizar cada tarea y seleccionar la herramienta más apropiada:

## Análisis de herramientas por tarea:

**Tarea 1: Verificar servidor de producción**
- **Herramienta: `http_request`**
- **Por qué:** Necesito hacer una petición HTTP GET a la URL del health check para verificar si el servidor responde. Es la herramienta diseñada específicamente para interactuar con APIs y URLs web.

**Tarea 2: Conteo de usuarios activos**
- **Herramienta: `query_database`**
- **Por qué:** Los datos de usuarios activos generalmente están almacenados en una base de datos. Necesitaría ejecutar una consulta SQL para obtener este conteo del último mes.

**Tarea 3: Calcular promedio de 3 números**
- **Herramienta: `run_script` (o incluso se puede calcular manualmente)**
- **Por qué:** Es un cálculo matemático simple. Podría usar un script Python de una línea, aunque este cálculo es tan básico que ni siquiera necesitaría una herramienta: (45+67+89)/3 = 67.

**Tarea 4: Encontrar artículos sobre competidores**
- **Herramienta: `search_web`**
- **Por qué:** Necesito buscar información actualizada en internet sobre competidores. Es la herramienta diseñada para realizar búsquedas web.

---

## Ejecutando Tarea 1: Verificar servidor de producción
