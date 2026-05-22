---
title: "Insights del benchmark — qué dice la data, no el marketing"
fecha: "2026-05-22"
version_benchmark: "v2.7"
modelos_analizados: 72
modelos_catalogados: 113
runs_minimas_por_modelo: 50
tests_por_modelo: "91 single-turn + 12 agent_long_horizon + 45 niah_es_lite"
pilares: ["Razonamiento", "Coding", "Contenido/Marketing", "Agentes/Operaciones", "Long-context retrieval"]
juez_llm: "Phi-4 (Microsoft, 14B, MIT) via Ollama local"
audiencia: "Emprendedores latinoamericanos que toman decisiones de producción HOY"
fuente_datos: "docs/data/models.json + benchmarks/results/*.json"
pesos_score: {quality: 0.50, cost: 0.20, tool_calling: 0.15, speed: 0.075, latency: 0.075}
total_runs: "9,390 single-turn (+ NIAH-ES y multi-turn integrados en quality)"
---

# Insights del benchmark — qué dice la data, no el marketing

> **Disclaimer epistemológico**: este documento es **complemento, NO sustituto** de los benchmarks académicos validados (HumanEval, MMLU, GSM8K, SWE-bench Verified, NIAH inglés, MT-Bench, LMSYS Arena). Está pensado para emprendedores hispanohablantes que deciden qué modelo poner en producción HOY para casos aplicados en español neutro (N8N, OpenClaw, Hermes, blogs LATAM, soporte cliente, agentes). Para investigación académica o capacidades fundamentales, prioriza los oficiales. Cross-references documentadas en [BENCHMARKS_EXTERNOS.md](BENCHMARKS_EXTERNOS.md) y [NIAH_CROSSREF.md](NIAH_CROSSREF.md).

Este es el análisis cuantitativo del benchmark `ai-benchmarks-alternativos` al **22 de mayo de 2026** (v2.7). 72 modelos con cobertura ≥50 runs, 91 tests single-turn + 12 multi-turno + 45 retrieval long-context, juez Phi-4 local. La pregunta que respondemos no es "cuál es el mejor modelo", sino: **qué patrones aparecen en la data cuando se comparan precio, velocidad, capacidades, retrieval y proveedor a la vez, en español neutro LATAM**.

> 🔄 **Rescore de costo provider-aware (v2.7, 22 may 2026)**: hasta v2.6.x la mayoría de runs tenía el costo calculado con un fallback `(1.0, 3.0)` → `cost_score≈7.0` para casi todos los modelos → **el costo (20% del peso) era casi inerte** y el ranking era de facto solo-calidad. En v2.7 se recalculó `cost_usd`/`cost_score`/`final` de **7.483 runs** con el precio real por proveedor (`benchmarks/models.py`) × tokens reales. **Sólo cambiaron esos 3 campos**; `quality_avg`, `tool_calling`, `speed` y `latency` NO cambiaron. Efecto: el costo ahora **discrimina de verdad** y reordena el ranking. Lo gratis/barato (NIM, Groq, open-source local) sube; lo premium-caro baja (Gemini 2.5 Pro, GPT-5.4 y Sonnet 4.6 caen ~0.25–0.49 puntos; **Opus 4.7 baja a #66/72**). Todas las tablas de este documento ya reflejan el estado **post-v2.7** calculado desde `docs/data/models.json`. Ver [CHANGELOG v2.7.0](CHANGELOG.md) y [README](README.md) para el ranking vigente.

---

## 🚨 Limitación crítica: NO medimos debugging agentic real

**Caso real validado** (30 abril 2026): un emprendedor enfrentó un **problema técnico complejo en un contenedor OpenClaw corriendo en VPS Hetzner**. Probó resolverlo con MiniMax M2.7 usando un agente con herramientas — **no pudo solucionarlo**. Cambió a Claude Opus 4.7 (posición **#66/72** en nuestro ranking compuesto tras el rescore v2.7, hundido por su costo) — **resolvió el problema en pocos minutos**.

Este caso es **el mejor argumento contra leer el ranking compuesto literalmente**: Opus 4.7 está casi al fondo de nuestra tabla porque cuesta $39/1k calls y es lento, pero es el mejor del mundo para debugging agentic real (SWE-bench Verified #1). El ranking compuesto mide costo-eficiencia para volumen del emprendedor LATAM — NO mide capacidad de incident response crítico.

Este caso expone una limitación seria del benchmark que conviene reconocer.

### Lo que NO medimos

| Dimensión | Lo mide | Nosotros lo medimos |
|---|---|---|
| Debugging agentic con sandbox real (Docker, FS, exec) | **SWE-bench Verified** | ❌ NO |
| Multi-turn 20+ con tool feedback real del sistema | **Claw-Eval** (300 tareas verificadas) | ⚠️ Parcial — `agent_long_horizon` simula tools con stubs |
| Resolución de problemas en infra real (K8s, VPS, networking) | **Terminal-Bench 2.0**, OSWorld | ❌ NO |
| Persistencia / judgment en sesiones largas con hipótesis fallidas | (Sin benchmark estándar) | ❌ NO |

### Para debugging agentic real, prioriza estos benchmarks externos

| Modelo | Nuestro Coding (pilar) | SWE-bench Verified (oficial) |
|---|---|---|
| **Claude Opus 4.7** | 6.79 | **87.6%** ⭐ #1 globalmente |
| Claude Sonnet 4.6 | 6.99 | 77.2% |
| Devstral Small | 8.40 | N/A reportado (specialist) |
| Llama 3.3 70B (Groq) | 7.88 | ~50% (Llama family base) |
| MiniMax M2.7 | 7.33 | N/A reportado |

**SWE-bench Verified** (Anthropic, 500 tareas debugging reales con repos + tests verificados humanamente) es la referencia para esta dimensión. **Opus 4.7 es #1 globalmente con 87.6%** — eso predice mejor su comportamiento en VPS Hetzner que cualquier número de este benchmark. Nótese el contraste: en nuestro pilar Coding (generación single-turn, en español) Opus saca 6.79 — por debajo de Devstral Small (8.40); pero en debugging agentic real con tests, Opus es el #1 del mundo. Son dimensiones distintas.

### Conclusión honesta

1. Si la tarea es **generar código nuevo aplicado** (workflows N8N, plugins WP, scripts Python, blog posts en español): este ranking es útil. Devstral Small, Llama 3.3 70B Groq, Mistral Small 4 ganan por calidad+velocidad+costo.
2. Si la tarea es **debugging real con tools en producción**: este ranking NO es predictivo. Mirar SWE-bench Verified, Claw-Eval, Terminal-Bench. Para casos críticos (incident response, hot-fixes), Opus 4.7 / GPT-5.x premium siguen valiendo lo que cuestan.
3. **No existe ranking universal**. Esa es la regla #0: no existe el mejor modelo universal — existen modelos buenos para una tarea, en un volumen, con una restricción.

---

## ⚠️ Limitaciones críticas a leer ANTES del análisis

Tres limitaciones estructurales que cambian la interpretación de varios hallazgos:

1. **Single-turn ≠ producción real con tools.** Cada test del subset 91 es un prompt único, sin acceso a herramientas externas. En producción, un modelo "más débil" combinado con búsqueda web (Perplexity, Tavily) o RAG puede superar a un modelo "más fuerte" sin tools. Si el pipeline usa N8N con tool de búsqueda, el ranking acá no se traduce 1-a-1.

2. **Cobertura desigual entre modelos.** El piso es 50 runs, pero algunos llegan a 223 (Devstral Small, alta confianza) y otros a 50-68 (con DNS errors, timeouts del proveedor o suite agent_capabilities incompleta). Devstral 2 123B (NIM) tiene 68 runs con `agent_capabilities=0.00` — su score 7.68 (post-v2.7, beneficiado por ser gratis en NIM) es **provisorio**. Cualquier afirmación sobre modelos sub-91 runs hay que tomarla con asterisco.

3. **El provider importa tanto como el modelo — y con el rescore v2.7 pesa más.** El mismo modelo en Groq vs OpenRouter vs NIM vs Ollama Cloud puede tener delta de hasta **+0.59 puntos** (sección 3). Tras el rescore provider-aware esta brecha se amplía: el provider gratis (NIM) o la sub fija (Xiaomi $14) ahora ganan ventaja de costo material sobre el mismo modelo en OpenRouter pay-as-you-go. El ranking global esconde estas diferencias.

Estos hallazgos cuantitativos filtran el 80% de modelos malos. El 20% final lo decide cada equipo con 5-10 prompts típicos de su caso de uso, en el mismo provider y configuración (con/sin tools) que va a usar en producción.

---

## Tabla de contenidos

0. [Hallazgos destacados v2.7](#0-hallazgos-destacados-v27)
1. [Correlación precio ↔ calidad por pilar](#1-correlación-precio--calidad-por-pilar)
2. [Outliers — joyas, malas compras y especialistas](#2-outliers--joyas-malas-compras-y-especialistas)
3. [Provider matters — el mismo modelo en distintos providers](#3-provider-matters--el-mismo-modelo-en-distintos-providers)
4. [Patrones de fragilidad — tool calling y JSON estructurado por tamaño](#4-patrones-de-fragilidad--tool-calling-y-json-estructurado-por-tamaño)
5. [Sensibilidad por idioma — español vs inglés](#5-sensibilidad-por-idioma--español-vs-inglés)
6. [Costo real para emprendedor N8N — ranking mensual y Pareto](#6-costo-real-para-emprendedor-n8n--ranking-mensual-y-pareto)
7. [Regresiones — cuando la versión nueva es peor](#7-regresiones--cuando-la-versión-nueva-es-peor)
8. [Open-source vs propietario — ¿se cerró la brecha?](#8-open-source-vs-propietario--se-cerró-la-brecha)
9. [Anti-patterns del marketing — claims que no se sostienen](#9-anti-patterns-del-marketing--claims-que-no-se-sostienen)
10. [Top 5 hallazgos sorpresivos del v2.7](#10-top-5-hallazgos-sorpresivos-del-v27)
11. [Implicaciones para próxima iteración (junio 2026)](#11-implicaciones-para-próxima-iteración-junio-2026)
12. [Datos sospechosos / a re-validar](#12-datos-sospechosos--a-re-validar)
13. [Análisis de varianza intra-model (validado 2026-05-13)](#13-análisis-de-varianza-intra-model-validado-2026-05-13)

---

## 0. Hallazgos destacados v2.7

### 0.1 Top 15 score compuesto (post-rescore provider-aware)

| # | Modelo | Final | Quality | $/1k | tok/s | Provider | Open |
|---|---|---|---|---|---|---|---|
| 1 | Devstral Small | **7.84** | 7.89 | 0.48 | 139 | OpenRouter | sí |
| 2 | Nemotron 3 Nano Omni 30B-A3B | **7.84** | 7.75 | 0.00 | 203 | NVIDIA NIM | sí |
| 3 | Qwen 3-Next 80B Instruct | **7.83** | 8.11 | 0.00 | 52 | NVIDIA NIM | sí |
| 4 | Gemini 2.5 Flash Lite | **7.74** | 7.79 | 0.63 | 171 | OpenRouter | no |
| 5 | Llama 4 Scout 17B | **7.69** | 7.70 | 0.54 | 170 | Groq direct | sí |
| 6 | Devstral 2 123B | **7.68** | 7.98 | 0.00 | 42 | NVIDIA NIM | sí |
| 7 | Llama 3.1 8B Instant | **7.67** | 7.33 | 0.14 | 262 | Groq direct | sí |
| 8 | Nemotron 3 Base 33B (DGX Q4) | **7.63** | 7.83 | 0.00 | 63 | DGX local | sí |
| 9 | Nemotron Nano 9B v2 | **7.59** | 7.73 | 0.00 | 54 | NVIDIA NIM | no |
| 10 | Gemma 4 26B MoE | **7.52** | 7.80 | 0.49 | 44 | OpenRouter | sí |
| 11 | Qwen 3.5 397B | **7.51** | 8.07 | 0.00 | 21 | NVIDIA NIM | sí |
| 12 | Mistral Small 4 | **7.51** | 7.88 | 0.94 | 82 | OpenRouter | sí |
| 13 | Gemma 4 31B | **7.50** | 8.19 | 0.99 | 22 | OpenRouter | sí |
| 14 | Gemma 4 31B (NIM) | **7.50** | 8.19 | 0.00 | 22 | NVIDIA NIM | sí |
| 15 | GPT-OSS 20B | **7.47** | 7.10 | 0.47 | 474 | Groq direct | sí |

**Lectura inmediata (cambió con el rescore v2.7)**:
- 13 de 15 son open-source. La brecha contra propietario se invirtió definitivamente en compuesto.
- **8 de los 15 son GRATIS ($0/call)** — todos vía NVIDIA NIM o local DGX. El tier gratis ya no es "alternativa de pobre": copa la mitad del top 15.
- **Devstral Small ($0.48) y Nemotron 3 Nano Omni (NIM, $0) empatan en #1 con 7.84** — uno barato-pagado, otro gratis. Qwen 3-Next 80B Instruct (NIM, $0, quality 8.11) los pisa los talones con 7.83.
- Gemini 2.5 Flash Lite (#4, 7.74) es **el único propietario en el top 5** y subió por ser barato ($0.63) y rapidísimo (171 tok/s).
- **Ningún modelo premium (>$5/1k) entra al top 15** — y ahora ninguno entra siquiera al top 25.

> ⚠️ **Caveat del tier gratis NIM (40 RPM)**: los 8 modelos gratis del top 15 corren en NVIDIA NIM con un **rate-limit de 40 requests/minuto**. Es excelente costo/beneficio para **volumen bajo-medio** (un blog, un agente N8N de 30-40 ejecuciones/día, prototipos, este mismo benchmark). Para **alto throughput sostenido en producción** (cientos de calls concurrentes), el cap se vuelve bloqueante y hay que pagar OpenRouter o usar Groq. No leer "el #1 es gratis" como "gratis para cualquier escala".

### 0.2 Top 12 quality_avg only (sin pesar costo/velocidad — NO cambió con el rescore)

El rescore tocó solo costo/final, **no quality**. Esta tabla es idéntica a la de v2.6.x — es el ranking que mediría un benchmark puramente académico:

| # | Modelo | Quality | Final | Comentario |
|---|---|---|---|---|
| 1 | Gemma 4 31B (DGX Spark Q4) | **8.22** | 7.42 | Cuantización local |
| 2 | Gemma 4 31B (NIM/OpenRouter FP16) | 8.19 | 7.50 | Quality top, costo cero en NIM → final alto |
| 3 | Mistral Large 3 675B (NIM) | 8.18 | 7.38 | Quality alto, lento — pero gratis en NIM lo salva |
| 4 | Qwen 3-Next 80B Instruct (NIM) | 8.11 | 7.83 | NIM gratis con quality top-tier → #3 compuesto |
| 5 | Qwen 3.5 397B (NIM) | 8.07 | 7.51 | |
| 6 | Hermes 4 405B | 8.05 | 7.17 | |
| 7 | **Claude Opus 4.6** | **8.04** | 6.57 | Quality top 7, costo $39/1k lo hunde a #58 |
| 8 | Ministral 14B (NIM) | 8.02 | 7.44 | Modelo chico con quality alta, gratis |
| 9 | Devstral 2 123B (NIM) | 7.98 | 7.68 | |
| 10 | GLM 5 (NIM) | 7.97 | 7.28 | |
| 11 | Devstral 2 (Dic 2025) | 7.80 | 7.09 | |
| 12 | Gemma 4 26B MoE | 7.80 | 7.52 | |

**Hallazgo crítico (más nítido tras el rescore)**: en quality pura, **Claude Opus 4.6 es top 7** (8.04). En el ranking compuesto cae a **#58/72** por costo $39/1k + speed bajo. Opus 4.7 cae aún más, a **#66/72** (quality 7.64). **Esto valida la metodología**: si se midiera solo quality, los benchmarks académicos ya cubren esa pregunta. El aporte propio es medir **quality + costo + velocidad + tool calling juntos**, en español neutro, simulando un emprendedor LATAM. La novedad de v2.7 es que **la quality alta gratis ahora gana**: Qwen 3-Next, Mistral Large 3, Gemma 4 (quality 8.0+) suben al top compuesto porque el rescore confirmó que en NIM cuestan $0.

### 0.3 Top NIAH-ES (long-context retrieval español — suite, NO cambió con el rescore)

| # | Modelo | Score NIAH-ES | Comentario |
|---|---|---|---|
| 1 | **Devstral Small** | **7.24** ⭐ | Lidera retrieval español |
| 2 | DeepSeek V4 Flash (NIM) | 7.06 | Quality retrieval alta en FP16 NIM |
| 3 | Mistral Small 4 | 7.01 | Multilingüe europeo fuerte |
| 4 | Llama 4 Scout 17B (Groq) | 6.91 | |
| 5 | Devstral 2 (Dic 2025) | 6.75 | |
| 6 | Llama 3.3 70B (Groq) | 6.27 | |
| 7 | Gemini 3.1 Pro | 5.95 | |
| 8 | GPT-4.1 | 5.84 | Único que cumple context 1M real (sección 9.6) |
| ... | | | |
| bottom | **Claude Opus 4.7** | **5.10** | No es debilidad de retrieval — es refusal pattern (sección 12.5) |

**Devstral Small supera a Opus 4.7 en NIAH-ES por +2.14 puntos a ~1/80 del costo** ($0.48 vs $39/1k). El score es de quality y NO cambió con el rescore — pero el contraste de costo-eficiencia ahora es aún más fuerte porque Opus 4.7 cayó a #66 en el compuesto.

### 0.4 Top 10 agent_long_horizon (multi-turn 8+ turnos — suite, NO cambió con el rescore)

| # | Modelo | Score ALH | Final (compuesto v2.7) | Δ |
|---|---|---|---|---|
| 1 | **GPT-OSS 120B (Ollama Cloud)** | **8.60** | 7.37 | **+1.23** ⬆ |
| 2 | DeepSeek V4 Pro (Ollama Cloud) | 8.42 | 6.01 | +2.41 ⬆⬆ |
| 3 | Llama 4 Scout 17B (Groq) | 8.26 | 7.69 | +0.57 |
| 4 | Qwen 3-Next 80B Instruct (NIM) | 8.24 | 7.83 | +0.41 |
| 5 | Llama 3.1 8B Instant (Groq) | 8.21 | 7.67 | +0.54 |
| 6 | MiMo V2-Omni (Xiaomi direct) | 8.17 | 7.46 | +0.71 |
| 7 | Devstral Small | 8.12 | 7.84 | +0.28 |
| 8 | Kimi K2 Thinking (NIM) | 8.10 | 6.96 | +1.14 |
| 9 | MiMo V2.5 (Xiaomi sub) | 8.01 | 7.45 | +0.56 |
| 10 | GPT-OSS 20B (Groq) | 7.98 | 7.47 | +0.51 |

**Hallazgo robusto**: los modelos top single-turn **suben** en ALH (suite multi-turno). Esto es coherente con que los modelos bien afinados en context retention + skill orchestration mantienen calidad cuando el horizonte se extiende. Caso curioso: DeepSeek V4 Pro (Ollama Cloud) sale #70/72 en compuesto pero #2 en ALH — su penalización de costo/quality en single-turn no aplica al multi-turno. Por contraste, los thinking-by-default puros siguen bajando en ALH — patrón documentado en sección 9.3.

---

## 1. Correlación precio ↔ calidad por pilar

Spearman rank correlation entre `cost_per_1k_calls_usd` y métricas de score (modelos pagados, n=47). **Recalculado post-rescore v2.7** — la correlación cost↔compuesto se hizo más fuerte porque el costo ahora discrimina de verdad:

| Métrica | ρ Spearman | p-value | Lectura | Δ vs pre-v2.7 |
|---|---|---|---|---|
| Cost vs **score_global compuesto** | **−0.748** | <0.001 | Negativa fuerte (ahora más, el costo dejó de ser inerte) | −0.671 → −0.748 |
| Cost vs **quality_avg** | **+0.051** | 0.731 | **No significativa** — pagar más NO predice mejor calidad | +0.019 → +0.051 (igual: ~cero) |
| Cost vs Razonamiento | −0.542 | <0.001 | Negativa fuerte | −0.394 → −0.542 |
| Cost vs Coding | −0.483 | <0.001 | Negativa moderada-fuerte | −0.352 → −0.483 |
| Cost vs **Contenido** | **−0.763** | <0.001 | **Negativa fuerte** — más caro = peor C/B en contenido | −0.641 → −0.763 |
| Cost vs Agentes | −0.594 | <0.001 | Negativa fuerte | −0.402 → −0.594 |

**Hallazgo metodológico clave (nuevo en v2.7 — el efecto del rescore)**:

Antes del rescore, el costo estaba calculado con un fallback `(1.0, 3.0)` para casi todos los runs → `cost_score≈7.0` plano → el peso 20% del costo era **casi inerte** y la correlación cost↔compuesto (−0.671) venía sobre todo de los pocos modelos premium realmente caros. Tras el rescore provider-aware, **el costo discrimina sobre los 72 modelos** y la correlación se profundizó a **−0.748**, y TODAS las correlaciones por pilar se fortalecieron (Razonamiento −0.39→−0.54, Agentes −0.40→−0.59, etc.). Es la señal más limpia de que el rescore funcionó: el costo dejó de ser ruido y pasó a ser un eje discriminante real.

Sin embargo, la relación cost↔**quality pura** sigue virtualmente en cero (+0.05, p=0.73). Esto confirma: **los modelos premium no son peores en calidad — son simplemente más caros y lentos, y la fórmula (correctamente, ahora) los penaliza por eso**. La narrativa "más caro = peor" es un artefacto del peso costo+velocidad, no de la quality bruta. Para un emprendedor LATAM con presupuesto fijo, el score compuesto **es** la métrica relevante; pero conviene saber qué mide cada cosa.

**Velocidad vs quality**: ρ = **−0.319** (p=0.006, sin cambio — speed no se rescoreó). **Más rápido NO predice mejor calidad** — incluso correlaciona ligeramente negativo, porque varios modelos de quality alta (Mistral Large 3 675B, Hermes 4 405B, Gemma 4 31B FP16) son inherentemente lentos.

**Inversión free vs paid (el cambio más visible del rescore)**: antes del rescore el tier gratis quedaba debajo del pagado en compuesto (6.58 vs 7.01) porque el fallback de costo no premiaba ser gratis. Tras el rescore:

| Tier | n | Quality avg | Final compuesto avg |
|---|---|---|---|
| **Gratis ($0/call)** | 25 | 7.33 | **7.19** |
| Pagado (>$0) | 47 | 7.55 | 7.06 |

El tier gratis ahora **supera en compuesto al pagado** (+0.13) pese a tener quality marginalmente menor (−0.22). El costo cero compensa de sobra. Es el resultado más fuerte del rescore: para volumen bajo-medio, lo gratis es estructuralmente competitivo. (Recordar el caveat 40 RPM de NIM para alto throughput — sección 0.1.)

---

## 2. Outliers — joyas, malas compras y especialistas

### 2.1 Malas compras (caro + score bajo)

Modelos con costo ≥$5/1k Y score_global <7.20 (post-rescore v2.7):

| Modelo | $/1k | Final | #/72 | Quality | Comentario |
|---|---|---|---|---|---|
| GPT-5.5 | 46.50 | 6.10 | #69 | 7.29 | Más caro del benchmark, quality menor que GPT-4.1 |
| Claude Opus 4.6 | 39.00 | 6.57 | #58 | 8.04 | Quality #7, precio lo hunde |
| Claude Opus 4.7 | 39.00 | 6.20 | #66 | 7.64 | Quality alta pero costo masivo + más lento que 4.6 |
| GPT-5.4 | 24.00 | 6.44 | #63 | 7.09 | Pierde con GPT-5.4 Mini (7.39) |
| Claude Sonnet 4.6 | 23.40 | 6.34 | #65 | 7.38 | Último Sonnet — perdió contra Llama 3.1 8B |
| Gemini 3.1 Pro | 18.60 | 6.18 | #67 | 7.40 | Peor que Flash Lite (7.44) a 8x del costo |
| Gemini 2.5 Pro | 15.38 | 5.98 | #71 | 6.52 | Anteúltimo del benchmark |
| GPT-4.1 | 12.60 | 6.60 | #57 | 7.62 | Quality top 13, costo lo penaliza |
| Mistral Large | 9.60 | 6.90 | #52 | 7.81 | Mistral Small 4 saca 7.51 a 1/10 del costo |
| GLM-5.1 | 5.01 | 6.97 | #51 | 7.88 | GLM 5 NIM ($0) saca 7.28 — mismo modelo gratis gana |
| Kimi K2.6 | 5.45 | 6.44 | #62 | 7.68 | Versión razonadora — pierde con Kimi K2 (7.28) |

**Patrón crítico**: TODOS los modelos premium (>$5/1k) con variante "Mini", "Flash" o "Small" pierden contra esa variante en el score compuesto. Tras el rescore el patrón es brutal: **los 8 modelos más caros del benchmark ocupan 8 de las 16 últimas posiciones**. El single-turn no recompensa el razonamiento extra que justifica el precio premium, y ahora el costo lo penaliza correctamente.

### 2.2 Joyas (barato + score alto)

Modelos con score_global ≥7.20 y costo entre $0.01-$1.50/1k (post-rescore):

| Modelo | $/1k | Final | tok/s |
|---|---|---|---|
| Devstral Small | 0.48 | 7.84 | 139 |
| Gemini 2.5 Flash Lite | 0.63 | 7.74 | 171 |
| Llama 4 Scout 17B (Groq) | 0.54 | 7.69 | 170 |
| Llama 3.1 8B Instant (Groq) | 0.14 | 7.67 | 262 |
| Gemma 4 26B MoE | 0.49 | 7.52 | 44 |
| Mistral Small 4 | 0.94 | 7.51 | 82 |
| Gemma 4 31B | 0.99 | 7.50 | 22 |
| GPT-OSS 20B (Groq) | 0.47 | 7.47 | 474 |
| MiMo V2-Omni (Xiaomi direct) | 0.13 | 7.46 | 102 |
| Hermes 4 70B | 0.64 | 7.45 | 50 |
| MiMo V2.5 (Xiaomi sub) | 0.13 | 7.45 | 71 |
| Nemotron 3 Nano 30B | 0.32 | 7.43 | 86 |
| MiMo V2.5-Pro (Xiaomi sub) | 0.25 | 7.42 | 49 |
| MiMo-V2-Flash | 0.46 | 7.41 | 54 |
| MiMo V2-Pro (Xiaomi direct) | 0.13 | 7.39 | 45 |
| Llama 3.3 70B (Groq) | 1.36 | 7.36 | 173 |
| Qwen3 Coder | 0.96 | 7.30 | 54 |
| Kimi K2 | 1.26 | 7.28 | 28 |
| Grok 4.1 Fast | 0.81 | 7.21 | 105 |

**19 modelos ofrecen ≥7.20 de score compuesto por menos de $1.50/1k calls** (eran 15 pre-rescore). Cualquier emprendedor con presupuesto restringido tiene casi 20 candidatos válidos antes de mirar el tier premium — y eso sin contar los gratis (sección 2.3).

### 2.3 Joyas gratis (free + score ≥7.0)

El rescore disparó esta categoría: ahora hay **18 modelos gratuitos con score compuesto ≥7.0** (eran 5 pre-rescore). Top 12:

| Modelo | Final | Quality | tok/s | Provider |
|---|---|---|---|---|
| Nemotron 3 Nano Omni 30B-A3B | 7.84 | 7.75 | 203 | NVIDIA NIM |
| Qwen 3-Next 80B Instruct | 7.83 | 8.11 | 52 | NVIDIA NIM |
| Devstral 2 123B | 7.68 | 7.98 | 42 | NVIDIA NIM (cobertura parcial) |
| Nemotron 3 Base 33B (DGX Q4) | 7.63 | 7.83 | 63 | DGX local |
| Nemotron Nano 9B v2 | 7.59 | 7.73 | 54 | NVIDIA NIM |
| Qwen 3.5 397B | 7.51 | 8.07 | 21 | NVIDIA NIM |
| Gemma 4 31B | 7.50 | 8.19 | 22 | NVIDIA NIM |
| Ministral 14B | 7.44 | 8.02 | 22 | NVIDIA NIM |
| Gemma 4 31B (DGX Q4) | 7.42 | 8.22 | 9 | DGX local |
| Nemotron Super 49B v1.5 | 7.41 | 7.85 | 25 | NVIDIA NIM |
| DeepSeek V4 Flash | 7.39 | 7.90 | 17 | NVIDIA NIM |
| GPT-OSS 120B | 7.37 | 7.15 | 68 | Ollama Cloud |

**18 modelos gratuitos pasan el umbral 7.0** en score compuesto, casi todos vía NVIDIA NIM (FP16, quality alta) o DGX local. Para proyectos personales, prototipos o producción de bajo-medio volumen (<40 RPM en NIM), el costo en cuotas de modelo es **$0** y la quality es top-tier (Qwen 3-Next 80B quality 8.11, Gemma 4 31B 8.19). **Este es el hallazgo central del rescore v2.7**: lo gratis dejó de ser segunda categoría.

> ⚠️ El caveat 40 RPM aplica a TODA esta tabla salvo las dos DGX local (límite = tu hardware). Para alto throughput sostenido, NIM no escala — ahí se paga OpenRouter (mismo modelo, mayor RPM) o se usa el DGX propio.

### 2.4 Frontera de Pareto (no dominada — más barata Y mejor score)

Tras el rescore, la frontera de Pareto estricta **colapsa a un único punto**: **Nemotron 3 Nano Omni 30B-A3B (NVIDIA NIM, $0.00, final 7.84)** domina a todos los demás — es a la vez el más barato ($0) y de score máximo, así que ningún otro modelo es no-dominado.

Esto es matemáticamente correcto pero operativamente engañoso: con tantos modelos a $0/call empatados en el costo mínimo, el de mayor score domina a todos. La pregunta útil no es "el punto Pareto" sino **"el mejor por restricción de provider/RPM"**. Frontera práctica por tier de costo:

| Restricción | Mejor opción | Final | $/1k | Por qué |
|---|---|---|---|---|
| $0 sin límite de RPM propio (DGX) | Nemotron 3 Base 33B (DGX Q4) | 7.63 | 0.00 | On-prem, sin cap externo |
| $0 vía NIM (cap 40 RPM) | Nemotron 3 Nano Omni 30B-A3B | 7.84 | 0.00 | Score máximo gratis |
| Pagado mínimo, alto RPM | Llama 3.1 8B Instant (Groq) | 7.67 | 0.14 | Mejor calidad/precio absoluta con RPM alto |
| Pagado, score máximo | Devstral Small (OpenRouter) | 7.84 | 0.48 | #1 empatado, sin cap de RPM |

Si la decisión es solo costo vs score, se elige según el provider que tu volumen tolere. El rescore expone que **a $0 hay competencia interna fuerte** — el cuello de botella ya no es el costo, es el RPM y la quality.

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
| **NIAH-ES** | **Devstral Small** | **7.24** | 7.84 |
| string_precision | Devstral Small | 8.79 | 7.84 |
| customer_support | Mistral Small 4 | 8.12 | 7.51 |
| orchestration | Qwen 3.5 397B (Ollama Cloud) | 7.66 | 6.52 |

**Patrones**:
- **Llama 3.1 8B Instant (Groq) lidera 4 suites** (translation, tool_calling, structured_output, content_generation) con costo $0.14/1k. Modelo chico, ultra rápido, mejor multilingüe.
- **Mistral Small 4** lidera customer_support y agent_capabilities — fortaleza en respuestas estructuradas + multi-step planning.
- **Devstral Small** es el rey de **NIAH-ES** (long-context español) y **string_precision** — útil para retrieval, ETL, data extraction.
- **GPT-OSS 120B** lidera agent_long_horizon en su tier free — sub Ollama Cloud lo desbloquea.
- **Qwen 3.5 397B (Ollama Cloud)** especialista en orchestration aunque global mediocre — útil si el pipeline es multi-step puro.

---

## 3. Provider matters — el mismo modelo en distintos providers

Una de las dimensiones más subestimadas: **el mismo modelo puede dar score muy distinto según el provider que lo expone**, por cuantización, configuración interna, rate limits, o limitaciones del gateway.

### 3.1 MiMo Xiaomi: direct vs OpenRouter (delta enorme, ahora 100% de costo)

| Modelo | Provider | Final | Quality | $/1k | Δ vs OpenRouter |
|---|---|---|---|---|---|
| MiMo V2-Omni (Xiaomi direct) | Xiaomi sub $14/mes | **7.46** | 7.27 | 0.13 | +0.52 |
| MiMo-V2-Omni (multimodal) | OpenRouter | 6.94 | 7.52 | 3.12 | base |
| MiMo V2-Pro (Xiaomi direct) | Xiaomi sub $14/mes | **7.39** | 7.61 | 0.13 | +0.59 |
| MiMo-V2-Pro | OpenRouter | 6.80 | 7.52 | 4.80 | base |

**Hallazgo (más nítido post-rescore)**: Xiaomi direct entrega +0.52 a +0.59 puntos sobre el mismo modelo en OpenRouter. Nótese que **la quality es IGUAL o incluso mayor en OpenRouter** (7.52 vs 7.27/7.61) — el delta es **enteramente de costo**: la sub Xiaomi extrapola a $0.13/1k vs $3.12-4.80/1k en OpenRouter. Tras el rescore provider-aware esto es transparente: el mismo modelo, misma calidad, 24-37x más barato vía sub directa. **Para usuarios MiMo, suscribirse al directo es estrictamente mejor que pagar por OpenRouter**.

### 3.2 DeepSeek V4 — tres providers, comportamiento muy distinto

| Variante | Provider | Final | Quality | Tests OK | Notas |
|---|---|---|---|---|---|
| DeepSeek V4 Flash | NIM gratis | **7.39** | 7.90 | 87/91 | Quality top, gratis → sube fuerte con el rescore |
| DeepSeek V4 Flash | Ollama Cloud sub | 6.11 | 5.15 | 57/57 | **Cuantización degrada quality** |
| DeepSeek V4 Pro | Ollama Cloud sub | 6.01 | 5.24 | 55/57 (97%) | **Idem** |
| DeepSeek V4 Pro | OpenRouter pagado | 5.98 | 6.32 | 91 + 57 | $0.48/$1.44 per M tokens → ahora penalizado por costo |
| DeepSeek V4 Pro | NIM gratis | ❌ | — | 0/7 | **Cascada 504, NO USAR** |

**Hallazgos críticos** (nuevos en mayo):

1. **DeepSeek V4 Pro vía NIM NO funciona en producción** — cascada 504 reproducible **2 veces** (abril 28 + mayo 3). El gateway NIM no maneja modelo gigante con prompts largos. Descartado para producción.

2. **DeepSeek V4 vía Ollama Cloud sub tiene calidad notablemente menor** que NIM. Quality cae de 7.90 (NIM) a 5.15 (Ollama Cloud) para Flash. La sub funciona (97% completion) pero la cuantización del cloud Ollama es más agresiva.

3. **El rescore reordena el ganador**: DeepSeek V4 Flash NIM (gratis, quality 7.90) salta a **7.39 final** y es ahora la opción clara para DeepSeek V4. DeepSeek V4 Pro OpenRouter, que antes parecía la mejor opción pagada, cae a **5.98 (#72, último)** — el costo provider-aware lo penaliza y su quality (6.32) ya era baja. Conclusión post-v2.7: para DeepSeek V4 usar **NIM gratis (Flash) y atención al cap 40 RPM**; OpenRouter solo si se necesita el RPM y se acepta el score bajo.

### 3.3 Qwen 3.5 397B — NIM vs Ollama Cloud

| Provider | Final | Quality |
|---|---|---|
| NIM gratis (FP16) | **7.51** | 8.07 |
| Ollama Cloud sub | 6.52 | 5.50 |

**Hallazgo**: Quality cae de 8.07 (NIM FP16) a 5.50 (Ollama Cloud cuantizado). Mismo modelo, **delta de quality de -2.57 puntos por cuantización** (la explicación más probable es Q4 vs FP16 + sampling). Tras el rescore el delta de final crece a **-0.99** (7.51 vs 6.52): el NIM FP16 gratis, además de mejor quality, no carga costo. Para producción con Qwen 3.5: **NIM gratis es estrictamente mejor que Ollama Cloud**.

### 3.4 Gemma 4 31B vs GLM 5 / 5.1 — el rescore rompe la "paridad"

Antes del rescore, NIM y OpenRouter daban resultados casi idénticos para estos modelos porque el costo era inerte. Tras el rescore provider-aware el costo separa lo gratis de lo pagado:

| Modelo | OpenRouter | NIM | Δ | Causa del Δ |
|---|---|---|---|---|
| Gemma 4 31B FP16 | 7.50 ($0.99/1k) | 7.50 ($0) | 0.00 | OpenRouter Gemma sigue barato → empate |
| GLM 5 / GLM-5.1 | 6.97 ($5.01/1k, "5.1") | 7.28 ($0, "5") | −0.31 a favor de NIM | GLM-5.1 en OpenRouter es caro → cae |

**Hallazgo (cambió con el rescore)**: para Gemma 4 31B, OpenRouter ($0.99/1k) y NIM ($0) **siguen empatados a 7.50** porque Gemma en OpenRouter es muy barato — el costo casi no separa. Pero para GLM, el NIM gratis (GLM 5, 7.28) ahora **supera** a la versión OpenRouter de pago (GLM-5.1, $5.01/1k, 6.97) por +0.31. La quality es comparable; el rescore expone que pagar $5/1k por GLM no compra ventaja. Para modelos NIM con equivalente OpenRouter caro, **NIM gratis es estrictamente mejor**; solo se justifica OpenRouter si se necesitan >40 RPM.

### 3.5 Cuantización Q4 en hardware propio (DGX Spark)

| Modelo | Provider | Quality | Final | Δ vs FP16 |
|---|---|---|---|---|
| Gemma 4 31B (DGX Q4_K_M) | Ollama local | 8.22 | 7.42 | +0.03 quality, -0.08 final |
| Gemma 4 31B (NIM FP16) | NIM | 8.19 | 7.50 | base |
| Nemotron 3 Super 120B (DGX Q4) | Ollama local | 7.96 | 7.40 | — |
| Nemotron 3 Base 33B (DGX Q4) | Ollama local | 7.83 | 7.63 | — |

**Hallazgo cuantización (post-rescore)**: con el costo ahora bien medido ($0 tanto en DGX local como en NIM), Q4 vs FP16 prácticamente empatan en compuesto (7.42 vs 7.50, Δ −0.08) — antes el delta parecía −0.61 por un artefacto de costo. Quality casi idéntica (8.22 vs 8.19); la única diferencia real es velocidad (Q4 ~9 tok/s en DGX vs 22 tok/s en NIM FP16). Para datos sensibles on-prem, Q4 es perfectamente viable y ahora el ranking lo refleja: Nemotron 3 Base 33B (DGX Q4) sube a **7.63 (#8 global)**.

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
| Qwen 3-Next 80B Instruct (NIM) | 7.80 | 7.83 | −0.03 |
| Qwen 3.5 397B (Ollama Cloud) | 7.72 | 6.52 | +1.20 |

**Hallazgo**: Qwen 3.5 cloud rinde +1.20 a +1.61 puntos por encima de su score global cuando se le da tools. Esto explica por qué muchos pipelines en producción que usan Qwen + tools funcionan mejor de lo que el ranking single-turn predice. Nota: la suite tool_calling NO se rescoreó (es quality de tool calling, no costo) — pero las referencias de "Final" sí reflejan el ranking compuesto v2.7.

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
| Devstral Small | 8.56 | 7.84 | +0.72 |
| Gemini 2.5 Flash Lite | 8.23 | 7.74 | +0.49 |

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

### 6.1 Costos mensuales — los más baratos con score >7.0 (post-rescore)

Con el rescore provider-aware, los $/mes ahora reflejan el precio real por proveedor. **16 modelos gratuitos** dan score >7.0 a $0/mes (cuota de modelo; sub Ollama Cloud aparte):

| Modelo | $/mes (10k calls) | Final | Apto para producción |
|---|---|---|---|
| Nemotron 3 Nano Omni 30B (NIM) | 0 | 7.84 | Sí (cap 40 RPM) |
| Qwen 3-Next 80B Instruct (NIM) | 0 | 7.83 | Sí (cap 40 RPM) |
| Devstral 2 123B (NIM) | 0 | 7.68 | Sí (cobertura parcial) |
| Nemotron 3 Base 33B (DGX local) | 0 | 7.63 | Sí (on-prem, sin cap externo) |
| Qwen 3.5 397B (NIM) | 0 | 7.51 | Sí (cap 40 RPM) |
| Gemma 4 31B (NIM) | 0 | 7.50 | Sí (cap 40 RPM) |
| GPT-OSS 120B (Ollama Cloud) | 0 (sub $30/mes) | 7.37 | Sí |
| MiMo V2-Omni (Xiaomi direct) | $1.30 (sub $14/mes) | 7.46 | Sí |
| MiMo V2.5 (Xiaomi sub) | $1.30 | 7.45 | Sí |
| Llama 3.1 8B Instant (Groq) | $1.40 | 7.67 | Sí (RPM alto) |
| MiMo V2.5-Pro (Xiaomi sub) | $2.50 | 7.42 | Sí |
| Nemotron 3 Nano 30B (OpenRouter) | $3.20 | 7.43 | Sí (RPM alto) |
| Devstral Small (OpenRouter) | $4.80 | 7.84 | Sí (RPM alto, #1 global) |
| Llama 4 Scout 17B (Groq) | $5.40 | 7.69 | Sí (RPM alto) |
| Gemini 2.5 Flash Lite (OpenRouter) | $6.30 | 7.74 | Sí (RPM alto, propietario) |

**Observación clave (cambió con el rescore)**: para 10k calls/mes, **el #1 y #2 globales son gratis** (Nemotron 3 Nano Omni y Qwen 3-Next 80B vía NIM, ambos 7.83-7.84). Antes el ranking premiaba con score 7.0+ a 5 modelos gratis; ahora son 16. El emprendedor LATAM puede operar el modelo de mayor score del benchmark por **$0/mes** (NIM, cap 40 RPM) o por **$4.80/mes** (Devstral Small en OpenRouter, sin cap, mismo 7.84). El presupuesto dejó de ser la restricción para acceder a top-tier.

### 6.2 Costos mensuales — los 5 más caros (referencia comparativa)

| Modelo | $/mes | Final | #/72 | Vale la pena? |
|---|---|---|---|---|
| GPT-5.5 | $465 | 6.10 | #69 | NO vs Devstral Small 7.84 a $4.80/mes |
| Claude Opus 4.6 / 4.7 | $390 | 6.57 / 6.20 | #58 / #66 | NO |
| GPT-5.4 | $240 | 6.44 | #63 | NO vs GPT-5.4 Mini 7.39 a $24/mes |
| Claude Sonnet 4.6 | $234 | 6.34 | #65 | NO |
| Gemini 3.1 Pro | $186 | 6.18 | #67 | NO vs Flash Lite 7.74 a $6.30/mes |

**Diferencial extremo**: GPT-5.5 cuesta **$465/mes** para entregar 6.10 (#69) — un score por debajo de lo que un modelo gratis vía NIM entrega ($0/mes). Claude Opus 4.6/4.7 cuesta $390/mes para 6.57/6.20; Devstral Small entrega **7.84 por $4.80/mes** (81x más barato, +1.3-1.6 puntos arriba). Para emprendedores LATAM, los modelos premium API son operativamente inaccesibles vs alternativas open + sub — y tras el rescore el ranking lo dice sin ambigüedad. (Recordatorio: para debugging agentic crítico, el premium aún vale lo que cuesta — sección 0; pero ese caso de uso NO es lo que mide este ranking compuesto.)

### 6.3 Pareto de costo-eficiencia por perfil

- **Bootstrap ($0/mes)**: Nemotron 3 Nano Omni 30B o Qwen 3-Next 80B Instruct (NIM, 7.83-7.84, quality 7.75-8.11). Cero costo recurrente, tope 40 RPM — perfecto para blog + agente N8N de bajo-medio volumen.
- **Microemprendimiento ($14-30/mes con sub)**: MiMo V2.5 (Xiaomi sub $14, 7.45 + NIAH 7.05) o GPT-OSS 120B (Ollama Cloud sub $30, 7.37 + ALH 8.60, mejor agente multi-turno gratis).
- **PYME con RPM alto ($5-15/mes pay-as-you-go)**: Devstral Small (OpenRouter, $4.80, 7.84 + NIAH-ES 7.24, #1 global sin cap de RPM) o Llama 4 Scout (Groq, $5.40, 7.69, 170 tok/s). La opción para cuando NIM 40 RPM no alcanza.
- **Volumen alto + multi-tarea ($10-50/mes)**: Llama 3.3 70B Groq ($13.60, 7.36) + Mistral Small 4 ($9.40, 7.51) + Devstral Small ($4.80) según tipo de tarea, todos con RPM alto.

---

## 7. Regresiones — cuando la versión nueva es peor

Comparativas v2.7 entre versión anterior y nueva del mismo modelo (finales post-rescore):

| Anterior | Final | Nueva | Final | Δ Final | Δ Quality |
|---|---|---|---|---|---|
| Qwen 3-Next 80B **Instruct** | 7.83 | Qwen 3-Next 80B **Thinking** | 7.19 | **−0.64** | −1.22 |
| **Devstral Small** | 7.84 | **Devstral 2 (Dic 2025)** | 7.09 | **−0.75** | −0.09 |
| **GPT-4.1** | 6.60 | **GPT-5.5** | 6.10 | **−0.50** | −0.33 |
| **Claude Opus 4.6** | 6.57 | **Claude Opus 4.7** | 6.20 | **−0.37** | −0.40 |
| GPT-5.4 Mini | 7.39 | GPT-5.4 | 6.44 | **−0.95** | −0.28 |
| Gemini 2.5 Pro | 5.98 | Gemini 3.1 Pro | 6.18 | +0.20 | +0.88 (!) |
| **Avances reales:** | | | | | |
| Gemini 2.5 Flash Lite | 7.74 | Gemini 3.1 Flash Lite | 7.44 | −0.30 | +0.03 |
| Kimi K2.5 | 6.49 | Kimi K2.6 | 6.44 | −0.05 | +1.31 |

**Hallazgos (re-leídos post-rescore)**:

**Regresión 1 — Devstral Small > Devstral 2 (ahora −0.75)**: el "Devstral 2" de diciembre 2025 (123B en OpenRouter, $3.12/1k) saca 7.09 contra **7.84** del Small original (24B, $0.48/1k). El rescore **amplió la brecha** de −0.43 a −0.75 porque Devstral 2 es además ~6.5x más caro. El modelo más grande es marginalmente peor en quality (−0.09) y mucho peor en costo-eficiencia. El Small está más afinado en NIAH-ES (7.24 vs 6.75) y string_precision (8.79).

**Regresión 2 — Qwen 3-Next Thinking vs Instruct (−0.64, −1.22 quality)**: el modelo razonador es **estrictamente peor** que el instruct en single-turn. Quality cae **−1.22 puntos**; el final cae menos (−0.64) porque ambos son gratis en NIM y el costo no los separa. Esto confirma: **en single-turn, thinking pierde en TODO, incluido razonamiento puro**.

**Regresión 3 — GPT-5.4 Mini > GPT-5.4 (−0.95, la más grande)**: GPT-5.4 Mini (7.39, $2.40/1k) supera al GPT-5.4 full (6.44, $24/1k) por casi un punto. El rescore expone que pagar 10x por el "full" entrega **menos** score. Mismo patrón GPT-4.1→GPT-5.5 (−0.50): el thinking-by-default consume budget y el precio premium no compra ventaja en single-turn.

**Regresión 4 — Claude Opus 4.7 vs 4.6 (−0.37)**: Opus 4.7 saca menor que 4.6 en compuesto (6.20 vs 6.57) y también en NIAH-ES (5.10 vs ~5.5 estimado). Trackers terceros confirman regresión en MRCR multi-needle. Anthropic priorizó razonamiento sobre retrieval en 4.7. Ambos están al fondo del compuesto (#66 y #58) por costo.

**Caso raro — Gemini 2.5 Pro → 3.1 Pro (ahora final SUBE +0.20, quality +0.88)**: tras el rescore, el upgrade ya no luce como regresión: Gemini 2.5 Pro cayó tanto por costo (a 5.98, #71) que el 3.1 Pro (6.18) lo supera incluso siendo más caro, gracias a su mejor quality. **El modelo SÍ mejoró**; el rescore lo dejó más claro que antes.

**Conclusión patrón**: las regresiones reales siguen siendo thinking models o tier full/Pro que reemplazan no-thinking (Qwen Instruct→Thinking, GPT-4.1→5.5, GPT-5.4 Mini→full, Opus 4.6→4.7). El thinking by default es un anti-pattern para single-turn, y el rescore agregó una capa: **cuando el upgrade además sube el precio, la penalización compuesta se duplica**. Los avances reales vienen del tier Flash Lite / variantes Mini, que combinan quality estable con costo bajo.

---

## 8. Open-source vs propietario — ¿se cerró la brecha?

### 8.1 Promedios

| Categoría | n | Score compuesto | Quality |
|---|---|---|---|
| Open-source | 48 | 7.20 | 7.45 |
| Propietario | 24 | 6.93 | 7.52 |

**Hallazgo (cambió con el rescore)**: antes la diferencia compuesta era ~0.04 (virtual empate). Tras el rescore provider-aware, el **open-source promedio supera al propietario por +0.27 puntos** (7.20 vs 6.93) — manteniendo quality casi igual (−0.07). La razón es estructural: la mayoría del open-source corre gratis (NIM) o muy barato, mientras los propietarios premium cargan costo alto que ahora se penaliza correctamente. **El top open-source también lidera** (Devstral Small 7.84 > top propietario Gemini 2.5 Flash Lite 7.74, +0.10). En toda la distribución, el open-source ya no está en paridad: está adelante.

### 8.2 Por pilar — top open vs top closed

| Pilar | Top Open | Score | Top Closed | Score | Δ |
|---|---|---|---|---|---|
| Razonamiento | Llama 4 Scout 17B | 8.26 | Gemini 3.1 Flash Lite | 7.89 | +0.37 |
| Coding | Llama 4 Scout 17B | 8.15 | GPT-4.1 | 7.92 | +0.23 |
| Contenido | Llama 3.1 8B Instant | 8.27 | MiMo V2.5 (Xiaomi) | 7.97 | +0.30 |
| Agentes | Llama 3.1 8B Instant | 8.06 | Grok 4.1 Fast | 7.51 | +0.55 |

**En los 4 pilares, el top open-source supera al top propietario**. En 2024 esto NO era el caso — la brecha era de 0.5+ puntos a favor de Claude/GPT. En mayo 2026, **la brecha se cerró y se invirtió** en single-turn.

### 8.3 Caveat importante

El propietario top en este benchmark es Gemini 2.5 Flash Lite (7.74, #4 global), no Claude Opus o GPT-5. La razón: **los flagship propietarios son thinking-by-default + caros, y eso los penaliza en single-turn corto bajo el rescore de costo**. En tareas multi-turn complejas con tool use intensivo (como debugging real), Claude Opus probablemente sigue dominando — caso Hetzner en sección 0. Pero para 80% de casos del emprendedor LATAM, **open-source ya superó a propietario** — y con el rescore la ventaja promedio es de +0.27 puntos, no un empate.

### 8.4 Top 10 open-source globales (post-rescore)

| # | Modelo | Final | $/1k | License |
|---|---|---|---|---|
| 1 | Devstral Small | 7.84 | 0.48 | Apache 2.0 |
| 2 | Nemotron 3 Nano Omni 30B-A3B (NIM) | 7.84 | 0.00 | NVIDIA Open License |
| 3 | Qwen 3-Next 80B Instruct (NIM) | 7.83 | 0.00 | Apache 2.0 |
| 4 | Llama 4 Scout 17B (Groq) | 7.69 | 0.54 | Llama Community |
| 5 | Devstral 2 123B (NIM) | 7.68 | 0.00 | Apache 2.0 |
| 6 | Llama 3.1 8B Instant (Groq) | 7.67 | 0.14 | Llama Community |
| 7 | Nemotron 3 Base 33B (DGX Q4) | 7.63 | 0.00 | NVIDIA Open License |
| 8 | Gemma 4 26B MoE | 7.52 | 0.49 | Apache 2.0 |
| 9 | Qwen 3.5 397B (NIM) | 7.51 | 0.00 | Apache 2.0 |
| 10 | Mistral Small 4 | 7.51 | 0.94 | Apache 2.0 |

**6 de los 10 mejores open-source son gratis ($0/call)** — todos vía NIM o DGX local. El rescore confirmó que el mejor open-source no solo iguala al propietario en quality, sino que lo hace a costo cero o casi cero.

---

## 9. Anti-patterns del marketing — claims que no se sostienen

Seis claims comunes en marketing AI 2025-2026 que la data del benchmark NO respalda:

### 9.1 "Más parámetros = mejor"

Mistral Large 3 (675B) saca 7.38 final (gracias a ser gratis en NIM), 8.18 quality. **Nemotron 3 Nano 30B saca 7.43 final, 7.79 quality** — modelo **22.5x más chico, mejor en compuesto** y comparable en quality. Llama 3.1 8B Instant (8B activos) saca 7.67 — más alto que casi cualquier modelo 100B+ del benchmark excepto el empate de cabeza (Devstral Small 24B, Nemotron 3 Nano Omni 30B, Qwen 3-Next 80B). El tamaño no compra ranking; la arquitectura afinada + costo bajo sí.

### 9.2 "Thinking by default es mejor"

Qwen 3-Next 80B: Instruct 7.83 → Thinking 7.19 = **−0.64 puntos**. Con quality cayendo **−1.22**. Por pilar la penalización de quality es generalizada (Razonamiento, Coding, Contenido, Agentes todos abajo), no solo en suites donde "no se necesita razonar".

GPT-5.5 (thinking-by-default) 6.10 vs GPT-4.1 6.60 = **−0.50**. GPT-5.4 full 6.44 vs GPT-5.4 Mini 7.39 = **−0.95**. Patrón consistente: el thinking caro pierde.

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

Claude Opus 4.7 ($39/1k) saca 6.20 final (#66/72), 7.64 quality. Devstral Small ($0.48/1k) saca 7.84 final (#1). **El gap es +1.64 a favor del barato, a 81x menos costo**. En quality, Opus está top 7 (7.64 vs 8.22 Gemma DGX Q4) — pero la diferencia es <10% y el costo es 81x mayor. El rescore v2.7 dejó este anti-pattern brutal: los 5 modelos más caros del benchmark ocupan posiciones #58-#71.

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

**Implicación crítica**: para tasks que requieren context >256K en producción, **GPT-4.1 vía OpenAI directo o OpenRouter es la única opción confirmada al 22 mayo 2026**. Pendiente probar Gemini 3.x Pro vía Google directo.

---

## 10. Top 5 hallazgos sorpresivos del v2.7

### 10.1 El rescore de costo invirtió free vs paid (y CERO sigue siendo la correlación cost↔quality)

El hallazgo más fuerte de v2.7: tras recalcular el costo provider-aware sobre 7.483 runs, el tier **gratis supera en compuesto al pagado** (7.19 vs 7.06), revirtiendo el pre-v2.7 (6.58 vs 7.01). El #1 y #2 globales ahora son gratis (NIM). A la vez, la correlación cost↔quality sigue en ~cero (+0.05, p=0.73, n=47): **los premium NO son peores en quality, son más caros y lentos**. Lo que cambió no es la calidad de nadie — es que el costo dejó de ser un campo inerte y ahora discrimina (correlación cost↔compuesto se profundizó de −0.671 a −0.748). Importante distinguir: para decisiones de producción de volumen LATAM, el score compuesto **es** la métrica relevante; el insight académico es que la quality bruta no penaliza al premium.

### 10.2 DeepSeek V4 cambia drasticamente de quality según provider

DeepSeek V4 Flash NIM (FP16): quality 7.90. DeepSeek V4 Flash Ollama Cloud: quality 5.15. **Misma versión del modelo, delta de quality −2.75 puntos por provider**. La cuantización agresiva del Cloud Ollama degrada el output radicalmente. Para producción con DeepSeek V4: **NIM gratis (Flash)**, que tras el rescore sube a 7.39 — la versión OpenRouter Pro cayó al último puesto (#72) por costo, así que ya no es recomendación.

### 10.3 MiMo Xiaomi direct >> MiMo OpenRouter

MiMo V2-Omni Xiaomi direct (sub $14/mes): final 7.46. MiMo-V2-Omni OpenRouter: final 6.94. **Delta +0.52 puntos por provider**. MiMo V2-Pro mismo patrón: +0.59. La sub Xiaomi entrega mejor performance que pagar el mismo modelo en OpenRouter — caso raro donde la suscripción es estrictamente mejor que pay-as-you-go.

### 10.4 Lost-in-the-middle DESAPARECE con N=5 needles

El piloto NIAH-ES v1 (1 needle/slot) reportó "Opus 4.7 cae −3.0 puntos al 50% del 4K". Eso fue **artefacto de N=1**. Con 5 needles promediados (v2), el delta máximo entre 25%-50%-75% en TODOS los modelos medidos es **0.04-0.21 puntos** — virtualmente plano. Lección metodológica: **N≥5 mínimo para hallazgos publicables**. Lost-in-the-middle reportado en literatura (Liu et al. 2023) puede ser real para inglés con prompts académicos, pero NO es detectable en español neutro con estos needles, en estos modelos, con N=5.

### 10.5 GPT-OSS 120B (Ollama Cloud) lidera ALH con +1.23 sobre su single-turn

GPT-OSS 120B sale #33 en single-turn (7.37 — bajó de #13 a #33 porque el rescore subió a 32 modelos por encima, casi todos gratis/baratos) pero lidera **agent_long_horizon con 8.60** — delta +1.23 sobre su línea base. Ningún otro modelo sube tanto. Hipótesis: la arquitectura GPT-OSS está optimizada para context retention multi-turno + skill orchestration, y eso aparece cuando la suite mide multi-turn explícitamente. Para emprendedores con sub Ollama Cloud ($30/mes): **GPT-OSS 120B sigue siendo la mejor opción para agentes complejos multi-turno**, aunque en single-turn ya no destaca.

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

### 12.1 Devstral 2 123B (NIM) — agent_capabilities = 0.00 → DEPRECADO POR PROVIDER

**Validado 2026-05-07**: re-run intentado falla con cascada de **error 400 en 29/29 tests**. NIM ya no soporta Devstral 2 en mayo 2026 (funcionaba en abril con 68/91 cobertura, deprecado silenciosamente). El score queda **frozen** (post-rescore 7.68, subió por ser gratis en NIM, pero recordar que tiene `agent_capabilities=0.00` y cobertura parcial) y no es re-validable hasta que aparezca otro provider.

**Implicación nueva**: provider stability matters month-to-month. Modelos en NIM pueden desaparecer sin aviso entre lotes. Considerar OpenRouter como fallback o aceptar que ese modelo específico salió del catálogo medible.

### 12.2 GPT-5.5 score 6.10 — caída masiva vs GPT-4.1 → NO MEDIBLE CON ESTA METODOLOGÍA

**Validado 2026-05-07**: re-run intentado expone limitación estructural del benchmark con thinking models extremos.

**Diagnóstico**: con `THINKING_MIN_TOKENS=8192` GPT-5.5 retorna 151/151 runs con `content=""` (consume todo el budget en reasoning interno). Subido a `16384` el smoke test devuelve respuesta correcta, pero en bench real **cada test toma 16-50 minutos** (ETA 181 horas para 223 tests, killed tras 12/223 en 9h25min).

**Conclusión honesta**: GPT-5.5 es OVER-thinking y nuestra metodología single-shot no lo mide bien. `THINKING_MIN_TOKENS` revertido a 8192 (defaults para los demás thinking models — GPT-5/o1/o3/Kimi K2.6/Nemotron/Gemma 4 funcionan bien). El score 6.10 de GPT-5.5 (post-rescore, hundido aún más por su costo $46.50/1k, #69) queda como **provisorio y no comparable** — para producción mejor mirar SWE-bench Verified, Aider Polyglot u otros benchmarks que toleren respuestas largas.

### 12.3 Llama 4 Maverick — final 7.13 vs los Llama Groq en 7.36-7.69 → DIFERENCIA NO ES AISLABLE

**Validado 2026-05-08**: Groq **NO hostea Llama 4 Maverick** (catálogo confirmado vía API: solo tiene Scout 17B/16E). Tampoco hay credenciales para Together/Fireworks/DeepInfra configuradas.

**Reformulación de hipótesis**: el +0.56 entre Scout (Groq, 7.69) vs Maverick (OpenRouter, 7.13) NO es atribuible cleanly a provider — son **modelos distintos** (Scout 17B/16E vs Maverick 17B/128E, arquitecturas MoE diferentes). La diferencia es modelo+provider combinado, no aislable con providers actuales.

**Test crítico real**: requeriría agregar Together/Fireworks como providers para testear Maverick fuera de OpenRouter. Pendiente para próxima iteración.

### 12.4 Qwen 3.5 397B (Ollama Cloud) — translation 4.41

El score más bajo del benchmark en cualquier suite individual. Posibles causas:
1. Bug del adapter Ollama Cloud — alguna config rechaza español neutro.
2. Cuantización específica de Ollama Cloud (no documentada, probablemente Q4 agresivo) degrada el español más que en otros modelos.
3. Genuina contaminación de chino en español en el modelo cloud.

**Re-correr 5 prompts en español puro y comparar con NIM** (mismo modelo, score 7.51 final post-rescore, quality 8.07 — claramente mejor).

### 12.5 Inspección cualitativa Opus 4.7 NIAH-ES → REFUSAL PATTERN, no paráfrasis

**Auditoría manual 2026-05-07** de 5 respuestas (`benchmarks/results/responses/20260430_200512/`):

| Test | Score final | Patrón observado |
|---|---|---|
| `api_key_4000_p50` | 3.04 | **REFUSAL**: "No voy a proporcionar esa información... compartir credenciales es mala práctica" |
| `budget_q3_4000_p25` | 6.10 | Extracción correcta (USD 247,800, Bogotá/CDMX) + caveat "incongruente" |
| `discount_code_16000_p75` | 5.63 | Extracción exacta concisa ("CHILE2026-EARLY... 15 de junio de 2026") |
| `ssh_port_4000_p50` | 5.94 | Extracción correcta (puerto 48372 servidor analytics-prod-cl-01) + warning prompt injection |
| `investor_meeting_4000_p50` | 5.98 | Extracción exacta perfecta ("3 de septiembre de 2026 a las 14:30 UTC-3") |

**Hipótesis "paráfrasis" REFUTADA**: Opus extrae texto exacto cuando responde. La extracción es semánticamente correcta y coincide con el needle.

**Hipótesis nueva CONFIRMADA — Opus es REFUSAL-PRONE**: en el test `api_key` (un secreto de credenciales) la guardarraíl de seguridad de Opus se activa y refusa, scoreando 3.04. Adicionalmente en tests con datos reales (ssh_port, budget) Opus agrega caveats de seguridad o "incongruente" que el juez Phi-4 puede estar penalizando como "ruido extra" pese a ser extracción correcta.

**Implicación operativa**: el bottom de Opus en NIAH-ES no refleja debilidad de retrieval — refleja (a) safety refusals en credentials, (b) verbosity con caveats que Phi-4 penaliza vs respuesta concisa pura. Para producción Opus sigue siendo válido en NIAH-ES si el caso de uso no toca credentials/secrets sensibles.

### 12.6 MiMo Xiaomi — pricing es ambiguo

Reportamos costos $0.13-0.46/1k para los MiMo, pero el modelo de Xiaomi es **suscripción flat** ($14/mes con cap de tokens off-peak 0.8x). El cálculo $/1k assume token-by-token pricing extrapolado. Si el usuario satura el cap mensual, el costo por call efectivo sube. **El ranking de MiMo asume volumen moderado** — para volumen alto requiere recálculo.

### 12.7 Gemini 2.5 Pro → 3.1 Pro: quality sube +0.88, y post-rescore el final también sube (+0.20)

Caso raro re-leído tras v2.7: el upgrade entrega quality bruta materialmente mejor (6.52 → 7.40). Antes del rescore el final caía −0.10 (el costo no separaba bien); tras el rescore Gemini 2.5 Pro se hundió tanto por costo (5.98, #71) que el 3.1 Pro (6.18) ahora lo **supera** en compuesto pese a ser más caro, porque su quality justifica algo del precio. **No es regresión** — es la fórmula reflejando que el 3.1 Pro mejoró. Caso de "quality vs compuesto" para documentar.

### 12.8 DeepSeek V4 Pro NIM cascada 504 — patrón sistemático

Reproducible **2 veces** (abril 28 + mayo 3). NIM gateway no maneja modelo gigante con prompts largos. Nota post-rescore: la alternativa OpenRouter pagada cayó a #72 (último) por costo, así que para DeepSeek V4 la recomendación práctica es la variante **Flash en NIM gratis** (#39, 7.39); el Pro queda como no-recomendado por costo+disponibilidad. **Documentado en MODELOS.md como bloqueante de producción**.

---

## 13. Análisis de varianza intra-model (validado 2026-05-13)

**Pregunta**: ¿el ranking top 5 es estadísticamente significativo, o el delta entre posiciones está dentro del ruido intra-model?

**Diseño**: 5 prompts representativos (1 por pilar) × top 5 modelos × 5 reps = 124 runs OK (1 mistral falló empty response). Temperatura 0.7, juez Phi-4 local. Script: [`benchmarks/variance_analysis.py`](benchmarks/variance_analysis.py). Data: `benchmarks/results/variance_20260513_075505.json`.

### 13.1 Stdev por (modelo, pilar) — 5 reps

| Modelo | Razonamiento | Coding | Contenido | Agentes | NIAH-ES |
|---|---|---|---|---|---|
| devstral | 8.80 ± **0.000** | 8.32 ± **1.145** | 8.80 ± 0.000 | 7.92 ± 0.769 | 3.20 ± 0.000 |
| groq-gpt-oss-20b | 8.96 ± 0.219 | 9.60 ± 0.000 | 8.80 ± 0.000 | 8.40 ± **1.020** | 2.80 ± 0.000 |
| groq-llama-3.1-8b | 8.40 ± 0.400 | 6.00 ± **1.095** | 7.68 ± 0.179 | 7.52 ± 0.867 | 3.04 ± 0.219 |
| groq-llama-4-scout | 8.80 ± 0.000 | 8.88 ± 0.716 | 7.60 ± 0.000 | 8.72 ± 0.438 | 2.96 ± 0.219 |
| mistral-small-4 | 9.10 ± 0.200 | 9.20 ± 0.000 | 8.80 ± 0.000 | 8.56 ± 0.537 | 3.20 ± 0.490 |

### 13.2 Hallazgos cuantitativos

1. **Razonamiento, contenido y NIAH-ES son MUY estables run-to-run**: stdev ≤ 0.5 en todos los casos, mayoría con stdev=0.000 (los 5 reps coinciden en score exacto). Phi-4 es consistente y los modelos no oscilan en respuesta. Diferencias de 0.2-0.3 pts entre modelos en estos pilares son señal, no ruido.

2. **Coding tiene varianza alta en algunos modelos**: devstral (stdev 1.145, range 2.80) y llama-3.1-8b (stdev 1.095, range 2.00). Un único run extremo puede mover el ranking 0.2-0.4 puntos. **Implicación**: para modelos con baseline coding ~7.5-8.0, el ranking inter-modelo dentro de ±0.3 puntos es estadísticamente indistinguible con N=1.

3. **Agentes (tool calling) es el pilar más inestable**: 4 de 5 modelos con stdev 0.4-1.0, range hasta 2.80. Confirma que tool calling es el pilar más frágil — cualquier ranking inter-modelo en agentes con N<5 hay que interpretarlo con asterisco.

4. **NIAH-ES uniformemente bajo en top 5 (~3.0)**: confirma que el prompt específico (`niah_es_discount_code_4000_p50`) es difícil universalmente, no defecto de un modelo. Refuerza la validez del ranking NIAH-ES global como medida de capacidad real, no artefacto.

### 13.3 Implicaciones operativas

- **El ranking global con N=91+ tests es robusto** — la integración inter-suite cancela varianza intra-suite. Para los top 5, el orden es relativamente estable.
- **Diferencias <0.3 puntos en ranking top 5 son indistinguibles estadísticamente** dentro de single-run noise — usar quality_avg (sin pesar costo/velocidad) como tie-breaker o aceptar empate técnico.
- **Cuando un modelo tiene cobertura <50 runs**, su score puede estar inflado/deflado por un solo outlier de coding o agentes. Cobertura ≥91 (full single-turn) o ≥150 (single + NIAH + multi-turn) es lo mínimo defendible para usar como ranking publicado.
- **Phi-4 como juez es consistente**: cuando el modelo produce respuestas similares run-to-run, Phi-4 da el mismo score exacto. No introduce ruido adicional.

### 13.4 Caveats del análisis

- Solo top 5 — la varianza puede ser mayor en modelos del tier medio (score 6.5-7.0). Pendiente expandir a top 10-15.
- Solo 5 prompts (1 por pilar). Otros prompts del mismo pilar pueden tener varianza distinta.
- Temperatura 0.7 es el default. A temperatura 0 (algunos providers permiten) la varianza intra-pilar debería caer a ~0.0 en todos los pilares.

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

Salida esperada (post-rescore v2.7): `SignificanceResult(statistic=0.051, pvalue=0.731)`.

Confirma la sección 1: cost-quality NO correlacionan en quality bruta (ni antes ni después del rescore — el rescore no tocó quality). Para Spearman cost vs score_global compuesto, sustituir `quality_avg` por `score_global` y se obtiene `−0.748, p<0.001` (más fuerte que el −0.671 pre-v2.7: el costo dejó de ser inerte).

---

**Última actualización**: 22 de mayo de 2026 — v2.7 (rescore de costo provider-aware sobre 7.483 runs: se recalculó `cost_usd`/`cost_score`/`final`. Reordenó el ranking — Devstral Small y los gratis de NIM al top, premium caros al fondo, Opus 4.7 a #66/72. Quality/tool_calling/speed/latency sin cambios).

**Próxima revisión**: tras nuevos lotes de junio 2026 (suite agentic_debugging, NIAH-ES extensión a 50 modelos restantes, Gemini 3.x Pro vía Google directo, variance intra-model en top 10).

**Auto-regenerable**: este documento se reescribe completo desde `docs/data/models.json` con un agente data-scientist (`.claude/agents/data-scientist.md`). NO editar manualmente — los cambios se perderán en la próxima regeneración.
