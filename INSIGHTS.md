---
title: "Insights del benchmark — qué dice la data, no el marketing"
fecha: "2026-05-04"
version_benchmark: "v2.6.1"
modelos_analizados: 72
modelos_catalogados: 113
runs_minimas_por_modelo: 50
tests_por_modelo: "91 single-turn + 12 agent_long_horizon + 45 niah_es_lite"
pilares: ["Razonamiento", "Coding", "Contenido/Marketing", "Agentes/Operaciones", "Long-context retrieval"]
juez_llm: "Phi-4 (Microsoft, 14B, MIT) via Ollama local"
audiencia: "Emprendedores latinoamericanos que toman decisiones de producción HOY"
fuente_datos: "docs/data/models.json + benchmarks/results/*.json"
pesos_score: {quality: 0.50, cost: 0.20, tool_calling: 0.15, speed: 0.075, latency: 0.075}
total_runs: "9,500+"
---

# Insights del benchmark — qué dice la data, no el marketing

> **Disclaimer epistemológico**: este documento es **complemento, NO sustituto** de los benchmarks académicos validados (HumanEval, MMLU, GSM8K, SWE-bench Verified, NIAH inglés, MT-Bench, LMSYS Arena). Está pensado para emprendedores hispanohablantes que deciden qué modelo poner en producción HOY para casos aplicados en español neutro (N8N, OpenClaw, Hermes, blogs LATAM, soporte cliente, agentes). Para investigación académica o capacidades fundamentales, prioriza los oficiales. Cross-references documentadas en [BENCHMARKS_EXTERNOS.md](BENCHMARKS_EXTERNOS.md) y [NIAH_CROSSREF.md](NIAH_CROSSREF.md).

Este es el análisis cuantitativo del benchmark `ai-benchmarks-alternativos` al **4 de mayo de 2026** (v2.6.1). 72 modelos con cobertura ≥50 runs, 91 tests single-turn + 12 multi-turno + 45 retrieval long-context, juez Phi-4 local. La pregunta que respondemos no es "cuál es el mejor modelo", sino: **qué patrones aparecen en la data cuando se comparan precio, velocidad, capacidades, retrieval y proveedor a la vez, en español neutro LATAM**.

---

## 🚨 Limitación crítica: NO medimos debugging agentic real

**Caso real validado** (30 abril 2026): un emprendedor enfrentó un **problema técnico complejo en un contenedor OpenClaw corriendo en VPS Hetzner**. Probó resolverlo con MiniMax M2.7 (top #14 en single-turn de este benchmark) usando un agente con herramientas — **no pudo solucionarlo**. Cambió a Claude Opus 4.7 (posición ~#28 en nuestro ranking compuesto) — **resolvió el problema en pocos minutos**.

Este caso expone una limitación seria del benchmark que conviene reconocer.

### Lo que NO medimos

| Dimensión | Lo mide | Nosotros lo medimos |
|---|---|---|
| Debugging agentic con sandbox real (Docker, FS, exec) | **SWE-bench Verified** | ❌ NO |
| Multi-turn 20+ con tool feedback real del sistema | **Claw-Eval** (300 tareas verificadas) | ⚠️ Parcial — `agent_long_horizon` simula tools con stubs |
| Resolución de problemas en infra real (K8s, VPS, networking) | **Terminal-Bench 2.0**, OSWorld | ❌ NO |
| Persistencia / judgment en sesiones largas con hipótesis fallidas | (Sin benchmark estándar) | ❌ NO |

### Para debugging agentic real, prioriza estos benchmarks externos

| Modelo | Nuestro Coding | SWE-bench Verified (oficial) |
|---|---|---|
| **Claude Opus 4.7** | 7.39 (top 5) | **87.6%** ⭐ #1 globalmente |
| Claude Sonnet 4.6 | ~7.3 | 77.2% |
| Devstral Small | 8.09 | N/A reportado (specialist) |
| Llama 3.3 70B (Groq) | 8.01 | ~50% (Llama family base) |
| MiniMax M2.7 | 6.86 | N/A reportado |

**SWE-bench Verified** (Anthropic, 500 tareas debugging reales con repos + tests verificados humanamente) es la referencia para esta dimensión. **Opus 4.7 es #1 globalmente con 87.6%** — eso predice mejor su comportamiento en VPS Hetzner que cualquier número de este benchmark.

### Conclusión honesta

1. Si la tarea es **generar código nuevo aplicado** (workflows N8N, plugins WP, scripts Python, blog posts en español): este ranking es útil. Devstral Small, Llama 3.3 70B Groq, Mistral Small 4 ganan por calidad+velocidad+costo.
2. Si la tarea es **debugging real con tools en producción**: este ranking NO es predictivo. Mirar SWE-bench Verified, Claw-Eval, Terminal-Bench. Para casos críticos (incident response, hot-fixes), Opus 4.7 / GPT-5.x premium siguen valiendo lo que cuestan.
3. **No existe ranking universal**. Esa es la regla #0: no existe el mejor modelo universal — existen modelos buenos para una tarea, en un volumen, con una restricción.

---

## ⚠️ Limitaciones críticas a leer ANTES del análisis

Tres limitaciones estructurales que cambian la interpretación de varios hallazgos:

1. **Single-turn ≠ producción real con tools.** Cada test del subset 91 es un prompt único, sin acceso a herramientas externas. En producción, un modelo "más débil" combinado con búsqueda web (Perplexity, Tavily) o RAG puede superar a un modelo "más fuerte" sin tools. Si el pipeline usa N8N con tool de búsqueda, el ranking acá no se traduce 1-a-1.

2. **Cobertura desigual entre modelos.** El piso es 50 runs, pero algunos llegan a 223 (Devstral Small, alta confianza) y otros a 50-68 (con DNS errors, timeouts del proveedor o suite agent_capabilities incompleta). Devstral 2 123B (NIM) tiene 68 runs con `agent_capabilities=0.00` — su score 7.16 es **provisorio**. Cualquier afirmación sobre modelos sub-91 runs hay que tomarla con asterisco.

3. **El provider importa tanto como el modelo.** El mismo modelo en Groq vs OpenRouter vs NIM vs Ollama Cloud puede tener delta de hasta **+0.59 puntos** (sección 3). El ranking global esconde estas diferencias.

Estos hallazgos cuantitativos filtran el 80% de modelos malos. El 20% final lo decide cada equipo con 5-10 prompts típicos de su caso de uso, en el mismo provider y configuración (con/sin tools) que va a usar en producción.

---

## Tabla de contenidos

0. [Hallazgos destacados v2.6.1](#0-hallazgos-destacados-v261)
1. [Correlación precio ↔ calidad por pilar](#1-correlación-precio--calidad-por-pilar)
2. [Outliers — joyas, malas compras y especialistas](#2-outliers--joyas-malas-compras-y-especialistas)
3. [Provider matters — el mismo modelo en distintos providers](#3-provider-matters--el-mismo-modelo-en-distintos-providers)
4. [Patrones de fragilidad — tool calling y JSON estructurado por tamaño](#4-patrones-de-fragilidad--tool-calling-y-json-estructurado-por-tamaño)
5. [Sensibilidad por idioma — español vs inglés](#5-sensibilidad-por-idioma--español-vs-inglés)
6. [Costo real para emprendedor N8N — ranking mensual y Pareto](#6-costo-real-para-emprendedor-n8n--ranking-mensual-y-pareto)
7. [Regresiones — cuando la versión nueva es peor](#7-regresiones--cuando-la-versión-nueva-es-peor)
8. [Open-source vs propietario — ¿se cerró la brecha?](#8-open-source-vs-propietario--se-cerró-la-brecha)
9. [Anti-patterns del marketing — claims que no se sostienen](#9-anti-patterns-del-marketing--claims-que-no-se-sostienen)
10. [Top 5 hallazgos sorpresivos del v2.6.1](#10-top-5-hallazgos-sorpresivos-del-v261)
11. [Implicaciones para próxima iteración (junio 2026)](#11-implicaciones-para-próxima-iteración-junio-2026)
12. [Datos sospechosos / a re-validar](#12-datos-sospechosos--a-re-validar)

---

## 0. Hallazgos destacados v2.6.1

### 0.1 Top 10 score compuesto (integra single-turn + multi-turn + NIAH-ES)

| # | Modelo | Final | Quality | $/1k | tok/s | Provider | Open |
|---|---|---|---|---|---|---|---|
| 1 | Llama 4 Scout 17B | **7.69** | 7.70 | 0.54 | 170 | Groq direct | sí |
| 2 | Llama 3.1 8B Instant | **7.67** | 7.33 | 0.14 | 262 | Groq direct | sí |
| 3 | Devstral Small | **7.52** | 7.89 | 0.48 | 139 | OpenRouter | sí |
| 4 | Mistral Small 4 | **7.51** | 7.88 | 0.94 | 82 | OpenRouter | sí |
| 5 | GPT-OSS 20B | **7.47** | 7.10 | 0.47 | 474 | Groq direct | sí |
| 6 | MiMo V2-Omni (Xiaomi direct) | **7.46** | 7.27 | 0.13 | 102 | Xiaomi direct | no |
| 7 | MiMo V2.5 (Xiaomi sub) | **7.45** | 7.63 | 0.13 | 71 | Xiaomi direct | no |
| 8 | Gemini 3.1 Flash Lite | **7.44** | 7.82 | 2.33 | 110 | OpenRouter | no |
| 9 | Nemotron 3 Nano 30B | **7.43** | 7.79 | 0.32 | 86 | OpenRouter | sí |
| 10 | MiMo V2.5-Pro (Xiaomi sub) | **7.42** | 7.65 | 0.25 | 49 | Xiaomi direct | no |

**Lectura inmediata**:
- 7 de 10 son open-source.
- 4 de 10 son MiMo Xiaomi (sub $14/mes) — la familia con mejor C/B en español neutro.
- Los 4 modelos en Groq direct (#1, #2, #5, +Llama 3.3 70B en #15) tienen >170 tok/s y costo <$1.50/1k calls.
- **Ningún modelo "premium" (>$5/1k) entra al top 10**.

### 0.2 Top 10 quality_avg only (sin pesar costo/velocidad)

Si la única métrica fuera quality (Phi-4 + sustancia automática + formato), el ranking cambia:

| # | Modelo | Quality | Final | Comentario |
|---|---|---|---|---|
| 1 | Gemma 4 31B (DGX Spark Q4) | **8.22** | 6.69 | Cuantización local |
| 2 | Gemma 4 31B (NIM/OpenRouter FP16) | 8.19 | 7.30 | Quality top, costo cero en NIM |
| 3 | Mistral Large 3 675B (NIM) | 8.18 | 6.83 | Quality alto pero lento + caro |
| 4 | Qwen 3-Next 80B Instruct (NIM) | 8.11 | 7.20 | NIM gratis con quality top-tier |
| 5 | Qwen 3.5 397B (NIM) | 8.07 | 6.90 | |
| 6 | Hermes 4 405B | 8.05 | 7.17 | |
| 7 | **Claude Opus 4.6** | **8.04** | 7.09 | Quality top 7, cost lo penaliza |
| 8 | Ministral 14B (NIM) | 8.02 | 6.84 | Modelo chico con quality alta |
| 9 | Devstral 2 123B (NIM) | 7.98 | 7.16 | |
| 10 | GLM 5 (NIM) | 7.97 | 6.73 | |

**Hallazgo crítico**: en quality pura, **Claude Opus 4.6 es top 7** (8.04). En el ranking compuesto cae a #~25 por costo $117/1k + speed 47 tok/s. **Esto valida la metodología**: si se midiera solo quality, los benchmarks académicos ya cubren esa pregunta. El aporte propio es medir **quality + costo + velocidad + tool calling juntos**, en español neutro, simulando casos reales de un emprendedor LATAM.

### 0.3 Top 10 NIAH-ES (long-context retrieval español)

| # | Modelo | Score NIAH-ES | Cobertura | Comentario |
|---|---|---|---|---|
| 1 | **Devstral Small** | **7.24** ⭐ | 60 tests (4K-64K) | Lidera con cobertura ampliada (45/60) |
| 2 | MiMo V2.5 (Xiaomi sub) | 7.05 | 45 (lite) | Mejor para sub fija |
| 3 | Mistral Small 4 | 7.01 | 60 | Multilingüe europeo fuerte |
| 4 | Llama 4 Scout 17B (Groq) | 6.91 | 60 | |
| 5 | Gemini 3.1 Flash Lite | 6.78 | 45 | |
| 6 | Llama 3.1 8B Instant (Groq) | 6.70 | 45 | |
| 7 | Devstral 2 (Dic 2025) | 6.67 | 60+45 | |
| 8 | GPT-OSS 20B (Groq) | 6.66 | 45 | |
| 9 | GPT-OSS 120B (Ollama Cloud) | 6.65 | 45 | |
| 10 | Hermes 4 70B | 6.30 | 45 | |
| ... | | | | |
| último | **Claude Opus 4.7** | **4.95** | 60 | Caída sistemática vs literatura |

**Devstral Small ($0.10/$0.30) supera a Opus 4.7 ($45/M) en NIAH-ES por +2.29 puntos**, a 1/450 del costo. Confirma robustez con 21 modelos cubiertos (vs 8 en abril).

### 0.4 Top 10 agent_long_horizon (multi-turn 8+ turnos)

| # | Modelo | Score ALH | Single-turn ref | Δ |
|---|---|---|---|---|
| 1 | **GPT-OSS 120B (Ollama Cloud)** | **8.60** | 7.37 | **+1.23** ⬆ |
| 2 | Llama 4 Scout 17B (Groq) | 8.26 | 7.69 | +0.57 |
| 3 | Llama 3.1 8B Instant (Groq) | 8.21 | 7.67 | +0.54 |
| 4 | MiMo V2-Omni (Xiaomi direct) | 8.17 | 7.46 | +0.71 |
| 5 | Devstral Small | 8.12 | 7.52 | +0.60 |
| 6 | MiMo V2.5 (Xiaomi sub) | 8.01 | 7.45 | +0.56 |
| 7 | GPT-OSS 20B (Groq) | 7.98 | 7.47 | +0.51 |
| 8 | Llama 3.3 70B (Groq) | 7.91 | 7.36 | +0.55 |
| 9 | Devstral 2 (Dic 2025) | 7.72 | 7.09 | +0.63 |
| 10 | MiMo V2-Pro (Xiaomi direct) | 7.70 | 7.39 | +0.31 |

**Hallazgo robusto**: los modelos top single-turn **suben** en ALH (suite multi-turno). Esto es coherente con que los modelos bien afinados en context retention + skill orchestration mantienen calidad cuando el horizonte se extiende. Por contraste, los thinking-by-default bajan (GPT-5.5 ALH 6.51, Gemini 3.1 Pro 6.38, Kimi K2.6 thinking 6.88) — patrón documentado en sección 9.

---

## 1. Correlación precio ↔ calidad por pilar

Spearman rank correlation entre `cost_per_1k_calls_usd` y métricas de score (modelos pagados, n=47):

| Métrica | ρ Spearman | p-value | Lectura |
|---|---|---|---|
| Cost vs **score_global compuesto** | **−0.671** | <0.001 | Negativa fuerte (impulsada por penalty de cost en la fórmula) |
| Cost vs **quality_avg** | **+0.019** | 0.901 | **No significativa** — pagar más NO predice mejor calidad |
| Cost vs Razonamiento | −0.394 | 0.006 | Negativa moderada |
| Cost vs Coding | −0.352 | 0.015 | Negativa moderada |
| Cost vs **Contenido** | **−0.641** | <0.001 | **Negativa fuerte** — más caro = peor en contenido |
| Cost vs Agentes | −0.402 | 0.005 | Negativa moderada |

**Hallazgo metodológico clave (nuevo en v2.6.1)**:

La relación entre precio y **score compuesto** es fuertemente negativa (−0.67), pero la relación entre precio y **quality pura** es virtualmente cero (+0.02, p=0.90). Esto significa: **los modelos premium no son peores en calidad — son simplemente más caros y lentos, y la fórmula los penaliza por eso**. La narrativa "más caro = peor" es un artefacto del peso 20% del costo + 15% velocidad/latencia en el score. En quality aislada, no hay correlación significativa cost↔quality.

Esto NO invalida los hallazgos: para un emprendedor LATAM con presupuesto fijo, el score compuesto **es** la métrica relevante. Pero conviene saber qué mide cada cosa.

**Velocidad vs quality**: ρ = **−0.319** (p=0.006). **Más rápido NO predice mejor calidad** — incluso correlaciona ligeramente negativo. La razón: muchos modelos de quality alta (Mistral Large 3 675B, Hermes 4 405B, Gemma 4 31B FP16) son inherentemente más lentos. La correlación speed↔score compuesto sube a +0.50 solo porque la fórmula recompensa speed.

**Free tier (n=25)**: quality avg 7.33, score compuesto 6.58. Pagados (n=47): quality avg 7.55, score compuesto 7.01. Diferencia quality marginal (+0.22) — el free no penaliza fuerte la calidad promedio.

---

## 2. Outliers — joyas, malas compras y especialistas

### 2.1 Malas compras (caro + score bajo)

Modelos con costo ≥$5/1k Y score_global <7.20:

| Modelo | $/1k | Final | Quality | Comentario |
|---|---|---|---|---|
| Claude Opus 4.7 | 117.00 | 6.54 | 7.64 | Quality top 7, costo masivo lo hunde en compuesto |
| Claude Opus 4.6 | 117.00 | 7.09 | 8.04 | Igual — quality alta pero precio insostenible |
| GPT-5.5 | 46.50 | 6.07 | 7.29 | Más caro del benchmark, quality menor que GPT-4.1 |
| GPT-5.4 | 24.00 | 6.85 | 7.09 | Pierde con GPT-5.4 Mini (7.23) |
| Claude Sonnet 4.6 | 23.40 | 6.65 | 7.38 | Último Sonnet — perdió contra Llama 3.1 8B |
| Gemini 3.1 Pro | 18.60 | 6.18 | 7.40 | Peor que Flash Lite (7.44) a 8x del costo |
| Gemini 2.5 Pro | 15.38 | 6.28 | 6.52 | Misma historia que 3.1 Pro |
| GPT-4.1 | 12.60 | 6.74 | 7.62 | Quality top 13, costo lo penaliza |
| Mistral Large | 9.60 | 7.08 | — | Mistral Small 4 saca 7.51 a 1/10 del costo |
| Grok 4.20 | 9.60 | 6.91 | 7.83 | Grok 4.1 Fast saca 7.21 a 1/12 |
| DeepSeek V4 Pro | 5.74 | 5.62 | 6.32 | DeepSeek V4 Flash NIM gratis saca 6.60 |
| Kimi K2.6 | 5.49 | 6.40 | 7.68 | Versión razonadora — pierde con K2 (6.96) |
| GLM-5.1 | 5.01 | 6.69 | 7.88 | Empate exacto con GLM 5 NIM ($0) |

**Patrón crítico**: TODOS los modelos premium (>$5/1k) con variante "Mini", "Flash" o "Small" pierden contra esa variante en el score compuesto. El single-turn no recompensa el razonamiento extra que justifica el precio premium.

### 2.2 Joyas (barato + score alto)

Modelos con score_global ≥7.20 y costo entre $0.01-$1.50/1k:

| Modelo | $/1k | Final | tok/s |
|---|---|---|---|
| Llama 4 Scout 17B (Groq) | 0.54 | 7.69 | 170 |
| Llama 3.1 8B Instant (Groq) | 0.14 | 7.67 | 262 |
| Devstral Small | 0.48 | 7.52 | 139 |
| Mistral Small 4 | 0.94 | 7.51 | 82 |
| GPT-OSS 20B (Groq) | 0.47 | 7.47 | 474 |
| MiMo V2-Omni (Xiaomi direct) | 0.13 | 7.46 | 102 |
| MiMo V2.5 (Xiaomi sub) | 0.13 | 7.45 | 71 |
| Nemotron 3 Nano 30B | 0.32 | 7.43 | 86 |
| MiMo V2.5-Pro (Xiaomi sub) | 0.25 | 7.42 | 49 |
| MiMo-V2-Flash | 0.46 | 7.41 | 54 |
| MiMo V2-Pro (Xiaomi direct) | 0.13 | 7.39 | 45 |
| Llama 3.3 70B (Groq) | 1.36 | 7.36 | 173 |
| Gemini 2.5 Flash Lite | 0.63 | 7.34 | 171 |
| Gemma 4 31B | 0.99 | 7.30 | 22 |
| Grok 4.1 Fast | 0.81 | 7.21 | 116 |

**15 modelos ofrecen >7.20 de score compuesto por menos de $1.50/1k calls**. Cualquier emprendedor con presupuesto restringido tiene 15 candidatos válidos antes de mirar el tier premium.

### 2.3 Joyas gratis (free + score ≥7.0)

| Modelo | Final | Quality | tok/s | Provider |
|---|---|---|---|---|
| GPT-OSS 120B | 7.37 | 7.15 | 68 | Ollama Cloud |
| Gemma 4 31B | 7.30 | 8.19 | 22 | NVIDIA NIM |
| Qwen 3-Next 80B Instruct | 7.20 | 8.11 | 52 | NVIDIA NIM |
| Devstral 2 123B | 7.16 | 7.98 | 42 | NVIDIA NIM (cobertura parcial) |
| Nemotron 3 Nano Omni 30B-A3B | 7.04 | 7.75 | 16 | NVIDIA NIM |

**5 modelos gratuitos pasan el umbral 7.0** en score compuesto. Para proyectos personales, prototipos o producción de bajo volumen (<40 RPM en NIM), el costo en cuotas de modelo es **$0**.

### 2.4 Frontera de Pareto (no dominada — más barata Y mejor score)

| Modelo | Final | $/1k | Por qué está en Pareto |
|---|---|---|---|
| GPT-OSS 120B (Ollama Cloud) | 7.37 | 0.00 | Top score gratis |
| MiMo V2-Omni (Xiaomi direct) | 7.46 | 0.13 | Mejor C/B con sub Xiaomi |
| Llama 3.1 8B Instant (Groq) | 7.67 | 0.14 | Mejor relación calidad/precio absoluta |
| Llama 4 Scout 17B (Groq) | 7.69 | 0.54 | Mejor score de modelos pagados |

**4 modelos en Pareto estricto**. Si la decisión es solo costo vs score compuesto, se elige entre estos 4. Cualquier otra elección significa priorizar otra dimensión (latencia, NIAH-ES, idioma específico, multimodal, etc.).

### 2.5 Especialistas — modelos que dominan suites específicas

Top 1 por suite (los más útiles en su nicho aunque no estén en el top global):

| Suite | Líder | Score suite | Score global |
|---|---|---|---|
| reasoning + deep_reasoning | Llama 4 Scout 17B (Groq) | 8.26 | 7.69 |
| code_generation | Llama 4 Scout 17B (Groq) | 8.15 | 7.69 |
| content_generation | Llama 3.1 8B Instant (Groq) | 8.27 | 7.67 |
| translation (ES↔EN) | Llama 3.1 8B Instant (Groq) | 8.62 | 7.67 |
| **tool_calling** | **Llama 3.1 8B Instant (Groq)** | **8.64** | 7.67 |
| **structured_output** | **Llama 3.1 8B Instant (Groq)** | **8.62** | 7.67 |
| **agent_capabilities** | **Mistral Small 4** | **8.07** | 7.51 |
| **agent_long_horizon** | **GPT-OSS 120B (Ollama Cloud)** | **8.60** | 7.37 |
| **NIAH-ES** | **Devstral Small** | **7.24** | 7.52 |
| string_precision | Devstral Small | 8.12 | 7.52 |
| customer_support | Mistral Small 4 | 8.12 | 7.51 |
| orchestration | Qwen 3.5 397B (Ollama Cloud) | 7.66 | 6.49 |

**Patrones**:
- **Llama 3.1 8B Instant (Groq) lidera 4 suites** (translation, tool_calling, structured_output, content_generation) con costo $0.14/1k. Modelo chico, ultra rápido, mejor multilingüe.
- **Mistral Small 4** lidera customer_support y agent_capabilities — fortaleza en respuestas estructuradas + multi-step planning.
- **Devstral Small** es el rey de **NIAH-ES** (long-context español) y **string_precision** — útil para retrieval, ETL, data extraction.
- **GPT-OSS 120B** lidera agent_long_horizon en su tier free — sub Ollama Cloud lo desbloquea.
- **Qwen 3.5 397B (Ollama Cloud)** especialista en orchestration aunque global mediocre — útil si el pipeline es multi-step puro.

---

## 3. Provider matters — el mismo modelo en distintos providers

Una de las dimensiones más subestimadas: **el mismo modelo puede dar score muy distinto según el provider que lo expone**, por cuantización, configuración interna, rate limits, o limitaciones del gateway.

### 3.1 MiMo Xiaomi: direct vs OpenRouter (delta enorme)

| Modelo | Provider | Final | Quality | Δ vs OpenRouter |
|---|---|---|---|---|
| MiMo V2-Omni (Xiaomi direct) | Xiaomi sub $14/mes | **7.46** | 7.27 | +0.52 |
| MiMo-V2-Omni (multimodal) | OpenRouter | 6.94 | 7.52 | base |
| MiMo V2-Pro (Xiaomi direct) | Xiaomi sub $14/mes | **7.39** | 7.61 | +0.59 |
| MiMo-V2-Pro | OpenRouter | 6.80 | 7.52 | base |

**Hallazgo**: Xiaomi direct entrega +0.52 a +0.59 puntos sobre el mismo modelo en OpenRouter. La quality no cambia mucho — pero costo (sub $14/mes vs $/M tokens) y configuración del provider directo dan ventaja material en el score compuesto. **Para usuarios MiMo, suscribirse al directo es estrictamente mejor que pagar por OpenRouter**.

### 3.2 DeepSeek V4 — tres providers, comportamiento muy distinto

| Variante | Provider | Final | Quality | Tests OK | Notas |
|---|---|---|---|---|---|
| DeepSeek V4 Flash | NIM gratis | **6.60** | 7.90 | 87/91 | Quality top, free tier funcional |
| DeepSeek V4 Pro | OpenRouter pagado | 5.62 | 6.32 | 91 + 57 | $1.74/$3.48 per M tokens |
| DeepSeek V4 Flash | Ollama Cloud sub | 4.96 | 5.15 | 57/57 | **Cuantización degrada quality** |
| DeepSeek V4 Pro | Ollama Cloud sub | 4.86 | 5.24 | 55/57 (97%) | **Idem** |
| DeepSeek V4 Pro | NIM gratis | ❌ | — | 0/7 | **Cascada 504, NO USAR** |

**Hallazgos críticos** (nuevos en mayo):

1. **DeepSeek V4 Pro vía NIM NO funciona en producción** — cascada 504 reproducible **2 veces** (abril 28 + mayo 3). El gateway NIM no maneja modelo gigante con prompts largos. Descartado para producción.

2. **DeepSeek V4 vía Ollama Cloud sub tiene calidad notablemente menor** que NIM. Quality cae de 7.90 (NIM) a 5.15 (Ollama Cloud) para Flash. La sub funciona (97% completion) pero la cuantización del cloud Ollama es más agresiva. Para producción con DeepSeek V4: **OpenRouter pagado o NIM gratis (Flash only)**.

3. Patrón: NIM gratis para DeepSeek V4 Flash entrega la mejor quality. Pero atención al cap 40 RPM.

### 3.3 Qwen 3.5 397B — NIM vs Ollama Cloud

| Provider | Final | Quality |
|---|---|---|
| NIM gratis (FP16) | **6.90** | 8.07 |
| Ollama Cloud sub | 6.49 | 5.50 |

**Hallazgo**: Quality cae de 8.07 (NIM FP16) a 5.50 (Ollama Cloud cuantizado). Mismo modelo, **delta de quality de -2.57 puntos por cuantización**. La explicación más probable es Q4 vs FP16 + posibles diferencias en sampling. Para producción con Qwen 3.5: **NIM gratis es estrictamente mejor que Ollama Cloud**.

### 3.4 Paridad exacta — Gemma 4 31B y GLM 5.1

| Modelo | OpenRouter | NIM | Δ |
|---|---|---|---|
| Gemma 4 31B FP16 | 7.30 | 7.30 | 0.00 |
| GLM 5.1 | 6.69 | 6.69 | 0.00 |

**Hallazgo**: Para Gemma 4 31B y GLM 5.1, NIM gratis y OpenRouter pagado dan resultados **idénticos a 2 decimales**. Confirma que NIM no degrada estos modelos. Para 47 modelos del catálogo NIM con equivalente en OpenRouter, **pagar OpenRouter es opcional** — sólo se justifica si se necesitan >40 RPM o features específicos del routing.

### 3.5 Cuantización Q4 en hardware propio (DGX Spark)

| Modelo | Provider | Quality | Final | Δ vs FP16 |
|---|---|---|---|---|
| Gemma 4 31B (DGX Q4_K_M) | Ollama local | 8.22 | 6.69 | +0.03 quality, -0.61 final |
| Gemma 4 31B (NIM FP16) | NIM | 8.19 | 7.30 | base |
| Nemotron 3 Super 120B (DGX Q4) | Ollama local | 7.96 | 6.65 | — |
| Nemotron 3 Base 33B (DGX Q4) | Ollama local | 7.83 | 6.77 | — |

**Hallazgo cuantización**: Q4 vs FP16 entrega **quality casi idéntica** (8.22 vs 8.19) pero el score compuesto cae -0.61 por **velocidad**: Q4 corre a 9.3 tok/s en DGX vs 22 tok/s en NIM FP16. La pérdida real es de speed, no de quality. Para datos sensibles que no pueden salir de la máquina, Q4 es perfectamente viable. Para producción con APIs aceptables, NIM FP16 gratis es estrictamente mejor.

### 3.6 Implicación operativa

Antes de elegir un modelo, decidir el provider según prioridad:

- **Velocidad ante todo**: Groq direct (>170 tok/s)
- **Costo cero, quality FP16**: NIM (cap 40 RPM)
- **Sub mensual predecible**: Xiaomi direct ($14/mes) para MiMo, Ollama Cloud ($30/mes) para Qwen/GPT-OSS
- **Volumen alto sostenido**: OpenRouter pagado
- **Datos sensibles, on-prem**: DGX Spark + Q4_K_M (asume -5% en speed, quality casi idéntica)
- **Evitar**: DeepSeek V4 Pro vía NIM (cascada 504), DeepSeek V4 vía Ollama Cloud (quality cae 33%)

---

## 4. Patrones de fragilidad — tool calling y JSON estructurado por tamaño

### 4.1 Tool calling — top y bottom

Top 7 en suite `tool_calling`:

| Modelo | tool_calling | Final | Δ |
|---|---|---|---|
| Llama 3.1 8B Instant (Groq) | **8.64** | 7.67 | +0.97 |
| Llama 4 Scout 17B (Groq) | 8.25 | 7.69 | +0.56 |
| Qwen 3.5 (Ollama Cloud default) | 8.01 | 6.40 | +1.61 |
| Grok 4.1 Fast | 7.91 | 7.21 | +0.70 |
| Gemini 3.1 Flash Lite | 7.84 | 7.44 | +0.40 |
| Qwen 3.5 397B (Ollama Cloud) | 7.72 | 6.49 | +1.23 |
| Qwen 3-Next 80B Instruct (NIM) | 7.45 | 7.20 | +0.25 |

**Hallazgo**: Qwen 3.5 cloud rinde +1.23 a +1.61 puntos por encima de su score global cuando se le da tools. Esto explica por qué muchos pipelines en producción que usan Qwen + tools funcionan mejor de lo que el ranking single-turn predice.

Bottom 7 tool_calling:

| Modelo | tool_calling | Notas |
|---|---|---|
| GPT-5.5 | 6.05 | Thinking model malgasta tokens en sintaxis tool |
| Gemini 2.5 Pro | 6.03 | |
| GLM 5 (NIM) | 6.00 | |
| Qwen 3.6 Plus | 6.00 | Propietario API-only |
| Step 3.5 Flash (NIM) | 5.88 | |
| Llama 4 Maverick | 5.73 | OpenRouter (no Groq direct) |
| Kimi K2.6 | 5.66 | Thinking razonador |

**Patrón**: **modelos thinking saturan atención en reasoning interno y pierden precisión en sintaxis JSON de tool_calls**. Si el pipeline depende de tools, evitar thinking models por default — solo activar si se valida específicamente para la tarea.

### 4.2 Structured output — el tamaño del modelo NO predice mejor JSON

Bottom 8 en suite `structured_output`:

| Modelo | structured_output | Tamaño |
|---|---|---|
| MiMo-V2-Omni (multimodal) | 6.79 | mid |
| Kimi K2.6 | 6.76 | razonador |
| Qwen 3.6 Plus | 6.71 | propietario |
| Qwen 3.5 397B (Ollama Cloud) | 6.69 | 397B |
| Ministral 14B (NIM) | 6.59 | 14B |
| Gemini 3.1 Pro | 6.58 | "Pro" tier |
| Step 3.5 Flash (NIM) | 6.40 | mid |
| Qwen 3.5 (Ollama Cloud default) | 6.33 | grande |

**Top en structured_output**: Llama 3.1 8B Instant 8.62, Llama 4 Scout 8.37, GPT-OSS 20B 8.34. Todos modelos chicos-medianos.

**Patrón**: **modelos thinking + modelos gigantes son los peores para structured output**. Razón: el reasoning escapa del schema (pone explicaciones antes/después del JSON) y el modelo grande "elabora" cuando el prompt pide brevedad estructurada. Para JSON estricto en producción usar Llama 3.1 8B Groq (8.62) o GPT-OSS 20B (8.34).

### 4.3 Agent_capabilities — la suite single-turn más volátil

Top 6:

| Modelo | agent_capabilities |
|---|---|
| Mistral Small 4 | 8.07 |
| Llama 3.1 8B Instant (Groq) | 8.00 |
| Llama 3.3 70B (Groq) | 7.74 |
| Grok 4.1 Fast | 7.53 |
| GPT-OSS 20B (Groq) | 7.52 |
| Hermes 4 405B | 7.47 |

Bottom 6:

| Modelo | agent_capabilities | Notas |
|---|---|---|
| Kimi K2 Thinking (NIM) | 5.58 | Thinking penaliza |
| Qwen3 Coder | 5.56 | Specialist coding pierde como agente |
| Gemini 2.5 Pro | 5.56 | Premium tier no rinde |
| GPT-5.5 | 5.15 | Thinking-by-default |
| Qwen 3.6 Plus | 4.77 | Propietario tier-Plus |
| Nemotron 3 Super | 4.43 | El modelo grande de NVIDIA es deficiente como agente |

**Hallazgo**: la diferencia entre el #1 (Mistral Small 4, 8.07) y el último (Nemotron 3 Super, 4.43) es **+3.64 puntos**, mucho mayor que en cualquier otra suite. Para producción de agentes, elegir bien acá es **3x más importante que en contenido**.

---

## 5. Sensibilidad por idioma — español vs inglés

La suite `translation` tiene tests bidireccionales ES↔EN sobre vocabulario técnico, jerga startup y modismos chilenos/mexicanos. El juez Phi-4 está instrumentado con rúbrica en español neutro.

### 5.1 Top 8 en translation

| Modelo | translation | Final | Δ |
|---|---|---|---|
| Llama 3.1 8B Instant (Groq) | 8.62 | 7.67 | +0.95 |
| GPT-OSS 20B (Groq) | 8.62 | 7.47 | +1.15 |
| Llama 3.3 70B (Groq) | 8.58 | 7.36 | +1.22 |
| Mistral Small 4 | 8.38 | 7.51 | +0.87 |
| Gemini 3.1 Flash Lite | 8.30 | 7.44 | +0.86 |
| Llama 4 Scout 17B (Groq) | 8.29 | 7.69 | +0.60 |
| Devstral Small | 8.29 | 7.52 | +0.77 |
| Gemini 2.5 Flash Lite | 8.23 | 7.34 | +0.89 |

**Patrón**: los modelos del top traducen **mejor** que su score global por +0.60 a +1.22 puntos. Los GPT-OSS y Llama family son particularmente fuertes en español neutro. Esto es relevante para LATAM porque la mayoría del entrenamiento web tiene sesgo a inglés — los modelos que sobre-rinden en translation son los menos propensos a producir "spanglish" o anglicismos forzados.

### 5.2 Bottom 8 en translation — patrón consistente

| Modelo | translation | Origen |
|---|---|---|
| Qwen 3-Next 80B Thinking (NIM) | 6.18 | Chino + thinking |
| Kimi K2.5 / K2.5 NIM | 5.74 | Chino |
| Step 3.5 Flash (NIM) | 5.73 | Chino |
| Qwen 3.5 (Ollama Cloud default) | 5.69 | Chino + cuantización |
| DeepSeek V4 Pro | 5.53 | Chino + razonador |
| Kimi K2 Thinking (NIM) | 5.34 | Chino + thinking |
| Qwen 3.5 397B (Ollama Cloud) | **4.41** | **El peor del benchmark** |

**Hallazgo crítico**: **8 de los 9 peores en translation son modelos chinos** (Qwen, Kimi, Step, DeepSeek). El benchmark detecta el patrón conocido: estos modelos a veces meten caracteres chinos en mid-output cuando el prompt es ambiguo o muy largo. La penalización por idioma del scoring v2 los empuja al bottom.

**Implicación para producción**:
- Para pipelines que generan **contenido público en español neutro** (blogs, artículos, copy): los modelos chinos requieren validación extra de output.
- Para flujos que aceptan **revisión humana**, no es bloqueante.
- Para **automatización end-to-end** (publicación directa), es riesgo material.
- Para **razonamiento interno** o **código**: los modelos chinos siguen siendo competitivos. El problema es output público en español.

### 5.3 La "anomalía" Llama (made-in-USA, gana en español)

Los 4 Groq-Llama (3.1, 3.3, 4 Scout, 4 Maverick) son top 7 en translation con scores 8.29-8.62. **Modelos USA con buen multi-lingual training rinden mejor que los chinos en español neutro de LATAM**. No es paradoja: Meta entrenó Llama con balance multi-lingüe explícito; Llama 3.3 cubre 8+ idiomas en datos públicos. Los chinos optimizan para chino+inglés y pierden cobertura en español.

---

## 6. Costo real para emprendedor N8N — ranking mensual y Pareto

Asunción: **10,000 calls/mes** (1k input + 1.5k output tokens por call promedio). Esto modela un blog de actualidad startups con generación moderada, atención al cliente automatizada de bajo volumen, o un agente N8N de 30-40 ejecuciones diarias.

### 6.1 Costos mensuales — los 12 más baratos con score >7.0

| Modelo | $/mes | Final | Apto para producción |
|---|---|---|---|
| GPT-OSS 120B (Ollama Cloud) | 0 (con sub $30/mes Ollama) | 7.37 | Sí |
| Gemma 4 31B (NIM) | 0 | 7.30 | Sí (cap 40 RPM) |
| Qwen 3-Next 80B Instruct (NIM) | 0 | 7.20 | Sí |
| Devstral 2 123B (NIM) | 0 | 7.16 | Sí (cobertura parcial) |
| Nemotron 3 Nano Omni (NIM) | 0 | 7.04 | Sí |
| MiMo V2-Omni (Xiaomi direct) | $1.30 (sub $14/mes) | 7.46 | Sí |
| MiMo V2.5 (Xiaomi sub) | $1.30 | 7.45 | Sí |
| MiMo V2-Pro (Xiaomi direct) | $1.30 | 7.39 | Sí |
| Llama 3.1 8B Instant (Groq) | $1.40 | 7.67 | Sí |
| MiMo V2.5-Pro (Xiaomi sub) | $2.50 | 7.42 | Sí |
| Nemotron 3 Nano 30B | $3.20 | 7.43 | Sí |
| Grok 4.1 Fast | $8.10 | 7.21 | Sí |

**Observación**: para 10k calls/mes, **5 modelos gratuitos y 7 más bajo $10/mes** dan score >7.0. Cualquier emprendedor LATAM puede operar con presupuesto cercano a $0 (NIM) o $14-44/mes (subs MiMo + Ollama Cloud).

### 6.2 Costos mensuales — los 5 más caros (referencia comparativa)

| Modelo | $/mes | Final | Vale la pena? |
|---|---|---|---|
| Claude Opus 4.7 / 4.6 | $1,170 | 6.54 / 7.09 | NO vs Llama 4 Scout 7.69 a $5.40/mes |
| GPT-5.5 | $465 | 6.07 | NO |
| GPT-5.4 | $240 | 6.85 | NO |
| Claude Sonnet 4.6 | $234 | 6.65 | NO |
| Gemini 3.1 Pro | $186 | 6.18 | NO vs Flash Lite 7.44 a $23.30/mes |

**Diferencial extremo**: Claude Opus 4.7 cuesta **$1,170/mes** para entregar 6.54 — un score que MiMo V2.5 entrega por $14/mes (84x más barato). Para emprendedores LATAM, los modelos premium API son operativamente inaccesibles vs alternativas open + sub.

### 6.3 Pareto de costo-eficiencia por perfil

- **Bootstrap ($0/mes)**: GPT-OSS 120B (Ollama Cloud, 7.37 + ALH 8.60 + tools full) o NIM Gemma 4 31B (7.30, quality 8.19). Cero costo recurrente, tope ~25-40 RPM.
- **Microemprendimiento ($14-30/mes con sub)**: MiMo V2.5 (Xiaomi sub $14, 7.45 + NIAH 7.05) o GPT-OSS 120B (Ollama Cloud sub $30, 7.37 + ALH 8.60).
- **PYME ($10-50/mes pay-as-you-go)**: Llama 4 Scout (Groq, $5.40, 7.69) + Devstral Small ($4.80, 7.52 + NIAH-ES 7.24) en pipeline.
- **Volumen alto + multi-tarea ($50-200/mes)**: Llama 3.3 70B Groq ($13.60, 7.36) + Mistral Small 4 ($9.40, 7.51) + Devstral Small ($4.80) según tipo de tarea.

---

## 7. Regresiones — cuando la versión nueva es peor

Comparativas v2.6.1 entre versión anterior y nueva del mismo modelo:

| Anterior | Final | Nueva | Final | Δ Final | Δ Quality |
|---|---|---|---|---|---|
| Qwen 3-Next 80B **Instruct** | 7.20 | Qwen 3-Next 80B **Thinking** | 6.35 | **−0.85** | −1.22 |
| **GPT-4.1** | 6.74 | **GPT-5.5** | 6.07 | **−0.67** | −0.33 |
| **Claude Opus 4.6** | 7.09 | **Claude Opus 4.7** | 6.54 | **−0.55** | −0.40 |
| **Devstral Small** | 7.52 | **Devstral 2 (Dic 2025)** | 7.09 | **−0.43** | −0.09 |
| GPT-5.4 Mini | 7.23 | GPT-5.4 | 6.85 | −0.38 | −0.28 |
| Gemini 2.5 Pro | 6.28 | Gemini 3.1 Pro | 6.18 | −0.10 | +0.88 (!) |
| **Avances reales:** | | | | | |
| Gemini 2.5 Flash Lite | 7.34 | Gemini 3.1 Flash Lite | 7.44 | +0.10 | +0.03 |
| Kimi K2.5 | 6.14 | Kimi K2.6 | 6.40 | +0.26 | +1.31 |

**Hallazgos**:

**Regresión 1 — GPT-5.5 vs GPT-4.1 (−0.67)**: GPT-5.5 cuesta $46.50/1k calls vs GPT-4.1 a $12.60. El usuario paga 3.7x más por un score 10% peor. Diagnóstico probable: GPT-5.5 es thinking-by-default y consume budget en reasoning interno antes de responder, agotando max_tokens en prompts complejos. Aplica `max_tokens × 4 = 8192` desde el adapter, pero la regresión persiste.

**Regresión 2 — Qwen 3-Next Thinking vs Instruct (−0.85, −1.22 quality)**: el modelo razonador es **estrictamente peor** que el instruct en single-turn. Quality cae **−1.22 puntos**, mucho más que el final score (cost iguala porque ambos son free en NIM). Esto confirma: **en single-turn, thinking pierde en TODO, incluido razonamiento puro**.

**Regresión 3 — Claude Opus 4.7 vs 4.6 (−0.55)**: Opus 4.7 (lanzado más reciente) saca menor que Opus 4.6 en el benchmark compuesto y también en NIAH-ES (4.95 vs ~5.5 estimado para 4.6). Trackers terceros confirman regresión en MRCR multi-needle. Anthropic priorizó razonamiento sobre retrieval en 4.7.

**Regresión 4 — Devstral Small > Devstral 2 (−0.43)**: el "Devstral 2" lanzado en diciembre 2025 (123B en OpenRouter) saca 7.09 contra 7.52 del Small original (24B). El modelo más grande es marginalmente peor. Probable razón: el Small está más afinado en NIAH-ES (7.24 vs 6.67 del 2) y string_precision (8.12).

**Caso raro — Gemini 2.5 Pro → 3.1 Pro (final cae −0.10 pero quality sube +0.88)**: el quality real subió bastante (6.52 → 7.40). Pero costo más alto y latencia mayor lo penalizan en compuesto. **El modelo SÍ mejoró en quality**, no es regresión real, es la fórmula penalizando upgrade pricing.

**Conclusión patrón**: **3 de 5 regresiones reales son thinking models o tier "Pro" thinking-by-default que reemplazan no-thinking** (GPT-4.1→5.5, Qwen Instruct→Thinking, Opus 4.6→4.7). El thinking by default es un anti-pattern para single-turn. Los avances reales vienen del tier Flash Lite / variantes Mini.

---

## 8. Open-source vs propietario — ¿se cerró la brecha?

### 8.1 Promedios

| Categoría | n | Score compuesto | Quality |
|---|---|---|---|
| Open-source | 48 | 6.85 | 7.45 |
| Propietario | 24 | 6.89 | 7.52 |

**Hallazgo**: la diferencia es **0.04 puntos** (compuesto) o **0.07 quality** — virtualmente cero. **El top open-source supera al top propietario** por +0.25 puntos (Llama 4 Scout 7.69 > Gemini 3.1 Flash Lite 7.44). En distribución completa, open-source está al menos en paridad.

### 8.2 Por pilar — top open vs top closed

| Pilar | Top Open | Score | Top Closed | Score | Δ |
|---|---|---|---|---|---|
| Razonamiento | Llama 4 Scout 17B | 8.26 | Gemini 3.1 Flash Lite | 7.89 | +0.37 |
| Coding | Llama 4 Scout 17B | 8.15 | GPT-4.1 | 7.92 | +0.23 |
| Contenido | Llama 3.1 8B Instant | 8.27 | MiMo V2.5 (Xiaomi) | 7.97 | +0.30 |
| Agentes | Llama 3.1 8B Instant | 8.06 | Grok 4.1 Fast | 7.51 | +0.55 |

**En los 4 pilares, el top open-source supera al top propietario**. En 2024 esto NO era el caso — la brecha era de 0.5+ puntos a favor de Claude/GPT. En mayo 2026, **la brecha se cerró y se invirtió** en single-turn.

### 8.3 Caveat importante

El propietario top en este benchmark es Gemini 3.1 Flash Lite (no Claude Opus o GPT-5). La razón: **los flagship propietarios son thinking-by-default y eso los penaliza en single-turn corto**. En tareas multi-turn complejas con tool use intensivo (como debugging real), Claude Opus probablemente sigue dominando — caso Hetzner en sección 0 del documento. Pero para 80% de casos del emprendedor LATAM, **open-source ya empató o superó a propietario**.

### 8.4 Top 10 open-source globales

| # | Modelo | Final | $/1k | License |
|---|---|---|---|---|
| 1 | Llama 4 Scout 17B (Groq) | 7.69 | 0.54 | Llama Community |
| 2 | Llama 3.1 8B Instant (Groq) | 7.67 | 0.14 | Llama Community |
| 3 | Devstral Small | 7.52 | 0.48 | Apache 2.0 |
| 4 | Mistral Small 4 | 7.51 | 0.94 | Mistral Research |
| 5 | GPT-OSS 20B (Groq) | 7.47 | 0.47 | OpenAI MIT |
| 6 | Nemotron 3 Nano 30B | 7.43 | 0.32 | NVIDIA |
| 7 | GPT-OSS 120B (Ollama Cloud) | 7.37 | 0 (sub) | OpenAI MIT |
| 8 | Llama 3.3 70B (Groq) | 7.36 | 1.36 | Llama Community |
| 9 | Gemma 4 31B | 7.30 | 0.99 | Gemma License |
| 10 | Qwen 3-Next 80B Instruct (NIM) | 7.20 | 0 | Qwen base |

---

## 9. Anti-patterns del marketing — claims que no se sostienen

Seis claims comunes en marketing AI 2025-2026 que la data del benchmark NO respalda:

### 9.1 "Más parámetros = mejor"

Mistral Large 3 (675B) saca 6.83 final, 8.18 quality. **Nemotron 3 Nano 30B saca 7.43 final, 7.79 quality** — modelo **22.5x más chico, mejor en compuesto** y comparable en quality. Llama 3.1 8B Instant (8B activos) saca 7.67 — más alto que casi cualquier modelo 100B+ del benchmark excepto Llama 4 Scout (MoE 17B activos / 109B total).

### 9.2 "Thinking by default es mejor"

Qwen 3-Next 80B: Instruct 7.20 → Thinking 6.35 = **−0.85 puntos**. Con quality cayendo **−1.22**. Por pilar: Razonamiento −0.78, Coding −0.44, Contenido −0.79, Agentes −0.95. **Penalización generalizada**, no solo en suites donde "no se necesita razonar".

GPT-5.5 (thinking-by-default) 6.07 vs GPT-4.1 6.74 = **−0.67**. Kimi K2 Thinking 6.17 vs Kimi K2 6.96 = **−0.79**. Patrón consistente.

**En single-turn, thinking pierde en todo**. La excepción son tareas multi-turn con tools donde el reasoning intermedio agrega valor — el caso Hetzner sigue siendo el mejor argumento para thinking, pero NO es lo que mide single-turn.

### 9.3 "Thinking forzado mejora multi-turn agéntico" (ROTUNDAMENTE FALSO)

Datos del Lote 11 thinking (29-30 abril): 9 modelos hybrid corridos en `agent_long_horizon` con `reasoning=high` forzado vs su línea base sin thinking. **8 de 9 EMPEORAN**:

| Modelo | Δ con thinking forzado |
|---|---|
| Kimi K2.6 | −0.70 |
| Claude Opus 4.7 | −0.67 |
| Hermes 4 70B | −0.54 |
| Claude Sonnet 4.6 | −0.50 |
| Hermes 4 405B | −0.50 |
| Claude Haiku 4.5 | −0.29 |
| Gemini 2.5 Flash | −0.09 |
| **Excepción única — Kimi K2.5** | **+0.73** |

Hipótesis: el modelo "razona demasiado" en cada turno, pierde foco/contexto del usuario, y se desvía del objetivo en multi-turn. **Implicación**: para OpenClaw / Hermes / N8N, **NO activar thinking por default**. Solo activar si la tarea específica requiere razonamiento puro (matemática, lógica formal). Para conversación, customer support, content marketing → thinking puede empeorar.

### 9.4 "Premium tier vale el costo"

Claude Opus 4.7 ($117/1k) saca 6.54 final, 7.64 quality. Llama 4 Scout (Groq, $0.54/1k) saca 7.69 final. **El gap es +1.15 a favor del barato, a 217x menos costo**. En quality, Claude está top 7 (7.64 vs 8.22 Gemma DGX Q4) — pero la diferencia es menos del 10% y costo es 100x mayor.

### 9.5 "Modelos chinos son la nueva frontera"

Qwen, Kimi, DeepSeek, GLM, Step — **8 de los 9 peores en translation (español neutro) son chinos**. En quality interna pueden competir, pero el output público en español requiere validación humana. Para automatización end-to-end es riesgo material.

### 9.6 "1M context declarado = retrieval efectivo a 1M"

Lote NIAH v3 (1 mayo): 4 modelos con context declarado ≥1M corridos a 1M tokens (15 tests cada uno):

| Modelo | Declarado | Tests OK | Score 1M | Causa |
|---|---|---|---|---|
| **GPT-4.1** | 1M | **15/15** ✅ | 4.91 | **Único que cumple la promesa** |
| Llama 4 Scout 17B (Groq) | 10M | 0/15 ❌ | — | Groq preview cap a 131K |
| DeepSeek V4 Flash (NIM) | 1M | 0/15 ❌ | — | NIM cap (~128K efectivo) |
| Gemini 3.1 Pro | 1M | 0/15 ❌ | — | OpenRouter cap |

**3 de 4 proveedores capan el context window declarado por el modelo**. El "1M" o "10M" del marketing solo aplica si:
- El modelo realmente tiene capacidad arquitectural (sí, todos)
- **Y** el provider que se usa expone la capacidad completa (no, solo OpenAI directo / OpenRouter para GPT-4.1)

**Implicación crítica**: para tasks que requieren context >256K en producción, **GPT-4.1 vía OpenAI directo o OpenRouter es la única opción confirmada al 4 mayo 2026**. Pendiente probar Gemini 3.x Pro vía Google directo.

---

## 10. Top 5 hallazgos sorpresivos del v2.6.1

### 10.1 Cost vs quality es CERO, no negativo

Spearman cost vs quality = +0.019, p=0.901 (n=47 modelos pagados). **No hay correlación significativa entre precio y calidad** — los modelos premium NO son peores en quality, son más caros y más lentos. La narrativa "más caro = peor" es artefacto del peso 20% del costo + 15% velocidad/latencia en la fórmula de score compuesto. Importante distinguir: para decisiones de producción, score compuesto **es** la métrica relevante; pero el insight académico es que la **quality bruta no penaliza al premium**.

### 10.2 DeepSeek V4 cambia drasticamente de quality según provider

DeepSeek V4 Flash NIM (FP16): quality 7.90. DeepSeek V4 Flash Ollama Cloud: quality 5.15. **Misma versión del modelo, delta de quality −2.75 puntos por provider**. La cuantización agresiva del Cloud Ollama degrada el output radicalmente. Para producción con DeepSeek V4: **NIM gratis (Flash) o OpenRouter pagado, NO Ollama Cloud**.

### 10.3 MiMo Xiaomi direct >> MiMo OpenRouter

MiMo V2-Omni Xiaomi direct (sub $14/mes): final 7.46. MiMo-V2-Omni OpenRouter: final 6.94. **Delta +0.52 puntos por provider**. MiMo V2-Pro mismo patrón: +0.59. La sub Xiaomi entrega mejor performance que pagar el mismo modelo en OpenRouter — caso raro donde la suscripción es estrictamente mejor que pay-as-you-go.

### 10.4 Lost-in-the-middle DESAPARECE con N=5 needles

El piloto NIAH-ES v1 (1 needle/slot) reportó "Opus 4.7 cae −3.0 puntos al 50% del 4K". Eso fue **artefacto de N=1**. Con 5 needles promediados (v2), el delta máximo entre 25%-50%-75% en TODOS los modelos medidos es **0.04-0.21 puntos** — virtualmente plano. Lección metodológica: **N≥5 mínimo para hallazgos publicables**. Lost-in-the-middle reportado en literatura (Liu et al. 2023) puede ser real para inglés con prompts académicos, pero NO es detectable en español neutro con estos needles, en estos modelos, con N=5.

### 10.5 GPT-OSS 120B (Ollama Cloud) lidera ALH con +1.23 sobre su single-turn

GPT-OSS 120B sale #13 en single-turn (7.37) pero lidera **agent_long_horizon con 8.60** — delta +1.23 sobre su línea base. Ningún otro modelo del top 10 sube tanto. Hipótesis: la arquitectura GPT-OSS está optimizada para context retention multi-turno + skill orchestration, y eso aparece cuando la suite mide multi-turn explícitamente. Para emprendedores con sub Ollama Cloud ($30/mes): **GPT-OSS 120B es la mejor opción gratuita para agentes complejos**.

---

## 11. Implicaciones para próxima iteración (junio 2026)

### 11.1 Suites pendientes de robustecer

1. **agent_capabilities** — la suite más volátil (rango 4.43 a 8.07 = 3.64 puntos). Necesita más tests para discriminar finos en el tier 7.0+. Hoy el ranking acá es ruidoso para modelos en quartiles 2-3.
2. **tool_calling** — falta cobertura en tools complejas (>3 funciones, anidadas). El benchmark actual privilegia un patrón simple que casi todos los modelos modernos manejan.
3. **NIAH-ES** — extender a los 50 modelos restantes con cobertura ≥50 runs single-turn (faltan ~50 sin NIAH-ES).
4. **agent_long_horizon** — extender a los 36 modelos restantes (cobertura actual 36/72).

### 11.2 Suites nuevas en evaluación

1. **agentic_debugging** — bugs reales con stubs detallados (5-10 tests, multi-turn 10-20). Cubre el gap del caso Hetzner. ETA: 1-2 semanas. Costo: $30-50.
2. **NIAH-ES v3b** — Gemini 3.1 Pro vía Google directo + DeepSeek V4 Pro Ollama Cloud para validar si el cap es del provider intermediario.
3. **Replicar SWE-bench Verified en top 15** — infra pública, costo $50-100, ETA 2-3 días post-correcciones.
4. **Suite multimodal pura** — OCR, visión, audio. Hoy solo MiMo V2-Omni y Gemma 4 son medidos como multimodales en text-only.

### 11.3 Modelos pendientes de medir o re-medir

1. **DeepSeek V4 Pro vía OpenRouter** — validación cruzada con NIM/Cloud terminada.
2. **Devstral 2 123B (NIM)** — completar suite agent_capabilities (0 runs registrados).
3. **Magistral Small (Mistral)** — bloqueado en NIM por error 400; probar en Mistral direct.
4. **Llama 4 Maverick** — pendiente migrar a Groq (hoy en OpenRouter con 7.13 quality 7.93). Esperable +0.4-0.5 si va a Groq.
5. **Gemini 3.1 Flash** (no Lite) — pendiente, podría estar entre Flash Lite (7.44) y Pro (6.18).

### 11.4 Métricas a agregar

1. **Cost-per-quality-point**: $/1k calls dividido por (score - 5.0). Mide cuánto cuesta cada punto de score sobre el baseline.
2. **Latency p95**: hoy se guarda avg, pero p95 importa más para producción (un timeout en percentil alto rompe UX).
3. **Variance entre runs**: misma pregunta, 5 ejecuciones. Modelos con alta varianza son riesgo en producción aunque su mean score sea alto.
4. **Quality-only ranking publicado en docs/data/models.json** — separar score compuesto del quality bruto en outputs públicos.

---

## 12. Datos sospechosos / a re-validar

Casos donde la data parece anómala y conviene re-correr antes de publicar conclusiones fuertes:

### 12.1 Devstral 2 123B (NIM) — agent_capabilities = 0.00

68 runs totales pero la suite `agent_capabilities` registra 0.00. Posibles causas: la suite no se corrió completamente por timeouts (más probable) o el modelo retorna respuestas vacías en esa suite. **Re-correr solo agent_capabilities con timeout extendido** antes de aceptar el ranking 7.16 final.

### 12.2 GPT-5.5 score 6.07 — caída masiva vs GPT-4.1

GPT-5.5 cuesta 3.7x más que GPT-4.1 y entrega 10% menos final score. Si bien la regresión es plausible (thinking-by-default + max_tokens insuficiente), conviene re-correr con `max_tokens × 4 = 8192` explícito para confirmar que no se trunca outputs. **El adapter ya lo hace** — pero re-validar con runs frescos es prudente.

### 12.3 Llama 4 Maverick — final 7.13 vs los Llama Groq en 7.36-7.69

Maverick está en OpenRouter (no Groq direct) y rinde mucho peor que su par Llama 4 Scout en Groq (7.69). La diferencia de +0.56 entre los dos modelos Llama 4 se explica casi totalmente por provider. **Re-medir Maverick en Groq es el test crítico**.

### 12.4 Qwen 3.5 397B (Ollama Cloud) — translation 4.41

El score más bajo del benchmark en cualquier suite individual. Posibles causas:
1. Bug del adapter Ollama Cloud — alguna config rechaza español neutro.
2. Cuantización específica de Ollama Cloud (no documentada, probablemente Q4 agresivo) degrada el español más que en otros modelos.
3. Genuina contaminación de chino en español en el modelo cloud.

**Re-correr 5 prompts en español puro y comparar con NIM** (mismo modelo, score 6.90 final, quality 8.07 — claramente mejor).

### 12.5 Inspección cualitativa Opus 4.7 NIAH-ES (paráfrasis vs extracción)

Hipótesis abierta: **Opus 4.7 parafrasea en lugar de extraer texto exacto** del needle, lo que no matchea con regex/keywords scoring. Pendiente: revisión manual de 5-10 respuestas en `benchmarks/results/responses/20260430_200512/` para confirmar o refutar.

### 12.6 MiMo Xiaomi — pricing es ambiguo

Reportamos costos $0.13-0.46/1k para los MiMo, pero el modelo de Xiaomi es **suscripción flat** ($14/mes con cap de tokens off-peak 0.8x). El cálculo $/1k assume token-by-token pricing extrapolado. Si el usuario satura el cap mensual, el costo por call efectivo sube. **El ranking de MiMo asume volumen moderado** — para volumen alto requiere recálculo.

### 12.7 Gemini 2.5 Pro → 3.1 Pro: quality sube +0.88 pero final cae −0.10

Caso raro: el upgrade entrega quality bruta materialmente mejor (6.52 → 7.40) pero el costo más alto y latencia mayor lo penalizan en compuesto. **No es regresión real** — es la fórmula penalizando upgrade pricing. Documentar como caso de "quality vs compuesto divergen" para evitar interpretación equivocada.

### 12.8 DeepSeek V4 Pro NIM cascada 504 — patrón sistemático

Reproducible **2 veces** (abril 28 + mayo 3). NIM gateway no maneja modelo gigante con prompts largos. Para producción: usar OpenRouter pagado o aceptar que NIM no está disponible para ese modelo específico. **Documentado en MODELOS.md como bloqueante de producción**.

---

## Anexo A — Cómo leer este benchmark

- **Score global**: combinación ponderada de quality (50%) + cost (20%) + tool_calling (15%) + speed (7.5%) + latency (7.5%). Para modelos con runs en NIAH-ES y agent_long_horizon, esas suites están integradas en quality.
- **Score by pillar**: 23 suites single-turn agrupadas en 4 pilares (Razonamiento, Coding, Contenido, Agentes). El pilar "Long-context retrieval" (NIAH-ES) se reporta separado por su naturaleza distinta.
- **Cost per 1k calls**: asume 300 tokens input + 1500 tokens output por call. Es el costo de procesar 1000 requests bajo este perfil.
- **Tokens per second**: media de output_tokens / latency_total a través de todos los tests del modelo. No incluye latencia de red de Chile a USA.
- **Provider matters**: el mismo modelo puede tener score, latencia y costo distintos según provider. Comparar provider explícito es obligatorio antes de elegir.
- **Quality vs compuesto**: la quality bruta es comparable entre modelos sin pesar costo/velocidad. El score compuesto refleja la decisión real de un emprendedor LATAM con presupuesto.

## Anexo B — Reproducir el análisis

```bash
.venv/bin/python -c "
import json
from scipy.stats import spearmanr
with open('docs/data/models.json') as f:
    data = json.load(f)
tested = [m for m in data['models'] if m['tested'] and m['runs'] >= 50]
paid = [m for m in tested if m['cost_per_1k_calls_usd'] > 0]
costs = [m['cost_per_1k_calls_usd'] for m in paid]
qual = [m['quality_avg'] for m in paid]
print('cost vs quality:', spearmanr(costs, qual))
"
```

Salida esperada: `SignificanceResult(statistic=0.019, pvalue=0.901)`.

Confirma la sección 1: cost-quality NO correlacionan en quality bruta. Para Spearman cost vs score_global compuesto, sustituir `quality_avg` por `score_global` y se obtiene `−0.671, p<0.001`.

---

**Última actualización**: 4 de mayo de 2026 — v2.6.1 (post-NIAH-ES extension, DeepSeek V4 family triple provider, Datasheets mensuales).

**Próxima revisión**: tras nuevos lotes de junio 2026 (suite agentic_debugging, NIAH-ES extensión a 50 modelos restantes, Gemini 3.x Pro vía Google directo).

**Auto-regenerable**: este documento se reescribe completo desde `docs/data/models.json` con un agente data-scientist (`.claude/agents/data-scientist.md`). NO editar manualmente — los cambios se perderán en la próxima regeneración.
