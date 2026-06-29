# Qwen 3.6 27B base (DGX Spark)

- **model_id**: `qwen3.6:27b`
- **Total tests**: 4/4 exitosos (0 errores)
- **Score final**: 6.62
- **Calidad**: 8.45
- **Judge score (Phi-4)**: 4.50/10
- **Velocidad**: 10 tok/s
- **Latencia primera token**: 195.59s
- **Costo promedio por test**: $0.00629

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| content_generation | 2 | 2 | 6.53 | 8.24 |
| reasoning | 2 | 2 | 6.71 | 8.66 |

## Detalle por test

### Razonamiento y Estrategia

#### reasoning

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| business_analysis | 6.56 | 8.36 | 4.4 | 11 | 189.04s | OK |
| logical_reasoning | 6.86 | 8.96 | 4.4 | 11 | 191.22s | OK |

<details><summary><code>business_analysis</code> — score 6.56</summary>

**Stats**: latencia 189.04s · 11 tok/s · 206→2048 tokens · $0.00661

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Here's a thinking process:

1.  **Understand User Input:**
   - **Data Provided:**
     - January: 1,200 users, $18,000 MRR, 45 churns, CAC $85, LTV $420
     - February: 1,350 users, $20,250 MRR, 52 churns, CAC $92, LTV $415
     - March: 1,480 users, $22,200 MRR, 68 churns, CAC $78, LTV $408
   -
```

**Respuesta completa**: [`results/responses/20260601_093819/local-qwen3.6-27b__reasoning__business_analysis.md`](../results/responses/20260601_093819/local-qwen3.6-27b__reasoning__business_analysis.md)

</details>

<details><summary><code>logical_reasoning</code> — score 6.86</summary>

**Stats**: latencia 191.22s · 11 tok/s · 135→2048 tokens · $0.00659

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
Here's a thinking process:

1.  **Understand the User's Request:**
   - **Problem:** A company has 5 teams (A, B, C, D, E).
   - **Given Conditions:**
     1. A > B and A < C (So B < A < C)
     2. D = A
     3. E < everyone else (E is the smallest)
     4. Total sum = 60
     5. No team has fewer t
```

**Respuesta completa**: [`results/responses/20260601_093819/local-qwen3.6-27b__reasoning__logical_reasoning.md`](../results/responses/20260601_093819/local-qwen3.6-27b__reasoning__logical_reasoning.md)

</details>

### Contenido y Marketing

#### content_generation

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| blog_post_es | 6.36 | 7.96 | 4.4 | 11 | 190.27s | OK |
| email_profesional | 6.70 | 8.52 | 4.8 | 8 | 211.83s | OK |

<details><summary><code>blog_post_es</code> — score 6.36</summary>

**Stats**: latencia 190.27s · 11 tok/s · 71→2048 tokens · $0.00657

**Juez Phi-4**: 4.4/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Cómo la Automatización con IA Está Transformando a las Pequeñas Empresas**

Durante años, la inteligencia artificial parecía un lujo reservado exclusivamente para grandes corporaciones con presupuestos millonarios. Hoy, ese panorama ha cambiado por completo. Las pequeñas empresas ahora pueden acce
```

**Respuesta completa**: [`results/responses/20260601_094658/local-qwen3.6-27b__content_generation__blog_post_es.md`](../results/responses/20260601_094658/local-qwen3.6-27b__content_generation__blog_post_es.md)

</details>

<details><summary><code>email_profesional</code> — score 6.70</summary>

**Stats**: latencia 211.83s · 8 tok/s · 82→1674 tokens · $0.00538

**Juez Phi-4**: 4.8/10 (precisión:3, relevancia:3, profundidad:3, claridad:3, utilidad:3)

**Respuesta (preview 300 chars)**:

```
**Asunto:** Propuesta técnica y comercial: Desarrollo de sitio web corporativo con e-commerce

Estimado/a [Nombre del Cliente]:

Espero que se encuentre muy bien. Agradezco la oportunidad de presentarles nuestra propuesta para el desarrollo de su sitio web corporativo integrado con tienda en línea,
```

**Respuesta completa**: [`results/responses/20260601_094658/local-qwen3.6-27b__content_generation__email_profesional.md`](../results/responses/20260601_094658/local-qwen3.6-27b__content_generation__email_profesional.md)

</details>
