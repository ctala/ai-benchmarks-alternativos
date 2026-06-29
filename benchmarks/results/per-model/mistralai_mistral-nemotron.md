# Mistral-Nemotron (NIM)

- **model_id**: `mistralai/mistral-nemotron`
- **Total tests**: 12/91 exitosos (79 errores)
- **Score final**: 7.30
- **Calidad**: 8.04
- **Judge score (Phi-4)**: 4.10/10
- **Velocidad**: 38 tok/s
- **Latencia primera token**: 19.95s
- **Costo promedio por test**: $0.00066

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| agent_capabilities | 5 | 0 | - | - |
| code_generation | 4 | 1 | 8.17 | 9.72 |
| content_generation | 4 | 4 | 7.96 | 9.25 |
| creativity | 4 | 0 | - | - |
| customer_support | 4 | 0 | - | - |
| deep_reasoning | 6 | 0 | - | - |
| hallucination | 3 | 0 | - | - |
| multi_turn | 4 | 0 | - | - |
| news_seo_writing | 5 | 0 | - | - |
| ocr_extraction | 5 | 0 | - | - |
| orchestration | 5 | 0 | - | - |
| policy_adherence | 4 | 0 | - | - |
| presentation | 2 | 0 | - | - |
| reasoning | 3 | 0 | - | - |
| sales_outreach | 3 | 0 | - | - |
| startup_content | 5 | 0 | - | - |
| strategy | 3 | 0 | - | - |
| string_precision | 6 | 0 | - | - |
| structured_output | 4 | 0 | - | - |
| summarization | 2 | 0 | - | - |
| task_management | 3 | 3 | 7.90 | 8.99 |
| tool_calling | 4 | 4 | 5.96 | 5.70 |
| translation | 3 | 0 | - | - |

## Detalle por test

### Razonamiento y Estrategia

#### deep_reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| math_word_problem | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| logic_puzzle_constraint | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| causal_reasoning | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| code_bug_subtle | 4.85 | 0.00 | - | 0 | 0.16s | ERROR |
| fermi_estimation | 4.85 | 0.00 | - | 0 | 0.16s | ERROR |
| ethical_dilemma_structured | 4.85 | 0.00 | - | 0 | 0.24s | ERROR |

<details><summary><code>math_word_problem</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>logic_puzzle_constraint</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>causal_reasoning</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>code_bug_subtle</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>fermi_estimation</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>ethical_dilemma_structured</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 4.85 | 0.00 | - | 0 | 242.07s | ERROR |
| logical_reasoning | 4.85 | 0.00 | - | 0 | 0.54s | ERROR |
| multi_constraint_decision | 4.85 | 0.00 | - | 0 | 0.16s | ERROR |

<details><summary><code>business_analysis</code> — score 4.85</summary>

**Error**: `Request timed out.`

</details>

<details><summary><code>logical_reasoning</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>multi_constraint_decision</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### hallucination

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| factual_trap_companies | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| context_faithfulness | 4.85 | 0.00 | - | 0 | 0.21s | ERROR |
| fake_citation_trap | 5.27 | 1.20 | - | 0 | 0.15s | ERROR |

<details><summary><code>factual_trap_companies</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>context_faithfulness</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>fake_citation_trap</code> — score 5.27</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### strategy

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| competitor_analysis | 4.85 | 0.00 | - | 0 | 0.14s | ERROR |
| pricing_strategy | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| business_model_validation | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>competitor_analysis</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>pricing_strategy</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>business_model_validation</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 8.17 | 9.72 | 4.8 | 52 | 16.21s | OK |
| n8n_workflow_json | 5.55 | 2.00 | - | 0 | 316.94s | ERROR |
| sql_query_complex | 5.55 | 2.00 | - | 0 | 2.32s | ERROR |
| debug_code | 4.85 | 0.00 | - | 0 | 13.49s | ERROR |

<details><summary><code>python_api_integration</code> — score 8.17</summary>

**Stats**: latencia 16.21s · 52 tok/s · 105→852 tokens · $0.00105

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí tienes una función Python que cumple con todos los requisitos usando `httpx` con manejo de errores, retries con backoff exponencial y filtros de productos:

```python
import httpx
import time
import random
from typing import List, Dict

async def get_expensive_products(bearer_token: str) -> Lis
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__code_generation__python_api_integration.md`](../results/responses/20260425_145813/nim-mistral-nemotron__code_generation__python_api_integration.md)

</details>

<details><summary><code>n8n_workflow_json</code> — score 5.55</summary>

**Error**: `Error code: 500`

</details>

<details><summary><code>sql_query_complex</code> — score 5.55</summary>

**Error**: `Error code: 500 - {'type': 'urn:inference-connection:problem-details:internal-server-error', 'title': 'Internal Server Error', 'status': 500, 'detail': 'Inference connection error while making inferen...`

</details>

<details><summary><code>debug_code</code> — score 4.85</summary>

**Error**: `Error code: 500 - {'type': 'urn:inference-connection:problem-details:internal-server-error', 'title': 'Internal Server Error', 'status': 500, 'detail': 'Inference connection error while making inferen...`

</details>

#### structured_output

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| json_simple_extraction | 6.18 | 3.80 | - | 0 | 0.14s | ERROR |
| json_array_classification | 6.18 | 3.80 | - | 0 | 0.15s | ERROR |
| json_nested_complex | 6.18 | 3.80 | - | 0 | 0.15s | ERROR |
| json_strict_no_extra | 6.18 | 3.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>json_simple_extraction</code> — score 6.18</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>json_array_classification</code> — score 6.18</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>json_nested_complex</code> — score 6.18</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>json_strict_no_extra</code> — score 6.18</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### string_precision

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| copy_hex_32 | 5.34 | 1.40 | - | 0 | 0.15s | ERROR |
| copy_hex_64 | 5.34 | 1.40 | - | 0 | 0.15s | ERROR |
| copy_api_key | 5.34 | 1.40 | - | 0 | 0.15s | ERROR |
| copy_jwt | 5.34 | 1.40 | - | 0 | 0.15s | ERROR |
| copy_mixed_special | 5.34 | 1.40 | - | 0 | 0.15s | ERROR |
| write_config_file | 5.13 | 0.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>copy_hex_32</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>copy_hex_64</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>copy_api_key</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>copy_jwt</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>copy_mixed_special</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>write_config_file</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### ocr_extraction

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| invoice_extraction | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| business_card_extraction | 5.13 | 0.80 | - | 0 | 0.16s | ERROR |
| receipt_math_verification | 5.13 | 0.80 | - | 0 | 0.22s | ERROR |
| screenshot_table_extraction | 5.13 | 0.80 | - | 0 | 0.14s | ERROR |
| handwritten_notes_extraction | 5.13 | 0.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>invoice_extraction</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>business_card_extraction</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>receipt_math_verification</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>screenshot_table_extraction</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>handwritten_notes_extraction</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 7.13 | 8.56 | 4.4 | 6 | 143.23s | OK |
| email_profesional | 8.28 | 9.72 | 4.8 | 51 | 10.99s | OK |
| social_media_batch | 7.80 | 8.92 | 4.8 | 54 | 14.24s | OK |
| product_description_en | 8.64 | 9.80 | 5 | 46 | 4.47s | OK |

<details><summary><code>blog_post_es</code> — score 7.13</summary>

**Stats**: latencia 143.23s · 6 tok/s · 65→901 tokens · $0.00110

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Cómo la Automatización con IA Puede Transformar tu Pequeña Empresa**

**Introducción**

En un mundo empresarial cada vez más competitivo, las pequeñas empresas buscan herramientas para mejorar su eficiencia, reducir costos y escalar sin aumentar drásticamente sus recursos. La automatización con in
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__content_generation__blog_post_es.md`](../results/responses/20260425_145813/nim-mistral-nemotron__content_generation__blog_post_es.md)

</details>

<details><summary><code>email_profesional</code> — score 8.28</summary>

**Stats**: latencia 10.99s · 51 tok/s · 79→562 tokens · $0.00070

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Asunto:** Propuesta para Desarrollo de Sitio Web Corporativo con E-Commerce

**Estimado/a [Nombre del Cliente],**

Es un placer presentarle nuestra propuesta para el desarrollo del sitio web corporativo con funcionalidades de e-commerce, tal como solicitó. En [Nombre de su Empresa], nos compromete
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__content_generation__email_profesional.md`](../results/responses/20260425_145813/nim-mistral-nemotron__content_generation__email_profesional.md)

</details>

<details><summary><code>social_media_batch</code> — score 7.80</summary>

**Stats**: latencia 14.24s · 54 tok/s · 77→767 tokens · $0.00094

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
### **Post 1 – Educativo**
**Hook:** "¿Sabías que el 90% de las empresas que no adoptan la transformación digital desaparecerán en 5 años? 🌍📈"

**Cuerpo:**
La digitalización ya no es una opción, es una necesidad. Desde automatización de procesos hasta inteligencia artificial, las empresas que se que
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__content_generation__social_media_batch.md`](../results/responses/20260425_145813/nim-mistral-nemotron__content_generation__social_media_batch.md)

</details>

<details><summary><code>product_description_en</code> — score 8.64</summary>

**Stats**: latencia 4.47s · 46 tok/s · 60→208 tokens · $0.00027

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con una estructura bien organizada que incluye un titular atractivo, características clave y un cierre convincente. Ofrece insights útiles para emprendedores al destacar beneficios específicos del producto.

**Respuesta (preview 300 chars)**:

```
**Headline:**
**Meet Pulse: The All-in-One Smart Home Hub for a Healthier, Smarter You**

**Key Features & Benefits:**
1. **Crystal-Clear Audio with Smart Voice Control** – Enjoy rich, immersive sound for music, podcasts, and calls, plus hands-free access to your favorite voice assistant. Perfect fo
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__content_generation__product_description_en.md`](../results/responses/20260425_145813/nim-mistral-nemotron__content_generation__product_description_en.md)

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| curso_emprendimiento_modulo | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| workshop_outline | 4.85 | 0.00 | - | 0 | 0.14s | ERROR |
| newsletter_startup | 4.85 | 0.00 | - | 0 | 0.20s | ERROR |
| perplexity_style_research | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>blog_actualidad_startup</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>workshop_outline</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>newsletter_startup</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>perplexity_style_research</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### news_seo_writing

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| news_seo_article_full | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| news_json_output_strict | 5.90 | 3.00 | - | 0 | 0.15s | ERROR |
| news_spanish_only | 5.90 | 3.00 | - | 0 | 0.15s | ERROR |
| news_no_hallucination_sources | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| news_perplexity_enrichment | 4.85 | 0.00 | - | 0 | 0.25s | ERROR |

<details><summary><code>news_seo_article_full</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>news_json_output_strict</code> — score 5.90</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>news_spanish_only</code> — score 5.90</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>news_no_hallucination_sources</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>news_perplexity_enrichment</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### creativity

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| creative_hook_writing | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |
| analogy_generation | 6.53 | 4.80 | - | 0 | 0.16s | ERROR |
| depth_vs_superficial | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |
| storytelling_quality | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>creative_hook_writing</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>analogy_generation</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>depth_vs_superficial</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>storytelling_quality</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### sales_outreach

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| cold_email_personalized | 6.53 | 4.80 | - | 0 | 0.20s | ERROR |
| lead_qualification | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| campaign_optimization | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>cold_email_personalized</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>lead_qualification</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>campaign_optimization</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### translation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| translate_marketing_es_en | 6.81 | 5.60 | - | 0 | 0.15s | ERROR |
| translate_technical_en_es | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| detect_language_issues | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>translate_marketing_es_en</code> — score 6.81</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>translate_technical_en_es</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>detect_language_issues</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 4.85 | 0.00 | - | 0 | 0.17s | ERROR |
| data_report | 4.85 | 0.00 | - | 0 | 0.17s | ERROR |

<details><summary><code>slide_outline</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>data_report</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 4.90 | 4.30 | 2.0 | 20 | 1.17s | OK |
| multi_tool_sequential | 5.80 | 6.26 | 3.4 | 40 | 2.45s | OK |
| tool_with_reasoning | 5.74 | 5.98 | 3.2 | 28 | 1.30s | OK |
| no_tool_needed | 7.38 | 6.26 | 3.4 | 10 | 0.76s | OK |

<details><summary><code>single_tool_calendar</code> — score 4.90</summary>

**Stats**: latencia 1.17s · 20 tok/s · 532→23 tokens · $0.00019

**Juez Phi-4**: 2.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Para agendar la reunión de proyecto, necesito la descripción del evento. ¿Podrías proporcionarla?
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__tool_calling__single_tool_calendar.md`](../results/responses/20260425_145813/nim-mistral-nemotron__tool_calling__single_tool_calendar.md)

</details>

<details><summary><code>multi_tool_sequential</code> — score 5.80</summary>

**Stats**: latencia 2.45s · 40 tok/s · 565→99 tokens · $0.00029

**Juez Phi-4**: 3.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Para realizar las tareas solicitadas, necesito confirmar algunos detalles adicionales:

1. Para la creación de la tarea:
   - ¿Quieres especificar a quién asignar esta tarea?

2. Para el envío del correo electrónico:
   - ¿Qué información específica del contrato o detalles adicionales deseas incluir
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__tool_calling__multi_tool_sequential.md`](../results/responses/20260425_145813/nim-mistral-nemotron__tool_calling__multi_tool_sequential.md)

</details>

<details><summary><code>tool_with_reasoning</code> — score 5.74</summary>

**Stats**: latencia 1.30s · 28 tok/s · 559→36 tokens · $0.00021

**Juez Phi-4**: 3.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Entendido. Crearé un recordatorio para hoy a las 5 PM para repasar las slides y buscaré en la web las mejores prácticas para presentaciones ejecutivas.
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__tool_calling__tool_with_reasoning.md`](../results/responses/20260425_145813/nim-mistral-nemotron__tool_calling__tool_with_reasoning.md)

</details>

<details><summary><code>no_tool_needed</code> — score 7.38</summary>

**Stats**: latencia 0.76s · 10 tok/s · 494→8 tokens · $0.00016

**Juez Phi-4**: 3.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
La capital de Francia es París.
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__tool_calling__no_tool_needed.md`](../results/responses/20260425_145813/nim-mistral-nemotron__tool_calling__no_tool_needed.md)

</details>

#### customer_support

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| angry_customer_refund | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| ambiguous_issue_classification | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| multi_issue_conversation | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| social_engineering_attempt | 3.10 | 0.00 | - | 0 | 0.17s | ERROR |

<details><summary><code>angry_customer_refund</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>ambiguous_issue_classification</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>multi_issue_conversation</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>social_engineering_attempt</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### orchestration

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| multi_step_research_plan | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| error_recovery_orchestration | 4.85 | 0.00 | - | 0 | 0.18s | ERROR |
| complex_workflow_decomposition | 3.80 | 2.00 | - | 0 | 0.17s | ERROR |
| tool_selection_precision | 3.38 | 0.80 | - | 0 | 0.15s | ERROR |
| parallel_vs_sequential_judgment | 4.85 | 0.00 | - | 0 | 0.20s | ERROR |

<details><summary><code>multi_step_research_plan</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>error_recovery_orchestration</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>complex_workflow_decomposition</code> — score 3.80</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>tool_selection_precision</code> — score 3.38</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>parallel_vs_sequential_judgment</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### multi_turn

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| content_iteration | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |
| support_escalation | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| requirements_change | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| debugging_conversation | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>content_iteration</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>support_escalation</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>requirements_change</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>debugging_conversation</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### policy_adherence

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| refund_policy_enforcement | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| data_privacy_protection | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| language_and_tone_rules | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| scope_boundaries | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>refund_policy_enforcement</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>data_privacy_protection</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>language_and_tone_rules</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>scope_boundaries</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### agent_capabilities

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| skill_execution_complex | 3.10 | 0.00 | - | 0 | 0.31s | ERROR |
| agent_team_delegation | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| ask_clarification_before_acting | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| context_following_complex_system | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| model_as_router | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>skill_execution_complex</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>agent_team_delegation</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>ask_clarification_before_acting</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>context_following_complex_system</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>model_as_router</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 7.88 | 8.28 | 4.2 | 45 | 3.96s | OK |
| weekly_planning | 7.86 | 9.24 | 4.6 | 54 | 20.19s | OK |
| project_breakdown | 7.97 | 9.44 | 4.6 | 53 | 20.44s | OK |

<details><summary><code>extract_action_items</code> — score 7.88</summary>

**Stats**: latencia 3.96s · 45 tok/s · 202→177 tokens · $0.00027

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí tienes la tabla con los **action items** extraídos de las notas de la reunión:

| **Responsable** | **Tarea**                                      | **Fecha límite** | **Prioridad sugerida** |
|-----------------|------------------------------------------------|------------------|---------------
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__task_management__extract_action_items.md`](../results/responses/20260425_145813/nim-mistral-nemotron__task_management__extract_action_items.md)

</details>

<details><summary><code>weekly_planning</code> — score 7.86</summary>

**Stats**: latencia 20.19s · 54 tok/s · 205→1085 tokens · $0.00136

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí tienes un plan semanal detallado que distribuye las tareas según tus restricciones y prioridades, optimizando el tiempo disponible:

### **Lunes**
- **9:00–11:00 AM**: Reunión de directivos (fija)
- **11:00–12:00 PM**: Revisar métricas del producto (**1h**)
- **12:00–1:00 PM**: Preparar present
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__task_management__weekly_planning.md`](../results/responses/20260425_145813/nim-mistral-nemotron__task_management__weekly_planning.md)

</details>

<details><summary><code>project_breakdown</code> — score 7.97</summary>

**Stats**: latencia 20.44s · 53 tok/s · 70→1088 tokens · $0.00133

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí tienes un desglose detallado del proyecto para lanzar la landing page en **4 semanas**, estructurado en **fases, tareas, dependencias, responsables y timeline**:

---

### **Fase 1: Definición de Requisitos (Día 1-3)**
**Objetivo**: Clarificar el alcance, público objetivo y mensaje clave.

| Ta
```

**Respuesta completa**: [`results/responses/20260425_145813/nim-mistral-nemotron__task_management__project_breakdown.md`](../results/responses/20260425_145813/nim-mistral-nemotron__task_management__project_breakdown.md)

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| extract_structured_data | 5.55 | 2.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>long_document_summary</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>extract_structured_data</code> — score 5.55</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id 'f81394d8-63c0-4023-afa2-7ad11aa54ca3': DEGRADED function cannot be invoked"}`

</details>
