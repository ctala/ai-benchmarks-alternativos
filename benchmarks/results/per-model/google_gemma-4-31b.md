# Gemma 4 31B

- **model_id**: `google/gemma-4-31b`
- **Total tests**: 87/123 exitosos (36 errores)
- **Score final**: 6.41
- **Calidad**: 7.68
- **Judge score (Phi-4)**: 1/10
- **Velocidad**: 8 tok/s
- **Latencia primera token**: 30.97s
- **Costo promedio por test**: $0.01135

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| agent_long_horizon | 12 | 12 | 7.44 | 9.25 |
| code_generation | 4 | 0 | - | - |
| content_generation | 8 | 3 | 6.60 | 7.00 |
| niah_es | 51 | 45 | 7.20 | 9.93 |
| presentation | 2 | 0 | - | - |
| prompt_injection_es | 20 | 20 | 3.74 | 1.82 |
| reasoning | 3 | 0 | - | - |
| startup_content | 10 | 4 | 7.81 | 9.55 |
| summarization | 2 | 0 | - | - |
| task_management | 3 | 0 | - | - |
| tool_calling | 8 | 3 | 6.15 | 5.00 |

## Detalle por test

### Razonamiento y Estrategia

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| logical_reasoning | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| multi_constraint_decision | 5.70 | 0.00 | - | 0 | 0.03s | ERROR |

<details><summary><code>business_analysis</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>logical_reasoning</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>multi_constraint_decision</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 6.20 | 2.00 | - | 0 | 0.03s | ERROR |
| n8n_workflow_json | 6.20 | 2.00 | - | 0 | 0.02s | ERROR |
| sql_query_complex | 6.20 | 2.00 | - | 0 | 0.03s | ERROR |
| debug_code | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |

<details><summary><code>python_api_integration</code> — score 6.20</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>n8n_workflow_json</code> — score 6.20</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>sql_query_complex</code> — score 6.20</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>debug_code</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 5.70 | 0.00 | - | 0 | 0.47s | ERROR |
| email_profesional | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| social_media_batch | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| product_description_en | 6.20 | 2.00 | - | 0 | 0.02s | ERROR |
| blog_post_es | 6.08 | 6.00 | - | 10 | 72.13s | OK |
| email_profesional | 7.95 | 10.00 | - | 10 | 117.54s | OK |
| social_media_batch | 5.70 | 0.00 | - | 0 | 138.00s | ERROR |
| product_description_en | 5.78 | 5.00 | - | 8 | 27.14s | OK |

<details><summary><code>blog_post_es</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>email_profesional</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>social_media_batch</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>product_description_en</code> — score 6.20</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>blog_post_es</code> — score 6.08</summary>

**Stats**: latencia 72.13s · 10 tok/s · 87→706 tokens · $0.00045

**Respuesta (preview 300 chars)**:

```
Aquí tienes una propuesta de blog post optimizada, con un tono profesional, cercano y persuasivo, diseñada para atraer a dueños de negocios.

***

# Impulsa tu Crecimiento: Ventajas de la Automatización con IA para Pequeñas Empresas

En el competitivo ecosistema empresarial actual, el tiempo es el r
```

</details>

<details><summary><code>email_profesional</code> — score 7.95</summary>

**Stats**: latencia 117.54s · 10 tok/s · 99→1218 tokens · $0.00076

**Respuesta (preview 300 chars)**:

```
Aquí tienes tres opciones dependiendo del nivel de confianza que tengas con el cliente: una **formal**, una **ejecutiva/directa** y una más **cercana/moderna**.

### Opción 1: Formal y Detallada
*Ideal para clientes corporativos, instituciones o clientes nuevos donde se quiere proyectar máxima serie
```

</details>

<details><summary><code>social_media_batch</code> — score 5.70</summary>

**Error**: `'NoneType' object is not subscriptable`

</details>

<details><summary><code>product_description_en</code> — score 5.78</summary>

**Stats**: latencia 27.14s · 8 tok/s · 67→231 tokens · $0.00016

**Respuesta (preview 300 chars)**:

```
**Meet Aura: Your Home’s New Sixth Sense**

Upgrade your living space with Aura, the all-in-one sanctuary hub designed for the modern minimalist. Why clutter your counters with gadgets when one sleek device can master your environment?

**Elevate Your Atmosphere**
*   **Immersive Sonic Experience:**
```

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| curso_emprendimiento_modulo | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| workshop_outline | 5.70 | 0.00 | - | 0 | 0.03s | ERROR |
| newsletter_startup | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| perplexity_style_research | 5.70 | 0.00 | - | 0 | 0.03s | ERROR |
| blog_actualidad_startup | 5.70 | 0.00 | - | 0 | 16.87s | ERROR |
| curso_emprendimiento_modulo | 7.74 | 9.40 | - | 20 | 72.16s | OK |
| workshop_outline | 8.03 | 10.00 | - | 16 | 97.42s | OK |
| newsletter_startup | 8.00 | 10.00 | - | 12 | 73.45s | OK |
| perplexity_style_research | 7.49 | 8.80 | - | 27 | 44.45s | OK |

<details><summary><code>blog_actualidad_startup</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>workshop_outline</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>newsletter_startup</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>perplexity_style_research</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>blog_actualidad_startup</code> — score 5.70</summary>

**Error**: `'NoneType' object is not subscriptable`

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 7.74</summary>

**Stats**: latencia 72.16s · 20 tok/s · 250→1460 tokens · $0.00095

**Respuesta (preview 300 chars)**:

```
# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

## 1. Objetivo del Módulo
Al finalizar este módulo, el emprendedor será capaz de identificar procesos repetitivos en su negocio y diseñar flujos de trabajo automatizados que integren Inteligencia Artificial. El objetivo es pasar de e
```

</details>

<details><summary><code>workshop_outline</code> — score 8.03</summary>

**Stats**: latencia 97.42s · 16 tok/s · 218→1540 tokens · $0.00099

**Respuesta (preview 300 chars)**:

```
¡Hola! Como facilitador, sé que con emprendedores no-técnicos el mayor riesgo es que se sientan abrumados por la tecnología o que sientan que es "magia" inalcanzable. 

El enfoque de este workshop es **"No-Code & Value-First"**. No vamos a escribir Python; vamos a diseñar flujos de valor y configura
```

</details>

<details><summary><code>newsletter_startup</code> — score 8.00</summary>

**Stats**: latencia 73.45s · 12 tok/s · 238→911 tokens · $0.00062

**Respuesta (preview 300 chars)**:

```
Aquí tienes la propuesta para la edición #47 del newsletter.

***

# 🚀 Ecosistema Startup #47: La guerra de los modelos y el impulso Deep Tech

**Hola, emprendedor/a,**

Bienvenidos a una nueva edición. Esta semana el tablero de la IA se ha movido más rápido que nunca con lanzamientos que obligan a
```

</details>

<details><summary><code>perplexity_style_research</code> — score 7.49</summary>

**Stats**: latencia 44.45s · 27 tok/s · 203→1219 tokens · $0.00079

**Respuesta (preview 300 chars)**:

```
***Nota importante:** Dado que actualmente nos encontramos en 2024, la información para el **Q1 2026** es una **proyección basada en tendencias actuales, ciclos de mercado y análisis predictivos**. A continuación, presento la investigación estructurada como un reporte de prospectiva económica.*

---
```

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 5.70 | 0.00 | - | 0 | 0.03s | ERROR |
| data_report | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |

<details><summary><code>slide_outline</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>data_report</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 4.30 | 0.00 | - | 0 | 0.03s | ERROR |
| multi_tool_sequential | 4.30 | 0.00 | - | 0 | 0.03s | ERROR |
| tool_with_reasoning | 4.30 | 0.00 | - | 0 | 0.02s | ERROR |
| no_tool_needed | 6.30 | 0.00 | - | 0 | 0.02s | ERROR |
| single_tool_calendar | 6.15 | 5.00 | - | 2 | 26.05s | OK |
| multi_tool_sequential | 6.15 | 5.00 | - | 2 | 50.39s | OK |
| tool_with_reasoning | 4.30 | 0.00 | - | 0 | 11.91s | ERROR |
| no_tool_needed | 6.15 | 5.00 | - | 0 | 30.88s | OK |

<details><summary><code>single_tool_calendar</code> — score 4.30</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>multi_tool_sequential</code> — score 4.30</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>tool_with_reasoning</code> — score 4.30</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>no_tool_needed</code> — score 6.30</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>tool_with_reasoning</code> — score 4.30</summary>

**Error**: `Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it is temporarily rate-limited upstream. Please retry shortly, or add your own k...`

</details>

<details><summary><code>no_tool_needed</code> — score 6.15</summary>

**Stats**: latencia 30.88s · 0 tok/s · 429→8 tokens · $0.00013

**Respuesta (preview 300 chars)**:

```
La capital de Francia es París.
```

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| weekly_planning | 5.70 | 0.00 | - | 0 | 0.02s | ERROR |
| project_breakdown | 5.70 | 0.00 | - | 0 | 0.03s | ERROR |

<details><summary><code>extract_action_items</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>weekly_planning</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>project_breakdown</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 5.70 | 0.00 | - | 0 | 0.03s | ERROR |
| extract_structured_data | 6.20 | 2.00 | - | 0 | 0.02s | ERROR |

<details><summary><code>long_document_summary</code> — score 5.70</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>extract_structured_data</code> — score 6.20</summary>

**Error**: `Error code: 400 - {'error': {'message': 'google/gemma-4-31b is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

### Otras suites

#### agent_long_horizon

#### niah_es

#### prompt_injection_es
