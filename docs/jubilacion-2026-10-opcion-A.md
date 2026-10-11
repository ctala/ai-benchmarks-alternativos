# Jubilación de Modelos AI - Octubre 2026

**Fecha**: 2026-10-10
**Opción**: A
**Decisión**: Roster de 100 modelos (62 activos + 38 cupos)

> **Opción A - Regla Estricta**: Todos los dominados (62) se jubilan.

## Resumen Ejecutivo

- **Total modelos en catálogo**: 227
- **Activos**: 62
- **Jubilados**: 165
- **Cupos reservados**: 38

### Desglose de Jubilados

- **Retired**: 16
- **Provider Variant**: 54
- **Sin Runs**: 26
- **Dominado**: 69

### Dominados

- Total detectados: 69
- Jubilados (los más claramente dominados): 69
- Quedan activos: 0

**Motivo**: Todos los dominados se jubilan (regla estricta)

## Definición de Familia

**Familia** = mismo proveedor y misma línea base, sin importar generación.

Ejemplos:
- Qwen 3.5, 3.6, 3.7, 3.8 → familia "Qwen"
- GPT-5.5, GPT-5.6 Luna → familia "GPT"
- Claude Opus 4.7, 4.8 → familia "ClaudeOpus"

Ver `METODOLOGIA.md` para definición completa.

## Proyección de Costos

### Costo Mensual Estimado

**$103.54/mes**

- Base: **$1.67/modelo/mes**
- Fuente: $119/mes ÷ 71 modelos/mes (abr-sep 2026)
- Modelos activos: 62
- Cálculo: 62 × $1.67 = $103.54/mes

### Examen Completo de Todos los Activos

**$530.72** (si se re-midieran todos)

- Costo por examen completo: **$8.56** (22 suites)
- Cálculo: 62 × $8.56 = $530.72

## Criterios de Jubilación (Orden de Prioridad)

1. **Retired** — Proveedor deprecó el modelo
2. **Provider variant** — Mide serving, no calidad
3. **Sin runs** — Nunca medido (0 runs)
4. **Dominado** — Otro de su familia tiene Q >= y costo <=

## Listado Completo de Modelos

### Activos (62)

| # | Modelo | Quality | Costo/examen | Runs | Nota |
|---|--------|---------|--------------|------|------|
| 1 | Sakana Namazu | 8.59 | $0.0063 | 1728 |  |
| 2 | Qwen 3.8 Omni Flash | 8.55 | $0.0008 | 110 |  |
| 3 | Bonsai 2 27B | 8.54 | $0.0008 | 99 |  |
| 4 | GPT-5.6 Luna | 8.52 | $0.0019 | 162 |  |
| 5 | GLM 5.3 | 8.52 | $0.0070 | 193 |  |
| 6 | LongCat 2.0 | 8.52 | $0.0019 | 22 |  |
| 7 | GLM 5.3 Flash | 8.51 | $0.0008 | 143 |  |
| 8 | Gemma 4 12B (Spark llama-server Q4_K_M) | 8.50 | $0.0003 | 86 |  |
| 9 | Qwen 3.7 Flash | 8.49 | $0.0002 | 163 |  |
| 10 | Tencent Hy3 | 8.49 | $0.0008 | 143 |  |
| 11 | Fugu Max | 8.49 | $0.0096 | 143 |  |
| 12 | Claude Opus 4.8 | 8.48 | $0.0390 | 165 |  |
| 13 | Claude Opus 4.6 | 8.48 | $0.0390 | 213 |  |
| 14 | DeepSeek R1 (reasoning) | 8.45 | $0.0040 | 158 |  |
| 15 | DeepSeek V4.1 Flash | 8.44 | $0.0009 | 143 |  |
| 16 | Seed 2.0 Code | 8.44 | $0.0047 | 1570 |  |
| 17 | Inkling Small | 8.43 | $0.0019 | 143 |  |
| 18 | MiMo V2.6 Flash | 8.42 | $0.0005 | 143 |  |
| 19 | Claude Fable 5 | 8.39 | $0.0780 | 213 |  |
| 20 | Granite 4.2 8B | 8.34 | $0.0004 | 143 |  |
| 21 | Ling 3.0 Flash VL | 8.33 | $0.0001 | 143 |  |
| 22 | Claude Sonnet 5 | 8.31 | $0.0156 | 296 |  |
| 23 | Gemini 3.6 Flash | 8.30 | $0.0059 | 234 |  |
| 24 | Gemini 3.7 Flash | 8.30 | $0.0059 | 506 |  |
| 25 | Kimi K2.6 | 8.30 | $0.0063 | 219 |  |
| 26 | Muse Spark 1.3 | 8.29 | $0.0068 | 143 |  |
| 27 | DeepSeek V3 | 8.29 | $0.0007 | 154 |  |
| 28 | GPT-6 Luna Pro | 8.28 | $0.0008 | 143 |  |
| 29 | Grok 4.6 | 8.27 | $0.0096 | 143 |  |
| 30 | Poolside Laguna XS 2.1 | 8.26 | $0.0002 | 143 |  |
| 31 | Mistral Large 3 675B | 8.26 | $0.0024 | 152 |  |
| 32 | Hermes 4 405B | 8.26 | $0.0048 | 478 |  |
| 33 | Seed 2.1 Turbo | 8.25 | $0.0039 | 1244 |  |
| 34 | Mercury 2.5 | 8.24 | $0.0002 | 143 |  |
| 35 | Gemini 3.5 Flash Lite | 8.23 | $0.0038 | 143 |  |
| 36 | Muse Glimmer 30B | 8.23 | $0.0024 | 143 |  |
| 37 | Claude Haiku 4.5 | 8.21 | $0.0078 | 157 |  |
| 38 | MiniMax M3 | 8.17 | $0.0019 | 230 |  |
| 39 | DeepSeek V4 Flash (OpenRouter) | 8.16 | $0.0003 | 168 |  |
| 40 | Kimi K2.5 | 8.14 | $0.0035 | 14119 |  |
| 41 | DiffusionGemma 26B-A4B (DGX Spark Q8_0) | 8.14 | $0.0005 | 91 |  |
| 42 | KAT Coder Air v2.5 | 8.13 | $0.0009 | 497 |  |
| 43 | Nex-N2-Mini | 8.13 | $0.0002 | 143 |  |
| 44 | Ministral 14B | 8.11 | $0.0004 | 161 |  |
| 45 | GPT-OSS 120B | 8.11 | $0.0003 | 154 |  |
| 46 | Gemini 3.1 Flash Lite | 8.09 | $0.0023 | 163 |  |
| 47 | MiniMax M2.5 | 8.08 | $0.0017 | 152 |  |
| 48 | DeepSeek V4 Flash 0731 | 8.05 | $0.0002 | 143 |  |
| 49 | Solar Pro 4 | 8.04 | $0.0006 | 143 |  |
| 50 | Llama 3.3 70B | 8.04 | $0.0005 | 160 |  |
| 51 | Mistral Small 4 | 8.03 | $0.0009 | 150 |  |
| 52 | Step 3.5 Flash | 8.03 | $0.0005 | 1140 |  |
| 53 | Nemotron Nano 9B v2 | 8.02 | $0.0003 | 134 |  |
| 54 | Claude Opus 5.5 | 7.94 | $0.0312 | 143 |  |
| 55 | GPT-OSS 20B | 7.91 | $0.0002 | 150 |  |
| 56 | Llama 4 Scout 17B | 7.88 | $0.0005 | 148 |  |
| 57 | Claude Haiku 5.5 | 7.85 | $0.0008 | 143 |  |
| 58 | Gemini 2.5 Flash Lite | 7.84 | $0.0006 | 153 |  |
| 59 | Hermes 4 70B | 7.78 | $0.0006 | 487 |  |
| 60 | Grok 4.3 | 7.77 | $0.0041 | 167 |  |
| 61 | Llama 3.1 8B Instant | 7.26 | $0.0001 | 155 |  |
| 62 | Mistral Nemo | 7.26 | $0.0000 | 522 |  |

### Jubilados (165)

#### Retired (16)

| Modelo | Runs | Nota |
|--------|------|------|
| Devstral 2 (Dic 2025) | 136 |  |
| Devstral Medium | 83 |  |
| Devstral Small | 34 |  |
| Grok 4.1 Fast | 86 |  |
| Llama 3.1 8B Instant (Groq) | 84 |  |
| Llama 3.3 70B (Groq) | 84 |  |
| MiMo V2-Omni (Xiaomi direct) | 74 | Mismo modelo que via OpenRouter — comparar provide |
| MiMo V2-Pro (Xiaomi direct) | 79 | Mismo modelo que via OpenRouter — comparar provide |
| MiMo-V2-Flash | 31 |  |
| MiMo-V2-Omni (multimodal) | 80 |  |
| MiMo-V2-Pro | 79 | API-only Xiaomi (NO confundir con MiMo V2 Flash qu |
| Nemotron Super 49B v1.5 | 128 |  |
| Phi-4 14B (local) | 0 |  |
| Qwen 3.5 (Ollama Cloud default) | 52 |  |
| Seed-OSS 36B Instruct | 0 | Reasoning + math + coding + agentic. 131K context. |
| Step3 (StepFun) | 0 | MoE 321B/38B activos, multimodal reasoning. 65K co |

#### Provider Variants (54)

| Modelo | Runs | Nota |
|--------|------|------|
| Claude Fable 5 (suscripción) | 102 | Fable 5 medido por la suscripción Claude Code (no  |
| Claude Haiku 4.5 (suscripción) | 86 | Haiku 4.5 vía suscripción Claude Code. |
| Claude Opus 4.7 (suscripción) | 70 | Opus 4.7 vía suscripción Claude Code. |
| Claude Opus 4.8 (suscripción) | 109 | Opus 4.8 medido por la suscripción Claude Code (no |
| Claude Opus 5 (suscripción) | 113 | Opus 5 vía suscripción Claude Code, costo marginal |
| Claude Sonnet 4.6 (suscripción) | 93 | Sonnet 4.6 vía suscripción Claude Code. |
| Claude Sonnet 5 (suscripción) | 123 | Sonnet 5 vía suscripción Claude Code, costo margin |
| DeepSeek V3 (local) | 0 |  |
| DeepSeek V4 Flash (NIM) | 81 | Mismo modelo que probamos via OpenRouter — compara |
| DeepSeek V4 Flash (Ollama Cloud) | 0 | Variante mas chica de V4. Comparar con V4 Flash NI |
| DeepSeek V4 Pro (NIM) | 2 | Re-test del flagship via NIM (vs OpenRouter que di |
| DeepSeek V4 Pro (Ollama Cloud) | 0 | Recien agregado a Ollama Cloud (abril 28). Smoke t |
| Devstral 2 123B (NIM) | 64 | Mismo modelo que probamos via OpenRouter - compara |
| GLM 5 (NIM) | 84 | Z.AI flagship base, comparar con 5.1 |
| GLM 5.1 (NIM) | 97 | Z.AI agentic, no tenemos. Variante GLM 5 con mejor |
| GPT-5.5 Pro | 0 | Sólo /v1/responses (no chat/completions) |
| GPT-OSS 120B (Groq) | 0 |  |
| GPT-OSS 120B (Ollama Cloud) | 84 |  |
| GPT-OSS 20B (Groq) | 91 |  |
| Gemma 4 31B (DGX Spark Q4_K_M) | 84 | Q4_K_M en DGX Spark via Ollama. Comparar con Gemma |
| Gemma 4 31B (NIM) | 92 | Mismo modelo que via OpenRouter (10 runs parciales |
| Gemma 4 31B (Spark llama-server Q4_K_M) | 86 | Q4_K_M en DGX Spark via llama.cpp/llama-server (mu |
| Gemma 4 31B (Spark llama-server, reasoning) | 0 | Mismo build que spark-gemma4-31b-llamacpp pero CON |
| Gemma 4 31B (local) | 0 |  |
| Kimi K2 Thinking (NIM) | 80 | Variante thinking de K2 — comparar con K2.6 thinki |
| Kimi K2.5 (NIM) | 553 | Version nueva 2026, no tenemos K2.5 antes. Compara |
| Llama 3.3 70B (local) | 0 |  |
| Llama 4 Maverick (local) | 0 |  |
| Llama 4 Scout 17B (Groq preview) | 97 |  |
| MiMo V2.5 (Xiaomi) | 79 | All-in-one multimodal nativo, 1M context, lanzado  |
| MiMo V2.5-Pro (Xiaomi) | 80 | Flagship reasoning, agentic, 1M context, lanzado 2 |
| MiniMax M2.5 (local, open-source) | 0 |  |
| MiniMax M2.7 (directo) | 271 | API directa MiniMax. Disponible también en sub Age |
| MiniMax M2.7 Highspeed | 0 | Acceso vía sub Agent Pro $19/mes. Misma calidad qu |
| MiniMax M3 (directo / sub) | 89 | M3 vía API directa de MiniMax (token plan del usua |
| Ministral 14B (NIM) | 85 | Mistral chico nuevo dic 2025 - comparar con Mistra |
| Mistral Large 3 675B (NIM) | 82 | Flagship Mistral diciembre 2025. Comparar contra M |
| Mistral Magistral Small (NIM) | 4 | Mistral con razonamiento, tamano medio |
| Mistral Nemo 12B (local) | 0 |  |
| Mistral-Nemotron (NIM) | 8 | Colaboración Mistral × NVIDIA, optimizado en Nemo |
| Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM) | 86 | Lanzado 20 abril 2026. MoE 30B totales / 3B activo |
| Nemotron 3 Super 120B (DGX Spark Q4_K_M) | 84 | Q4_K_M en DGX Spark. Modelo gigante, primer test p |
| Nemotron 3.5 Lightning (NIM) | 14 | Única ruta con tool calling. Mide lo que OpenRoute |
| Nemotron Nano 9B v2 (NIM) | 86 | Variante chica de Nemotron 3, comparar con Nano 30 |
| Nemotron Super 49B v1.5 (NIM) | 92 | Versión iterada del Nemotron Super 120B que ya med |
| Qwen 2.5 72B (DGX Spark) | 0 | Generación previa instalada en el Spark — baseline |
| Qwen 3-Next 80B Instruct (NIM) | 95 | Próxima generación Qwen — pendiente desde Lote 4 |
| Qwen 3-Next 80B Thinking (NIM) | 184 | Variante thinking — comparar con Qwen 3-Next Instr |
| Qwen 3.5 35B (DGX Spark) | 0 | Tag real instalado en DGX Spark. Comparar vs Qwen  |
| Qwen 3.5 397B (NIM) | 94 | Mismo modelo que Cristian usa via Ollama Cloud par |
| Qwen 3.5 397B (Ollama Cloud) | 56 |  |
| Qwen 3.6 27B base (DGX Spark) | 4 | Qwen 3.6 BASE (Apache 2.0, pesos en HF) — cierra e |
| Qwen3-Coder-Next (DGX Spark Q4_K_M) | 0 | Coding-especializado next-gen. Corre gratis local  |
| Step 3.5 Flash (NIM) | 68 | Step 3.5 Flash - reemplazo de Step3 que fallo 91/9 |

#### Sin Runs (26)

| Modelo | Runs | Nota |
|--------|------|------|
| Claude Haiku 4.5 (thinking) | 0 | Misma versión con extended thinking forzado. |
| Claude Opus 4.7 (thinking) | 0 | Mismo modelo que claude-opus-4.7 con extended thin |
| Claude Sonnet 4 | 0 |  |
| Claude Sonnet 4.6 (thinking) | 0 | Mismo modelo que claude-sonnet-4.6 con extended th |
| DeepSeek R1 (free) | 0 |  |
| Devstral Small 2 24B (DGX Spark Q4_K_M) | 0 | Nueva generación pequeña de Mistral (24B). Verific |
| GPT-4o | 0 |  |
| GPT-4o High | 0 |  |
| Gemini 2.5 Flash (thinking) | 0 | Misma versión que gemini-flash con thinking forzad |
| Gemini 3.1 Flash Lite (thinking) | 0 | Misma versión con thinking forzado. |
| Gemini 3.1 Pro (thinking) | 0 | Misma versión con thinking forzado (effort=high).  |
| Gemma 4 26B MoE (local, solo 3.8B activos) | 0 |  |
| Grok 4.20 Multi-Agent | 0 | Variante multi-agente (Heavy) de Grok 4.20, contex |
| Hermes 4 405B (thinking) | 0 | Misma versión que hermes-4-405b pero con reasoning |
| Hermes 4 70B (thinking) | 0 | Misma versión que hermes-4-70b pero con reasoning  |
| Kimi K2.5 (thinking) | 0 | Misma versión que kimi-k2.5 pero con reasoning for |
| Kimi K2.6 (thinking) | 0 | Misma versión que kimi-k2.6 con thinking forzado v |
| LFM2 24B A2B | 0 | MoE de Liquid AI: 24B totales, ~2B activos por tok |
| Llama 3.3 70B (free) | 0 |  |
| MiMo-V2-Flash (free) | 0 |  |
| Nemotron 3 Nano Omni 30B-A3B Reasoning (DGX Spark Q4_K_M) | 0 | MoE 30B totales / 3B activos (A3B), thinking + mul |
| North Mini Code | 0 | Modelo de Cohere enfocado en coding via OpenRouter |
| Qwen 3.5 Plus | 0 | Plus = API-only propietario de Alibaba |
| Qwen 3.6 35B base (DGX Spark) | 0 | Qwen 3.6 BASE 35B (MoE a3b) abierto. Corre gratis  |
| Qwen 3.6 Plus (free) | 0 |  |
| Qwen3 Coder 480B (free) | 0 |  |

#### Dominados Jubilados (69)

Los 31 más claramente dominados:

| # | Modelo | Quality | Costo | Dominado por | Q Dom. | Costo Dom. |
|---|--------|---------|-------|--------------|--------|------------|
| 1 | Qwen 3.8 2.4T (A95B) | 8.41 | $0.0096 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 2 | Qwen 3.8 Max | 8.43 | $0.0096 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 3 | Qwen 3.8 Max 0902 | 8.46 | $0.0096 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 4 | Qwen 3.6 Max | 8.46 | $0.0096 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 5 | Qwen 3.7 Max | 8.24 | $0.0071 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 6 | Qwen 3.5 397B | 7.80 | $0.0054 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 7 | Kimi K2 Thinking | 5.00 | $0.0039 | Kimi K2.5 | 8.14 | $0.0035 |
| 8 | GPT-5.5 | 8.15 | $0.0465 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 9 | Qwen 3.6 27B base (OpenRouter FP8) | 7.74 | $0.0031 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 10 | Qwen 3-Next 80B Thinking | 7.52 | $0.0018 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 11 | Qwen 3.6 Plus | 8.20 | $0.0030 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 12 | Qwen3 Coder | 7.78 | $0.0016 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 13 | GPT-5.4 | 8.39 | $0.0240 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 14 | Qwen 3.5 35B | 8.07 | $0.0020 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 15 | Qwen 3.6 35B base (OpenRouter FP8) | 7.82 | $0.0014 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 16 | Qwen 3-Next 80B Instruct | 8.01 | $0.0017 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 17 | Qwen3-Coder-Next (OpenRouter FP8) | 7.81 | $0.0012 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 18 | Gemini 3.1 Pro | 7.48 | $0.0186 | Gemini 3.5 Flash Lite | 8.23 | $0.0038 |
| 19 | Nemotron 3 Ultra 550B | 8.01 | $0.0038 | Nemotron Nano 9B v2 | 8.02 | $0.0003 |
| 20 | GPT-5.6 Terra | 8.31 | $0.0186 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 21 | GPT-5.6 Terra Pro | 8.40 | $0.0186 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 22 | Gemini 3.5 Flash | 7.51 | $0.0140 | Gemini 3.5 Flash Lite | 8.23 | $0.0038 |
| 23 | GPT-5.6 Sol | 8.28 | $0.0156 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 24 | GPT-4.1 | 8.15 | $0.0126 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 25 | Gemini 2.5 Pro | 7.68 | $0.0154 | Gemini 3.5 Flash Lite | 8.23 | $0.0038 |
| 26 | KAT Coder Pro v2.5 | 7.83 | $0.0047 | KAT Coder Air v2.5 | 8.13 | $0.0009 |
| 27 | DeepSeek V4 Pro | 8.22 | $0.0053 | DeepSeek V4.1 Flash | 8.44 | $0.0009 |
| 28 | GLM-5.1 | 8.36 | $0.0048 | GLM 5.3 Flash | 8.51 | $0.0008 |
| 29 | GPT-4.1 Mini | 7.91 | $0.0025 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 30 | Mistral Large | 7.99 | $0.0096 | Mistral Large 3 675B | 8.26 | $0.0024 |
| 31 | GLM 5.2 | 8.36 | $0.0034 | GLM 5.3 Flash | 8.51 | $0.0008 |
| 32 | Tencent Hy4 preview | 8.39 | $0.0040 | Tencent Hy3 | 8.49 | $0.0008 |
| 33 | Kimi K3 | 8.06 | $0.0207 | Kimi K2.6 | 8.30 | $0.0063 |
| 34 | Qwen 3.8 27B | 8.50 | $0.0039 | Qwen 3.8 Omni Flash | 8.55 | $0.0008 |
| 35 | Qwen 2.5 72B | 8.27 | $0.0007 | Qwen 3.7 Flash | 8.49 | $0.0002 |
| 36 | MiMo-V2.5 Pro | 8.17 | $0.0014 | MiMo V2.6 Flash | 8.42 | $0.0005 |
| 37 | Claude Sonnet 5.5 | 7.87 | $0.0156 | Claude Sonnet 5 | 8.31 | $0.0156 |
| 38 | Poolside Laguna S 2.1 | 7.89 | $0.0003 | Poolside Laguna XS 2.1 | 8.26 | $0.0002 |
| 39 | DeepSeek V3.2 | 8.11 | $0.0016 | DeepSeek V4.1 Flash | 8.44 | $0.0009 |
| 40 | GPT-5.4 Mini | 8.17 | $0.0024 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 41 | GLM 5 | 8.42 | $0.0031 | GLM 5.3 Flash | 8.51 | $0.0008 |
| 42 | Claude Fable 5.1 | 8.03 | $0.0780 | Claude Fable 5 | 8.39 | $0.0780 |
| 43 | Ling 3.0 Flash | 7.98 | $0.0001 | Ling 3.0 Flash VL | 8.33 | $0.0001 |
| 44 | Claude Opus 5 Fast | 8.23 | $0.0780 | Claude Opus 4.8 | 8.48 | $0.0390 |
| 45 | MiniMax M2.7 | 7.83 | $0.0019 | MiniMax M3 | 8.17 | $0.0019 |
| 46 | Nemotron 3 Nano 30B | 7.69 | $0.0003 | Nemotron Nano 9B v2 | 8.02 | $0.0003 |
| 47 | Nemotron 3 Base 33B (DGX Spark Q4_K_M) | 7.82 | $0.0007 | Nemotron Nano 9B v2 | 8.02 | $0.0003 |
| 48 | MiMo-V2.5 (omnimodal) | 8.10 | $0.0005 | MiMo V2.6 Flash | 8.42 | $0.0005 |
| 49 | Gemma 4 12B (Spark llama-server, reasoning) | 8.19 | $0.0003 | Gemma 4 12B (Spark llama-server Q4_K_M) | 8.50 | $0.0003 |
| 50 | Nemotron 3.5 Lightning | 7.74 | $0.0003 | Nemotron Nano 9B v2 | 8.02 | $0.0003 |
| 51 | Claude Opus 5 | 8.21 | $0.0390 | Claude Opus 4.8 | 8.48 | $0.0390 |
| 52 | Claude Sonnet 4.6 | 8.12 | $0.0234 | Claude Sonnet 5 | 8.31 | $0.0156 |
| 53 | Gemma 4 26B MoE (3.8B activos) | 8.34 | $0.0005 | Gemma 4 12B (Spark llama-server Q4_K_M) | 8.50 | $0.0003 |
| 54 | Nemotron 3 Super | 7.91 | $0.0006 | Nemotron Nano 9B v2 | 8.02 | $0.0003 |
| 55 | Llama 4 Maverick | 7.95 | $0.0011 | Llama 3.3 70B | 8.04 | $0.0005 |
| 56 | Gemini 2.5 Flash | 8.08 | $0.0038 | Gemini 3.5 Flash Lite | 8.23 | $0.0038 |
| 57 | Grok 4.5 | 8.12 | $0.0096 | Grok 4.6 | 8.27 | $0.0096 |
| 58 | Kimi K2.7 Code | 8.06 | $0.0055 | Kimi K2.5 | 8.14 | $0.0035 |
| 59 | Nemotron 3 Nano Omni 30B-A3B Reasoning | 7.99 | $0.0006 | Nemotron Nano 9B v2 | 8.02 | $0.0003 |
| 60 | Gemma 4 31B | 8.48 | $0.0005 | Gemma 4 12B (Spark llama-server Q4_K_M) | 8.50 | $0.0003 |
| 61 | Claude Opus 4.7 | 8.39 | $0.0390 | Claude Opus 4.8 | 8.48 | $0.0390 |
| 62 | Grok 4.20 | 7.70 | $0.0041 | Grok 4.3 | 7.77 | $0.0041 |
| 63 | Gemini 3.8 Flash | 8.26 | $0.0059 | Gemini 3.6 Flash | 8.30 | $0.0059 |
| 64 | Kimi K2 | 8.11 | $0.0036 | Kimi K2.5 | 8.14 | $0.0035 |
| 65 | Qwen 3.8 Flash | 8.53 | $0.0008 | Qwen 3.8 Omni Flash | 8.55 | $0.0008 |
| 66 | GPT-5.6 Luna Pro | 8.50 | $0.0019 | GPT-5.6 Luna | 8.52 | $0.0019 |
| 67 | DeepSeek V4 Pro (0813) | 8.45 | $0.0047 | DeepSeek R1 (reasoning) | 8.45 | $0.0040 |
| 68 | GPT-6 Luna | 8.27 | $0.0008 | GPT-6 Luna Pro | 8.28 | $0.0008 |
| 69 | Muse Spark 1.2 | 8.28 | $0.0068 | Muse Spark 1.3 | 8.29 | $0.0068 |
