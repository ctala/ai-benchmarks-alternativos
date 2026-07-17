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

#### Score global (perfil emprendedor: calidad 70%, costo 15%, velocidad 7.5%, latencia 7.5%)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.34** | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.80** | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.21** | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.19** | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260716_rm_gemma_4_26b_/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.17** | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.14** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.08** | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **6.87** | 128 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260716_rm_nemotron_super_/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.86** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **6.86** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260716_rm_glm_5_2_/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **6.85** | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **6.79** | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.78** | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.77** | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **6.70** | 138 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_r1_/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **6.65** | 132 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.57** | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260716_rm_minimax_m3_/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.54** | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.51** | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.50** | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **6.49** | 138 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **6.49** | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **6.47** | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **6.30** | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_flash_/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.28** | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.25** | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **6.22** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **6.09** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **6.02** | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **5.93** | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **5.89** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **5.80** | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **5.69** | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.64** | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **5.56** | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_7_code_/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **5.56** | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **5.53** | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **5.46** | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **5.44** | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **5.42** | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **5.41** | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **5.39** | 141 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260716_rm_llama_4_maverick_/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **5.37** | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **5.37** | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **5.30** | 136 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260716_rm_devstral_2_/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **5.29** | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_120b_/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **5.21** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **5.16** | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **5.15** | 213 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.14** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **5.12** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **5.02** | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **4.67** | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **4.64** | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **4.59** | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **4.51** | 128 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260716_rm_or_llama_4_scout_/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **4.43** | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **4.31** | 135 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **4.18** | 147 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **3.96** | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **3.88** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_20b_/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **3.80** | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **3.54** | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **3.24** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **3.07** | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **2.66** | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **1.44** | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **1.43** | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **0.50** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |

#### Mejor calidad pura (sin considerar costo ni velocidad)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.41** | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.34** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **8.30** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.30** | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.29** | 138 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_r1_/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **8.29** | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **8.27** | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.26** | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **8.25** | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **8.24** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260716_rm_glm_5_2_/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.21** | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **8.20** | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **8.20** | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **8.19** | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260716_rm_gemma_4_26b_/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.18** | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **8.17** | 128 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260716_rm_nemotron_super_/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.17** | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.16** | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **8.15** | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260716_rm_minimax_m3_/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **8.15** | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **8.15** | 138 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **8.14** | 132 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **8.13** | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **8.12** | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **8.12** | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **8.09** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **8.06** | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **8.05** | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **8.05** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.02** | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_flash_/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **8.00** | 213 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.97** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.95** | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.94** | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_7_code_/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.93** | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.91** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.90** | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.88** | 141 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260716_rm_llama_4_maverick_/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.87** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.87** | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.86** | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.85** | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.85** | 136 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260716_rm_devstral_2_/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.85** | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_120b_/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.85** | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.83** | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.83** | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.82** | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.82** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **7.82** | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.81** | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.79** | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.75** | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.73** | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.72** | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.71** | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.68** | 135 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.66** | 147 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **7.66** | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **7.63** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.60** | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.59** | 128 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260716_rm_or_llama_4_scout_/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.53** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_20b_/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.52** | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.44** | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.32** | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.20** | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **7.11** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **7.09** | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |

#### Mejor coding

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.77** | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.70** | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.70** | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.64** | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.56** | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.54** | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.53** | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.46** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.43** | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.42** | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.40** | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.40** | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.35** | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.32** | 135 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.30** | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.29** | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.26** | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.25** | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.25** | 136 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260716_rm_devstral_2_/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.25** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_20b_/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.24** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.24** | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_7_code_/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.23** | 138 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.22** | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.21** | 141 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260716_rm_llama_4_maverick_/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.21** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.19** | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_flash_/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.19** | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.17** | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.16** | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.13** | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.12** | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.11** | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.10** | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.09** | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260716_rm_gemma_4_26b_/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.07** | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.06** | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.04** | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_120b_/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.03** | 128 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260716_rm_nemotron_super_/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.02** | 132 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.01** | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.00** | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **6.99** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **6.89** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260716_rm_glm_5_2_/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.88** | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.86** | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **6.86** | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **6.84** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.82** | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **6.81** | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.80** | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.79** | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260716_rm_minimax_m3_/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **6.78** | 128 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260716_rm_or_llama_4_scout_/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.74** | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.71** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.71** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.70** | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **6.67** | 138 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_r1_/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.65** | 147 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.63** | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.61** | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.59** | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.59** | 213 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.56** | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.41** | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.29** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **6.29** | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.24** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **6.13** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |

#### Mejor razonamiento

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.13** | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.13** | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **8.01** | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.94** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.88** | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.88** | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.87** | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260716_rm_gemma_4_26b_/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.84** | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.84** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.82** | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.77** | 132 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.77** | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.76** | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.75** | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.71** | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_7_code_/) |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.67** | 136 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260716_rm_devstral_2_/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.66** | 128 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260716_rm_nemotron_super_/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.63** | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.61** | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.60** | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.59** | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_120b_/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.57** | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_flash_/) |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.53** | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.53** | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.50** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.45** | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.43** | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.41** | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.40** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_20b_/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.38** | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.36** | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.33** | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.31** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.31** | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.29** | 128 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260716_rm_or_llama_4_scout_/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.28** | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.25** | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.23** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.22** | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.21** | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.20** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260716_rm_glm_5_2_/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.17** | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.13** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.12** | 138 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_r1_/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.10** | 141 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260716_rm_llama_4_maverick_/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.04** | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.02** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.02** | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.01** | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.96** | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **6.91** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.89** | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.88** | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.84** | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260716_rm_minimax_m3_/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **6.83** | 138 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.82** | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.82** | 147 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.82** | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.79** | 213 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **6.71** | 135 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **6.61** | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.54** | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.43** | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.42** | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.38** | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.38** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **5.97** | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **5.00** | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **4.85** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |

#### Mejor contenido/marketing

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.64** | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.61** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.58** | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.57** | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.55** | 128 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260716_rm_or_llama_4_scout_/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.55** | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.54** | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.51** | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.50** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_20b_/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.49** | 128 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260716_rm_nemotron_super_/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.48** | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_flash_/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.47** | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.45** | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.41** | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_120b_/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.41** | 132 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.38** | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.37** | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260716_rm_gemma_4_26b_/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.36** | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.36** | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.34** | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.33** | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.29** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.29** | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.28** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.28** | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.28** | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.22** | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.22** | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.20** | 147 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.19** | 136 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260716_rm_devstral_2_/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.19** | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.19** | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260716_rm_minimax_m3_/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.17** | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **7.16** | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.15** | 135 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.13** | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.12** | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.09** | 141 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260716_rm_llama_4_maverick_/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.06** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260716_rm_glm_5_2_/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.05** | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.03** | 138 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_r1_/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.02** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.02** | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_7_code_/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.00** | 138 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **6.98** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.98** | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **6.97** | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.94** | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **6.91** | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.83** | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.80** | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **6.79** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.78** | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.76** | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.76** | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.70** | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **6.68** | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.67** | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.66** | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.65** | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.65** | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **6.59** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.51** | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.48** | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.46** | 213 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.43** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.29** | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.26** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.20** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |

#### Mejor relación calidad/costo (pesos v2.9: 60% quality, 20% costo, 10% speed, 10% latency)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **9.31** | 138 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.23** | 130 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.81** | 127 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.69** | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.69** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.50** | 124 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.40** | 172 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.38** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.36** | 140 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.33** | 139 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.10** | 128 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260716_rm_mistral_large_/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.06** | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.04** | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **6.96** | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260716_rm_gemma_4_26b_/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.95** | 141 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **6.93** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.89** | 141 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260716_rm_or_mistral_large_3_/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **6.88** | 130 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260716_rm_glm_5_2_/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.76** | 133 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **6.65** | 144 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_flash_/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **6.53** | 128 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260716_rm_nemotron_super_/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **6.52** | 138 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_r1_/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **6.52** | 138 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.46** | 206 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260716_rm_minimax_m3_/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **6.43** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.36** | 134 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **6.17** | 128 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **6.08** | 132 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v3_/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **6.00** | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **5.96** | 246 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **5.79** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.70** | 139 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **5.69** | 185 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **5.64** | 130 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_120b_/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **5.52** | 129 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **5.48** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.46** | 125 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **5.40** | 138 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **5.27** | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **5.15** | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **5.10** | 138 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **5.10** | 126 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **5.10** | 213 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **5.09** | 138 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **5.06** | 124 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260716_rnano/) |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **4.96** | 136 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260716_rm_devstral_2_/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **4.94** | 172 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260716_rm_deepseek_v4_pro_/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **4.90** | 133 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **4.88** | 121 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **4.85** | 138 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_405b_/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **4.82** | 156 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_7_code_/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **4.73** | 141 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260716_rm_llama_4_maverick_/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **4.67** | 126 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260716_rm_or_gpt_oss_20b_/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **4.48** | 193 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **4.43** | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **4.25** | 130 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **4.24** | 122 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **3.97** | 128 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260716_rm_or_llama_4_scout_/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **3.95** | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260716_sr/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **3.47** | 135 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **3.32** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **3.30** | 133 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **3.17** | 141 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260716_rm_hermes_4_70b_/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **3.07** | 147 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **3.03** | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **2.40** | 132 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **2.33** | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **0.95** | 142 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **0.00** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |

#### Vía suscripción Claude — plano propio (comparables entre sí)

> Medidos aprovechando la **suscripción de Claude Code** (costo marginal $0), todos por el mismo camino → **comparables entre ellos**. Ese camino arrastra ~8.8K tokens de scaffolding del CLI y **deprime la nota**: en los 2 modelos medidos por ambos caminos, la calidad por API dio **+0.15 y +0.22 más** que por suscripción. Leé estos números como **piso conservador**, no como techo — y no los compares 1:1 contra la tabla principal (la latencia por CLI es 2.5-4× peor y no es del modelo). Sirven para la pregunta de quien ya paga el plan: *¿qué modelo uso dentro de mi suscripción?*

| Modelo | Calidad (piso) | Velocidad | Runs | Per-model MD | Responses |
|---|---:|---:|---:|---|---|
| `claude-fable-5` | **8.35** | 58 tok/s | 102 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260716_rm_or_claude_fable_5_/) |
| `claude-opus-4-8` | **8.20** | 58 tok/s | 109 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `claude-sonnet-4-6` | **8.10** | 49 tok/s | 93 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `claude-opus-4-7` | **8.05** | 53 tok/s | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `claude-haiku-4-5` | **7.98** | 102 tok/s | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |

#### Variantes de proveedor (36 mediciones)

> El mismo modelo servido por otra infraestructura (Groq, NVIDIA NIM, Ollama Cloud, API directa del proveedor, self-hosted). **No compiten acá** — comparar infra contra infra es otra pregunta, y tiene su propia página: [el proveedor te cambia el modelo](https://benchmarks.cristiantala.com/mismo-modelo-distinto-proveedor/). El caso extremo medido: el mismo Qwen 3.5 397B da **7.96 en NVIDIA NIM y 5.46 en Ollama Cloud** — 2.5 puntos por la infraestructura, no por el modelo.

#### En evaluación — muestra parcial (<50 runs, NO rankeados)

> Estos modelos tienen menos runs que el piso del ranking, así que su score es **indicativo, no comparable**: con pocas muestras la varianza permite que un modelo quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** en las tablas de arriba hasta completar la cobertura.

| Modelo | OS | $ in/out | Score (indicativo) | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `gpt-5.5` | ❌  | $5.0/30.0 | **5.85** | 152 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **5.36** | 2 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260716_rm_kimi_k2_/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **0.00** | 166 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260715_082251_44555/) |

#### Retirados — el proveedor ya no los sirve

> **Estos modelos ya no se pueden llamar.** El endpoint devuelve *deprecated* o *no endpoints found*. Sus números son reales y quedan acá por transparencia (alimentan el análisis histórico), pero **están fuera del ranking y de las recomendaciones**: un modelo que no puedes usar no es un candidato. Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera.

| Modelo | OS | $ in/out | Score (histórico) | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **10.00** | 31 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **9.86** | 34 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **6.07** | 74 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **5.85** | 79 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **5.72** | 79 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **5.37** | 86 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **4.70** | 83 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **4.17** | 80 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen-2.5-72b-instruct` | ✅ Apache 2.0 | $0.36/0.4 | **3.87** | 63 | [per-model](benchmarks/results/per-model/qwen_qwen-2_5-72b-instruct.md) | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **2.80** | 52 | [per-model](benchmarks/results/per-model/qwen3_5_cloud.md) | — |

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
