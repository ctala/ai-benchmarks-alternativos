<!-- doc: generado -->
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

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `tencent/hy3` | ✅  | $0.132/0.528 | **8.57** | ⭐ | 139 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.49** | ⭐ | 158 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.47** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.46** | ⭐ | 159 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.45** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.44** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **8.42** |  | 169 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.39** |  | 139 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **8.38** |  | 160 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **8.38** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.36** |  | 202 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **8.35** |  | 144 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **8.35** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **8.33** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **8.32** |  | 169 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **8.30** | ⭐ | 151 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **8.28** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **8.28** |  | 315 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **8.26** |  | 215 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **8.25** |  | 150 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **8.24** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **8.24** |  | 161 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.22** | ⭐ | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.22** |  | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **8.22** ⛔ |  | 158 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **8.21** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **8.19** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **8.18** |  | 226 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **8.18** |  | 192 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **8.17** | ⭐ | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.16** | ⭐ | 139 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **8.15** |  | 148 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.14** |  | 157 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **8.14** |  | 164 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.13** | ⭐ | 150 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **8.13** |  | 159 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **8.12** |  | 153 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **8.10** |  | 159 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **8.09** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **8.08** |  | 153 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.08** |  | 163 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **8.07** |  | 139 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **8.07** |  | 176 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **8.06** |  | 139 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **8.06** |  | 266 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.04** | ⭐ | 159 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **8.04** |  | 158 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **8.04** |  | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.03** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **8.03** |  | 139 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **8.02** |  | 226 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **8.02** |  | 153 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.01** |  | 146 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **8.00** |  | 156 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **7.99** |  | 157 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.98** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **7.98** |  | 275 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.94** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.93** | ⭐ | 139 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **7.93** |  | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.92** |  | 213 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **7.91** |  | 178 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.90** ⛔ |  | 153 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.86** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.85** |  | 176 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.85** |  | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.85** |  | 158 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.83** | ⭐ | 144 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.79** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.78** | ⭐ | 149 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.72** ⛔ |  | 161 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.72** |  | 163 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.71** |  | 142 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **7.70** |  | 175 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.69** |  | 145 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **7.68** |  | 145 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.63** |  | 148 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **7.59** ⛔ |  | 152 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | [responses](benchmarks/results/responses/nim-qwen3-next-thinking/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **7.57** |  | 139 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **7.52** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.45** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **7.42** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **7.19** ⛔ |  | 151 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |

#### Mejor coding

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **9.11** | ⭐ | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.99** | ⭐ | 139 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.92** | ⭐ | 159 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **8.79** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **8.76** |  | 139 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.70** |  | 139 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.63** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.58** |  | 176 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.57** |  | 146 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.51** | ⭐ | 159 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **8.51** | ⭐ | 139 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.46** |  | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.44** | ⭐ | 150 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **8.44** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **8.41** |  | 153 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **8.38** | ⭐ | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.37** | ⭐ | 149 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **8.36** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **8.36** |  | 164 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **8.34** |  | 148 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **8.33** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **8.30** |  | 158 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **8.30** |  | 148 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **8.29** |  | 163 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **8.27** |  | 159 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **8.27** |  | 139 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **8.26** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **8.26** | ⭐ | 151 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **8.24** |  | 158 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **8.20** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **8.18** |  | 150 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **8.17** |  | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **8.17** ⛔ |  | 161 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **8.15** |  | 157 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.09** | ⭐ | 158 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **8.09** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **8.08** |  | 159 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **8.06** |  | 160 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **8.06** |  | 275 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **8.05** |  | 144 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **8.03** |  | 142 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **8.03** |  | 145 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **8.01** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.00** |  | 157 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.98** |  | 266 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.97** ⛔ |  | 158 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.97** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.96** |  | 226 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.96** ⛔ |  | 153 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.95** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.95** | ⭐ | 139 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.94** |  | 192 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **7.94** |  | 176 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **7.93** |  | 226 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **7.91** |  | 153 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.88** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.86** |  | 161 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.85** |  | 213 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.84** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.84** |  | 202 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **7.81** |  | 215 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **7.81** |  | 169 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.80** |  | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.78** |  | 153 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **7.77** |  | 169 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **7.71** |  | 178 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.58** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.49** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.43** |  | 156 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **7.43** |  | 315 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.41** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **7.39** |  | 145 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.39** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **7.30** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.28** | ⭐ | 144 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.15** |  | 163 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **7.15** ⛔ |  | 152 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | [responses](benchmarks/results/responses/nim-qwen3-next-thinking/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **7.09** |  | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.99** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **6.99** ⛔ |  | 151 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.94** |  | 175 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.85** |  | 139 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **6.81** |  | 139 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |

#### Mejor razonamiento

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.28** | ⭐ | 159 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.25** | ⭐ | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.13** |  | 146 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.08** | ⭐ | 159 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.94** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **7.92** | ⭐ | 158 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **7.92** |  | 139 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.88** |  | 157 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.87** | ⭐ | 139 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **7.87** | ⭐ | 151 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.84** | ⭐ | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **7.84** |  | 148 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.82** |  | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **7.80** |  | 157 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.79** |  | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **7.77** |  | 150 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.75** | ⭐ | 150 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.72** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.60** | ⭐ | 149 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.60** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.59** |  | 158 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.59** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.59** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.58** |  | 266 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **7.55** |  | 176 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **7.54** |  | 164 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.53** |  | 159 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.50** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **7.49** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **7.49** |  | 159 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **7.45** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.45** |  | 213 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.44** | ⭐ | 144 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.43** |  | 148 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.42** | ⭐ | 139 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.42** |  | 145 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.41** |  | 176 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.36** |  | 158 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.31** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **7.30** |  | 139 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **7.29** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **7.28** |  | 139 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **7.27** |  | 160 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.26** |  | 192 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.26** ⛔ |  | 158 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.25** ⛔ |  | 161 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **7.22** | ⭐ | 139 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **7.21** |  | 169 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **7.18** |  | 226 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.17** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **7.16** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.12** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.12** ⛔ |  | 153 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.08** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.06** |  | 153 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.02** |  | 153 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.02** |  | 142 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.01** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.96** |  | 144 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **6.96** |  | 215 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **6.91** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.88** |  | 202 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.84** |  | 226 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.83** |  | 139 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.82** |  | 163 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.82** |  | 156 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **6.82** |  | 153 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **6.72** |  | 275 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **6.72** |  | 169 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.66** |  | 315 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **6.61** ⛔ |  | 151 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.57** |  | 161 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.54** |  | 163 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.53** |  | 175 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **6.46** |  | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **6.34** ⛔ |  | 152 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | [responses](benchmarks/results/responses/nim-qwen3-next-thinking/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **6.34** |  | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **6.18** |  | 145 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **5.95** |  | 178 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **5.92** |  | 139 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **5.44** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **5.14** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **4.85** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |

#### Mejor contenido/marketing

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.13** | ⭐ | 158 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.11** | ⭐ | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.03** | ⭐ | 139 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.03** | ⭐ | 159 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.02** |  | 146 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **7.99** | ⭐ | 159 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.96** |  | 176 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.95** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **7.93** |  | 164 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **7.91** |  | 148 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **7.86** |  | 150 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.85** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.84** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **7.84** |  | 139 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **7.83** |  | 139 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **7.82** | ⭐ | 151 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.81** |  | 158 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.80** |  | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.75** ⛔ |  | 161 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.73** | ⭐ | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.71** |  | 148 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **7.66** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.65** |  | 156 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.65** | ⭐ | 144 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.64** |  | 226 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **7.62** ⛔ |  | 151 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **7.62** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.62** | ⭐ | 139 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.59** |  | 157 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.57** |  | 142 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.56** | ⭐ | 139 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.54** | ⭐ | 149 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.52** |  | 192 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.47** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **7.47** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.47** |  | 153 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.47** | ⭐ | 150 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **7.43** |  | 139 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **7.38** |  | 159 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **7.37** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **7.36** ⛔ |  | 152 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | [responses](benchmarks/results/responses/nim-qwen3-next-thinking/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **7.35** |  | 157 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.35** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **7.33** |  | 226 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **7.28** |  | 275 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.27** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.27** |  | 158 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.25** ⛔ |  | 158 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.23** |  | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.22** |  | 163 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.22** |  | 144 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.22** |  | 153 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.21** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.21** |  | 161 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.18** |  | 266 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **7.15** |  | 153 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.13** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.09** ⛔ |  | 153 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.04** |  | 159 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **7.04** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.01** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.99** |  | 315 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **6.98** |  | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **6.97** |  | 213 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **6.97** |  | 215 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.94** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **6.92** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **6.89** |  | 169 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.88** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.88** |  | 145 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **6.86** |  | 176 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **6.79** |  | 160 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **6.74** |  | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **6.72** |  | 169 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.65** |  | 163 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.57** |  | 139 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.51** |  | 202 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **6.44** |  | 139 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.38** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **6.35** |  | 178 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.32** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.28** |  | 175 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **6.21** |  | 145 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |

#### Calidad por dólar — cuánta calidad rinde cada peso (calidad ÷ $/1k calls; premia lo barato a propósito, mirá la columna Calidad)

| Modelo | OS | $ in/out | Calidad/$ | Frontera | Runs | Per-model MD | Responses |

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **78.51** | ⭐ | 139 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **53.26** ⛔ |  | 151 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **51.65** | ⭐ | 139 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **42.65** |  | 139 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **41.52** | ⭐ | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **41.47** | ⭐ | 159 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **35.89** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **28.79** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **27.45** |  | 139 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **26.43** |  | 139 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **24.22** |  | 148 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **22.61** |  | 157 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **19.80** |  | 226 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **17.62** |  | 164 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **17.60** |  | 159 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **16.31** | ⭐ | 144 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **15.69** |  | 156 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **13.05** | ⭐ | 151 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **12.77** |  | 275 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **12.35** | ⭐ | 149 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **12.11** |  | 150 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **12.08** ⛔ |  | 161 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **10.30** | ⭐ | 139 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **9.13** | ⭐ | 158 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.48** |  | 146 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.16** ⛔ |  | 153 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **6.37** |  | 176 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **5.76** |  | 148 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **5.66** |  | 153 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.18** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **4.99** |  | 145 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **4.98** |  | 266 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **4.90** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **4.79** |  | 153 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **4.34** |  | 139 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **4.33** |  | 226 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **4.19** |  | 213 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **4.11** ⛔ |  | 152 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | [responses](benchmarks/results/responses/nim-qwen3-next-thinking/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **3.92** |  | 192 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **3.48** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **3.46** | ⭐ | 159 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **3.43** |  | 148 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **3.40** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **3.39** | ⭐ | 150 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **3.12** |  | 158 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **2.77** |  | 160 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **2.23** |  | 176 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **2.15** |  | 215 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **2.14** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **2.09** |  | 158 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **2.04** |  | 150 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **1.87** |  | 163 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **1.87** |  | 142 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **1.74** |  | 169 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **1.71** ⛔ |  | 158 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **1.47** |  | 153 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **1.43** |  | 157 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **1.43** |  | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **1.42** |  | 178 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **1.29** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **1.22** |  | 139 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **1.16** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **1.05** | ⭐ | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **0.89** |  | 146 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **0.88** |  | 169 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **0.84** |  | 153 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **0.83** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **0.64** |  | 159 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **0.53** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **0.52** |  | 149 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.50** |  | 175 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **0.40** |  | 139 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **0.35** |  | 144 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **0.35** |  | 163 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **0.34** |  | 139 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **0.22** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **0.22** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **0.21** |  | 202 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **0.20** |  | 145 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **0.18** |  | 315 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **0.18** |  | 161 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **0.11** |  | 205 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **0.10** |  | 139 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |

#### Vía suscripción Claude — plano propio (comparables entre sí)

> Medidos aprovechando la **suscripción de Claude Code** (costo marginal $0), todos por el mismo camino → **comparables entre ellos**. Ese camino arrastra ~8.8K tokens de scaffolding del CLI y **deprime la nota**: en los 2 modelos medidos por ambos caminos, la calidad por API dio **+0.15 y +0.22 más** que por suscripción. Leé estos números como **piso conservador**, no como techo — y no los compares 1:1 contra la tabla principal (la latencia por CLI es 2.5-4× peor y no es del modelo). Sirven para la pregunta de quien ya paga el plan: *¿qué modelo uso dentro de mi suscripción?*

| Modelo | Calidad (piso) | Velocidad | Runs | Per-model MD | Responses |
|---|---:|---:|---:|---|---|
| `claude-sonnet-5` | **8.86** | 55 tok/s | 119 | [per-model](benchmarks/results/per-model/claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5-sub/) |
| `claude-fable-5` | **8.61** | 58 tok/s | 102 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/claude-fable-5-sub/) |
| `claude-opus-5` | **8.49** | 46 tok/s | 113 | [per-model](benchmarks/results/per-model/claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5-sub/) |
| `claude-opus-4-8` | **8.38** | 58 tok/s | 109 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | [responses](benchmarks/results/responses/claude-opus-4.8-sub/) |
| `claude-haiku-4-5` | **8.29** | 102 tok/s | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5-sub/) |
| `claude-sonnet-4-6` | **8.29** | 49 tok/s | 93 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6-sub/) |
| `claude-opus-4-7` | **8.27** | 53 tok/s | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7-sub/) |

#### Variantes de proveedor (35 mediciones)

> El mismo modelo servido por otra infraestructura (Groq, NVIDIA NIM, Ollama Cloud, API directa del proveedor, self-hosted). **No compiten acá** — comparar infra contra infra es otra pregunta, y tiene su propia página: [el proveedor te cambia el modelo](https://benchmarks.cristiantala.com/mismo-modelo-distinto-proveedor/). El caso extremo medido: el mismo Qwen 3.5 397B da **7.96 en NVIDIA NIM y 5.46 en Ollama Cloud** — 2.5 puntos por la infraestructura, no por el modelo.

#### En evaluación — muestra parcial (<50 runs, NO rankeados)

> Estos modelos tienen menos runs que el piso del ranking, así que su score es **indicativo, no comparable**: con pocas muestras la varianza permite que un modelo quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** en las tablas de arriba hasta completar la cobertura.

| Modelo | OS | $ in/out | Calidad (indic.) | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `openai/gpt-5.6-luna-pro` | ❌  | $0.1/0.6 | **8.60** |  | 117 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna-pro.md) | [responses](benchmarks/results/responses/gpt-5.6-luna-pro/) |
| `openai/gpt-5.6-terra-pro` | ❌  | $1.0/6.0 | **8.34** |  | 128 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra-pro.md) | [responses](benchmarks/results/responses/gpt-5.6-terra-pro/) |
| `qwen/qwen-2.5-72b-instruct` | ✅ Apache 2.0 | $0.36/0.4 | **8.24** |  | 63 | [per-model](benchmarks/results/per-model/qwen_qwen-2_5-72b-instruct.md) | [responses](benchmarks/results/responses/or-qwen-2.5-72b/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **8.02** |  | 134 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/or-nemotron-nano-9b-v2/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.99** |  | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | [responses](benchmarks/results/responses/or-nemotron-3-nano-omni-reasoning/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.03** |  | 166 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/mistral-nemo/) |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **5.00** |  | 2 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/nim-kimi-k2-thinking/) |

#### Retirados — fuera del ranking y de las recomendaciones

> **Un modelo que no puedes usar no es un candidato.** Sus números son reales y quedan acá por transparencia (alimentan el análisis histórico), pero no compiten. Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera, y Nemotron Super 49B v1.5 estaba **#8** el día que NVIDIA lo sacó de OpenRouter.

> **`Quién`** distingue lo que decidió el proveedor de lo que decidimos nosotros: Phi-4 no lo retiró nadie, es el modelo juez y no compite. **`Sigue vivo en`** avisa cuando lo que murió fue *una ruta* y no el modelo — el caso normal, no la excepción. Y el retiro **se re-verifica** (`check_endpoints.py --recheck-retired`): el 12-ago-2026 dos modelos retirados en julio habían vuelto a responder porque un proveedor los recogió, y volvieron al catálogo.

| Modelo | Retirado | Quién | Causa | Sigue vivo en | Score (histórico) | Runs |
|---|---|---|---|---|---:|---:|
| `llama-3.1-8b-instant` | 2026-08-16 | proveedor | Groq deprecó el endpoint (anunciado el 17-jun-2026, apagado el 16-ago). Recomiendan migrar a openai/gpt-oss-20b. Ojo: era el mejor de Groq en tool calling (8,01) y el reemplazo sugerido marca 6,45. | — | **2.88** | 84 |
| `llama-3.3-70b-versatile` | 2026-08-16 | proveedor | Groq deprecó el endpoint (anunciado por correo el 17-jun-2026, apagado el 16-ago). Recomiendan migrar a openai/gpt-oss-120b o qwen/qwen3.6-27b. El modelo Llama 3.3 70B sigue vivo en OpenRouter: lo que murió es esta ruta. | — | **5.15** | 84 |
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
| mistralai/devstral-2512 | Si (Apache 2.0) | 0.40/2.0 | L3 | Devstral 2 (Dic 2025) (retirado) |
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
| **NVIDIA NIM (8 modelos)** | **Desbloqueado abril 25** — provider `nvidia_nim` con base URL `https://integrate.api.nvidia.com/v1`. Free tier: 40 RPM, **gratis** para benchmarks secuenciales. Catálogo de 135+ modelos. Smoke test OK con Nemotron Super 49B v1.5 (retirado). Modelos agregados al config (claves `nim-*`): Nemotron Super 49B v1.5, Nemotron Ultra 253B, Qwen 3-Next 80B (instruct + thinking), Mistral-Nemotron, Kimi K2 Thinking, DeepSeek V4 Flash, Qwen 3.5 397B. |

---

## Por agregar al config (mercado, abril 2026)

> Modelos lanzados que aún no están en `config.py`. Verificar IDs reales en OpenRouter antes de agregar.

| Modelo | Esperado | $ aprox | Razón |
|---|---|---|---|
| Mistral Small 4 | `mistralai/mistral-small-2603` | 0.15/0.60 | Apache 2.0, baseline. **Está en `config.example.py`, falta copiar a `config.py`**. |
| Grok 4.1 Fast (retirado) | `x-ai/grok-4.1-fast` | 0.20/0.50 | xAI rápido. Está en `config.example.py`. |
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
1. `nim-nemotron-super-1.5` (Nemotron Super 49B v1.5 (retirado))
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
| Devstral Small (retirado) | abr 2025 | abr 2024 |
| Devstral Medium (retirado) | nov 2025 | jul 2025 |
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
