# MiniMax M2.7 (directo)

- **model_id**: `MiniMax-M2.7`
- **Total tests**: 27/27 exitosos (0 errores)
- **Score final**: 7.60
- **Calidad**: 8.69
- **Velocidad**: 57 tok/s
- **Latencia primera token**: 26.52s
- **Costo promedio por test**: $0.00170

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| code_generation | 4 | 4 | 8.15 | 10.00 |
| content_generation | 4 | 4 | 7.56 | 8.75 |
| presentation | 2 | 2 | 7.85 | 9.62 |
| reasoning | 3 | 3 | 7.92 | 9.67 |
| startup_content | 5 | 5 | 7.82 | 9.68 |
| summarization | 2 | 2 | 6.96 | 7.50 |
| task_management | 3 | 3 | 7.80 | 9.30 |
| tool_calling | 4 | 4 | 6.61 | 5.00 |

## Detalle por test

### Razonamiento y Estrategia

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 8.08 | 10.00 | - | 75 | 27.35s | OK |
| logical_reasoning | 7.74 | 9.00 | - | 112 | 18.33s | OK |
| multi_constraint_decision | 7.93 | 10.00 | - | 39 | 52.36s | OK |

<details><summary><code>business_analysis</code> — score 8.08</summary>

**Stats**: latencia 27.35s · 75 tok/s · 198→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>El usuario me pide un análisis completo de su SaaS con datos de enero a marzo. Voy a calcular todas las métricas solicitadas y proporcionar insights accionables.

**Métricas a calcular:**

1. **Churn Rate** = (Churns / Usuarios начала período) × 100
   - Enero: 45/1200 = 3.75%
   - Febrero: 5
```

</details>

<details><summary><code>logical_reasoning</code> — score 7.74</summary>

**Stats**: latencia 18.33s · 112 tok/s · 158→2048 tokens · $0.00250

**Respuesta (preview 300 chars)**:

```
<think>The problem: We have 5 teams A, B, C, D, E. We know certain constraints:

1. A has more members than B but less than C: A > B and A < C.
2. D has the same number as A: D = A.
3. E has fewer members than all: E is less than A, B, C, D. So E < A, E < B, etc.
4. Sum total is 60.
5. No team has l
```

</details>

<details><summary><code>multi_constraint_decision</code> — score 7.93</summary>

**Stats**: latencia 52.36s · 39 tok/s · 199→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere ayuda para elegir un stack tecnológico para un MVP de un marketplace de servicios freelance. Voy a analizar al menos 3 opciones de stack, compararlas y dar una recomendación con costos estimados.

Analicemos los requisitos:
1. Auth (autenticación)
2. Pagos (integración con
```

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 7.94 | 10.00 | - | 48 | 42.74s | OK |
| n8n_workflow_json | 8.09 | 10.00 | - | 64 | 31.79s | OK |
| sql_query_complex | 8.22 | 10.00 | - | 62 | 19.42s | OK |
| debug_code | 8.37 | 10.00 | - | 96 | 9.11s | OK |

<details><summary><code>python_api_integration</code> — score 7.94</summary>

**Stats**: latencia 42.74s · 48 tok/s · 133→2048 tokens · $0.00250

**Respuesta (preview 300 chars)**:

```
<think>
The user asks to write a Python function that does GET request to https://api.example.com/products with Bearer token authentication, filters products with price > 100, returns list of dicts with only id, name, price. Handle network errors and timeout (10 seconds). Include retry with exponent
```

</details>

<details><summary><code>n8n_workflow_json</code> — score 8.09</summary>

**Stats**: latencia 31.79s · 64 tok/s · 157→2048 tokens · $0.00250

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere un workflow de N8N en formato JSON que:

1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Según la clasificación, envie el email a un canal de Sla
```

</details>

<details><summary><code>sql_query_complex</code> — score 8.22</summary>

**Stats**: latencia 19.42s · 62 tok/s · 181→1207 tokens · $0.00150

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere una consulta SQL que muestre:
1. Top 10 clientes por revenue total en los últimos 6 meses
2. Con columnas específicas: nombre, email, país, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
3. Ordenado por total_revenue DESC
4. Solo clientes con al menos
```

</details>

<details><summary><code>debug_code</code> — score 8.37</summary>

**Stats**: latencia 9.11s · 96 tok/s · 252→875 tokens · $0.00113

**Respuesta (preview 300 chars)**:

```
<think>El usuario me pide que identifique los bugs en el código y los corrija. Ya me ha dado las pistas de los bugs:

1. División por cero si no hay órdenes pending
2. Muta el diccionario original
3. 'count' debería ser len(processed), no len(orders)

Déjame analizar el código:

```python
def proces
```

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 6.74 | 7.00 | - | 43 | 14.83s | OK |
| email_profesional | 7.99 | 9.00 | - | 70 | 8.22s | OK |
| social_media_batch | 8.01 | 10.00 | - | 27 | 31.74s | OK |
| product_description_en | 7.51 | 9.00 | - | 48 | 32.00s | OK |

<details><summary><code>blog_post_es</code> — score 6.74</summary>

**Stats**: latencia 14.83s · 43 tok/s · 71→639 tokens · $0.00079

**Respuesta (preview 300 chars)**:

```
<think>The user wants me to write a blog post of approximately 500 words about the advantages of AI automation for small businesses. I need to include:
- Title
- Introduction
- 3 sections with subtitles
- Conclusion with call-to-action

Let me write this in Spanish since the request is in Spanish.
<
```

</details>

<details><summary><code>email_profesional</code> — score 7.99</summary>

**Stats**: latencia 8.22s · 70 tok/s · 78→576 tokens · $0.00072

**Respuesta (preview 300 chars)**:

```
<think>El usuario me pide redactar un email profesional para un cliente que solicitó una propuesta. El proyecto es un sitio web corporativo con e-commerce. Necesito incluir:
- Saludo
- Resumen de la propuesta
- Timeline
- Siguiente paso

Presupuesto: $15,000 USD
Plazo: 3 meses

Voy a redactar un ema
```

</details>

<details><summary><code>social_media_batch</code> — score 8.01</summary>

**Stats**: latencia 31.74s · 27 tok/s · 79→867 tokens · $0.00106

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide crear 5 posts para LinkedIn sobre transformación digital. Necesito:

1. Variar los tonos: educativo, inspiracional y datos duros
2. Cada post debe tener:
   - Hook (primera línea llamativa)
   - Cuerpo (3-4 líneas)
   - CTA
   - 3 hashtags relevantes

Voy a crear 5 posts c
```

</details>

<details><summary><code>product_description_en</code> — score 7.51</summary>

**Stats**: latencia 32.00s · 48 tok/s · 92→1531 tokens · $0.00186

**Respuesta (preview 300 chars)**:

```
<think>
The user wants: "Write a compelling product description for a smart home device that combines a speaker, air quality monitor, and ambient light. Target audience: tech-savvy millennials. Include: headline, 3 key features with benefits, and a closing statement. Max 200 words."

We need to prod
```

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 7.49 | 9.00 | - | 35 | 46.92s | OK |
| curso_emprendimiento_modulo | 7.63 | 9.40 | - | 36 | 56.11s | OK |
| workshop_outline | 8.08 | 10.00 | - | 61 | 33.54s | OK |
| newsletter_startup | 7.98 | 10.00 | - | 34 | 49.89s | OK |
| perplexity_style_research | 7.94 | 10.00 | - | 42 | 48.38s | OK |

<details><summary><code>blog_actualidad_startup</code> — score 7.49</summary>

**Stats**: latencia 46.92s · 35 tok/s · 207→1649 tokens · $0.00204

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide escribir un artículo de blog SEO-friendly sobre el impacto de los modelos de IA open-source en las startups latinoamericanas en 2026. Debo seguir una estructura específica con título SEO, meta description, introducción, 3-4 secciones H2, datos regionales, modelos mencionad
```

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 7.63</summary>

**Stats**: latencia 56.11s · 36 tok/s · 221→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide diseñar el Módulo 3 de un curso sobre IA práctica para emprendedores. El módulo se titula "Automatización con IA: De la idea al flujo de trabajo".

Debo incluir:
1. Objetivo del módulo
2. Contenido teórico sobre automatización con IA, incluyendo herramientas como N8N
3. 3
```

</details>

<details><summary><code>workshop_outline</code> — score 8.08</summary>

**Stats**: latencia 33.54s · 61 tok/s · 187→2048 tokens · $0.00251

**Respuesta (preview 300 chars)**:

```
<think>El usuario me pide crear un outline completo para un workshop presencial de 3 horas sobre "Construye tu Asistente de IA para tu Startup". Necesito diseñar algo muy detallado y práctico para emprendedores no técnicos.

Voy a estructurar esto siguiendo exactamente lo que me piden:

1. Agenda de
```

</details>

<details><summary><code>newsletter_startup</code> — score 7.98</summary>

**Stats**: latencia 49.89s · 34 tok/s · 209→1708 tokens · $0.00211

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide que genere un newsletter semanal #47 para ecosistemastartup.com con 5 temas específicos relacionados con IA y startups en América Latina. Debo seguir el formato solicitado, con tono profesional pero cercano, informativo y con opinión editorial.

Voy a estructurar el newsle
```

</details>

<details><summary><code>perplexity_style_research</code> — score 7.94</summary>

**Stats**: latencia 48.38s · 42 tok/s · 180→2048 tokens · $0.00251

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide una investigación sobre el estado del venture capital en Latinoamérica para Q1 2026. Necesito ser claro aquí: estamos en enero de 2025 según mi conocimiento. Q1 2026 serían datos futuros que no están disponibles.

Debo ser honesto sobre esta limitación temporal. Puedo ofre
```

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 7.71 | 9.25 | - | 51 | 39.81s | OK |
| data_report | 7.99 | 10.00 | - | 47 | 34.92s | OK |

<details><summary><code>slide_outline</code> — score 7.71</summary>

**Stats**: latencia 39.81s · 51 tok/s · 157→2048 tokens · $0.00250

**Respuesta (preview 300 chars)**:

```
<think>El usuario me pide crear un outline completo para una presentación de 15 slides sobre el proyecto "Plataforma Digital 2.0" dirigida al board de directors. Necesito incluir para cada slide:
- Número y título
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido
- Notas del pr
```

</details>

<details><summary><code>data_report</code> — score 7.99</summary>

**Stats**: latencia 34.92s · 47 tok/s · 181→1642 tokens · $0.00202

**Respuesta (preview 300 chars)**:

```
<think>
The user wants a sales report in markdown format with tables and analysis based on the provided sales data:

Producto A: Ene $45K, Feb $52K, Mar $48K, Abr $61K
Producto B: Ene $23K, Feb $25K, Mar $31K, Abr $29K
Producto C: Ene $12K, Feb $15K, Mar $18K, Abr $22K

They want:
1. Monthly data ta
```

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 6.90 | 5.00 | - | 85 | 1.86s | OK |
| multi_tool_sequential | 6.69 | 5.00 | - | 83 | 2.84s | OK |
| tool_with_reasoning | 5.86 | 5.00 | - | 37 | 4.04s | OK |
| no_tool_needed | 6.97 | 5.00 | - | 53 | 1.78s | OK |

<details><summary><code>single_tool_calendar</code> — score 6.90</summary>

**Stats**: latencia 1.86s · 85 tok/s · 642→158 tokens · $0.00038

**Respuesta (preview 300 chars)**:

```
<think>El usuario quiere agendar una reunión con los siguientes detalles:
- Título: 'Sprint Planning Q2'
- Fecha: 15 de mayo de 2026
- Hora: 10:00 AM
- Duración: 60 minutos

Voy a usar la función create_calendar_event con los parámetros proporcionados.
</think>
```

</details>

<details><summary><code>multi_tool_sequential</code> — score 6.69</summary>

**Stats**: latencia 2.84s · 83 tok/s · 668→236 tokens · $0.00048

**Respuesta (preview 300 chars)**:

```
<think>El usuario necesita que realice dos acciones:
1. Crear una tarea urgente con título 'Revisar contrato cliente ABC' y fecha límite 2026-05-10
2. Enviar un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente'

Ambas acciones son independientes entre sí, así que puedo ejecutarl
```

</details>

<details><summary><code>tool_with_reasoning</code> — score 5.86</summary>

**Stats**: latencia 4.04s · 37 tok/s · 647→148 tokens · $0.00037

**Respuesta (preview 300 chars)**:

```
<think>El usuario necesita:
1. Crear un recordatorio (tarea) para hoy a las 5 PM para repasar slides
2. Buscar en la web mejores prácticas para presentaciones ejecutivas

Voy a hacer ambas cosas en paralelo ya que son independientes.
</think>
```

</details>

<details><summary><code>no_tool_needed</code> — score 6.97</summary>

**Stats**: latencia 1.78s · 53 tok/s · 611→94 tokens · $0.00030

**Respuesta (preview 300 chars)**:

```
<think>El usuario me está preguntando cuál es la capital de Francia. Esta es una pregunta de conocimiento general muy básica que no requiere ninguna herramienta especial. La respuesta es simple: París.
</think>

La capital de Francia es **París**. Es una de las ciudades más famosas y visitadas del m
```

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 8.03 | 9.50 | - | 33 | 15.44s | OK |
| weekly_planning | 7.28 | 8.40 | - | 81 | 25.41s | OK |
| project_breakdown | 8.09 | 10.00 | - | 66 | 30.89s | OK |

<details><summary><code>extract_action_items</code> — score 8.03</summary>

**Stats**: latencia 15.44s · 33 tok/s · 194→503 tokens · $0.00066

**Respuesta (preview 300 chars)**:

```
<think>
The user wants me to extract action items from the meeting notes and format them as a table with: responsible person, task, deadline, and suggested priority.

Let me identify all action items from the notes:

1. Carlos - Terminar el API de pagos - antes del 20 de abril
2. Ana - Entregar los
```

</details>

<details><summary><code>weekly_planning</code> — score 7.28</summary>

**Stats**: latencia 25.41s · 81 tok/s · 216→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>Voy a crear un plan semanal detallado para este Product Manager. Primero necesito identificar los huecos disponibles en cada día, considerando las restricciones existentes y luego asignar las tareas de manera eficiente.

**Análisis de restricciones:**
- Lunes: 9-11 AM (reunión directivos), 1-
```

</details>

<details><summary><code>project_breakdown</code> — score 8.09</summary>

**Stats**: latencia 30.89s · 66 tok/s · 98→2048 tokens · $0.00249

**Respuesta (preview 300 chars)**:

```
<think>Here's a thinking process that leads to the suggested project plan:

1.  **Analyze the Request:**
    *   **Goal:** Launch a Landing Page for a new Inventory Management SaaS.
    *   **Timeframe:** 4 weeks (approx. 20-25 working days).
    *   **Team:**
        *   1 Designer.
        *   2 D
```

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 7.28 | 8.00 | - | 39 | 11.63s | OK |
| extract_structured_data | 6.63 | 7.00 | - | 70 | 24.55s | OK |

<details><summary><code>long_document_summary</code> — score 7.28</summary>

**Stats**: latencia 11.63s · 39 tok/s · 439→451 tokens · $0.00067

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide resumir un reporte trimestral en formato ejecutivo con un máximo de 200 palabras. Debo incluir: métricas clave, logros, preocupaciones y próximos pasos recomendados.

Voy a estructurar el resumen de manera clara y concisa:

1. **Métricas clave**: Ventas $2.3M (+18%), marge
```

</details>

<details><summary><code>extract_structured_data</code> — score 6.63</summary>

**Stats**: latencia 24.55s · 70 tok/s · 292→1706 tokens · $0.00214

**Respuesta (preview 300 chars)**:

```
<think>
The user wants us to extract info from three candidate profiles and return as JSON.

The user wrote:

"Extrae la informacion de estos 3 perfiles de candidatos y devuelvelos como JSON:

Candidato 1: Maria Garcia, 28 anos, ingeniera de software con 5 anos de experiencia. Trabaja en Google desd
```

</details>
