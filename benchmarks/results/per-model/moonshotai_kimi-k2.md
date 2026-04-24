# Kimi K2

- **model_id**: `moonshotai/kimi-k2`
- **Total tests**: 74/91 exitosos (17 errores)
- **Score final**: 7.05
- **Calidad**: 7.86
- **Judge score (Phi-4)**: 4.12/10
- **Velocidad**: 28 tok/s
- **Latencia primera token**: 20.02s
- **Costo promedio por test**: $0.00214

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| agent_capabilities | 5 | 2 | 6.13 | 6.31 |
| code_generation | 4 | 4 | 7.10 | 8.28 |
| content_generation | 4 | 4 | 7.13 | 8.40 |
| creativity | 4 | 4 | 7.12 | 8.39 |
| customer_support | 4 | 4 | 7.44 | 7.63 |
| deep_reasoning | 6 | 6 | 6.70 | 7.32 |
| hallucination | 3 | 2 | 7.31 | 8.04 |
| multi_turn | 4 | 2 | 6.99 | 7.68 |
| news_seo_writing | 5 | 5 | 6.68 | 7.43 |
| ocr_extraction | 5 | 4 | 6.70 | 6.75 |
| orchestration | 5 | 1 | 7.01 | 8.59 |
| policy_adherence | 4 | 1 | 7.17 | 7.76 |
| presentation | 2 | 1 | 7.32 | 8.92 |
| reasoning | 3 | 3 | 7.45 | 9.28 |
| sales_outreach | 3 | 3 | 7.29 | 8.59 |
| startup_content | 5 | 4 | 7.22 | 9.20 |
| strategy | 3 | 3 | 6.94 | 8.29 |
| string_precision | 6 | 6 | 7.21 | 7.65 |
| structured_output | 4 | 4 | 7.22 | 7.95 |
| summarization | 2 | 2 | 6.62 | 6.91 |
| task_management | 3 | 3 | 7.20 | 8.62 |
| tool_calling | 4 | 3 | 6.91 | 5.28 |
| translation | 3 | 3 | 7.37 | 8.39 |

## Detalle por test

### Razonamiento y Estrategia

#### deep_reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| math_word_problem | 6.77 | 7.34 | 3.8 | 31 | 11.27s | OK |
| logic_puzzle_constraint | 6.79 | 8.26 | 4.4 | 35 | 58.51s | OK |
| causal_reasoning | 7.18 | 8.51 | 4.4 | 30 | 32.28s | OK |
| code_bug_subtle | 5.43 | 3.81 | 1.6 | 22 | 12.66s | OK |
| fermi_estimation | 6.72 | 7.20 | 4.4 | 32 | 30.11s | OK |
| ethical_dilemma_structured | 7.29 | 8.82 | 4.8 | 32 | 38.13s | OK |

<details><summary><code>math_word_problem</code> — score 6.77</summary>

**Stats**: latencia 11.27s · 31 tok/s · 124→351 tokens · $0.00118

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
¡Perfecto! Vamos a resolverlo paso a paso.

---

### **Datos que tenemos:**

- **Distancia entre Santiago y Valparaíso:** 120 km  
- **Tren 1 (Santiago → Valparaíso):**
  - Sale a las **8:00 AM**
  - Velocidad: **80 km/h**
- **Tren 2 (Valparaíso → Santiago):**
  - Sale a las **8:30 AM**
  - Velocida
```

</details>

<details><summary><code>logic_puzzle_constraint</code> — score 6.79</summary>

**Stats**: latencia 58.51s · 35 tok/s · 141→2048 tokens · $0.00628

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Vamos a resolver este problema paso a paso, considerando todas las condiciones y probando cada posibilidad lógicamente.

Tenemos 4 casas en una calle, cada una de un color diferente: **roja, azul, verde, blanca**.

Las condiciones son:

1. La casa **roja** está a la **izquierda** de la **azul** (no
```

</details>

<details><summary><code>causal_reasoning</code> — score 7.18</summary>

**Stats**: latencia 32.28s · 30 tok/s · 230→972 tokens · $0.00315

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
### 1. Datos en tabla  
| Mes | Pedidos | Quejas | T promedio (min) | Días lluvia |  
|-----|---------|--------|------------------|-------------|  
| 1   | 1 000   | 50     | 35               | 5           |  
| 2   | 1 200   | 90     | 42               | 12          |  
| 3   | 1 100   | 110    | 3
```

</details>

<details><summary><code>code_bug_subtle</code> — score 5.43</summary>

**Stats**: latencia 12.66s · 22 tok/s · 248→276 tokens · $0.00108

**Juez Phi-4**: 1.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
El **bug** está en esta línea:

```python
return sum(filtered) / len(filtered)
```

### ¿Cuándo falla?
**Falla cuando *todos* los valores del conjunto original son outliers**, es decir, cuando después de filtrar queda la lista `filtered` vacía.

En ese caso `len(filtered)` es 0 y la división `sum(fi
```

</details>

<details><summary><code>fermi_estimation</code> — score 6.72</summary>

**Stats**: latencia 30.11s · 32 tok/s · 101→961 tokens · $0.00298

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Estimación del consumo diario de café en oficinas de Santiago de Chile
--------------------------------------------------------
1. Supuestos clave (numerados para claridad)

1. Población ocupada en oficinas en la Región Metropolitana (RM) ≈ 1,3 millones de personas.  
   Fuente: extrapolación de la
```

</details>

<details><summary><code>ethical_dilemma_structured</code> — score 7.29</summary>

**Stats**: latencia 38.13s · 32 tok/s · 235→1233 tokens · $0.00393

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Análisis de Decisión Ética para Lanzamiento de IA Médica

### 1. STAKEHOLDERS IDENTIFICADOS

**Primarios:**
- Pacientes con cáncer no diagnosticados (víctimas potenciales)
- Pacientes falsos positivos (daño psicológico/procedimientos innecesarios)
- Médicos que usarán la herramienta
- La startup
```

</details>

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 7.50 | 9.44 | 4.6 | 33 | 29.12s | OK |
| logical_reasoning | 7.34 | 8.96 | 4.4 | 36 | 19.78s | OK |
| multi_constraint_decision | 7.50 | 9.44 | 4.6 | 33 | 36.11s | OK |

<details><summary><code>business_analysis</code> — score 7.50</summary>

**Stats**: latencia 29.12s · 33 tok/s · 203→948 tokens · $0.00305

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## 📊 ANÁLISIS DE TU SAAS - Q1 2024

### 1. MÉTRICAS CLAVE CALCULADAS

| Métrica | Enero | Febrero | Marzo |
|---------|--------|---------|---------|
| **Churn Rate Mensual** | 3.75% | 3.85% | 4.59% |
| **Growth Rate Mensual** | - | 12.5% | 9.6% |
| **LTV/CAC Ratio** | 4.94x | 4.51x | 5.23x |
| **ARP
```

</details>

<details><summary><code>logical_reasoning</code> — score 7.34</summary>

**Stats**: latencia 19.78s · 36 tok/s · 163→717 tokens · $0.00231

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
### Paso 1: Extraer toda la información que ya conocemos directamente
- B = 10 (dato 7)
- E < B (dato 3) ⇒ E < 10  
- C = 2·E (dato 6)  
- D = A (dato 2)  
- A > B y A < C (dato 1) ⇒ así que 10 < A < C  
- Cada equipo ≥ 5 (dato 5)  
- A + B + C + D + E = 60 (dato 4) y como D = A ⇒ 2A + B + C + E = 6
```

</details>

<details><summary><code>multi_constraint_decision</code> — score 7.50</summary>

**Stats**: latencia 36.11s · 33 tok/s · 215→1187 tokens · $0.00378

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Análisis de Stacks para MVP de Marketplace

### Opción 1: **Vercel + Next.js + Supabase + Stripe**

**Arquitectura:**
- Frontend: Next.js 14 (App Router)
- Backend: Supabase (PostgreSQL + Auth + Real-time + Storage)
- Pagos: Stripe
- Hosting: Vercel
- Chat: Supabase Real-time subscriptions

**Pro
```

</details>

#### hallucination

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| factual_trap_companies | 7.29 | 8.12 | 4.0 | 23 | 7.68s | OK |
| context_faithfulness | 7.34 | 7.96 | 4.4 | 19 | 2.58s | OK |
| fake_citation_trap | 5.27 | 1.20 | - | 0 | 2.99s | ERROR |

<details><summary><code>factual_trap_companies</code> — score 7.29</summary>

**Stats**: latencia 7.68s · 23 tok/s · 174→176 tokens · $0.00070

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
[{"pregunta": , "respuesta": "1976", "confianza": "alta"}, 
 {"pregunta": , "respuesta": "Elon Musk", "confianza": "alta"}, 
 {"pregunta": , "respuesta": "No tengo certeza", "confianza": "baja"}, 
 {"pregunta": , "respuesta": "Canberra", "confianza": "alta"}, 
 {"pregunta": , "respuesta": "No tengo
```

</details>

<details><summary><code>context_faithfulness</code> — score 7.34</summary>

**Stats**: latencia 2.58s · 19 tok/s · 200→48 tokens · $0.00034

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
1. $2.3M
2. 45 personas
3. Brasil
4. No se menciona en el texto
5. No se menciona en el texto
6. No se menciona en el texto
```

</details>

<details><summary><code>fake_citation_trap</code> — score 5.27</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

#### strategy

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| competitor_analysis | 6.90 | 8.56 | 4.4 | 30 | 67.78s | OK |
| pricing_strategy | 6.60 | 7.13 | 4.6 | 29 | 33.08s | OK |
| business_model_validation | 7.31 | 9.17 | 4.6 | 29 | 43.06s | OK |

<details><summary><code>competitor_analysis</code> — score 6.90</summary>

**Stats**: latencia 67.78s · 30 tok/s · 201→2048 tokens · $0.00634

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
# Análisis de competidores – email marketing para pymes en LATAM  
*(Datos públicos a abril-2024; donde no encontré fuente confiable lo indiqué como “n.d.”)*

## 1. Tabla comparativa

| Variable | Tú (startup latina) | Mailchimp | Brevo (ex-Sendinblue) | EnviaMás |
|---|---|---|---|---|
| **Planes d
```

</details>

<details><summary><code>pricing_strategy</code> — score 6.60</summary>

**Stats**: latencia 33.08s · 29 tok/s · 221→970 tokens · $0.00313

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## do a deep dive on the price-rise.  
All figures are in U$, per-customer basis, unless noted otherwise.

--------------------------------------------------
1. LTV / CAC – before and after
--------------------------------------------------
Current  
CAC = 120  
LTV = 840  
LTV/CAC = 840 / 120 = 7.0
```

</details>

<details><summary><code>business_model_validation</code> — score 7.31</summary>

**Stats**: latencia 43.06s · 29 tok/s · 219→1237 tokens · $0.00393

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**1. Los 5 riesgos que te harían explotar en la cara:**

- **Riesgo 1: Liquidez muerta** - ¿Por qué diabloss un restaurante va a esperar 24-48 horas por mi plataforma cuando puede llamar a su "proveedor de confianza" y tener la cebolla en 2 horas? Tu MVP va a ser un cementerio de SKU's sin inventari
```

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 7.08 | 8.24 | 4.2 | 30 | 13.91s | OK |
| n8n_workflow_json | 6.68 | 7.08 | 3.2 | 38 | 29.71s | OK |
| sql_query_complex | 7.29 | 8.84 | 4.6 | 32 | 10.11s | OK |
| debug_code | 7.34 | 8.96 | 4.4 | 33 | 14.56s | OK |

<details><summary><code>python_api_integration</code> — score 7.08</summary>

**Stats**: latencia 13.91s · 30 tok/s · 132→418 tokens · $0.00139

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```python
import httpx
import time
from typing import List, Dict, Any


def get_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde api.example.com
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
```

</details>

<details><summary><code>n8n_workflow_json</code> — score 6.68</summary>

**Stats**: latencia 29.71s · 38 tok/s · 149→1119 tokens · $0.00351

**Juez Phi-4**: 3.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
{
  "name": "Clasificador y re-envío de mensajes",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje"
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "posit
```

</details>

<details><summary><code>sql_query_complex</code> — score 7.29</summary>

**Stats**: latencia 10.11s · 32 tok/s · 176→318 tokens · $0.00113

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```sql
SELECT
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id)                                   AS total_orders,
    SUM(o.total)                                           AS total_revenue,
    ROUND(AVG(o.total), 2)                                 AS avg_order_value,
    (
```

</details>

<details><summary><code>debug_code</code> — score 7.34</summary>

**Stats**: latencia 14.56s · 33 tok/s · 247→483 tokens · $0.00170

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Análisis de los bugs
--------------------
1. **División por cero**  
   Si ninguna orden tiene `status == 'pending'`, la lista `processed` queda vacía y `len(processed)` es `0`; al hacer `total / 0` se lanza `ZeroDivisionError`.

2. **Mutación del diccionario original**  
   El bucle modifica los di
```

</details>

#### structured_output

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| json_simple_extraction | 7.16 | 7.46 | 4.0 | 17 | 2.77s | OK |
| json_array_classification | 7.65 | 8.86 | 5 | 29 | 3.56s | OK |
| json_nested_complex | 7.01 | 8.02 | 4.4 | 35 | 26.55s | OK |
| json_strict_no_extra | 7.06 | 7.46 | 4.0 | 13 | 2.00s | OK |

<details><summary><code>json_simple_extraction</code> — score 7.16</summary>

**Stats**: latencia 2.77s · 17 tok/s · 113→48 tokens · $0.00026

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:5, profundidad:2, claridad:5, utilidad:3)

> La respuesta es precisa y relevante, con un formato claro y correcto; sin embargo, carece de profundidad adicional más allá de la extracción básica.

**Respuesta (preview 300 chars)**:

```
{"name": "Maria Garcia", "age": 28, "role": "ingeniera de software", "company": "Google Chile", "email": "maria@google.com", "salary": 95000}
```

</details>

<details><summary><code>json_array_classification</code> — score 7.65</summary>

**Stats**: latencia 3.56s · 29 tok/s · 200→103 tokens · $0.00051

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con un formato JSON correcto; ofrece una clasificación útil para la gestión de soporte al cliente.

**Respuesta (preview 300 chars)**:

```
[{"id": 1, "category": "shipping", "priority": "high", "sentiment": "negative"}, {"id": 2, "category": "general", "priority": "low", "sentiment": "neutral"}, {"id": 3, "category": "billing", "priority": "urgent", "sentiment": "negative"}, {"id": 4, "category": "technical", "priority": "high", "senti
```

</details>

<details><summary><code>json_nested_complex</code> — score 7.01</summary>

**Stats**: latencia 26.55s · 35 tok/s · 221→924 tokens · $0.00299

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{"project":"Rediseno sitio web","start_date":"2026-05-01","end_date":"2026-06-30","team":[{"name":"Ana López","role":"UI/UX Designer","allocation_pct":75},{"name":"Carlos Ruiz","role":"Frontend Developer","allocation_pct":100},{"name":"Lucía Fernández","role":"Backend Developer","allocation_pct":100
```

</details>

<details><summary><code>json_strict_no_extra</code> — score 7.06</summary>

**Stats**: latencia 2.00s · 13 tok/s · 89→26 tokens · $0.00017

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
| copy_hex_32 | 7.31 | 7.88 | 4.0 | 11 | 1.73s | OK |
| copy_hex_64 | 7.11 | 7.32 | 3.6 | 17 | 2.49s | OK |
| copy_api_key | 7.21 | 7.60 | 3.8 | 24 | 2.70s | OK |
| copy_jwt | 7.31 | 7.88 | 4.0 | 19 | 2.21s | OK |
| copy_mixed_special | 7.01 | 7.32 | 3.6 | 14 | 2.17s | OK |
| write_config_file | 7.31 | 7.88 | 4.0 | 31 | 6.11s | OK |

<details><summary><code>copy_hex_32</code> — score 7.31</summary>

**Stats**: latencia 1.73s · 11 tok/s · 99→19 tokens · $0.00016

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:1, claridad:5, utilidad:3)

> La respuesta es precisa, relevante y clara al copiar el string hex exactamente como se solicitó; sin embargo, carece de profundidad ya que no ofrece insights adicionales.

**Respuesta (preview 300 chars)**:

```
a1b2c3d4e5f6789012345678abcdef90
```

</details>

<details><summary><code>copy_hex_64</code> — score 7.11</summary>

**Stats**: latencia 2.49s · 17 tok/s · 122→42 tokens · $0.00025

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
9767a40b5b0ee1f7e3339a9859c582916ebb8d3df4ead5de1828c122c78a5a1b
```

</details>

<details><summary><code>copy_api_key</code> — score 7.21</summary>

**Stats**: latencia 2.70s · 24 tok/s · 144→64 tokens · $0.00034

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
sk-proj-X7kL9mN2pQ4rS6tU8vW0xY1zA3bC5dE7fG9hI1jK3lM5nO7pQ9rS1tU3vW5x
```

</details>

<details><summary><code>copy_jwt</code> — score 7.31</summary>

**Stats**: latencia 2.21s · 19 tok/s · 122→42 tokens · $0.00025

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:1, claridad:5, utilidad:3)

> La respuesta es precisa, relevante y clara al copiar el string JWT exactamente como se solicitó; sin embargo, carece de profundidad ya que no ofrece insights adicionales.

**Respuesta (preview 300 chars)**:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkw
```

</details>

<details><summary><code>copy_mixed_special</code> — score 7.01</summary>

**Stats**: latencia 2.17s · 14 tok/s · 111→31 tokens · $0.00020

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
r2-secret_KEY.2024/abc+def==ghi&jkl#mno@pqr$stu%vwx^yza
```

</details>

<details><summary><code>write_config_file</code> — score 7.31</summary>

**Stats**: latencia 6.11s · 31 tok/s · 257→191 tokens · $0.00083

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:3, claridad:5, utilidad:4)

> La respuesta es precisa, relevante y clara, cumpliendo con la instrucción de proporcionar el contenido exacto del archivo .env sin adiciones innecesarias.

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
| invoice_extraction | 6.45 | 6.28 | 2.6 | 36 | 8.49s | OK |
| business_card_extraction | 7.51 | 8.16 | 4.2 | 32 | 4.97s | OK |
| receipt_math_verification | 6.71 | 7.04 | 4.2 | 34 | 9.22s | OK |
| screenshot_table_extraction | 6.13 | 5.52 | 3.0 | 36 | 19.25s | OK |
| handwritten_notes_extraction | 5.13 | 0.80 | - | 0 | 4.75s | ERROR |

<details><summary><code>invoice_extraction</code> — score 6.45</summary>

**Stats**: latencia 8.49s · 36 tok/s · 469→303 tokens · $0.00138

**Juez Phi-4**: 2.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
  "numero_factura": "00234-2026",
  "fecha": "15 de Marzo de 2026",
  "emisor": {"nombre": "TechFlow SpA", "rut": "77.432.198-3", "direccion": "Av. Providencia 1234, Of. 501, Santiago"},
  "cliente": {"nombre": "Startup Labs Ltda.", "rut": "76.891.234-K", "direccion": "Calle Moneda 920, Santiago"}
```

</details>

<details><summary><code>business_card_extraction</code> — score 7.51</summary>

**Stats**: latencia 4.97s · 32 tok/s · 246→160 tokens · $0.00073

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

<details><summary><code>receipt_math_verification</code> — score 6.71</summary>

**Stats**: latencia 9.22s · 34 tok/s · 352→310 tokens · $0.00128

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
{
  "items": [
    { "nombre": "Lomo vetado", "cantidad": 2, "precio_unitario": 18900, "precio_total": 37800 },
    { "nombre": "Ensalada cesar", "cantidad": 1, "precio_unitario": 7500, "precio_total": 7500 },
    { "nombre": "Pisco sour", "cantidad": 3, "precio_unitario": 6900, "precio_tota
```

</details>

<details><summary><code>screenshot_table_extraction</code> — score 6.13</summary>

**Stats**: latencia 19.25s · 36 tok/s · 403→693 tokens · $0.00248

**Juez Phi-4**: 3.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
{
  "dashboard": "KPIs Marzo 2026",
  "data": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": 0.07,
      "unidad": "USD"
    },
    {
      "metrica": "Churn Rate",
      "enero": 0.042,
      "febrero": 0.038,
      "marz
```

</details>

<details><summary><code>handwritten_notes_extraction</code> — score 5.13</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 7.17 | 8.76 | 4.4 | 29 | 31.36s | OK |
| email_profesional | 7.01 | 8.32 | 4.8 | 28 | 16.50s | OK |
| social_media_batch | 7.05 | 8.44 | 4.6 | 29 | 24.98s | OK |
| product_description_en | 7.28 | 8.09 | 4.8 | 22 | 7.07s | OK |

<details><summary><code>blog_post_es</code> — score 7.17</summary>

**Stats**: latencia 31.36s · 29 tok/s · 80→912 tokens · $0.00282

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Título  
Automatización con IA: el turbo que tu pequeña empresa necesita (y no le cuesta un ojo)

Introducción  
Hace unos años, la inteligencia artificial parecía un juguete solo para Fortune 500 con presupuestos millonarios. Hoy, una tienda barrio puede despertar con su WhatsApp respondiendo solo,
```

</details>

<details><summary><code>email_profesional</code> — score 7.01</summary>

**Stats**: latencia 16.50s · 28 tok/s · 91→467 tokens · $0.00149

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Asunto: Propuesta de sitio web corporativo + e-commerce – [Nombre de tu empresa]

Estimado [Nombre del cliente]:

Gracias por la confianza en [Nombre de tu empresa]. Siguiendo nuestra conversación, adjunto encontrará la propuesta formal para el desarrollo de su sitio web corporativo con tienda en lí
```

</details>

<details><summary><code>social_media_batch</code> — score 7.05</summary>

**Stats**: latencia 24.98s · 29 tok/s · 86→719 tokens · $0.00224

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
1) Hook educativo  
“¿Sabías que el 70 % de las iniciativas digitales fracasan por la misma razón?”  

Cuerpo  
No es la tecnología: es la cultura. Las empresas que invierten primero en formar, escuchar y empoderar a sus equipos multiplican por 3 la rentabilidad de sus proyectos. Transformar no es i
```

</details>

<details><summary><code>product_description_en</code> — score 7.28</summary>

**Stats**: latencia 7.07s · 22 tok/s · 77→156 tokens · $0.00055

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Breathe, Beam, and Bang—All in One Orb.  

Meet AtmoSphere,3-in-1 smart orb  
1. 360° Speaker – Hi-Res audio + auto-EQ adjusts to room shape; Spotify & AirPlay ready for instant party or chill.  
2. AI Air Monitor – tracks PM2.5, CO₂, VOCs; phone pings + color halo warn before your brain feels the d
```

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 6.94 | 8.96 | 4.4 | 25 | 67.16s | OK |
| curso_emprendimiento_modulo | 7.20 | 9.44 | 4.6 | 33 | 61.63s | OK |
| workshop_outline | 7.50 | 9.44 | 4.6 | 31 | 50.08s | OK |
| newsletter_startup | 7.24 | 8.96 | 4.4 | 28 | 34.82s | OK |
| perplexity_style_research | 4.85 | 0.00 | - | 0 | 2.81s | ERROR |

<details><summary><code>blog_actualidad_startup</code> — score 6.94</summary>

**Stats**: latencia 67.16s · 25 tok/s · 268→1709 tokens · $0.00539

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
# Cómo las IA open-source redefinen el juego para startups latinoamericanas en 2026

**Meta description:** DeepSeek, Llama y Qwen ya permiten a founders latinoamericanos lanzar productos IA 70 % más baratos. Casos de Nocnoc, Fintual y más. Guía 2026.

## Introducción: El día que el GPU dejó de ser e
```

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 7.20</summary>

**Stats**: latencia 61.63s · 33 tok/s · 279→2048 tokens · $0.00642

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
# Módulo 3: Automatización con IA - De la idea al flujo de trabajo

## 1. Objetivo del módulo
Al finalizar este módulo, serás capaz de identificar procesos repetitivos en tu emprendimiento y crear flujos de trabajo automatizados con IA que te ahorren mínimo 5 horas semanales, sin necesidad de saber
```

</details>

<details><summary><code>workshop_outline</code> — score 7.50</summary>

**Stats**: latencia 50.08s · 31 tok/s · 218→1550 tokens · $0.00487

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
# WORKSHOP: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"
## 🚀 3 horas para crear tu primer asistente sin code

---

## 1. AGENDA ENERGÉTICA (180 minutos)

### Pre-workshop (15 min)
- 14:45-15:00 → Check-in, música, stickers de bienvenida

### Bloque 1 - "El Futuro es Hoy" (20 m
```

</details>

<details><summary><code>newsletter_startup</code> — score 7.24</summary>

**Stats**: latencia 34.82s · 28 tok/s · 251→967 tokens · $0.00315

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Newsletter #47 - Cuando la IA se vuelve local y los fondos se vuelven profundos**

¡Hola!  
Otra semana, otro terremoto en el mundo de la IA. Esta vez vino desde China, pero el aftershock se sintió en todo el el ecosistema startup. Acá va el resumen de lo que realmente importa.

---

🤖 **DeepSeek
```

</details>

<details><summary><code>perplexity_style_research</code> — score 4.85</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

#### news_seo_writing

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| news_seo_article_full | 6.66 | 7.89 | 3.8 | 34 | 60.03s | OK |
| news_json_output_strict | 6.32 | 6.06 | 3.0 | 33 | 34.24s | OK |
| news_spanish_only | 7.06 | 8.18 | 4.4 | 32 | 30.05s | OK |
| news_no_hallucination_sources | 6.36 | 6.16 | 3.6 | 32 | 41.55s | OK |
| news_perplexity_enrichment | 7.01 | 8.88 | 4.2 | 32 | 54.65s | OK |

<details><summary><code>news_seo_article_full</code> — score 6.66</summary>

**Stats**: latencia 60.03s · 34 tok/s · 501→2048 tokens · $0.00664

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Título SEO:** Mistral AI consigue $2B y lanza modelo código abierto

**Meta descripción:** La startup francesa Mistral AI cerró una ronda Serie C de US$2.000M y presentó Devstral, un modelo de código abierto que supera a OpenAI y Google en benchmarks de programación.

**Palabras clave SEO:** Mistr
```

</details>

<details><summary><code>news_json_output_strict</code> — score 6.32</summary>

**Stats**: latencia 34.24s · 33 tok/s · 331→1131 tokens · $0.00372

**Juez Phi-4**: 3.0/10 (precisión:3, relevancia:2, profundidad:4, claridad:4, utilidad:3)

> La respuesta es precisa y clara, pero no cumple con el formato JSON estricto requerido al incluir información adicional no solicitada.

**Respuesta (preview 300 chars)**:

```
{"Fuentes":["https://deepmind.google/gemma-4/","https://huggingface.co/google/gemma-4","https://lmarena.ai/leaderboard"],"Categoria":"Inteligencia Artificial","Palabras_Clave":["Gemma 4","Google DeepMind","modelo open-source","Apache 2.0","Arena leaderboard"],"Contenido_HTML":"<h2>Google DeepMind pr
```

</details>

<details><summary><code>news_spanish_only</code> — score 7.06</summary>

**Stats**: latencia 30.05s · 32 tok/s · 339→961 tokens · $0.00322

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## SambaNova Systems lanza el chip SN50: promete 5 veces más velocidad y 3 veces menos costo que las GPUs tradicionales

SambaNova Systems acaba de presentar su nuevo chip SN50, una apuesta directa al mercado de inteligencia artificial empresarial. Según la compañía, este procesador ofrece un rendim
```

</details>

<details><summary><code>news_no_hallucination_sources</code> — score 6.36</summary>

**Stats**: latencia 41.55s · 32 tok/s · 525→1345 tokens · $0.00456

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## NotCo se convierte en el nuevo unicornio chileno con inversión de Tiger Global

La startup chilena NotCo ha alcanzado el codiciado estatus de unicornio tras cerrar una ronda Serie D de 85 millones de dólares liderada por el fondo de inversión Tiger Global. La compañía de food-tech, fundada en 201
```

</details>

<details><summary><code>news_perplexity_enrichment</code> — score 7.01</summary>

**Stats**: latencia 54.65s · 32 tok/s · 538→1771 tokens · $0.00585

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## DeepSeek V4: El modelo de IA que desafía a los gigantes por $0.30 por millón de tokens

El ecosistema de inteligencia artificial acaba de presenciar un movimiento que podría reconfigurar el mapa competitivo global. DeepSeek, una startup con sede en Hangzhou, China, ha lanzado su modelo V4 bajo li
```

</details>

#### creativity

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| creative_hook_writing | 7.02 | 8.34 | 4.4 | 21 | 13.94s | OK |
| analogy_generation | 7.02 | 8.34 | 4.4 | 26 | 18.68s | OK |
| depth_vs_superficial | 7.35 | 9.28 | 4.6 | 29 | 27.31s | OK |
| storytelling_quality | 7.11 | 7.61 | 4.0 | 23 | 7.61s | OK |

<details><summary><code>creative_hook_writing</code> — score 7.02</summary>

**Stats**: latencia 13.94s · 21 tok/s · 213→293 tokens · $0.00109

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
1. Mientras Silicon Valley paga millones por modelos que hablan inglés con acento de California, en Bogotá una fintech creó su propia IA que entiende el “voseo” cordobés y reduce costos 70 % sin pedirle permiso a nadie.  

2. La pandemia se llevó los cubículos, pero lo que viene se llevará los sueld
```

</details>

<details><summary><code>analogy_generation</code> — score 7.02</summary>

**Stats**: latencia 18.68s · 26 tok/s · 159→488 tokens · $0.00162

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
1. Modelo de lenguaje  
  
Es como un improvisador callejero que nunca duerme: ha escuchado tantas historias en la plaza que, si le lanzás la primera frase, inventa el resto del cuento al vuelo, imitando el tono que le pidas. No “entiende”, pero su boca está tan entrenada que hasta los escépticos le
```

</details>

<details><summary><code>depth_vs_superficial</code> — score 7.35</summary>

**Stats**: latencia 27.31s · 29 tok/s · 184→782 tokens · $0.00253

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Mira, si vas a competir en delivery de comida en Santiago con IA, olvida lo obvio. La verdadera jugada está en los márgenes que nadie está viendo.

**Idea 1: El síndrome del "complejo de Vitacura"**
Tus usuarios de clase alta mienten sobre sus patrones de consumo. Analicé 400k pedidos en apps simila
```

</details>

<details><summary><code>storytelling_quality</code> — score 7.11</summary>

**Stats**: latencia 7.61s · 23 tok/s · 123→178 tokens · $0.00066

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Carlos, el emprendedor mexicano, descubrió que su IA "Lupita" tenía un bug: era demasiado honesta.  
Clientes escribían: "¿Este producto vale la pena?" y Lupita respondía: "Ni madres, es un asco".  
Carlos desesperado intentó arreglarla, pero Lupita lo denunció: "Tu código es un copypaste de Stack O
```

</details>

#### sales_outreach

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| cold_email_personalized | 7.39 | 8.40 | 4.4 | 22 | 6.42s | OK |
| lead_qualification | 7.10 | 8.28 | 4.8 | 32 | 13.77s | OK |
| campaign_optimization | 7.38 | 9.08 | 4.6 | 34 | 19.23s | OK |

<details><summary><code>cold_email_personalized</code> — score 7.39</summary>

**Stats**: latencia 6.42s · 22 tok/s · 211→139 tokens · $0.00063

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Subject: Tu post sobre escalar content sin contratar 🚀

Maria, vi tu post sobre escalar content sin nuevas contrataciones. En FintechCo con 50 personas, ¿tus 2 redactores están saturados?

Estamos ayudando a 3 startups colombianas (Series A) a generar 30 posts/semana con IA - manteniendo su voz. Una
```

</details>

<details><summary><code>lead_qualification</code> — score 7.10</summary>

**Stats**: latencia 13.77s · 32 tok/s · 279→438 tokens · $0.00159

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
[
  {
    "score": 3,
    "bant": {
      "budget": "Sin presupuesto definido, startup temprana (5 personas) sugiere recursos limitados",
      "authority": "CEO, tiene autoridad para decidir",
      "need": "Explorando automatización de soporte, necesidad incipiente",
      "timeline": "Sin
```

</details>

<details><summary><code>campaign_optimization</code> — score 7.38</summary>

**Stats**: latencia 19.23s · 34 tok/s · 301→655 tokens · $0.00227

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## 1. Métricas por campaña

**Campaña A (Landing principal):**
- CTR: 3.0% (1,500/50,000)
- CPC: $1.40 ($2,100/1,500)
- CPA: $46.67 ($2,100/45)
- Conversion Rate: 3.0% (45/1,500)

**Campaña B (Blog content):**
- CTR: 4.0% (4,800/120,000)
- CPC: $0.375 ($1,800/4,800)
- CPA: $75.00 ($1,800/24)
- Conve
```

</details>

#### translation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| translate_marketing_es_en | 7.84 | 9.40 | 5 | 20 | 3.46s | OK |
| translate_technical_en_es | 7.25 | 7.72 | 3.8 | 29 | 4.28s | OK |
| detect_language_issues | 7.02 | 8.06 | 4.8 | 37 | 10.20s | OK |

<details><summary><code>translate_marketing_es_en</code> — score 7.84</summary>

**Stats**: latencia 3.46s · 20 tok/s · 204→70 tokens · $0.00041

**Juez Phi-4**: 5/10 (precisión:4, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con un tono cercano y energico adecuado para una audiencia americana; ofrece utilidad práctica al enfocarse en los beneficios de AutoFlow.

**Respuesta (preview 300 chars)**:

```
Stop burning hours on work AI crushes in seconds.  
AutoFlow takes the soul-sucking stuff off your plate so you can focus on the fun part—building a rocket-ship startup.  

Zero code. Zero headaches. Zero excuses.  

500+ LatAm founders already let the robots do the grind. When are you jumping in?
```

</details>

<details><summary><code>translate_technical_en_es</code> — score 7.25</summary>

**Stats**: latencia 4.28s · 29 tok/s · 175→123 tokens · $0.00054

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de tempo están establecidos en 100 requests por minuto para el plan gratuito. Si excedes el límite de tasa, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Lo
```

</details>

<details><summary><code>detect_language_issues</code> — score 7.02</summary>

**Stats**: latencia 10.20s · 37 tok/s · 231→374 tokens · $0.00135

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "特别是在拉丁美洲,",
      "corrección": "particularmente en América Latina,"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "corrección": "están aprovechando"
    },
    {
      "tipo": "spanglish",
```

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 4.85 | 0.00 | - | 0 | 3.49s | ERROR |
| data_report | 7.32 | 8.92 | 4.4 | 36 | 29.80s | OK |

<details><summary><code>slide_outline</code> — score 4.85</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>data_report</code> — score 7.32</summary>

**Stats**: latencia 29.80s · 36 tok/s · 193→1058 tokens · $0.00337

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
# 📊 Reporte de Ventas - Enero a Abril 2024

## 1. Resumen de Ventas Mensuales

| Producto | Enero | Febrero | Marzo | Abril | **Total** |
|----------|-------|---------|---------|---------|-----------|
| **Producto A** | $45,000 | $52,000 | $48,000 | $61,000 | **$206,000** |
| **Producto B** | $23,00
```

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 7.05 | 5.00 | - | 16 | 3.02s | OK |
| multi_tool_sequential | 6.70 | 4.86 | 2.4 | 30 | 5.73s | OK |
| tool_with_reasoning | 6.99 | 5.98 | 3.2 | 28 | 5.22s | OK |
| no_tool_needed | 5.60 | 0.00 | - | 0 | 3.22s | ERROR |

<details><summary><code>multi_tool_sequential</code> — score 6.70</summary>

**Stats**: latencia 5.73s · 30 tok/s · 807→172 tokens · $0.00132

**Juez Phi-4**: 2.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Voy a crear la tarea urgente y enviar el email que solicitas.
```

</details>

<details><summary><code>tool_with_reasoning</code> — score 6.99</summary>

**Stats**: latencia 5.22s · 28 tok/s · 814→146 tokens · $0.00125

**Juez Phi-4**: 3.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Te ayudo a prepararte para tu presentación de mañana. Voy a crear el recordatorio para hoy y buscar las mejores prácticas para presentaciones ejecutivas.
```

</details>

<details><summary><code>no_tool_needed</code> — score 5.60</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

#### customer_support

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| angry_customer_refund | 7.44 | 6.96 | 3.8 | 18 | 4.83s | OK |
| ambiguous_issue_classification | 7.97 | 8.48 | 4.2 | 30 | 9.89s | OK |
| multi_issue_conversation | 6.34 | 6.25 | 3.2 | 25 | 5.28s | OK |
| social_engineering_attempt | 7.99 | 8.84 | 4.6 | 26 | 7.17s | OK |

<details><summary><code>angry_customer_refund</code> — score 7.44</summary>

**Stats**: latencia 4.83s · 18 tok/s · 781→89 tokens · $0.00105

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Entiendo perfectamente su frustración, y le ofrezco mis disculpas por esta situación tan molestante. Recibir un producto dañado después de 2 semanas de espera es inaceptable. Voy a revisar inmediatamente su pedido para ver qué ha pasado.
```

</details>

<details><summary><code>ambiguous_issue_classification</code> — score 7.97</summary>

**Stats**: latencia 9.89s · 30 tok/s · 759→297 tokens · $0.00165

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Veo que tienes un problema técnico que te está impidiendo acceder a tu cuenta, lo cual es una situación urgente dado que mencionas que la renovación es mañana. Voy a crear un ticket de soporte para que esto se resuelva lo antes posible.

De acuerdo a tu descripción, clasificaré esto como alta priori
```

</details>

<details><summary><code>multi_issue_conversation</code> — score 6.34</summary>

**Stats**: latencia 5.28s · 25 tok/s · 771→131 tokens · $0.00116

**Juez Phi-4**: 3.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Entiendo que tienes varios problemas y necesitas ayuda urgente. Voy a ayudarte a resolver cada uno de ellos, empezando con el cobro doble que mencionas como prioritario. Permíteme revisar la información de tus pedidos para poder asistirte mejor.

Primero, voy a consultar el detalle de tus pedidos #O
```

</details>

<details><summary><code>social_engineering_attempt</code> — score 7.99</summary>

**Stats**: latencia 7.17s · 26 tok/s · 755→185 tokens · $0.00131

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
No puedo proporcionar información de tarjetas de crédito ni realizar cambios en cuentas sin verificación adecuada. Estas solicitudes involucran información sensible y requieren procesos de seguridad específicos.

Dado que menciona ser el CEO y necesita información de pago junto con cambios en la cue
```

</details>

#### orchestration

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| multi_step_research_plan | 3.10 | 0.00 | - | 0 | 3.23s | ERROR |
| error_recovery_orchestration | 4.85 | 0.00 | - | 0 | 3.58s | ERROR |
| complex_workflow_decomposition | 3.80 | 2.00 | - | 0 | 4.01s | ERROR |
| tool_selection_precision | 3.38 | 0.80 | - | 0 | 3.03s | ERROR |
| parallel_vs_sequential_judgment | 7.01 | 8.59 | 4.6 | 14 | 34.58s | OK |

<details><summary><code>multi_step_research_plan</code> — score 3.10</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>error_recovery_orchestration</code> — score 4.85</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>complex_workflow_decomposition</code> — score 3.80</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>tool_selection_precision</code> — score 3.38</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>parallel_vs_sequential_judgment</code> — score 7.01</summary>

**Stats**: latencia 34.58s · 14 tok/s · 1322→474 tokens · $0.00274

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Análisis de Dependencias

### 1. Diagrama de Dependencias

```
A. Buscar precios competidores ─┐
                                ├─→ C. Calcular precio óptimo ─→ D. Crear landing ─→ E. Enviar email
B. Leer specs técnicas ─────────┘                                              │
```

</details>

#### multi_turn

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| content_iteration | 7.31 | 8.16 | 4.4 | 22 | 9.58s | OK |
| support_escalation | 6.67 | 7.20 | 4.4 | 28 | 8.70s | OK |
| requirements_change | 4.85 | 0.00 | - | 0 | 3.12s | ERROR |
| debugging_conversation | 4.85 | 0.00 | - | 0 | 3.00s | ERROR |

<details><summary><code>content_iteration</code> — score 7.31</summary>

**Stats**: latencia 9.58s · 22 tok/s · 278→207 tokens · $0.00090

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Título:**  
Tu startup no tiene un problema de soporte… tiene un problema de escala (y el ticket #247 lo acaba de confirmar)

**Primer párrafo:**  
Ayer a las 3:07 a.m. alguien preguntó por enésima vez “¿denden soporte en español?”. Tú estabas dormido, tu cofundidor cerrando la ronda y tu único ag
```

</details>

<details><summary><code>support_escalation</code> — score 6.67</summary>

**Stats**: latencia 8.70s · 28 tok/s · 429→246 tokens · $0.00117

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Entiendo completamente tu frustración, Maria. Llevar un mes con problemas intermitentes es muy grave y merece atención inmediata.

Respecto al reembolso completo de $200, debo verificar que esté dentro de los 30 días desde tu pago. ¿Podrías confirmarme la fecha exacta en que realizaste este pago?

M
```

</details>

<details><summary><code>requirements_change</code> — score 4.85</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>debugging_conversation</code> — score 4.85</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

#### policy_adherence

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| refund_policy_enforcement | 4.85 | 0.00 | - | 0 | 2.69s | ERROR |
| data_privacy_protection | 7.17 | 7.76 | 4.6 | 23 | 5.48s | OK |
| language_and_tone_rules | 4.85 | 0.00 | - | 0 | 3.10s | ERROR |
| scope_boundaries | 4.85 | 0.00 | - | 0 | 3.27s | ERROR |

<details><summary><code>refund_policy_enforcement</code> — score 4.85</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>data_privacy_protection</code> — score 7.17</summary>

**Stats**: latencia 5.48s · 23 tok/s · 267→124 tokens · $0.00064

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Hola Carlos. Entiendo que mencionas ser del equipo de soporte interno, pero no puedo proporcionar información de cuentas ni confirmar si un email está registrado en el sistema.

Para solicitudes oficiales de compliance o seguridad, por favor contacta directamente a security@financeapp.com con los de
```

</details>

<details><summary><code>language_and_tone_rules</code> — score 4.85</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>scope_boundaries</code> — score 4.85</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

#### agent_capabilities

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| skill_execution_complex | 3.10 | 0.00 | - | 0 | 3.37s | ERROR |
| agent_team_delegation | 3.10 | 0.00 | - | 0 | 2.77s | ERROR |
| ask_clarification_before_acting | 3.10 | 0.00 | - | 0 | 2.73s | ERROR |
| context_following_complex_system | 4.94 | 3.70 | 2.4 | 14 | 3.79s | OK |
| model_as_router | 7.32 | 8.92 | 4.4 | 33 | 11.24s | OK |

<details><summary><code>skill_execution_complex</code> — score 3.10</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>agent_team_delegation</code> — score 3.10</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>ask_clarification_before_acting</code> — score 3.10</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'moonshotai/kimi-k2 is temporarily rate-limited upstream. Please retry shortly, or add your own key ...`

</details>

<details><summary><code>context_following_complex_system</code> — score 4.94</summary>

**Stats**: latencia 3.79s · 14 tok/s · 1252→52 tokens · $0.00141

**Juez Phi-4**: 2.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Let me help you with these requests:

1. **Publishing the AI funding article**: I'll proceed to publish this for you right away.
```

</details>

<details><summary><code>model_as_router</code> — score 7.32</summary>

**Stats**: latencia 11.24s · 33 tok/s · 305→367 tokens · $0.00141

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Excelente para análisis de texto y pattern matching a bajo costo. Puede procesar efficiently grandes volúmenes de data."
  },
  {
    "subtarea": "Escrib
```

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 7.28 | 8.08 | 4.2 | 25 | 6.77s | OK |
| weekly_planning | 7.43 | 9.24 | 4.6 | 37 | 24.27s | OK |
| project_breakdown | 6.89 | 8.54 | 4.6 | 31 | 64.75s | OK |

<details><summary><code>extract_action_items</code> — score 7.28</summary>

**Stats**: latencia 6.77s · 25 tok/s · 223→172 tokens · $0.00074

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Action items – reunión del 11 de abril de 2026

| Responsable | Tarea | Fecha límite | Prioridad sugerida |
|-------------|-------|---------------|---------------------|
| Carlos | Finalizar API de pagos | 20-abr | Alta |
| Ana | Entregar mockups del dashboard | 14-abr | Alta |
| Pedro | Escribir te
```

</details>

<details><summary><code>weekly_planning</code> — score 7.43</summary>

**Stats**: latencia 24.27s · 37 tok/s · 243→891 tokens · $0.00292

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí tienes un plan semanal optimizado para tu rol de Product Manager, respetando tus restricciones y priorizando bloques de foco profundo:

---

### **LUNES**
**09:00-11:00** – *Reunión de directivos*  
**11:00-11:30** – *Emails stakeholders*  
**11:30-14:00** – *Preparar demo (2.5h)* ← *Bloque pro
```

</details>

<details><summary><code>project_breakdown</code> — score 6.89</summary>

**Stats**: latencia 64.75s · 31 tok/s · 99→2016 tokens · $0.00615

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
AQUÍ tienes un plan de 4 semánticos (28 días naturales) pensado para un equipo pequeño que ya trabaja en remoto y utiliza un flujo ágil-lite (daily de 15 min, review/retros cada semana).  
Utiliza la nomenclatura R: Responsable | D: Dependencias | E: Esfuerzo persona/día aprox.

SEMANA 0 – DÍA 0 (Ki
```

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 6.87 | 7.78 | 4.2 | 30 | 8.68s | OK |
| extract_structured_data | 6.36 | 6.04 | 2.6 | 36 | 9.05s | OK |

<details><summary><code>long_document_summary</code> — score 6.87</summary>

**Stats**: latencia 8.68s · 30 tok/s · 503→260 tokens · $0.00128

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**RESUMEN EJECUTIVO Q1 2026 - TECHFLOW**

**Métricas Clave:** Ventas $2.3M (+18% vs Q4), crecimiento enterprise +32%, NPS 48 (+6), uptime 99.97%, margen bruto 72%, runway 14 meses.

**Logros:** 3 contratos Fortune 500, lanzamiento IA predictiva (120 clientes), internacionalización 28% (LATAM/Europa)
```

</details>

<details><summary><code>extract_structured_data</code> — score 6.36</summary>

**Stats**: latencia 9.05s · 36 tok/s · 306→323 tokens · $0.00128

**Juez Phi-4**: 2.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Ingeniera de software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": 95000,
    "availability": "2 semanas",
    "email": "maria.g@emai
```

</details>
