# MiniMax M2.7 Highspeed

- **model_id**: `MiniMax-M2.7-highspeed`
- **Total tests**: 39/39 exitosos (0 errores)
- **Score final**: 7.31
- **Calidad**: 8.36
- **Velocidad**: 49 tok/s
- **Latencia primera token**: 23.50s
- **Costo promedio por test**: $0.00413

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| agent_long_horizon | 12 | 12 | 6.61 | 7.50 |
| code_generation | 4 | 4 | 7.89 | 9.50 |
| content_generation | 4 | 4 | 7.58 | 8.75 |
| presentation | 2 | 2 | 7.88 | 9.62 |
| reasoning | 3 | 3 | 8.09 | 10.00 |
| startup_content | 5 | 5 | 7.75 | 9.56 |
| summarization | 2 | 2 | 7.65 | 8.50 |
| task_management | 3 | 3 | 7.97 | 9.63 |
| tool_calling | 4 | 4 | 6.50 | 5.00 |

## Detalle por test

### Razonamiento y Estrategia

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 8.08 | 10.00 | - | 52 | 39.25s | OK |
| logical_reasoning | 8.11 | 10.00 | - | 62 | 29.74s | OK |
| multi_constraint_decision | 8.08 | 10.00 | - | 54 | 37.66s | OK |

<details><summary><code>business_analysis</code> — score 8.08</summary>

**Stats**: latencia 39.25s · 52 tok/s · 201→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide un análisis completo de datos de su SaaS. Voy a analizar:

**Datos proporcionados:**
- Enero: 1,200 usuarios, $18,000 MRR, 45 churns, CAC $85, LTV $420
- Febrero: 1,350 usuarios, $20,250 MRR, 52 churns, CAC $92, LTV $415
- Marzo: 1,480 usuarios, $22,200 MRR, 68 churns, CAC
```

</details>

<details><summary><code>logical_reasoning</code> — score 8.11</summary>

**Stats**: latencia 29.74s · 62 tok/s · 161→1835 tokens · $0.00225

**Respuesta (preview 300 chars)**:

```
<think>
Necesito resolver este problema de lógica con ecuaciones.

Dados:
- 5 equipos: A, B, C, D, E
- A > B (A tiene más que B)
- A < C (A tiene menos que C)
- D = A (D tiene el mismo número que A)
- E < todos (E tiene menos que todos)
- A + B + C + D + E = 60
- Ningún equipo tiene menos de 5 perso
```

</details>

<details><summary><code>multi_constraint_decision</code> — score 8.08</summary>

**Stats**: latencia 37.66s · 54 tok/s · 199→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere ayuda para elegir un stack tecnológico para un MVP de un marketplace de servicios freelance. Necesito comparar al menos 3 opciones de stack considerando:

1. Restricciones:
   - Presupuesto: $5,000 total (infra + herramientas)
   - Timeline: 6 semanas
   - Equipo: 1 fullsta
```

</details>

### Coding y Datos

#### code_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| python_api_integration | 7.59 | 9.00 | - | 50 | 40.55s | OK |
| n8n_workflow_json | 8.09 | 10.00 | - | 75 | 27.27s | OK |
| sql_query_complex | 7.58 | 9.00 | - | 64 | 32.02s | OK |
| debug_code | 8.29 | 10.00 | - | 65 | 13.71s | OK |

<details><summary><code>python_api_integration</code> — score 7.59</summary>

**Stats**: latencia 40.55s · 50 tok/s · 133→2048 tokens · $0.00250

**Respuesta (preview 300 chars)**:

```
<think>
The user wants a Python function that does GET request to https://api.example.com/products with Bearer token auth, filters products with price > 100, returns a list of dicts with only id, name, price, handles network errors and timeout (10 seconds), includes retry with exponential backoff (m
```

</details>

<details><summary><code>n8n_workflow_json</code> — score 8.09</summary>

**Stats**: latencia 27.27s · 75 tok/s · 157→2048 tokens · $0.00250

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere un workflow de N8N en formato JSON. Voy a crear un workflow completo que:

1. Se active con un webhook POST
2. Extraiga los campos "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje
4. Envíe a diferentes canales de Slack según la clasifica
```

</details>

<details><summary><code>sql_query_complex</code> — score 7.58</summary>

**Stats**: latencia 32.02s · 64 tok/s · 181→2048 tokens · $0.00251

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere una consulta SQL compleja que muestre:
1. Top 10 clientes por revenue total en los últimos 6 meses
2. Con columnas específicas
3. Solo clientes con al menos 3 órdenes completadas

Necesito:
1. Filtrar órdenes de los últimos 6 meses
2. Filtrar solo status = 'completed'
3. Ag
```

</details>

<details><summary><code>debug_code</code> — score 8.29</summary>

**Stats**: latencia 13.71s · 65 tok/s · 255→894 tokens · $0.00115

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide que analice el código y encuentre los bugs mencionados, los explique y dé una versión corregida.

Veamos los bugs:

1. **División por cero**: Si no hay órdenes con status 'pending', `processed` estará vacío, y `len(processed)` será 0, causando una división por cero en `ave
```

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 6.72 | 7.00 | - | 37 | 18.54s | OK |
| email_profesional | 8.24 | 10.00 | - | 44 | 14.45s | OK |
| social_media_batch | 7.70 | 9.00 | - | 34 | 21.56s | OK |
| product_description_en | 7.64 | 9.00 | - | 62 | 27.23s | OK |

<details><summary><code>blog_post_es</code> — score 6.72</summary>

**Stats**: latencia 18.54s · 37 tok/s · 69→688 tokens · $0.00085

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide que escriba un blog post de aproximadamente 500 palabras sobre las ventajas de la automatización con IA para pequeñas empresas. Debo incluir:

1. Título
2. Introducción
3. 3 secciones con subtítulos
4. Conclusión con call-to-action

Voy a estructurar el contenido de manera
```

</details>

<details><summary><code>email_profesional</code> — score 8.24</summary>

**Stats**: latencia 14.45s · 44 tok/s · 76→635 tokens · $0.00078

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide que redacte un email profesional para un cliente que solicitó una propuesta. Los detalles del proyecto son:

- Sitio web corporativo con e-commerce
- Presupuesto: $15,000 USD
- Plazo: 3 meses

El email debe incluir:
1. Saludo
2. Resumen de la propuesta
3. Timeline
4. Sigui
```

</details>

<details><summary><code>social_media_batch</code> — score 7.70</summary>

**Stats**: latencia 21.56s · 34 tok/s · 79→730 tokens · $0.00090

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide generar 5 posts para LinkedIn sobre transformación digital. Cada post debe tener:
- Hook (primera línea llamativa)
- Cuerpo (3-4 líneas)
- CTA (llamada a la acción)
- 3 hashtags relevantes

Debo variar el tono entre:
- Educativo
- Inspiracional
- Datos duros (informativo c
```

</details>

<details><summary><code>product_description_en</code> — score 7.64</summary>

**Stats**: latencia 27.23s · 62 tok/s · 92→1678 tokens · $0.00204

**Respuesta (preview 300 chars)**:

```
<think>
The user wants: "Write a compelling product description for a smart home device that combines a speaker, air quality monitor, and ambient light. Target audience: tech-savvy millennials. Include: headline, 3 key features with benefits, and a closing statement. Max 200 words."

So we need to p
```

</details>

#### startup_content

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_actualidad_startup | 7.43 | 9.00 | - | 41 | 50.49s | OK |
| curso_emprendimiento_modulo | 7.63 | 9.40 | - | 42 | 49.03s | OK |
| workshop_outline | 7.93 | 10.00 | - | 44 | 47.06s | OK |
| newsletter_startup | 8.04 | 10.00 | - | 36 | 36.83s | OK |
| perplexity_style_research | 7.70 | 9.40 | - | 43 | 37.20s | OK |

<details><summary><code>blog_actualidad_startup</code> — score 7.43</summary>

**Stats**: latencia 50.49s · 41 tok/s · 207→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide escribir un artículo de blog en español sobre el impacto de los modelos de IA open-source en las startups latinoamericanas en 2026. Debo seguir una estructura específica con título SEO, meta description, introducción con gancho, 3-4 secciones H2 con subtítulos, datos concr
```

</details>

<details><summary><code>curso_emprendimiento_modulo</code> — score 7.63</summary>

**Stats**: latencia 49.03s · 42 tok/s · 221→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide diseñar el Módulo 3 de un curso sobre IA para emprendedores. Necesito crear contenido educativo completo y práctico siguiendo exactamente la estructura que me pide:

1. Objetivo del módulo
2. Contenido teórico sobre automatización con IA (incluyendo N8N)
3. 3 ejemplos prác
```

</details>

<details><summary><code>workshop_outline</code> — score 7.93</summary>

**Stats**: latencia 47.06s · 44 tok/s · 185→2048 tokens · $0.00251

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere un outline completo para un workshop presencial de 3 horas sobre construir asistentes de IA para startups. La audiencia es emprendedores early-stage no-técnicos. Necesito crear algo muy detallado, práctico y energizante.

Voy a estructurar esto de manera muy clara y util pa
```

</details>

<details><summary><code>newsletter_startup</code> — score 8.04</summary>

**Stats**: latencia 36.83s · 36 tok/s · 209→1337 tokens · $0.00167

**Respuesta (preview 300 chars)**:

```
<think>
The user wants me to create a weekly newsletter #47 for ecosistemastartup.com. Let me create it with a professional but friendly tone, following the format they've specified. I'll use Spanish throughout since the request is in Spanish and it's for a Spanish-language platform.

Let me craft t
```

</details>

<details><summary><code>perplexity_style_research</code> — score 7.70</summary>

**Stats**: latencia 37.20s · 43 tok/s · 180→1588 tokens · $0.00196

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide investigar sobre el estado del venture capital en Latinoamérica para Q1 2026. Sin embargo, debo ser honesto aquí: estamos a mayo de 2025 según mi conocimiento. Q1 2026 (enero-marzo 2026) todavía no ha ocurrido y no tengo datos reales sobre ese período.

Debo ser transparen
```

</details>

#### presentation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| slide_outline | 7.56 | 9.25 | - | 49 | 41.49s | OK |
| data_report | 8.19 | 10.00 | - | 52 | 26.11s | OK |

<details><summary><code>slide_outline</code> — score 7.56</summary>

**Stats**: latencia 41.49s · 49 tok/s · 160→2048 tokens · $0.00251

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere un outline completo para una presentación de 15 slides sobre "Plataforma Digital 2.0" dirigida al board de directores. Necesito estructurar esto de manera profesional y comprehensiva, cubriendo todos los temas mencionados:

1. Estado actual
2. Métricas de progreso
3. Riesgo
```

</details>

<details><summary><code>data_report</code> — score 8.19</summary>

**Stats**: latencia 26.11s · 52 tok/s · 181→1368 tokens · $0.00170

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide crear un reporte en formato markdown con análisis de ventas. Voy a estructurar la información proporcionada:

**Datos:**
- Producto A: Ene $45K, Feb $52K, Mar $48K, Abr $61K
- Producto B: Ene $23K, Feb $25K, Mar $31K, Abr $29K
- Producto C: Ene $12K, Feb $15K, Mar $18K, Ab
```

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 6.62 | 5.00 | - | 42 | 3.25s | OK |
| multi_tool_sequential | 6.70 | 5.00 | - | 59 | 3.74s | OK |
| tool_with_reasoning | 6.03 | 5.00 | - | 50 | 2.44s | OK |
| no_tool_needed | 6.66 | 5.00 | - | 32 | 3.37s | OK |

<details><summary><code>single_tool_calendar</code> — score 6.62</summary>

**Stats**: latencia 3.25s · 42 tok/s · 630→138 tokens · $0.00036

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere crear un evento en el calendario con los siguientes detalles:
- Título: 'Sprint Planning Q2'
- Fecha: 15 de mayo de 2026
- Hora: 10:00 AM
- Duración: 60 minutos

Voy a usar la función create_calendar_event con estos parámetros.
</think>
```

</details>

<details><summary><code>multi_tool_sequential</code> — score 6.70</summary>

**Stats**: latencia 3.74s · 59 tok/s · 656→221 tokens · $0.00046

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide hacer dos cosas:
1. Crear una tarea urgente con título 'Revisar contrato cliente ABC' con fecha límite 2026-05-10
2. Enviar un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente' explicando que necesitan revisión antes del 10 de mayo

Voy a ejecutar amba
```

</details>

<details><summary><code>tool_with_reasoning</code> — score 6.03</summary>

**Stats**: latencia 2.44s · 50 tok/s · 630→122 tokens · $0.00034

**Respuesta (preview 300 chars)**:

```
<think>
El usuario necesita dos cosas:
1. Crear un recordatorio/tarea para hoy a las 5 PM para repasar slides
2. Buscar en la web mejores prácticas para presentaciones ejecutivas

Voy a ejecutar ambas tareas en paralelo ya que son independientes.
</think>
```

</details>

<details><summary><code>no_tool_needed</code> — score 6.66</summary>

**Stats**: latencia 3.37s · 32 tok/s · 599→106 tokens · $0.00031

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pregunta cuál es la capital de Francia. Esta es una pregunta de conocimiento general que no requiere ninguna herramienta. Francia es un país muy conocido y su capital es París.
</think>

La capital de Francia es **París**. 🇫🇷

París es una de las ciudades más emblemáticas del m
```

</details>

#### task_management

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| extract_action_items | 8.04 | 9.50 | - | 46 | 10.42s | OK |
| weekly_planning | 7.78 | 9.40 | - | 60 | 34.29s | OK |
| project_breakdown | 8.09 | 10.00 | - | 55 | 37.16s | OK |

<details><summary><code>extract_action_items</code> — score 8.04</summary>

**Stats**: latencia 10.42s · 46 tok/s · 194→480 tokens · $0.00063

**Respuesta (preview 300 chars)**:

```
<think>
The user wants me to extract action items from a meeting note and format them as a table with: responsible person, task, deadline, and suggested priority.

Let me identify all action items from the notes:

1. **Carlos** - Terminar el API de pagos - antes del 20 de abril
2. **Ana** - Entregar
```

</details>

<details><summary><code>weekly_planning</code> — score 7.78</summary>

**Stats**: latencia 34.29s · 60 tok/s · 219→2048 tokens · $0.00252

**Respuesta (preview 300 chars)**:

```
<think>
El usuario es un Product Manager que necesita ayuda para planificar su semana. Voy a crear un calendario detallado que respete las restricciones given y quepa todas las tareas.

Primero, voy a mapear las restricciones:
- Lunes: 9-11 AM reunión directivos, 1-2 PM almuerzo cliente
- Martes: li
```

</details>

<details><summary><code>project_breakdown</code> — score 8.09</summary>

**Stats**: latencia 37.16s · 55 tok/s · 101→2048 tokens · $0.00249

**Respuesta (preview 300 chars)**:

```
<think>
El usuario necesita un plan detallado para lanzar una landing page de SaaS de gestión de inventario en 4 semanas con un equipo específico (1 diseñador, 2 desarrolladores, 1 copywriter). Necesito crear un desglose completo con fases, tareas, dependencias, responsables y timeline realista.

Vo
```

</details>

#### summarization

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| long_document_summary | 7.88 | 9.00 | - | 56 | 10.14s | OK |
| extract_structured_data | 7.42 | 8.00 | - | 77 | 9.02s | OK |

<details><summary><code>long_document_summary</code> — score 7.88</summary>

**Stats**: latencia 10.14s · 56 tok/s · 439→564 tokens · $0.00081

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide resumir un reporte trimestral en formato ejecutivo con un máximo de 200 palabras. Debo incluir:
- Métricas clave
- Logros
- Preocupaciones
- Próximos pasos recomendados

Voy a condensar la información más relevante de cada sección del reporte.

Métricas clave:
- Ventas: $2
```

</details>

<details><summary><code>extract_structured_data</code> — score 7.42</summary>

**Stats**: latencia 9.02s · 77 tok/s · 292→698 tokens · $0.00093

**Respuesta (preview 300 chars)**:

```
<think>
The user wants me to extract information from 3 candidate profiles and return them as JSON with specific fields:

- name
- age
- current_role
- years_experience
- current_company
- skills[]
- salary_expectation
- availability
- email
- certifications[]

Let me extract the information for eac
```

</details>

### Otras suites

#### agent_long_horizon
