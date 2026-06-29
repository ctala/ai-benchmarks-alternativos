# DeepSeek V4 Pro (NIM)

- **model_id**: `deepseek-ai/deepseek-v4-pro`
- **Total tests**: 3/58 exitosos (55 errores)
- **Score final**: 7.79
- **Calidad**: 8.83
- **Judge score (Phi-4)**: 4.67/10
- **Velocidad**: 5 tok/s
- **Latencia primera token**: 176.92s
- **Costo promedio por test**: $0.00000

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| agent_long_horizon | 7 | 0 | - | - |
| code_generation | 4 | 0 | - | - |
| content_generation | 8 | 2 | 7.95 | 9.42 |
| creativity | 2 | 0 | - | - |
| customer_support | 4 | 0 | - | - |
| deep_reasoning | 6 | 0 | - | - |
| hallucination | 3 | 0 | - | - |
| presentation | 2 | 0 | - | - |
| reasoning | 3 | 0 | - | - |
| startup_content | 5 | 0 | - | - |
| structured_output | 4 | 0 | - | - |
| summarization | 2 | 0 | - | - |
| task_management | 3 | 0 | - | - |
| tool_calling | 5 | 1 | 7.48 | 7.66 |

## Detalle por test

### Razonamiento y Estrategia

#### deep_reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| math_word_problem | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| logic_puzzle_constraint | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| causal_reasoning | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| code_bug_subtle | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| fermi_estimation | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| ethical_dilemma_structured | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>math_word_problem</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>logic_puzzle_constraint</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>causal_reasoning</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>code_bug_subtle</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>fermi_estimation</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>ethical_dilemma_structured</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| logical_reasoning | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| multi_constraint_decision | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>business_analysis</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>logical_reasoning</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>multi_constraint_decision</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### hallucination

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| factual_trap_companies | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| context_faithfulness | 3.88 | 0.00 | - | 0 | 0.23s | ERROR |
| fake_citation_trap | 4.48 | 1.20 | - | 0 | 0.01s | ERROR |

<details><summary><code>factual_trap_companies</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>context_faithfulness</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>fake_citation_trap</code> — score 4.48</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 4.88 | 2.00 | - | 0 | 0.01s | ERROR |
| n8n_workflow_json | 4.88 | 2.00 | - | 0 | 0.01s | ERROR |
| sql_query_complex | 4.88 | 2.00 | - | 0 | 0.01s | ERROR |
| debug_code | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>python_api_integration</code> — score 4.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>n8n_workflow_json</code> — score 4.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>sql_query_complex</code> — score 4.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>debug_code</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### structured_output

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| json_simple_extraction | 5.77 | 3.80 | - | 0 | 0.01s | ERROR |
| json_array_classification | 5.77 | 3.80 | - | 0 | 0.01s | ERROR |
| json_nested_complex | 5.77 | 3.80 | - | 0 | 0.01s | ERROR |
| json_strict_no_extra | 5.77 | 3.80 | - | 0 | 0.01s | ERROR |

<details><summary><code>json_simple_extraction</code> — score 5.77</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>json_array_classification</code> — score 5.77</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>json_nested_complex</code> — score 5.77</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>json_strict_no_extra</code> — score 5.77</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 8.04 | 9.52 | 4.8 | 10 | 110.05s | OK |
| email_profesional | 7.86 | 9.32 | 4.8 | 4 | 106.82s | OK |
| social_media_batch | 4.85 | 0.00 | - | 0 | 619.65s | ERROR |
| product_description_en | 5.55 | 2.00 | - | 0 | 401.78s | ERROR |
| blog_post_es | 3.88 | 0.00 | - | 0 | 0.14s | ERROR |
| email_profesional | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| social_media_batch | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| product_description_en | 4.88 | 2.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>blog_post_es</code> — score 8.04</summary>

**Stats**: latencia 110.05s · 10 tok/s · 64→1050 tokens · $0.00000

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Título: Cómo la Automatización con IA Está Nivelando el Campo de Juego para las Pequeñas Empresas**

**Introducción**
Durante décadas, la automatización avanzada fue un lujo exclusivo de las grandes corporaciones con presupuestos abultados y equipos de TI dedicados. Las pequeñas empresas, atrapada
```

**Respuesta completa**: [`results/responses/20260427_185648/nim-deepseek-v4-pro__content_generation__blog_post_es.md`](../results/responses/20260427_185648/nim-deepseek-v4-pro__content_generation__blog_post_es.md)

</details>

<details><summary><code>email_profesional</code> — score 7.86</summary>

**Stats**: latencia 106.82s · 4 tok/s · 78→394 tokens · $0.00000

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Asunto: Propuesta para el desarrollo de su sitio web corporativo con e-commerce

Estimado/a [Nombre del cliente]:

Espero que este mensaje le encuentre bien. En respuesta a su solicitud, adjunto a este correo la propuesta detallada para el desarrollo de su sitio web corporativo con funcionalidad de
```

**Respuesta completa**: [`results/responses/20260427_185648/nim-deepseek-v4-pro__content_generation__email_profesional.md`](../results/responses/20260427_185648/nim-deepseek-v4-pro__content_generation__email_profesional.md)

</details>

<details><summary><code>social_media_batch</code> — score 4.85</summary>

**Error**: `<html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
</body>
</html>`

</details>

<details><summary><code>product_description_en</code> — score 5.55</summary>

**Error**: `<html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
</body>
</html>`

</details>

<details><summary><code>blog_post_es</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>email_profesional</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>social_media_batch</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>product_description_en</code> — score 4.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| curso_emprendimiento_modulo | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| workshop_outline | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| newsletter_startup | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| perplexity_style_research | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>blog_actualidad_startup</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>workshop_outline</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>newsletter_startup</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>perplexity_style_research</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### creativity

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| creative_hook_writing | 6.28 | 4.80 | - | 0 | 0.01s | ERROR |
| analogy_generation | 6.28 | 4.80 | - | 0 | 0.01s | ERROR |

<details><summary><code>creative_hook_writing</code> — score 6.28</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>analogy_generation</code> — score 6.28</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| data_report | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>slide_outline</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>data_report</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 7.48 | 7.66 | 4.4 | 0 | 313.89s | OK |
| single_tool_calendar | 2.83 | 0.00 | - | 0 | 0.01s | ERROR |
| multi_tool_sequential | 2.83 | 0.00 | - | 0 | 0.01s | ERROR |
| tool_with_reasoning | 2.83 | 0.00 | - | 0 | 0.01s | ERROR |
| no_tool_needed | 4.33 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>single_tool_calendar</code> — score 7.48</summary>

**Stats**: latencia 313.89s · 0 tok/s · 739→140 tokens · $0.00000

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
[tool_call] create_calendar_event({"title": "Sprint Planning Q2", "date": "2026-05-15", "time": "10:00", "duration_minutes": 60, "description": "Reunión de planificación del sprint para el segundo trimestre de 2026."})
```

**Respuesta completa**: [`results/responses/20260427_185648/nim-deepseek-v4-pro__tool_calling__single_tool_calendar.md`](../results/responses/20260427_185648/nim-deepseek-v4-pro__tool_calling__single_tool_calendar.md)

</details>

<details><summary><code>single_tool_calendar</code> — score 2.83</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>multi_tool_sequential</code> — score 2.83</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>tool_with_reasoning</code> — score 2.83</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>no_tool_needed</code> — score 4.33</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### customer_support

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| angry_customer_refund | 2.83 | 0.00 | - | 0 | 0.01s | ERROR |
| ambiguous_issue_classification | 2.83 | 0.00 | - | 0 | 0.01s | ERROR |
| multi_issue_conversation | 2.83 | 0.00 | - | 0 | 0.01s | ERROR |
| social_engineering_attempt | 2.83 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>angry_customer_refund</code> — score 2.83</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>ambiguous_issue_classification</code> — score 2.83</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>multi_issue_conversation</code> — score 2.83</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>social_engineering_attempt</code> — score 2.83</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| weekly_planning | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| project_breakdown | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>extract_action_items</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>weekly_planning</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>project_breakdown</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 3.88 | 0.00 | - | 0 | 0.01s | ERROR |
| extract_structured_data | 4.88 | 2.00 | - | 0 | 0.01s | ERROR |

<details><summary><code>long_document_summary</code> — score 3.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

<details><summary><code>extract_structured_data</code> — score 4.88</summary>

**Error**: `Error code: 400 - {'error': {'message': 'deepseek-ai/deepseek-v4-pro is not a valid model ID', 'code': 400}, 'user_id': 'user_2vdCEjaT9wK3SkZiYPhzNuwzhNp'}`

</details>

### Otras suites

#### agent_long_horizon
