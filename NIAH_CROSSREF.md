---
title: "NIAH-ES vs literatura — triangulación con benchmarks NIAH oficiales"
fecha: "2026-04-30"
fuente_principal: "Papers oficiales (Gemini 1.5, Gemini 2.5/3, DeepSeek V4, Llama 3.3/4, Mistral), Anthropic system cards, OpenAI GPT-4.1 announcement, Greg Kamradt repo"
---

# Cross-reference NIAH-ES con literatura NIAH (inglés)

> 📍 **Posición epistémica**: NIAH-ES es **complemento** del NIAH original (no sustituto). Mide retrieval en **español neutro LATAM** con datos realistas para emprendedores hispanohablantes. La literatura NIAH inglesa (Greg Kamradt, Gemini 1.5 paper, Anthropic system cards) sigue siendo la referencia para capacidad fundamental. Acá triangulamos para validez convergente y discriminante. Si tu task es retrieval en inglés con prompts académicos, **usá los benchmarks oficiales**. Si tu task es "extraer info concreta de un documento de 64K tokens en español neutro LATAM en producción", NIAH-ES suma data que los oficiales no cubren.

NIAH-ES (nuestro benchmark) mide retrieval en español neutro LATAM con scoring 0–10
basado en sustancia + formato + LLM-as-Judge. La literatura inglesa reporta
**% de retrieval accuracy** (binario: needle encontrado o no), generalmente sobre
prompts en inglés. Los rangos de contexto y scoring **no son directamente
comparables**, pero el **ranking relativo entre modelos** sí lo es.

## Tabla cruzada

| Modelo | NIAH oficial (inglés) | Variante / contexto | Nuestro NIAH-ES (0–10) | Cita |
|---|---|---|---|---|
| Gemini 3 Pro | 77.0% (avg 128K) — supera a 2.5 Pro por +9.9 puntos a 1M | MRCR v2, hasta 1M | **5.96** (avg 4K–256K) | [1] |
| Gemini 2.5 Pro | ~99% retrieval simple-needle | NIAH clásico, 1M | (no medido — 3.1 Pro sí) | [2] |
| Gemini 1.5 Pro | 99.7% recall hasta 1M; 99.2% hasta 10M | NIAH single-needle | (no medido — generación previa) | [3] |
| GPT-4.1 | 100% retrieval all positions all lengths (single-needle); MRCR mejor que GPT-4o hasta 1M | NIAH + OpenAI-MRCR, 1M | **5.86** | [4] |
| Claude Opus 4.7 | Sin reporte oficial dedicado al 4.7. Opus 4.6 = 76% en MRCR v2 8-needle 1M (vs Sonnet 4.5 = 18.5%). Opus 4.7 reporta regresión en MRCR según trackers de terceros | MRCR v2, 1M | **4.98** | [5][6] |
| Claude 3 Opus (referencia familia) | >99% accuracy NIAH single-needle (rúbrica Anthropic con 30 needle/question pairs) | NIAH-style, 200K | (no medido — generación previa) | [7] |
| DeepSeek V4 (Pro-Max) | 83.5% MRCR 1M; conditional memory paper reporta 97% NIAH 1M | MRCR-8-needle + NIAH single | **5.92** (Flash NIM) | [8] |
| Llama 4 Scout 17B | 98% retrieval @10M (NIAH single-needle, reporte Meta) | NIAH, 10M | **6.89** (Groq, 4K–128K útil) | [9] |
| Llama 3.3 70B | 97.5 NIH/Multi-Needle (igual a 3.1 70B, –0.6 vs 405B) | Multi-needle, 128K | **6.26** (Groq) | [10] |
| Mistral Small (4 / Devstral) | Sin score numérico oficial publicado por Mistral. Inspect Evals (UK BEIS) reporta NIAH "generally good across most context lengths" para mistral-small-latest, leve degradación en contextos máximos | NIAH, 128K | **7.06** / **7.25** | [11][12] |

## Hallazgos

### 1. Correlación de ranking: parcial
El ranking inglés NIAH **single-needle** (Gemini 1.5/2.5 ≈ Llama 4 ≈ GPT-4.1 ≈ 99–100% >> Claude 4.x en MRCR multi-needle) **no se traduce 1:1** a NIAH-ES. En nuestro
benchmark Devstral/Mistral lideran y los frontier (Gemini 3 Pro, GPT-4.1, Claude
Opus 4.7) quedan **abajo**. Esto sugiere dos efectos confluentes:

- **Brecha lingüística español-LATAM**: los modelos optimizados para inglés
  pierden precisión al recuperar needles en español neutro, mientras que
  Mistral (entrenado fuertemente en multilingüe europeo) preserva calidad.
- **Diferencia de rúbrica**: NIAH-ES penaliza hallucination, formato y deriva
  de idioma (chino/inglés intercalado). NIAH inglés clásico solo mide presencia
  literal del needle.

### 2. Claude Opus 4.7 último (4.98) — coherente con literatura reciente
Anthropic mismo reportó que Opus 4.6 cae a 76% en MRCR multi-needle a 1M (vs
Sonnet 4.5 con apenas 18.5%). Trackers de terceros muestran **regresión adicional
en Opus 4.7** respecto a 4.6. Nuestro 4.98 (último puesto) es **consistente** con
ese patrón: la familia Claude prioriza razonamiento sobre retrieval puro.

### 3. Gemini 3 Pro 5.96 — divergencia parcial vs literatura
Gemini 3 Pro reporta 77% MRCR a 128K (oficial) y +9.9 puntos sobre 2.5 Pro a 1M.
En NIAH-ES queda mid-table (5.96). Hipótesis: el corpus de needles en español
es donde pierde puntos; literatura inglesa no detecta esa brecha.

### 4. Devstral Small lidera (7.25) con 128K nominal
Devstral Small **no soporta 256K** y aun así lidera. Esto valida que **calidad
de retrieval ≠ tamaño de ventana**. Mistral entrena con multilingüe europeo y
preserva precisión en español, donde frontier USA-céntricos derivan.

### 5. Llama 4 Scout (6.89) > Llama 3.3 70B (6.26) — coherente con Meta
Meta reporta 98% @10M para Scout vs 97.5% multi-needle 128K para 3.3 70B.
Nuestro ranking relativo respeta el oficial.

## Limitaciones del cross-reference

- **Idioma**: 100% de los benchmarks oficiales citados están en inglés.
  NIAH-ES es el primer NIAH público en español neutro LATAM (al 30 abril 2026).
- **Métrica**: NIAH oficial = % accuracy binario. NIAH-ES = score 0–10 con
  componentes de sustancia, formato y juez. Los rangos no son aritméticamente
  comparables, solo ordinalmente.
- **Variantes NIAH**: single-needle (clásico) vs multi-needle (MRCR v2, NIH/MN)
  miden cosas distintas. Mezclamos ambos en la tabla por disponibilidad.
- **Versiones**: Gemini 1.5/2.5 Pro **no fueron medidos** en NIAH-ES (sólo 3.1
  Pro). Claude 3 Opus tampoco (sólo Opus 4.7). Comparar generaciones cruza
  tres ejes: idioma, scoring y arquitectura.

## Fuentes citadas

- [1] Vellum — Google Gemini 3 Benchmarks: <https://www.vellum.ai/blog/google-gemini-3-benchmarks>
- [2] Railwail / DeepMind blog (Gemini 2.5 Pro): <https://railwail.com/en/blog/gemini-2-5-pro-complete-guide>
- [3] Gemini 1.5 paper, arxiv 2403.05530: <https://arxiv.org/abs/2403.05530>
- [4] OpenAI — Introducing GPT-4.1: <https://openai.com/index/gpt-4-1/>
- [5] Anthropic — Introducing Claude Opus 4.6: <https://www.anthropic.com/news/claude-opus-4-6>
- [6] WentuoAI — Claude Opus 4.7 long context regression: <https://blog.wentuo.ai/en/claude-opus-4-7-long-context-regression-en.html>
- [7] Anthropic — Introducing the next generation of Claude (3 family): <https://www.anthropic.com/news/claude-3-family>
- [8] DeepSeek V4 release notes + Datacamp review: <https://api-docs.deepseek.com/news/news260424> · <https://www.datacamp.com/blog/deepseek-v4>
- [9] Meta — The Llama 4 herd: <https://ai.meta.com/blog/llama-4-multimodal-intelligence/>
- [10] Datacamp / Llama 3.3 70B benchmarks: <https://www.datacamp.com/blog/llama-3-3-70b>
- [11] Mistral — Introducing Mistral Small 4: <https://mistral.ai/news/mistral-small-4>
- [12] UK BEIS Inspect Evals NIAH (mistral-small-latest): <https://ukgovernmentbeis.github.io/inspect_evals/evals/reasoning/niah/>
- Greg Kamradt repo (autoridad de facto NIAH): <https://github.com/gkamradt/LLMTest_NeedleInAHaystack>
- Anthropic — Long context prompting Claude 2.1: <https://www.anthropic.com/news/claude-2-1-prompting>
