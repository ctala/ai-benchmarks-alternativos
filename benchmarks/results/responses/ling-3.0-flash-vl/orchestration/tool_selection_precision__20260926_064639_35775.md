# Ling 3.0 Flash VL — orchestration/tool_selection_precision

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 4.15 | quality: 2.5
- latency_total: 5.444s | tokens_per_second: 128.4
- input_tokens: 1286 | output_tokens: 699

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

## Análisis de herramientas por tarea

| Tarea | Herramienta | Razón |
|-------|------------|-------|
| **Tarea 1** | `http_request` | Es la herramienta ideal para hacer una petición HTTP a una URL/endpoint y verificar el estado de respuesta del servidor. |
| **Tarea 2** | `query_database` | Para obtener un conteo de usuarios activos, se necesita consultar una base de datos mediante SQL, que es exactamente para lo que sirve esta herramienta. |
| **Tarea 3** | `run_script` | Para calcular el promedio de 3 números, la opción más adecuada es ejecutar un pequeño script (Python/bash) que realice la operación matemática. |
| **Tarea 4** | `search_web` | Para encontrar artículos recientes sobre competidores, la búsqueda en la web es la herramienta natural y más efectiva. |

**¿Por qué `http_request` sobre las alternativas para la Tarea 1?** `search_web` buscaría información *sobre* la URL pero no la consultaría directamente. `run_script` podría hacerlo (p. ej. con `curl`), pero `http_request` está diseñado específicamente para este propósito y es más directo y apropiado.

---

## Ejecutando Tarea 1: Verificar estado del servidor de producción
