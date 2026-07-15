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
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.23** | 129 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **8.04** | 127 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.85** | 123 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.72** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_180704_98902/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.63** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.53** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.47** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.33** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.19** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.11** | 286 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.03** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.00** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_164558_56411/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **6.99** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.96** | 165 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260714_163618_51389/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.93** | 128 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **6.90** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **6.89** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **6.84** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.58** | 176 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **6.55** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.51** | 127 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **6.49** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.41** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.38** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **6.36** | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **6.34** | 163 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.30** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **6.27** | 186 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_142058_71509/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.25** | 167 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **6.12** | 172 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_180509_98060/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **5.95** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **5.92** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **5.86** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **5.84** | 131 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **5.75** | 179 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **5.58** | 169 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **5.58** | 125 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **5.52** | 179 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.50** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **5.49** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **5.45** | 131 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_142058_71510/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **5.43** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.27** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **5.25** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **5.07** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **5.01** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **4.85** | 140 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **4.77** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **4.71** | 132 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **4.68** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **4.61** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **4.32** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **3.97** | 140 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **3.83** | 157 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **3.78** | 121 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **3.55** | 191 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **3.50** | 162 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_180807_99667/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **3.38** | 112 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **3.33** | 157 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **3.04** | 139 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **2.86** | 131 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **1.93** | 152 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **1.86** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **1.49** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **1.39** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.50** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |

#### Mejor calidad pura (sin considerar costo ni velocidad)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.39** | 123 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **8.35** | 127 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.31** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **8.28** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_180704_98902/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.28** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.26** | 129 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.26** | 286 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **8.26** | 128 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **8.14** | 127 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.13** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **8.11** | 165 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260714_163618_51389/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **8.10** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.09** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **8.09** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **8.08** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **8.06** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_164558_56411/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **8.03** | 176 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.03** | 167 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.01** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **8.01** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **8.00** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.97** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.94** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **7.94** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.93** | 186 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_142058_71509/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.92** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.90** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.88** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **7.87** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.86** | 172 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_180509_98060/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.85** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.85** | 179 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.85** | 125 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.84** | 163 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.81** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.79** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.78** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.76** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **7.76** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.74** | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.74** | 169 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.74** | 179 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.73** | 131 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_142058_71510/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.69** | 131 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.68** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.63** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.63** | 140 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.62** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.60** | 132 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.60** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.59** | 121 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.58** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **7.54** | 112 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.49** | 140 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.46** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.45** | 191 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.45** | 162 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_180807_99667/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.36** | 139 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.30** | 157 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.26** | 157 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.22** | 131 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **7.18** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.17** | 152 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.16** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.99** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **6.93** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |

#### Mejor coding

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.18** | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.95** | 169 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.89** | 176 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.88** | 179 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.85** | 157 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.80** | 157 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.73** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.64** | 172 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_180509_98060/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.62** | 179 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.52** | 163 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.45** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.44** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.43** | 152 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.43** | 186 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_142058_71509/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.42** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.41** | 139 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.35** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.33** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.31** | 191 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.30** | 131 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.29** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.28** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.28** | 167 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.25** | 131 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_142058_71510/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.25** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.20** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.17** | 131 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.13** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.11** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.10** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.09** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.08** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.06** | 162 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_180807_99667/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.04** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.04** | 125 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.03** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_164558_56411/) |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.00** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.98** | 140 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **6.96** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.95** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.94** | 112 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **6.94** | 132 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **6.93** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_180704_98902/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **6.84** | 127 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **6.81** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.81** | 286 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.79** | 165 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260714_163618_51389/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **6.78** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **6.78** | 129 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **6.78** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.76** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.75** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.74** | 121 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.72** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.71** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **6.71** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.68** | 127 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **6.67** | 123 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.61** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.60** | 128 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.56** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.41** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.29** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.26** | 140 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **5.94** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **5.90** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |

#### Mejor razonamiento

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.14** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.13** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.13** | 131 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **8.10** | 179 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **8.08** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.06** | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **8.03** | 157 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.99** | 179 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.98** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.92** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.88** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.87** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.85** | 186 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_142058_71509/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.84** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.82** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.80** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.79** | 169 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.77** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_164558_56411/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.68** | 176 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.67** | 131 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_142058_71510/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.66** | 132 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.62** | 172 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_180509_98060/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.62** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.60** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.59** | 163 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.53** | 129 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.50** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.48** | 157 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.47** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.43** | 131 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.41** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.40** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.37** | 139 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.31** | 127 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.29** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.29** | 286 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.17** | 167 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.16** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.14** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.13** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.13** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_180704_98902/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.04** | 123 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.02** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.02** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.99** | 128 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.96** | 112 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.89** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.84** | 165 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260714_163618_51389/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.82** | 140 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.80** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.77** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.62** | 121 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **6.61** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.54** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.46** | 140 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.38** | 127 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.30** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.22** | 152 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **6.09** | 191 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **5.97** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **5.95** | 125 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **5.86** | 162 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_180807_99667/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.84** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **5.00** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **4.98** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **4.85** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |

#### Mejor contenido/marketing

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.91** | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.74** | 157 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.69** | 163 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.67** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.61** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.61** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.60** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.59** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.57** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.55** | 179 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.54** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.54** | 131 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.53** | 179 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.51** | 169 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.49** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.48** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.48** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_164558_56411/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.45** | 157 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.43** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.43** | 172 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_180509_98060/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.42** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.41** | 139 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.40** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.39** | 186 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_142058_71509/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **7.36** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.35** | 191 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.34** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.34** | 125 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.33** | 129 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.29** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.28** | 131 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.24** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.20** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.19** | 131 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_142058_71510/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **7.16** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.16** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.16** | 165 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260714_163618_51389/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.15** | 176 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.12** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.09** | 167 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.04** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_180704_98902/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.04** | 140 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.03** | 123 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.02** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.01** | 132 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **7.00** | 112 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **6.99** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.99** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **6.96** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.85** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **6.79** | 127 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.79** | 140 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.75** | 127 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.71** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.70** | 121 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.68** | 286 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **6.68** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.67** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.67** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.66** | 128 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **6.47** | 162 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_180807_99667/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.42** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.41** | 152 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.29** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.26** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **5.51** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |

#### Mejor relación calidad/costo (pesos v2.9: 60% quality, 20% costo, 10% speed, 10% latency)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.78** | 129 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.31** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **8.15** | 127 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.05** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.91** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.71** | 286 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.65** | 123 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.61** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_180704_98902/) |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.57** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.38** | 128 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.37** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.32** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.16** | 127 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.14** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **6.97** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **6.89** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.86** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.69** | 176 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.59** | 167 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.55** | 165 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260714_163618_51389/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **6.48** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_164558_56411/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **6.43** | 163 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.36** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **6.31** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **6.31** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.27** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **6.26** | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **6.05** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **6.00** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **5.88** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **5.81** | 169 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **5.79** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **5.68** | 131 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **5.55** | 186 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_142058_71509/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **5.53** | 172 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_180509_98060/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **5.41** | 125 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **5.38** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **5.34** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **5.34** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.25** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **5.21** | 131 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_142058_71510/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **5.20** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **5.17** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.07** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **4.99** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **4.92** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **4.89** | 179 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **4.85** | 179 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **4.77** | 140 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **4.66** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **4.57** | 132 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **4.54** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **4.30** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `gpt-5.5` | ❌  | $5.0/30.0 | **3.92** | 112 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **3.57** | 157 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **3.51** | 121 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **3.02** | 140 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **2.95** | 131 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **2.79** | 157 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **2.75** | 191 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **2.72** | 162 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_180807_99667/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **2.10** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **2.09** | 139 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **1.92** | 152 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **1.80** | 131 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.63** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |

#### Vía suscripción Claude — plano propio (comparables entre sí)

> Medidos aprovechando la **suscripción de Claude Code** (costo marginal $0), todos por el mismo camino → **comparables entre ellos**. Ese camino arrastra ~8.8K tokens de scaffolding del CLI y **deprime la nota**: en los 2 modelos medidos por ambos caminos, la calidad por API dio **+0.15 y +0.22 más** que por suscripción. Leé estos números como **piso conservador**, no como techo — y no los compares 1:1 contra la tabla principal (la latencia por CLI es 2.5-4× peor y no es del modelo). Sirven para la pregunta de quien ya paga el plan: *¿qué modelo uso dentro de mi suscripción?*

| Modelo | Calidad (piso) | Velocidad | Runs | Per-model MD | Responses |
|---|---:|---:|---:|---|---|
| `claude-fable-5` | **8.38** | 58 tok/s | 114 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260713_075422_74587/) |
| `claude-opus-4-7` | **8.13** | 55 tok/s | 92 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `claude-opus-4-8` | **8.09** | 60 tok/s | 132 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `claude-sonnet-4-6` | **7.98** | 50 tok/s | 108 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `claude-haiku-4-5` | **7.92** | 102 tok/s | 108 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |

#### Variantes de proveedor (40 mediciones)

> El mismo modelo servido por otra infraestructura (Groq, NVIDIA NIM, Ollama Cloud, API directa del proveedor, self-hosted). **No compiten acá** — comparar infra contra infra es otra pregunta, y tiene su propia página: [el proveedor te cambia el modelo](https://benchmarks.cristiantala.com/mismo-modelo-distinto-proveedor/). El caso extremo medido: el mismo Qwen 3.5 397B da **7.96 en NVIDIA NIM y 5.46 en Ollama Cloud** — 2.5 puntos por la infraestructura, no por el modelo.

#### En evaluación — muestra parcial (<50 runs, NO rankeados)

> Estos modelos tienen menos runs que el piso del ranking, así que su score es **indicativo, no comparable**: con pocas muestras la varianza permite que un modelo quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** en las tablas de arriba hasta completar la cobertura.

| Modelo | OS | $ in/out | Score (indicativo) | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.97** | 12 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.79** | 12 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.77** | 12 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260714_133916_48506/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.35 | **7.77** | 19 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.2/0.8 | **7.50** | 12 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.33** | 12 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.09** | 12 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.97** | 12 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.96** | 12 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **6.83** | 12 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.73** | 12 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.60** | 12 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **5.79** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **5.36** | 2 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **3.90** | 121 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260714_133916_48506/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **0.38** | 205 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260714_181940_6188/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.375/2.025 | **0.00** | 35 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260714_135305_55786/) |

#### Retirados — el proveedor ya no los sirve

> **Estos modelos ya no se pueden llamar.** El endpoint devuelve *deprecated* o *no endpoints found*. Sus números son reales y quedan acá por transparencia (alimentan el análisis histórico), pero **están fuera del ranking y de las recomendaciones**: un modelo que no puedes usar no es un candidato. Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera.

| Modelo | OS | $ in/out | Score (histórico) | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **8.62** | 161 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **6.62** | 99 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `qwen/qwen-2.5-72b-instruct` | ✅ Apache 2.0 | $0.36/0.4 | **6.24** | 76 | [per-model](benchmarks/results/per-model/qwen_qwen-2_5-72b-instruct.md) | — |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **6.03** | 99 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **5.19** | 84 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **3.75** | 99 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **3.72** | 99 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **3.44** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **3.35** | 98 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `qwen3.5:cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 87 | [per-model](benchmarks/results/per-model/qwen3_5_cloud.md) | — |

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
