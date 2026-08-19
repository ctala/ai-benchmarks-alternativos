# LongCat 2.0

- **model_id**: `meituan/longcat-2.0`
- **Total tests**: 23/26 exitosos (3 errores)
- **Score final**: 7.50
- **Calidad**: 8.29
- **Judge score (Phi-4)**: 4.91/10
- **Velocidad**: 35 tok/s
- **Latencia primera token**: 29.37s
- **Costo promedio por test**: $0.00126

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| business_audit | 6 | 6 | 5.86 | 5.89 |
| business_strategy | 4 | 2 | 8.64 | 10.00 |
| content_generation | 7 | 6 | 8.03 | 9.15 |
| content_verificable | 8 | 8 | 8.08 | 9.14 |
| tool_calling | 1 | 1 | 7.24 | 7.38 |

## Detalle por test

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 7.71 | 8.77 | 5 | 37 | 52.10s | OK |
| email_profesional | 8.22 | 9.41 | 4.8 | 41 | 32.68s | OK |
| social_media_batch | 8.32 | 9.55 | 5.0 | 35 | 28.32s | OK |
| blog_post_es | 7.80 | 8.84 | 5 | 38 | 40.39s | OK |
| email_profesional | 8.33 | 9.60 | 5 | 40 | 37.25s | OK |
| social_media_batch | 4.28 | 3.11 | - | 14 | 9.07s | ERROR |
| product_description_en | 7.83 | 8.73 | 5 | 34 | 21.51s | OK |

<details><summary><code>blog_post_es</code> — score 7.71</summary>

**Stats**: latencia 52.10s · 37 tok/s · 72→1616 tokens · $0.00200

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante, clara y profundiza en aspectos útiles de la automatización con IA para pequeñas empresas, proporcionando ejemplos concretos y aplicables.

**Respuesta (preview 300 chars)**:

```
# La Inteligencia Artificial al Alcance de Tu Negocio: Ventajas de la Automatización para Pequeñas Empresas

**Por qué la IA ya no es solo para las grandes corporaciones**

Durante años, la inteligencia artificial parecía un lujo reservado para gigantes tecnológicos con presupuestos millonarios. Sin
```

**Respuesta completa**: [`results/responses/longcat-2.0/content_generation/blog_post_es__20260817_n4.md`](../results/responses/longcat-2.0/content_generation/blog_post_es__20260817_n4.md)

</details>

<details><summary><code>email_profesional</code> — score 8.22</summary>

**Stats**: latencia 32.68s · 41 tok/s · 91→1375 tokens · $0.00200

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Asunto: Propuesta de Proyecto: Sitio Web Corporativo con E-commerce – [Tu Nombre o Empresa]

Estimado/a [Nombre del Cliente],

Gracias por la oportunidad de presentar nuestra propuesta para el desarrollo de su nuevo sitio web corporativo con e-commerce. Valoramos mucho su interés en nuestros servici
```

**Respuesta completa**: [`results/responses/longcat-2.0/content_generation/email_profesional__20260817_n4.md`](../results/responses/longcat-2.0/content_generation/email_profesional__20260817_n4.md)

</details>

<details><summary><code>social_media_batch</code> — score 8.32</summary>

**Stats**: latencia 28.32s · 35 tok/s · 84→935 tokens · $0.00100

**Juez Phi-4**: 5.0/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Aquí tienes 5 posts para LinkedIn sobre transformación digital:

---

**Post 1 (Tono: Datos duros)**
📊 El 70% de las iniciativas de transformación digital fracasan según McKinsey. No por falta de tecnología, sino por falta de estrategia.

Las empresas que tratan la transformación digital como un pro
```

**Respuesta completa**: [`results/responses/longcat-2.0/content_generation/social_media_batch__20260817_n4.md`](../results/responses/longcat-2.0/content_generation/social_media_batch__20260817_n4.md)

</details>

<details><summary><code>blog_post_es</code> — score 7.80</summary>

**Stats**: latencia 40.39s · 38 tok/s · 72→1931 tokens · $0.00200

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:5, claridad:5, utilidad:5)

> La respuesta es precisa, relevante, y ofrece una discusión profunda sobre los beneficios de la automatización con IA para pequeñas empresas, con ejemplos claros y aplicables, estructurada de manera lógica y fácil de entender.

**Respuesta (preview 300 chars)**:

```
**Automatización con IA: La ventaja competitiva que tu pequeña empresa necesita**

Dirigir una pequeña empresa es un acto de equilibrio constante. Con recursos limitados y un tiempo que nunca parece suficiente, cada minuto y cada euro cuentan. Sin embargo, la Inteligencia Artificial (IA) ha dejado d
```

**Respuesta completa**: [`results/responses/longcat-2.0/content_generation/blog_post_es__20260818_longcat-2.0.md`](../results/responses/longcat-2.0/content_generation/blog_post_es__20260818_longcat-2.0.md)

</details>

<details><summary><code>email_profesional</code> — score 8.33</summary>

**Stats**: latencia 37.25s · 40 tok/s · 91→1621 tokens · $0.00200

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante, clara y profundamente útil, proporcionando detalles específicos y un plan de acción claro.

**Respuesta (preview 300 chars)**:

```
Asunto: Propuesta de Proyecto: Sitio Web Corporativo y E-commerce – [Nombre de la Empresa]

Estimado/a [Nombre del Cliente],

Gracias por la oportunidad de presentar esta propuesta. Hemos analizado sus necesidades y estamos entusiasmados con la posibilidad de colaborar en la transformación digital d
```

**Respuesta completa**: [`results/responses/longcat-2.0/content_generation/email_profesional__20260818_longcat-2.0.md`](../results/responses/longcat-2.0/content_generation/email_profesional__20260818_longcat-2.0.md)

</details>

<details><summary><code>social_media_batch</code> — score 4.28</summary>

**Error**: `Response sin choices (provider devolvio respuesta vacia)`

</details>

<details><summary><code>product_description_en</code> — score 7.83</summary>

**Stats**: latencia 21.51s · 34 tok/s · 70→1341 tokens · $0.00100

**Juez Phi-4**: 5/10 (precisión:5, relevancia:5, profundidad:4, claridad:5, utilidad:5)

> La respuesta es precisa, relevante, clara y profundiza en las características y beneficios del dispositivo, proporcionando una descripción útil para un emprendedor.

**Respuesta (preview 300 chars)**:

```
**Breathe Easy. Sound Off. Set the Mood.**

Meet the ultimate smart home sidekick that does it all. Designed for the modern minimalist, this sleek device fuses crystal-clear audio, real-time air quality tracking, and customizable ambient lighting into one aesthetic masterpiece.

**1. Breathe Better,
```

**Respuesta completa**: [`results/responses/longcat-2.0/content_generation/product_description_en__20260818_longcat-2.0.md`](../results/responses/longcat-2.0/content_generation/product_description_en__20260818_longcat-2.0.md)

</details>

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 7.24 | 7.38 | 4.6 | 38 | 5.37s | OK |

<details><summary><code>single_tool_calendar</code> — score 7.24</summary>

**Stats**: latencia 5.37s · 38 tok/s · 574→269 tokens · $0.00000

**Juez Phi-4**: 4.6/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
The user wants to schedule a project meeting with the following details:
- Date: May 15, 2026 (2026-05-15)
- Time: 10:00 AM (10:00)
- Duration: 60 minutes
- Title: 'Sprint Planning Q2'

This is a calendar event creation request, so I need to use the create_calendar_event function. Let me check the
```

**Respuesta completa**: [`results/responses/longcat-2.0/tool_calling/single_tool_calendar__20260818_longcat-2.0.md`](../results/responses/longcat-2.0/tool_calling/single_tool_calendar__20260818_longcat-2.0.md)

</details>

### Otras suites

#### business_audit

#### business_strategy

#### content_verificable
