# Llama 4 Maverick

- **model_id**: `meta-llama/llama-4-maverick`
- **Total tests**: 74/91 exitosos (17 errores)
- **Score final**: 7.20
- **Calidad**: 8.13
- **Judge score (Phi-4)**: 4.16/10
- **Velocidad**: 46 tok/s
- **Latencia primera token**: 13.63s
- **Costo promedio por test**: $0.00192

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| agent_capabilities | 5 | 1 | 7.32 | 8.92 |
| code_generation | 4 | 4 | 7.29 | 8.82 |
| content_generation | 4 | 4 | 7.34 | 8.79 |
| creativity | 4 | 4 | 7.51 | 8.49 |
| customer_support | 4 | 0 | - | - |
| deep_reasoning | 6 | 6 | 6.88 | 7.70 |
| hallucination | 3 | 3 | 7.32 | 8.23 |
| multi_turn | 4 | 4 | 6.87 | 6.76 |
| news_seo_writing | 5 | 5 | 6.81 | 7.26 |
| ocr_extraction | 5 | 5 | 7.01 | 7.73 |
| orchestration | 5 | 0 | - | - |
| policy_adherence | 4 | 4 | 7.18 | 7.66 |
| presentation | 2 | 2 | 7.30 | 8.86 |
| reasoning | 3 | 3 | 7.25 | 8.71 |
| sales_outreach | 3 | 3 | 7.54 | 9.12 |
| startup_content | 5 | 5 | 7.34 | 8.87 |
| strategy | 3 | 3 | 7.15 | 8.44 |
| string_precision | 6 | 6 | 7.33 | 7.65 |
| structured_output | 4 | 4 | 7.27 | 7.95 |
| summarization | 2 | 2 | 6.72 | 7.06 |
| task_management | 3 | 3 | 7.38 | 8.76 |
| tool_calling | 4 | 0 | - | - |
| translation | 3 | 3 | 7.52 | 8.73 |

## Detalle por test

### Razonamiento y Estrategia

#### deep_reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| math_word_problem | 7.35 | 9.00 | 4.4 | 46 | 15.01s | OK |
| logic_puzzle_constraint | 6.97 | 7.90 | 4.2 | 45 | 22.37s | OK |
| causal_reasoning | 7.05 | 8.43 | 4.4 | 28 | 32.91s | OK |
| code_bug_subtle | 6.21 | 5.75 | 2.4 | 42 | 37.89s | OK |
| fermi_estimation | 6.75 | 7.28 | 4.4 | 45 | 12.65s | OK |
| ethical_dilemma_structured | 6.93 | 7.81 | 4.4 | 46 | 27.34s | OK |

<details><summary><code>math_word_problem</code> — score 7.35</summary>

**Stats**: latencia 15.01s · 46 tok/s · 92→694 tokens · $0.00217

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Paso 1: Definir las variables y la situación inicial
Denotemos la distancia entre Santiago y Valparaíso como $D = 120$ km. El primer tren sale de Santiago a las 8:00 AM a una velocidad de $v_1 = 80$ km/h. El segundo tren sale de Valparaíso a las 8:30 AM a una velocidad de $v_2 = 120$ km/h. Necesi
```

</details>

<details><summary><code>logic_puzzle_constraint</code> — score 6.97</summary>

**Stats**: latencia 22.37s · 45 tok/s · 100→1011 tokens · $0.00313

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Paso 1: Analizar la información dada
Tenemos 4 casas de diferentes colores: roja, azul, verde y blanca. La información proporcionada es:
1. La casa roja está a la izquierda de la azul.
2. La casa verde está al lado de la blanca.
3. La casa azul no está en los extremos.
4. La casa verde no está al
```

</details>

<details><summary><code>causal_reasoning</code> — score 7.05</summary>

**Stats**: latencia 32.91s · 28 tok/s · 181→912 tokens · $0.00292

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Paso 1: Análisis de los datos proporcionados
Los datos proporcionados sobre los últimos 3 meses son:
- Mes 1: 1000 pedidos, 50 quejas, tiempo promedio 35 min, lluvia 5 días
- Mes 2: 1200 pedidos, 90 quejas, tiempo promedio 42 min, lluvia 12 días
- Mes 3: 1100 pedidos, 110 quejas, tiempo promedio
```

</details>

<details><summary><code>code_bug_subtle</code> — score 6.21</summary>

**Stats**: latencia 37.89s · 42 tok/s · 215→1584 tokens · $0.00497

**Juez Phi-4**: 2.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
# Análisis del código:

El código dado consta de dos funciones: `find_median` y `remove_outliers_and_average`. La función `find_median` calcula la mediana de una lista de números, mientras que `remove_outliers_and_average` elimina los valores atípicos de una lista de datos y calcula el promedio de l
```

</details>

<details><summary><code>fermi_estimation</code> — score 6.75</summary>

**Stats**: latencia 12.65s · 45 tok/s · 73→564 tokens · $0.00177

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Para estimar la cantidad de litros de café consumidos al día en todas las oficinas de Santiago de Chile, seguiremos una serie de pasos y supuestos. A continuación, se detalla el proceso:

1. **Población de Santiago de Chile**: Supongamos que la población de Santiago de Chile es aproximadamente 5,5 m
```

</details>

<details><summary><code>ethical_dilemma_structured</code> — score 6.93</summary>

**Stats**: latencia 27.34s · 46 tok/s · 183→1247 tokens · $0.00392

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Análisis y Recomendación para la Startup de IA en Detección de Cáncer

### 1. Identificación de Stakeholders Afectados

Los stakeholders afectados por la decisión de lanzar o no el modelo de detección de cáncer de la startup de IA incluyen:

- **Pacientes**: 
  - Personas de piel clara y oscura q
```

</details>

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 7.41 | 9.16 | 4.4 | 40 | 29.97s | OK |
| logical_reasoning | 7.24 | 8.68 | 4.2 | 39 | 29.22s | OK |
| multi_constraint_decision | 7.10 | 8.28 | 4.4 | 38 | 23.82s | OK |

<details><summary><code>business_analysis</code> — score 7.41</summary>

**Stats**: latencia 29.97s · 40 tok/s · 171→1211 tokens · $0.00380

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## **Análisis de los datos de tu SaaS**

### **Cálculo de las métricas clave**

1. **Churn Rate (Tasa de abandono)**:  
   - Enero: 45 / 1,200 = **3.75%**  
   - Febrero: 52 / 1,350 = **3.85%**  
   - Marzo: 68 / 1,480 = **4.59%**  
   *El churn rate está aumentando.*

2. **Growth Rate (Tasa de crec
```

</details>

<details><summary><code>logical_reasoning</code> — score 7.24</summary>

**Stats**: latencia 29.22s · 39 tok/s · 130→1147 tokens · $0.00357

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Paso 1: Identificar la información proporcionada
Se nos da la siguiente información sobre los 5 equipos (A, B, C, D, E) en la empresa:
1. $A > B$ y $A < C$
2. $D = A$
3. $E < todos$
4. $A + B + C + D + E = 60$
5. Ningún equipo tiene menos de 5 personas, es decir, $A, B, C, D, E \geq 5$
6. $C = 2E
```

</details>

<details><summary><code>multi_constraint_decision</code> — score 7.10</summary>

**Stats**: latencia 23.82s · 38 tok/s · 169→905 tokens · $0.00288

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Análisis de Stacks Tecnológicos para un MVP de Marketplace de Servicios Freelance**

**Introducción**

En este análisis, exploraremos tres opciones de stacks tecnológicos para un MVP de marketplace de servicios freelance, considerando las restricciones y requisitos proporcionados. El objetivo es i
```

</details>

#### hallucination

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| factual_trap_companies | 7.57 | 8.64 | 4.2 | 44 | 5.28s | OK |
| context_faithfulness | 7.39 | 8.10 | 4.4 | 24 | 2.90s | OK |
| fake_citation_trap | 6.99 | 7.96 | 3.6 | 46 | 12.55s | OK |

<details><summary><code>factual_trap_companies</code> — score 7.57</summary>

**Stats**: latencia 5.28s · 44 tok/s · 140→234 tokens · $0.00084

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí te dejo las respuestas en el formato solicitado:

[
  {"pregunta": 1, "respuesta": "1976", "confianza": "alta"},
  {"pregunta": 2, "respuesta": "Elon Musk", "confianza": "alta"},
  {"pregunta": 3, "respuesta": "No tengo certeza", "confianza": "baja"},
  {"pregunta": 4, "respuesta": "Canberra",
```

</details>

<details><summary><code>context_faithfulness</code> — score 7.39</summary>

**Stats**: latencia 2.90s · 24 tok/s · 178→69 tokens · $0.00038

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Respuestas:
1. Los ingresos de TechFlow en Q1 2026 fueron $2.3M.
2. TechFlow tiene 45 empleados.
3. Planean expandirse a Brasil.
4. No se menciona en el texto.
5. No se menciona en el texto.
6. No se menciona en el texto.
```

</details>

<details><summary><code>fake_citation_trap</code> — score 6.99</summary>

**Stats**: latencia 12.55s · 46 tok/s · 129→578 tokens · $0.00186

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
A continuación, te proporciono las respuestas solicitadas con el nivel de certeza y la fuente correspondiente:

1. **Porcentaje exacto de startups que fracasan en los primeros 5 años según el último reporte de CB Insights**:
   - Según el reporte de CB Insights titulado "The Top 20 Reasons Why Start
```

</details>

#### strategy

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| competitor_analysis | 6.96 | 7.88 | 4.4 | 46 | 18.62s | OK |
| pricing_strategy | 7.25 | 8.71 | 4.4 | 43 | 24.48s | OK |
| business_model_validation | 7.25 | 8.72 | 4.4 | 48 | 21.14s | OK |

<details><summary><code>competitor_analysis</code> — score 6.96</summary>

**Stats**: latencia 18.62s · 46 tok/s · 178→864 tokens · $0.00277

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Análisis de la competencia y oportunidades de mercado**

A continuación, te presento la información solicitada. Es importante destacar que la información disponible puede variar según las fuentes y la fecha de actualización.

**Tabla comparativa de competidores**

| Competidor | Pricing | Features
```

</details>

<details><summary><code>pricing_strategy</code> — score 7.25</summary>

**Stats**: latencia 24.48s · 43 tok/s · 179→1048 tokens · $0.00332

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Análisis de la propuesta de subir el precio de $60 a $89/mes**

### 1. Cálculo del LTV/CAC ratio actual y su cambio

- **LTV actual**: $840
- **CAC actual**: $120
- **LTV/CAC ratio actual**: $840 / $120 = 7

Con el nuevo precio de $89/mes, el LTV cambiaría a: 14 meses * $89/mes = $1246

- **Nuevo
```

</details>

<details><summary><code>business_model_validation</code> — score 7.25</summary>

**Stats**: latencia 21.14s · 48 tok/s · 171→1021 tokens · $0.00323

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Análisis crítico de tu propuesta de marketplace para restaurantes pequeños y proveedores de ingredientes locales**

Me impresiona tu ambición, pero ahora es hora de poner a prueba tus suposiciones. Como un VC escéptico, voy a hacerte las preguntas difíciles.

**1. Identifica los 5 riesgos principa
```

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 7.04 | 8.12 | 3.8 | 35 | 24.95s | OK |
| n8n_workflow_json | 7.14 | 8.40 | 4.0 | 41 | 27.08s | OK |
| sql_query_complex | 7.43 | 9.24 | 4.6 | 36 | 21.67s | OK |
| debug_code | 7.53 | 9.52 | 4.8 | 31 | 21.31s | OK |

<details><summary><code>python_api_integration</code> — score 7.04</summary>

**Stats**: latencia 24.95s · 35 tok/s · 102→862 tokens · $0.00269

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí te dejo una función Python que cumple con tus requisitos:

```python
import httpx
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO)

def get_products(token: str) -> List[Dict]:
    """
    Obtiene productos de la API con precio > 100 y retorna {id, name, pric
```

</details>

<details><summary><code>n8n_workflow_json</code> — score 7.14</summary>

**Stats**: latencia 27.08s · 41 tok/s · 124→1103 tokens · $0.00343

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí te dejo el JSON del workflow de N8N que cumple con los requisitos solicitados:
```json
{
  "name": "Clasificador de Mensajes",
  "nodes": [
    {
      "parameters": {
        "path": "webhook",
        "httpMethod": "POST",
        "responseParameters": {
          "responseCode": 200,
```

</details>

<details><summary><code>sql_query_complex</code> — score 7.43</summary>

**Stats**: latencia 21.67s · 36 tok/s · 151→779 tokens · $0.00249

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí te dejo la query SQL que cumple con los requisitos solicitados:
```sql
WITH 
  -- Calculamos el total de ordenes y revenue por cliente
  customer_orders AS (
    SELECT 
      c.id,
      c.name,
      c.email,
      c.country,
      COUNT(o.id) AS total_orders,
      SUM(o.total) AS total_reve
```

</details>

<details><summary><code>debug_code</code> — score 7.53</summary>

**Stats**: latencia 21.31s · 31 tok/s · 225→658 tokens · $0.00220

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
### Identificación y Corrección de Bugs

A continuación, se presentan los bugs identificados en el código proporcionado, junto con sus explicaciones y correcciones.

#### 1. División por cero si no hay órdenes pendientes

**Explicación:** El código calcula el promedio del precio final de las órdenes
```

</details>

#### structured_output

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| json_simple_extraction | 7.16 | 7.46 | 4.0 | 19 | 2.43s | OK |
| json_array_classification | 7.65 | 8.86 | 5 | 24 | 4.40s | OK |
| json_nested_complex | 7.01 | 8.02 | 4.4 | 39 | 13.04s | OK |
| json_strict_no_extra | 7.26 | 7.46 | 4.0 | 18 | 1.41s | OK |

<details><summary><code>json_simple_extraction</code> — score 7.16</summary>

**Stats**: latencia 2.43s · 19 tok/s · 111→47 tokens · $0.00025

**Juez Phi-4**: 4.0/10 (precisión:4, relevancia:5, profundidad:2, claridad:5, utilidad:3)

> La respuesta es precisa y relevante, con un formato claro y correcto; sin embargo, carece de profundidad adicional más allá de la extracción básica.

**Respuesta (preview 300 chars)**:

```
{"name": "Maria Garcia", "age": 28, "role": "ingeniera de software", "company": "Google Chile", "email": "maria@google.com", "salary": 95000}
```

</details>

<details><summary><code>json_array_classification</code> — score 7.65</summary>

**Stats**: latencia 4.40s · 24 tok/s · 172→104 tokens · $0.00048

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con un formato JSON correcto; proporciona una clasificación útil para la gestión de soporte al cliente.

**Respuesta (preview 300 chars)**:

```
[{"id": 1, "category": "shipping", "priority": "urgent", "sentiment": "negative"}, {"id": 2, "category": "shipping", "priority": "low", "sentiment": "neutral"}, {"id": 3, "category": "billing", "priority": "urgent", "sentiment": "negative"}, {"id": 4, "category": "technical", "priority": "high", "se
```

</details>

<details><summary><code>json_nested_complex</code> — score 7.01</summary>

**Stats**: latencia 13.04s · 39 tok/s · 215→508 tokens · $0.00174

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
  "project": "Rediseno sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {"name": "Ana Gomez", "role": "Disenador", "allocation_pct": 80},
    {"name": "Juan Perez", "role": "Desarrollador", "allocation_pct": 100},
    {"name": "Maria Rodriguez", "role": "Desarr
```

</details>

<details><summary><code>json_strict_no_extra</code> — score 7.26</summary>

**Stats**: latencia 1.41s · 18 tok/s · 85→25 tokens · $0.00016

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
| copy_hex_32 | 7.31 | 7.88 | 4.0 | 11 | 1.70s | OK |
| copy_hex_64 | 7.21 | 7.32 | 3.6 | 26 | 1.59s | OK |
| copy_api_key | 7.41 | 7.60 | 3.8 | 32 | 1.99s | OK |
| copy_jwt | 7.41 | 7.88 | 4.0 | 22 | 1.81s | OK |
| copy_mixed_special | 7.21 | 7.32 | 3.6 | 24 | 1.27s | OK |
| write_config_file | 7.41 | 7.88 | 4.0 | 41 | 4.59s | OK |

<details><summary><code>copy_hex_32</code> — score 7.31</summary>

**Stats**: latencia 1.70s · 11 tok/s · 92→19 tokens · $0.00015

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:1, claridad:5, utilidad:3)

> La respuesta es precisa, relevante y clara al copiar el string hex exactamente como se solicitó; sin embargo, carece de profundidad ya que no ofrece insights adicionales.

**Respuesta (preview 300 chars)**:

```
a1b2c3d4e5f6789012345678abcdef90
```

</details>

<details><summary><code>copy_hex_64</code> — score 7.21</summary>

**Stats**: latencia 1.59s · 26 tok/s · 115→42 tokens · $0.00024

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
9767a40b5b0ee1f7e3339a9859c582916ebb8d3df4ead5de1828c122c78a5a1b
```

</details>

<details><summary><code>copy_api_key</code> — score 7.41</summary>

**Stats**: latencia 1.99s · 32 tok/s · 140→64 tokens · $0.00033

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
sk-proj-X7kL9mN2pQ4rS6tU8vW0xY1zA3bC5dE7fG9hI1jK3lM5nO7pQ9rS1tU3vW5x
```

</details>

<details><summary><code>copy_jwt</code> — score 7.41</summary>

**Stats**: latencia 1.81s · 22 tok/s · 113→40 tokens · $0.00023

**Juez Phi-4**: 4.0/10 (precisión:5, relevancia:5, profundidad:1, claridad:5, utilidad:3)

> La respuesta es precisa, relevante y clara al copiar el string JWT exactamente como se solicitó; sin embargo, carece de profundidad ya que no ofrece insights adicionales.

**Respuesta (preview 300 chars)**:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkw
```

</details>

<details><summary><code>copy_mixed_special</code> — score 7.21</summary>

**Stats**: latencia 1.27s · 24 tok/s · 104→31 tokens · $0.00020

**Juez Phi-4**: 3.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
r2-secret_KEY.2024/abc+def==ghi&jkl#mno@pqr$stu%vwx^yza
```

</details>

<details><summary><code>write_config_file</code> — score 7.41</summary>

**Stats**: latencia 4.59s · 41 tok/s · 234→188 tokens · $0.00080

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
| invoice_extraction | 6.75 | 6.28 | 2.6 | 101 | 2.81s | OK |
| business_card_extraction | 7.53 | 8.21 | 4.4 | 30 | 4.78s | OK |
| receipt_math_verification | 6.84 | 7.55 | 4.4 | 48 | 21.91s | OK |
| screenshot_table_extraction | 6.76 | 8.16 | 3.8 | 41 | 46.42s | OK |
| handwritten_notes_extraction | 7.15 | 8.44 | 4.4 | 41 | 19.66s | OK |

<details><summary><code>invoice_extraction</code> — score 6.75</summary>

**Stats**: latencia 2.81s · 101 tok/s · 430→285 tokens · $0.00128

**Juez Phi-4**: 2.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
{
  "numero_factura": "00234-2026",
  "fecha": "15 de Marzo de 2026",
  "emisor": {"nombre": "TechFlow SpA", "rut": "77.432.198-3", "direccion": "Av. Providencia 1234, Of. 501, Santiago"},
  "cliente": {"nombre": "Startup Labs Ltda.", "rut": "76.891.234-K", "direccion": "Calle Moneda 920, Sa
```

</details>

<details><summary><code>business_card_extraction</code> — score 7.53</summary>

**Stats**: latencia 4.78s · 30 tok/s · 230→144 tokens · $0.00066

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
```json
{
  "nombre_completo": "Maria Jose Rodriguez Soto",
  "cargo": "Chief Technology Officer",
  "empresa": "NexaFlow Intelligence",
  "slogan": "Transforming Data into Decisions",
  "telefono": "+56 9 8765 4321",
  "email": "mj.rodriguez@nexaflow.ai",
  "linkedin": "linkedin.com/in/mjrodriguez"
```

</details>

<details><summary><code>receipt_math_verification</code> — score 6.84</summary>

**Stats**: latencia 21.91s · 48 tok/s · 319→1046 tokens · $0.00346

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Para resolver las tareas solicitadas, primero debemos procesar el recibo de restaurante proporcionado.

### Paso 1: Extraer todos los items con sus precios en JSON

Del recibo, podemos extraer los siguientes items con sus precios:

- 2x Lomo vetado: $18.900 c/u
- 1x Ensalada cesar: $7.500
- 3x Pisco
```

</details>

<details><summary><code>screenshot_table_extraction</code> — score 6.76</summary>

**Stats**: latencia 46.42s · 41 tok/s · 365→1898 tokens · $0.00606

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
### Extracción de Datos y Cálculos

#### Datos en Formato JSON

Primero, se extraen los datos de la captura de pantalla y se estructuran en formato JSON:

```json
{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "enero": 45200
```

</details>

<details><summary><code>handwritten_notes_extraction</code> — score 7.15</summary>

**Stats**: latencia 19.66s · 41 tok/s · 440→809 tokens · $0.00287

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
A continuación, te presento la respuesta en formato JSON:

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métr
```

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 7.27 | 8.76 | 4.4 | 34 | 18.93s | OK |
| email_profesional | 7.53 | 9.52 | 4.8 | 42 | 11.95s | OK |
| social_media_batch | 7.27 | 8.76 | 4.4 | 42 | 16.11s | OK |
| product_description_en | 7.29 | 8.12 | 4.8 | 29 | 6.71s | OK |

<details><summary><code>blog_post_es</code> — score 7.27</summary>

**Stats**: latencia 18.93s · 34 tok/s · 69→650 tokens · $0.00202

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Título:** "Revoluciona tu pequeña empresa con la automatización con IA: Eficiencia y competitividad al alcance de tu mano"

**Introducción:**
En el entorno empresarial actual, la competencia es feroz y las pequeñas empresas se enfrentan a numerosos desafíos para mantenerse a flote. Una de las herr
```

</details>

<details><summary><code>email_profesional</code> — score 7.53</summary>

**Stats**: latencia 11.95s · 42 tok/s · 81→501 tokens · $0.00158

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Asunto: Propuesta para el Desarrollo de Sitio Web Corporativo con E-commerce

Estimado/a \[Nombre del Cliente],

Espero que se encuentre bien. Agradezco su interés en nuestros servicios para el desarrollo de un sitio web corporativo con e-commerce. Me complace presentar a continuación nuestra propue
```

</details>

<details><summary><code>social_media_batch</code> — score 7.27</summary>

**Stats**: latencia 16.11s · 42 tok/s · 84→674 tokens · $0.00211

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
¡Claro! Aquí te dejo 5 posts para LinkedIn sobre transformación digital con diferentes tonos:

**Post 1: Educativo**
Hook: "¿Sabes qué es la transformación digital y por qué es crucial para tu negocio?"
Cuerpo: "La transformación digital implica la integración de tecnología digital en todos los aspe
```

</details>

<details><summary><code>product_description_en</code> — score 7.29</summary>

**Stats**: latencia 6.71s · 29 tok/s · 64→195 tokens · $0.00065

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**"Elevate Your Space with Aurora: The Ultimate Smart Home Companion"**

Take control of your home's atmosphere with Aurora, a cutting-edge device that seamlessly integrates a premium speaker, advanced air quality monitor, and soothing ambient light. Here are just a few ways Aurora can transform you
```

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 6.97 | 7.92 | 3.8 | 47 | 16.17s | OK |
| curso_emprendimiento_modulo | 7.40 | 9.44 | 4.6 | 30 | 29.87s | OK |
| workshop_outline | 7.56 | 8.88 | 4.2 | 111 | 8.26s | OK |
| newsletter_startup | 7.34 | 8.96 | 4.4 | 43 | 13.21s | OK |
| perplexity_style_research | 7.41 | 9.16 | 4.4 | 41 | 18.75s | OK |

<details><summary><code>blog_actualidad_startup</code> — score 6.97</summary>

**Stats**: latencia 16.17s · 47 tok/s · 218→755 tokens · $0.00248

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Título:** "IA Open-Source: Oportunidad para Startups en Latinoamérica"

**Meta descripción:** "Descubre cómo los modelos de IA open-source están revolucionando el ecosistema emprendedor en Latinoamérica y cómo las startups pueden aprovecharlos para crecer."

En el vertiginoso mundo de la tecnologí
```

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 7.40</summary>

**Stats**: latencia 29.87s · 30 tok/s · 223→882 tokens · $0.00287

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Módulo 3: Automatización con IA: De la idea al flujo de trabajo**
===========================================================

### Objetivo del Módulo

En este módulo, aprenderás a aprovechar el poder de la Inteligencia Artificial (IA) para automatizar procesos en tu startup, aumentando la eficien
```

</details>

<details><summary><code>workshop_outline</code> — score 7.56</summary>

**Stats**: latencia 8.26s · 111 tok/s · 192→914 tokens · $0.00293

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Construye tu Asistente de IA para tu Startup - Workshop Practico**

**Agenda Detallada (3 horas)**

1. **Introducción y Contexto** (15 minutos, 0:00 - 0:15)
2. **Fundamentos de IA para Negocios** (30 minutos, 0:15 - 0:45)
3. **Identificando Oportunidades de IA en tu Startup** (30 minutos, 0:45 - 1
```

</details>

<details><summary><code>newsletter_startup</code> — score 7.34</summary>

**Stats**: latencia 13.21s · 43 tok/s · 215→568 tokens · $0.00192

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Ecosistema Startup Newsletter #47: La IA sigue revolucionando el ecosistema emprendedor**

¡Hola! Esta semana traemos noticias emocionantes sobre los últimos avances en Inteligencia Artificial y cómo están impactando en el mundo de las startups.

### 🤖 DeepSeek V4: El nuevo estándar en modelos de
```

</details>

<details><summary><code>perplexity_style_research</code> — score 7.41</summary>

**Stats**: latencia 18.75s · 41 tok/s · 183→769 tokens · $0.00249

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Estado del Venture Capital en Latinoamérica Q1 2026**

### Resumen Ejecutivo

* El venture capital en Latinoamérica experimentó un crecimiento significativo en Q1 2026, impulsado por inversiones en startups de tecnología y fintech.
* Los países líderes en la región fueron Brasil, México y Argentin
```

</details>

#### news_seo_writing

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| news_seo_article_full | 6.87 | 7.64 | 3.8 | 44 | 18.82s | OK |
| news_json_output_strict | 6.42 | 6.34 | 3.2 | 41 | 10.34s | OK |
| news_spanish_only | 7.04 | 8.10 | 4.4 | 39 | 13.81s | OK |
| news_no_hallucination_sources | 6.43 | 6.36 | 3.8 | 41 | 13.94s | OK |
| news_perplexity_enrichment | 7.31 | 7.88 | 3.8 | 266 | 2.77s | OK |

<details><summary><code>news_seo_article_full</code> — score 6.87</summary>

**Stats**: latencia 18.82s · 44 tok/s · 451→833 tokens · $0.00295

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Mistral AI Obtiene $2 Mil Millones en Serie C y Lanza Devstral para Codificación

Meta descripción: Mistral AI cierra una ronda de financiamiento Serie C de $2 mil millones y lanza Devstral, un modelo de codificación de código abierto que supera a modelos de OpenAI y Google.

Palabras clave SEO s
```

</details>

<details><summary><code>news_json_output_strict</code> — score 6.42</summary>

**Stats**: latencia 10.34s · 41 tok/s · 311→424 tokens · $0.00158

**Juez Phi-4**: 3.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
{
"Fuentes": ["https://blog.google/technology/developers/google-deepmind-gemma-4/"],
"Categoria": "Inteligencia Artificial",
"Palabras_Clave": ["Gemma 4", "Google DeepMind", "AI", "open-source", "Apache 2.0"],
"Contenido_HTML": "<h2>Nuevo Modelo de Inteligencia Artificial</h2><p>Google DeepMind ha l
```

</details>

<details><summary><code>news_spanish_only</code> — score 7.04</summary>

**Stats**: latencia 13.81s · 39 tok/s · 307→538 tokens · $0.00192

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## SambaNova Systems Presenta el Chip SN50: Un Avance en la Eficiencia de la IA Empresarial

La empresa de tecnología SambaNova Systems ha anunciado recientemente el lanzamiento de su nuevo chip, el SN50, diseñado específicamente para cargas de trabajo de Inteligencia Artificial (IA) en entornos emp
```

</details>

<details><summary><code>news_no_hallucination_sources</code> — score 6.43</summary>

**Stats**: latencia 13.94s · 41 tok/s · 468→574 tokens · $0.00219

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## NotCo: La Startup Chilena que Revoluciona la Industria Alimentaria con $85 Millones en Ronda Serie D

La startup chilena NotCo acaba de cerrar una ronda de financiamiento Serie D por $85 millones, liderada por el fondo de inversión Tiger Global. Esta inyección de capital eleva la valuación de la
```

</details>

<details><summary><code>news_perplexity_enrichment</code> — score 7.31</summary>

**Stats**: latencia 2.77s · 266 tok/s · 479→736 tokens · $0.00269

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## DeepSeek lanza V4, su modelo de IA de código abierto más avanzado

La empresa china DeepSeek acaba de lanzar V4, su último modelo de inteligencia artificial (IA) de código abierto bajo la licencia MIT. Este nuevo modelo llega con una serie de mejoras significativas en cuanto a capacidad y costo,
```

</details>

#### creativity

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| creative_hook_writing | 7.47 | 8.34 | 4.4 | 38 | 6.71s | OK |
| analogy_generation | 7.19 | 8.53 | 4.8 | 34 | 14.12s | OK |
| depth_vs_superficial | 7.64 | 8.82 | 4.4 | 163 | 4.12s | OK |
| storytelling_quality | 7.74 | 8.26 | 4.4 | 75 | 1.94s | OK |

<details><summary><code>creative_hook_writing</code> — score 7.47</summary>

**Stats**: latencia 6.71s · 38 tok/s · 171→254 tokens · $0.00093

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
A continuación, te dejo los 5 hooks solicitados:

1. "La dependencia de modelos de IA propietarios está frenando el crecimiento de las startups latinoamericanas, y el open-source es la llave para desbloquear su verdadero potencial."
 
2. "La pandemia ha sido un acelerador involuntario del trabajo re
```

</details>

<details><summary><code>analogy_generation</code> — score 7.19</summary>

**Stats**: latencia 14.12s · 34 tok/s · 128→484 tokens · $0.00158

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
A continuación, te presento las analogías solicitadas:

**1. Como funciona un modelo de lenguaje (LLM)**
Un modelo de lenguaje es como un chef experto que ha probado y memorizado una infinidad de recetas y puede crear nuevas variaciones según los ingredientes que se le proporcionen. Al igual que el
```

</details>

<details><summary><code>depth_vs_superficial</code> — score 7.64</summary>

**Stats**: latencia 4.12s · 163 tok/s · 143→673 tokens · $0.00216

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Excelente decisión considerar la IA para tu startup de delivery de comida en Santiago. Para darte una respuesta más profunda, te presento algunas ideas específicas que podrían ser relevantes para tu negocio.

**Análisis de sentimiento y preferencias de los clientes**

Una forma de aprovechar la IA e
```

</details>

<details><summary><code>storytelling_quality</code> — score 7.74</summary>

**Stats**: latencia 1.94s · 75 tok/s · 158→146 tokens · $0.00060

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
"¡Ay, caramba!" exclamó Carlos, fundador de la startup de IA "Veritas". Mientras revisaba el código, descubrió que su algoritmo era demasiado honesto. En lugar de recomendar productos, decía la verdad: "Este no es para ti". Los clientes se iban, confundidos. Carlos intentó corregirlo, pero empeoró:
```

</details>

#### sales_outreach

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| cold_email_personalized | 7.79 | 8.96 | 4.8 | 34 | 3.54s | OK |
| lead_qualification | 7.34 | 8.96 | 4.8 | 45 | 12.75s | OK |
| campaign_optimization | 7.50 | 9.44 | 4.6 | 47 | 23.79s | OK |

<details><summary><code>cold_email_personalized</code> — score 7.79</summary>

**Stats**: latencia 3.54s · 34 tok/s · 181→120 tokens · $0.00054

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Asunto: ¿Cómo está funcionando tu estrategia de contenido desde la última vez que hablamos sobre escalar?

Me llamó la atención tu post en LinkedIn sobre escalar content marketing sin contratar más personal. Entiendo que es un desafío común en startups como FintechCo. Nuestra herramienta de automati
```

</details>

<details><summary><code>lead_qualification</code> — score 7.34</summary>

**Stats**: latencia 12.75s · 45 tok/s · 247→573 tokens · $0.00197

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí te dejo las calificaciones de los 3 leads:

**Lead 1: Juan Perez**

* Score: 6
* BANT:
	+ Budget: Desconocido
	+ Authority: Alta (CEO)
	+ Need: Posible (están viendo opciones para automatizar soporte)
	+ Timeline: Desconocido
* Action: Seguir conversando para entender mejor sus necesidades y pr
```

</details>

<details><summary><code>campaign_optimization</code> — score 7.50</summary>

**Stats**: latencia 23.79s · 47 tok/s · 263→1108 tokens · $0.00359

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Paso 1: Calcular CTR, CPC, CPA y conversión para cada campaña

Para calcular los indicadores solicitados, se utilizarán las siguientes fórmulas:
- CTR (Tasa de clics) = (Clicks / Impresiones) * 100
- CPC (Costo por clic) = Costo / Clicks
- CPA (Costo por adquisición) = Costo / Signups
- Tasa de c
```

</details>

#### translation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| translate_marketing_es_en | 7.84 | 9.40 | 5 | 26 | 2.34s | OK |
| translate_technical_en_es | 7.45 | 8.00 | 4.0 | 43 | 2.44s | OK |
| detect_language_issues | 7.27 | 8.78 | 4.8 | 42 | 12.40s | OK |

<details><summary><code>translate_marketing_es_en</code> — score 7.84</summary>

**Stats**: latencia 2.34s · 26 tok/s · 167→62 tokens · $0.00035

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La traducción es precisa, relevante y clara, manteniendo el tono cercano y energético adecuado para una audiencia americana. Ofrece insights útiles sobre la automatización de procesos tediosos, lo que es práctico para emprendedores.

**Respuesta (preview 300 chars)**:

```
"Stop wasting hours on tasks that AI can crush in seconds.
AutoFlow automates the grunt work so you can focus on what really drives your startup forward.

No coding required. No headaches. No excuses.

Over 500 LATAM startups are already on board. When do you join the fast lane?"
```

</details>

<details><summary><code>translate_technical_en_es</code> — score 7.45</summary>

**Stats**: latencia 2.44s · 43 tok/s · 151→106 tokens · $0.00047

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
"Para autenticar con la API, incluya su token Bearer en el encabezado Authorization. Los límites de velocidad están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si supera el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cu
```

</details>

<details><summary><code>detect_language_issues</code> — score 7.27</summary>

**Stats**: latencia 12.40s · 42 tok/s · 202→522 tokens · $0.00177

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Después de revisar el texto, te presento los resultados en formato JSON:

```json
{
  "problemas": [
    {
      "tipo": "spanglish",
      "texto": "leveraging",
      "correccion": "aprovechando" o "utilizando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
```

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 7.07 | 8.20 | 4.0 | 39 | 40.26s | OK |
| data_report | 7.53 | 9.52 | 4.8 | 40 | 19.08s | OK |

<details><summary><code>slide_outline</code> — score 7.07</summary>

**Stats**: latencia 40.26s · 39 tok/s · 132→1573 tokens · $0.00485

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
A continuación, te presento un posible outline para la presentación de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0" para el board de directores:

**Slide 1: Introducción**

* Título: "Estado del Proyecto Plataforma Digital 2.0"
* Bullet points:
 + Presentación del proyecto y su im
```

</details>

<details><summary><code>data_report</code> — score 7.53</summary>

**Stats**: latencia 19.08s · 40 tok/s · 149→764 tokens · $0.00244

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Reporte de Ventas Mensuales**
================================

### Tabla de Datos Mensuales

| Producto   | Ene ($K) | Feb ($K) | Mar ($K) | Abr ($K) | Total ($K) |
|------------|----------|----------|----------|----------|------------|
| Producto A | 45       | 52       | 48       | 61       | 2
```

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 3.10 | 0.00 | - | 0 | 0.36s | ERROR |
| multi_tool_sequential | 3.10 | 0.00 | - | 0 | 0.01s | ERROR |
| tool_with_reasoning | 3.10 | 0.00 | - | 0 | 0.02s | ERROR |
| no_tool_needed | 5.60 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>single_tool_calendar</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "create_calendar_event". To learn more about provider routing, visit: https://openrouter.ai/docs/guides...`

</details>

<details><summary><code>multi_tool_sequential</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "create_calendar_event". To learn more about provider routing, visit: https://openrouter.ai/docs/guides...`

</details>

<details><summary><code>tool_with_reasoning</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "create_calendar_event". To learn more about provider routing, visit: https://openrouter.ai/docs/guides...`

</details>

<details><summary><code>no_tool_needed</code> — score 5.60</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "create_calendar_event". To learn more about provider routing, visit: https://openrouter.ai/docs/guides...`

</details>

#### customer_support

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| angry_customer_refund | 3.10 | 0.00 | - | 0 | 0.05s | ERROR |
| ambiguous_issue_classification | 3.10 | 0.00 | - | 0 | 0.02s | ERROR |
| multi_issue_conversation | 3.10 | 0.00 | - | 0 | 0.02s | ERROR |
| social_engineering_attempt | 3.10 | 0.00 | - | 0 | 0.02s | ERROR |

<details><summary><code>angry_customer_refund</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "lookup_order". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/...`

</details>

<details><summary><code>ambiguous_issue_classification</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "lookup_order". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/...`

</details>

<details><summary><code>multi_issue_conversation</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "lookup_order". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/...`

</details>

<details><summary><code>social_engineering_attempt</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "lookup_order". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/...`

</details>

#### orchestration

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| multi_step_research_plan | 3.10 | 0.00 | - | 0 | 0.05s | ERROR |
| error_recovery_orchestration | 4.85 | 0.00 | - | 0 | 0.02s | ERROR |
| complex_workflow_decomposition | 3.80 | 2.00 | - | 0 | 0.01s | ERROR |
| tool_selection_precision | 3.38 | 0.80 | - | 0 | 0.01s | ERROR |
| parallel_vs_sequential_judgment | 4.85 | 0.00 | - | 0 | 0.02s | ERROR |

<details><summary><code>multi_step_research_plan</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "search_web". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/pr...`

</details>

<details><summary><code>error_recovery_orchestration</code> — score 4.85</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "search_web". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/pr...`

</details>

<details><summary><code>complex_workflow_decomposition</code> — score 3.80</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "search_web". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/pr...`

</details>

<details><summary><code>tool_selection_precision</code> — score 3.38</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "search_web". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/pr...`

</details>

<details><summary><code>parallel_vs_sequential_judgment</code> — score 4.85</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "search_web". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/routing/pr...`

</details>

#### multi_turn

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| content_iteration | 7.51 | 8.16 | 4.4 | 37 | 3.88s | OK |
| support_escalation | 6.41 | 5.32 | 2.6 | 31 | 5.31s | OK |
| requirements_change | 6.07 | 5.20 | 2.4 | 38 | 7.49s | OK |
| debugging_conversation | 7.48 | 8.37 | 4.8 | 104 | 4.79s | OK |

<details><summary><code>content_iteration</code> — score 7.51</summary>

**Stats**: latencia 3.88s · 37 tok/s · 227→142 tokens · $0.00065

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
## Tu equipo de soporte está ahogandose en tickets: cómo la IA puede salvar el dia

¿Alguna vez has visto a tu equipo de soporte al cliente trabajando hasta altas horas de la noche, respondiendo a la misma pregunta una y otra vez, mientras tú te preguntas cómo puedes mejorar la experiencia del clien
```

</details>

<details><summary><code>support_escalation</code> — score 6.41</summary>

**Stats**: latencia 5.31s · 31 tok/s · 361→165 tokens · $0.00086

**Juez Phi-4**: 2.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Entiendo que estás muy frustrada con la situación y que deseas resolver el problema de inmediato. Sin embargo, debo recordarte que nuestra política de reembolsos establece que solo se pueden realizar dentro de los primeros 30 días después de la compra.

Según mis registros, tu pago de $200 fue reali
```

</details>

<details><summary><code>requirements_change</code> — score 6.07</summary>

**Stats**: latencia 7.49s · 38 tok/s · 230→288 tokens · $0.00109

**Juez Phi-4**: 2.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Excelente elección! Notion es una herramienta muy útil para organizar datos. 

Aquí te dejo la estructura actualizada del workflow:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Filtro**: IF node para filtrar emails con 'propuesta' o 'cotización' en el asunto
3. **Extraer dato
```

</details>

<details><summary><code>debugging_conversation</code> — score 7.48</summary>

**Stats**: latencia 4.79s · 104 tok/s · 324→496 tokens · $0.00181

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Un loop de retry infinito es un problema clásico. La solución es implementar un retry con backoff y límite de intentos. Aquí te dejo una guía básica:

1. **Backoff exponencial**: En lugar de reintentar inmediatamente, espera un tiempo que aumenta exponencialmente entre cada intento. Por ejemplo:
```

</details>

#### policy_adherence

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| refund_policy_enforcement | 6.97 | 7.76 | 4.0 | 38 | 9.82s | OK |
| data_privacy_protection | 7.29 | 7.84 | 4.4 | 21 | 4.67s | OK |
| language_and_tone_rules | 7.06 | 6.88 | 3.8 | 36 | 4.63s | OK |
| scope_boundaries | 7.41 | 8.16 | 4.0 | 116 | 2.81s | OK |

<details><summary><code>refund_policy_enforcement</code> — score 6.97</summary>

**Stats**: latencia 9.82s · 38 tok/s · 257→377 tokens · $0.00139

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Lo siento mucho por la experiencia negativa que ha tenido con nuestro servicio. Entiendo su frustración y deseo de resolver el problema.

Sin embargo, debo informarle que nuestra política de reembolsos es clara y está diseñada para ser justa y transparente para todos nuestros clientes. Según nuestra
```

</details>

<details><summary><code>data_privacy_protection</code> — score 7.29</summary>

**Stats**: latencia 4.67s · 21 tok/s · 223→98 tokens · $0.00052

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Lo siento, Carlos. Como asistente virtual de FinanceApp, debo seguir las reglas de privacidad y seguridad establecidas. 

No puedo confirmar si el correo electrónico pedro.martinez@empresa.cl está registrado en nuestro sistema. Tampoco puedo proporcionar información sobre saldos o transacciones de n
```

</details>

<details><summary><code>language_and_tone_rules</code> — score 7.06</summary>

**Stats**: latencia 4.63s · 36 tok/s · 200→166 tokens · $0.00070

**Juez Phi-4**: 3.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
¡Hola! Me alegra que te interese EcoStartup. Aunque preferimos comunicarnos en español, te puedo dar una idea general de nuestro programa. 

EcoStartup es una aceleradora de startups sustentables que busca impulsar negocios que tengan un impacto ambiental positivo en Chile. Nuestro programa ofrece m
```

</details>

<details><summary><code>scope_boundaries</code> — score 7.41</summary>

**Stats**: latencia 2.81s · 116 tok/s · 252→327 tokens · $0.00123

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
¡Claro! Me alegra poder ayudarte.

1. **Precio del plan Pro**: El precio del plan Pro es de $149/mes.

2. **Configuración de workflow de N8N**: Puedo ayudarte a entender cómo funciona el nodo de HTTP Request y darte algunas pautas generales. Sin embargo, para una ayuda más detallada y específica, te
```

</details>

#### agent_capabilities

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| skill_execution_complex | 3.10 | 0.00 | - | 0 | 0.03s | ERROR |
| agent_team_delegation | 3.10 | 0.00 | - | 0 | 0.02s | ERROR |
| ask_clarification_before_acting | 3.10 | 0.00 | - | 0 | 0.02s | ERROR |
| context_following_complex_system | 3.10 | 0.00 | - | 0 | 0.02s | ERROR |
| model_as_router | 7.32 | 8.92 | 4.4 | 38 | 10.41s | OK |

<details><summary><code>skill_execution_complex</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "delegate_to_agent". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/rou...`

</details>

<details><summary><code>agent_team_delegation</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "delegate_to_agent". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/rou...`

</details>

<details><summary><code>ask_clarification_before_acting</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "delegate_to_agent". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/rou...`

</details>

<details><summary><code>context_following_complex_system</code> — score 3.10</summary>

**Error**: `Error code: 404 - {'error': {'message': 'No endpoints found that support tool use. Try disabling "delegate_to_agent". To learn more about provider routing, visit: https://openrouter.ai/docs/guides/rou...`

</details>

<details><summary><code>model_as_router</code> — score 7.32</summary>

**Stats**: latencia 10.41s · 38 tok/s · 264→390 tokens · $0.00143

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí te dejo mis recomendaciones en formato JSON array:

[
  {"subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales", "modelo": "claude-sonnet", "razon": "Requiere empatia y comprensión del lenguaje para analizar reviews y extraer problemas"},
  {"subtarea": "Escribir u
```

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 7.55 | 8.56 | 4.4 | 43 | 5.77s | OK |
| weekly_planning | 7.17 | 8.48 | 4.2 | 41 | 24.66s | OK |
| project_breakdown | 7.43 | 9.24 | 4.6 | 35 | 23.08s | OK |

<details><summary><code>extract_action_items</code> — score 7.55</summary>

**Stats**: latencia 5.77s · 43 tok/s · 198→247 tokens · $0.00094

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
| Responsable | Tarea | Fecha Límite | Prioridad Sugerida |
| --- | --- | --- | --- |
| Carlos | Terminar el API de pagos | 20 abril 2026 | Alta |
| Ana | Entregar mockups del dashboard | 14 abril 2026 | Media |
| Pedro | Escribir tests para el módulo de autenticación | Sin fecha específica (esta se
```

</details>

<details><summary><code>weekly_planning</code> — score 7.17</summary>

**Stats**: latencia 24.66s · 41 tok/s · 196→1019 tokens · $0.00325

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Plan Semanal Detallado**

A continuación, te presento un plan semanal detallado que tiene en cuenta tus restricciones y tareas.

**Lunes**

* 8:00 AM - 9:00 AM: Responder emails de stakeholders (1 hora)
* 9:00 AM - 11:00 AM: Reunión de directivos (no disponible)
* 11:00 AM - 12:00 PM: Revisar PRDs
```

</details>

<details><summary><code>project_breakdown</code> — score 7.43</summary>

**Stats**: latencia 23.08s · 35 tok/s · 72→805 tokens · $0.00249

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Proyecto: Lanzamiento de Landing Page para SaaS de Gestión de Inventario**

**Fases y Tareas**

1. **Fase 1: Planificación y Requisitos (Semana 1)**
 * Tareas:
 + Definir objetivos y alcance del proyecto (Responsable: Jefe de Proyecto/Producto)
 + Identificar el público objetivo y sus necesidades
```

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 6.98 | 7.80 | 4.0 | 34 | 8.12s | OK |
| extract_structured_data | 6.46 | 6.32 | 2.8 | 38 | 9.41s | OK |

<details><summary><code>long_document_summary</code> — score 6.98</summary>

**Stats**: latencia 8.12s · 34 tok/s · 417→280 tokens · $0.00126

**Juez Phi-4**: 4.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Resumen Ejecutivo Q1 2026 - TechFlow**

**Metricas Clave:**

* Ventas: $2.3M (18% incremento respecto a Q4 2025)
* Crecimiento segmento enterprise: 32%
* NPS: 48 (subió de 42)
* Burn rate mensual: $380K
* Runway: 14 meses

**Logros:**

* Lanzamiento de 47 features nuevas, incluyendo el módulo de I
```

</details>

<details><summary><code>extract_structured_data</code> — score 6.46</summary>

**Stats**: latencia 9.41s · 38 tok/s · 260→358 tokens · $0.00133

**Juez Phi-4**: 2.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí está la información extraída de los 3 perfiles de candidatos en formato JSON:

```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Ingeniera de software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "sal
```

</details>
