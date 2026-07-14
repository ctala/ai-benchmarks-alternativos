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
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.76** | 124 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **8.40** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_071245_48066/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.37** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.30** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.27** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **8.24** | 122 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.97** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0/0 | **7.91** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.87** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.74** | 123 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_171017_4861/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.71** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.47** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.29** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.23** | 174 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.16** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.13** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.06** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.06** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.87** | 117 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **6.86** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.75** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.67** | 281 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **6.59** | 166 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_065727_39949/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.57** | 162 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **6.32** | 158 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.30** | 171 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.26** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.26** | 115 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **6.26** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.25** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ❌ NVIDIA Open License | $0/0 | **6.24** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.01** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **5.85** | 174 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.64** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **5.61** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **5.57** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **5.54** | 151 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **5.53** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **5.49** | 115 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **5.42** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **5.36** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **5.26** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.21** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **5.20** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **4.84** | 119 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **4.73** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **4.71** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **4.70** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **4.58** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **4.43** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **4.28** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **4.23** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **4.18** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **3.80** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **3.11** | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **2.97** | 174 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **1.92** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **1.69** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **1.39** | 102 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_060938_14793/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **0.89** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **0.81** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **0.71** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **0.00** | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.00** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |

#### Mejor calidad pura (sin considerar costo ni velocidad)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.39** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **8.37** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_071245_48066/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **8.36** | 122 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.31** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.30** | 124 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **8.26** | 117 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **8.25** | 123 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_171017_4861/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.24** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.23** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **8.20** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.20** | 281 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.18** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **8.17** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **8.12** | 115 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **8.11** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.11** | 162 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **8.09** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **8.09** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **8.09** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **8.08** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **8.07** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.06** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0/0 | **8.05** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **8.03** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **8.00** | 171 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.96** | 158 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.95** | 166 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_065727_39949/) |
| `nvidia/nemotron-nano-9b-v2:free` | ❌ NVIDIA Open License | $0/0 | **7.95** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **7.93** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.90** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.90** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.90** | 174 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.88** | 174 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.88** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.88** | 115 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.87** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.85** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.79** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.78** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.78** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.76** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **7.74** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.72** | 151 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.68** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.67** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.67** | 119 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.67** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.64** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.63** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.62** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **7.59** | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.58** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.58** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.57** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.55** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.46** | 174 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.27** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.25** | 102 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_060938_14793/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **7.23** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.19** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.16** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **7.01** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.99** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **6.80** | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |

#### Mejor coding

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.18** | 174 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.89** | 171 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.88** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0/0 | **7.88** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.86** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.76** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.73** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.71** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.68** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.64** | 166 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_065727_39949/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.62** | 174 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.56** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.52** | 151 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.51** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `nvidia/nemotron-nano-9b-v2:free` | ❌ NVIDIA Open License | $0/0 | **7.47** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.46** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.43** | 158 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.42** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.41** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.39** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.37** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.35** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_071245_48066/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.35** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.30** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.30** | 174 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.29** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.28** | 162 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.25** | 119 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.20** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **7.19** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.17** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.15** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **7.11** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.10** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.09** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.04** | 115 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.00** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.00** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **6.99** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.98** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **6.87** | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **6.85** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **6.84** | 122 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **6.81** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.81** | 281 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.80** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.79** | 123 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_171017_4861/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **6.78** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **6.78** | 124 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.75** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.74** | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.71** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **6.71** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.68** | 115 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **6.67** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.61** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.61** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.60** | 117 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **6.56** | 102 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_060938_14793/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.56** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.41** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.29** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **6.25** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **5.94** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |

#### Mejor razonamiento

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0/0 | **8.15** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.14** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.13** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.13** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **8.10** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.05** | 174 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ❌ NVIDIA Open License | $0/0 | **7.99** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.99** | 174 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.90** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.88** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.87** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.85** | 158 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.84** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.82** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.80** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.77** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.68** | 171 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.67** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.67** | 119 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.62** | 166 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_065727_39949/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.62** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.60** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.59** | 151 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.53** | 124 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.50** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.47** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.43** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.41** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.40** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.37** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.31** | 122 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.29** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.29** | 281 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.17** | 162 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.16** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.14** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.13** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.13** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_071245_48066/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.11** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.09** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.04** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.02** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.02** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.99** | 117 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.89** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.84** | 123 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_171017_4861/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.82** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **6.80** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.77** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.61** | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **6.61** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.54** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.54** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.38** | 115 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **6.33** | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.30** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.21** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **6.09** | 174 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **5.95** | 115 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **5.84** | 102 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_060938_14793/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.84** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **5.00** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **4.98** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **4.85** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |

#### Mejor contenido/marketing

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.91** | 174 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0/0 | **7.77** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.69** | 151 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.61** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.61** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **7.60** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.59** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **7.57** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **7.55** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.54** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.54** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **7.53** | 174 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **7.49** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.48** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **7.48** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.43** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **7.43** | 166 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_065727_39949/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.42** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **7.41** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **7.40** | 158 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **7.40** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `nvidia/nemotron-nano-9b-v2:free` | ❌ NVIDIA Open License | $0/0 | **7.36** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.35** | 174 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.34** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **7.34** | 115 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **7.33** | 124 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.29** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.29** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.28** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **7.24** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **7.20** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.20** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **7.19** | 119 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.18** | 123 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_171017_4861/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **7.16** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **7.16** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.15** | 171 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.12** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.09** | 162 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.04** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_071245_48066/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.03** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.02** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **7.01** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **6.99** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.99** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **6.96** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **6.94** | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.85** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.80** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **6.79** | 122 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.79** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.75** | 115 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.71** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **6.70** | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.68** | 281 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **6.68** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.67** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.67** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **6.66** | 117 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **6.42** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.29** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.26** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **5.92** | 102 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_060938_14793/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **5.51** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |

#### Mejor relación calidad/costo (pesos v2.9: 60% quality, 20% costo, 10% speed, 10% latency)

| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0/0 | **10.00** | 94 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | — |
| `nvidia/nemotron-nano-9b-v2:free` | ❌ NVIDIA Open License | $0/0 | **8.95** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `openai/gpt-5.6-luna` | ❌  | $1.0/6.0 | **8.64** | 124 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | — |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.92** | 119 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | — |
| `z-ai/glm-5.2` | ✅ MIT | $0.95/3.0 | **7.79** | 122 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | — |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.73** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/20260714_071245_48066/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.66** | 119 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | — |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.60** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.45** | 194 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | — |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.45** | 145 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.37** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.27** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `openai/gpt-5.6-terra` | ❌  | $2.5/15.0 | **7.27** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | — |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.02** | 281 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | — |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.04/6.24 | **7.00** | 117 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | — |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **6.93** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | — |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.87** | 123 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/20260713_171017_4861/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **6.86** | 174 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | — |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.79** | 115 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.4/0.4 | **6.77** | 119 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.75** | 162 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.385/2.45 | **6.55** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `qwen/qwen3.7-max` | ❌ Proprietary | $2.5/7.5 | **6.47** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | — |
| `minimax/minimax-m2.5` | ✅ MIT | $0.15/0.9 | **6.40** | 119 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | — |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.15/0.3 | **6.38** | 128 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/20260714_075333_69162/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.27** | 171 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.95/3.15 | **6.06** | 119 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.214/0.322 | **6.03** | 119 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.00** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | — |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.5/1.0 | **5.85** | 166 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/20260714_065727_39949/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **5.75** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **5.57** | 151 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | — |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.49** | 99 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | — |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.2/0.8 | **5.47** | 158 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **5.42** | 119 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | — |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.29/3.2 | **5.39** | 147 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | — |
| `xiaomi/mimo-v2.5-pro` | ❌  | $1.0/3.0 | **5.37** | 115 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | — |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **5.18** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **5.15** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **5.13** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | — |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **5.06** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.4/2.0 | **5.05** | 119 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | — |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.18/1.07 | **5.04** | 175 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | — |
| `deepseek/deepseek-chat` | ❌  | $0.14/0.28 | **4.96** | 174 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | — |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.2/0.6 | **4.91** | 174 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/20260714_080950_77433/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **4.85** | 133 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | — |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **4.80** | 119 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `mistralai/devstral-2512` | ✅ Apache 2.0 | $0.4/2.0 | **4.68** | 119 | [per-model](benchmarks/results/per-model/mistralai_devstral-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **4.48** | 119 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **4.43** | 106 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.5/2.2 | **4.42** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | — |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **4.20** | 119 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | — |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.73/3.49 | **4.06** | 206 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **3.72** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | — |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.74/3.5 | **3.39** | 119 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **2.73** | 174 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | — |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **2.10** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | — |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **2.09** | 119 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | — |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.02/0.03 | **2.08** | 119 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | — |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **2.07** | 119 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | — |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.1/0.5 | **1.42** | 118 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | — |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **1.38** | 102 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_060938_14793/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.69** | 119 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | — |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **0.46** | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |

#### En evaluación — muestra parcial (<50 runs, NO rankeados)

> Estos modelos tienen menos runs que el piso del ranking, así que su score es **indicativo, no comparable**: con pocas muestras la varianza permite que un modelo quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** en las tablas de arriba hasta completar la cobertura.

| Modelo | OS | $ in/out | Score (indicativo) | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `MiniMax-M2.7` | ❌  | $0.3/1.2 | **10.00** | 23 | [per-model](benchmarks/results/per-model/MiniMax-M2_7.md) | — |
| `MiniMax-M2.7-highspeed` | ❌  | $0.3/1.2 | **10.00** | 23 | [per-model](benchmarks/results/per-model/MiniMax-M2_7-highspeed.md) | — |
| `mistralai/mistral-nemotron` | ✅ Apache 2.0 | $0.3/1.2 | **8.27** | 8 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemotron.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **8.19** | 10 | [per-model](benchmarks/results/per-model/deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_060938_14793/) |
| `deepseek-ai/deepseek-v4-pro` | ✅ MIT | $0.435/0.87 | **7.98** | 2 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/20260714_060938_14793/) |
| `claude-fable-5` | ❌  | $10.0/50.0 | **7.81** | 99 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/20260713_075422_74587/) |
| `deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **7.67** | 12 | [per-model](benchmarks/results/per-model/deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `google/gemma-4-31b-it` | ✅ Apache 2.0 | $0.3/0.6 | **7.41** | 7 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.35 | **7.41** | 7 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `gemma4:31b` | ✅ Gemma Terms | $0.12/0.37 | **7.12** | 85 | [per-model](benchmarks/results/per-model/gemma4_31b.md) | — |
| `qwen3.6:27b` | ✅ Apache 2.0 | $0.29/3.2 | **6.98** | 4 | [per-model](benchmarks/results/per-model/qwen3_6_27b.md) | — |
| `gemma-4-31B-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.12/0.37 | **6.83** | 99 | [per-model](benchmarks/results/per-model/gemma-4-31B-it-Q4_K_M_gguf.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0` | ✅ Apache 2.0 | $0.06/0.33 | **6.48** | 96 | [per-model](benchmarks/results/per-model/hf_co_unsloth_diffusiongemma-26B-A4B-it-GGUF_Q8_0.md) | — |
| `mistralai/devstral-2-123b-instruct-2512` | ✅ Apache 2.0 | $0.4/2.0 | **6.44** | 64 | [per-model](benchmarks/results/per-model/mistralai_devstral-2-123b-instruct-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `MiniMax-M3` | ❌  | $0.3/1.2 | **6.28** | 109 | [per-model](benchmarks/results/per-model/MiniMax-M3.md) | [responses](benchmarks/results/responses/20260713_171017_4861/) |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **6.16** | 99 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `mistralai/mistral-large-3-675b-instruct-2512` | ✅ Apache 2.0 | $2.0/6.0 | **6.10** | 83 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-3-675b-instruct-2512.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `claude-opus-4-7` | ❌  | $5.0/25.0 | **6.08** | 92 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | — |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.39/2.34 | **6.07** | 97 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | — |
| `gemma-4-12b-it-Q4_K_M.gguf` | ✅ Gemma Terms | $0.05/0.2 | **5.99** | 99 | [per-model](benchmarks/results/per-model/gemma-4-12b-it-Q4_K_M_gguf.md) | — |
| `claude-haiku-4-5` | ❌  | $1.0/5.0 | **5.93** | 108 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | — |
| `claude-opus-4-8` | ❌  | $5.0/25.0 | **5.85** | 101 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | — |
| `deepseek-ai/deepseek-v4-flash` | ✅ MIT | $0.098/0.197 | **5.79** | 83 | [per-model](benchmarks/results/per-model/deepseek-ai_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/20260713_192644_77095/) |
| `mistralai/magistral-small-2506` | ✅ Apache 2.0 | $0.5/1.5 | **5.67** | 6 | [per-model](benchmarks/results/per-model/mistralai_magistral-small-2506.md) | — |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **5.62** | 97 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | — |
| `gpt-4.1` | ❌  | $2.0/8.0 | **5.48** | 152 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | — |
| `llama-3.3-70b-versatile` | ✅ Llama Community | $0.59/0.79 | **5.48** | 85 | [per-model](benchmarks/results/per-model/llama-3_3-70b-versatile.md) | — |
| `z-ai/glm-5.1` | ✅ MIT | $0.98/3.08 | **5.48** | 97 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | — |
| `claude-sonnet-4-6` | ❌  | $3.0/15.0 | **5.46** | 108 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | — |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.12/0.37 | **5.37** | 92 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/20260602_125449_2513169/) |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **5.36** | 2 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `z-ai/glm5` | ✅ MIT | $0.98/3.08 | **5.34** | 86 | [per-model](benchmarks/results/per-model/z-ai_glm5.md) | [responses](benchmarks/results/responses/20260714_085112_98609/) |
| `mistralai/ministral-14b-instruct-2512` | ✅ Apache 2.0 | $0.1/0.4 | **5.23** | 86 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-instruct-2512.md) | — |
| `meta-llama/llama-4-scout-17b-16e-instruct` | ✅ Llama Community | $0.11/0.34 | **4.92** | 97 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout-17b-16e-instruct.md) | — |
| `nemotron-3-super:120b` | ❌ NVIDIA Open License | $0.09/0.45 | **4.48** | 86 | [per-model](benchmarks/results/per-model/nemotron-3-super_120b.md) | — |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **4.09** | 152 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | — |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | ✅ NVIDIA Open License | $0.1/0.4 | **4.05** | 87 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning.md) | — |
| `nemotron3:33b-q4_K_M` | ✅ NVIDIA Open License | $0.09/0.45 | **3.90** | 99 | [per-model](benchmarks/results/per-model/nemotron3_33b-q4_K_M.md) | — |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **3.82** | 152 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | — |
| `mimo-v2.5` | ❌ Xiaomi Commercial | $0.07/0.07 | **2.90** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5.md) | — |
| `nvidia/nvidia-nemotron-nano-9b-v2` | ❌ NVIDIA Open License | $0.05/0.2 | **2.80** | 87 | [per-model](benchmarks/results/per-model/nvidia_nvidia-nemotron-nano-9b-v2.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `llama-3.1-8b-instant` | ✅ Llama Community | $0.05/0.08 | **2.62** | 85 | [per-model](benchmarks/results/per-model/llama-3_1-8b-instant.md) | — |
| `mimo-v2.5-pro` | ❌ Xiaomi Commercial | $0.14/0.14 | **2.52** | 87 | [per-model](benchmarks/results/per-model/mimo-v2_5-pro.md) | — |
| `gpt-oss:120b-cloud` | ✅ Apache 2.0 | $0.039/0.18 | **2.40** | 87 | [per-model](benchmarks/results/per-model/gpt-oss_120b-cloud.md) | — |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | ✅ NVIDIA Open Model | $0.1/0.4 | **1.91** | 92 | [per-model](benchmarks/results/per-model/nvidia_llama-3_3-nemotron-super-49b-v1_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **1.54** | 97 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | — |
| `gpt-5.4` | ❌  | $5.0/15.0 | **1.04** | 152 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | — |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.075/0.3 | **0.89** | 96 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/20260713_204935_20776/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.098/0.78 | **0.67** | 184 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.2/0.8 | **0.00** | 23 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `qwen3.5:397b-cloud` | ✅ Apache 2.0 | $0.39/2.34 | **0.00** | 87 | [per-model](benchmarks/results/per-model/qwen3_5_397b-cloud.md) | — |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **0.00** | 96 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.4/1.9 | **0.00** | 97 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |
| `stepfun-ai/step-3.5-flash` | ✅ Apache 2.0 | $1.0/3.0 | **0.00** | 87 | [per-model](benchmarks/results/per-model/stepfun-ai_step-3_5-flash.md) | — |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.375/2.025 | **0.00** | 23 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/20260714_063011_25831/) |

#### Retirados — el proveedor ya no los sirve

> **Estos modelos ya no se pueden llamar.** El endpoint devuelve *deprecated* o *no endpoints found*. Sus números son reales y quedan acá por transparencia (alimentan el análisis histórico), pero **están fuera del ranking y de las recomendaciones**: un modelo que no puedes usar no es un candidato. Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera.

| Modelo | OS | $ in/out | Score (histórico) | Runs | Per-model MD | Responses |
|---|---|---:|---:|---:|---|---|
| `mistralai/devstral-small` | ✅ Apache 2.0 | $0.1/0.3 | **9.03** | 144 | [per-model](benchmarks/results/per-model/mistralai_devstral-small.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `qwen/qwen-2.5-72b-instruct` | ✅ Apache 2.0 | $0.36/0.4 | **7.28** | 76 | [per-model](benchmarks/results/per-model/qwen_qwen-2_5-72b-instruct.md) | — |
| `x-ai/grok-4.1-fast` | ❌  | $0.2/0.5 | **5.89** | 87 | [per-model](benchmarks/results/per-model/x-ai_grok-4_1-fast.md) | — |
| `xiaomi/mimo-v2-flash` | ✅ MIT | $0.09/0.29 | **5.16** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-flash.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mistralai/devstral-medium` | ✅ Apache 2.0 | $0.4/2.0 | **4.89** | 84 | [per-model](benchmarks/results/per-model/mistralai_devstral-medium.md) | [responses](benchmarks/results/responses/20260430_200512/) |
| `xiaomi/mimo-v2-pro` | ❌ Proprietary | $1.0/3.0 | **2.74** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2-pro` | ✅ MIT | $0.07/0.07 | **1.94** | 87 | [per-model](benchmarks/results/per-model/mimo-v2-pro.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `xiaomi/mimo-v2-omni` | ❌  | $0.4/2.0 | **1.88** | 87 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
| `mimo-v2-omni` | ✅ MIT | $0.07/0.07 | **0.92** | 86 | [per-model](benchmarks/results/per-model/mimo-v2-omni.md) | [responses](benchmarks/results/responses/20260429_165839/) |
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
