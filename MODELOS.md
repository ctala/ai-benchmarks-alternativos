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

> **No existe un único 'mejor modelo'.** El score global es una combinación de calidad, costo, velocidad y latencia con pesos elegidos para emprendedores (70% calidad, 15% costo, 7.5% velocidad, 7.5% latencia). Usá las tablas por caso de uso para tu decisión real. Para pesos personalizados usá la [calculadora](https://benchmarks.cristiantala.com/).

#### Score global (perfil emprendedor: calidad 70%, costo 15%, velocidad 7.5%, latencia 7.5%)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.29** | 133 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.25** | 103 | — | [responses](benchmarks/results/responses/20260602_125445_2513153/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.09** | 103 | — | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **8.08** | 101 | — | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **7.97** | 98 | — | — |
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **7.96** | 169 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.89** | 98 | — | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.81** | 101 | — | — |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.80** | 103 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **7.77** | 103 | — | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **7.71** | 115 | — | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.63** | 103 | — | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.59** | 82 | — | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.44** | 105 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.39** | 103 | — | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.39** | 86 | — | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **7.37** | 103 | — | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.34** | 103 | — | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.18** | 103 | — | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.12** | 103 | — | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.11** | 103 | — | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.11** | 99 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **7.07** | 103 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **7.06** | 97 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **7.05** | 100 | — | — |
| `claude-fable-5` | ❌  | $10.0/50.0 | **6.95** | 103 | — | [responses](benchmarks/results/responses/20260609_144836_25113/) |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **6.90** | 89 | — | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **6.79** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **6.78** | 103 | — | — |
| `llama-3.1-8b-instant` | ✅ Llama Community | $0.05/0.08 | **6.77** | 100 | — | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **6.68** | 103 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.61** | 135 | — | — |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **6.51** | 90 | — | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.50** | 74 | — | [responses](benchmarks/results/responses/20260429_210054/) |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **6.49** | 68 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **6.43** | 135 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **6.43** | 134 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260602_135955_2529872/) |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **6.33** | 103 | — | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **6.20** | 97 | — | — |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **6.14** | 88 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **6.14** | 87 | — | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **6.13** | 91 | — | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **6.07** | 104 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260424_053942/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **6.07** | 99 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **6.04** | 103 | — | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.02** | 103 | — | — |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **5.99** | 90 | — | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **5.91** | 103 | — | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **5.88** | 182 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **5.80** | 103 | — | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **5.77** | 91 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **5.76** | 103 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **5.73** | 91 | — | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **5.72** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **5.67** | 246 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **5.65** | 86 | — | [responses](benchmarks/results/responses/20260602_125451_2513176/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **5.58** | 138 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260625_172532_3007190/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **5.47** | 167 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **5.44** | 90 | — | [responses](benchmarks/results/responses/20260427_185648/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **5.40** | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **5.40** | 103 | — | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **5.36** | 155 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **5.24** | 155 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **5.23** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **5.11** | 155 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **5.05** | 105 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **5.01** | 155 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **4.92** | 91 | — | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **4.74** | 155 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **4.56** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **4.46** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **4.31** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **4.28** | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **4.22** | 182 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | — |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **4.15** | 91 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **4.14** | 103 | — | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **3.81** | 81 | — | [responses](benchmarks/results/responses/20260503_125944/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **3.77** | 106 | — | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **3.61** | 91 | — | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **3.43** | 167 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **3.16** | 103 | — | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **2.99** | 91 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **2.75** | 122 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260425_145813/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **2.39** | 150 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **2.06** | 182 | — | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **1.44** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **1.13** | 103 | — | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.00** | 91 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 94 | — | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 91 | — | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **0.00** | 91 | — | — |

#### Mejor calidad pura (sin considerar costo ni velocidad)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.69** | 103 | — | [responses](benchmarks/results/responses/20260602_125445_2513153/) |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **8.65** | 101 | — | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **8.62** | 101 | — | — |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.57** | 98 | — | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **8.55** | 82 | — | — |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **8.47** | 103 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **8.44** | 98 | — | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.39** | 103 | — | — |
| `claude-fable-5` | ❌  | $10.0/50.0 | **8.38** | 103 | — | [responses](benchmarks/results/responses/20260609_144836_25113/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **8.37** | 105 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.34** | 133 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.22** | 103 | — | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **8.22** | 103 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **8.22** | 89 | — | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **8.21** | 135 | — | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **8.19** | 103 | — | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **8.18** | 87 | — | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.14** | 99 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **8.14** | 97 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **8.14** | 100 | — | — |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **8.13** | 103 | — | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **8.13** | 103 | — | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **8.12** | 103 | — | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **8.12** | 103 | — | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.11** | 103 | — | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.08** | 103 | — | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.08** | 182 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **8.07** | 97 | — | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **8.05** | 74 | — | [responses](benchmarks/results/responses/20260429_210054/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **8.04** | 86 | — | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **8.04** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.04** | 246 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **8.03** | 169 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **8.02** | 90 | — | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **8.01** | 115 | — | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.01** | 103 | — | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.99** | 103 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.98** | 68 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **7.97** | 90 | — | [responses](benchmarks/results/responses/20260427_185648/) |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **7.96** | 90 | — | — |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **7.93** | 103 | — | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.93** | 134 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260602_135955_2529872/) |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **7.89** | 88 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.89** | 155 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.87** | 135 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **7.85** | 86 | — | [responses](benchmarks/results/responses/20260602_125451_2513176/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.85** | 105 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **7.83** | 103 | — | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.83** | 91 | — | — |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **7.81** | 103 | — | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.81** | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.80** | 104 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260424_053942/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.79** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.79** | 103 | — | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.76** | 138 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260625_172532_3007190/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **7.75** | 91 | — | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **7.73** | 91 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **7.72** | 103 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.72** | 167 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.72** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **7.68** | 103 | — | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **7.68** | 182 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | — |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **7.65** | 103 | — | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.65** | 155 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `llama-3.1-8b-instant` | ✅ Llama Community | $0.05/0.08 | **7.61** | 100 | — | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **7.61** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.60** | 91 | — | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.57** | 155 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.56** | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.55** | 103 | — | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **7.55** | 106 | — | — |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **7.52** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **7.52** | 91 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **7.51** | 99 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.49** | 155 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.47** | 81 | — | [responses](benchmarks/results/responses/20260503_125944/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **7.39** | 103 | — | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.37** | 155 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.36** | 91 | — | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.30** | 167 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **7.27** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.17** | 91 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.09** | 150 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **6.97** | 122 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260425_145813/) |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **6.94** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.89** | 182 | — | — |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **6.85** | 103 | — | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.52** | 91 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **6.27** | 91 | — | — |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **5.50** | 94 | — | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **5.29** | 91 | — | — |

#### Mejor coding

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **8.67** | 169 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **8.46** | 103 | — | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **8.41** | 99 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.39** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.33** | 103 | — | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `llama-3.1-8b-instant` | ✅ Llama Community | $0.05/0.08 | **8.24** | 100 | — | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.19** | 133 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.15** | 103 | — | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **8.12** | 155 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.09** | 103 | — | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **8.03** | 155 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **8.02** | 103 | — | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **8.02** | 103 | — | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **8.01** | 91 | — | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **8.01** | 167 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **8.00** | 115 | — | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **8.00** | 103 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **8.00** | 86 | — | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.97** | 155 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.96** | 104 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260424_053942/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.96** | 135 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.96** | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **7.95** | 91 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **7.93** | 103 | — | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.90** | 155 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.87** | 103 | — | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.82** | 134 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260602_135955_2529872/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.81** | 103 | — | — |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **7.80** | 103 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.78** | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **7.76** | 97 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **7.73** | 103 | — | — |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **7.72** | 88 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.70** | 99 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.70** | 68 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.69** | 91 | — | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.68** | 103 | — | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **7.68** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **7.66** | 103 | — | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.66** | 138 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260625_172532_3007190/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.65** | 105 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **7.64** | 98 | — | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **7.64** | 103 | — | — |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **7.63** | 103 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.62** | 91 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.55** | 98 | — | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.55** | 103 | — | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.52** | 74 | — | [responses](benchmarks/results/responses/20260429_210054/) |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **7.52** | 90 | — | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **7.49** | 86 | — | [responses](benchmarks/results/responses/20260602_125451_2513176/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.44** | 167 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.44** | 150 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.43** | 103 | — | [responses](benchmarks/results/responses/20260602_125445_2513153/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.42** | 122 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260425_145813/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.42** | 103 | — | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.41** | 81 | — | [responses](benchmarks/results/responses/20260503_125944/) |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **7.39** | 89 | — | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **7.35** | 135 | — | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.34** | 82 | — | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **7.33** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.33** | 101 | — | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **7.33** | 103 | — | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.32** | 105 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | — |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **7.30** | 90 | — | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.30** | 182 | — | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.29** | 155 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.29** | 182 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.27** | 103 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **7.27** | 97 | — | — |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **7.25** | 91 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **7.23** | 90 | — | [responses](benchmarks/results/responses/20260427_185648/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.21** | 91 | — | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.14** | 91 | — | — |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **7.12** | 101 | — | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.12** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.11** | 103 | — | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **7.10** | 182 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **7.07** | 87 | — | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.06** | 246 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **6.99** | 94 | — | — |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **6.97** | 100 | — | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.94** | 106 | — | — |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **6.89** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `claude-fable-5` | ❌  | $10.0/50.0 | **6.89** | 103 | — | [responses](benchmarks/results/responses/20260609_144836_25113/) |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **6.86** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.75** | 103 | — | — |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **6.66** | 103 | — | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.46** | 91 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **6.39** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **6.26** | 91 | — | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **5.77** | 91 | — | — |

#### Mejor razonamiento

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **8.61** | 169 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **8.29** | 103 | — | — |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **8.23** | 103 | — | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **8.22** | 155 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **8.16** | 155 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **8.14** | 103 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.12** | 103 | — | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.11** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.09** | 133 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.07** | 103 | — | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **8.06** | 104 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260424_053942/) |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **8.05** | 103 | — | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.03** | 99 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **8.03** | 155 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **8.00** | 98 | — | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.97** | 103 | — | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.91** | 103 | — | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **7.91** | 91 | — | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **7.90** | 115 | — | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.90** | 138 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260625_172532_3007190/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.90** | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **7.89** | 97 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.84** | 103 | — | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **7.83** | 99 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.81** | 86 | — | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.79** | 167 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **7.78** | 89 | — | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **7.78** | 103 | — | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.77** | 103 | — | — |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **7.77** | 103 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **7.72** | 86 | — | [responses](benchmarks/results/responses/20260602_125451_2513176/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.71** | 135 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.71** | 105 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.70** | 68 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **7.69** | 101 | — | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.68** | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **7.66** | 100 | — | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.66** | 101 | — | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.64** | 103 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.64** | 134 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260602_135955_2529872/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.63** | 91 | — | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **7.62** | 91 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.62** | 103 | — | — |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **7.57** | 90 | — | — |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **7.57** | 90 | — | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.56** | 103 | — | [responses](benchmarks/results/responses/20260602_125445_2513153/) |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.50** | 98 | — | — |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.50** | 103 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **7.49** | 88 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.48** | 155 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `claude-fable-5` | ❌  | $10.0/50.0 | **7.47** | 103 | — | [responses](benchmarks/results/responses/20260609_144836_25113/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **7.44** | 97 | — | — |
| `llama-3.1-8b-instant` | ✅ Llama Community | $0.05/0.08 | **7.41** | 100 | — | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.40** | 74 | — | [responses](benchmarks/results/responses/20260429_210054/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.39** | 91 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.37** | 103 | — | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.33** | 246 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **7.30** | 103 | — | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.28** | 103 | — | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.25** | 82 | — | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **7.21** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.17** | 155 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.16** | 182 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.16** | 105 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **7.13** | 90 | — | [responses](benchmarks/results/responses/20260427_185648/) |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **7.03** | 87 | — | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.96** | 106 | — | — |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **6.96** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **6.89** | 122 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260425_145813/) |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **6.88** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.86** | 135 | — | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.83** | 182 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.79** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **6.46** | 91 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **6.40** | 103 | — | — |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **6.31** | 103 | — | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.22** | 150 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.19** | 182 | — | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.09** | 103 | — | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **6.09** | 167 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **5.97** | 81 | — | [responses](benchmarks/results/responses/20260503_125944/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **5.95** | 91 | — | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **5.94** | 103 | — | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.84** | 91 | — | — |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **5.65** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **4.98** | 91 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **4.45** | 91 | — | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **4.01** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **3.85** | 103 | — | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **3.73** | 91 | — | — |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **3.35** | 94 | — | — |

#### Mejor contenido/marketing

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **8.37** | 99 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **8.23** | 103 | — | — |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **8.19** | 103 | — | — |
| `llama-3.1-8b-instant` | ✅ Llama Community | $0.05/0.08 | **8.17** | 100 | — | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.15** | 133 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **8.15** | 169 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.09** | 103 | — | — |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **8.08** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.07** | 103 | — | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.07** | 103 | — | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **8.06** | 115 | — | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.05** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **8.01** | 91 | — | — |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **8.01** | 103 | — | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **8.00** | 91 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.97** | 103 | — | — |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **7.97** | 103 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.96** | 135 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.96** | 103 | — | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.95** | 86 | — | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **7.95** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **7.94** | 103 | — | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.93** | 103 | — | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.88** | 104 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260424_053942/) |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.88** | 99 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **7.87** | 103 | — | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.85** | 103 | — | — |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **7.83** | 97 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.80** | 155 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.78** | 103 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **7.78** | 103 | — | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.77** | 155 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.76** | 105 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **7.76** | 98 | — | — |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **7.70** | 90 | — | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.68** | 103 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **7.67** | 103 | — | — |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **7.66** | 88 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **7.66** | 103 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.65** | 155 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **7.64** | 100 | — | — |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **7.63** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **7.61** | 86 | — | [responses](benchmarks/results/responses/20260602_125451_2513176/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.61** | 91 | — | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.59** | 91 | — | — |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.59** | 68 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **7.57** | 90 | — | — |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **7.55** | 89 | — | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.54** | 91 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.51** | 167 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **7.50** | 101 | — | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.50** | 103 | — | [responses](benchmarks/results/responses/20260602_125445_2513153/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.50** | 134 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260602_135955_2529872/) |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **7.50** | 91 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.48** | 155 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.46** | 138 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260625_172532_3007190/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.44** | 122 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260425_145813/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.35** | 167 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.34** | 98 | — | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.34** | 91 | — | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.30** | 82 | — | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.27** | 103 | — | — |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **7.25** | 103 | — | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.24** | 74 | — | [responses](benchmarks/results/responses/20260429_210054/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **7.21** | 97 | — | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **7.20** | 135 | — | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.20** | 101 | — | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.20** | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **7.19** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **7.16** | 103 | — | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.15** | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.15** | 105 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | — |
| `claude-fable-5` | ❌  | $10.0/50.0 | **7.14** | 103 | — | [responses](benchmarks/results/responses/20260609_144836_25113/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.09** | 155 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.02** | 182 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **7.01** | 90 | — | [responses](benchmarks/results/responses/20260427_185648/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **7.00** | 106 | — | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **6.97** | 87 | — | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.87** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.84** | 246 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.84** | 182 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.76** | 182 | — | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.63** | 103 | — | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.52** | 103 | — | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **6.52** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.41** | 150 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **6.39** | 81 | — | [responses](benchmarks/results/responses/20260503_125944/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **5.93** | 91 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **5.61** | 91 | — | — |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **5.45** | 94 | — | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **4.53** | 91 | — | — |

#### Mejor relación calidad/costo (pesos v2.9: 60% quality, 20% costo, 10% speed, 10% latency)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **8.66** | 101 | — | — |
| `llama-3.1-8b-instant` | ✅ Llama Community | $0.05/0.08 | **8.61** | 100 | — | — |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.11** | 98 | — | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **8.09** | 98 | — | — |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **7.93** | 82 | — | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.89** | 133 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.81** | 101 | — | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.72** | 103 | — | [responses](benchmarks/results/responses/20260602_125445_2513153/) |
| `claude-fable-5` | ❌  | $10.0/50.0 | **7.64** | 103 | — | [responses](benchmarks/results/responses/20260609_144836_25113/) |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **7.55** | 115 | — | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.52** | 103 | — | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.49** | 103 | — | — |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **7.33** | 103 | — | — |
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **7.32** | 169 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **7.29** | 103 | — | — |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **7.10** | 103 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.08** | 103 | — | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.08** | 103 | — | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.07** | 103 | — | — |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **6.82** | 103 | — | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.75** | 105 | — | [responses](benchmarks/results/responses/20260602_135949_2529847/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **6.73** | 122 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260425_145813/) |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **6.70** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **6.68** | 103 | — | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **6.63** | 99 | — | [responses](benchmarks/results/responses/20260602_135951_2529854/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **6.61** | 86 | — | [responses](benchmarks/results/responses/20260605_161554_3529029/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **6.58** | 103 | — | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.56** | 135 | — | — |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **6.48** | 103 | — | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.41** | 103 | — | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **6.41** | 103 | — | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **6.37** | 103 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260503_074942/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.36** | 182 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **6.34** | 155 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **6.31** | 135 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **6.13** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **6.13** | 100 | — | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **6.11** | 103 | — | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.08** | 246 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.04** | 74 | — | [responses](benchmarks/results/responses/20260429_210054/) |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **6.03** | 68 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **6.00** | 97 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **5.98** | 99 | — | [responses](benchmarks/results/responses/20260503_074942/) |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **5.88** | 103 | — | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **5.82** | 91 | — | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **5.79** | 134 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260602_135955_2529872/) |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **5.78** | 89 | — | — |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **5.76** | 103 | — | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **5.75** | 87 | — | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **5.74** | 167 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **5.73** | 155 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **5.70** | 91 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **5.69** | 88 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **5.65** | 97 | — | — |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **5.57** | 90 | — | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **5.50** | 103 | — | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **5.49** | 91 | — | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **5.48** | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260427_185648/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **5.26** | 104 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260424_053942/) |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **5.17** | 90 | — | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **5.15** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **5.12** | 103 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **5.11** | 105 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **4.94** | 91 | — | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **4.91** | 138 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260625_172532_3007190/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **4.90** | 103 | — | — |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **4.90** | 90 | — | [responses](benchmarks/results/responses/20260427_185648/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **4.89** | 86 | — | [responses](benchmarks/results/responses/20260602_125451_2513176/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **4.82** | 155 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **4.77** | 155 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **4.64** | 106 | — | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **4.62** | 91 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **4.59** | 103 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **4.57** | 155 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260602_125441_2513137/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **4.43** | 182 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **4.40** | 155 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **4.30** | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **4.26** | 91 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **4.04** | 103 | — | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **3.84** | 91 | — | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **3.65** | 81 | — | [responses](benchmarks/results/responses/20260503_125944/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **3.33** | 167 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **3.17** | 150 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **2.59** | 91 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **2.34** | 182 | — | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **1.86** | 102 | — | [responses](benchmarks/results/responses/20260429_165839/) |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **1.73** | 103 | — | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **1.04** | 91 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 94 | — | — |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 91 | — | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **0.00** | 91 | — | — |

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
