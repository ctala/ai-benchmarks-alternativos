---
title: "Datasheet junio 2026 — v3.0.1: DiffusionGemma, unificación de scores y pesos v3.0"
mes: "2026-06"
fecha_snapshot: "2026-06-26"
version_benchmark: "v3.0.1"
audiencia: "Lectores que quieren ver evolución mes a mes y los hallazgos nuevos"
---

# 📊 Datasheet junio 2026 — qué cambió vs mayo

> 📍 **Disclaimer**: este benchmark NO sustituye a los benchmarks académicos validados (HumanEval, MMLU, SWE-bench, NIAH inglés). Es un complemento para emprendedores hispanohablantes que deciden qué modelo poner en producción HOY. Ver [README.md](README.md) y [DATASHEET_2026-05.md](DATASHEET_2026-05.md) para el snapshot anterior.

## TL;DR de junio

Junio consolidó tres cambios grandes:

1. **Unificación de scores**: `MODELOS.md` y la calculadora web ahora usan el mismo `score_global` z-scoreado.
2. **Pesos v3.0**: Quality 70% · Costo 15% · Speed/Latency 7.5%. El tool_calling sale del compuesto y se muestra como badge.
3. **DiffusionGemma medido**: primera difusión textual del benchmark, corriendo local en el DGX Spark. Score global 7.05, posición #25/91, empata con Gemma 4 31B local.

## Cobertura mayo vs junio

| Métrica | Mayo (v2.7) | Junio (v3.0.1) | Δ |
|---|---|---|---|
| Modelos catalogados | 113 | **143** | **+30** |
| Modelos con cobertura ≥50 runs | 72 | **91** | **+19** |
| Total runs | ~9,390 | **10,508** | **+1,118** |
| Score compuesto | v2.7 (costo 20%) | **v3.0 (quality 70%, costo 15%)** | z-score |

## Modelos nuevos medidos en junio

| Modelo | Tipo | Hallazgo |
|---|---|---|
| **Kimi K2.7 Code** | OpenRouter | Coding sólido, score 5.07 (v3.0). Thinking model lento. |
| **Claude Fable 5** | Suscripción/API | Quality 8.58 vs Opus 4.8 8.81. Gana en `agent_long_horizon`, pierde en tareas cortas de formato. |
| **MiniMax M3** | Directo/sub/OR | Contexto usable real 512K (directo) / 256K (OR), no 1M. |
| **DeepSeek V4 Flash** | OpenRouter | #9 general, quality 8.34, barato. |
| **Qwen 3.6 base/Plus/Max** | Open/propietario | Familia completa. Max en #8. |
| **Qwen3-Coder-Next** | OpenRouter FP8 | #3 general, coding top. |
| **DeepSeek R1** | Reasoning | Menos práctico que V4 Flash (thinking ≠ mejor en estas tareas). |
| **Claude Opus 4.8** | Flagship | Quality top (8.4), rey de seguridad (8.79), pero costo lo deja atrás en ranking compuesto. |
| **Gemini 3.5 Flash** | Flagship | Long-context usable = 800K, igual que 2.5 Flash Lite. |
| **DiffusionGemma 26B-A4B** | Local Spark | **Primera difusión textual**. Score 7.05, #25/91. Empata con Gemma 4 31B local. |
| **GLM 5.2** | Z.ai | Sucesor de GLM 5.1. Score 6.93, #26/92. Rápido (51.8 tok/s) pero no supera a DiffusionGemma ni a Gemma 4. |

## 🌟 El hallazgo del mes: DiffusionGemma funciona

Medimos **DiffusionGemma 26B-A4B** (Google, modelo de difusión textual, 26B total / 3.8B activos) en el DGX Spark con llama.cpp PR #24423, Q8_0, 103 tests y juez Phi-4.

**Resultado**: score global **7.05**, posición **#25/91**. Eso lo ubica al nivel de **Gemma 4 31B local** (#23-#24) y por encima de **Claude Fable 5** (#26).

| Pilar | DiffusionGemma | Gemma 4 31B (NIM) |
|---|---:|---:|
| Coding | 7.02 | 7.42 |
| Contenido | 7.68 | 7.81 |
| Agentes/Operaciones | **7.76** | 7.10 |
| Razonamiento | 7.67 | **7.85** |

**Fortalezas**: agentes, soporte, orquestación, políticas, y costo $0 local.
**Debilidades**: precisión de strings (5.26), coding puro por debajo de Gemma 4, latencia ~39 tok/s.

> **Conclusión**: la difusión textual ya es una alternativa real para producción local. No supera a los top cloud, pero entrega calidad #25 mundial sin costo por token y con privacidad de datos.

## 🏆 Ranking general v3.0.1

| # | Modelo | Score | Nota |
|---|---|---:|---|
| 1 | DeepSeek V4 Flash (OpenRouter) | 8.29 | Mejor balance calidad/costo/velocidad |
| 2 | DeepSeek R1 (reasoning) | 8.25 | Reasoning, pero costoso y lento |
| 3 | Qwen3-Coder-Next (OpenRouter FP8) | 8.09 | Coding top |
| 4 | Claude Opus 4.8 (suscripción) | 8.08 | Quality máxima, costo alto |
| 5 | Claude Haiku 4.5 (suscripción) | 7.97 | Eficiencia Anthropic |
| 6 | Devstral Small | 7.96 | Top open-source Apache |
| 7 | Claude Sonnet 4.6 (suscripción) | 7.89 | Flagship accesible |
| 8 | Qwen 3.6 Max | 7.81 | Premium chino |
| 9 | MiniMax M3 (directo / sub) | 7.80 | Caso activo de Cristian |
| 10 | Llama 4 Scout 17B (Groq) | 7.77 | Velocidad + open weights |
| 25 | **DiffusionGemma 26B-A4B (Spark Q8_0)** | **7.05** | **Local, $0, difusión textual** |

## ⚙️ Infraestructura

- **DGX Spark** como host del juez Phi-4 vLLM FP16 y ahora también como runner local para DiffusionGemma.
- **llama.cpp PR #24423** habilita DiffusionGemma mediante `llama-diffusion-cli`.
- Pipeline de regeneración centralizado en `benchmarks/regenerate_all.py`.

## Caveats honestos de junio

- DiffusionGemma fue medido con **ctx-size 8K** en la primera corrida; 7 errores en `agent_long_horizon` se atribuyen a eso. La config ya fue ajustada a **262K**.
- La suite `string_precision` expone un límite real de la difusión: no copia exactamente credenciales/configs.
- NIAH-es y seguridad siguen con cobertura parcial (~17 modelos).

## Qué sigue (julio)

- Re-correr `agent_long_horizon` de DiffusionGemma con 262K de contexto.
- Medir modelos nuevos de junio: Nemotron 3 Ultra, GLM 5.2, Qwen 3.7 Plus, Cohere North Mini Code, Poolside Laguna, Claude Opus 4.8 Fast, Grok 4.3.
- Completar long-context + seguridad en más modelos.
- Implementar adapter multi-turn con `-cnv` para DiffusionGemma si es necesario.
