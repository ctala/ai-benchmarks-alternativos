# Tencent Hy3 — orchestration/tool_selection_precision

- model_id: `tencent/hy3`
- success: True  | final: 8.99 | quality: 10.0
- latency_total: 13.61s | tokens_per_second: 55.6
- input_tokens: 1145 | output_tokens: 757

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

Aquí tienes el análisis de herramientas para cada tarea, y luego ejecuto la Tarea 1.

## Análisis de herramientas por tarea

| Tarea | Herramienta | Por qué |
|-------|-------------|---------|
| **1. Verificar servidor de producción** | `http_request` (GET) | Necesitamos hacer una petición HTTP real a un endpoint (`/health`) para comprobar si responde y con qué estado. Es la herramienta exacta para consumir una API/URL. |
| **2. Conteo de usuarios activos del último mes** | `query_database` | El conteo de usuarios vive en la base de datos. Una consulta SQL (`COUNT` con filtro de fecha/estado) es la vía directa y fiable, sin pasar por una API externa. |
| **3. Promedio de 45, 67, 89** | *Ninguna* | Es una operación aritmética simple (45+67+89 = 201; 201/3 = 67). No requiere herramienta ni datos externos; se resuelve directamente. |
| **4. Artículos recientes sobre competidores** | `search_web` | Buscar información/noveledades en la web es justo lo que hace esta herramienta. No hay base de datos ni API interna que cubra "noticias de competidores". |

**Nota sobre la Tarea 3:** la ejecuto mentalmente sin herramienta, como indica la regla de no usar herramientas innecesarias. Resultado: **67**.

---

## Ejecutando Tarea 1

Verifico el endpoint de salud del servidor de producción con una petición GET.