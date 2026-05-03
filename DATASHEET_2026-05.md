---
title: "Datasheet mayo 2026 — comparación vs abril"
mes: "2026-05"
fecha_snapshot: "2026-05-03"
version_benchmark: "v2.6.0"
audiencia: "Lectores que quieren ver evolución mes a mes y los hallazgos nuevos"
---

# 📊 Datasheet mayo 2026 — qué cambió vs abril

> 📍 **Disclaimer**: este benchmark NO sustituye a los benchmarks académicos validados. Es un complemento para emprendedores hispanohablantes. Ver [README.md](README.md) y [DATASHEET_2026-04.md](DATASHEET_2026-04.md) para snapshot anterior.

## Cobertura mayo vs abril

| Métrica | Abril (v2.5.2) | Mayo (v2.6.0) | Δ |
|---|---|---|---|
| Modelos catalogados | 113 | **113** | = |
| Modelos con cobertura ≥50 runs single-turn | 70 | **72** | **+2** |
| Modelos con runs en agent_long_horizon | 38 | **49** | **+11** |
| Modelos con runs en NIAH-ES (cualquier suite) | 8 | **21** | **+13** ⬆ |
| Total runs preservados | 8,475 | **~9,500+** | +1,000+ |

## Lotes corridos en mayo

| Lote | Tests | Resultado |
|---|---|---|
| **GPT-5.5 completar** (3 mayo) | 12 agent_long_horizon + 45 niah_es_lite | ✅ 57/57 OK |
| **NIAH-ES extension lite** (3 mayo) | 9 modelos × 45 tests | ✅ 405/405 OK |
| **DeepSeek V4 family completar** (3 mayo) | 3 variantes × 57 tests | V4 Pro Cloud 55/57 ✅, V4 Flash Cloud 57/57 ✅, V4 Pro NIM 0/7 ❌ (cascada 504) |
| **DeepSeek V4 Pro OpenRouter** (3 mayo) | 12 agent_long_horizon + 45 niah_es_lite | ✅ 57/57 OK |

## Hallazgos nuevos de mayo (no en abril)

### 1. GPT-5.5 validación cruzada

GPT-5.5 ya tenía 91/91 single-turn al cierre de abril (score 6.32, regresión vs GPT-5.4 7.23). Mayo agregó cobertura completa con multi-turn + NIAH:

| Suite | Score GPT-5.5 |
|---|---|
| Single-turn (91 tests, abril) | 6.32 |
| agent_long_horizon (12 tests, mayo) | _TBD post-export_ |
| niah_es_lite (45 tests, mayo) | _TBD post-export_ |

**Hipótesis a validar**: si GPT-5.5 mejora en multi-turn agéntico, refuta el patrón "thinking empeora multi-turn" para OpenAI específicamente. Si baja, valida.

### 2. Devstral 2 (Dec 2025) entra al ranking NIAH-ES

Devstral 2 corrió NIAH-ES v2 + extension lite. Resultados a confirmar tras export final.

### 3. MiMo V2.5 Xiaomi sub se confirma como mejor C/B en español

MiMo V2.5 (sub $14/mes) entra al top 10 score compuesto + top 10 NIAH-ES. Para emprendedores con presupuesto, mejor opción de su rango.

### 4. DeepSeek V4 family — comparación 3 providers

| Variante | Cobertura | Score | Notas |
|---|---|---|---|
| **DeepSeek V4 Pro (OpenRouter pagado)** | 91 single + 57 nuevos | TBD | ~$1.74/$3.48 per M tokens |
| **DeepSeek V4 Pro (Ollama Cloud sub $30/mes)** | 55/57 (97%) | TBD | Más estable que NIM |
| **DeepSeek V4 Pro (NIM gratis)** | 0/7 (cascada 504) | ❌ | Descartado para producción |
| **DeepSeek V4 Flash (Ollama Cloud)** | 57/57 ✅ | TBD | Excelente alternativa C/B |

**Hallazgo robusto del mes**: DeepSeek V4 Pro vía NIM **NO funciona en producción** con prompts largos — gateway timeouts cascada. **Confirmado dos veces** (abril 28 y mayo 3). Para usar V4 Pro: usar OpenRouter pagado o Ollama Cloud sub.

### 5. NIAH-ES extension — 17 modelos cubiertos (vs 8 en abril)

Top 5 NIAH-ES con 17 modelos:

| # | Modelo | Score | Detalle |
|---|---|---|---|
| 1 | Devstral Small | 7.25 | Lidera (mantiene desde abril v2) |
| 2 | Mistral Small 4 | 7.06 | |
| 3 | Llama 4 Scout 17B (Groq) | 6.89 | |
| ... | (9 modelos más agregados en mayo) | TBD | |

## Top 10 score compuesto mayo

| # | Modelo | Final | Quality | Cost | Notas |
|---|---|---|---|---|---|
| 1 | Llama 4 Scout 17B (Groq preview) | 7.69 | 7.7 | — | (era 8.11 en abril, baja por NIAH agregado) |
| 2 | Llama 3.1 8B Instant (Groq) | 7.67 | 7.33 | — | |
| 3 | Devstral Small | 7.52 | **7.89** | — | sube de #10 a #3 |
| 4 | Mistral Small 4 | 7.51 | 7.88 | — | |
| 5 | GPT-OSS 20B (Groq) | 7.47 | 7.10 | — | |
| 6 | MiMo V2-Omni Xiaomi direct | 7.46 | 7.27 | — | |
| 7 | MiMo V2.5 (Xiaomi sub) | 7.45 | 7.63 | — | |
| 8 | Gemini 3.1 Flash Lite | 7.44 | 7.82 | — | |
| 9 | Nemotron 3 Nano 30B | 7.43 | 7.79 | — | |
| 10 | MiMo V2.5-Pro (Xiaomi sub) | 7.42 | 7.65 | — | |

⚠️ **Cambio metodológico importante**: mayo integra NIAH-ES al score compuesto. Modelos con NIAH-ES corrido tienen score promedio ligeramente menor (NIAH suele ser 5-7 vs single-turn 7-8). **Esto NO significa que los modelos empeoraron** — significa que el ranking ahora incluye una dimensión adicional (long-context retrieval).

## Cambios en ranking (mayo vs abril)

| Modelo | Abril | Mayo | Δ | Causa |
|---|---|---|---|---|
| Devstral Small | #10 (7.61) | **#3** (7.52) | ⬆ +7 posiciones | NIAH-ES alto (7.25) lo sube relativamente |
| Llama 4 Scout 17B | #1 (8.11) | #1 (7.69) | = | Sigue líder pero con score absoluto menor |
| MiMo V2-Omni Xiaomi | #11 | **#6** | ⬆ +5 | Xiaomi sub multimodal mejora con NIAH |
| GPT-OSS 120B Cloud | #7 (7.69) | #13 (7.37) | ⬇ -6 | NIAH-ES baja su agéntica histórica |
| Grok 4.1 Fast | #8 | #~16 | ⬇ | NIAH-ES no le va bien |

## Limitaciones documentadas en mayo

- DeepSeek V4 Pro NIM continúa con timeouts/504 cascada — descartado para producción (segundo mes con el problema).
- NIAH-ES no incluye contexto 256K para modelos donde el provider lo cap. Solo evalúa lo que el provider expone (effective context).
- 1M context aún solo cubierto en GPT-4.1 (3 de 4 providers cap el context). Pendiente probar Gemini Pro vía Google directo.

## Pendientes para junio 2026

- Suite `agentic_debugging` — bugs reales con stubs detallados (5-10 tests)
- v3b NIAH 1M con Gemini Pro vía Google directo + DeepSeek V4 Pro Ollama Cloud
- Inspección cualitativa Opus 4.7 (paráfrasis vs extracción exacta)
- Cobertura completa NIAH-ES en los 70 modelos con ≥50 runs (faltan ~50)
- Datasheet junio 2026 (1 junio)

## Versión del benchmark al cierre

**v2.6.0** (3 mayo 2026): GPT-5.5 completo + NIAH-ES extension (17 modelos) + DeepSeek V4 family con 3 providers + datasheet mensual establecido.
