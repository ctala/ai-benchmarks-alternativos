# Inventario de Modelos del Benchmark

> Snapshot de cobertura: qué modelos están probados, cuáles esperan en cola, y qué falta del mercado. Actualizado 2 de Junio 2026.

## Regla de mantenimiento

Un modelo se mide **una sola vez** salvo:
1. **Versión nueva** del proveedor (ID distinto = modelo distinto, se mide).
2. **Suites/tests nuevos** o **scoring cambiado** (afecta a todos por igual).
3. **Bug del adapter/runner** que invalida runs previos (ej. fix de `max_tokens` para thinking, abril 2026 → solo `--rerun-empty`).
4. **Cambio visible del modelo** anunciado por el proveedor (re-training silencioso, cambio radical de precio).

No se re-mide por: refactors del runner, mejoras cosméticas, regeneración de MDs.

---

## Probados

<!-- AUTO-TABLE-START -->

> Auto-generado por `benchmarks/generate_modelos_md_table.py`.

> **No existe un único 'mejor modelo'.** El score global combina calidad, costo, velocidad y latencia con pesos elegidos para emprendedores (70% calidad, 15% costo, 7.5% velocidad, 7.5% latencia) — **es un punto de partida, no un veredicto**. Un modelo puede quedar bajo en el global y ser el correcto para vos: si tu caso es batch nocturno, la latencia no te importa y el ranking la está penalizando igual. Mirá las tablas por caso de uso, y para tus propios pesos usá la [calculadora](https://benchmarks.cristiantala.com/).

> **Piso de ranking: 50 runs.** Los modelos con menos muestra van a *En evaluación* al final — su score es indicativo, no comparable.

#### Índice de calidad — qué modelo responde mejor (⭐ = en la frontera de Pareto: nadie lo supera a la vez en calidad, precio y latencia)

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `tencent/hy3` | ✅  | $0.132/0.528 | **8.65** | ⭐ | 119 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/20260812_tencent-hy3/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.59** | ⭐ | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.55** |  | 134 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260812_tools_deepseek-r1/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.54** | ⭐ | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.53** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.50** |  | 119 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/20260812_inkling-small/) |
| `openai/gpt-5.6-terra-pro` | ❌  | $1.0/6.0 | **8.49** |  | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra-pro.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **8.49** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260812_tools_glm-5.1/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.47** |  | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **8.46** |  | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **8.45** | ⭐ | 131 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/canario/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **8.43** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **8.43** |  | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.42** |  | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **8.40** |  | 149 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **8.39** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **8.39** |  | 130 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **8.38** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **8.37** |  | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **8.36** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **8.36** |  | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **8.36** |  | 195 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **8.34** | ⭐ | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.33** |  | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.30** | ⭐ | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **8.30** |  | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260812_tools_minimax-m3/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.29** | ⭐ | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **8.29** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/20260812_glimmer/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.28** | ⭐ | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | — |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.26** | ⭐ | 119 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/20260812_nex-n2-mini/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **8.25** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **8.24** |  | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **8.24** |  | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **8.21** |  | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **8.21** |  | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **8.20** |  | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **8.19** |  | 133 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **8.18** |  | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **8.17** |  | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **8.17** |  | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.16** | ⭐ | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.15** |  | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **8.15** |  | 119 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/20260812_solar-pro4/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **8.15** |  | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k3/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **8.14** |  | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k2.6/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.14** |  | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **8.13** |  | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **8.13** |  | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-120b/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **8.10** |  | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.08** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **8.07** |  | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `inclusionai/ling-3.0-flash` | ✅  | $0.021/0.063 | **8.05** | ⭐ | 119 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | — |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **8.03** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/20260812_claude-sonnet-5-sub/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **8.02** |  | 133 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260812_tools_llama-4-maverick/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **8.02** |  | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **8.01** |  | 136 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **8.01** |  | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **8.00** |  | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.99** |  | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **7.97** |  | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.96** | ⭐ | 124 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260812_tools_or-llama-4-scout/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **7.96** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.96** |  | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.95** |  | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.95** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.93** |  | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.92** |  | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.91** |  | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.90** |  | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **7.88** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.87** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.86** | ⭐ | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.82** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-20b/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **7.76** |  | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.75** |  | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **7.70** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/canario/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.59** |  | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **7.53** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/canario/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **7.51** |  | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.44** |  | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **7.36** |  | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **7.26** |  | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |

#### Mejor coding

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **9.11** | ⭐ | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | — |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.99** | ⭐ | 119 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/20260812_nex-n2-mini/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.92** | ⭐ | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | — |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **8.79** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | — |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **8.76** |  | 119 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/20260812_solar-pro4/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.70** |  | 119 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/20260812_inkling-small/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.63** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **8.59** |  | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.58** |  | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.57** |  | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.51** | ⭐ | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `tencent/hy3` | ✅  | $0.132/0.528 | **8.51** | ⭐ | 119 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/20260812_tencent-hy3/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.46** |  | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.44** | ⭐ | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **8.44** |  | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `openai/gpt-5.6-terra-pro` | ❌  | $1.0/6.0 | **8.42** |  | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra-pro.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **8.41** |  | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **8.38** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.37** | ⭐ | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **8.36** | ⭐ | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **8.34** |  | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **8.33** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-20b/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **8.30** |  | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **8.30** |  | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **8.29** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **8.27** |  | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **8.27** |  | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **8.26** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **8.26** | ⭐ | 131 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/canario/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **8.24** |  | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **8.20** |  | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-120b/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **8.18** |  | 130 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **8.17** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/20260812_claude-sonnet-5-sub/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **8.17** |  | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **8.15** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **8.09** |  | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.09** | ⭐ | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **8.09** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **8.08** |  | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **8.06** |  | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **8.05** |  | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **8.03** |  | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **8.03** |  | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **8.01** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260812_tools_glm-5.1/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.00** | ⭐ | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.98** |  | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.97** |  | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.97** |  | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.96** |  | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260812_tools_minimax-m3/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.96** |  | 133 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260812_tools_llama-4-maverick/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.95** |  | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `inclusionai/ling-3.0-flash` | ✅  | $0.021/0.063 | **7.95** | ⭐ | 119 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.94** |  | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **7.94** |  | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k2.6/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **7.91** |  | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.88** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.86** |  | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.85** |  | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.84** |  | 134 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260812_tools_deepseek-r1/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.84** |  | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **7.81** |  | 195 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **7.81** |  | 149 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.80** |  | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.78** |  | 133 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **7.77** |  | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **7.71** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.58** |  | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.49** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.43** |  | 136 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.41** |  | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **7.39** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/canario/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.39** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/20260812_glimmer/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **7.30** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.28** | ⭐ | 124 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260812_tools_or-llama-4-scout/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.15** |  | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **7.15** |  | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **7.09** |  | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.99** |  | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **6.99** |  | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.94** |  | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.85** |  | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k3/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **6.81** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/canario/) |

#### Mejor razonamiento

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.28** | ⭐ | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.25** | ⭐ | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.13** |  | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.08** | ⭐ | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **8.01** |  | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.94** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **7.92** | ⭐ | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **7.92** |  | 119 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/20260812_solar-pro4/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.88** | ⭐ | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.88** |  | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `inclusionai/ling-3.0-flash` | ✅  | $0.021/0.063 | **7.87** | ⭐ | 119 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **7.87** | ⭐ | 131 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/canario/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.84** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **7.84** |  | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.82** |  | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **7.80** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.79** |  | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **7.77** |  | 130 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.75** | ⭐ | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.72** |  | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.60** | ⭐ | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.60** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-20b/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.59** |  | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.59** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/20260812_glimmer/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.59** |  | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-120b/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.58** |  | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **7.55** |  | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k2.6/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **7.54** | ⭐ | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.53** |  | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.50** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **7.49** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **7.49** |  | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **7.45** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.45** |  | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.44** | ⭐ | 124 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260812_tools_or-llama-4-scout/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.43** |  | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.42** | ⭐ | 119 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/20260812_tencent-hy3/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.42** |  | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.41** |  | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.36** |  | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.31** |  | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **7.30** |  | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **7.29** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260812_tools_glm-5.1/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **7.28** |  | 119 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/20260812_inkling-small/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **7.27** |  | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.26** |  | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.26** |  | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.25** |  | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **7.22** | ⭐ | 119 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/20260812_nex-n2-mini/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **7.21** |  | 149 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.17** |  | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **7.16** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.12** |  | 134 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260812_tools_deepseek-r1/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.12** |  | 133 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260812_tools_llama-4-maverick/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.08** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.06** |  | 133 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.02** |  | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.02** |  | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.01** |  | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.96** |  | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **6.96** |  | 195 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **6.91** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.88** |  | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.84** |  | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260812_tools_minimax-m3/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.83** |  | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k3/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.82** |  | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.82** |  | 136 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **6.82** |  | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **6.72** |  | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `openai/gpt-5.6-terra-pro` | ❌  | $1.0/6.0 | **6.65** |  | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra-pro.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **6.61** |  | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.57** |  | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.54** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.53** |  | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **6.46** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/20260812_claude-sonnet-5-sub/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **6.34** |  | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **6.34** |  | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **6.18** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/canario/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **5.95** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **5.92** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/canario/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **5.14** |  | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **4.85** |  | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |

#### Mejor contenido/marketing

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.13** | ⭐ | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.11** | ⭐ | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | — |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.03** | ⭐ | 119 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/20260812_nex-n2-mini/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.03** | ⭐ | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.02** |  | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **7.99** | ⭐ | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.96** |  | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.95** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-20b/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **7.93** | ⭐ | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **7.91** |  | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **7.86** |  | 130 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.85** |  | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-120b/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.84** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **7.84** |  | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **7.83** |  | 119 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/20260812_solar-pro4/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **7.82** | ⭐ | 131 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/canario/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.81** |  | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.80** |  | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.75** |  | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.73** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.73** |  | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.71** |  | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **7.66** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.65** | ⭐ | 124 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260812_tools_or-llama-4-scout/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.65** |  | 136 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.64** |  | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260812_tools_minimax-m3/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **7.62** |  | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **7.62** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `inclusionai/ling-3.0-flash` | ✅  | $0.021/0.063 | **7.62** | ⭐ | 119 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.59** | ⭐ | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.57** |  | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.56** | ⭐ | 119 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/20260812_tencent-hy3/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.54** | ⭐ | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.52** |  | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.47** |  | 134 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260812_tools_deepseek-r1/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **7.47** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260812_tools_glm-5.1/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.47** |  | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.47** | ⭐ | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.43** |  | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **7.43** |  | 119 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/20260812_inkling-small/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **7.38** |  | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **7.37** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **7.36** |  | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **7.35** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.35** |  | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `openai/gpt-5.6-terra-pro` | ❌  | $1.0/6.0 | **7.28** |  | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra-pro.md) | — |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.27** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/20260812_glimmer/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.27** |  | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.25** |  | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.23** |  | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.22** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.22** |  | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.22** |  | 133 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.21** |  | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.21** |  | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.18** |  | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **7.15** |  | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.13** |  | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.09** |  | 133 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260812_tools_llama-4-maverick/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.04** |  | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **7.04** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.01** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **6.98** |  | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **6.97** |  | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **6.97** |  | 195 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.94** |  | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **6.89** |  | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.88** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.88** |  | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **6.86** |  | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k2.6/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **6.79** |  | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **6.74** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/20260812_claude-sonnet-5-sub/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **6.72** |  | 149 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.65** |  | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.57** |  | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k3/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.51** |  | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **6.44** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/canario/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.38** |  | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **6.35** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.32** |  | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.28** |  | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **6.21** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/canario/) |

#### Calidad por dólar — cuánta calidad rinde cada peso (calidad ÷ $/1k calls; premia lo barato a propósito, mirá la columna Calidad)

| Modelo | OS | $ in/out | Calidad/$ | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `inclusionai/ling-3.0-flash` | ✅  | $0.021/0.063 | **79.70** | ⭐ | 119 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **53.78** |  | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **52.28** | ⭐ | 119 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/20260812_nex-n2-mini/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **43.12** |  | 119 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/20260812_solar-pro4/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **41.86** | ⭐ | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | — |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **41.82** | ⭐ | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **35.71** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-20b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **28.93** |  | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260812_tools_or-gpt-oss-120b/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **27.79** |  | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **26.60** |  | 119 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **25.46** |  | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **24.10** |  | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **23.06** | ⭐ | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **18.05** | ⭐ | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260812_deepseek-v4-flash-0731/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **17.60** |  | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **16.58** | ⭐ | 124 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260812_tools_or-llama-4-scout/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **15.71** |  | 136 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **13.29** | ⭐ | 131 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/canario/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **12.68** |  | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **12.48** | ⭐ | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **12.32** |  | 130 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **12.13** |  | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **10.40** | ⭐ | 119 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/20260812_tencent-hy3/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **9.24** | ⭐ | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.62** |  | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.26** |  | 133 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260812_tools_llama-4-maverick/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **6.42** |  | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **5.80** |  | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **5.71** |  | 133 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.19** |  | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.16** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **5.05** |  | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **4.99** |  | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **4.82** |  | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **4.39** |  | 119 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/20260812_inkling-small/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **4.39** |  | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260812_tools_minimax-m3/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **4.21** |  | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **4.07** |  | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **3.94** |  | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **3.52** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/20260812_glimmer/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **3.51** | ⭐ | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **3.51** |  | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **3.45** | ⭐ | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **3.44** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **3.15** |  | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **2.77** |  | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **2.25** |  | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k2.6/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **2.18** |  | 195 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **2.16** |  | 134 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260812_tools_deepseek-r1/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **2.11** |  | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **2.07** |  | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260812_tools_glm-5.1/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **1.92** |  | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **1.91** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **1.76** |  | 149 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **1.72** |  | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **1.47** |  | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **1.44** |  | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **1.43** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **1.41** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **1.24** |  | 119 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **1.16** |  | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **1.06** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `openai/gpt-5.6-terra-pro` | ❌  | $1.0/6.0 | **0.91** |  | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra-pro.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **0.90** |  | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **0.88** |  | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **0.85** |  | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **0.84** |  | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **0.65** |  | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **0.53** |  | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **0.51** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/20260812_claude-sonnet-5-sub/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.50** |  | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **0.40** |  | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **0.35** |  | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **0.35** |  | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/20260812_tools_kimi-k3/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **0.35** |  | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **0.22** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **0.22** |  | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **0.21** |  | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **0.20** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/canario/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **0.18** |  | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **0.11** |  | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **0.10** |  | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/canario/) |

#### Vía suscripción Claude — plano propio (comparables entre sí)

> Medidos aprovechando la **suscripción de Claude Code** (costo marginal $0), todos por el mismo camino → **comparables entre ellos**. Ese camino arrastra ~8.8K tokens de scaffolding del CLI y **deprime la nota**: en los 2 modelos medidos por ambos caminos, la calidad por API dio **+0.15 y +0.22 más** que por suscripción. Leé estos números como **piso conservador**, no como techo — y no los compares 1:1 contra la tabla principal (la latencia por CLI es 2.5-4× peor y no es del modelo). Sirven para la pregunta de quien ya paga el plan: *¿qué modelo uso dentro de mi suscripción?*

| Modelo | Calidad (piso) | Velocidad | Runs | Per-model MD | Responses |
|---|---:|---:|---:|---|---|
| `claude-sonnet-5` | **8.86** | 55 tok/s | 119 | [per-model](benchmarks/results/per-model/claude-sonnet-5.md) | [responses](benchmarks/results/responses/20260812_claude-sonnet-5-sub/) |
| `claude-fable-5` | **8.61** | 58 tok/s | 102 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `claude-opus-5` | **8.49** | 46 tok/s | 113 | [per-model](benchmarks/results/per-model/claude-opus-5.md) | [responses](benchmarks/results/responses/canario/) |
| `claude-opus-4-8` | **8.38** | 58 tok/s | 109 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `claude-haiku-4-5` | **8.29** | 102 tok/s | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |
| `claude-sonnet-4-6` | **8.29** | 49 tok/s | 93 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `claude-opus-4-7` | **8.27** | 53 tok/s | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |

#### Variantes de proveedor (37 mediciones)

> El mismo modelo servido por otra infraestructura (Groq, NVIDIA NIM, Ollama Cloud, API directa del proveedor, self-hosted). **No compiten acá** — comparar infra contra infra es otra pregunta, y tiene su propia página: [el proveedor te cambia el modelo](https://benchmarks.cristiantala.com/mismo-modelo-distinto-proveedor/). El caso extremo medido: el mismo Qwen 3.5 397B da **7.96 en NVIDIA NIM y 5.46 en Ollama Cloud** — 2.5 puntos por la infraestructura, no por el modelo.

#### En evaluación — muestra parcial (<50 runs, NO rankeados)

> Estos modelos tienen menos runs que el piso del ranking, así que su score es **indicativo, no comparable**: con pocas muestras la varianza permite que un modelo quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** en las tablas de arriba hasta completar la cobertura.

| Modelo | OS | $ in/out | Calidad (indic.) | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `openai/gpt-5.6-luna-pro` | ❌  | $0.1/0.6 | **8.60** |  | 117 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna-pro.md) | — |
| `qwen/qwen-2.5-72b-instruct` | ✅ Apache 2.0 | $0.36/0.4 | **8.24** |  | 63 | [per-model](benchmarks/results/per-model/qwen_qwen-2_5-72b-instruct.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **8.23** |  | 152 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **7.98** |  | 106 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **7.93** |  | 131 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.03** |  | 166 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260715_082251_44555/) |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **5.00** |  | 2 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |

#### Retirados — fuera del ranking y de las recomendaciones

> **Un modelo que no puedes usar no es un candidato.** Sus números son reales y quedan acá por transparencia (alimentan el análisis histórico), pero no compiten. Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera, y Nemotron Super 49B v1.5 estaba **#8** el día que NVIDIA lo sacó de OpenRouter.

> **`Quién`** distingue lo que decidió el proveedor de lo que decidimos nosotros: Phi-4 no lo retiró nadie, es el modelo juez y no compite. **`Sigue vivo en`** avisa cuando lo que murió fue *una ruta* y no el modelo — el caso normal, no la excepción. Y el retiro **se re-verifica** (`check_endpoints.py --recheck-retired`): el 12-ago-2026 dos modelos retirados en julio habían vuelto a responder porque un proveedor los recogió, y volvieron al catálogo.

| Modelo | Retirado | Quién | Causa | Sigue vivo en | Score (histórico) | Runs |
|---|---|---|---|---|---:|---:|
| `mistralai/devstral-2512` | 2026-08-12 | proveedor | OpenRouter 404: la familia Devstral entera salió del catálogo | — | **5.35** | 136 |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | 2026-08-12 | proveedor | OpenRouter 404 'No endpoints found'; NVIDIA movió su oferta a la familia Nemotron 3 | ✅ Nemotron Super 49B v1.5 (NIM) (92 runs) | **7.05** | 128 |
| `phi4` | 2026-07-14 | decisión propia | decisión del benchmark, no del proveedor: no compite (Phi-4 es el modelo juez) | — | — | 0 |
| `qwen3.5:cloud` | 2026-07-14 | sin registrar | sin causa registrada; fecha recuperada del historial de git | — | **2.54** | 52 |
| `mimo-v2-omni` | 2026-07-14 | sin registrar | sin causa registrada; fecha recuperada del historial de git | — | **4.40** | 74 |
| `mimo-v2-pro` | 2026-07-14 | sin registrar | sin causa registrada; fecha recuperada del historial de git | — | **5.45** | 79 |
| `xiaomi/mimo-v2-omni` | 2026-07-13 | proveedor | Xiaomi lo deprecó; recomienda migrar a MiMo V2.5 | — | **3.96** | 80 |
| `mistralai/devstral-medium` | 2026-07-13 | proveedor | OpenRouter: 'No endpoints found' | — | **5.51** | 83 |
| `x-ai/grok-4.1-fast` | 2026-07-13 | proveedor | xAI lo deprecó; recomienda migrar a Grok 4.3 | — | **5.66** | 86 |
| `xiaomi/mimo-v2-pro` | 2026-07-13 | proveedor | Xiaomi deprecó el modelo | — | **6.32** | 79 |
| `mistralai/devstral-small` | 2026-07-13 | proveedor | OpenRouter: 'No endpoints found'. Llegó a estar #5 del ranking. | — | **8.85** | 34 |
| `xiaomi/mimo-v2-flash` | 2026-07-13 | proveedor | Xiaomi deprecó el modelo | — | **9.04** | 31 |

<!-- AUTO-TABLE-END -->

#### Tabla manual (legacy): (68 modelos × 91 tests = 5,551 runs)

> Cobertura completa con juez Phi-4. **No re-medir** estos a menos que se cumpla la regla de mantenimiento.

| Modelo | OS | $ in/out | Lote | Notas |
|---|---|---|---|---|
| anthropic/claude-opus-4-7 | No | 15.0/75.0 | L2+1.5 | Premium baseline |
| anthropic/claude-opus-4-6 | No | 15.0/75.0 | KvO | El #1 Arena, baseline calidad |
| anthropic/claude-sonnet-4-6 | No | 3.0/15.0 | L1 | Top en honestidad |
| moonshotai/kimi-k2.6 | No | 1.5/9.0 | L3+KvO | Thinking, recuperado en Lote 5 |
| moonshotai/kimi-k2 | No | 1.0/3.0 | L2 | 17 errores 429 |
| deepseek/deepseek-chat | Si (MIT) | 0.252/0.378 | L1 | DeepSeek V3.2, top noticias SEO |
| minimax/minimax-m2.7 | Parcial | 0.30/1.20 | L1 | Highspeed via API directa |
| xiaomi/mimo-v2-flash | Si (MIT) | 0.09/0.29 | L1 | Sorpresa: top en strategy/code |
| xiaomi/mimo-v2-pro | No | 1.0/3.0 | L3 | Decepción: rinde menos que Flash |
| mistralai/devstral-small | Si (Apache 2.0) | 0.10/0.30 | L1 | **#1 global 7.35** |
| mistralai/devstral-medium | Si (Apache 2.0) | 0.40/2.0 | L3 | 3 errores 503 puntuales |
| mistralai/devstral-2512 | Si (Apache 2.0) | 0.40/2.0 | L3 | Devstral 2 (Dic 2025) |
| mistralai/mistral-large | Si (Apache) | 2.0/6.0 | L2 | 100% timeout en news_seo_writing |
| mistralai/mistral-nemo | Si (Apache) | 0.02/0.02 | L3 | Baseline ultra económico |
| qwen/qwen3-coder | Si (Apache) | 0.15/0.60 | L2 | Sólido en coding |
| qwen/qwen3.6-plus | No (proprietary) | 0.33/0.65 | L2 | API-only Alibaba, NO Apache |
| google/gemini-2.5-flash | No | 0.075/0.30 | L3 | Excluido del corte alternativas |
| google/gemini-2.5-flash-lite | No | 0.075/0.30 | L1 | El más rápido (165 tok/s) |
| google/gemini-2.5-pro | No | 1.25/5.0 | L3 | Thinking, recuperado en Lote 5 |
| google/gemma-4-26b-a4b-it | Si (Apache 2.0) | 0.05/0.20 | L3 | Open-source competitivo |
| gpt-4.1 | No | 2.0/8.0 | L2 | #3 global, supera a 5.4 |
| gpt-4.1-mini | No | 0.40/1.60 | L1 | Equilibrado |
| gpt-5.4 | No | 1.25/10.0 | L3 | Thinking, decepciona vs 4.1 |
| gpt-5.4-mini | No | 0.25/2.0 | L2 | Sorpresa: gana al grande |
| gpt-5.5 | No | 8.0/45.0 | L4 | Thinking, recuperado en L5 → 6.42 |
| meta-llama/llama-4-maverick | Si (Llama) | 0.40/2.40 | L1 | 17 errores 404 sin tools |
| nvidia/nemotron-3-super-120b-a12b | Si (NVIDIA Open) | 0.10/0.50 | L2 | Thinking, en Lote 5 |
| z-ai/glm-5.1 | Si (MIT) | 0.95/3.15 | L2 | Thinking, en Lote 5 |

**KvO** = Lote Kimi vs Opus (abril 22). **L1-L4** = Lotes oficiales. **L5** = re-corrida de empties (abril 25, en curso).

---

## En config sin probar (20 modelos)

> Configurados en `config.py` pero todavía sin run. Priorizados para próximos lotes.

### Prioridad alta (modelos producción / valor inmediato)

| Modelo | Tier | $ in/out | Razón para probar |
|---|---|---|---|
| `qwen3.5-397b-cloud` | cloud_ollama | $0/$0 | **Cristian usa este en producción** para ecosistemastartup.com. Smoke-test pasó (3 tests). |
| `groq-llama-3.3-70b` | cheap | 0.59/0.79 | Provider directo Groq, latencia ultra baja. |
| `groq-gpt-oss-120b` | cheap | 0.15/0.60 | OpenAI-OSS via Groq, alternativa a la versión OpenRouter. |
| `groq-llama-4-scout` | cheap | 0.11/0.34 | Multimodal Llama 4 vía Groq. |
| `deepseek-v4-flash` | cheap | 0.14/0.28 | Sucesor V3.2, 1M context. **Recién agregado abril 25**. |
| `deepseek-v4-pro` | medium | 1.74/3.48 | Flagship V4 1.6T params. |

### Prioridad media (cobertura de mercado)

| Modelo | Tier | $ in/out | Razón |
|---|---|---|---|
| `gpt-4o` | medium | 2.5/10 | Faltante de OpenAI no-thinking |
| `gpt-4o-high` | premium | 5.0/15 | High reasoning effort |
| `claude-sonnet` | medium | 3.0/15 | Sonnet 4 base (4.6 ya cubierto) |
| `gemma-4-31b` | cheap | 0.30/0.60 | El 26B ya está; el 31B podría sumar |
| `kimi-k2.5` | cheap | 0.20/0.80 | Versión intermedia entre K2 y K2.6 |
| `groq-gpt-oss-20b` | ultra_cheap | 0.075/0.30 | Modelo más chico de OpenAI-OSS |
| `groq-llama-3.1-8b` | ultra_cheap | 0.05/0.08 | Baseline ultra barato Groq |
| `gpt-oss-120b-cloud` | cloud_ollama | $0/$0 | Misma familia que el de Groq, comparar |
| `qwen3.5-cloud` | cloud_ollama | $0/$0 | El no-flagship de Ollama Cloud |

### Prioridad baja (duplicados o desuso)

| Modelo | Razón para no probar (todavía) |
|---|---|
| `minimax-m2.7-direct` | Mismo modelo que `minimax-m2.7` ya cubierto, distinto endpoint. Sólo si interesa medir latencia API directa. |
| `minimax-m2.7-highspeed` | Variante highspeed; diferencia marginal documentada (~1%). |
| `qwen-3.5-plus` | Versión vieja del Plus (3.6 Plus ya cubierto). |
| `deepseek-r1-free` / `llama-3.3-70b-free` / `qwen3-coder-free` | `:free` deprecados frecuentemente, baja confiabilidad para benchmark formal. |

### Listo para probar (desbloqueado)

| Modelo | Notas |
|---|---|
| `gpt-5.5-pro` | **Desbloqueado abril 25** — `OpenAIResponsesProvider` agregado. Smoke test OK: 39 reasoning_tokens + 46 output_tokens visibles para "hola" (~$0.009 por test, ~$72 por lote completo de 91 tests). Captura reasoning_tokens en metadata. |
| **NVIDIA NIM (8 modelos)** | **Desbloqueado abril 25** — provider `nvidia_nim` con base URL `https://integrate.api.nvidia.com/v1`. Free tier: 40 RPM, **gratis** para benchmarks secuenciales. Catálogo de 135+ modelos. Smoke test OK con Nemotron Super 49B v1.5. Modelos agregados al config (claves `nim-*`): Nemotron Super 49B v1.5, Nemotron Ultra 253B, Qwen 3-Next 80B (instruct + thinking), Mistral-Nemotron, Kimi K2 Thinking, DeepSeek V4 Flash, Qwen 3.5 397B. |

---

## Por agregar al config (mercado, abril 2026)

> Modelos lanzados que aún no están en `config.py`. Verificar IDs reales en OpenRouter antes de agregar.

| Modelo | Esperado | $ aprox | Razón |
|---|---|---|---|
| Mistral Small 4 | `mistralai/mistral-small-2603` | 0.15/0.60 | Apache 2.0, baseline. **Está en `config.example.py`, falta copiar a `config.py`**. |
| Grok 4.1 Fast | `x-ai/grok-4.1-fast` | 0.20/0.50 | xAI rápido. Está en `config.example.py`. |
| Grok 4.20 | TBD | 2.0/6.0 | Flagship xAI |
| Gemini 3.1 Flash Lite | TBD | 0.25/1.50 | Sucesor del 2.5 Flash Lite |
| Gemini 3.1 Pro | TBD | 2.0/12 | Sucesor del 2.5 Pro |
| DeepSeek R1, R1-0528 | `deepseek/deepseek-r1`, `deepseek-r1-0528` | 0.50-0.70/2.15-2.50 | Razonamiento dedicado |
| Hermes 4 | TBD | TBD | Open-source de Nous Research |
| Step 3.5 Flash | TBD | TBD | StepFun |
| Muse Spark | TBD | TBD | Mencionado en mercado abril 2026 |
| Qwen 3-Next 80B | TBD | TBD | Próxima generación Qwen |
| MiMo V2.5 / V2.5-Pro | `xiaomi/mimo-v2.5-*` | TBD | Multimodal nuevo abril 2026 |

**Acción**: agregar IDs verificados en `config.example.py` y `config.py`. Lote 6 medirá los priority high + estos nuevos.

---

## Plan de ejecución sugerido (Lote 6 — actualizado abril 25 con sync completo)

> Foco: cubrir TODOS los modelos del mercado abril 2026 + provider-direct sin probar.
> Total config: 130 modelos · 83 probados · **47 pendientes**.

### Sub-lote 6A: NIM gratis (8 modelos, ~2-3h, $0)
Prioridad alta — gratis con 40 RPM, joyas no disponibles en otros providers:
1. `nim-nemotron-super-1.5` (Nemotron Super 49B v1.5)
2. `nim-nemotron-ultra-253b` (más grande de la familia)
3. `nim-qwen3-next-instruct` (Qwen 3-Next 80B)
4. `nim-qwen3-next-thinking` (Qwen 3-Next thinking)
5. `nim-mistral-nemotron` (colab Mistral × NVIDIA)
6. `nim-kimi-k2-thinking` (variante explícita de K2)
7. `nim-deepseek-v4-flash` (vs OpenRouter, comparar)
8. `nim-qwen3.5-397b` (Cristian lo usa en producción via Ollama Cloud — comparar)

### Sub-lote 6B: Mercado nuevo OpenRouter (15 modelos, ~3-4h, ~$30-50)
Prioridad alta — productos lanzados abril 2026 sin medir:
1. `deepseek-v4-flash` ($0.14/$0.28, 1M context, MIT) — sucesor V3.2
2. `deepseek-v4-pro` ($1.74/$3.48, 1.6T params) — flagship V4
3. `gemini-3.1-flash-lite` ($0.25/$1.50)
4. `gemini-3.1-pro` ($2.00/$12.00)
5. `grok-4.1-fast` ($0.20/$0.50, xAI rápido)
6. `grok-4.20` ($2.00/$6.00, flagship xAI)
7. `mistral-small-4` ($0.15/$0.60, Apache 2.0)
8. `nemotron-nano` (30B, $0.05/$0.20, NVIDIA Open)
9. `mimo-v2-omni` ($0.40/$2.00, multimodal)
10. `mimo-v2.5` ($0.40/$2.00, omnimodal nuevo)
11. `mimo-v2.5-pro` ($1.00/$3.00, flagship Xiaomi)
12. `hermes-4-70b` ($0.13/$0.40, Nous Research, hybrid reasoning)
13. `hermes-4-405b` ($1.00/$3.00, flagship Hermes 4)
14. `step3` ($1.00/$3.00, MoE 321B multimodal)
15. `seed-oss-36b` ($0.20/$0.60, Apache 2.0, ByteDance)

### Sub-lote 6C: Cloud Ollama (3 modelos, ~1.5h, $0 con suscripción)
1. `qwen3.5-397b-cloud` (el que Cristian usa en producción)
2. `qwen3.5-cloud` (default Ollama Cloud)
3. `gpt-oss-120b-cloud`

### Sub-lote 6D: Groq direct (5 modelos, ~1h, ~$5-10)
1. `groq-llama-3.3-70b` ($0.59/$0.79)
2. `groq-llama-3.1-8b` ($0.05/$0.08, ultra-cheap)
3. `groq-llama-4-scout` ($0.11/$0.34, multimodal)
4. `groq-gpt-oss-120b` ($0.15/$0.60)
5. `groq-gpt-oss-20b` ($0.075/$0.30)

### Sub-lote 6E: Free tier (5 modelos, ~1h, $0)
1. `deepseek-r1-free`
2. `llama-3.3-70b-free`
3. `qwen3-coder-free`
4. `mimo-v2-flash-free`
5. `qwen-3.6-plus-free`

### Sub-lote 6F: Otros pendientes OpenRouter (9 modelos, ~2h, ~$15-25)
1. `kimi-k2.5` (cobertura entre K2 y K2.6)
2. `gpt-4o` ($2.5/$10)
3. `gpt-4o-high` ($5/$15, premium)
4. `claude-sonnet` (Sonnet 4 base)
5. `gemma-4-31b` (variante 31B vs 26B ya probado)
6. `qwen-3.5-plus` (vs 3.6 Plus)
7. `minimax-m2.7-direct` (provider directo, comparar latencia)
8. `minimax-m2.7-highspeed`
9. `gpt-5.5-pro` ($30/$180 — caro, ~$72/lote completo, decidir si vale)

### Resumen Lote 6 completo
- **68 modelos × 91 tests = 5,551 runs**
- **Tiempo total**: ~10-14h wall clock (en serial), ~6-8h en 2 parallel runs
- **Costo total**: ~$50-100 OpenRouter (NIM/Cloud/Free son $0)

### Recomendación de ejecución
Empezar con **6A + 6E + 6C** (todo gratis, ~16 modelos). Mientras corre, decidir si vale 6F (OpenAI/Claude/MiniMax legacy) y revisar pricing de 6B antes de commitear el costo OpenRouter.

---

*Para hacer un nuevo lote, usar `python benchmarks/runner.py --quick --judge --judge-model phi4 --models <key1> <key2> ...`. El runner es atómico: si se corta, retomar con `--resume <archivo.json>`.*

---

## Fechas de lanzamiento y knowledge cutoff

Snapshot de los modelos probados — útil para juzgar si un modelo "recuerda" eventos recientes o si tu prompt requiere modelo más nuevo. Verificado abril 2026.

### Anthropic
| Modelo | Lanzamiento | Knowledge cutoff |
|---|---|---|
| Claude Opus 4.7 | feb 2026 | oct 2025 |
| Claude Opus 4.6 | dic 2025 | jul 2025 |
| Claude Sonnet 4.6 | feb 2026 | oct 2025 |

### OpenAI
| Modelo | Lanzamiento | Knowledge cutoff |
|---|---|---|
| GPT-4.1 | abr 2025 | abr 2024 |
| GPT-4.1 Mini | abr 2025 | abr 2024 |
| GPT-5.4 | nov 2025 | sep 2025 |
| GPT-5.4 Mini | nov 2025 | sep 2025 |
| GPT-5.5 | mar 2026 | dic 2025 |
| GPT-5.5 Pro | mar 2026 | dic 2025 |

### Google
| Modelo | Lanzamiento | Knowledge cutoff |
|---|---|---|
| Gemini 2.5 Flash | jun 2025 | ene 2025 |
| Gemini 2.5 Flash Lite | jun 2025 | ene 2025 |
| Gemini 2.5 Pro | jun 2025 | ene 2025 |
| Gemma 4 26B | ene 2026 | jun 2025 |

### Mistral
| Modelo | Lanzamiento | Knowledge cutoff |
|---|---|---|
| Devstral Small | abr 2025 | abr 2024 |
| Devstral Medium | nov 2025 | jul 2025 |
| Devstral 2 (2512) | dic 2025 | sep 2025 |
| Mistral Large 2 | jul 2024 | feb 2024 |
| Mistral Nemo | jul 2024 | feb 2024 |

### DeepSeek
| Modelo | Lanzamiento | Knowledge cutoff |
|---|---|---|
| DeepSeek V3.2 | dic 2025 | jul 2025 |
| DeepSeek V4 Flash | abr 2026 | dic 2025 |
| DeepSeek V4 Pro | abr 2026 | dic 2025 |

### Moonshot Kimi
| Modelo | Lanzamiento | Knowledge cutoff |
|---|---|---|
| Kimi K2 | jul 2025 | abr 2025 |
| Kimi K2.5 | nov 2025 | jul 2025 |
| Kimi K2.6 (thinking) | mar 2026 | nov 2025 |

### Otros
| Modelo | Lanzamiento | Knowledge cutoff |
|---|---|---|
| MiniMax M2.7 | abr 2026 | dic 2025 |
| Qwen 3.6 Plus | ene 2026 | sep 2025 |
| Qwen3 Coder | ago 2025 | abr 2025 |
| MiMo V2 Flash (Xiaomi) | feb 2026 | sep 2025 |
| MiMo V2 Pro | feb 2026 | sep 2025 |
| GLM-5.1 | dic 2025 | jul 2025 |
| Llama 4 Maverick | abr 2025 | dic 2024 |
| Nemotron 3 Super | feb 2026 | sep 2025 |

> Datos basados en model cards de proveedores y HuggingFace. **Verificar antes de citar** — los proveedores a veces re-entrenan en silencio sin actualizar la fecha pública. Si aplica un caso de uso que requiere conocimiento de eventos recientes (ej. noticias post-cutoff), enriquecer con búsqueda web o RAG.
