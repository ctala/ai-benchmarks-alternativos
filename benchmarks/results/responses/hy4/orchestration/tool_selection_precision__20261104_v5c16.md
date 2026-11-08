# Tencent Hy4 — orchestration/tool_selection_precision

- model_id: `tencent/hy4`
- success: True  | final: 6.96 | quality: 7.5
- latency_total: 17.393s | tokens_per_second: 86.5
- input_tokens: 1053 | output_tokens: 1504

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

## Elección de herramienta por tarea

| # | Tarea | Herramienta | Por qué (y por qué no las alternativas) |
|---|-------|-------------|------------------------------------------|
| 1 | Verificar `https://api.example.com/health` | **`http_request`** (GET) | Es una comprobación directa de un endpoint HTTP: devuelve código de estado, cabeceras y cuerpo en vivo. `search_web` solo sirve para contenido indexado (no estado en tiempo real de una API) y `run_script` con `curl`/`requests` sería una capa innecesaria de indirección. |
| 2 | Conteo de usuarios activos del último mes | **`query_database`** (SQL: `SELECT COUNT(*) ... WHERE last_active >= ...`) | Son datos internos y estructurados; la BD es la fuente de verdad. `search_web` no tiene acceso a datos privados y `http_request` requeriría un endpoint de analítica que no se ha especificado. |
| 3 | Promedio de 45, 67, 89 | **Ninguna herramienta** | Operación aritmética trivial y determinista: la regla de orquestación dice «si algo no requiere herramienta, no la uses». `run_script` sería la única opción plausible si hubiera que dejar constancia o integrarlo en un pipeline, pero aquí sería un uso innecesario. (Resultado directo: 201 / 3 = 67.) |
| 4 | Artículos recientes sobre competidores | **`search_web`** | Información externa, pública y cambiante, que requiere frescura: es exactamente el caso de un buscador. `query_database` es interno, `http_request` necesitaría una URL conocida y `run_script` no indexa la web por sí solo. |

Ahora ejecuto **solo la tarea 1**, con una petición GET al health check: