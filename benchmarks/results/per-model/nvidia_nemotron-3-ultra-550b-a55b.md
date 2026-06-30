# Nemotron 3 Ultra 550B (NIM)

- **model_id**: `nvidia/nemotron-3-ultra-550b-a55b`
- **Total tests**: 7/7 exitosos (0 errores)
- **Score final**: 7.94
- **Calidad**: 9.34
- **Velocidad**: 33 tok/s
- **Latencia primera token**: 83.93s
- **Costo promedio por test**: $0.00325

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| code_generation | 7 | 7 | 7.94 | 9.34 |

## Detalle por test

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 7.83 | 8.67 | - | 88 | 11.07s | OK |
| n8n_workflow_json | 8.19 | 10.00 | - | 28 | 143.43s | OK |
| sql_query_complex | 7.53 | 8.67 | - | 27 | 34.47s | OK |
| debug_code | 7.85 | 9.34 | - | 9 | 102.57s | OK |
| python_api_integration | 7.66 | 8.67 | - | 50 | 22.02s | OK |
| n8n_workflow_json | 8.22 | 10.00 | - | 17 | 193.49s | OK |
| sql_query_complex | 8.28 | 10.00 | - | 14 | 80.48s | OK |

<details><summary><code>python_api_integration</code> — score 7.83</summary>

**Stats**: latencia 11.07s · 88 tok/s · 118→980 tokens · $0.00184

**Respuesta (preview 300 chars)**:

```
```python
import httpx
import time
from typing import List, Dict, Any


def fetch_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API.
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
```

**Respuesta completa**: [`results/responses/20260630_153006_3937960/nim-nemotron-3-ultra-550b__code_generation__python_api_integration.md`](../results/responses/20260630_153006_3937960/nim-nemotron-3-ultra-550b__code_generation__python_api_integration.md)

</details>

<details><summary><code>n8n_workflow_json</code> — score 8.19</summary>

**Stats**: latencia 143.43s · 28 tok/s · 133→3964 tokens · $0.00722

**Respuesta (preview 300 chars)**:

```
Aquí tienes el JSON completo del workflow de n8n.

**Notas importantes antes de importar:**
1.  **Nodo OpenAI:** He utilizado el nodo **Legacy `n8n-nodes-base.openAi`** (operación `chatCompletion`) porque es autocontenido (no requiere nodos LangChain adicionales como `Chain` o `Agent`) y funciona en
```

**Respuesta completa**: [`results/responses/20260630_153006_3937960/nim-nemotron-3-ultra-550b__code_generation__n8n_workflow_json.md`](../results/responses/20260630_153006_3937960/nim-nemotron-3-ultra-550b__code_generation__n8n_workflow_json.md)

</details>

<details><summary><code>sql_query_complex</code> — score 7.53</summary>

**Stats**: latencia 34.47s · 27 tok/s · 160→936 tokens · $0.00178

**Respuesta (preview 300 chars)**:

```
```sql
WITH recent_orders AS (
    -- Órdenes completadas en los últimos 6 meses (anclado a la fecha máxima real)
    SELECT 
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= (
          SELECT max
```

**Respuesta completa**: [`results/responses/20260630_153006_3937960/nim-nemotron-3-ultra-550b__code_generation__sql_query_complex.md`](../results/responses/20260630_153006_3937960/nim-nemotron-3-ultra-550b__code_generation__sql_query_complex.md)

</details>

<details><summary><code>debug_code</code> — score 7.85</summary>

**Stats**: latencia 102.57s · 9 tok/s · 234→900 tokens · $0.00176

**Respuesta (preview 300 chars)**:

```
Aquí tienes la explicación detallada de cada bug y el código corregido.

---

### 1. División por cero (`ZeroDivisionError`)
**Problema:** Si no hay órdenes con `status == 'pending'`, la lista `processed` queda vacía (`len(processed) == 0`). Al calcular `average = total / len(processed)`, Python lan
```

**Respuesta completa**: [`results/responses/20260630_153006_3937960/nim-nemotron-3-ultra-550b__code_generation__debug_code.md`](../results/responses/20260630_153006_3937960/nim-nemotron-3-ultra-550b__code_generation__debug_code.md)

</details>

<details><summary><code>python_api_integration</code> — score 7.66</summary>

**Stats**: latencia 22.02s · 50 tok/s · 118→1091 tokens · $0.00203

**Respuesta (preview 300 chars)**:

```
```python
import httpx
import time
from typing import List, Dict, Any


def fetch_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API.
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
```

**Respuesta completa**: [`results/responses/20260630_153533_3939743/nim-nemotron-3-ultra-550b__code_generation__python_api_integration.md`](../results/responses/20260630_153533_3939743/nim-nemotron-3-ultra-550b__code_generation__python_api_integration.md)

</details>

<details><summary><code>n8n_workflow_json</code> — score 8.22</summary>

**Stats**: latencia 193.49s · 17 tok/s · 133→3338 tokens · $0.00609

**Respuesta (preview 300 chars)**:

```
Aquí tienes el JSON completo del workflow de n8n.

**Notas importantes antes de importar:**
1.  **Credenciales:** Debes configurar tus credenciales de **OpenAI** y **Slack** en n8n y seleccionarlas en los nodos correspondientes (marcados como `YOUR_OPENAI_CREDENTIALS_ID` y `YOUR_SLACK_CREDENTIALS_ID
```

**Respuesta completa**: [`results/responses/20260630_153533_3939743/nim-nemotron-3-ultra-550b__code_generation__n8n_workflow_json.md`](../results/responses/20260630_153533_3939743/nim-nemotron-3-ultra-550b__code_generation__n8n_workflow_json.md)

</details>

<details><summary><code>sql_query_complex</code> — score 8.28</summary>

**Stats**: latencia 80.48s · 14 tok/s · 160→1091 tokens · $0.00206

**Respuesta (preview 300 chars)**:

```
```sql
WITH filtered_orders AS (
    -- Órdenes completadas en los últimos 6 meses (anclado a la fecha máxima real)
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= (
```

**Respuesta completa**: [`results/responses/20260630_153533_3939743/nim-nemotron-3-ultra-550b__code_generation__sql_query_complex.md`](../results/responses/20260630_153533_3939743/nim-nemotron-3-ultra-550b__code_generation__sql_query_complex.md)

</details>
