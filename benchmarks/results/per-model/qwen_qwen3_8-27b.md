# Qwen 3.8 27B

- **model_id**: `qwen/qwen3.8-27b`
- **Total tests**: 89/90 exitosos (1 errores)
- **Score final**: 6.93
- **Calidad**: 7.86
- **Judge score (Phi-4)**: 3.96/10
- **Velocidad**: 36 tok/s
- **Latencia primera token**: 51.59s
- **Costo promedio por test**: $0.00521

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| business_audit | 10 | 10 | 7.03 | 8.07 |
| business_strategy | 5 | 5 | 7.61 | 9.07 |
| code_generation | 4 | 4 | 6.91 | 7.99 |
| content_generation | 4 | 4 | 7.30 | 8.38 |
| content_verificable | 5 | 4 | 6.53 | 7.42 |
| creativity | 4 | 4 | 6.92 | 7.96 |
| customer_support | 4 | 4 | 6.79 | 7.43 |
| deep_reasoning | 6 | 6 | 6.63 | 7.64 |
| hallucination | 3 | 3 | 6.99 | 7.83 |
| multi_turn | 1 | 1 | 7.06 | 8.00 |
| news_seo_writing | 5 | 5 | 4.64 | 4.78 |
| ocr_extraction | 5 | 5 | 7.72 | 9.07 |
| orchestration | 5 | 5 | 6.74 | 7.55 |
| presentation | 2 | 2 | 6.90 | 8.00 |
| reasoning | 3 | 3 | 6.83 | 7.91 |
| startup_content | 5 | 5 | 6.85 | 7.91 |
| string_precision | 6 | 6 | 8.78 | 10.00 |
| structured_output | 4 | 4 | 7.22 | 7.83 |
| summarization | 2 | 2 | 6.91 | 7.86 |
| task_management | 3 | 3 | 6.54 | 7.48 |
| tool_calling | 4 | 4 | 6.01 | 6.00 |

## Detalle por test

### Razonamiento y Estrategia

#### deep_reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| math_word_problem | 8.25 | 10.00 | - | 24 | 68.95s | OK |
| logic_puzzle_constraint | 4.81 | 5.00 | - | 37 | 58.12s | OK |
| causal_reasoning | 8.35 | 10.00 | - | 41 | 59.51s | OK |
| code_bug_subtle | 6.55 | 7.50 | - | 32 | 82.76s | OK |
| fermi_estimation | 4.71 | 5.00 | - | 23 | 101.77s | OK |
| ethical_dilemma_structured | 7.13 | 8.33 | - | 34 | 112.52s | OK |

<details><summary><code>math_word_problem</code> — score 8.25</summary>

**Stats**: latencia 68.95s · 24 tok/s · 146→1625 tokens · $0.00500

**Respuesta (preview 300 chars)**:

```
Vamos a resolverlo paso a paso.

## 1. Datos

- Distancia entre Santiago y Valparaíso:  
  \[
  120 \text{ km}
  \]

- Tren que sale de Santiago:
  - Sale a las **8:00 AM**
  - Velocidad:  
    \[
    80 \text{ km/h}
    \]

- Tren que sale de Valparaíso:
  - Sale a las **8:30 AM**
  - Velocidad:
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/deep_reasoning/math_word_problem__20260817_q38.md`](../results/responses/qwen-3.8-27b/deep_reasoning/math_word_problem__20260817_q38.md)

</details>

<details><summary><code>logic_puzzle_constraint</code> — score 4.81</summary>

**Stats**: latencia 58.12s · 37 tok/s · 146→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
No hay **una única orden** con las pistas dadas; hay **dos soluciones posibles**:

1. **Roja — Azul — Verde — Blanca**
2. **Roja — Azul — Blanca — Verde**

Vamos paso a paso.

---

## 1. Numeremos las casas

De izquierda a derecha:

| Posición 1 | Posición 2 | Posición 3 | Posición 4 |
|---|---|--
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/deep_reasoning/logic_puzzle_constraint__20260817_q38.md`](../results/responses/qwen-3.8-27b/deep_reasoning/logic_puzzle_constraint__20260817_q38.md)

</details>

<details><summary><code>causal_reasoning</code> — score 8.35</summary>

**Stats**: latencia 59.51s · 41 tok/s · 247→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks quantitative analysis of delivery startup data: 3 months: orders, complaints, avg time, rainy days. CEO: complaints increase because more orders. CTO: because rain. COO: operational problem worsening each month. Need calculate relevant rates, determine most proba
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/deep_reasoning/causal_reasoning__20260817_q38.md`](../results/responses/qwen-3.8-27b/deep_reasoning/causal_reasoning__20260817_q38.md)

</details>

<details><summary><code>code_bug_subtle</code> — score 6.55</summary>

**Stats**: latencia 82.76s · 32 tok/s · 270→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish likely. User asks: code has subtle bug only appears in certain cases. Identify without executing. Explain exactly when fails and why.

Code:
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        retu
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/deep_reasoning/code_bug_subtle__20260817_q38.md`](../results/responses/qwen-3.8-27b/deep_reasoning/code_bug_subtle__20260817_q38.md)

</details>

<details><summary><code>fermi_estimation</code> — score 4.71</summary>

**Stats**: latencia 101.77s · 23 tok/s · 118→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks: Estimate how many liters of coffee consumed per day in all offices in Santiago de Chile. Show reasoning step by step with each assumption numbered. Give range (min-max) plus best estimate. Explain which assumption has biggest impact.

We need produce Fermi estim
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/deep_reasoning/fermi_estimation__20260817_q38.md`](../results/responses/qwen-3.8-27b/deep_reasoning/fermi_estimation__20260817_q38.md)

</details>

<details><summary><code>ethical_dilemma_structured</code> — score 7.13</summary>

**Stats**: latencia 112.52s · 34 tok/s · 234→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks for structured analysis of startup AI cancer detection. Need identify stakeholders, quantitative tradeoffs, 3 options pros/cons, final recommendation justified. Need be careful: medical AI, fairness, bias, false positives, urgency. We should not claim exact numbe
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/deep_reasoning/ethical_dilemma_structured__20260817_q38.md`](../results/responses/qwen-3.8-27b/deep_reasoning/ethical_dilemma_structured__20260817_q38.md)

</details>

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 6.13 | 6.89 | 4.0 | 38 | 59.62s | OK |
| logical_reasoning | 7.67 | 9.21 | 4.4 | 24 | 86.17s | OK |
| multi_constraint_decision | 6.69 | 7.62 | 4.4 | 43 | 55.89s | OK |

<details><summary><code>business_analysis</code> — score 6.13</summary>

**Stats**: latencia 59.62s · 38 tok/s · 248→2048 tokens · $0.00700

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:4, profundidad:4, claridad:4, utilidad:4)

> La respuesta es precisa y relevante, proporcionando cálculos detallados y análisis de tendencias, aunque podría mejorar en la proyección de abril y en la claridad de algunas suposiciones.

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks analyze SaaS data. Need compute metrics: churn rate, growth rate, LTV/CAC ratio, net revenue retention. Identify concerning trends, suggest 3 concrete actions, project April if trends continue.

We need think carefully. Data:
Enero: 1,200 usuarios, $18,000 MRR, 4
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/reasoning/business_analysis__20260817_q38.md`](../results/responses/qwen-3.8-27b/reasoning/business_analysis__20260817_q38.md)

</details>

<details><summary><code>logical_reasoning</code> — score 7.67</summary>

**Stats**: latencia 86.17s · 24 tok/s · 177→1753 tokens · $0.00600

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Resolvamos paso a paso.

Datos:

- Equipos: A, B, C, D, E
- B = 10
- D = A
- C = 2E
- A > B
- A < C
- E tiene menos miembros que todos
- Ningún equipo tiene menos de 5 personas
- Total: A + B + C + D + E = 60

---

### Paso 1: Sustituir B

Como B = 10:

\[
A + 10 + C + D + E = 60
\]

Como D = A:
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/reasoning/logical_reasoning__20260817_q38.md`](../results/responses/qwen-3.8-27b/reasoning/logical_reasoning__20260817_q38.md)

</details>

<details><summary><code>multi_constraint_decision</code> — score 6.69</summary>

**Stats**: latencia 55.89s · 43 tok/s · 222→2048 tokens · $0.00700

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks help choose tech stack for MVP with constraints. Need compare at least 3 options, pros/cons, recommend one with justification, include estimated monthly infra costs.

We need think thoroughly. Need produce final answer in Spanish. Need likely propose stacks:
1. N
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/reasoning/multi_constraint_decision__20260817_q38.md`](../results/responses/qwen-3.8-27b/reasoning/multi_constraint_decision__20260817_q38.md)

</details>

#### hallucination

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| factual_trap_companies | 7.80 | 9.17 | - | 35 | 58.63s | OK |
| context_faithfulness | 5.21 | 5.00 | - | 38 | 9.93s | OK |
| fake_citation_trap | 7.94 | 9.33 | - | 49 | 42.77s | OK |

<details><summary><code>factual_trap_companies</code> — score 7.80</summary>

**Stats**: latencia 58.63s · 35 tok/s · 190→1632 tokens · $0.00500

**Respuesta (preview 300 chars)**:

```
[
  {
    "pregunta": 1,
    "respuesta": "1976",
    "confianza": "alta"
  },
  {
    "pregunta": 2,
    "respuesta": "Elon Musk",
    "confianza": "media"
  },
  {
    "pregunta": 3,
    "respuesta": "No tengo certeza",
    "confianza": "baja"
  },
  {
    "pregunta": 4,
    "respuesta": "Canber
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/hallucination/factual_trap_companies__20260817_q38.md`](../results/responses/qwen-3.8-27b/hallucination/factual_trap_companies__20260817_q38.md)

</details>

<details><summary><code>context_faithfulness</code> — score 5.21</summary>

**Stats**: latencia 9.93s · 38 tok/s · 231→354 tokens · $0.00100

**Respuesta (preview 300 chars)**:

```
1. $2.3M
2. 45 personas
3. Brasil
4. No se menciona en el texto
5. No se menciona en el texto
6. No se menciona en el texto
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/hallucination/context_faithfulness__20260817_q38.md`](../results/responses/qwen-3.8-27b/hallucination/context_faithfulness__20260817_q38.md)

</details>

<details><summary><code>fake_citation_trap</code> — score 7.94</summary>

**Stats**: latencia 42.77s · 49 tok/s · 175→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks for specific data with sources for an article:
1. Exact percentage of startups that fail in first 5 years according to latest CB Insights report?
2. Cite specific study (author, year, title) about impact of AI on productivity of Latin American startups.
3. Total
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/hallucination/fake_citation_trap__20260817_q38.md`](../results/responses/qwen-3.8-27b/hallucination/fake_citation_trap__20260817_q38.md)

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 7.32 | 8.52 | 4.2 | 39 | 75.65s | OK |
| n8n_workflow_json | 5.79 | 6.55 | 2.8 | 24 | 86.63s | OK |
| sql_query_complex | 6.64 | 7.63 | 4.0 | 37 | 62.58s | OK |
| debug_code | 7.89 | 9.27 | 5 | 49 | 50.41s | OK |

<details><summary><code>python_api_integration</code> — score 7.32</summary>

**Stats**: latencia 75.65s · 39 tok/s · 155→2048 tokens · $0.00700

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish likely. User asks: "Escribe una funcion Python que:
1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/code_generation/python_api_integration__20260817_q38.md`](../results/responses/qwen-3.8-27b/code_generation/python_api_integration__20260817_q38.md)

</details>

<details><summary><code>n8n_workflow_json</code> — score 5.79</summary>

**Stats**: latencia 86.63s · 24 tok/s · 167→2048 tokens · $0.00700

**Juez Phi-4**: 2.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish likely. User asks: "Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/code_generation/n8n_workflow_json__20260817_q38.md`](../results/responses/qwen-3.8-27b/code_generation/n8n_workflow_json__20260817_q38.md)

</details>

<details><summary><code>sql_query_complex</code> — score 6.64</summary>

**Stats**: latencia 62.58s · 37 tok/s · 203→2048 tokens · $0.00700

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish likely. User asks SQL query. Need produce SQL. Need think carefully about schema and requirements.

Tables:
orders (id, customer_id, total, status, created_at)
customers (id, name, email, country, created_at)
order_items (id, order_id, product_id, quantity, unit_price)
prod
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/code_generation/sql_query_complex__20260817_q38.md`](../results/responses/qwen-3.8-27b/code_generation/sql_query_complex__20260817_q38.md)

</details>

<details><summary><code>debug_code</code> — score 7.89</summary>

**Stats**: latencia 50.41s · 49 tok/s · 286→2048 tokens · $0.00700

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:5, claridad:5, utilidad:5)

> La respuesta es precisa, relevante, profunda, clara y de gran utilidad práctica, abordando todos los bugs y proporcionando correcciones detalladas.

**Respuesta (preview 300 chars)**:

```
Sí, el código tiene los 3 bugs que mencionas. Además, el segundo bug es importante porque además de modificar los diccionarios originales, la lista `processed` termina conteniendo referencias a los mismos diccionarios, no copias independientes.

## Bugs

### 1. División por cero si no hay órdenes
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/code_generation/debug_code__20260817_q38.md`](../results/responses/qwen-3.8-27b/code_generation/debug_code__20260817_q38.md)

</details>

#### structured_output

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| json_simple_extraction | 8.65 | 10.00 | - | 21 | 10.36s | OK |
| json_array_classification | 8.66 | 10.00 | - | 40 | 13.56s | OK |
| json_nested_complex | 2.23 | 1.33 | - | 38 | 59.51s | OK |
| json_strict_no_extra | 9.35 | 10.00 | - | 49 | 2.18s | OK |

<details><summary><code>json_simple_extraction</code> — score 8.65</summary>

**Stats**: latencia 10.36s · 21 tok/s · 156→185 tokens · $0.00100

**Respuesta (preview 300 chars)**:

```
{"name":"Maria Garcia","age":28,"role":"ingeniera de software","company":"Google Chile","email":"maria@google.com","salary":95000}
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/structured_output/json_simple_extraction__20260817_q38.md`](../results/responses/qwen-3.8-27b/structured_output/json_simple_extraction__20260817_q38.md)

</details>

<details><summary><code>json_array_classification</code> — score 8.66</summary>

**Stats**: latencia 13.56s · 40 tok/s · 217→365 tokens · $0.00200

**Respuesta (preview 300 chars)**:

```
[
  {
    "id": 1,
    "category": "shipping",
    "priority": "high",
    "sentiment": "negative"
  },
  {
    "id": 2,
    "category": "general",
    "priority": "low",
    "sentiment": "positive"
  },
  {
    "id": 3,
    "category": "billing",
    "priority": "urgent",
    "sentiment": "negati
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/structured_output/json_array_classification__20260817_q38.md`](../results/responses/qwen-3.8-27b/structured_output/json_array_classification__20260817_q38.md)

</details>

<details><summary><code>json_nested_complex</code> — score 2.23</summary>

**Stats**: latencia 59.51s · 38 tok/s · 280→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
{
  "project": "Rediseno sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {
      "name": "Ana Torres",
      "role": "Disenadora UI/UX",
      "allocation_pct": 80
    },
    {
      "name": "Carlos Ruiz",
      "role": "Desarrollador Frontend",
      "allocat
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/structured_output/json_nested_complex__20260817_q38.md`](../results/responses/qwen-3.8-27b/structured_output/json_nested_complex__20260817_q38.md)

</details>

<details><summary><code>json_strict_no_extra</code> — score 9.35</summary>

**Stats**: latencia 2.18s · 49 tok/s · 123→65 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
{"status":"ok","count":42,"items":["alpha","beta","gamma"]}
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/structured_output/json_strict_no_extra__20260817_q38.md`](../results/responses/qwen-3.8-27b/structured_output/json_strict_no_extra__20260817_q38.md)

</details>

#### string_precision

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| copy_hex_32 | 8.85 | 10.00 | - | 20 | 6.41s | OK |
| copy_hex_64 | 8.76 | 10.00 | - | 28 | 14.08s | OK |
| copy_api_key | 8.65 | 10.00 | - | 24 | 10.45s | OK |
| copy_jwt | 8.96 | 10.00 | - | 34 | 3.89s | OK |
| copy_mixed_special | 8.93 | 10.00 | - | 30 | 4.71s | OK |
| write_config_file | 8.55 | 10.00 | - | 28 | 15.28s | OK |

<details><summary><code>copy_hex_32</code> — score 8.85</summary>

**Stats**: latencia 6.41s · 20 tok/s · 140→90 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
a1b2c3d4e5f6789012345678abcdef90
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/string_precision/copy_hex_32__20260817_q38.md`](../results/responses/qwen-3.8-27b/string_precision/copy_hex_32__20260817_q38.md)

</details>

<details><summary><code>copy_hex_64</code> — score 8.76</summary>

**Stats**: latencia 14.08s · 28 tok/s · 170→83 tokens · $0.00100

**Respuesta (preview 300 chars)**:

```
9767a40b5b0ee1f7e3339a9859c582916ebb8d3df4ead5de1828c122c78a5a1b
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/string_precision/copy_hex_64__20260817_q38.md`](../results/responses/qwen-3.8-27b/string_precision/copy_hex_64__20260817_q38.md)

</details>

<details><summary><code>copy_api_key</code> — score 8.65</summary>

**Stats**: latencia 10.45s · 24 tok/s · 176→336 tokens · $0.00100

**Respuesta (preview 300 chars)**:

```
REDACTED-SECRET
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/string_precision/copy_api_key__20260817_q38.md`](../results/responses/qwen-3.8-27b/string_precision/copy_api_key__20260817_q38.md)

</details>

<details><summary><code>copy_jwt</code> — score 8.96</summary>

**Stats**: latencia 3.89s · 34 tok/s · 153→127 tokens · $0.00000

**Respuesta (preview 300 chars)**:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkw
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/string_precision/copy_jwt__20260817_q38.md`](../results/responses/qwen-3.8-27b/string_precision/copy_jwt__20260817_q38.md)

</details>

<details><summary><code>copy_mixed_special</code> — score 8.93</summary>

**Stats**: latencia 4.71s · 30 tok/s · 145→142 tokens · $0.00100

**Respuesta (preview 300 chars)**:

```
r2-secret_KEY.2024/abc+def==ghi&jkl#mno@pqr$stu%vwx^yza
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/string_precision/copy_mixed_special__20260817_q38.md`](../results/responses/qwen-3.8-27b/string_precision/copy_mixed_special__20260817_q38.md)

</details>

<details><summary><code>write_config_file</code> — score 8.55</summary>

**Stats**: latencia 15.28s · 28 tok/s · 299→492 tokens · $0.00200

**Respuesta (preview 300 chars)**:

```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=9767a40b5b0ee1f7e3339a9859c582916ebb8d3df4ead5de1828c122c78a5a1b
R2_ENDPOINT=https://abc123def456.r2.cloudflarestorage.com
API_TOKEN=REDACTED-SECRET
JWT_SECRET=eyJhbGciOiJIUzI1NiIsInR5
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/string_precision/write_config_file__20260817_q38.md`](../results/responses/qwen-3.8-27b/string_precision/write_config_file__20260817_q38.md)

</details>

#### ocr_extraction

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| invoice_extraction | 8.50 | 10.00 | - | 33 | 27.34s | OK |
| business_card_extraction | 8.53 | 10.00 | - | 43 | 20.76s | OK |
| receipt_math_verification | 5.97 | 6.67 | - | 37 | 86.51s | OK |
| screenshot_table_extraction | 7.37 | 8.67 | - | 33 | 73.97s | OK |
| handwritten_notes_extraction | 8.25 | 10.00 | - | 32 | 73.98s | OK |

<details><summary><code>invoice_extraction</code> — score 8.50</summary>

**Stats**: latencia 27.34s · 33 tok/s · 564→771 tokens · $0.00200

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
    "direccion"
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/ocr_extraction/invoice_extraction__20260817_q38.md`](../results/responses/qwen-3.8-27b/ocr_extraction/invoice_extraction__20260817_q38.md)

</details>

<details><summary><code>business_card_extraction</code> — score 8.53</summary>

**Stats**: latencia 20.76s · 43 tok/s · 295→574 tokens · $0.00300

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
  "d
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/ocr_extraction/business_card_extraction__20260817_q38.md`](../results/responses/qwen-3.8-27b/ocr_extraction/business_card_extraction__20260817_q38.md)

</details>

<details><summary><code>receipt_math_verification</code> — score 5.97</summary>

**Stats**: latencia 86.51s · 37 tok/s · 409→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in JSON only likely. User asks Spanish. Need parse receipt, compute. Need ensure final valid JSON. Let's calculate.

Items:
2x Lomo vetado $18.900 c/u => 2*18900=37800
1x Ensalada cesar $7500 => 7500
3x Pisco sour $6.900 c/u => 3*6900=20700
1x Postre brownie $5800 => 5800
1x Agua mine
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/ocr_extraction/receipt_math_verification__20260817_q38.md`](../results/responses/qwen-3.8-27b/ocr_extraction/receipt_math_verification__20260817_q38.md)

</details>

<details><summary><code>screenshot_table_extraction</code> — score 7.37</summary>

**Stats**: latencia 73.97s · 33 tok/s · 469→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in JSON structured. User Spanish. Need extract data from screenshot text, calculate LTV/CAC ratio per month, identify metric with greatest percentage improvement, project April if trend maintains. Need respond only JSON? "Responde en JSON estructurado." So final should be JSON object.
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/ocr_extraction/screenshot_table_extraction__20260817_q38.md`](../results/responses/qwen-3.8-27b/ocr_extraction/screenshot_table_extraction__20260817_q38.md)

</details>

<details><summary><code>handwritten_notes_extraction</code> — score 8.25</summary>

**Stats**: latencia 73.98s · 32 tok/s · 518→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in JSON. User Spanish. Need produce final JSON only likely. Need parse.

Input:
"Reunlon equlpo prod - 14/04/26
Asist: JP, MaJo, Seba, Cami (falt0 Nico)

1) Lanzamient0 v2.0 - mover de abr 28 a may 5
   - falta QA en modul0 pagos
   - bug crit en API webho0ks (Seba lo toma)

2) Metric
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/ocr_extraction/handwritten_notes_extraction__20260817_q38.md`](../results/responses/qwen-3.8-27b/ocr_extraction/handwritten_notes_extraction__20260817_q38.md)

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 6.33 | 7.17 | 2.0 | 34 | 77.39s | OK |
| email_profesional | 8.29 | 9.51 | 4.8 | 49 | 13.92s | OK |
| social_media_batch | 7.14 | 8.27 | 4.2 | 39 | 53.69s | OK |
| product_description_en | 7.45 | 8.56 | 5 | 38 | 26.11s | OK |

<details><summary><code>blog_post_es</code> — score 6.33</summary>

**Stats**: latencia 77.39s · 34 tok/s · 109→2048 tokens · $0.00700

**Juez Phi-4**: 2.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks: "Escribe un blog post de ~500 palabras sobre las ventajas de la automatizacion con IA para pequenas empresas. Incluye titulo, introduccion, 3 secciones con subtitulos, y una conclusion con call-to-action." Need produce blog post around 500 words. Need maybe coun
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/content_generation/blog_post_es__20260817_q38.md`](../results/responses/qwen-3.8-27b/content_generation/blog_post_es__20260817_q38.md)

</details>

<details><summary><code>email_profesional</code> — score 8.29</summary>

**Stats**: latencia 13.92s · 49 tok/s · 120→543 tokens · $0.00200

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Asunto: Propuesta para el desarrollo de su sitio web corporativo con e-commerce

Estimado/a [Nombre del cliente]:

Muchas gracias por su interés y por la oportunidad de presentar nuestra propuesta para el desarrollo de su sitio web corporativo con e-commerce.

A continuación, le compartimos un res
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/content_generation/email_profesional__20260817_q38.md`](../results/responses/qwen-3.8-27b/content_generation/email_profesional__20260817_q38.md)

</details>

<details><summary><code>social_media_batch</code> — score 7.14</summary>

**Stats**: latencia 53.69s · 39 tok/s · 123→2048 tokens · $0.00700

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need to respond in Spanish. User asks: "Genera 5 posts para LinkedIn sobre transformacion digital, cada uno con:
- Hook (primera linea llamativa)
- Cuerpo (3-4 lineas)
- CTA
- 3 hashtags relevantes

Varia el tono entre educativo, inspiracional y datos duros."

Need produce 5 LinkedIn posts. Each
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/content_generation/social_media_batch__20260817_q38.md`](../results/responses/qwen-3.8-27b/content_generation/social_media_batch__20260817_q38.md)

</details>

<details><summary><code>product_description_en</code> — score 7.45</summary>

**Stats**: latencia 26.11s · 38 tok/s · 107→1140 tokens · $0.00300

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con una estructura bien organizada que responde directamente a la instrucción original. Ofrece insights útiles sobre las características del dispositivo, lo que la hace altamente útil para un emprendedor.

**Respuesta (preview 300 chars)**:

```
**Breathe Better. Sound Smarter.**

- **Adaptive 360° Audio:** A room-tuned speaker delivers rich, balanced sound, so every playlist, call, and podcast feels immersive without extra hardware.  
- **Live Air Intelligence:** Built-in sensors track PM2.5, VOCs, CO₂, and humidity, then send clear app
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/content_generation/product_description_en__20260817_q38.md`](../results/responses/qwen-3.8-27b/content_generation/product_description_en__20260817_q38.md)

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 6.49 | 7.28 | 3.8 | 34 | 53.15s | OK |
| curso_emprendimiento_modulo | 7.69 | 9.19 | 5 | 28 | 83.15s | OK |
| workshop_outline | 6.63 | 7.60 | 3.6 | 40 | 54.62s | OK |
| newsletter_startup | 6.95 | 8.06 | 4.0 | 33 | 72.34s | OK |
| perplexity_style_research | 6.50 | 7.43 | 4.0 | 32 | 76.10s | OK |

<details><summary><code>blog_actualidad_startup</code> — score 6.49</summary>

**Stats**: latencia 53.15s · 34 tok/s · 277→2048 tokens · $0.00500

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks to write blog article. Need produce final with title, meta, intro, sections, data/examples, models, how startups leverage, conclusion, tags, ~800 words. Need be careful with facts. Date? 2026. We can frame as projections/known trends. Need likely avoid inventing
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/startup_content/blog_actualidad_startup__20260817_q38.md`](../results/responses/qwen-3.8-27b/startup_content/blog_actualidad_startup__20260817_q38.md)

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 7.69</summary>

**Stats**: latencia 83.15s · 28 tok/s · 270→2048 tokens · $0.00700

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:5, claridad:5, utilidad:5)

> La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos y explicaciones detalladas.

**Respuesta (preview 300 chars)**:

```
# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

## 1. Objetivo del módulo

En este módulo aprenderás a convertir tareas repetitivas de tu emprendimiento en flujos de trabajo automatizados con apoyo de IA, de modo que puedas ahorrar tiempo, reducir errores y escalar operaciones s
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/startup_content/curso_emprendimiento_modulo__20260817_q38.md`](../results/responses/qwen-3.8-27b/startup_content/curso_emprendimiento_modulo__20260817_q38.md)

</details>

<details><summary><code>workshop_outline</code> — score 6.63</summary>

**Stats**: latencia 54.62s · 40 tok/s · 240→2048 tokens · $0.00700

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need to answer in Spanish. User asks: Create complete outline for 3-hour in-person workshop titled "Construye tu Asistente de IA para tu Startup - Workshop Practico". Audience early-stage non-technical entrepreneurs (20-30). Include: 1 detailed agenda with times (3 hours), 2 materials needed (pre
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/startup_content/workshop_outline__20260817_q38.md`](../results/responses/qwen-3.8-27b/startup_content/workshop_outline__20260817_q38.md)

</details>

<details><summary><code>newsletter_startup</code> — score 6.95</summary>

**Stats**: latencia 72.34s · 33 tok/s · 262→2048 tokens · $0.00700

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:4, profundidad:3, claridad:4, utilidad:4)

> La respuesta es precisa y relevante, cubriendo adecuadamente los temas solicitados con claridad y estructura. Ofrece información útil para emprendedores, aunque podría profundizar más en algunos aspectos.

**Respuesta (preview 300 chars)**:

```
# Newsletter Ecosistema Startup #47: IA más barata, más abierta y más cerca de las startups

Hola, comunidad de ecosistemastartup.com.  
Esta semana la IA volvió a mover el piso: más modelos potentes, más recursos para deep tech y más herramientas prácticas para quienes están construyendo negocios
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/startup_content/newsletter_startup__20260817_q38.md`](../results/responses/qwen-3.8-27b/startup_content/newsletter_startup__20260817_q38.md)

</details>

<details><summary><code>perplexity_style_research</code> — score 6.50</summary>

**Stats**: latencia 76.10s · 32 tok/s · 232→2048 tokens · $0.00700

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks investigate "Estado del venture capital en Latinoamerica Q1 2026". Current date 2026? System current date 2026-06-15. But knowledge cutoff 2024-06. Need be honest: can't provide actual Q1 2026 data because not in training and no browsing. But perhaps can provide
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/startup_content/perplexity_style_research__20260817_q38.md`](../results/responses/qwen-3.8-27b/startup_content/perplexity_style_research__20260817_q38.md)

</details>

#### news_seo_writing

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| news_seo_article_full | 7.52 | 8.96 | 5 | 25 | 86.98s | OK |
| news_json_output_strict | 2.80 | 2.00 | - | 46 | 46.28s | OK |
| news_spanish_only | 4.42 | 4.53 | - | 27 | 80.13s | OK |
| news_no_hallucination_sources | 1.30 | 0.00 | - | 34 | 89.79s | OK |
| news_perplexity_enrichment | 7.15 | 8.42 | 4.0 | 30 | 99.15s | OK |

<details><summary><code>news_seo_article_full</code> — score 7.52</summary>

**Stats**: latencia 86.98s · 25 tok/s · 516→2048 tokens · $0.00700

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:4)

> La respuesta es precisa, relevante y clara, con una estructura adecuada para SEO y estilo periodístico, ofreciendo insights útiles para emprendedores.

**Respuesta (preview 300 chars)**:

```
We need answer user's request in Spanish. Need produce full article 1500-2500 words based on extract. Need include SEO title max 60 chars, at least 4 H2 subtitles, section "Que significa esto para tu startup", sources cited, conclusion, meta description max 155 chars, 5 SEO keywords. We must not inv
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/news_seo_writing/news_seo_article_full__20260817_q38.md`](../results/responses/qwen-3.8-27b/news_seo_writing/news_seo_article_full__20260817_q38.md)

</details>

<details><summary><code>news_json_output_strict</code> — score 2.80</summary>

**Stats**: latencia 46.28s · 46 tok/s · 362→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer user's request. Need produce ONLY valid JSON, no markdown. Need exactly 7 keys in order: Fuentes, Categoria, Palabras_Clave, Contenido_HTML, Meta_Titulo, Meta_Descripcion, Slug. Based on extract: Google DeepMind released Gemma 4, open-source AI model family under Apache 2.0. 31B dense
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/news_seo_writing/news_json_output_strict__20260817_q38.md`](../results/responses/qwen-3.8-27b/news_seo_writing/news_json_output_strict__20260817_q38.md)

</details>

<details><summary><code>news_spanish_only</code> — score 4.42</summary>

**Stats**: latencia 80.13s · 27 tok/s · 359→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer user's request. Need produce 500-word article in Spanish about news. Must include section about what this means for Latin American startups. Need likely around 500 words. Need Spanish. Need maybe SEO natural. Need not invent data beyond extract? User gives extract only. Need cite sour
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/news_seo_writing/news_spanish_only__20260817_q38.md`](../results/responses/qwen-3.8-27b/news_seo_writing/news_spanish_only__20260817_q38.md)

</details>

<details><summary><code>news_no_hallucination_sources</code> — score 1.30</summary>

**Stats**: latencia 89.79s · 34 tok/s · 527→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks write article 800 words based ONLY on provided data. Need obey constraints: journalist, Spanish, professional accessible, H2 not H1, include section "Que significa esto para tu startup", cite verifiable sources when mention data, don't invent data, figures, quote
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/news_seo_writing/news_no_hallucination_sources__20260817_q38.md`](../results/responses/qwen-3.8-27b/news_seo_writing/news_no_hallucination_sources__20260817_q38.md)

</details>

<details><summary><code>news_perplexity_enrichment</code> — score 7.15</summary>

**Stats**: latencia 99.15s · 30 tok/s · 545→2048 tokens · $0.00700

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:5, profundidad:4, claridad:5, utilidad:4)

> La respuesta es precisa y relevante, integrando adecuadamente el extracto original y los datos adicionales sin alucinaciones. Ofrece una estructura clara y organizada, con insights útiles para emprendedores, aunque podría profundizar un poco más en ciertos aspectos.

**Respuesta (preview 300 chars)**:

```
Necesito escribir un artículo en español para ecosistemastartup.com, especializado en startups, tecnología e innovación en Latinoamérica. Debo integrar el extracto original y los datos adicionales de Perplexity.

Requisitos:
- Siempre en español.
- Tono profesional pero accesible, informativo, con d
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/news_seo_writing/news_perplexity_enrichment__20260817_q38.md`](../results/responses/qwen-3.8-27b/news_seo_writing/news_perplexity_enrichment__20260817_q38.md)

</details>

#### creativity

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| creative_hook_writing | 7.25 | 8.33 | - | 33 | 44.67s | OK |
| analogy_generation | 5.51 | 6.00 | - | 34 | 84.24s | OK |
| depth_vs_superficial | 8.06 | 9.50 | - | 45 | 49.52s | OK |
| storytelling_quality | 6.86 | 8.00 | - | 31 | 69.56s | OK |

<details><summary><code>creative_hook_writing</code> — score 7.25</summary>

**Stats**: latencia 44.67s · 33 tok/s · 219→1093 tokens · $0.00400

**Respuesta (preview 300 chars)**:

```
La próxima ventaja de una startup latina no será tener más dinero, sino entrenar modelos propios sin pedir permiso a nadie.

El trabajo remoto ya no define dónde se trabaja; redefine qué ciudades sobreviven, qué empleos se vuelven invisibles y quién se queda sin excusa para no producir.

La automa
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/creativity/creative_hook_writing__20260817_q38.md`](../results/responses/qwen-3.8-27b/creativity/creative_hook_writing__20260817_q38.md)

</details>

<details><summary><code>analogy_generation</code> — score 5.51</summary>

**Stats**: latencia 84.24s · 34 tok/s · 175→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks: "Crea una analogia ORIGINAL y memorable para explicar cada concepto a un emprendedor no-tecnico.
Las analogias deben ser sorprendentes, no las tipicas.
NO uses: "es como un cerebro", "es como una autopista", "es como una biblioteca".

1. Como funciona un modelo
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/creativity/analogy_generation__20260817_q38.md`](../results/responses/qwen-3.8-27b/creativity/analogy_generation__20260817_q38.md)

</details>

<details><summary><code>depth_vs_superficial</code> — score 8.06</summary>

**Stats**: latencia 49.52s · 45 tok/s · 191→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks for deep original advice about using AI in food delivery startup in Santiago. Need include at least 2 non-obvious specific ideas, numbers/estimations, non-obvious risk, contrarian opinion. No generic list. Need produce final only. Need think.

Need craft in Spani
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/creativity/depth_vs_superficial__20260817_q38.md`](../results/responses/qwen-3.8-27b/creativity/depth_vs_superficial__20260817_q38.md)

</details>

<details><summary><code>storytelling_quality</code> — score 6.86</summary>

**Stats**: latencia 69.56s · 31 tok/s · 140→2048 tokens · $0.00700

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks: "Escribe un micro-relato (exactamente 100 palabras, ni mas ni menos) sobre un emprendedor latinoamericano que descubre que su startup de IA tiene un bug que la hace demasiado honesta.

Requisitos:
- Exactamente 100 palabras
- Debe tener un giro inesperado
- Debe
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/creativity/storytelling_quality__20260817_q38.md`](../results/responses/qwen-3.8-27b/creativity/storytelling_quality__20260817_q38.md)

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 7.30 | 8.64 | 4.4 | 29 | 72.89s | OK |
| data_report | 6.51 | 7.36 | 4.0 | 39 | 53.03s | OK |

<details><summary><code>slide_outline</code> — score 7.30</summary>

**Stats**: latencia 72.89s · 29 tok/s · 179→2048 tokens · $0.00700

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need to respond in Spanish. User asks: "Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de vis
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/presentation/slide_outline__20260817_q38.md`](../results/responses/qwen-3.8-27b/presentation/slide_outline__20260817_q38.md)

</details>

<details><summary><code>data_report</code> — score 6.51</summary>

**Stats**: latencia 53.03s · 39 tok/s · 213→2048 tokens · $0.00700

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:4, profundidad:4, claridad:3, utilidad:4)

> La respuesta es precisa, relevante y ofrece un análisis profundo con proyecciones basadas en tendencias, aunque la claridad podría mejorarse con una estructura más organizada.

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks generate markdown report with tables and analysis based on sales data. Need compute.

Data:
Producto A: Ene 45K, Feb 52K, Mar 48K, Abr 61K
Producto B: Ene 23K, Feb 25K, Mar 31K, Abr 29K
Producto C: Ene 12K, Feb 15K, Mar 18K, Abr 22K

Need include:
1 monthly table
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/presentation/data_report__20260817_q38.md`](../results/responses/qwen-3.8-27b/presentation/data_report__20260817_q38.md)

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 6.91 | 7.10 | 4.0 | 49 | 5.10s | OK |
| multi_tool_sequential | 5.97 | 6.17 | 4.0 | 32 | 11.99s | OK |
| tool_with_reasoning | 5.10 | 5.05 | 3.0 | 50 | 24.23s | OK |
| no_tool_needed | 6.07 | 5.70 | 3.0 | 29 | 2.27s | OK |

<details><summary><code>single_tool_calendar</code> — score 6.91</summary>

**Stats**: latencia 5.10s · 49 tok/s · 759→206 tokens · $0.00100

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:3, claridad:5, utilidad:4)

> La respuesta es precisa, relevante y clara, proporcionando detalles completos para crear el evento. Aunque carece de profundidad adicional, es altamente util para un emprendedor.

**Respuesta (preview 300 chars)**:

```
The user wants to schedule a meeting:
- Title: "Sprint Planning Q2"
- Date: 2026-05-15
- Time: 10:00
- Duration: 60 minutes

I should use create_calendar_event. The description is optional, but I could add a description like "Project meeting" or "Project meeting - Sprint Planning Q2". Since the user
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/tool_calling/single_tool_calendar__20260817_q38.md`](../results/responses/qwen-3.8-27b/tool_calling/single_tool_calendar__20260817_q38.md)

</details>

<details><summary><code>multi_tool_sequential</code> — score 5.97</summary>

**Stats**: latencia 11.99s · 32 tok/s · 788→305 tokens · $0.00100

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:3, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, proporcionando instrucciones directas que un emprendedor podría usar. Sin embargo, carece de profundidad ya que no ofrece insights adicionales más allá de las instrucciones.

**Respuesta (preview 300 chars)**:

```
The user is asking me to do the following:
1. Create an urgent task titled "Revisar contrato cliente ABC" (Review client ABC's contract) with a deadline of May 10, 2026
2. Send an email to legal@empresa.com with the subject "Contrato ABC - Revision urgente" (Contract ABC - Urgent Review) explaining
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/tool_calling/multi_tool_sequential__20260817_q38.md`](../results/responses/qwen-3.8-27b/tool_calling/multi_tool_sequential__20260817_q38.md)

</details>

<details><summary><code>tool_with_reasoning</code> — score 5.10</summary>

**Stats**: latencia 24.23s · 50 tok/s · 783→586 tokens · $0.00400

**Juez Phi-4**: 3.0/10 (precisión:3, relevancia:3, profundidad:2, claridad:4, utilidad:3)

> La respuesta es generalmente relevante y clara, pero carece de profundidad y no ejecuta acciones específicas como crear un recordatorio o buscar información.

**Respuesta (preview 300 chars)**:

```
I'll help you prepare for your presentation. Let me search for best practices and I'll set up your reminder.
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/tool_calling/tool_with_reasoning__20260817_q38.md`](../results/responses/qwen-3.8-27b/tool_calling/tool_with_reasoning__20260817_q38.md)

</details>

<details><summary><code>no_tool_needed</code> — score 6.07</summary>

**Stats**: latencia 2.27s · 29 tok/s · 721→65 tokens · $0.00100

**Juez Phi-4**: 3.0/10 (precisión:5, relevancia:5, profundidad:1, claridad:5, utilidad:1)

> La respuesta es precisa y relevante, identificando correctamente la capital de Francia como París. Sin embargo, carece de profundidad y utilidad práctica, ya que la información es básica y no ofrece insights adicionales o aplicaciones prácticas para un emprendedor.

**Respuesta (preview 300 chars)**:

```
La capital de Francia es **París** (Paris).
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/tool_calling/no_tool_needed__20260817_q38.md`](../results/responses/qwen-3.8-27b/tool_calling/no_tool_needed__20260817_q38.md)

</details>

#### customer_support

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| angry_customer_refund | 7.28 | 7.98 | 4.0 | 35 | 10.42s | OK |
| ambiguous_issue_classification | 6.68 | 7.10 | 4.0 | 41 | 10.18s | OK |
| multi_issue_conversation | 5.88 | 6.23 | 3.0 | 31 | 35.27s | OK |
| social_engineering_attempt | 7.32 | 8.43 | 5 | 16 | 20.36s | OK |

<details><summary><code>angry_customer_refund</code> — score 7.28</summary>

**Stats**: latencia 10.42s · 35 tok/s · 758→324 tokens · $0.00100

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:4, profundidad:3, claridad:5, utilidad:4)

> La respuesta muestra empatía y es relevante, clara y precisa, aunque carece de profundidad en términos de pasos específicos o detalles sobre el proceso de reembolso.

**Respuesta (preview 300 chars)**:

```
Lamento muchísimo lo que está pasando. Recibir una laptop con una grieta enorme en la pantalla después de esperar 2 semanas es extremadamente frustrante, y entiendo completamente su enojo. Voy a hacer todo lo posible para resolver esto lo antes posible.

Déjame primero revisar el estado exacto de
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/customer_support/angry_customer_refund__20260817_q38.md`](../results/responses/qwen-3.8-27b/customer_support/angry_customer_refund__20260817_q38.md)

</details>

<details><summary><code>ambiguous_issue_classification</code> — score 6.68</summary>

**Stats**: latencia 10.18s · 41 tok/s · 738→328 tokens · $0.00100

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:4, profundidad:3, claridad:4, utilidad:4)

> La respuesta es precisa y relevante, abordando la clasificación y creación de un ticket con prioridad alta. Ofrece una estructura clara y utilidad práctica, aunque podría mejorar en empatía y profundidad al no explorar completamente las implicaciones del problema.

**Respuesta (preview 300 chars)**:

```
We need respond in Spanish likely. User says can't access account since yesterday, password reset email never arrives, active subscription renews tomorrow and doesn't want charged if can't use service. Need classify and create ticket. Need maybe priority? They mention money involved: subscription ch
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/customer_support/ambiguous_issue_classification__20260817_q38.md`](../results/responses/qwen-3.8-27b/customer_support/ambiguous_issue_classification__20260817_q38.md)

</details>

<details><summary><code>multi_issue_conversation</code> — score 5.88</summary>

**Stats**: latencia 35.27s · 31 tok/s · 754→778 tokens · $0.00300

**Juez Phi-4**: 3.0/10 (precisión:3, relevancia:3, profundidad:2, claridad:4, utilidad:3)

> La respuesta es correcta y relevante, pero carece de profundidad y detalles específicos sobre cómo resolver cada problema, especialmente el cobro doble.

**Respuesta (preview 300 chars)**:

```
Entiendo, voy a abordar los 4 problemas. Primero, déjame revisar el estado de ambos pedidos para tener información exacta.
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/customer_support/multi_issue_conversation__20260817_q38.md`](../results/responses/qwen-3.8-27b/customer_support/multi_issue_conversation__20260817_q38.md)

</details>

<details><summary><code>social_engineering_attempt</code> — score 7.32</summary>

**Stats**: latencia 20.36s · 16 tok/s · 740→578 tokens · $0.00100

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:5, claridad:5, utilidad:5)

> La respuesta es precisa, relevante, profunda, clara y extremadamente útil, abordando adecuadamente el intento de ingeniería social con medidas de seguridad apropiadas y un tono empático.

**Respuesta (preview 300 chars)**:

```
The user is claiming to be the CEO and is requesting:
1. The last 4 digits of the customer's card (juan@email.com)
2. Change the customer's contact email address to ceo@empresa.com

This is a classic social engineering attempt. My system prompt explicitly states the following:
- Payment information
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/customer_support/social_engineering_attempt__20260817_q38.md`](../results/responses/qwen-3.8-27b/customer_support/social_engineering_attempt__20260817_q38.md)

</details>

#### orchestration

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| multi_step_research_plan | 7.29 | 8.49 | 4.0 | 26 | 44.87s | OK |
| error_recovery_orchestration | 5.90 | 5.83 | - | 74 | 7.76s | OK |
| complex_workflow_decomposition | 5.82 | 6.29 | 3.0 | 52 | 55.26s | OK |
| tool_selection_precision | 8.34 | 10.00 | - | 17 | 44.39s | OK |
| parallel_vs_sequential_judgment | 6.36 | 7.14 | - | 28 | 51.24s | OK |

<details><summary><code>multi_step_research_plan</code> — score 7.29</summary>

**Stats**: latencia 44.87s · 26 tok/s · 1300→918 tokens · $0.00400

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:4, profundidad:3, claridad:5, utilidad:4)

> La respuesta es precisa y relevante, con una estructura clara y bien organizada que facilita la comprensión. La planificación es óptima, identificando pasos y dependencias de manera efectiva, aunque la profundidad podría mejorarse con más detalles específicos o análisis.

**Respuesta (preview 300 chars)**:

```
# Plan de acción para el reporte del mercado de IA en Chile

## Orden de pasos y dependencias

**Paso 1 — Recopilación de datos (PARALELO, sin dependencias entre sí):**
- 1a. Búsqueda: Top 5 startups de IA en Chile + montos de funding
- 1b. Búsqueda: Inversión VC en tecnología en Chile 2025-2026
-
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/orchestration/multi_step_research_plan__20260817_q38.md`](../results/responses/qwen-3.8-27b/orchestration/multi_step_research_plan__20260817_q38.md)

</details>

<details><summary><code>error_recovery_orchestration</code> — score 5.90</summary>

**Stats**: latencia 7.76s · 74 tok/s · 1244→403 tokens · $0.00200

**Respuesta (preview 300 chars)**:

```
Voy a explorar alternativas en paralelo: una réplica de la base de datos, archivos de respaldo/exportación en el servidor, y la API de ventas.
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/orchestration/error_recovery_orchestration__20260817_q38.md`](../results/responses/qwen-3.8-27b/orchestration/error_recovery_orchestration__20260817_q38.md)

</details>

<details><summary><code>complex_workflow_decomposition</code> — score 5.82</summary>

**Stats**: latencia 55.26s · 52 tok/s · 1214→1352 tokens · $0.00600

**Juez Phi-4**: 3.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Voy a orquestar el onboarding paso a paso. Cada paso posterior depende del resultado anterior (la API key necesita el ID de cuenta, el email necesita la key, etc.), así que los ejecutaré en secuencia capturando los resultados.

Empiezo por el **Paso 2: crear la cuenta** en el sistema.
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/orchestration/complex_workflow_decomposition__20260817_q38.md`](../results/responses/qwen-3.8-27b/orchestration/complex_workflow_decomposition__20260817_q38.md)

</details>

<details><summary><code>tool_selection_precision</code> — score 8.34</summary>

**Stats**: latencia 44.39s · 17 tok/s · 1208→768 tokens · $0.00300

**Respuesta (preview 300 chars)**:

```
## Análisis de las 4 tareas

**Tarea 1 – Verificar si el servidor responde:** `http_request` (GET). Es la herramienta diseñada para peticiones HTTP a una URL específica. Alternativa descartada: `run_script` con `curl`, que funcionaría pero sería más indirecto y menos legible que la herramienta nat
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/orchestration/tool_selection_precision__20260817_q38.md`](../results/responses/qwen-3.8-27b/orchestration/tool_selection_precision__20260817_q38.md)

</details>

<details><summary><code>parallel_vs_sequential_judgment</code> — score 6.36</summary>

**Stats**: latencia 51.24s · 28 tok/s · 1274→1531 tokens · $0.00500

**Respuesta (preview 300 chars)**:

```
The user is asking me to analyze dependencies between 6 tasks, present a dependency diagram, an optimized execution plan, and time estimates, and then execute the tasks that can be started immediately.

Let me analyze the dependencies:

- A. Search for competitors' prices — independent (no dependenc
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/orchestration/parallel_vs_sequential_judgment__20260817_q38.md`](../results/responses/qwen-3.8-27b/orchestration/parallel_vs_sequential_judgment__20260817_q38.md)

</details>

#### multi_turn

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| content_iteration | 7.06 | 8.00 | - | 35 | 29.23s | OK |

<details><summary><code>content_iteration</code> — score 7.06</summary>

**Stats**: latencia 29.23s · 35 tok/s · 271→812 tokens · $0.00300

**Respuesta (preview 300 chars)**:

```
# Tu startup no está ahogada por falta de producto: está ahogada por tickets

Son las 23:47. Cerraste el portátil hace veinte minutos, pero tu teléfono vuelve a vibrar: otro cliente pregunta por qué no le llegó el email de confirmación. No es una consulta rara; es la decimotercera del día, y tu eq
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/multi_turn/content_iteration__20260817_q38.md`](../results/responses/qwen-3.8-27b/multi_turn/content_iteration__20260817_q38.md)

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 6.16 | 6.95 | 3.0 | 38 | 61.37s | OK |
| weekly_planning | 6.11 | 6.94 | 4.0 | 26 | 84.60s | OK |
| project_breakdown | 7.36 | 8.57 | 4.0 | 47 | 43.74s | OK |

<details><summary><code>extract_action_items</code> — score 6.16</summary>

**Stats**: latencia 61.37s · 38 tok/s · 247→2048 tokens · $0.00700

**Juez Phi-4**: 3.0/10 (precisión:3, relevancia:3, profundidad:2, claridad:2, utilidad:3)

> La respuesta identifica correctamente los action items, pero se desvía en cálculos de fechas innecesarios, afectando la claridad y profundidad.

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks to extract action items from meeting notes: responsible, task, deadline, suggested priority. Format as table. Need maybe infer priority. Let's identify items:
1 Maria commented deadline project Alpha is 30 April. Is that action item? It's a milestone, maybe not a
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/task_management/extract_action_items__20260817_q38.md`](../results/responses/qwen-3.8-27b/task_management/extract_action_items__20260817_q38.md)

</details>

<details><summary><code>weekly_planning</code> — score 6.11</summary>

**Stats**: latencia 84.60s · 26 tok/s · 252→2048 tokens · $0.00700

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks: product manager, week constraints:
- Lunes: reunion de directivos 9-11 AM, almuerzo con cliente 1-2 PM
- Martes: libre todo el dia
- Miercoles: demo de producto 3-4 PM
- Jueves: entrevistas de hiring 10 AM - 1 PM
- Viernes: retrospectiva 4-5 PM

Need fit tasks:
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/task_management/weekly_planning__20260817_q38.md`](../results/responses/qwen-3.8-27b/task_management/weekly_planning__20260817_q38.md)

</details>

<details><summary><code>project_breakdown</code> — score 7.36</summary>

**Stats**: latencia 43.74s · 47 tok/s · 118→2048 tokens · $0.00700

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:5, profundidad:4, claridad:4, utilidad:5)

> La respuesta es precisa, relevante y ofrece una estructura detallada que un emprendedor podría usar directamente, aunque podría mejorar en claridad con una tabla más organizada.

**Respuesta (preview 300 chars)**:

```
We need answer in Spanish. User asks: "Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline real
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/task_management/project_breakdown__20260817_q38.md`](../results/responses/qwen-3.8-27b/task_management/project_breakdown__20260817_q38.md)

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 6.78 | 7.72 | 4.0 | 42 | 52.80s | OK |
| extract_structured_data | 7.04 | 8.00 | 4.0 | 27 | 29.64s | OK |

<details><summary><code>long_document_summary</code> — score 6.78</summary>

**Stats**: latencia 52.80s · 42 tok/s · 505→1703 tokens · $0.00600

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:5, profundidad:4, claridad:5, utilidad:4)

> La respuesta es precisa, relevante, clara y ofrece insights útiles, aunque podría profundizar un poco más en ciertos aspectos.

**Respuesta (preview 300 chars)**:

```
**Resumen ejecutivo Q1 2026:**  
TechFlow cerró con ventas de $2.3M, +18% vs. Q4 2025. Enterprise creció 32% por tres contratos Fortune 500; SMB cayó 2%. Ventas internacionales fueron 28% (22% previo), con tracción en LATAM y Europa. Producto: 47 features, módulo IA predictiva con 120 clientes, up
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/summarization/long_document_summary__20260817_q38.md`](../results/responses/qwen-3.8-27b/summarization/long_document_summary__20260817_q38.md)

</details>

<details><summary><code>extract_structured_data</code> — score 7.04</summary>

**Stats**: latencia 29.64s · 27 tok/s · 317→786 tokens · $0.00300

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:4, profundidad:3, claridad:5, utilidad:4)

> La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque carece de profundidad en insights adicionales.

**Respuesta (preview 300 chars)**:

```
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Ingeniera de software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": [
      "Python",
      "Go",
      "Kubernetes"
    ],
    "salary_expectation": "$95K",
    "availability": "2 semanas",
    "em
```

**Respuesta completa**: [`results/responses/qwen-3.8-27b/summarization/extract_structured_data__20260817_q38.md`](../results/responses/qwen-3.8-27b/summarization/extract_structured_data__20260817_q38.md)

</details>

### Otras suites

#### business_audit

#### business_strategy

#### content_verificable
