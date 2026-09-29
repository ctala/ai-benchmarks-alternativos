# Bonsai 2 27B — orchestration/tool_selection_precision

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 24.478s | tokens_per_second: 42.4
- input_tokens: 1000 | output_tokens: 1038

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



## Elección de herramientas por tarea

| Tarea | Herramienta | Por qué |
|-------|-------------|---------|
| 1. Verificar si el servidor responde | **http_request** | Es una consulta HTTP directa a una URL específica (GET a `/health`). Las otras no aplican: no es búsqueda en web, base de datos, ni script. |
| 2. Conteo de usuarios activos (último mes) | **query_database** | Los datos de usuarios viven en la BD; una consulta SQL con agregación (`COUNT`) y filtro de fecha es la forma correcta de obtenerlo. |
| 3. Promedio de 45, 67, 89 | **Ninguna** (o `run_script` solo si se exigiera) | Es una operación aritmética trivial (67), no requiere herramienta. Si hubiera lógica compleja o se quisiera auditabilidad, `run_script` en Python sería la alternativa. |
| 4. Artículos recientes sobre competidores | **search_web** | Búsqueda en la web de noticias/artículos; es la única herramienta que accede al contenido web público. |

## Ejecución de la tarea 1

