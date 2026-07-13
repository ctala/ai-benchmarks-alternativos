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
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **8.50** | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.39** | 113 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.38** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **8.22** | 87 | [per-model](benchmarks/results/per-model/MiniMax-M3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.22** | 87 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_072815_69729/) |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **8.12** | 89 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.97** | 86 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.96** | 89 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.84** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.76** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.54** | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.46** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.45** | 87 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.39** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.30** | 87 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.27** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.23** | 147 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **7.14** | 87 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout-17b-16e-instruct.md) | — |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **7.12** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **6.99** | 83 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **6.98** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **6.94** | 85 | [per-model](benchmarks/results/per-model/llama-3_3-70b-versatile.md) | — |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **6.85** | 85 | [per-model](benchmarks/results/per-model/gemma4_31b.md) | — |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **6.83** | 91 | [per-model](benchmarks/results/per-model/hf_co_unsloth_diffusiongemma-26B-A4B-it-GGUF_Q8_0.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **6.82** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.80** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **6.74** | 64 | [per-model](benchmarks/results/per-model/mistralai_devstral-2-123b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **6.66** | 130 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **6.62** | 90 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **6.62** | 96 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **6.57** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `claude-fable-5` | ❌  | $10.0/50.0 | **6.55** | 87 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260713_075422_74587/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.49** | 115 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **6.48** | 87 | [per-model](benchmarks/results/per-model/gemma-4-31B-it-Q4_K_M_gguf.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **6.47** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **6.42** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.42** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260429_210054/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **6.40** | 82 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **6.39** | 86 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-instruct-2512.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **6.34** | 87 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **6.34** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **6.33** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **6.16** | 83 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-3-675b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **6.04** | 86 | [per-model](benchmarks/results/per-model/nemotron-3-super_120b.md) | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **6.00** | 87 | [per-model](benchmarks/results/per-model/nemotron3_33b-q4_K_M.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **5.98** | 131 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **5.98** | 174 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **5.93** | 86 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **5.92** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **5.91** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **5.86** | 144 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **5.83** | 234 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **5.82** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **5.81** | 86 | [per-model](benchmarks/results/per-model/z-ai_glm5.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **5.80** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **5.79** | 87 | [per-model](benchmarks/results/per-model/nvidia_nvidia-nemotron-nano-9b-v2.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **5.77** | 82 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **5.71** | 147 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **5.68** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **5.54** | 87 | [per-model](benchmarks/results/per-model/gpt-oss_120b-cloud.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **5.49** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **5.47** | 147 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **5.47** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **5.45** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **5.37** | 89 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **5.30** | 147 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **5.25** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5-pro.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.20** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **5.07** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **4.90** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **4.82** | 142 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **4.67** | 87 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **4.58** | 174 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **4.16** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **3.93** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **3.88** | 147 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **3.72** | 100 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **3.58** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **3.34** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **3.33** | 86 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **3.27** | 90 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **3.02** | 108 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **3.01** | 66 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260503_125944/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **2.90** | 142 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **2.88** | 118 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **2.78** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **2.48** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **0.88** | 87 | [per-model](benchmarks/results/per-model/stepfun-ai_step-3_5-flash.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **0.69** | 86 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.21** | 87 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 90 | [per-model](benchmarks/results/per-model/qwen3_5_397b-cloud.md) | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 87 | [per-model](benchmarks/results/per-model/qwen3_5_cloud.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **0.00** | 87 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |

#### Mejor calidad pura (sin considerar costo ni velocidad)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **8.81** | 89 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.77** | 87 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_072815_69729/) |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.71** | 86 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **8.65** | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **8.64** | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **8.64** | 87 | [per-model](benchmarks/results/per-model/MiniMax-M3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **8.63** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **8.56** | 89 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.54** | 87 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.47** | 113 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **8.40** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `claude-fable-5` | ❌  | $10.0/50.0 | **8.40** | 87 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260713_075422_74587/) |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **8.39** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.38** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.34** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **8.32** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **8.28** | 85 | [per-model](benchmarks/results/per-model/gemma4_31b.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **8.24** | 90 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **8.24** | 115 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **8.24** | 83 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-3-675b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.20** | 83 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **8.20** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.20** | 174 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **8.17** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.17** | 234 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **8.16** | 87 | [per-model](benchmarks/results/per-model/gemma-4-31B-it-Q4_K_M_gguf.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **8.15** | 91 | [per-model](benchmarks/results/per-model/hf_co_unsloth_diffusiongemma-26B-A4B-it-GGUF_Q8_0.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **8.15** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **8.13** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **8.10** | 86 | [per-model](benchmarks/results/per-model/z-ai_glm5.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **8.08** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **8.08** | 64 | [per-model](benchmarks/results/per-model/mistralai_devstral-2-123b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **8.08** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.07** | 87 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.06** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **8.06** | 86 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-instruct-2512.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **8.05** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260429_210054/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **8.05** | 82 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.04** | 147 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **8.02** | 130 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **8.02** | 96 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **8.02** | 86 | [per-model](benchmarks/results/per-model/nemotron-3-super_120b.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.97** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.96** | 144 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.96** | 89 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.94** | 147 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **7.92** | 82 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.91** | 87 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.90** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.90** | 131 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.90** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.87** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.87** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **7.86** | 87 | [per-model](benchmarks/results/per-model/nemotron3_33b-q4_K_M.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.83** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **7.82** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning.md) | — |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **7.81** | 87 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout-17b-16e-instruct.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **7.81** | 174 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **7.80** | 87 | [per-model](benchmarks/results/per-model/nvidia_nvidia-nemotron-nano-9b-v2.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.79** | 147 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.77** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **7.76** | 85 | [per-model](benchmarks/results/per-model/llama-3_3-70b-versatile.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.76** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.70** | 142 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.68** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **7.67** | 87 | [per-model](benchmarks/results/per-model/gpt-oss_120b-cloud.md) | — |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **7.66** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5-pro.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.66** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.61** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **7.56** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5.md) | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **7.53** | 87 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.49** | 147 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **7.45** | 86 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **7.44** | 90 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.42** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.41** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **7.40** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.38** | 147 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **7.30** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.24** | 100 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.24** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.22** | 66 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260503_125944/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.20** | 142 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.08** | 108 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **7.04** | 86 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.03** | 118 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.91** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **6.69** | 87 | [per-model](benchmarks/results/per-model/stepfun-ai_step-3_5-flash.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **6.65** | 86 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.59** | 87 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **6.28** | 87 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **5.43** | 90 | [per-model](benchmarks/results/per-model/qwen3_5_397b-cloud.md) | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **5.19** | 87 | [per-model](benchmarks/results/per-model/qwen3_5_cloud.md) | — |

#### Mejor coding

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.18** | 147 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **8.17** | 86 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **8.17** | 87 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout-17b-16e-instruct.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.14** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.95** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.93** | 113 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.93** | 87 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.92** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.89** | 144 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.88** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **7.85** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.85** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.84** | 87 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **7.81** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.81** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **7.80** | 85 | [per-model](benchmarks/results/per-model/llama-3_3-70b-versatile.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.80** | 147 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.78** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.73** | 142 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.71** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.71** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **7.71** | 87 | [per-model](benchmarks/results/per-model/nvidia_nvidia-nemotron-nano-9b-v2.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.70** | 96 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **7.65** | 87 | [per-model](benchmarks/results/per-model/gpt-oss_120b-cloud.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.64** | 130 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.63** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **7.62** | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.62** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.62** | 147 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.59** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.58** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.55** | 87 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.54** | 64 | [per-model](benchmarks/results/per-model/mistralai_devstral-2-123b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.51** | 86 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.51** | 89 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **7.50** | 82 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.47** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.46** | 90 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **7.45** | 87 | [per-model](benchmarks/results/per-model/nemotron3_33b-q4_K_M.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.43** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.43** | 131 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **7.43** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.43** | 142 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.41** | 83 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.41** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.39** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260429_210054/) |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **7.38** | 87 | [per-model](benchmarks/results/per-model/gemma-4-31B-it-Q4_K_M_gguf.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **7.38** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5-pro.md) | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **7.38** | 87 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.37** | 87 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_072815_69729/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.37** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **7.35** | 115 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.34** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.33** | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **7.33** | 86 | [per-model](benchmarks/results/per-model/nemotron-3-super_120b.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **7.33** | 82 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.33** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **7.33** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.30** | 147 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.29** | 174 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.28** | 147 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.27** | 89 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.27** | 66 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260503_125944/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.24** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **7.20** | 85 | [per-model](benchmarks/results/per-model/gemma4_31b.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **7.19** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.12** | 118 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.12** | 87 | [per-model](benchmarks/results/per-model/MiniMax-M3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **7.12** | 89 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **7.11** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.11** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.11** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.10** | 108 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.10** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **7.10** | 86 | [per-model](benchmarks/results/per-model/z-ai_glm5.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **7.09** | 174 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **7.07** | 86 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-instruct-2512.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.06** | 234 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.04** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.03** | 100 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **7.00** | 83 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-3-675b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **6.99** | 90 | [per-model](benchmarks/results/per-model/qwen3_5_397b-cloud.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.94** | 90 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `claude-fable-5` | ❌  | $10.0/50.0 | **6.89** | 87 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260713_075422_74587/) |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **6.83** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **6.76** | 91 | [per-model](benchmarks/results/per-model/hf_co_unsloth_diffusiongemma-26B-A4B-it-GGUF_Q8_0.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.75** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **6.64** | 87 | [per-model](benchmarks/results/per-model/stepfun-ai_step-3_5-flash.md) | — |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **6.56** | 86 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.46** | 87 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **6.34** | 86 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **6.29** | 87 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **5.77** | 87 | [per-model](benchmarks/results/per-model/qwen3_5_cloud.md) | — |

#### Mejor razonamiento

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **8.23** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.12** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **8.10** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.05** | 147 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **8.05** | 87 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout-17b-16e-instruct.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **8.03** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **8.00** | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.99** | 147 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.98** | 87 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.97** | 113 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.91** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.90** | 142 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.90** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **7.88** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.88** | 96 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **7.86** | 85 | [per-model](benchmarks/results/per-model/llama-3_3-70b-versatile.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.85** | 131 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **7.84** | 87 | [per-model](benchmarks/results/per-model/gpt-oss_120b-cloud.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.84** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.79** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.79** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.78** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.78** | 83 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **7.78** | 87 | [per-model](benchmarks/results/per-model/nemotron3_33b-q4_K_M.md) | — |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **7.74** | 85 | [per-model](benchmarks/results/per-model/gemma4_31b.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.72** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **7.72** | 82 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **7.72** | 86 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **7.72** | 82 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.71** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.71** | 89 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.70** | 64 | [per-model](benchmarks/results/per-model/mistralai_devstral-2-123b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **7.69** | 89 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.68** | 144 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.66** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.64** | 87 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.63** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.62** | 130 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.62** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **7.59** | 87 | [per-model](benchmarks/results/per-model/gemma-4-31B-it-Q4_K_M_gguf.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **7.58** | 91 | [per-model](benchmarks/results/per-model/hf_co_unsloth_diffusiongemma-26B-A4B-it-GGUF_Q8_0.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.56** | 87 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_072815_69729/) |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **7.56** | 86 | [per-model](benchmarks/results/per-model/nemotron-3-super_120b.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.54** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.50** | 87 | [per-model](benchmarks/results/per-model/MiniMax-M3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.50** | 86 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **7.50** | 87 | [per-model](benchmarks/results/per-model/nvidia_nvidia-nemotron-nano-9b-v2.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **7.50** | 86 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-instruct-2512.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.48** | 147 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.48** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `claude-fable-5` | ❌  | $10.0/50.0 | **7.47** | 87 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260713_075422_74587/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **7.44** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.40** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260429_210054/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.38** | 90 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.37** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.33** | 234 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **7.30** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.28** | 87 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.25** | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.24** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.21** | 100 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **7.21** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.20** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.17** | 147 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.16** | 174 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.16** | 89 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **7.13** | 86 | [per-model](benchmarks/results/per-model/z-ai_glm5.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **7.03** | 83 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-3-675b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.96** | 90 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **6.88** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.86** | 115 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.83** | 174 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.79** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **6.65** | 86 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **6.59** | 118 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.28** | 108 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.22** | 142 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.19** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **6.17** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5-pro.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **6.09** | 147 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.09** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **6.00** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **5.97** | 66 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260503_125944/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **5.95** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **5.94** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.84** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **5.34** | 87 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **4.98** | 87 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **4.45** | 87 | [per-model](benchmarks/results/per-model/qwen3_5_cloud.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **4.01** | 86 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **3.90** | 87 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **3.85** | 87 | [per-model](benchmarks/results/per-model/stepfun-ai_step-3_5-flash.md) | — |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **3.35** | 90 | [per-model](benchmarks/results/per-model/qwen3_5_397b-cloud.md) | — |

#### Mejor contenido/marketing

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **8.19** | 86 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.06** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.03** | 87 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.00** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **8.00** | 85 | [per-model](benchmarks/results/per-model/llama-3_3-70b-versatile.md) | — |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **7.95** | 87 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout-17b-16e-instruct.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.95** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **7.94** | 87 | [per-model](benchmarks/results/per-model/gpt-oss_120b-cloud.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.93** | 113 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **7.93** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.93** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.93** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.91** | 147 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.82** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **7.81** | 87 | [per-model](benchmarks/results/per-model/nemotron3_33b-q4_K_M.md) | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **7.79** | 87 | [per-model](benchmarks/results/per-model/nvidia_nvidia-nemotron-nano-9b-v2.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **7.78** | 86 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.77** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.77** | 87 | [per-model](benchmarks/results/per-model/MiniMax-M3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **7.76** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5-pro.md) | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **7.76** | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.75** | 89 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.75** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.74** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **7.73** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.67** | 87 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.67** | 96 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **7.65** | 82 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **7.65** | 87 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **7.64** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5.md) | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.63** | 83 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **7.63** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **7.61** | 86 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-instruct-2512.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.60** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.58** | 64 | [per-model](benchmarks/results/per-model/mistralai_devstral-2-123b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.58** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.57** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.55** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **7.55** | 82 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.55** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.54** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **7.53** | 91 | [per-model](benchmarks/results/per-model/hf_co_unsloth_diffusiongemma-26B-A4B-it-GGUF_Q8_0.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.53** | 147 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.51** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **7.50** | 89 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.50** | 87 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_072815_69729/) |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.50** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **7.48** | 85 | [per-model](benchmarks/results/per-model/gemma4_31b.md) | — |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **7.48** | 86 | [per-model](benchmarks/results/per-model/nemotron-3-super_120b.md) | — |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **7.47** | 87 | [per-model](benchmarks/results/per-model/gemma-4-31B-it-Q4_K_M_gguf.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.47** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.45** | 147 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.43** | 130 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.40** | 131 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.35** | 147 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.34** | 86 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.34** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.32** | 100 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.30** | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.30** | 90 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.30** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.27** | 87 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **7.25** | 87 | [per-model](benchmarks/results/per-model/stepfun-ai_step-3_5-flash.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.23** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260429_210054/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **7.20** | 115 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **7.20** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.20** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.20** | 142 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **7.19** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **7.16** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.15** | 144 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.15** | 89 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.14** | 118 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `claude-fable-5` | ❌  | $10.0/50.0 | **7.14** | 87 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260713_075422_74587/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.09** | 147 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.08** | 108 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.02** | 174 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **7.01** | 86 | [per-model](benchmarks/results/per-model/z-ai_glm5.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **7.00** | 90 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **6.97** | 83 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-3-675b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.87** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.84** | 234 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.84** | 174 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.76** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.63** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.52** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **6.52** | 86 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.41** | 142 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **6.39** | 66 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260503_125944/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **5.93** | 87 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **5.78** | 87 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **5.45** | 90 | [per-model](benchmarks/results/per-model/qwen3_5_397b-cloud.md) | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **4.53** | 87 | [per-model](benchmarks/results/per-model/qwen3_5_cloud.md) | — |

#### Mejor relación calidad/costo (pesos v2.9: 60% quality, 20% costo, 10% speed, 10% latency)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **8.83** | 89 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **8.48** | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.22** | 86 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.09** | 113 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.92** | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.72** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.72** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.70** | 87 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.67** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.58** | 87 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_072815_69729/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.46** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `claude-fable-5` | ❌  | $10.0/50.0 | **7.44** | 87 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260713_075422_74587/) |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.31** | 87 | [per-model](benchmarks/results/per-model/MiniMax-M3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.29** | 118 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.25** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.21** | 87 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.04** | 89 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **6.99** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5.md) | — |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **6.92** | 87 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout-17b-16e-instruct.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **6.91** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **6.89** | 87 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **6.81** | 147 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **6.74** | 85 | [per-model](benchmarks/results/per-model/llama-3_3-70b-versatile.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **6.73** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **6.68** | 83 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.54** | 174 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **6.51** | 87 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **6.47** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **6.38** | 90 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.36** | 115 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.30** | 234 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **6.25** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.24** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **6.20** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **6.18** | 64 | [per-model](benchmarks/results/per-model/mistralai_devstral-2-123b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **6.08** | 87 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.05** | 147 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **6.00** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **5.96** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **5.95** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **5.95** | 87 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **5.94** | 87 | [per-model](benchmarks/results/per-model/gpt-oss_120b-cloud.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **5.94** | 86 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **5.93** | 130 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **5.90** | 91 | [per-model](benchmarks/results/per-model/hf_co_unsloth_diffusiongemma-26B-A4B-it-GGUF_Q8_0.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **5.87** | 74 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260429_210054/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **5.85** | 96 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **5.84** | 87 | [per-model](benchmarks/results/per-model/nvidia_nvidia-nemotron-nano-9b-v2.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **5.84** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **5.83** | 144 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **5.83** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **5.78** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5-pro.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **5.77** | 87 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **5.71** | 85 | [per-model](benchmarks/results/per-model/gemma4_31b.md) | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **5.69** | 83 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-3-675b-instruct-2512.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **5.59** | 86 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **5.54** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **5.50** | 82 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **5.47** | 86 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-instruct-2512.md) | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **5.46** | 87 | [per-model](benchmarks/results/per-model/nemotron3_33b-q4_K_M.md) | — |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **5.42** | 87 | [per-model](benchmarks/results/per-model/gemma-4-31B-it-Q4_K_M_gguf.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **5.28** | 89 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **5.25** | 131 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **5.22** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **5.22** | 147 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **5.20** | 147 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **5.18** | 86 | [per-model](benchmarks/results/per-model/nemotron-3-super_120b.md) | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **5.12** | 86 | [per-model](benchmarks/results/per-model/z-ai_glm5.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.07** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **4.95** | 82 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **4.90** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **4.87** | 87 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **4.74** | 147 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **4.74** | 174 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **4.67** | 142 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **4.41** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **4.27** | 90 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **4.14** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **4.04** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **3.92** | 100 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **3.76** | 87 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **3.63** | 142 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **3.56** | 147 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **3.35** | 108 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **2.87** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **2.76** | 66 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260503_125944/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **2.54** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **1.50** | 87 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **1.37** | 87 | [per-model](benchmarks/results/per-model/stepfun-ai_step-3_5-flash.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **1.09** | 86 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 90 | [per-model](benchmarks/results/per-model/qwen3_5_397b-cloud.md) | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 87 | [per-model](benchmarks/results/per-model/qwen3_5_cloud.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **0.00** | 87 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |

#### En evaluación — muestra parcial (<50 runs, NO rankeados)

> Estos modelos tienen menos runs que el piso del ranking, así que su score es **indicativo, no comparable**: con pocas muestras la varianza permite que un modelo quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** en las tablas de arriba hasta completar la cobertura.

| Modelo | OS | $ in/out | Score (indicativo) | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `MiniMax-M2.7` | ❌  | $0.3/1.2 | **10.00** | 23 | [per-model](benchmarks/results/per-model/MiniMax-M2_7.md) | — |
| `MiniMax-M2.7-highspeed` | ❌  | $0.3/1.2 | **10.00** | 23 | [per-model](benchmarks/results/per-model/MiniMax-M2_7-highspeed.md) | — |
| `mistralai/mistral-nemotron` | ✅ Apache 2.0 | $0.3/1.2 | **8.27** | 8 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemotron.md) | [responses](benchmarks/results/responses/20260713_095126_91593/) |
| `deepseek-ai/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.98** | 2 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260503_125944/) |
| `google/gemma-4-31b-it` | ✅ Apache 2.0 | $0.3/0.6 | **7.41** | 7 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `qwen3.6:27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.98** | 4 | [per-model](benchmarks/results/per-model/qwen3_6_27b.md) | — |
| `mistralai/magistral-small-2506` | ✅ Apache 2.0 | $0.5/1.5 | **5.67** | 6 | [per-model](benchmarks/results/per-model/mistralai_magistral-small-2506.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.2/0.8 | **0.00** | 23 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260713_083709_82198/) |

#### Retirados — el proveedor ya no los sirve

> **Estos modelos ya no se pueden llamar.** El endpoint devuelve *deprecated* o *no endpoints found*. Sus números son reales y quedan acá por transparencia (alimentan el análisis histórico), pero **están fuera del ranking y de las recomendaciones**: un modelo que no puedes usar no es un candidato. Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera.

| Modelo | OS | $ in/out | Score (histórico) | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **7.94** | 149 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **6.50** | 84 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `llama-3.1-8b-instant` | ✅ Llama Community | $0.05/0.08 | **6.31** | 85 | [per-model](benchmarks/results/per-model/llama-3_1-8b-instant.md) | — |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **5.56** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **4.58** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |

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
