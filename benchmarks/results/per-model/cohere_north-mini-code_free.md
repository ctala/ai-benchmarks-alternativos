# North Mini Code

- **model_id**: `cohere/north-mini-code:free`
- **Total tests**: 7/7 exitosos (0 errores)
- **Score final**: 8.00
- **Calidad**: 8.39
- **Velocidad**: 63 tok/s
- **Latencia primera token**: 34.20s
- **Costo promedio por test**: $0.00000

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| code_generation | 4 | 4 | 8.14 | 8.64 |
| reasoning | 3 | 3 | 7.81 | 8.05 |

## Detalle por test

### Razonamiento y Estrategia

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 8.15 | 8.54 | - | 71 | 28.80s | OK |
| logical_reasoning | 8.24 | 8.67 | - | 94 | 16.81s | OK |
| multi_constraint_decision | 7.03 | 6.94 | - | 78 | 26.05s | OK |

<details><summary><code>business_analysis</code> — score 8.15</summary>

**Stats**: latencia 28.80s · 71 tok/s · 157→2046 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
A continuación, encontrarás un análisis conciso y basado en datos de tus tres meses de actividad, junto con las métricas clave solicitadas, las señales de alerta, tres acciones prácticas y una proyección para abril (si las tendencias actuales continúan).

---

## 1️⃣ Cálculo de las métricas clave

|
```

**Respuesta completa**: [`results/responses/20260701_120925_4094866/openrouter-north-mini-code__reasoning__business_analysis.md`](../results/responses/20260701_120925_4094866/openrouter-north-mini-code__reasoning__business_analysis.md)

</details>

<details><summary><code>logical_reasoning</code> — score 8.24</summary>

**Stats**: latencia 16.81s · 94 tok/s · 121→1571 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
**Definamos las variables**

- \(A\) = miembros en el equipo A
- \(B\) = miembros en el equipo B
- \(C\) = miembros en el equipo C
- \(D\) = miembros en el equipo D
- \(E\) = miembros en el equipo E

**Reescribamos las condiciones dadas**

1. \(A > B\) y \(A < C\)
2. \(D = A\)
3. \(E\) es menor que
```

**Respuesta completa**: [`results/responses/20260701_120925_4094866/openrouter-north-mini-code__reasoning__logical_reasoning.md`](../results/responses/20260701_120925_4094866/openrouter-north-mini-code__reasoning__logical_reasoning.md)

</details>

<details><summary><code>multi_constraint_decision</code> — score 7.03</summary>

**Stats**: latencia 26.05s · 78 tok/s · 161→2046 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
## Resumen

| Stack | Lenguajes / Frameworks principales | Base de datos / Almacenamiento | Tiempo real | Búsqueda | Costo de infraestructura mensual aproximado* |
|-------|---------------------------|-------------------|--------------|--------|--------------------------------------|
| **A** – *Reac
```

**Respuesta completa**: [`results/responses/20260701_120925_4094866/openrouter-north-mini-code__reasoning__multi_constraint_decision.md`](../results/responses/20260701_120925_4094866/openrouter-north-mini-code__reasoning__multi_constraint_decision.md)

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 7.68 | 7.87 | - | 59 | 24.77s | OK |
| n8n_workflow_json | 8.24 | 8.67 | - | 60 | 34.02s | OK |
| sql_query_complex | 8.24 | 8.67 | - | 57 | 34.39s | OK |
| debug_code | 8.41 | 9.34 | - | 19 | 74.58s | OK |

<details><summary><code>python_api_integration</code> — score 7.68</summary>

**Stats**: latencia 24.77s · 59 tok/s · 94→1465 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
```python
import time
from typing import List, Dict, Any
import httpx


def fetch_expensive_products(
    token: str,
    url: str = "https://api.example.com/products",
    timeout: float = 10.0,
    max_retries: int = 3,
) -> List[Dict[str, Any]]:
    """
    Obtiene la lista de productos del API,
```

**Respuesta completa**: [`results/responses/20260701_120925_4094866/openrouter-north-mini-code__code_generation__python_api_integration.md`](../results/responses/20260701_120925_4094866/openrouter-north-mini-code__code_generation__python_api_integration.md)

</details>

<details><summary><code>n8n_workflow_json</code> — score 8.24</summary>

**Stats**: latencia 34.02s · 60 tok/s · 113→2048 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
The user asks for a N8N workflow JSON. That's permissible content. We need to generate a JSON representation of a workflow. This is not disallowed. We can provide it. The request is fairly straightforward: a webhook, extract fields, AI node classification, and conditional routing to Slack channels b
```

**Respuesta completa**: [`results/responses/20260701_120925_4094866/openrouter-north-mini-code__code_generation__n8n_workflow_json.md`](../results/responses/20260701_120925_4094866/openrouter-north-mini-code__code_generation__n8n_workflow_json.md)

</details>

<details><summary><code>sql_query_complex</code> — score 8.24</summary>

**Stats**: latencia 34.39s · 57 tok/s · 140→1963 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
**Consulta – “Top 10 clientes por revenue (últimos 6 meses)”**

```sql
/* -------------------------------------------------------------
   1️⃣  Estadísticas de clientes (orders completados en los últimos 6 meses)
   ------------------------------------------------------------- */
WITH customer_stats
```

**Respuesta completa**: [`results/responses/20260701_120925_4094866/openrouter-north-mini-code__code_generation__sql_query_complex.md`](../results/responses/20260701_120925_4094866/openrouter-north-mini-code__code_generation__sql_query_complex.md)

</details>

<details><summary><code>debug_code</code> — score 8.41</summary>

**Stats**: latencia 74.58s · 19 tok/s · 211→1448 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
**Explicación de los problemas**

| # | Bug | Por qué es un problema | Cómo solucionarlo |
|---|-----|--------------------|---------------|
| 1 | **Posible división por cero** (`average = total / len(processed)`) | Si la lista `orders` no contiene órdenes con estado `'pending'`, el bucle no añade ni
```

**Respuesta completa**: [`results/responses/20260701_120925_4094866/openrouter-north-mini-code__code_generation__debug_code.md`](../results/responses/20260701_120925_4094866/openrouter-north-mini-code__code_generation__debug_code.md)

</details>
