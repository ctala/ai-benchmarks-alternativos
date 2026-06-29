# Mistral Magistral Small (NIM)

- **model_id**: `mistralai/magistral-small-2506`
- **Total tests**: 10/91 exitosos (81 errores)
- **Score final**: 5.70
- **Calidad**: 5.90
- **Judge score (Phi-4)**: 4.56/10
- **Velocidad**: 24 tok/s
- **Latencia primera token**: 43.64s
- **Costo promedio por test**: $0.00188

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| agent_capabilities | 5 | 0 | - | - |
| code_generation | 4 | 0 | - | - |
| content_generation | 4 | 4 | 7.39 | 9.16 |
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
| task_management | 3 | 2 | 2.72 | 0.00 |
| tool_calling | 4 | 4 | 5.49 | 5.59 |
| translation | 3 | 0 | - | - |

## Detalle por test

### Razonamiento y Estrategia

#### deep_reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| math_word_problem | 4.85 | 0.00 | - | 0 | 0.16s | ERROR |
| logic_puzzle_constraint | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| causal_reasoning | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| code_bug_subtle | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| fermi_estimation | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| ethical_dilemma_structured | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>math_word_problem</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>logic_puzzle_constraint</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>causal_reasoning</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>code_bug_subtle</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>fermi_estimation</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>ethical_dilemma_structured</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| logical_reasoning | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| multi_constraint_decision | 4.85 | 0.00 | - | 0 | 0.16s | ERROR |

<details><summary><code>business_analysis</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>logical_reasoning</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>multi_constraint_decision</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### hallucination

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| factual_trap_companies | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| context_faithfulness | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| fake_citation_trap | 5.27 | 1.20 | - | 0 | 0.15s | ERROR |

<details><summary><code>factual_trap_companies</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>context_faithfulness</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>fake_citation_trap</code> — score 5.27</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### strategy

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| competitor_analysis | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| pricing_strategy | 4.85 | 0.00 | - | 0 | 0.14s | ERROR |
| business_model_validation | 6.53 | 4.80 | - | 0 | 0.21s | ERROR |

<details><summary><code>competitor_analysis</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>pricing_strategy</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>business_model_validation</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 5.55 | 2.00 | - | 0 | 301.36s | ERROR |
| n8n_workflow_json | 5.55 | 2.00 | - | 0 | 0.16s | ERROR |
| sql_query_complex | 5.55 | 2.00 | - | 0 | 0.15s | ERROR |
| debug_code | 4.85 | 0.00 | - | 0 | 0.16s | ERROR |

<details><summary><code>python_api_integration</code> — score 5.55</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>n8n_workflow_json</code> — score 5.55</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>sql_query_complex</code> — score 5.55</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>debug_code</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### structured_output

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| json_simple_extraction | 6.18 | 3.80 | - | 0 | 0.14s | ERROR |
| json_array_classification | 6.18 | 3.80 | - | 0 | 0.15s | ERROR |
| json_nested_complex | 6.18 | 3.80 | - | 0 | 0.15s | ERROR |
| json_strict_no_extra | 6.18 | 3.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>json_simple_extraction</code> — score 6.18</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>json_array_classification</code> — score 6.18</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>json_nested_complex</code> — score 6.18</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>json_strict_no_extra</code> — score 6.18</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### string_precision

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| copy_hex_32 | 5.34 | 1.40 | - | 0 | 0.16s | ERROR |
| copy_hex_64 | 5.34 | 1.40 | - | 0 | 0.15s | ERROR |
| copy_api_key | 5.34 | 1.40 | - | 0 | 0.15s | ERROR |
| copy_jwt | 5.34 | 1.40 | - | 0 | 0.14s | ERROR |
| copy_mixed_special | 5.34 | 1.40 | - | 0 | 0.15s | ERROR |
| write_config_file | 5.13 | 0.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>copy_hex_32</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>copy_hex_64</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>copy_api_key</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>copy_jwt</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>copy_mixed_special</code> — score 5.34</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>write_config_file</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### ocr_extraction

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| invoice_extraction | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| business_card_extraction | 5.13 | 0.80 | - | 0 | 0.15s | ERROR |
| receipt_math_verification | 5.13 | 0.80 | - | 0 | 0.15s | ERROR |
| screenshot_table_extraction | 5.13 | 0.80 | - | 0 | 0.15s | ERROR |
| handwritten_notes_extraction | 5.13 | 0.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>invoice_extraction</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>business_card_extraction</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>receipt_math_verification</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>screenshot_table_extraction</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>handwritten_notes_extraction</code> — score 5.13</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 6.80 | 8.08 | 4.2 | 25 | 68.64s | OK |
| email_profesional | 7.72 | 9.52 | 4.8 | 25 | 30.25s | OK |
| social_media_batch | 7.42 | 9.24 | 4.6 | 25 | 58.65s | OK |
| product_description_en | 7.62 | 9.80 | 5 | 25 | 81.50s | OK |

<details><summary><code>blog_post_es</code> — score 6.80</summary>

**Stats**: latencia 68.64s · 25 tok/s · 234→1732 tokens · $0.00271

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Blog Post:**

**Título:** "Cómo la automatización con IA puede transformar tu pequeña empresa"

En el mundo actual, donde la tecnología avanza a un ritmo vertiginoso, las pequeñas empresas pueden aprovechar herramientas innovadoras para compete y crecer. Una de las tecnologías más prometedoras e
```

**Respuesta completa**: [`results/responses/20260427_185648/nim-magistral-small__content_generation__blog_post_es.md`](../results/responses/20260427_185648/nim-magistral-small__content_generation__blog_post_es.md)

</details>

<details><summary><code>email_profesional</code> — score 7.72</summary>

**Stats**: latencia 30.25s · 25 tok/s · 248→763 tokens · $0.00127

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Asunto:** Propuesta para el Desarrollo de su Sitio Web Corporativo con E-commerce

**Estimado [Nombre del Cliente],**

Espero que este mensaje lo encuentre bien. Agradecemos su interés en nuestros servicios y nos complace presentarle nuestra propuesta para el desarrollo de su sitio web corporati
```

**Respuesta completa**: [`results/responses/20260427_185648/nim-magistral-small__content_generation__email_profesional.md`](../results/responses/20260427_185648/nim-magistral-small__content_generation__email_profesional.md)

</details>

<details><summary><code>social_media_batch</code> — score 7.42</summary>

**Stats**: latencia 58.65s · 25 tok/s · 246→1478 tokens · $0.00234

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
### Post 1 (Educativo)
**Hook:** "¿Sabes qué es lo más criticado en las empresas hoy en día?"
**Cuerpo:** La resistencia al cambio. La transformación digital no es solo sobre tecnología, es sobre cultura. Las empresas que adoptan una mentalidad de aprendizaje continuo son las que lideran en el mer
```

**Respuesta completa**: [`results/responses/20260427_185648/nim-magistral-small__content_generation__social_media_batch.md`](../results/responses/20260427_185648/nim-magistral-small__content_generation__social_media_batch.md)

</details>

<details><summary><code>product_description_en</code> — score 7.62</summary>

**Stats**: latencia 81.50s · 25 tok/s · 229→2048 tokens · $0.00319

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante y clara, con una estructura bien organizada que destaca las características clave del producto de manera efectiva. Ofrece insights útiles para un emprendedor al enfocarse en beneficios específicos que atraen al público objetivo.

**Respuesta (preview 300 chars)**:

```
**Headline:** "Your Smart Home, Simplified: The Ultimate All-in-One Device"

**Key Features with Benefits:**
1. "Immersive Sound & Smart Control: Enjoy high-fidelity audio with built-in voice assistants for effortless control of your smart home devices and streaming services. Perfect for movie nig
```

**Respuesta completa**: [`results/responses/20260427_185648/nim-magistral-small__content_generation__product_description_en.md`](../results/responses/20260427_185648/nim-magistral-small__content_generation__product_description_en.md)

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| curso_emprendimiento_modulo | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| workshop_outline | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| newsletter_startup | 4.85 | 0.00 | - | 0 | 0.23s | ERROR |
| perplexity_style_research | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>blog_actualidad_startup</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>workshop_outline</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>newsletter_startup</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>perplexity_style_research</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### news_seo_writing

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| news_seo_article_full | 4.85 | 0.00 | - | 0 | 0.14s | ERROR |
| news_json_output_strict | 5.90 | 3.00 | - | 0 | 0.15s | ERROR |
| news_spanish_only | 5.90 | 3.00 | - | 0 | 0.15s | ERROR |
| news_no_hallucination_sources | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| news_perplexity_enrichment | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>news_seo_article_full</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>news_json_output_strict</code> — score 5.90</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>news_spanish_only</code> — score 5.90</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>news_no_hallucination_sources</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>news_perplexity_enrichment</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### creativity

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| creative_hook_writing | 6.53 | 4.80 | - | 0 | 0.24s | ERROR |
| analogy_generation | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |
| depth_vs_superficial | 6.53 | 4.80 | - | 0 | 0.18s | ERROR |
| storytelling_quality | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |

<details><summary><code>creative_hook_writing</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>analogy_generation</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>depth_vs_superficial</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>storytelling_quality</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### sales_outreach

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| cold_email_personalized | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |
| lead_qualification | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| campaign_optimization | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>cold_email_personalized</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>lead_qualification</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>campaign_optimization</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### translation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| translate_marketing_es_en | 6.81 | 5.60 | - | 0 | 0.15s | ERROR |
| translate_technical_en_es | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| detect_language_issues | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>translate_marketing_es_en</code> — score 6.81</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>translate_technical_en_es</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>detect_language_issues</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 4.85 | 0.00 | - | 0 | 0.16s | ERROR |
| data_report | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>slide_outline</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>data_report</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 5.58 | 7.38 | 4.2 | 25 | 27.23s | OK |
| multi_tool_sequential | 4.87 | 5.00 | - | 21 | 4.60s | OK |
| tool_with_reasoning | 4.88 | 5.00 | - | 22 | 4.03s | OK |
| no_tool_needed | 6.62 | 5.00 | - | 18 | 1.06s | OK |

<details><summary><code>single_tool_calendar</code> — score 5.58</summary>

**Stats**: latencia 27.23s · 25 tok/s · 701→678 tokens · $0.00137

**Juez Phi-4**: 4.2/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Para agendar la reunion, se utilizara la siguiente informacion:

- Titolo: 'Sprint Planning Q2'
- Fecha: '2026-05-15'
- Hora: '10:00'
- Duracion: 60 minutos

A continuacion, se procedera a agendar la reunion con estos detalles.

```python
response = create_calendar_event(
    title='Sprint Plannin
```

**Respuesta completa**: [`results/responses/20260427_185648/nim-magistral-small__tool_calling__single_tool_calendar.md`](../results/responses/20260427_185648/nim-magistral-small__tool_calling__single_tool_calendar.md)

</details>

#### customer_support

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| angry_customer_refund | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| ambiguous_issue_classification | 3.10 | 0.00 | - | 0 | 0.17s | ERROR |
| multi_issue_conversation | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| social_engineering_attempt | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>angry_customer_refund</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>ambiguous_issue_classification</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>multi_issue_conversation</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>social_engineering_attempt</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### orchestration

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| multi_step_research_plan | 3.10 | 0.00 | - | 0 | 0.16s | ERROR |
| error_recovery_orchestration | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| complex_workflow_decomposition | 3.80 | 2.00 | - | 0 | 0.15s | ERROR |
| tool_selection_precision | 3.38 | 0.80 | - | 0 | 0.21s | ERROR |
| parallel_vs_sequential_judgment | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>multi_step_research_plan</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>error_recovery_orchestration</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>complex_workflow_decomposition</code> — score 3.80</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>tool_selection_precision</code> — score 3.38</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>parallel_vs_sequential_judgment</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### multi_turn

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| content_iteration | 6.53 | 4.80 | - | 0 | 0.15s | ERROR |
| support_escalation | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| requirements_change | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| debugging_conversation | 4.85 | 0.00 | - | 0 | 0.16s | ERROR |

<details><summary><code>content_iteration</code> — score 6.53</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>support_escalation</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>requirements_change</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>debugging_conversation</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### policy_adherence

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| refund_policy_enforcement | 4.85 | 0.00 | - | 0 | 0.22s | ERROR |
| data_privacy_protection | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| language_and_tone_rules | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| scope_boundaries | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>refund_policy_enforcement</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>data_privacy_protection</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>language_and_tone_rules</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>scope_boundaries</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### agent_capabilities

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| skill_execution_complex | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| agent_team_delegation | 3.10 | 0.00 | - | 0 | 0.15s | ERROR |
| ask_clarification_before_acting | 3.10 | 0.00 | - | 0 | 0.20s | ERROR |
| context_following_complex_system | 3.10 | 0.00 | - | 0 | 0.16s | ERROR |
| model_as_router | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>skill_execution_complex</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>agent_team_delegation</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>ask_clarification_before_acting</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>context_following_complex_system</code> — score 3.10</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>model_as_router</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 2.72 | 0.00 | - | 24 | 83.52s | OK |
| weekly_planning | 2.72 | 0.00 | - | 27 | 76.96s | OK |
| project_breakdown | 4.85 | 0.00 | - | 0 | 46.93s | ERROR |

<details><summary><code>project_breakdown</code> — score 4.85</summary>

**Error**: `Error code: 500 - {'type': 'urn:inference-connection:problem-details:internal-server-error', 'title': 'Internal Server Error', 'status': 500, 'detail': 'Inference connection error while making inferen...`

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 4.85 | 0.00 | - | 0 | 0.15s | ERROR |
| extract_structured_data | 5.55 | 2.00 | - | 0 | 0.15s | ERROR |

<details><summary><code>long_document_summary</code> — score 4.85</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>

<details><summary><code>extract_structured_data</code> — score 5.55</summary>

**Error**: `Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': "Function id '9080da86-7a09-42de-aca4-e86ee2dc7297': DEGRADED function cannot be invoked"}`

</details>
