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
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.52** | ⭐ | 162 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.49** | ⭐ | 163 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **8.49** | ⭐ | 143 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **8.48** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.48** |  | 165 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.48** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.45/3.2 | **8.47** |  | 686 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **8.46** |  | 173 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **8.45** |  | 158 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.43** |  | 143 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **8.42** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **8.41** |  | 1566 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `qwen/qwen3.8-max` | ❌ Proprietary | $2.0/6.0 | **8.40** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max.md) | [responses](benchmarks/results/responses/qwen-3.8-max/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **8.39** |  | 148 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.39** |  | 210 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **8.39** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `qwen/qwen3.8-2.4t-a95b` | ❌  | $2.0/6.0 | **8.38** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-2_4t-a95b.md) | [responses](benchmarks/results/responses/qwen-3.8-2.4t/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **8.36** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **8.36** |  | 173 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **8.34** |  | 155 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **8.31** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **8.31** |  | 296 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `google/gemini-3.7-flash` | ❌ Proprietary | $0.38/1.88 | **8.30** |  | 506 | [per-model](benchmarks/results/per-model/google_gemini-3_7-flash.md) | [responses](benchmarks/results/responses/gemini-3.7-flash/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **8.30** |  | 234 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **8.30** |  | 219 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **8.29** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **8.28** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **8.28** |  | 165 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `x-ai/grok-4.6` | ❌ Proprietary | $2.0/6.0 | **8.27** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_6.md) | [responses](benchmarks/results/responses/grok-4.6/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.26** | ⭐ | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.26** |  | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **8.26** ⛔ |  | 478 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **8.24** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **8.23** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **8.23** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **8.23** |  | 451 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **8.22** |  | 196 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **8.21** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `bytedance-seed/seed-2-1-turbo` | ❌  | $0.5/2.5 | **8.21** |  | 1240 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2-1-turbo.md) | [responses](benchmarks/results/responses/seed-2-1-turbo/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **8.21** |  | 472 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **8.20** |  | 164 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.17** | ⭐ | 154 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **8.17** |  | 157 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **8.17** |  | 230 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **8.16** |  | 168 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **8.15** |  | 163 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **8.15** |  | 653 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `kwaipilot/kat-coder-air-v2.5` | ❌  | $0.15/0.6 | **8.13** | ⭐ | 497 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-air-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-air-2.5/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.13** | ⭐ | 143 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **8.12** |  | 157 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.12** |  | 171 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.11** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **8.11** |  | 154 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **8.11** |  | 180 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **8.11** |  | 270 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **8.10** |  | 163 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.09** | ⭐ | 163 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **8.08** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **8.08** |  | 152 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **8.06** |  | 157 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **8.06** |  | 143 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **8.05** |  | 143 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **8.04** |  | 143 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **8.04** |  | 160 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.03** |  | 150 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **8.03** |  | 1140 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **8.02** |  | 280 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.01** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **8.01** |  | 161 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.99** |  | 165 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.98** | ⭐ | 143 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.95** ⛔ |  | 157 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.91** |  | 162 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.91** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **7.91** |  | 855 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.89** |  | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.88** | ⭐ | 148 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.84** | ⭐ | 153 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `kwaipilot/kat-coder-pro-v2.5` | ❌  | $0.74/2.96 | **7.83** |  | 262 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-pro-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-pro-2.5/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.83** |  | 217 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.82** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.81** |  | 180 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **7.80** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.78** ⛔ |  | 487 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.78** |  | 162 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.77** |  | 167 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **7.74** |  | 493 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **7.74** |  | 182 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.70** |  | 146 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.69** |  | 152 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **7.68** |  | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.51** |  | 166 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **7.48** |  | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **7.26** ⛔ |  | 155 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |

#### Mejor coding

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **9.11** | ⭐ | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **9.08** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.99** | ⭐ | 143 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.92** | ⭐ | 163 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **8.86** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `google/gemini-3.7-flash` | ❌ Proprietary | $0.38/1.88 | **8.84** |  | 506 | [per-model](benchmarks/results/per-model/google_gemini-3_7-flash.md) | [responses](benchmarks/results/responses/gemini-3.7-flash/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **8.79** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **8.76** |  | 143 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `kwaipilot/kat-coder-air-v2.5` | ❌  | $0.15/0.6 | **8.73** | ⭐ | 497 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-air-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-air-2.5/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.70** |  | 143 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **8.69** |  | 234 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.63** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.58** |  | 180 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.57** |  | 150 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.51** | ⭐ | 163 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **8.51** | ⭐ | 143 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `qwen/qwen3.8-2.4t-a95b` | ❌  | $2.0/6.0 | **8.46** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-2_4t-a95b.md) | [responses](benchmarks/results/responses/qwen-3.8-2.4t/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.46** |  | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.44** | ⭐ | 154 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **8.44** |  | 162 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **8.41** |  | 157 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **8.40** |  | 1566 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **8.38** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **8.37** | ⭐ | 153 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.45/3.2 | **8.36** |  | 686 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **8.36** |  | 168 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **8.34** |  | 152 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **8.33** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `kwaipilot/kat-coder-pro-v2.5` | ❌  | $0.74/2.96 | **8.32** |  | 262 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-pro-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-pro-2.5/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **8.31** |  | 296 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **8.30** |  | 162 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **8.30** |  | 152 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **8.29** |  | 167 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **8.27** |  | 163 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **8.27** |  | 143 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **8.26** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **8.26** |  | 155 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `x-ai/grok-4.6` | ❌ Proprietary | $2.0/6.0 | **8.26** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_6.md) | [responses](benchmarks/results/responses/grok-4.6/) |
| `bytedance-seed/seed-2-1-turbo` | ❌  | $0.5/2.5 | **8.25** |  | 1240 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2-1-turbo.md) | [responses](benchmarks/results/responses/seed-2-1-turbo/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **8.24** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **8.20** |  | 154 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **8.18** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **8.17** ⛔ |  | 487 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **8.15** |  | 161 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **8.11** |  | 1140 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.09** | ⭐ | 162 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **8.09** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **8.08** |  | 163 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **8.06** |  | 164 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **8.06** |  | 855 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **8.05** |  | 148 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **8.03** |  | 146 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **8.03** |  | 280 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **8.01** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.00** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.98** |  | 270 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.97** ⛔ |  | 478 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.97** |  | 165 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.96** |  | 230 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.96** ⛔ |  | 157 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.95** |  | 165 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.95** | ⭐ | 143 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.94** |  | 196 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **7.94** |  | 180 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **7.93** |  | 493 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **7.91** |  | 157 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.88** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `qwen/qwen3.8-max` | ❌ Proprietary | $2.0/6.0 | **7.87** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max.md) | [responses](benchmarks/results/responses/qwen-3.8-max/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.86** |  | 165 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.85** |  | 217 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.84** |  | 158 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **7.84** |  | 210 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **7.81** |  | 219 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **7.81** |  | 173 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.80** |  | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.78** |  | 157 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **7.77** |  | 173 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **7.71** |  | 182 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **7.58** |  | 166 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **7.52** |  | 472 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **7.52** |  | 451 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.49** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.43** |  | 160 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **7.43** |  | 653 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.41** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.39** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **7.30** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.28** | ⭐ | 148 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **7.15** |  | 171 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **7.09** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.99** |  | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **6.99** ⛔ |  | 155 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.94** |  | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.85** |  | 143 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |

#### Mejor razonamiento

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.28** | ⭐ | 163 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.25** | ⭐ | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.13** |  | 150 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.08** | ⭐ | 163 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **7.97** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.94** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **7.92** | ⭐ | 162 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **7.92** |  | 143 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.88** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.87** | ⭐ | 143 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **7.87** |  | 155 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.84** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **7.84** |  | 152 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.82** |  | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **7.80** |  | 161 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.79** |  | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **7.77** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.75** | ⭐ | 154 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.72** |  | 162 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **7.68** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.60** | ⭐ | 153 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.60** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.59** |  | 162 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.59** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.59** |  | 154 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.58** |  | 270 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **7.55** |  | 180 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **7.54** |  | 168 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.53** |  | 163 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.50** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `kwaipilot/kat-coder-air-v2.5` | ❌  | $0.15/0.6 | **7.50** | ⭐ | 497 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-air-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-air-2.5/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **7.49** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **7.49** |  | 163 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **7.45** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **7.45** |  | 217 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.44** | ⭐ | 148 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.43** |  | 152 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.42** | ⭐ | 143 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.42** |  | 280 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.41** |  | 180 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.36** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **7.31** |  | 165 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `google/gemini-3.7-flash` | ❌ Proprietary | $0.38/1.88 | **7.30** |  | 506 | [per-model](benchmarks/results/per-model/google_gemini-3_7-flash.md) | [responses](benchmarks/results/responses/gemini-3.7-flash/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **7.30** |  | 143 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **7.29** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **7.28** |  | 143 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **7.27** |  | 164 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.26** |  | 196 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.26** ⛔ |  | 478 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **7.25** |  | 234 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.25** ⛔ |  | 487 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **7.22** | ⭐ | 143 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **7.21** |  | 173 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **7.18** |  | 493 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.17** |  | 165 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **7.16** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `bytedance-seed/seed-2-1-turbo` | ❌  | $0.5/2.5 | **7.14** |  | 1240 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2-1-turbo.md) | [responses](benchmarks/results/responses/seed-2-1-turbo/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.12** |  | 158 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.12** ⛔ |  | 157 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **7.08** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.06** |  | 157 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **7.04** |  | 1140 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.02** |  | 157 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.02** |  | 146 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.01** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **6.99** |  | 1566 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.45/3.2 | **6.97** |  | 686 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **6.96** |  | 148 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **6.96** |  | 219 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `qwen/qwen3.8-2.4t-a95b` | ❌  | $2.0/6.0 | **6.93** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-2_4t-a95b.md) | [responses](benchmarks/results/responses/qwen-3.8-2.4t/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **6.91** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.88** |  | 210 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **6.84** |  | 230 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.83** |  | 143 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.82** |  | 171 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.82** |  | 160 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **6.82** |  | 157 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **6.79** |  | 296 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **6.74** |  | 472 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **6.72** |  | 855 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **6.72** |  | 173 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **6.67** |  | 451 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.66** |  | 653 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `kwaipilot/kat-coder-pro-v2.5` | ❌  | $0.74/2.96 | **6.63** |  | 262 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-pro-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-pro-2.5/) |
| `x-ai/grok-4.6` | ❌ Proprietary | $2.0/6.0 | **6.62** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_6.md) | [responses](benchmarks/results/responses/grok-4.6/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **6.61** ⛔ |  | 155 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **6.57** |  | 165 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **6.54** |  | 167 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.53** |  | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `qwen/qwen3.8-max` | ❌ Proprietary | $2.0/6.0 | **6.44** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max.md) | [responses](benchmarks/results/responses/qwen-3.8-max/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **6.34** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **5.95** |  | 182 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **5.14** |  | 166 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **4.85** |  | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |

#### Mejor contenido/marketing

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **8.13** | ⭐ | 162 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `kwaipilot/kat-coder-air-v2.5` | ❌  | $0.15/0.6 | **8.13** | ⭐ | 497 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-air-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-air-2.5/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **8.11** | ⭐ | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **8.04** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **8.03** | ⭐ | 143 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.03** | ⭐ | 163 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.02** |  | 150 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **7.99** | ⭐ | 163 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.96** |  | 180 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.95** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **7.93** |  | 168 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **7.91** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **7.91** |  | 152 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **7.86** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.85** |  | 154 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.84** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **7.84** |  | 143 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **7.83** |  | 143 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **7.82** |  | 155 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **7.81** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **7.80** |  | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **7.75** ⛔ |  | 487 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **7.73** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `google/gemini-3.7-flash` | ❌ Proprietary | $0.38/1.88 | **7.71** |  | 506 | [per-model](benchmarks/results/per-model/google_gemini-3_7-flash.md) | [responses](benchmarks/results/responses/gemini-3.7-flash/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.71** |  | 152 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **7.68** |  | 234 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **7.66** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.65** |  | 160 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.65** | ⭐ | 148 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **7.64** |  | 230 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **7.62** ⛔ |  | 155 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **7.62** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.62** | ⭐ | 143 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.59** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **7.57** |  | 146 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **7.57** |  | 1566 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.56** | ⭐ | 143 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.54** | ⭐ | 153 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **7.52** |  | 196 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **7.48** |  | 1140 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **7.47** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **7.47** |  | 158 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **7.47** |  | 157 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **7.47** | ⭐ | 154 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **7.43** |  | 143 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **7.38** |  | 163 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **7.37** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **7.35** |  | 161 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.35** |  | 162 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **7.33** |  | 493 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **7.28** |  | 855 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.27** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **7.27** |  | 162 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **7.25** ⛔ |  | 478 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `qwen/qwen3.8-2.4t-a95b` | ❌  | $2.0/6.0 | **7.24** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-2_4t-a95b.md) | [responses](benchmarks/results/responses/qwen-3.8-2.4t/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **7.23** |  | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `x-ai/grok-4.6` | ❌ Proprietary | $2.0/6.0 | **7.22** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_6.md) | [responses](benchmarks/results/responses/grok-4.6/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **7.22** |  | 167 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **7.22** |  | 148 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **7.22** |  | 157 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **7.21** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **7.21** |  | 165 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `qwen/qwen3.8-max` | ❌ Proprietary | $2.0/6.0 | **7.19** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max.md) | [responses](benchmarks/results/responses/qwen-3.8-max/) |
| `bytedance-seed/seed-2-1-turbo` | ❌  | $0.5/2.5 | **7.19** |  | 1240 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2-1-turbo.md) | [responses](benchmarks/results/responses/seed-2-1-turbo/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **7.18** |  | 270 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.45/3.2 | **7.16** |  | 686 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **7.16** |  | 451 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **7.15** |  | 157 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **7.13** |  | 165 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **7.10** |  | 296 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.09** ⛔ |  | 157 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **7.08** |  | 472 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.04** |  | 163 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **7.04** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **7.01** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **6.99** |  | 653 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **6.98** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **6.97** |  | 217 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **6.97** |  | 219 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **6.94** |  | 165 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **6.89** |  | 173 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **6.88** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **6.88** |  | 280 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **6.86** |  | 180 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **6.79** |  | 164 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `kwaipilot/kat-coder-pro-v2.5` | ❌  | $0.74/2.96 | **6.74** |  | 262 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-pro-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-pro-2.5/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **6.72** |  | 173 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **6.65** |  | 171 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **6.57** |  | 143 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **6.51** |  | 210 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **6.38** |  | 166 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **6.35** |  | 182 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **6.32** |  | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **6.28** |  | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |

#### Calidad por dólar — cuánta calidad rinde cada peso (calidad ÷ $/1k calls; premia lo barato a propósito, mirá la columna Calidad)

| Modelo | OS | $ in/out | Calidad/$ | Frontera | Runs | Per-model MD | Responses |

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **79.01** | ⭐ | 143 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **53.78** ⛔ |  | 155 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `nex-agi/nex-n2-mini` | ✅  | $0.025/0.1 | **51.46** | ⭐ | 143 | [per-model](benchmarks/results/per-model/nex-agi_nex-n2-mini.md) | [responses](benchmarks/results/responses/nex-n2-mini/) |
| `upstage/solar-pro4` | ❌  | $0.03/0.12 | **42.54** |  | 143 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `poolside/laguna-xs-2.1` | ✅ OpenMDW-1.1 | $0.06/0.12 | **41.72** | ⭐ | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-xs-2_1.md) | [responses](benchmarks/results/responses/laguna-xs-2.1/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **41.62** | ⭐ | 163 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **36.12** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **28.86** |  | 154 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.08/0.18 | **27.38** |  | 143 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `poolside/laguna-s-2.1` | ✅ OpenMDW-1.1 | $0.09/0.18 | **26.57** |  | 143 | [per-model](benchmarks/results/per-model/poolside_laguna-s-2_1.md) | [responses](benchmarks/results/responses/laguna-s-2.1/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **24.41** |  | 152 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **22.53** |  | 161 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.1/0.25 | **19.11** |  | 493 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.14/0.28 | **17.66** |  | 168 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `xiaomi/mimo-v2.5` | ❌  | $0.14/0.28 | **17.53** |  | 163 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **16.73** |  | 1140 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **16.42** | ⭐ | 148 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **15.76** |  | 160 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **15.70** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.12/0.4 | **13.11** |  | 155 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **12.66** |  | 855 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **12.44** | ⭐ | 153 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `nousresearch/hermes-4-70b` | ✅ Llama 3 community | $0.13/0.4 | **12.18** ⛔ |  | 487 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-70b.md) | [responses](benchmarks/results/responses/hermes-4-70b/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **12.17** |  | 154 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **10.20** | ⭐ | 143 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `openai/gpt-5.6-luna` | ❌  | $0.1/0.6 | **9.16** | ⭐ | 162 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `kwaipilot/kat-coder-air-v2.5` | ❌  | $0.15/0.6 | **8.60** | ⭐ | 497 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-air-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-air-2.5/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.50** |  | 150 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.20** ⛔ |  | 157 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **6.33** |  | 180 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.22/0.9 | **5.71** |  | 152 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `xiaomi/mimo-v2.5-pro` | ❌  | $0.435/0.87 | **5.69** |  | 157 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.20** |  | 280 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.14/1.0 | **5.07** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `deepseek/deepseek-chat` | ❌  | $0.2574/1.0287 | **5.01** |  | 270 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **4.89** |  | 162 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **4.78** |  | 157 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **4.36** |  | 143 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `minimax/minimax-m3` | ❌  | $0.3/1.2 | **4.32** |  | 230 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `minimax/minimax-m2.7` | ❌  | $0.3/1.2 | **4.14** |  | 217 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $0.63168/1.26336 | **3.94** |  | 196 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **3.49** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **3.48** | ⭐ | 163 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **3.44** |  | 152 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.4886/1.5356 | **3.41** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **3.40** | ⭐ | 154 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **3.14** |  | 162 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `google/gemini-3.7-flash` | ❌ Proprietary | $0.38/1.88 | **2.83** |  | 506 | [per-model](benchmarks/results/per-model/google_gemini-3_7-flash.md) | [responses](benchmarks/results/responses/gemini-3.7-flash/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **2.71** |  | 164 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **2.24** |  | 180 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.5795/2.44 | **2.16** |  | 219 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **2.14** | ⭐ | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `deepseek/deepseek-r1` | ✅ MIT | $0.7/2.5 | **2.13** |  | 158 | [per-model](benchmarks/results/per-model/deepseek_deepseek-r1.md) | [responses](benchmarks/results/responses/deepseek-r1/) |
| `bytedance-seed/seed-2-1-turbo` | ❌  | $0.5/2.5 | **2.11** |  | 1240 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2-1-turbo.md) | [responses](benchmarks/results/responses/seed-2-1-turbo/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **2.10** |  | 162 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `z-ai/glm-5` | ✅ MIT | $0.95/2.55 | **2.05** |  | 154 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **1.88** |  | 167 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **1.87** |  | 146 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **1.81** |  | 1566 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.952/2.992 | **1.75** |  | 173 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **1.72** ⛔ |  | 478 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.45/3.2 | **1.72** |  | 686 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `kwaipilot/kat-coder-pro-v2.5` | ❌  | $0.74/2.96 | **1.68** |  | 262 | [per-model](benchmarks/results/per-model/kwaipilot_kat-coder-pro-v2_5.md) | [responses](benchmarks/results/responses/kat-coder-pro-2.5/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **1.48** |  | 157 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/3.6 | **1.44** |  | 161 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **1.42** |  | 234 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.5/3.6 | **1.41** |  | 154 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.6/3.6 | **1.39** |  | 182 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **1.23** |  | 143 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **1.16** |  | 158 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **1.05** |  | 157 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `openai/gpt-5.6-terra` | ❌  | $1/6 | **0.89** |  | 150 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `qwen/qwen3.6-max-preview` | ❌ Proprietary | $1.027/6.162 | **0.89** |  | 173 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-max-preview.md) | [responses](benchmarks/results/responses/qwen-3.6-max/) |
| `qwen/qwen3.8-max` | ❌ Proprietary | $2.0/6.0 | **0.88** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max.md) | [responses](benchmarks/results/responses/qwen-3.8-max/) |
| `qwen/qwen3.8-2.4t-a95b` | ❌  | $2.0/6.0 | **0.87** |  | 291 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-2_4t-a95b.md) | [responses](benchmarks/results/responses/qwen-3.8-2.4t/) |
| `x-ai/grok-4.6` | ❌ Proprietary | $2.0/6.0 | **0.86** |  | 143 | [per-model](benchmarks/results/per-model/x-ai_grok-4_6.md) | [responses](benchmarks/results/responses/grok-4.6/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **0.85** |  | 157 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **0.83** |  | 165 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **0.65** |  | 163 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **0.54** |  | 166 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **0.53** |  | 296 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **0.50** |  | 179 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **0.40** |  | 143 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **0.35** |  | 148 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **0.35** |  | 171 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `moonshotai/kimi-k3` | ✅  | $3.0/15.0 | **0.34** |  | 143 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **0.22** |  | 165 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **0.22** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **0.22** |  | 210 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **0.21** |  | 472 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `openai/gpt-5.6-sol` | ❌  | $5.0/30.0 | **0.18** |  | 165 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **0.18** |  | 653 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **0.11** |  | 213 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **0.11** |  | 451 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |

#### Vía suscripción Claude — plano propio (comparables entre sí)

> Medidos aprovechando la **suscripción de Claude Code** (costo marginal $0), todos por el mismo camino → **comparables entre ellos**. Ese camino arrastra ~8.8K tokens de scaffolding del CLI y **deprime la nota**: en los 2 modelos medidos por ambos caminos, la calidad por API dio **+0.15 y +0.22 más** que por suscripción. Leé estos números como **piso conservador**, no como techo — y no los compares 1:1 contra la tabla principal (la latencia por CLI es 2.5-4× peor y no es del modelo). Sirven para la pregunta de quien ya paga el plan: *¿qué modelo uso dentro de mi suscripción?*

| Modelo | Calidad (piso) | Velocidad | Runs | Per-model MD | Responses |
|---|---:|---:|---:|---|---|
| `claude-sonnet-5` | **8.88** | 55 tok/s | 123 | [per-model](benchmarks/results/per-model/claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5-sub/) |
| `claude-fable-5` | **8.61** | 58 tok/s | 102 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/claude-fable-5-sub/) |
| `claude-opus-5` | **8.49** | 46 tok/s | 113 | [per-model](benchmarks/results/per-model/claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5-sub/) |
| `claude-opus-4-8` | **8.38** | 58 tok/s | 109 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | [responses](benchmarks/results/responses/claude-opus-4.8-sub/) |
| `claude-haiku-4-5` | **8.29** | 102 tok/s | 86 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5-sub/) |
| `claude-sonnet-4-6` | **8.29** | 49 tok/s | 93 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6-sub/) |
| `claude-opus-4-7` | **8.27** | 53 tok/s | 70 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7-sub/) |

#### Variantes de proveedor (36 mediciones)

> El mismo modelo servido por otra infraestructura (Groq, NVIDIA NIM, Ollama Cloud, API directa del proveedor, self-hosted). **No compiten acá** — comparar infra contra infra es otra pregunta, y tiene su propia página: [el proveedor te cambia el modelo](https://benchmarks.cristiantala.com/mismo-modelo-distinto-proveedor/). El caso extremo medido: el mismo Qwen 3.5 397B da **7.96 en NVIDIA NIM y 5.46 en Ollama Cloud** — 2.5 puntos por la infraestructura, no por el modelo.

#### En evaluación — muestra parcial (<50 runs, NO rankeados)

> Estos modelos tienen menos runs que el piso del ranking, así que su score es **indicativo, no comparable**: con pocas muestras la varianza permite que un modelo quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** en las tablas de arriba hasta completar la cobertura.

| Modelo | OS | $ in/out | Calidad (indic.) | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `sakana/sakana-namazu` | ❌  | $0.95/4.0 | **8.59** |  | 1728 | [per-model](benchmarks/results/per-model/sakana_sakana-namazu.md) | [responses](benchmarks/results/responses/sakana-namazu/) |
| `meituan/longcat-2.0` | ❌  | $0.3/1.2 | **8.52** |  | 22 | [per-model](benchmarks/results/per-model/meituan_longcat-2_0.md) | [responses](benchmarks/results/responses/longcat-2.0/) |
| `openai/gpt-5.6-luna-pro` | ❌  | $0.1/0.6 | **8.50** |  | 264 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna-pro.md) | [responses](benchmarks/results/responses/gpt-5.6-luna-pro/) |
| `deepseek/deepseek-v4-pro-0813` | ❌  | $0.66/1.98 | **8.50** |  | 405 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro-0813.md) | [responses](benchmarks/results/responses/deepseek-v4-pro-0813/) |
| `openai/gpt-5.6-terra-pro` | ❌  | $1.0/6.0 | **8.40** |  | 275 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra-pro.md) | [responses](benchmarks/results/responses/gpt-5.6-terra-pro/) |
| `qwen/qwen-2.5-72b-instruct` | ✅ Apache 2.0 | $0.36/0.4 | **8.27** |  | 172 | [per-model](benchmarks/results/per-model/qwen_qwen-2_5-72b-instruct.md) | [responses](benchmarks/results/responses/or-qwen-2.5-72b/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.57/2.85 | **8.08** |  | 14110 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/kimi-k2.5-thinking/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **8.02** |  | 134 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/or-nemotron-nano-9b-v2/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **7.99** |  | 147 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | [responses](benchmarks/results/responses/or-nemotron-3-nano-omni-reasoning/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **7.52** ⛔ |  | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | [responses](benchmarks/results/responses/nim-qwen3-next-thinking/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **7.26** |  | 522 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/mistral-nemo/) |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **5.00** |  | 2 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/nim-kimi-k2-thinking/) |

#### Retirados — fuera del ranking y de las recomendaciones

> **Un modelo que no puedes usar no es un candidato.** Sus números son reales y quedan acá por transparencia (alimentan el análisis histórico), pero no compiten. Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera, y Nemotron Super 49B v1.5 estaba **#8** el día que NVIDIA lo sacó de OpenRouter.

> **`Quién`** distingue lo que decidió el proveedor de lo que decidimos nosotros: Phi-4 no lo retiró nadie, es el modelo juez y no compite. **`Sigue vivo en`** avisa cuando lo que murió fue *una ruta* y no el modelo — el caso normal, no la excepción. Y el retiro **se re-verifica** (`check_endpoints.py --recheck-retired`): el 12-ago-2026 dos modelos retirados en julio habían vuelto a responder porque un proveedor los recogió, y volvieron al catálogo.

| Modelo | Retirado | Quién | Causa | Sigue vivo en | Score (histórico) | Runs |
|---|---|---|---|---|---:|---:|
| `stepfun-ai/step3` | 2026-08-17 | proveedor | OpenRouter: 'No endpoints found for stepfun'. El id no existe en el catálogo; la familia sigue viva en step-3.5/3.7-flash. | — | — | 0 |
| `bytedance/seed-oss-36b-instruct` | 2026-08-17 | proveedor | OpenRouter: 'No endpoints found for bytedance'. El namespace pasó a `bytedance-seed/` y Seed-OSS 36B no está en el catálogo. | — | — | 0 |
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
