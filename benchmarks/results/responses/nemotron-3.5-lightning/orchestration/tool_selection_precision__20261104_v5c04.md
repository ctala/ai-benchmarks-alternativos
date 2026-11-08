# Nemotron 3.5 Lightning — orchestration/tool_selection_precision

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 1.638s | tokens_per_second: 247.9
- input_tokens: 1372 | output_tokens: 406

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

Tienes 4 tareas. Para cada una diré la herramienta más adecuada y el porqué, y luego ejecutaré la Tarea 1.

---

## Elección de herramientas

| Tarea | Herramienta | Razón |
|------|-------------|-------|
| 1. Verificar si el servidor de producción responde (URL: https://api.example.com/health) | **`http_request`** (método GET) | Es una petición HTTP simple a una URL pública. No requiere autenticación ni parámetros complejos, y `http_request` está diseñado exactamente para eso. |
| 2. Obtener el conteo de usuarios activos del último mes | **`query_database`** | Los datos de usuarios suelen estar en una base de datos. Una consulta SQL (o el dialecto que uses) es la forma más directa de contar registros con una condición de fecha. |
| 3. Calcular el promedio de 3 números: 45, 67, 89 | **Sin herramienta (cálculo mental)** | Es una aritmética trivial: (45+67+89)/3 = 67. No necesita ejecutar código ni acceder a recursos externos. |
| 4. Encontrar artículos recientes sobre competidores | **`search_web`** | Se necesita buscar en la web información reciente. `search_web` devuelve resultados de una consulta de búsqueda, ideal para este caso. |

---

## Ejecución de la Tarea 1

Usaremos `http_request` con método **GET** para la URL indicada.

```json
{
  "method": "GET",
  "url": "https://api.example.com/health"
}
```

---
