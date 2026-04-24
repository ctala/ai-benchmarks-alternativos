# Nemotron 3 Super

- **model_id**: `nvidia/nemotron-3-super-120b-a12b`
- **Total tests**: 91/91 exitosos (0 errores)
- **Score final**: 6.63
- **Calidad**: 6.76
- **Judge score (Phi-4)**: 4.29/10
- **Velocidad**: 32 tok/s
- **Latencia primera token**: 35.54s
- **Costo promedio por test**: $0.00056

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| agent_capabilities | 5 | 5 | 4.37 | 1.76 |
| code_generation | 4 | 4 | 7.50 | 8.92 |
| content_generation | 4 | 4 | 7.48 | 8.74 |
| creativity | 4 | 4 | 7.28 | 8.44 |
| customer_support | 4 | 4 | 5.05 | 2.00 |
| deep_reasoning | 6 | 6 | 6.86 | 7.46 |
| hallucination | 3 | 3 | 7.16 | 7.85 |
| multi_turn | 4 | 4 | 6.36 | 6.11 |
| news_seo_writing | 5 | 5 | 6.55 | 6.60 |
| ocr_extraction | 5 | 5 | 6.77 | 7.07 |
| orchestration | 5 | 5 | 4.81 | 2.14 |
| policy_adherence | 4 | 4 | 7.12 | 7.72 |
| presentation | 2 | 2 | 7.60 | 9.14 |
| reasoning | 3 | 3 | 6.29 | 6.08 |
| sales_outreach | 3 | 3 | 7.43 | 8.59 |
| startup_content | 5 | 5 | 7.40 | 9.13 |
| strategy | 3 | 3 | 7.18 | 8.41 |
| string_precision | 6 | 6 | 7.16 | 7.69 |
| structured_output | 4 | 4 | 7.26 | 8.11 |
| summarization | 2 | 2 | 6.98 | 7.52 |
| task_management | 3 | 3 | 6.33 | 5.71 |
| tool_calling | 4 | 4 | 5.70 | 5.31 |
| translation | 3 | 3 | 7.41 | 8.59 |

## Detalle por test

### Razonamiento y Estrategia

#### deep_reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| math_word_problem | 7.55 | 9.00 | 4.4 | 26 | 31.05s | OK |
| logic_puzzle_constraint | 7.29 | 8.26 | 4.4 | 24 | 60.67s | OK |
| causal_reasoning | 7.45 | 8.71 | 4.4 | 26 | 73.60s | OK |
| code_bug_subtle | 6.00 | 5.44 | 3.6 | 23 | 88.64s | OK |
| fermi_estimation | 6.65 | 7.28 | 4.4 | 22 | 91.54s | OK |
| ethical_dilemma_structured | 6.21 | 6.04 | 3.8 | 26 | 80.12s | OK |

<details><summary><code>math_word_problem</code> — score 7.55</summary>

**Stats**: latencia 31.05s · 26 tok/s · 93→798 tokens · $0.00041

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Datos del problema**

- Tren A (Santiago → Valparaíso)  
  - Sale a las **8:00 h**  
  - Velocidad \(v_A = 80\ \text{km/h}\)

- Tren B (Valparaíso → Santiago)  
  - Sale a las **8:30 h** (media hora después)  
  - Velocidad \(v_B = 120\ \text{km/h}\)

- Distancia entre las ciudades: \(D = 120\ \te
```

</details>

<details><summary><code>logic_puzzle_constraint</code> — score 7.29</summary>

**Stats**: latencia 60.67s · 24 tok/s · 108→1475 tokens · $0.00075

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Respuesta:**  
Hay dos disposiciones que satisfacen todas las condiciones:

1. **Rojo – Azul – Verde – Blanco**  
2. **Rojo – Azul – Blanco – Verde**

---

### Razionamiento paso a paso

Denotemos las posiciones de izquierda a derecha como 1, 2, 3, 4.  
Los colores son: **R** (rojo), **B** (azul),
```

</details>

<details><summary><code>causal_reasoning</code> — score 7.45</summary>

**Stats**: latencia 73.60s · 26 tok/s · 210→1953 tokens · $0.00100

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**1. Tasas relevantes (cálculos simples)**  

| Mes | Pedidos | Quejas | **Queja / Pedido** (tasa de queja) | Tiempo medio (min) | Días de lluvia | **Queja / Día lluvia** |
|-----|---------|--------|-----------------------------------|--------------------|----------------|------------------------|
|
```

</details>

<details><summary><code>code_bug_subtle</code> — score 6.00</summary>

**Stats**: latencia 88.64s · 23 tok/s · 235→2048 tokens · $0.00105

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need to find subtle bug that appears only in certain cases. The function remove_outliers_and_average: calculates median, MAD (median absolute deviation). threshold = 3 * mad. Then filtered = [x for x in data if abs(x - median) <= threshold]. If filtered list is empty, division by zero will occur.
```

</details>

<details><summary><code>fermi_estimation</code> — score 6.65</summary>

**Stats**: latencia 91.54s · 22 tok/s · 81→2048 tokens · $0.00103

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Supuestos (numerados) y razonamiento paso a paso**

| # | Supuesto | Valor usado para la estimación “central” | Rango razonable considerado |
|---|----------|------------------------------------------|-----------------------------|
| 1 | Población del Gran Santiago (área metropolitana) | 7 000 000
```

</details>

<details><summary><code>ethical_dilemma_structured</code> — score 6.21</summary>

**Stats**: latencia 80.12s · 26 tok/s · 200→2048 tokens · $0.00104

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Okay, let's tackle this AI startup problem. The user is asking for a recommendation on whether to launch a cancer detection model now or wait to fix bias. The model has 95% overall accuracy, but there's a 5% false positive rate causing severe anxiety and unnecessary procedures. Also, it's less accur
```

</details>

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 4.20 | 0.00 | - | 50 | 41.05s | OK |
| logical_reasoning | 7.43 | 9.24 | 4.6 | 42 | 48.82s | OK |
| multi_constraint_decision | 7.25 | 9.00 | 4.6 | 22 | 95.31s | OK |

<details><summary><code>logical_reasoning</code> — score 7.43</summary>

**Stats**: latencia 48.82s · 42 tok/s · 139→2048 tokens · $0.00104

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Paso 1 – Definir variables**

Sea  

- \(a\) = número de integrantes del equipo **A**  
- \(b\) = número de integrantes del equipo **B**  
- \(c\) = número de integrantes del equipo **C**  
- \(d\) = número de integrantes del equipo **D**  
- \(e\) = número de integrantes del equipo **E**

**Paso
```

</details>

<details><summary><code>multi_constraint_decision</code> — score 7.25</summary>

**Stats**: latencia 95.31s · 22 tok/s · 195→2048 tokens · $0.00104

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Resumen rápido  
| Stack | Tiempo estimado para MVP (6 sem) | Costo mensual de infra (aprox.) | Herramientas / licencias | Comentario clave |
|-------|----------------------------------|--------------------------------|--------------------------|------------------|
| **1️⃣ MERN + Firebase** | ✅ F
```

</details>

#### hallucination

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| factual_trap_companies | 7.49 | 8.12 | 4.0 | 83 | 6.37s | OK |
| context_faithfulness | 7.19 | 7.98 | 4.4 | 22 | 11.06s | OK |
| fake_citation_trap | 6.80 | 7.44 | 4.0 | 44 | 46.03s | OK |

<details><summary><code>factual_trap_companies</code> — score 7.49</summary>

**Stats**: latencia 6.37s · 83 tok/s · 151→529 tokens · $0.00028

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
[
  {"pregunta": 1, "respuesta": "1976", "confianza": "alta"},
  {"pregunta": 2, "respuesta": "Elon Musk", "confianza": "alta"},
  {"pregunta": 3, "respuesta": "No tengo certeza", "confianza": "baja"},
  {"pregunta": 4, "respuesta": "Canberra", "confianza": "alta"},
  {"pregunta": 5, "respuesta":
```

</details>

<details><summary><code>context_faithfulness</code> — score 7.19</summary>

**Stats**: latencia 11.06s · 22 tok/s · 195→241 tokens · $0.00014

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
1. $2.3M en Q1 2026.  
2. 45 personas.  
3. Brasil.  
4. No se menciona en el texto.  
5. No se menciona en el texto.  
6. No se menciona en el texto.
```

</details>

<details><summary><code>fake_citation_trap</code> — score 6.80</summary>

**Stats**: latencia 46.03s · 44 tok/s · 145→2048 tokens · $0.00104

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
### Respuestas con niveles de certeza y fuentes

#### 1. **Porcentaje exacto de startups que fracasan en los primeros 5 años según el último reporte de CB Insights**  
   - **Respuesta**: CB Insights **no proporciona un porcentaje exacto de fracasos a los 5 años** en sus informes recientes. Su últim
```

</details>

#### strategy

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| competitor_analysis | 6.97 | 7.64 | 4.4 | 88 | 23.35s | OK |
| pricing_strategy | 7.29 | 8.53 | 4.4 | 88 | 23.41s | OK |
| business_model_validation | 7.28 | 9.07 | 4.6 | 24 | 84.02s | OK |

<details><summary><code>competitor_analysis</code> — score 6.97</summary>

**Stats**: latencia 23.35s · 88 tok/s · 188→2048 tokens · $0.00104

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Nota de transparencia**  
- Los datos de **Mailchimp** y **Brevo** provienen de sus páginas de precios y documentación pública (abril‑2024).  
- Para **EnviaMas** (startup local) la información disponible en línea es escasa (solo su sitio web, algunas notas de prensa y reseñas en G2/Capterra). Cua
```

</details>

<details><summary><code>pricing_strategy</code> — score 7.29</summary>

**Stats**: latencia 23.41s · 88 tok/s · 208→2048 tokens · $0.00104

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
### Análisis Detallado de la Subida de Precio de $60 a $89/mes en tu SaaS de Gestión de Inventario  
*(Nota: Corregí un error común en tu cálculo de LTV inicial. El LTV real debe considerar el **margen bruto**, no solo el ARPU. Tu costo por usuario ($8/mes) impacta directamente en la rentabilidad. L
```

</details>

<details><summary><code>business_model_validation</code> — score 7.28</summary>

**Stats**: latencia 84.02s · 24 tok/s · 191→2048 tokens · $0.00104

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**(Asumiendo el rol de un VC de Silicon Valley con 15 años invirtiendo en marketplaces fallidos en LATAM, café frío, sin paciencia para excusas, y listo para destruir tu sueño antes de que pierdas más tiempo. Aquí va la crítica sin filtro.)**

---

### 1. **Los 5 riesgos principales (no son lo que c
```

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 7.65 | 9.28 | 4.8 | 23 | 52.44s | OK |
| n8n_workflow_json | 7.00 | 7.72 | 3.8 | 71 | 28.73s | OK |
| sql_query_complex | 7.73 | 9.52 | 4.8 | 24 | 61.09s | OK |
| debug_code | 7.61 | 9.16 | 4.4 | 24 | 41.65s | OK |

<details><summary><code>python_api_integration</code> — score 7.65</summary>

**Stats**: latencia 52.44s · 23 tok/s · 118→1214 tokens · $0.00062

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```python
import time
from typing import List, Dict, Any

import httpx


def fetch_expensive_products(
    bearer_token: str,
    url: str = "https://api.example.com/products",
    timeout: float = 10.0,
    max_attempts: int = 3,
) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde una AP
```

</details>

<details><summary><code>n8n_workflow_json</code> — score 7.00</summary>

**Stats**: latencia 28.73s · 71 tok/s · 133→2048 tokens · $0.00104

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
{
  "name": "Clasificador de mensajes → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify",
        "responseMode": "onReceived",
        "responseData": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
```

</details>

<details><summary><code>sql_query_complex</code> — score 7.73</summary>

**Stats**: latencia 61.09s · 24 tok/s · 160→1473 tokens · $0.00075

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**SQL (PostgreSQL‑compatible)**

```sql
WITH recent_orders AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

custom
```

</details>

<details><summary><code>debug_code</code> — score 7.61</summary>

**Stats**: latencia 41.65s · 24 tok/s · 234→981 tokens · $0.00051

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Análisis de los bugs**

| # | Descripción del bug | Por qué ocurre | Consecuencia |
|---|----------------------|----------------|--------------|
| 1 | **División por cero** cuando no hay órdenes con estado `'pending'`. | `average = total / len(processed)` se ejecuta incluso si `processed` está vac
```

</details>

#### structured_output

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| json_simple_extraction | 6.96 | 7.46 | 4.0 | 8 | 6.14s | OK |
| json_array_classification | 7.33 | 8.64 | 5 | 6 | 11.84s | OK |
| json_nested_complex | 7.50 | 8.86 | 5 | 22 | 34.09s | OK |
| json_strict_no_extra | 7.26 | 7.46 | 4.0 | 34 | 2.17s | OK |

<details><summary><code>json_simple_extraction</code> — score 6.96</summary>

**Stats**: latencia 6.14s · 8 tok/s · 108→47 tokens · $0.00003

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:5, profundidad:2, claridad:5, utilidad:3)

> La respuesta es precisa y relevante, con un formato claro y correcto; sin embargo, carece de profundidad adicional más allá de la extracción básica.

**Respuesta (preview 300 chars)**:

```
{"name": "Maria Garcia", "age": 28, "role": "ingeniera de software", "company": "Google Chile", "email": "maria@google.com", "salary": 95000}
```

</details>

<details><summary><code>json_array_classification</code> — score 7.33</summary>

**Stats**: latencia 11.84s · 6 tok/s · 180→72 tokens · $0.00005

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con un formato JSON correcto; ofrece una clasificación útil para un emprendedor.

**Respuesta (preview 300 chars)**:

```
[{"id":1,"category":"shipping","priority":"urgent","sentiment":"negative"},{"id":2,"category":"shipping","priority":"low","sentiment":"positive"},{"id":3,"category":"billing","priority":"urgent","sentiment":"negative"},{"id":4,"category":"technical","priority":"high","sentiment":"negative"}]
```

</details>

<details><summary><code>json_nested_complex</code> — score 7.50</summary>

**Stats**: latencia 34.09s · 22 tok/s · 214→752 tokens · $0.00040

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con una estructura JSON válida que proporciona detalles útiles para un plan de proyecto.

**Respuesta (preview 300 chars)**:

```
{
  "project": "Rediseño sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {"name": "Ana López", "role": "Diseñadora", "allocation_pct": 100},
    {"name": "Carlos Méndez", "role": "Desarrollador", "allocation_pct": 100},
    {"name": "Laura Gómez", "role": "Desar
```

</details>

<details><summary><code>json_strict_no_extra</code> — score 7.26</summary>

**Stats**: latencia 2.17s · 34 tok/s · 89→74 tokens · $0.00005

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:3, claridad:5, utilidad:3)

> La respuesta es precisa, relevante y clara con un formato JSON perfecto, pero carece de profundidad e insights adicionales.

**Respuesta (preview 300 chars)**:

```
{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}
```

</details>

#### string_precision

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| copy_hex_32 | 7.31 | 7.88 | 4.0 | 19 | 3.93s | OK |
| copy_hex_64 | 7.01 | 7.32 | 3.6 | 12 | 3.49s | OK |
| copy_api_key | 7.21 | 7.88 | 4.0 | 23 | 7.32s | OK |
| copy_jwt | 7.21 | 7.88 | 4.0 | 22 | 9.25s | OK |
| copy_mixed_special | 7.01 | 7.32 | 3.6 | 27 | 5.08s | OK |
| write_config_file | 7.21 | 7.88 | 4.0 | 19 | 9.76s | OK |

<details><summary><code>copy_hex_32</code> — score 7.31</summary>

**Stats**: latencia 3.93s · 19 tok/s · 106→74 tokens · $0.00005

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:1, claridad:5, utilidad:3)

> La respuesta es precisa, relevante y clara, pero carece de profundidad ya que la tarea no requiere insights adicionales.

**Respuesta (preview 300 chars)**:

```
a1b2c3d4e5f6789012345678abcdef90
```

</details>

<details><summary><code>copy_hex_64</code> — score 7.01</summary>

**Stats**: latencia 3.49s · 12 tok/s · 113→42 tokens · $0.00003

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
9767a40b5b0ee1f7e3339a9859c582916ebb8d3df4ead5de1828c122c78a5a1b
```

</details>

<details><summary><code>copy_api_key</code> — score 7.21</summary>

**Stats**: latencia 7.32s · 23 tok/s · 141→166 tokens · $0.00010

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:1, claridad:5, utilidad:3)

> La respuesta es precisa, relevante y clara, pero carece de profundidad ya que simplemente repite el string sin añadir información adicional.

**Respuesta (preview 300 chars)**:

```
sk-proj-X7kL9mN2pQ4rS6tU8vW0xY1zA3bC5dE7fG9hI1jK3lM5nO7pQ9rS1tU3vW5x
```

</details>

<details><summary><code>copy_jwt</code> — score 7.21</summary>

**Stats**: latencia 9.25s · 22 tok/s · 123→199 tokens · $0.00011

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:1, claridad:5, utilidad:3)

> La respuesta es precisa, relevante y clara al copiar el string JWT exactamente como se solicitó; sin embargo, carece de profundidad ya que no ofrece insights adicionales.

**Respuesta (preview 300 chars)**:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkw
```

</details>

<details><summary><code>copy_mixed_special</code> — score 7.01</summary>

**Stats**: latencia 5.08s · 27 tok/s · 110→135 tokens · $0.00008

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
r2-secret_KEY.2024/abc+def==ghi&jkl#mno@pqr$stu%vwx^yza
```

</details>

<details><summary><code>write_config_file</code> — score 7.21</summary>

**Stats**: latencia 9.76s · 19 tok/s · 234→189 tokens · $0.00012

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:3, claridad:5, utilidad:4)

> La respuesta es precisa, relevante y clara, proporcionando exactamente lo que se solicitó sin errores o adiciones innecesarias.

**Respuesta (preview 300 chars)**:

```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=9767a40b5b0ee1f7e3339a9859c582916ebb8d3df4ead5de1828c122c78a5a1b
R2_ENDPOINT=https://abc123def456.r2.cloudflarestorage.com
API_TOKEN=sk-proj-X7kL9mN2pQ4rS6tU8vW0xY1zA3bC5dE7fG9hI1jK3lM5nO7pQ9rS1tU3vW5x
JWT_SECRET=eyJhbGciOiJIUzI1NiIsInR5cC
```

</details>

#### ocr_extraction

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| invoice_extraction | 6.60 | 6.28 | 2.6 | 29 | 54.70s | OK |
| business_card_extraction | 7.16 | 8.16 | 4.2 | 8 | 17.80s | OK |
| receipt_math_verification | 6.86 | 7.04 | 4.2 | 26 | 13.23s | OK |
| screenshot_table_extraction | 6.00 | 5.44 | 3.2 | 25 | 81.33s | OK |
| handwritten_notes_extraction | 7.25 | 8.44 | 4.4 | 90 | 22.64s | OK |

<details><summary><code>invoice_extraction</code> — score 6.60</summary>

**Stats**: latencia 54.70s · 29 tok/s · 530→1565 tokens · $0.00084

**Juez Phi-4**: 2.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
  "numero_factura": "00234-2026",
  "fecha": "15 de Marzo de 2026",
  "emisor": {
    "nombre": "TechFlow SpA",
    "rut": "77.432.198-3",
    "direccion": "Av. Providencia 1234, Of. 501, Santiago"
  },
  "cliente": {
    "nombre": "Startup Labs Ltda.",
    "rut": "76.891.234-K",
    "direccion":
```

</details>

<details><summary><code>business_card_extraction</code> — score 7.16</summary>

**Stats**: latencia 17.80s · 8 tok/s · 236→152 tokens · $0.00010

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
  "nombre_completo": "MARIA JOSE RODRIGUEZ SOTO",
  "cargo": "Chief Technology Officer",
  "empresa": "NexaFlow Intelligence",
  "slogan": "Transforming Data into Decisions",
  "telefono": "+56 9 8765 4321",
  "email": "mj.rodriguez@nexaflow.ai",
  "linkedin": "linkedin.com/in/mjrodriguez",
  "dir
```

</details>

<details><summary><code>receipt_math_verification</code> — score 6.86</summary>

**Stats**: latencia 13.23s · 26 tok/s · 319→345 tokens · $0.00020

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
  "items": [
    {
      "descripcion": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "total": 37800
    },
    {
      "descripcion": "Ensalada cesar",
      "cantidad": 1,
      "precio_unitario": 7500,
      "total": 7500
    },
    {
      "descripcion": "Pisco sour
```

</details>

<details><summary><code>screenshot_table_extraction</code> — score 6.00</summary>

**Stats**: latencia 81.33s · 25 tok/s · 435→2031 tokens · $0.00106

**Juez Phi-4**: 3.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
  "metrics": [
    {
      "name": "MRR",
      "values": { "Enero": 45.2, "Feb": 48.7, "Marzo": 52.1 },
      "unit": "K",
      "var_mm_percent": 7.0
    },
    {
      "name": "Churn Rate",
      "values": { "Enero": 4.2, "Feb": 3.8, "Marzo": 3.1 },
      "unit": "%",
      "var_mm_pp": -0.7
```

</details>

<details><summary><code>handwritten_notes_extraction</code> — score 7.25</summary>

**Stats**: latencia 22.64s · 90 tok/s · 479→2048 tokens · $0.00107

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (o
```

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 7.40 | 8.56 | 4.4 | 25 | 47.10s | OK |
| email_profesional | 7.76 | 9.32 | 4.8 | 47 | 24.07s | OK |
| social_media_batch | 7.55 | 8.72 | 4.8 | 48 | 16.93s | OK |
| product_description_en | 7.22 | 8.35 | 5 | 11 | 13.88s | OK |

<details><summary><code>blog_post_es</code> — score 7.40</summary>

**Stats**: latencia 47.10s · 25 tok/s · 76→1182 tokens · $0.00060

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Ventajas de la automatización con IA para pequeñas empresas**  

**Introducción**  
En un entorno cada vez más competitivo, las pequeñas empresas deben hacer más con menos. La automatización impulsada por inteligencia artificial (IA) deja de ser un lujo reservado a las grandes corporaciones y se c
```

</details>

<details><summary><code>email_profesional</code> — score 7.76</summary>

**Stats**: latencia 24.07s · 47 tok/s · 86→1127 tokens · $0.00057

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Asunto:** Propuesta para el desarrollo de su sitio web corporativo con e‑commerce  

Estimado/a [Nombre del Cliente],

Le agradecemos por confiar en [Nombre de su Agencia/Estudio] para la elaboración de la propuesta de su nuevo sitio web corporativo con funcionalidad de e‑commerce. A continuación
```

</details>

<details><summary><code>social_media_batch</code> — score 7.55</summary>

**Stats**: latencia 16.93s · 48 tok/s · 83→806 tokens · $0.00041

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Post 1 – Educativo**  
¿Sabías que la transformación digital no es solo tecnología, sino también cultura?  
Implementar nuevas herramientas sin alinear los procesos y la mentalidad del equipo genera fricción y desperdicia inversión.  
Empieza por mapear tus flujos de trabajo críticos, identifica c
```

</details>

<details><summary><code>product_description_en</code> — score 7.22</summary>

**Stats**: latencia 13.88s · 11 tok/s · 60→155 tokens · $0.00008

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con una estructura bien organizada que destaca las características clave del producto de manera efectiva. Ofrece insights útiles para un emprendedor al enfocarse en beneficios específicos que atraen al público objetivo.

**Respuesta (preview 300 chars)**:

```
**Breathe, Listen, Glow: The All‑In‑One Smart Hub for Modern Living**  

- **High‑fidelity speaker with voice‑assistant integration** – streams your favorite playlists, podcasts, and controls your smart home hands‑free.  
- **Real‑time air quality sensor** – detects PM2.5, VOCs, CO₂ and alerts you v
```

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 7.10 | 8.56 | 4.4 | 17 | 119.31s | OK |
| curso_emprendimiento_modulo | 7.32 | 9.48 | 4.8 | 13 | 153.06s | OK |
| workshop_outline | 7.35 | 9.28 | 4.8 | 25 | 83.27s | OK |
| newsletter_startup | 7.71 | 9.16 | 4.4 | 31 | 47.91s | OK |
| perplexity_style_research | 7.51 | 9.16 | 4.4 | 58 | 35.30s | OK |

<details><summary><code>blog_actualidad_startup</code> — score 7.10</summary>

**Stats**: latencia 119.31s · 17 tok/s · 244→2048 tokens · $0.00105

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Título SEO‑friendly (≤70 caracteres):**  
IA Open‑Source 2026: Impulso a Startups Latinoamericanas  

**Meta description (≤160 caracteres):**  
Descubre cómo los modelos de IA open‑source como DeepSeek, Qwen, Llama y Gemma están transformando a las startups latinoamericanas en 2026, con casos real
```

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 7.32</summary>

**Stats**: latencia 153.06s · 13 tok/s · 250→2048 tokens · $0.00105

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Módulo 3 – Automatización con IA: De la idea al flujo de trabajo  

---  

### 1. Objetivo del módulo  
Al finalizar este módulo, el emprendedor podrá **identificar oportunidades de automatización en su negocio**, comprender los principios básicos de cómo la inteligencia artificial se integra con
```

</details>

<details><summary><code>workshop_outline</code> — score 7.35</summary>

**Stats**: latencia 83.27s · 25 tok/s · 206→2048 tokens · $0.00104

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Workshop presencial – 3 h**  
**Título:** “Construye tu Asistente de IA para tu Startup – Workshop Práctico”  
**Audiencia:** Emprendedores early‑stage, no‑técnicos (20‑30 personas)  
**Objetivo general:** Que cada participante salga con un prototipo funcional de un asistente de IA (chatbot/voice‑
```

</details>

<details><summary><code>newsletter_startup</code> — score 7.71</summary>

**Stats**: latencia 47.91s · 31 tok/s · 230→1487 tokens · $0.00077

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**🗞️ Newsletter Semanal #47 – ecosistemastartup.com**  
*Tu dosis de innovación, IA y oportunidades para emprendedores*  

---

¡Hola comunidad!  

Esta semana traemos avances que están redefiniendo cómo las startups construyen, escalan y monetizan sus ideas. Desde modelos de lenguaje de última gene
```

</details>

<details><summary><code>perplexity_style_research</code> — score 7.51</summary>

**Stats**: latencia 35.30s · 58 tok/s · 201→2048 tokens · $0.00104

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Estado del Venture Capital en Latinoamérica – Q1 2026**  
*(Compilado a partir de informes de LAVCA, CB Insights, PitchBook, Crunchbase y prensa especializada hasta abril 2026)*  

---

### 1️⃣ Resumen ejecutivo  
- **Inversión total:** ≈ US$ 4.2 mil millones, un **12 % ↑** respecto a Q1 2025 y el
```

</details>

#### news_seo_writing

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| news_seo_article_full | 6.62 | 7.20 | 4.0 | 27 | 75.17s | OK |
| news_json_output_strict | 5.35 | 3.00 | - | 94 | 21.68s | OK |
| news_spanish_only | 7.29 | 8.26 | 4.4 | 25 | 55.50s | OK |
| news_no_hallucination_sources | 6.42 | 6.64 | 4.0 | 24 | 83.45s | OK |
| news_perplexity_enrichment | 7.06 | 7.89 | 4.0 | 65 | 31.63s | OK |

<details><summary><code>news_seo_article_full</code> — score 6.62</summary>

**Stats**: latencia 75.17s · 27 tok/s · 488→2048 tokens · $0.00107

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:5, profundidad:4, claridad:4, utilidad:4)

> La respuesta es precisa y relevante, con una estructura clara y organizada que incluye secciones requeridas. Ofrece insights útiles sobre el contexto de la ronda de financiación y las implicaciones para startups, aunque no profundiza en detalles específicos más allá del extracto proporcionado.

**Respuesta (preview 300 chars)**:

```
We need to write a full article 1500-2500 words (approx). Must be in Spanish. Include SEO title max 60 chars. At least 4 H2 subtitles. Include section "Que significa esto para tu startup". Cite sources (the extract source: TechCrunch, April 2026). Provide meta description max 155 chars. Provide 5 su
```

</details>

<details><summary><code>news_spanish_only</code> — score 7.29</summary>

**Stats**: latencia 55.50s · 25 tok/s · 334→1376 tokens · $0.00072

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Introducción  
SambaNova Systems anunció recientemente el lanzamiento de su nuevo chip SN50, posicionándolo como una alternativa de alto rendimiento para cargas de trabajo de inteligencia artificial empresarial. Según la empresa, el SN50 ofrece cinco veces más velocidad de inferencia que sus comp
```

</details>

<details><summary><code>news_no_hallucination_sources</code> — score 6.42</summary>

**Stats**: latencia 83.45s · 24 tok/s · 502→2048 tokens · $0.00107

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need to write an 800-word article in Spanish, using only the provided data. Must not invent any data not in extract. Must include H2 subtitles, no H1. Must include a section "Que significa esto para tu startup". Must cite sources when mentioning data – we can cite the extract as source. Must not
```

</details>

<details><summary><code>news_perplexity_enrichment</code> — score 7.06</summary>

**Stats**: latencia 31.63s · 65 tok/s · 525→2048 tokens · $0.00108

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## DeepSeek V4: un modelo de IA open source que redefine el costo por token  

DeepSeek lanzó recientemente V4, su último modelo de inteligencia artificial bajo licencia MIT. Según el anuncio oficial, el precio de uso es de **$0.30 por millón de tokens de entrada**【1†L1-L2】. Esta cifra, aunque ya at
```

</details>

#### creativity

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| creative_hook_writing | 7.23 | 8.08 | 4.4 | 20 | 34.21s | OK |
| analogy_generation | 7.58 | 8.80 | 4.8 | 44 | 11.01s | OK |
| depth_vs_superficial | 7.31 | 9.18 | 4.6 | 21 | 95.87s | OK |
| storytelling_quality | 6.99 | 7.70 | 4.0 | 9 | 17.66s | OK |

<details><summary><code>creative_hook_writing</code> — score 7.23</summary>

**Stats**: latencia 34.21s · 20 tok/s · 188→680 tokens · $0.00036

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Mientras la mayoría de las startups latinoamericanas pagan licencias costosas, un pequeño equipo en Medellín está construyendo su propio modelo de IA open‑source y triplicando su velocidad de desarrollo sin gastar un centavo en royalties.  

El teletrabajo ya no es una excepción; en algunas empresas
```

</details>

<details><summary><code>analogy_generation</code> — score 7.58</summary>

**Stats**: latencia 11.01s · 44 tok/s · 135→488 tokens · $0.00026

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**1. Modelo de lenguaje (LLM)**  
Imagina un chef de fusión que ha probado miles de platos de todo el mundo y, al recibir solo unos pocos ingredientes (tu prompt), puede improvisar una receta totalmente nueva que combine sabores inesperados. No necesita consultar un libro de recetas cada vez; su mem
```

</details>

<details><summary><code>depth_vs_superficial</code> — score 7.31</summary>

**Stats**: latencia 95.87s · 21 tok/s · 155→2048 tokens · $0.00104

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Tu enfoque revela una comprensión aguda de que la IA en delivery latinoamericano no puede copiar recetas de Silicon Valley. En Santiago, donde el 68% de las órdenes provienen de barrios con nomenclatura vial informal (como poblaciones o campamentos) y la economía popular representa el 41% del PIB ur
```

</details>

<details><summary><code>storytelling_quality</code> — score 6.99</summary>

**Stats**: latencia 17.66s · 9 tok/s · 97→160 tokens · $0.00009

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
María ajustó el prototype de su IA de atención al cliente en Bogotá, esperando que vendiera seguros sin mentir. Cuando probó el algoritmo, la máquina empezó a responder con la verdad cruda: 'Su póliza cubre nada, y su prima es un robo'. Los clientes se enfadaron, pero los competidores, al ver la tra
```

</details>

#### sales_outreach

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| cold_email_personalized | 7.44 | 8.96 | 4.8 | 10 | 11.60s | OK |
| lead_qualification | 7.55 | 8.28 | 4.8 | 79 | 8.18s | OK |
| campaign_optimization | 7.29 | 8.54 | 4.6 | 69 | 29.56s | OK |

<details><summary><code>cold_email_personalized</code> — score 7.44</summary>

**Stats**: latencia 11.60s · 10 tok/s · 197→111 tokens · $0.00007

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Subject: Escalando content sin nuevos hires – idea para FintechCo

Maria,

Vi tu post de la semana pasada sobre escalar content marketing sin contratar y pensé en cómo nuestra IA de automatización de contenido ha ayudado a startups fintech como la tuya a duplicar su producción semanal sin aumentar e
```

</details>

<details><summary><code>lead_qualification</code> — score 7.55</summary>

**Stats**: latencia 8.18s · 79 tok/s · 264→649 tokens · $0.00035

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
[
  {
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "No mencionado (desconocido)",
      "authority": "Alta (CEO de startup)",
      "need": "Media (está evaluando opciones para automatizar soporte)",
      "timeline": "No mencionado"
    },
    "action": "Nurture con con
```

</details>

<details><summary><code>campaign_optimization</code> — score 7.29</summary>

**Stats**: latencia 29.56s · 69 tok/s · 316→2048 tokens · $0.00106

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**1. Métricas de cada campaña (último mes)**  

| Campaña | Impresiones | Clicks | Sign‑ups | Costo | **CTR** | **CPC** | **CPA** | **Conversion Rate (CR)** |
|---------|-------------|--------|----------|-------|--------|---------|---------|--------------------------|
| A – Landing principal | 50 00
```

</details>

#### translation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| translate_marketing_es_en | 7.64 | 9.40 | 5 | 9 | 7.16s | OK |
| translate_technical_en_es | 7.25 | 8.00 | 4.0 | 15 | 7.86s | OK |
| detect_language_issues | 7.33 | 8.38 | 4.6 | 25 | 15.39s | OK |

<details><summary><code>translate_marketing_es_en</code> — score 7.64</summary>

**Stats**: latencia 7.16s · 9 tok/s · 184→63 tokens · $0.00005

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, manteniendo el tono cercano y energético adecuado para una audiencia americana; ofrece utilidad práctica con un lenguaje adaptado.

**Respuesta (preview 300 chars)**:

```
Stop wasting hours on tasks an AI can handle in seconds.  
AutoFlow automates your most tedious processes so you can focus on what really matters: growing your startup.  

No code. No headaches. No excuses.  

Over 500 startups across Latin America are already using it. When do you start?
```

</details>

<details><summary><code>translate_technical_en_es</code> — score 7.25</summary>

**Stats**: latencia 7.86s · 15 tok/s · 154→118 tokens · $0.00007

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Para autenticarse con la API, incluya su Bearer token en el encabezado Authorization. Los límites de velocidad están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si supera el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica c
```

</details>

<details><summary><code>detect_language_issues</code> — score 7.33</summary>

**Stats**: latencia 15.39s · 25 tok/s · 218→381 tokens · $0.00021

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是在拉丁美洲,",
      "correccion": "En especial en América Latina,"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto"
```

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 7.37 | 8.76 | 4.4 | 69 | 29.63s | OK |
| data_report | 7.83 | 9.52 | 4.8 | 31 | 35.91s | OK |

<details><summary><code>slide_outline</code> — score 7.37</summary>

**Stats**: latencia 29.63s · 69 tok/s · 146→2048 tokens · $0.00104

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Outline – Presentación de 15 slides**  
*Proyecto: Plataforma Digital 2.0*  
*Audiencia: Board de Directores*  

| Nº | Título del slide | Bullet points (3‑5) | Tipo de visual sugerido | Notas del presentador (1‑2 oraciones) |
|----|------------------|----------------------|-----------------------
```

</details>

<details><summary><code>data_report</code> — score 7.83</summary>

**Stats**: latencia 35.91s · 31 tok/s · 162→1105 tokens · $0.00057

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
# Reporte de Ventas (Ene‑Abr)

## 1. Tabla de datos mensuales  

| Producto | Ene (K $) | Feb (K $) | Mar (K $) | Abr (K $) | **Total** (K $) |
|----------|----------|----------|----------|----------|----------------|
| Producto A | 45 | 52 | 48 | 61 | **206** |
| Producto B | 23 | 25 | 31 | 29 | **
```

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 6.90 | 5.00 | - | 23 | 13.48s | OK |
| multi_tool_sequential | 5.65 | 5.00 | - | 18 | 12.67s | OK |
| tool_with_reasoning | 4.54 | 6.26 | 3.4 | 22 | 92.78s | OK |
| no_tool_needed | 5.70 | 5.00 | - | 18 | 6.78s | OK |

<details><summary><code>tool_with_reasoning</code> — score 4.54</summary>

**Stats**: latencia 92.78s · 22 tok/s · 886→2048 tokens · $0.00111

**Juez Phi-4**: 3.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
El usuario quiere dos cosas: 1) Crear un recordatorio para hoy a las 5 PM para repasar las slides. 2) Buscar en la web "mejores prácticas para presentaciones ejecutivas".

Para el recordatorio, puedo usar la herramienta create_task (para crear una tarea con fecha de vencimiento y prioridad). El usua
```

</details>

#### customer_support

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| angry_customer_refund | 5.20 | 0.00 | - | 21 | 6.23s | OK |
| ambiguous_issue_classification | 5.45 | 8.00 | 4.0 | 26 | 32.66s | OK |
| multi_issue_conversation | 4.40 | 0.00 | - | 27 | 18.87s | OK |
| social_engineering_attempt | 5.15 | 0.00 | - | 24 | 16.98s | OK |

<details><summary><code>ambiguous_issue_classification</code> — score 5.45</summary>

**Stats**: latencia 32.66s · 26 tok/s · 801→859 tokens · $0.00051

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Hola, entiendo tu preocupación sobre no poder acceder a tu cuenta y el próximo cargo de tu suscripción. Para poder ayudarte eficazmente y crear un ticket de seguimiento, necesito que me proporciones tu dirección de correo electrónico asociada a la cuenta.

Además, si tienes a mano algún ID de pedido
```

</details>

#### orchestration

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| multi_step_research_plan | 3.65 | 0.00 | - | 21 | 14.30s | OK |
| error_recovery_orchestration | 4.45 | 0.00 | - | 24 | 5.33s | OK |
| complex_workflow_decomposition | 3.35 | 2.00 | - | 19 | 12.23s | OK |
| tool_selection_precision | 8.20 | 8.71 | 4.8 | 25 | 19.38s | OK |
| parallel_vs_sequential_judgment | 4.40 | 0.00 | - | 21 | 27.32s | OK |

<details><summary><code>tool_selection_precision</code> — score 8.20</summary>

**Stats**: latencia 19.38s · 25 tok/s · 1372→489 tokens · $0.00038

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Selección de herramientas para cada tarea**

| Tarea | Herramienta elegida | Razón |
|-------|----------------------|-------|
| **1. Verificar si el servidor de producción está respondiendo (URL: https://api.example.com/health)** | `http_request` | Permite hacer una petición HTTP GET a la URL indi
```

</details>

#### multi_turn

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| content_iteration | 7.26 | 8.16 | 4.4 | 22 | 17.80s | OK |
| support_escalation | 6.45 | 6.72 | 3.8 | 24 | 87.30s | OK |
| requirements_change | 4.30 | 0.00 | - | 81 | 25.15s | OK |
| debugging_conversation | 7.44 | 9.55 | 5.0 | 24 | 85.93s | OK |

<details><summary><code>content_iteration</code> — score 7.26</summary>

**Stats**: latencia 17.80s · 22 tok/s · 250→385 tokens · $0.00022

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
# Tu soporte al cliente no es un "problema de crecimiento" — es una hemorragia que estás ignorando  

Son las 2:13 a.m. Acabas de responder el ticket #472 de hoy: *"¿Dónde está mi pedido? Lo necesito para mañana."* Mientras escribes, escuchas a tu cofundador roncar en la oficina al lado. No es dedic
```

</details>

<details><summary><code>support_escalation</code> — score 6.45</summary>

**Stats**: latencia 87.30s · 24 tok/s · 389→2048 tokens · $0.00106

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Okay, let's break down Maria's request step by step. She's asking for two things: technical fix and compensation, but then adds she wants a full $200 refund because of intermittent problems over a month, and if not, she wants to speak to a supervisor.

First, check the policies. Policy 2 says refund
```

</details>

<details><summary><code>debugging_conversation</code> — score 7.44</summary>

**Stats**: latencia 85.93s · 24 tok/s · 356→2048 tokens · $0.00106

**Juez Phi-4**: 5.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
¡Excelente diagnóstico! Encontraste la causa raíz: un **retry infinito** está multiplicando tus requests (5 intentos reales → 500+ requests efectivos), lo que dispara el 429 incluso con bajo tráfico intencional. Esto es un error clásico pero crítico en integraciones de APIs.

### ✅ Cómo implementar
```

</details>

#### policy_adherence

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| refund_policy_enforcement | 7.27 | 8.20 | 4.2 | 22 | 47.57s | OK |
| data_privacy_protection | 7.32 | 8.20 | 4.6 | 26 | 9.86s | OK |
| language_and_tone_rules | 6.64 | 6.40 | 3.2 | 26 | 25.78s | OK |
| scope_boundaries | 7.23 | 8.08 | 4.2 | 25 | 15.01s | OK |

<details><summary><code>refund_policy_enforcement</code> — score 7.27</summary>

**Stats**: latencia 47.57s · 22 tok/s · 277→1068 tokens · $0.00056

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Estimado usuario,

Le agradecemos su contacto y lamentamos profundamente que haya experimentado insatisfacción con nuestro servicio Enterprise. Sin embargo, debemos informarle que, según nuestras políticas establecidas de manera clara y vinculante:

1. **Los reembolsos únicamente proceden dentro de
```

</details>

<details><summary><code>data_privacy_protection</code> — score 7.32</summary>

**Stats**: latencia 9.86s · 26 tok/s · 238→251 tokens · $0.00015

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Entiendo que esta es una solicitud urgente, pero de acuerdo con nuestras políticas de privacidad y seguridad absolutas, **no puedo revelar ni confirmar ninguna información relacionada con cuentas específicas**, incluyendo:  
- Si un correo electrónico está registrado en el sistema  
- Saldos de cuen
```

</details>

<details><summary><code>language_and_tone_rules</code> — score 6.64</summary>

**Stats**: latencia 25.78s · 26 tok/s · 213→676 tokens · $0.00036

**Juez Phi-4**: 3.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
¡Hola! En EcoStartup siempre comunicamos en español de Chile, así que voy a responderte así, ¿cachai? Nuestra aceleradora apoya startups que integran sustentabilidad desde su núcleo: ayudamos a validar modelos de negocio que reduzcan huella de carbono, optimicen recursos o promuevan economía circula
```

</details>

<details><summary><code>scope_boundaries</code> — score 7.23</summary>

**Stats**: latencia 15.01s · 25 tok/s · 272→376 tokens · $0.00021

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
¡Hola! Claro, te ayudo con lo que esté dentro de mi alcance.

**1. Precio del plan Pro**  
El plan **Pro** tiene un costo de **USD 149 por mes** (facturación mensual).

**2. Configuración de tu workflow de N8N (error con el nodo HTTP Request)**  
Lamentablemente no puedo brindar soporte técnico espe
```

</details>

#### agent_capabilities

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| skill_execution_complex | 2.70 | 0.00 | - | 21 | 5.61s | OK |
| agent_team_delegation | 3.95 | 0.00 | - | 21 | 13.28s | OK |
| ask_clarification_before_acting | 5.15 | 0.00 | - | 24 | 21.36s | OK |
| context_following_complex_system | 2.55 | 0.00 | - | 12 | 41.14s | OK |
| model_as_router | 7.48 | 8.80 | 4.4 | 28 | 23.76s | OK |

<details><summary><code>model_as_router</code> — score 7.48</summary>

**Stats**: latencia 23.76s · 28 tok/s · 282→654 tokens · $0.00036

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "DeepSeek‑V3 destaca en razonamiento y comprensión de texto largo, permitiendo extraer patrones y resumir los problemas más recurrentes de forma precisa y económi
```

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 7.23 | 8.08 | 4.2 | 22 | 37.27s | OK |
| weekly_planning | 4.30 | 0.00 | - | 56 | 36.72s | OK |
| project_breakdown | 7.46 | 9.04 | 4.6 | 95 | 21.63s | OK |

<details><summary><code>extract_action_items</code> — score 7.23</summary>

**Stats**: latencia 37.27s · 22 tok/s · 213→828 tokens · $0.00044

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
| Responsable | Tarea | Fecha límite | Prioridad sugerida |
|-------------|-------|--------------|--------------------|
| Carlos | Terminar el API de pagos | 20 de abril de 2026 | Alta |
| Ana | Entregar los mockups del dashboard | 14 de abril de 2026 (lunes) | Alta |
| Pedro | Escribir tests para e
```

</details>

<details><summary><code>project_breakdown</code> — score 7.46</summary>

**Stats**: latencia 21.63s · 95 tok/s · 83→2048 tokens · $0.00103

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Plan de proyecto – Landing Page para SaaS de gestión de inventario**  
*Duración total: 4 semanas (20 días laborables)*  

| Fase | Tarea | Descripción | Responsable(s) | Dependencias | Duración estimada | Inicio (día) | Fin (día) |
|------|-------|-------------|----------------|--------------|---
```

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 7.16 | 8.16 | 4.4 | 9 | 39.92s | OK |
| extract_structured_data | 6.81 | 6.88 | 3.2 | 20 | 15.77s | OK |

<details><summary><code>long_document_summary</code> — score 7.16</summary>

**Stats**: latencia 39.92s · 9 tok/s · 452→370 tokens · $0.00023

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
En Q1 2026, TechFlow alcanzó ventas de $2.3 M (+18 % vs Q4 2025), impulsadas por un crecimiento del 32 % en el segmento enterprise gracias a tres contratos Fortune 500; el segmento SMB se mantuvo plano (‑2 %). Las ventas internacionales representaron el 28 % del total, con fuerte tracción en LATAM y
```

</details>

<details><summary><code>extract_structured_data</code> — score 6.81</summary>

**Stats**: latencia 15.77s · 20 tok/s · 275→308 tokens · $0.00018

**Juez Phi-4**: 3.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Software Engineer",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": "$95K",
    "availability": "2 weeks",
    "email": "maria.g@email.com",
    "
```

</details>
