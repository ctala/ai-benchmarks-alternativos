---
title: "Datasheet abril 2026 — snapshot del benchmark al cierre del mes"
mes: "2026-04"
fecha_snapshot: "2026-04-30"
version_benchmark: "v2.4.2 → v2.5.2 (cierre)"
audiencia: "Lectores que quieren entender la evolución mes a mes del benchmark"
---

# 📊 Datasheet abril 2026 — snapshot retroactivo

> 📍 **Disclaimer**: este benchmark NO sustituye a los benchmarks académicos validados (HumanEval, MMLU, GSM8K, SWE-bench, NIAH inglés). Es un complemento para emprendedores hispanohablantes que deciden producción real. Ver [README.md](README.md) para contexto completo.

## Cobertura al cierre de abril

| Métrica | Valor |
|---|---|
| Modelos catalogados | **113** |
| Modelos con cobertura ≥50 runs single-turn | **70** |
| Modelos con runs en agent_long_horizon (multi-turn 8+ turnos) | **38** |
| Modelos con runs en NIAH-ES (long-context retrieval español) | **8** (v2 solo) |
| Total runs preservados | **8,475** |
| Suites del benchmark | 23 single-turn + agent_long_horizon + niah_es + niah_es_1m = 26 |

## Lotes principales del mes

| Lote | Modelos | Tests | Hallazgo destacado |
|---|---|---|---|
| **Lote 9 NIM** (29 abril) | 12 modelos NIM gratis | 1,358 runs (117 errores) | Magistral Small NIM 0/91 (error 400 instant). DeepSeek V4 Pro NIM 0/91 (502/504 cascada). |
| **DGX Spark Lote 1** (29 abril) | Gemma 4 31B + Nemotron 3 Super 120B Q4 | 180 runs (1 timeout) | Gemma Q4 vs FP16 NIM = -0.36 puntos. |
| **Lote 10 agent_long_horizon** (29 abril) | 27 modelos × 12 tests | 324 runs (10 errores) | GPT-OSS 120B Cloud #1 agéntico (8.15). |
| **Lote 10b MiniMax** (29 abril) | M2.7, M2.7-Direct, M2.7-Highspeed | 36 runs | Provider matters: direct > OpenRouter +0.16. Highspeed = velocidad sin mejor calidad. |
| **Lote 11/11b/11c thinking** (29-30 abril) | 11 modelos hybrid forced reasoning | 144 runs | Thinking forzado EMPEORA multi-turn en 8/9 modelos. Solo Kimi K2.5 sube +0.73. |
| **NIAH-ES v1+v2** (30 abril) | 8 modelos × 12+60 tests | 576 runs | Devstral Small lidera 7.25 vs Opus 4.7 último 4.98. |
| **NIAH-ES v3 1M** (30 abril-1 mayo) | 4 modelos × 15 tests | 60 runs | Solo GPT-4.1 procesa 1M tokens efectivamente. Otros 3 cap en provider. |

## Top 10 score compuesto v2.4.2 (snapshot 30 abril)

Pesos: quality 50% / cost 20% / tool_calling 15% / speed 7.5% / latency 7.5%.

| # | Modelo | Final | Quality | Cost score |
|---|---|---|---|---|
| 1 | Llama 4 Scout 17B (Groq preview) | **8.11** | 7.93 | 8.83 |
| 2 | Llama 3.1 8B Instant (Groq) | 8.11 | 7.61 | 8.98 |
| 3 | Llama 3.3 70B (Groq) | 7.86 | 8.01 | 8.17 |
| 4 | GPT-OSS 20B (Groq) | 7.84 | 7.51 | 8.80 |
| 5 | Mistral Small 4 | 7.81 | 8.08 | 8.30 |
| 6 | Gemini 3.1 Flash Lite | 7.73 | 8.01 | 7.85 |
| 7 | GPT-OSS 120B (Ollama Cloud) | 7.69 | 7.81 | 10.00 |
| 8 | Grok 4.1 Fast | 7.62 | 8.13 | 8.18 |
| 9 | MiMo V2.5 (Xiaomi sub) | 7.62 | 7.68 | 8.84 |
| 10 | Devstral Small | 7.61 | 8.03 | 7.63 |

⚠️ **Esta tabla NO incluye runs de NIAH-ES** (suite nueva con scores típicamente menores). Ver datasheet mayo para ver cómo cambia el ranking al integrar NIAH.

## Top 5 NIAH-ES v2 (8 modelos al cierre de abril)

| # | Modelo | Score |
|---|---|---|
| 1 | Devstral Small | **7.25** |
| 2 | Mistral Small 4 | 7.06 |
| 3 | Llama 4 Scout 17B Groq | 6.89 |
| 4 | Llama 3.3 70B Groq | 6.26 |
| 5 | Gemini 3.1 Pro | 5.96 |
| ... | ... | ... |
| 8 | Claude Opus 4.7 | **4.98** ⬇ último |

## Top 5 agent_long_horizon (38 modelos al cierre)

| # | Modelo | Score | Notas |
|---|---|---|---|
| 1 | GPT-OSS 120B (Ollama Cloud) | **8.15** | Gratis con sub Ollama Cloud |
| 2 | Llama 4 Scout 17B (Groq) | 7.86 | |
| 3 | Llama 3.1 8B Instant (Groq) | 7.85 | |
| 4 | Devstral Small | 7.77 | Apache 2.0 |
| 5 | MiMo V2-Omni Xiaomi direct | 7.75 | Sub $14/mes |

## Hallazgos publicables del mes

1. **Provider matters cuantificado** — mismo modelo en provider directo (Xiaomi/Groq/NIM gratis/MiniMax) +0.16 a +0.25 vs OpenRouter. Confirmado en 4 proveedores.
2. **Thinking forzado EMPEORA agéntica multi-turn** en 8/9 modelos hybrid. Excepción: Kimi K2.5 +0.73.
3. **Why Opus doesn't top our benchmark** — quality 8.08 (top 6) pero costo 40-100x mayor + speed 5-10x menor lo penaliza en score compuesto. Phi-4 lo califica MEJOR que Llama (4.22 vs 4.00) — descarta sesgo del juez.
4. **"1M context declarado" ≠ retrieval efectivo** — solo GPT-4.1 procesa 1M sin error 400 (3/4 providers cap el context).
5. **Modelo gigante NO siempre gana** — Mistral Large 3 (675B) 6.89 < Nemotron Nano 9B v2 6.91 en NIM.
6. **Q4 cuantización cuesta -5%** en hardware propio DGX Spark.

## Limitación documentada (caso real)

MiniMax M2.7 (top #7 nuestro single-turn) NO pudo resolver problema técnico complejo en VPS Hetzner / OpenClaw. Opus 4.7 (fuera del top 10 nuestro) lo resolvió en minutos. Confirma que **nuestro benchmark NO mide debugging agentic real** — para esa dimensión, mirar SWE-bench Verified (Opus 4.7 = 87.6% top 1 globalmente).

## Versión del benchmark al cierre

**v2.5.2** (1 mayo 2026): final del bloque de abril con NIAH-ES v3 1M y cross-ref con literatura.
