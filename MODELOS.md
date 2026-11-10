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

> **No existe un único 'mejor modelo'.** El score global combina calidad, costo, velocidad y latencia con pesos elegidos para emprendedores (70% calidad, 15% costo, 7.5% velocidad, 7.5% latencia) — **es un punto de partida, no un veredicto**. Un modelo puede quedar bajo en el global y ser el correcto para vos: si tu caso es batch nocturno, la latencia no te importa y el ranking la está penalizando igual. Mira las tablas por caso de uso, y para tus propios pesos usá la [calculadora](https://benchmarks.cristiantala.com/).

> **Piso de ranking: 50 runs.** Los modelos con menos muestra van a *En evaluación* al final — su score es indicativo, no comparable.

#### Índice de calidad — qué modelo responde mejor (⭐ = en la frontera de Pareto: nadie lo supera a la vez en calidad, precio y latencia)

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `z-ai/glm-5.3` | ✅ MIT | $1.4/4.4 | **9.00** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3.md) | [responses](benchmarks/results/responses/glm-5.3/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.6832/2.1472 | **8.95** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `qwen/qwen3.8-flash` | ❌  | $0.15/0.47 | **8.91** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-flash.md) | [responses](benchmarks/results/responses/qwen3.8-flash/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.214/2.55 | **8.90** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `qwen/qwen3.8-max-0902` | ❌ Proprietary | $2.0/6.0 | **8.90** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max-0902.md) | [responses](benchmarks/results/responses/qwen-3.8-max-0902/) |
| `google/gemini-4-argon` | ❌ Proprietary | $2/10 | **8.90** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-4-argon.md) | [responses](benchmarks/results/responses/gemini-4-argon/) |
| `z-ai/glm-5.3-flash` | ✅ MIT | $0.15/0.5 | **8.88** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3-flash.md) | [responses](benchmarks/results/responses/glm-5.3-flash/) |
| `anthropic/claude-fable-5.1` | ❌ Proprietary | $10.0/50.0 | **8.88** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_1.md) | [responses](benchmarks/results/responses/claude-fable-5.1/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **8.87** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **8.85** | ⭐ | 137 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `meta/muse-spark-1.3` | ❌  | $1.25/4.25 | **8.84** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_3.md) | [responses](benchmarks/results/responses/muse-spark-1.3/) |
| `xiaomi/mimo-v2.6-pro` | ❌ MIT (pesos -RL y -MOPD; sin confirmar cuál sirve la API) | $0.435/0.87 | **8.84** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-pro.md) | [responses](benchmarks/results/responses/mimo-v2.6-pro/) |
| `moonshotai/kimi-k3.1-pro` | ✅ Kimi K3.1 Pro License (propia de Moonshot) | $2/10 | **8.82** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3_1-pro.md) | [responses](benchmarks/results/responses/kimi-k3.1-pro/) |
| `mistralai/mistral-large-4-0` | ✅ Mistral Ecosystem Open-Weight License | $0.7/2.1 | **8.82** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-4-0.md) | [responses](benchmarks/results/responses/mistral-large-4/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.3/2 | **8.81** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `anthropic/claude-opus-5.5` | ❌ Proprietary | $4.0/20.0 | **8.81** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5_5.md) | [responses](benchmarks/results/responses/claude-opus-5.5/) |
| `anthropic/claude-fable-5.2` | ❌ Proprietary | $8.0/40.0 | **8.81** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_2.md) | [responses](benchmarks/results/responses/claude-fable-5.2/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.966/3.036 | **8.80** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **8.80** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `deepseek/deepseek-v4-pro-0813` | ✅ MIT | $0.9834/2.9502 | **8.79** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro-0813.md) | [responses](benchmarks/results/responses/deepseek-v4-pro-0813/) |
| `anthropic/claude-sonnet-5.5` | ❌ Proprietary | $2.0/10.0 | **8.79** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5_5.md) | [responses](benchmarks/results/responses/claude-sonnet-5.5/) |
| `google/gemini-3.8-flash` | ❌ Proprietary | $0.75/3.75 | **8.79** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_8-flash.md) | [responses](benchmarks/results/responses/gemini-3.8-flash/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **8.78** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **8.77** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.55/3.5 | **8.77** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.06/0.12 | **8.74** | ⭐ | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.45/2.25 | **8.74** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/kimi-k2.5-thinking/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.95/4 | **8.73** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `tencent/hy4` | ❌  | $0.417/1.2505 | **8.73** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy4.md) | [responses](benchmarks/results/responses/hy4/) |
| `sakana/fugu-max` | ❌ Proprietary | $2.0/6.0 | **8.73** |  | 137 | [per-model](benchmarks/results/per-model/sakana_fugu-max.md) | [responses](benchmarks/results/responses/fugu-max/) |
| `openai/gpt-6-luna` | ❌  | $0.1/0.5 | **8.71** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna.md) | [responses](benchmarks/results/responses/gpt-6-luna/) |
| `xiaomi/mimo-v2.6-flash` | ✅  | $0.14/0.28 | **8.70** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-flash.md) | [responses](benchmarks/results/responses/mimo-v2.6-flash/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **8.69** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `openai/gpt-6.1-sol` | ❌ Proprietary | $2/10 | **8.69** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-sol.md) | [responses](benchmarks/results/responses/gpt-6.1-sol/) |
| `meta/muse-wonder` | ❌ Proprietary | $4/20 | **8.69** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-wonder.md) | [responses](benchmarks/results/responses/muse-wonder/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **8.67** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `anthropic/claude-haiku-5.5` | ❌ Proprietary | $0.1/0.5 | **8.67** | ⭐ | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-5_5.md) | [responses](benchmarks/results/responses/claude-haiku-5.5/) |
| `openai/gpt-6-astra` | ❌ Proprietary | $10/50 | **8.67** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-astra.md) | [responses](benchmarks/results/responses/gpt-6-astra/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **8.66** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `deepseek/deepseek-v4.1-flash` | ✅ MIT | $0.15/0.6 | **8.66** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4_1-flash.md) | [responses](benchmarks/results/responses/deepseek-v4.1-flash/) |
| `meta/muse-ember` | ❌ Proprietary | $0.1/0.5 | **8.64** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-ember.md) | [responses](benchmarks/results/responses/muse-ember/) |
| `x-ai/grok-4.7` | ❌ Proprietary | $2/6 | **8.63** |  | 137 | [per-model](benchmarks/results/per-model/x-ai_grok-4_7.md) | [responses](benchmarks/results/responses/grok-4.7/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $1.6/3.2 | **8.62** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `openai/gpt-6.1-terra` | ❌ Proprietary | $1/5 | **8.61** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-terra.md) | [responses](benchmarks/results/responses/gpt-6.1-terra/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **8.59** |  | 137 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.55** |  | 137 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.088606/0.177212 | **8.51** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.27/1.08 | **8.48** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.1/0.9 | **8.47** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **8.41** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **8.35** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `minimax/minimax-m3.1-flash` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.075/0.3 | **8.35** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3_1-flash.md) | [responses](benchmarks/results/responses/minimax-m3.1-flash/) |
| `minimax/minimax-m3` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.3/1.2 | **8.33** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **8.28** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/2.4 | **8.18** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **8.17** |  | 137 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `google/gemini-3.1-flash-lite` | ❌ Proprietary | $0.25/1.5 | **8.12** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite-ga/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.99** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.96** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `ibm-granite/granite-4.2-8b` | ✅ Apache 2.0 | $0.06/0.25 | **7.92** |  | 137 | [per-model](benchmarks/results/per-model/ibm-granite_granite-4_2-8b.md) | [responses](benchmarks/results/responses/granite-4.2-8b/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.3125/1.25 | **7.76** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `openai/gpt-6-luna-pro` | ❌  | $0.1/0.5 | **7.75** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna-pro.md) | [responses](benchmarks/results/responses/gpt-6-luna-pro/) |
| `upstage/solar-pro4` | ❌  | $0.09/0.36 | **7.69** |  | 137 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.51** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.09/0.3 | **7.48** |  | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.44** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.29** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.08/0.2 | **7.18** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.16** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **6.92** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **6.76** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **6.15** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **6.00** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **5.31** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |

#### Mejor coding

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Examen | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **9.18** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.08/0.2 | **9.15** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `google/gemini-3.1-flash-lite` | ❌ Proprietary | $0.25/1.5 | **9.08** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite-ga/) |
| `meta/muse-ember` | ❌ Proprietary | $0.1/0.5 | **9.05** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-ember.md) | [responses](benchmarks/results/responses/muse-ember/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **9.03** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **9.03** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **9.01** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `anthropic/claude-haiku-5.5` | ❌ Proprietary | $0.1/0.5 | **8.99** | ⭐ | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-5_5.md) | [responses](benchmarks/results/responses/claude-haiku-5.5/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **8.98** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `ibm-granite/granite-4.2-8b` | ✅ Apache 2.0 | $0.06/0.25 | **8.98** |  | 137 | [per-model](benchmarks/results/per-model/ibm-granite_granite-4_2-8b.md) | [responses](benchmarks/results/responses/granite-4.2-8b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **8.97** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.1/0.9 | **8.95** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **8.94** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.06/0.12 | **8.94** | ⭐ | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.27/1.08 | **8.94** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **8.92** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.3125/1.25 | **8.90** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **8.89** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **8.88** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/2.4 | **8.87** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `minimax/minimax-m3` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.3/1.2 | **8.82** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **8.82** |  | 137 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **8.81** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `minimax/minimax-m3.1-flash` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.075/0.3 | **8.80** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3_1-flash.md) | [responses](benchmarks/results/responses/minimax-m3.1-flash/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.09/0.3 | **8.79** |  | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.6832/2.1472 | **8.78** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `upstage/solar-pro4` | ❌  | $0.09/0.36 | **8.76** |  | 137 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **8.75** | ⭐ | 137 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `qwen/qwen3.8-flash` | ❌  | $0.15/0.47 | **8.74** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-flash.md) | [responses](benchmarks/results/responses/qwen3.8-flash/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.3/2 | **8.73** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `tencent/hy4` | ❌  | $0.417/1.2505 | **8.73** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy4.md) | [responses](benchmarks/results/responses/hy4/) |
| `z-ai/glm-5.3-flash` | ✅ MIT | $0.15/0.5 | **8.72** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3-flash.md) | [responses](benchmarks/results/responses/glm-5.3-flash/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.95/4 | **8.72** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.70** |  | 137 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **8.70** |  | 137 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.966/3.036 | **8.67** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.088606/0.177212 | **8.66** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **8.66** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `meta/muse-spark-1.3` | ❌  | $1.25/4.25 | **8.66** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_3.md) | [responses](benchmarks/results/responses/muse-spark-1.3/) |
| `openai/gpt-6-luna` | ❌  | $0.1/0.5 | **8.66** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna.md) | [responses](benchmarks/results/responses/gpt-6-luna/) |
| `mistralai/mistral-large-4-0` | ✅ Mistral Ecosystem Open-Weight License | $0.7/2.1 | **8.64** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-4-0.md) | [responses](benchmarks/results/responses/mistral-large-4/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **8.64** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **8.63** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `openai/gpt-6.1-terra` | ❌ Proprietary | $1/5 | **8.63** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-terra.md) | [responses](benchmarks/results/responses/gpt-6.1-terra/) |
| `google/gemini-3.8-flash` | ❌ Proprietary | $0.75/3.75 | **8.62** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_8-flash.md) | [responses](benchmarks/results/responses/gemini-3.8-flash/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **8.62** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **8.62** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `deepseek/deepseek-v4.1-flash` | ✅ MIT | $0.15/0.6 | **8.61** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4_1-flash.md) | [responses](benchmarks/results/responses/deepseek-v4.1-flash/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.55/3.5 | **8.61** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **8.58** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `xiaomi/mimo-v2.6-flash` | ✅  | $0.14/0.28 | **8.56** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-flash.md) | [responses](benchmarks/results/responses/mimo-v2.6-flash/) |
| `openai/gpt-6-luna-pro` | ❌  | $0.1/0.5 | **8.55** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna-pro.md) | [responses](benchmarks/results/responses/gpt-6-luna-pro/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **8.55** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **8.52** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `xiaomi/mimo-v2.6-pro` | ❌ MIT (pesos -RL y -MOPD; sin confirmar cuál sirve la API) | $0.435/0.87 | **8.49** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-pro.md) | [responses](benchmarks/results/responses/mimo-v2.6-pro/) |
| `openai/gpt-6.1-sol` | ❌ Proprietary | $2/10 | **8.49** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-sol.md) | [responses](benchmarks/results/responses/gpt-6.1-sol/) |
| `deepseek/deepseek-v4-pro-0813` | ✅ MIT | $0.9834/2.9502 | **8.49** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro-0813.md) | [responses](benchmarks/results/responses/deepseek-v4-pro-0813/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.214/2.55 | **8.48** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `sakana/fugu-max` | ❌ Proprietary | $2.0/6.0 | **8.47** |  | 137 | [per-model](benchmarks/results/per-model/sakana_fugu-max.md) | [responses](benchmarks/results/responses/fugu-max/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $1.6/3.2 | **8.45** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.45/2.25 | **8.43** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/kimi-k2.5-thinking/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **8.41** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `google/gemini-4-argon` | ❌ Proprietary | $2/10 | **8.38** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-4-argon.md) | [responses](benchmarks/results/responses/gemini-4-argon/) |
| `anthropic/claude-opus-5.5` | ❌ Proprietary | $4.0/20.0 | **8.38** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5_5.md) | [responses](benchmarks/results/responses/claude-opus-5.5/) |
| `z-ai/glm-5.3` | ✅ MIT | $1.4/4.4 | **8.36** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3.md) | [responses](benchmarks/results/responses/glm-5.3/) |
| `openai/gpt-6-astra` | ❌ Proprietary | $10/50 | **8.24** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-astra.md) | [responses](benchmarks/results/responses/gpt-6-astra/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **8.21** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `qwen/qwen3.8-max-0902` | ❌ Proprietary | $2.0/6.0 | **8.18** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max-0902.md) | [responses](benchmarks/results/responses/qwen-3.8-max-0902/) |
| `anthropic/claude-fable-5.2` | ❌ Proprietary | $8.0/40.0 | **8.14** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_2.md) | [responses](benchmarks/results/responses/claude-fable-5.2/) |
| `moonshotai/kimi-k3.1-pro` | ✅ Kimi K3.1 Pro License (propia de Moonshot) | $2/10 | **8.11** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3_1-pro.md) | [responses](benchmarks/results/responses/kimi-k3.1-pro/) |
| `meta/muse-wonder` | ❌ Proprietary | $4/20 | **8.01** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-wonder.md) | [responses](benchmarks/results/responses/muse-wonder/) |
| `anthropic/claude-sonnet-5.5` | ❌ Proprietary | $2.0/10.0 | **7.86** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5_5.md) | [responses](benchmarks/results/responses/claude-sonnet-5.5/) |
| `x-ai/grok-4.7` | ❌ Proprietary | $2/6 | **7.46** |  | 137 | [per-model](benchmarks/results/per-model/x-ai_grok-4_7.md) | [responses](benchmarks/results/responses/grok-4.7/) |
| `anthropic/claude-fable-5.1` | ❌ Proprietary | $10.0/50.0 | **7.30** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_1.md) | [responses](benchmarks/results/responses/claude-fable-5.1/) |

#### Mejor razonamiento

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Examen | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **8.20** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.02** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.09/0.3 | **8.00** |  | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.08/0.2 | **7.99** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `google/gemini-3.1-flash-lite` | ❌ Proprietary | $0.25/1.5 | **7.95** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite-ga/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.27/1.08 | **7.92** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `qwen/qwen3.8-flash` | ❌  | $0.15/0.47 | **7.91** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-flash.md) | [responses](benchmarks/results/responses/qwen3.8-flash/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **7.87** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.06/0.12 | **7.85** | ⭐ | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **7.84** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.81** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.80** | ⭐ | 137 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **7.78** |  | 137 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `ibm-granite/granite-4.2-8b` | ✅ Apache 2.0 | $0.06/0.25 | **7.78** |  | 137 | [per-model](benchmarks/results/per-model/ibm-granite_granite-4_2-8b.md) | [responses](benchmarks/results/responses/granite-4.2-8b/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **7.77** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.75** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **7.73** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.72** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `openai/gpt-6-luna` | ❌  | $0.1/0.5 | **7.70** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna.md) | [responses](benchmarks/results/responses/gpt-6-luna/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **7.69** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `meta/muse-ember` | ❌ Proprietary | $0.1/0.5 | **7.68** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-ember.md) | [responses](benchmarks/results/responses/muse-ember/) |
| `anthropic/claude-haiku-5.5` | ❌ Proprietary | $0.1/0.5 | **7.65** | ⭐ | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-5_5.md) | [responses](benchmarks/results/responses/claude-haiku-5.5/) |
| `upstage/solar-pro4` | ❌  | $0.09/0.36 | **7.63** |  | 137 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.62** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **7.61** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **7.58** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.6832/2.1472 | **7.57** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.088606/0.177212 | **7.55** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.1/0.9 | **7.54** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `minimax/minimax-m3.1-flash` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.075/0.3 | **7.54** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3_1-flash.md) | [responses](benchmarks/results/responses/minimax-m3.1-flash/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.54** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **7.52** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.966/3.036 | **7.49** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.3125/1.25 | **7.47** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.46** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **7.46** |  | 137 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **7.43** |  | 137 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `openai/gpt-6-luna-pro` | ❌  | $0.1/0.5 | **7.42** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna-pro.md) | [responses](benchmarks/results/responses/gpt-6-luna-pro/) |
| `xiaomi/mimo-v2.6-flash` | ✅  | $0.14/0.28 | **7.38** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-flash.md) | [responses](benchmarks/results/responses/mimo-v2.6-flash/) |
| `meta/muse-spark-1.3` | ❌  | $1.25/4.25 | **7.37** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_3.md) | [responses](benchmarks/results/responses/muse-spark-1.3/) |
| `xiaomi/mimo-v2.6-pro` | ❌ MIT (pesos -RL y -MOPD; sin confirmar cuál sirve la API) | $0.435/0.87 | **7.36** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-pro.md) | [responses](benchmarks/results/responses/mimo-v2.6-pro/) |
| `anthropic/claude-sonnet-5.5` | ❌ Proprietary | $2.0/10.0 | **7.35** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5_5.md) | [responses](benchmarks/results/responses/claude-sonnet-5.5/) |
| `z-ai/glm-5.3-flash` | ✅ MIT | $0.15/0.5 | **7.32** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3-flash.md) | [responses](benchmarks/results/responses/glm-5.3-flash/) |
| `google/gemini-4-argon` | ❌ Proprietary | $2/10 | **7.30** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-4-argon.md) | [responses](benchmarks/results/responses/gemini-4-argon/) |
| `mistralai/mistral-large-4-0` | ✅ Mistral Ecosystem Open-Weight License | $0.7/2.1 | **7.30** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-4-0.md) | [responses](benchmarks/results/responses/mistral-large-4/) |
| `openai/gpt-6.1-terra` | ❌ Proprietary | $1/5 | **7.27** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-terra.md) | [responses](benchmarks/results/responses/gpt-6.1-terra/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.55/3.5 | **7.27** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `openai/gpt-6.1-sol` | ❌ Proprietary | $2/10 | **7.23** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-sol.md) | [responses](benchmarks/results/responses/gpt-6.1-sol/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.22** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.22** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.3/2 | **7.21** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **7.21** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `x-ai/grok-4.7` | ❌ Proprietary | $2/6 | **7.18** |  | 137 | [per-model](benchmarks/results/per-model/x-ai_grok-4_7.md) | [responses](benchmarks/results/responses/grok-4.7/) |
| `deepseek/deepseek-v4.1-flash` | ✅ MIT | $0.15/0.6 | **7.17** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4_1-flash.md) | [responses](benchmarks/results/responses/deepseek-v4.1-flash/) |
| `tencent/hy4` | ❌  | $0.417/1.2505 | **7.17** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy4.md) | [responses](benchmarks/results/responses/hy4/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/2.4 | **7.17** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `sakana/fugu-max` | ❌ Proprietary | $2.0/6.0 | **7.16** |  | 137 | [per-model](benchmarks/results/per-model/sakana_fugu-max.md) | [responses](benchmarks/results/responses/fugu-max/) |
| `google/gemini-3.8-flash` | ❌ Proprietary | $0.75/3.75 | **7.13** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_8-flash.md) | [responses](benchmarks/results/responses/gemini-3.8-flash/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.214/2.55 | **7.12** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `meta/muse-wonder` | ❌ Proprietary | $4/20 | **7.10** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-wonder.md) | [responses](benchmarks/results/responses/muse-wonder/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $1.6/3.2 | **7.08** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.95/4 | **7.07** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `z-ai/glm-5.3` | ✅ MIT | $1.4/4.4 | **7.06** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3.md) | [responses](benchmarks/results/responses/glm-5.3/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **6.98** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `anthropic/claude-opus-5.5` | ❌ Proprietary | $4.0/20.0 | **6.98** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5_5.md) | [responses](benchmarks/results/responses/claude-opus-5.5/) |
| `minimax/minimax-m3` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.3/1.2 | **6.96** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.45/2.25 | **6.95** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/kimi-k2.5-thinking/) |
| `deepseek/deepseek-v4-pro-0813` | ✅ MIT | $0.9834/2.9502 | **6.89** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro-0813.md) | [responses](benchmarks/results/responses/deepseek-v4-pro-0813/) |
| `qwen/qwen3.8-max-0902` | ❌ Proprietary | $2.0/6.0 | **6.82** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max-0902.md) | [responses](benchmarks/results/responses/qwen-3.8-max-0902/) |
| `anthropic/claude-fable-5.1` | ❌ Proprietary | $10.0/50.0 | **6.82** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_1.md) | [responses](benchmarks/results/responses/claude-fable-5.1/) |
| `anthropic/claude-fable-5.2` | ❌ Proprietary | $8.0/40.0 | **6.81** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_2.md) | [responses](benchmarks/results/responses/claude-fable-5.2/) |
| `openai/gpt-6-astra` | ❌ Proprietary | $10/50 | **6.80** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-astra.md) | [responses](benchmarks/results/responses/gpt-6-astra/) |
| `moonshotai/kimi-k3.1-pro` | ✅ Kimi K3.1 Pro License (propia de Moonshot) | $2/10 | **6.53** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3_1-pro.md) | [responses](benchmarks/results/responses/kimi-k3.1-pro/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **6.43** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |

#### Mejor contenido/marketing

> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** (sin endpoint con herramientas, o no sostiene el bucle). Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).

| Modelo | OS | $ in/out | Examen | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **8.36** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.08/0.2 | **8.32** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.06/0.12 | **8.24** | ⭐ | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `google/gemini-3.1-flash-lite` | ❌ Proprietary | $0.25/1.5 | **8.22** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite-ga/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **8.20** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **8.19** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **8.14** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `ibm-granite/granite-4.2-8b` | ✅ Apache 2.0 | $0.06/0.25 | **8.13** |  | 137 | [per-model](benchmarks/results/per-model/ibm-granite_granite-4_2-8b.md) | [responses](benchmarks/results/responses/granite-4.2-8b/) |
| `anthropic/claude-haiku-5.5` | ❌ Proprietary | $0.1/0.5 | **8.12** | ⭐ | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-5_5.md) | [responses](benchmarks/results/responses/claude-haiku-5.5/) |
| `meta/muse-ember` | ❌ Proprietary | $0.1/0.5 | **8.11** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-ember.md) | [responses](benchmarks/results/responses/muse-ember/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **8.10** |  | 137 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `deepseek/deepseek-v4.1-flash` | ✅ MIT | $0.15/0.6 | **8.08** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4_1-flash.md) | [responses](benchmarks/results/responses/deepseek-v4.1-flash/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **8.06** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **8.03** |  | 137 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.3125/1.25 | **8.03** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.088606/0.177212 | **8.01** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.1/0.9 | **8.01** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.27/1.08 | **8.01** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **8.00** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **7.95** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `upstage/solar-pro4` | ❌  | $0.09/0.36 | **7.94** |  | 137 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **7.94** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `openai/gpt-6-luna-pro` | ❌  | $0.1/0.5 | **7.94** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna-pro.md) | [responses](benchmarks/results/responses/gpt-6-luna-pro/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/2.4 | **7.94** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **7.93** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **7.93** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **7.92** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.09/0.3 | **7.92** |  | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `openai/gpt-6-luna` | ❌  | $0.1/0.5 | **7.87** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna.md) | [responses](benchmarks/results/responses/gpt-6-luna/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **7.86** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **7.86** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `qwen/qwen3.8-flash` | ❌  | $0.15/0.47 | **7.85** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-flash.md) | [responses](benchmarks/results/responses/qwen3.8-flash/) |
| `tencent/hy4` | ❌  | $0.417/1.2505 | **7.85** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy4.md) | [responses](benchmarks/results/responses/hy4/) |
| `z-ai/glm-5.3-flash` | ✅ MIT | $0.15/0.5 | **7.85** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3-flash.md) | [responses](benchmarks/results/responses/glm-5.3-flash/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **7.81** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.6832/2.1472 | **7.80** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **7.79** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `xiaomi/mimo-v2.6-flash` | ✅  | $0.14/0.28 | **7.79** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-flash.md) | [responses](benchmarks/results/responses/mimo-v2.6-flash/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **7.79** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `xiaomi/mimo-v2.6-pro` | ❌ MIT (pesos -RL y -MOPD; sin confirmar cuál sirve la API) | $0.435/0.87 | **7.78** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-pro.md) | [responses](benchmarks/results/responses/mimo-v2.6-pro/) |
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **7.77** | ⭐ | 137 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **7.77** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `sakana/fugu-max` | ❌ Proprietary | $2.0/6.0 | **7.75** |  | 137 | [per-model](benchmarks/results/per-model/sakana_fugu-max.md) | [responses](benchmarks/results/responses/fugu-max/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **7.73** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.3/2 | **7.72** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.966/3.036 | **7.70** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `google/gemini-3.8-flash` | ❌ Proprietary | $0.75/3.75 | **7.69** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_8-flash.md) | [responses](benchmarks/results/responses/gemini-3.8-flash/) |
| `minimax/minimax-m3.1-flash` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.075/0.3 | **7.69** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3_1-flash.md) | [responses](benchmarks/results/responses/minimax-m3.1-flash/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $1.6/3.2 | **7.66** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `openai/gpt-6.1-terra` | ❌ Proprietary | $1/5 | **7.66** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-terra.md) | [responses](benchmarks/results/responses/gpt-6.1-terra/) |
| `meta/muse-spark-1.3` | ❌  | $1.25/4.25 | **7.66** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_3.md) | [responses](benchmarks/results/responses/muse-spark-1.3/) |
| `mistralai/mistral-large-4-0` | ✅ Mistral Ecosystem Open-Weight License | $0.7/2.1 | **7.65** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-4-0.md) | [responses](benchmarks/results/responses/mistral-large-4/) |
| `deepseek/deepseek-v4-pro-0813` | ✅ MIT | $0.9834/2.9502 | **7.63** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro-0813.md) | [responses](benchmarks/results/responses/deepseek-v4-pro-0813/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.214/2.55 | **7.62** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.55/3.5 | **7.62** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **7.58** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.95/4 | **7.57** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **7.56** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **7.52** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `anthropic/claude-sonnet-5.5` | ❌ Proprietary | $2.0/10.0 | **7.50** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5_5.md) | [responses](benchmarks/results/responses/claude-sonnet-5.5/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **7.48** |  | 137 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.45/2.25 | **7.40** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/kimi-k2.5-thinking/) |
| `z-ai/glm-5.3` | ✅ MIT | $1.4/4.4 | **7.36** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3.md) | [responses](benchmarks/results/responses/glm-5.3/) |
| `x-ai/grok-4.7` | ❌ Proprietary | $2/6 | **7.31** |  | 137 | [per-model](benchmarks/results/per-model/x-ai_grok-4_7.md) | [responses](benchmarks/results/responses/grok-4.7/) |
| `google/gemini-4-argon` | ❌ Proprietary | $2/10 | **7.29** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-4-argon.md) | [responses](benchmarks/results/responses/gemini-4-argon/) |
| `meta/muse-wonder` | ❌ Proprietary | $4/20 | **7.27** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-wonder.md) | [responses](benchmarks/results/responses/muse-wonder/) |
| `openai/gpt-6.1-sol` | ❌ Proprietary | $2/10 | **7.27** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-sol.md) | [responses](benchmarks/results/responses/gpt-6.1-sol/) |
| `moonshotai/kimi-k3.1-pro` | ✅ Kimi K3.1 Pro License (propia de Moonshot) | $2/10 | **7.25** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3_1-pro.md) | [responses](benchmarks/results/responses/kimi-k3.1-pro/) |
| `anthropic/claude-opus-5.5` | ❌ Proprietary | $4.0/20.0 | **7.16** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5_5.md) | [responses](benchmarks/results/responses/claude-opus-5.5/) |
| `qwen/qwen3.8-max-0902` | ❌ Proprietary | $2.0/6.0 | **7.16** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max-0902.md) | [responses](benchmarks/results/responses/qwen-3.8-max-0902/) |
| `anthropic/claude-fable-5.2` | ❌ Proprietary | $8.0/40.0 | **7.04** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_2.md) | [responses](benchmarks/results/responses/claude-fable-5.2/) |
| `anthropic/claude-fable-5.1` | ❌ Proprietary | $10.0/50.0 | **7.01** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_1.md) | [responses](benchmarks/results/responses/claude-fable-5.1/) |
| `minimax/minimax-m3` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.3/1.2 | **6.81** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `openai/gpt-6-astra` | ❌ Proprietary | $10/50 | **6.78** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-astra.md) | [responses](benchmarks/results/responses/gpt-6-astra/) |

#### Calidad por dólar — cuánta calidad rinde cada peso (calidad ÷ $/1k calls; premia lo barato a propósito, mira la columna Calidad)

| Modelo | OS | $ in/out | Calidad/$ | Frontera | Runs | Per-model MD | Responses |

| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `inclusionai/ling-3.0-flash` | ✅ MIT | $0.021/0.063 | **87.62** | ⭐ | 137 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash.md) | [responses](benchmarks/results/responses/ling-3.0-flash/) |
| `deepseek/deepseek-v4-flash-0731` | ✅  | $0.06/0.12 | **44.14** | ⭐ | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash-0731.md) | [responses](benchmarks/results/responses/deepseek-v4-flash-0731/) |
| `qwen/qwen3.7-flash` | ❌  | $0.03/0.13 | **42.60** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-flash.md) | [responses](benchmarks/results/responses/qwen3.7-flash/) |
| `meta-llama/llama-3.1-8b-instruct` | ✅ Llama Community | $0.05/0.08 | **39.33** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_1-8b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.1-8b/) |
| `openai/gpt-oss-20b` | ✅ Apache 2.0 | $0.029/0.14 | **30.87** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-20b.md) | [responses](benchmarks/results/responses/groq-gpt-oss-20b/) |
| `deepseek/deepseek-v4-flash` | ✅ MIT | $0.088606/0.177212 | **29.14** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-flash.md) | [responses](benchmarks/results/responses/deepseek-v4-flash/) |
| `openai/gpt-oss-120b` | ✅ Apache 2.0 | $0.036/0.18 | **26.48** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-oss-120b.md) | [responses](benchmarks/results/responses/or-gpt-oss-120b/) |
| `nvidia/nemotron-3-nano-30b-a3b` | ✅ NVIDIA Open | $0.05/0.2 | **22.73** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-30b-a3b.md) | [responses](benchmarks/results/responses/nemotron-nano/) |
| `nvidia/nemotron-3.5-lightning` | ✅  | $0.08/0.2 | **22.16** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3_5-lightning.md) | [responses](benchmarks/results/responses/nemotron-3.5-lightning/) |
| `ibm-granite/granite-4.2-8b` | ✅ Apache 2.0 | $0.06/0.25 | **20.15** |  | 137 | [per-model](benchmarks/results/per-model/ibm-granite_granite-4_2-8b.md) | [responses](benchmarks/results/responses/granite-4.2-8b/) |
| `mistralai/ministral-14b-2512` | ✅ Apache 2.0 | $0.2/0.2 | **19.22** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_ministral-14b-2512.md) | [responses](benchmarks/results/responses/or-ministral-14b/) |
| `xiaomi/mimo-v2.6-flash` | ✅  | $0.14/0.28 | **18.83** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-flash.md) | [responses](benchmarks/results/responses/mimo-v2.6-flash/) |
| `minimax/minimax-m3.1-flash` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.075/0.3 | **17.69** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3_1-flash.md) | [responses](benchmarks/results/responses/minimax-m3.1-flash/) |
| `stepfun/step-3.5-flash` | ✅ Apache 2.0 | $0.1/0.3 | **17.02** |  | 137 | [per-model](benchmarks/results/per-model/stepfun_step-3_5-flash.md) | [responses](benchmarks/results/responses/or-step-3.5-flash/) |
| `google/gemma-4-26b-a4b-it` | ✅ Apache 2.0 | $0.09/0.3 | **15.68** |  | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-26b-a4b-it.md) | [responses](benchmarks/results/responses/gemma-4-26b/) |
| `google/gemma-4-31b-it` | ✅ Gemma Terms | $0.1/0.34 | **15.46** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemma-4-31b-it.md) | [responses](benchmarks/results/responses/nim-gemma-4-31b/) |
| `nvidia/nemotron-3-super-120b-a12b` | ✅ NVIDIA Open | $0.085/0.4 | **14.05** | ⭐ | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-super-120b-a12b.md) | [responses](benchmarks/results/responses/nemotron-super/) |
| `upstage/solar-pro4` | ❌  | $0.09/0.36 | **13.56** |  | 137 | [per-model](benchmarks/results/per-model/upstage_solar-pro4.md) | [responses](benchmarks/results/responses/solar-pro4/) |
| `deepseek/deepseek-v3.2` | ✅ MIT | $0.269/0.4 | **12.16** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v3_2.md) | [responses](benchmarks/results/responses/or-deepseek-v3/) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ Llama Community | $0.1/0.32 | **12.06** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-3_3-70b-instruct.md) | [responses](benchmarks/results/responses/or-llama-3.3-70b/) |
| `qwen/qwen3.8-flash` | ❌  | $0.15/0.47 | **11.88** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-flash.md) | [responses](benchmarks/results/responses/qwen3.8-flash/) |
| `z-ai/glm-5.3-flash` | ✅ MIT | $0.15/0.5 | **11.17** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3-flash.md) | [responses](benchmarks/results/responses/glm-5.3-flash/) |
| `openai/gpt-6-luna` | ❌  | $0.1/0.5 | **11.17** | ⭐ | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna.md) | [responses](benchmarks/results/responses/gpt-6-luna/) |
| `anthropic/claude-haiku-5.5` | ❌ Proprietary | $0.1/0.5 | **11.12** | ⭐ | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-5_5.md) | [responses](benchmarks/results/responses/claude-haiku-5.5/) |
| `meta/muse-ember` | ❌ Proprietary | $0.1/0.5 | **11.08** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-ember.md) | [responses](benchmarks/results/responses/muse-ember/) |
| `openai/gpt-6-luna-pro` | ❌  | $0.1/0.5 | **9.94** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-luna-pro.md) | [responses](benchmarks/results/responses/gpt-6-luna-pro/) |
| `deepseek/deepseek-v4.1-flash` | ✅ MIT | $0.15/0.6 | **9.16** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4_1-flash.md) | [responses](benchmarks/results/responses/deepseek-v4.1-flash/) |
| `tencent/hy3` | ✅  | $0.132/0.528 | **9.03** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy3.md) | [responses](benchmarks/results/responses/tencent-hy3/) |
| `mistralai/mistral-small-2603` | ✅ Apache 2.0 | $0.15/0.6 | **8.42** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-small-2603.md) | [responses](benchmarks/results/responses/mistral-small-4/) |
| `qwen/qwen3-coder-next` | ✅ Apache 2.0 | $0.11/0.8 | **6.48** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder-next.md) | [responses](benchmarks/results/responses/qwen3-coder-next/) |
| `xiaomi/mimo-v2.6-pro` | ❌ MIT (pesos -RL y -MOPD; sin confirmar cuál sirve la API) | $0.435/0.87 | **6.16** |  | 137 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_6-pro.md) | [responses](benchmarks/results/responses/mimo-v2.6-pro/) |
| `qwen/qwen3.6-35b-a3b` | ✅ Apache 2.0 | $0.1/0.9 | **6.14** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-35b-a3b.md) | [responses](benchmarks/results/responses/qwen3.6-35b/) |
| `meta-llama/llama-4-maverick` | ✅ Llama Community | $0.2/0.696 | **5.43** |  | 137 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-maverick.md) | [responses](benchmarks/results/responses/llama-4-maverick/) |
| `minimax/minimax-m2.5` | ✅ MIT | $0.27/1.08 | **4.99** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_5.md) | [responses](benchmarks/results/responses/or-minimax-m2.5/) |
| `thinkingmachines/inkling-small` | ✅  | $0.45/1.2 | **4.42** |  | 137 | [per-model](benchmarks/results/per-model/thinkingmachines_inkling-small.md) | [responses](benchmarks/results/responses/inkling-small/) |
| `minimax/minimax-m3` | ✅ MiniMax Community License (propia de MiniMax, no MIT) | $0.3/1.2 | **4.41** |  | 137 | [per-model](benchmarks/results/per-model/minimax_minimax-m3.md) | [responses](benchmarks/results/responses/minimax-m3/) |
| `tencent/hy4` | ❌  | $0.417/1.2505 | **4.36** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy4.md) | [responses](benchmarks/results/responses/hy4/) |
| `qwen/qwen3-next-80b-a3b-instruct` | ✅ Apache 2.0 | $0.09/1.1 | **4.35** | ⭐ | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-instruct.md) | [responses](benchmarks/results/responses/nim-qwen3-next-instruct/) |
| `qwen/qwen3.5-35b-a3b` | ✅ Apache 2.0 | $0.3125/1.25 | **3.94** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-35b-a3b.md) | [responses](benchmarks/results/responses/or-qwen-3.5-35b/) |
| `meta/muse-glimmer-30b` | ✅  | $0.35/1.5 | **3.74** | ⭐ | 137 | [per-model](benchmarks/results/per-model/meta_muse-glimmer-30b.md) | [responses](benchmarks/results/responses/muse-glimmer-30b/) |
| `google/gemini-3.1-flash-lite` | ❌ Proprietary | $0.25/1.5 | **3.49** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite-ga/) |
| `qwen/qwen3.6-plus` | ❌ Proprietary | $0.325/1.95 | **2.90** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-plus.md) | [responses](benchmarks/results/responses/qwen-3.6-plus/) |
| `z-ai/glm-5` | ✅ MIT | $0.6/1.92 | **2.90** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5.md) | [responses](benchmarks/results/responses/or-glm5/) |
| `qwen/qwen3.6-27b` | ✅ Apache 2.0 | $0.3/2 | **2.85** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_6-27b.md) | [responses](benchmarks/results/responses/qwen3.6-27b/) |
| `mistralai/mistral-large-4-0` | ✅ Mistral Ecosystem Open-Weight License | $0.7/2.1 | **2.62** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-4-0.md) | [responses](benchmarks/results/responses/mistral-large-4/) |
| `z-ai/glm-5.2` | ✅ MIT | $0.6832/2.1472 | **2.61** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_2.md) | [responses](benchmarks/results/responses/glm-5.2/) |
| `moonshotai/kimi-k2.5` | ✅ Modified MIT | $0.45/2.25 | **2.49** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_5.md) | [responses](benchmarks/results/responses/kimi-k2.5-thinking/) |
| `moonshotai/kimi-k2` | ✅ Modified MIT | $0.57/2.3 | **2.32** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2.md) | [responses](benchmarks/results/responses/kimi-k2/) |
| `qwen/qwen3.8-27b` | ✅ Apache 2.0 | $0.214/2.55 | **2.29** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-27b.md) | [responses](benchmarks/results/responses/qwen-3.8-27b/) |
| `google/gemini-3.5-flash-lite` | ❌ Proprietary | $0.3/2.5 | **2.26** | ⭐ | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-3.5-flash-lite/) |
| `nvidia/nemotron-3-ultra-550b-a55b` | ✅ NVIDIA Open Model | $0.6/2.4 | **2.16** |  | 137 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-ultra-550b-a55b.md) | [responses](benchmarks/results/responses/openrouter-nemotron-3-ultra-550b/) |
| `deepseek/deepseek-v4-pro-0813` | ✅ MIT | $0.9834/2.9502 | **1.86** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro-0813.md) | [responses](benchmarks/results/responses/deepseek-v4-pro-0813/) |
| `bytedance-seed/seed-2.0-code` | ❌  | $0.5/3.0 | **1.85** |  | 137 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2_0-code.md) | [responses](benchmarks/results/responses/seed-2.0-code/) |
| `z-ai/glm-5.1` | ✅ MIT | $0.966/3.036 | **1.82** |  | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_1.md) | [responses](benchmarks/results/responses/glm-5.1/) |
| `deepseek/deepseek-v4-pro` | ✅ MIT | $1.6/3.2 | **1.63** |  | 137 | [per-model](benchmarks/results/per-model/deepseek_deepseek-v4-pro.md) | [responses](benchmarks/results/responses/deepseek-v4-pro/) |
| `qwen/qwen3.5-397b-a17b` | ✅ Apache 2.0 | $0.55/3.5 | **1.62** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_5-397b-a17b.md) | [responses](benchmarks/results/responses/nim-qwen3.5-397b/) |
| `moonshotai/kimi-k2.7-code` | ✅ Modified MIT | $0.7/3.5 | **1.59** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_7-code.md) | [responses](benchmarks/results/responses/kimi-k2.7-code/) |
| `google/gemini-3.8-flash` | ❌ Proprietary | $0.75/3.75 | **1.50** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_8-flash.md) | [responses](benchmarks/results/responses/gemini-3.8-flash/) |
| `moonshotai/kimi-k2.6` | ✅ Modified MIT | $0.95/4 | **1.39** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2_6.md) | [responses](benchmarks/results/responses/kimi-k2.6/) |
| `meta/muse-spark-1.3` | ❌  | $1.25/4.25 | **1.31** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_3.md) | [responses](benchmarks/results/responses/muse-spark-1.3/) |
| `z-ai/glm-5.3` | ✅ MIT | $1.4/4.4 | **1.28** | ⭐ | 137 | [per-model](benchmarks/results/per-model/z-ai_glm-5_3.md) | [responses](benchmarks/results/responses/glm-5.3/) |
| `openai/gpt-6.1-terra` | ❌ Proprietary | $1/5 | **1.10** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-terra.md) | [responses](benchmarks/results/responses/gpt-6.1-terra/) |
| `qwen/qwen3.8-max-0902` | ❌ Proprietary | $2.0/6.0 | **0.93** |  | 137 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max-0902.md) | [responses](benchmarks/results/responses/qwen-3.8-max-0902/) |
| `sakana/fugu-max` | ❌ Proprietary | $2.0/6.0 | **0.91** |  | 137 | [per-model](benchmarks/results/per-model/sakana_fugu-max.md) | [responses](benchmarks/results/responses/fugu-max/) |
| `x-ai/grok-4.7` | ❌ Proprietary | $2/6 | **0.90** |  | 137 | [per-model](benchmarks/results/per-model/x-ai_grok-4_7.md) | [responses](benchmarks/results/responses/grok-4.7/) |
| `google/gemini-4-argon` | ❌ Proprietary | $2/10 | **0.57** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-4-argon.md) | [responses](benchmarks/results/responses/gemini-4-argon/) |
| `moonshotai/kimi-k3.1-pro` | ✅ Kimi K3.1 Pro License (propia de Moonshot) | $2/10 | **0.57** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3_1-pro.md) | [responses](benchmarks/results/responses/kimi-k3.1-pro/) |
| `anthropic/claude-sonnet-5.5` | ❌ Proprietary | $2.0/10.0 | **0.56** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5_5.md) | [responses](benchmarks/results/responses/claude-sonnet-5.5/) |
| `openai/gpt-6.1-sol` | ❌ Proprietary | $2/10 | **0.56** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6_1-sol.md) | [responses](benchmarks/results/responses/gpt-6.1-sol/) |
| `anthropic/claude-opus-5.5` | ❌ Proprietary | $4.0/20.0 | **0.28** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5_5.md) | [responses](benchmarks/results/responses/claude-opus-5.5/) |
| `meta/muse-wonder` | ❌ Proprietary | $4/20 | **0.28** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-wonder.md) | [responses](benchmarks/results/responses/muse-wonder/) |
| `anthropic/claude-fable-5.2` | ❌ Proprietary | $8.0/40.0 | **0.14** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_2.md) | [responses](benchmarks/results/responses/claude-fable-5.2/) |
| `anthropic/claude-fable-5.1` | ❌ Proprietary | $10.0/50.0 | **0.11** |  | 137 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5_1.md) | [responses](benchmarks/results/responses/claude-fable-5.1/) |
| `openai/gpt-6-astra` | ❌ Proprietary | $10/50 | **0.11** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-6-astra.md) | [responses](benchmarks/results/responses/gpt-6-astra/) |

#### Vía suscripción Claude — plano propio (comparables entre sí)

> Medidos aprovechando la **suscripción de Claude Code** (costo marginal $0), todos por el mismo camino → **comparables entre ellos**. Ese camino arrastra ~8.8K tokens de scaffolding del CLI y **deprime la nota**: en los 2 modelos medidos por ambos caminos, la calidad por API dio **+0.15 y +0.22 más** que por suscripción. Leé estos números como **piso conservador**, no como techo — y no los compares 1:1 contra la tabla principal (la latencia por CLI es 2.5-4× peor y no es del modelo). Sirven para la pregunta de quien ya paga el plan: *¿qué modelo uso dentro de mi suscripción?*

| Modelo | Examen (piso) | Velocidad | Runs | Per-model MD | Responses |
|---|---:|---:|---:|---|---|
| `claude-sonnet-5` | **8.82** | 58 tok/s | 117 | [per-model](benchmarks/results/per-model/claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5-sub/) |
| `claude-fable-5` | **8.66** | 60 tok/s | 96 | [per-model](benchmarks/results/per-model/claude-fable-5.md) | [responses](benchmarks/results/responses/claude-fable-5-sub/) |
| `claude-opus-4-8` | **8.47** | 61 tok/s | 103 | [per-model](benchmarks/results/per-model/claude-opus-4-8.md) | [responses](benchmarks/results/responses/claude-opus-4.8-sub/) |
| `claude-sonnet-4-6` | **8.42** | 51 tok/s | 87 | [per-model](benchmarks/results/per-model/claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6-sub/) |
| `claude-haiku-4-5` | **8.42** | 103 tok/s | 80 | [per-model](benchmarks/results/per-model/claude-haiku-4-5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5-sub/) |
| `claude-opus-4-7` | **8.41** | 56 tok/s | 64 | [per-model](benchmarks/results/per-model/claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7-sub/) |
| `claude-opus-5` | **8.40** | 48 tok/s | 107 | [per-model](benchmarks/results/per-model/claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5-sub/) |

#### Variantes de proveedor (36 mediciones)

> El mismo modelo servido por otra infraestructura (Groq, NVIDIA NIM, Ollama Cloud, API directa del proveedor, self-hosted). **No compiten acá** — comparar infra contra infra es otra pregunta, y tiene su propia página: [el proveedor te cambia el modelo](https://benchmarks.cristiantala.com/mismo-modelo-distinto-proveedor/). El caso extremo medido: el mismo Qwen 3.5 397B da **7.96 en NVIDIA NIM y 5.46 en Ollama Cloud** — 2.5 puntos por la infraestructura, no por el modelo.

#### En evaluación — muestra parcial (<50 runs, NO rankeados)

> Estos modelos tienen menos runs que el piso del ranking, así que su score es **indicativo, no comparable**: con pocas muestras la varianza permite que un modelo quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** en las tablas de arriba hasta completar la cobertura.

| Modelo | OS | $ in/out | Calidad (indic.) | Frontera | Runs | Per-model MD | Responses |
|---|---|---:|---:|:-:|---:|---|---|
| `openai/gpt-5.6-luna` | ❌  | $0.2/1.2 | **8.94** |  | 154 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna.md) | [responses](benchmarks/results/responses/gpt-5.6-luna/) |
| `anthropic/claude-opus-4-6` | ❌  | $5.0/25.0 | **8.92** |  | 207 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-6.md) | [responses](benchmarks/results/responses/claude-opus-4.6/) |
| `anthropic/claude-opus-4.8` | ❌  | $5.0/25.0 | **8.88** |  | 159 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4_8.md) | [responses](benchmarks/results/responses/claude-opus-4.8/) |
| `moonshotai/kimi-k3` | ✅  | $2.64814/13.2827 | **8.87** |  | 137 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k3.md) | [responses](benchmarks/results/responses/kimi-k3/) |
| `openai/gpt-5.6-sol` | ❌  | $2/10 | **8.86** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-sol.md) | [responses](benchmarks/results/responses/gpt-5.6-sol/) |
| `anthropic/claude-fable-5` | ❌ Proprietary | $10.0/50.0 | **8.84** |  | 189 | [per-model](benchmarks/results/per-model/anthropic_claude-fable-5.md) | [responses](benchmarks/results/responses/or-claude-fable-5/) |
| `google/gemini-3.1-pro-preview` | ❌  | $2.0/12.0 | **8.82** |  | 137 | [per-model](benchmarks/results/per-model/google_gemini-3_1-pro-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-pro/) |
| `anthropic/claude-opus-4-7` | ❌  | $5.0/25.0 | **8.81** |  | 204 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-4-7.md) | [responses](benchmarks/results/responses/claude-opus-4.7/) |
| `gpt-5.4` | ❌  | $5.0/15.0 | **8.81** |  | 142 | [per-model](benchmarks/results/per-model/gpt-5_4.md) | [responses](benchmarks/results/responses/gpt-5.4/) |
| `x-ai/grok-4.6` | ❌ Proprietary | $2.0/6.0 | **8.77** |  | 137 | [per-model](benchmarks/results/per-model/x-ai_grok-4_6.md) | [responses](benchmarks/results/responses/grok-4.6/) |
| `qwen/qwen3.8-max` | ❌ Proprietary | $2.0/6.0 | **8.77** |  | 277 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-max.md) | [responses](benchmarks/results/responses/qwen-3.8-max/) |
| `qwen/qwen3.7-max` | ❌ Proprietary | $1.475/4.425 | **8.77** |  | 149 | [per-model](benchmarks/results/per-model/qwen_qwen3_7-max.md) | [responses](benchmarks/results/responses/qwen-3.7-max/) |
| `qwen/qwen3.8-2.4t-a95b` | ✅ Licencia Qwen 3.8 Max (propia de Alibaba) | $2.0/6.0 | **8.75** |  | 277 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-2_4t-a95b.md) | [responses](benchmarks/results/responses/qwen-3.8-2.4t/) |
| `anthropic/claude-sonnet-5` | ❌  | $2.0/10.0 | **8.74** |  | 233 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-5.md) | [responses](benchmarks/results/responses/claude-sonnet-5/) |
| `anthropic/claude-opus-5-fast` | ❌  | $10.0/50.0 | **8.71** |  | 427 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5-fast.md) | [responses](benchmarks/results/responses/claude-opus-5-fast/) |
| `google/gemini-3.7-flash` | ❌ Proprietary | $0.75/3.75 | **8.70** |  | 482 | [per-model](benchmarks/results/per-model/google_gemini-3_7-flash.md) | [responses](benchmarks/results/responses/gemini-3.7-flash/) |
| `openai/gpt-5.6-terra` | ❌  | $2/12 | **8.70** |  | 137 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra.md) | [responses](benchmarks/results/responses/gpt-5.6-terra/) |
| `bytedance-seed/seed-2-1-turbo` | ❌  | $0.5/2.5 | **8.69** |  | 510 | [per-model](benchmarks/results/per-model/bytedance-seed_seed-2-1-turbo.md) | [responses](benchmarks/results/responses/seed-2-1-turbo/) |
| `google/gemini-3.6-flash` | ❌  | $0.75/3.75 | **8.68** |  | 222 | [per-model](benchmarks/results/per-model/google_gemini-3_6-flash.md) | [responses](benchmarks/results/responses/gemini-3.6-flash/) |
| `tencent/hy4-preview` | ✅ Apache 2.0 | $0.83/2.5 | **8.68** |  | 137 | [per-model](benchmarks/results/per-model/tencent_hy4-preview.md) | [responses](benchmarks/results/responses/hy4-preview/) |
| `xiaomi/mimo-v2.5-pro` | ✅ MIT | $0.435/0.87 | **8.67** |  | 151 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5-pro.md) | [responses](benchmarks/results/responses/mimo-v2.5-pro-or/) |
| `anthropic/claude-haiku-4.5` | ❌  | $1.0/5.0 | **8.66** |  | 151 | [per-model](benchmarks/results/per-model/anthropic_claude-haiku-4_5.md) | [responses](benchmarks/results/responses/claude-haiku-4.5/) |
| `anthropic/claude-opus-5` | ❌  | $5.0/25.0 | **8.66** |  | 337 | [per-model](benchmarks/results/per-model/anthropic_claude-opus-5.md) | [responses](benchmarks/results/responses/claude-opus-5/) |
| `meta/muse-spark-1.2` | ❌  | $1.25/4.25 | **8.66** |  | 137 | [per-model](benchmarks/results/per-model/meta_muse-spark-1_2.md) | [responses](benchmarks/results/responses/muse-spark-1.2/) |
| `anthropic/claude-sonnet-4-6` | ❌  | $3.0/15.0 | **8.64** |  | 165 | [per-model](benchmarks/results/per-model/anthropic_claude-sonnet-4-6.md) | [responses](benchmarks/results/responses/claude-sonnet-4.6/) |
| `gpt-5.4-mini` | ❌  | $0.5/1.5 | **8.64** |  | 148 | [per-model](benchmarks/results/per-model/gpt-5_4-mini.md) | [responses](benchmarks/results/responses/gpt-5.4-mini/) |
| `gpt-5.5` | ❌  | $5.0/30.0 | **8.61** |  | 443 | [per-model](benchmarks/results/per-model/gpt-5_5.md) | [responses](benchmarks/results/responses/gpt-5.5/) |
| `xiaomi/mimo-v2.5` | ✅ MIT | $0.14/0.28 | **8.58** |  | 157 | [per-model](benchmarks/results/per-model/xiaomi_mimo-v2_5.md) | [responses](benchmarks/results/responses/mimo-v2.5-or/) |
| `x-ai/grok-4.5` | ❌  | $2.0/6.0 | **8.55** |  | 146 | [per-model](benchmarks/results/per-model/x-ai_grok-4_5.md) | [responses](benchmarks/results/responses/grok-4.5/) |
| `mistralai/mistral-large-2512` | ✅ Apache 2.0 | $0.5/1.5 | **8.48** |  | 137 | [per-model](benchmarks/results/per-model/mistralai_mistral-large-2512.md) | [responses](benchmarks/results/responses/or-mistral-large-3/) |
| `google/gemini-2.5-flash` | ❌  | $0.3/2.5 | **8.41** |  | 156 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash.md) | [responses](benchmarks/results/responses/gemini-flash/) |
| `google/gemini-3.1-flash-lite-preview` | ❌  | $0.25/1.5 | **8.41** |  | 157 | [per-model](benchmarks/results/per-model/google_gemini-3_1-flash-lite-preview.md) | [responses](benchmarks/results/responses/gemini-3.1-flash-lite/) |
| `minimax/minimax-m2.7` | ✅ Licencia propia de MiniMax | $0.3/1.2 | **8.39** |  | 211 | [per-model](benchmarks/results/per-model/minimax_minimax-m2_7.md) | [responses](benchmarks/results/responses/minimax-m2.7/) |
| `mistralai/mistral-large` | ❌ MRL (no comercial) | $2.0/6.0 | **8.36** |  | 159 | [per-model](benchmarks/results/per-model/mistralai_mistral-large.md) | [responses](benchmarks/results/responses/mistral-large/) |
| `gpt-4.1-mini` | ❌  | $0.4/1.6 | **8.29** |  | 156 | [per-model](benchmarks/results/per-model/gpt-4_1-mini.md) | [responses](benchmarks/results/responses/gpt-4.1-mini/) |
| `x-ai/grok-4.3` | ❌  | $1.25/2.5 | **8.29** |  | 147 | [per-model](benchmarks/results/per-model/x-ai_grok-4_3.md) | [responses](benchmarks/results/responses/grok-4.3/) |
| `google/gemini-3.5-flash` | ❌  | $1.5/9.0 | **8.12** |  | 160 | [per-model](benchmarks/results/per-model/google_gemini-3_5-flash.md) | [responses](benchmarks/results/responses/gemini-3.5-flash/) |
| `x-ai/grok-4.20` | ❌  | $1.25/2.5 | **8.00** |  | 140 | [per-model](benchmarks/results/per-model/x-ai_grok-4_20.md) | [responses](benchmarks/results/responses/grok-4.20/) |
| `google/gemini-2.5-pro` | ❌  | $1.25/10.0 | **7.95** |  | 173 | [per-model](benchmarks/results/per-model/google_gemini-2_5-pro.md) | [responses](benchmarks/results/responses/gemini-pro/) |
| `qwen/qwen3-coder` | ✅ Apache 2.0 | $0.3/1 | **7.92** |  | 156 | [per-model](benchmarks/results/per-model/qwen_qwen3-coder.md) | [responses](benchmarks/results/responses/qwen3-coder/) |
| `deepseek/deepseek-chat` | ✅ DeepSeek Model License (código MIT) | $0.2574/1.0287 | **7.91** |  | 264 | [per-model](benchmarks/results/per-model/deepseek_deepseek-chat.md) | [responses](benchmarks/results/responses/deepseek-v3/) |
| `gpt-4.1` | ❌  | $2.0/8.0 | **7.27** |  | 157 | [per-model](benchmarks/results/per-model/gpt-4_1.md) | [responses](benchmarks/results/responses/gpt-4.1/) |
| `google/gemini-2.5-flash-lite` | ❌  | $0.1/0.4 | **7.17** |  | 147 | [per-model](benchmarks/results/per-model/google_gemini-2_5-flash-lite.md) | [responses](benchmarks/results/responses/gemini-flash-lite/) |
| `meta-llama/llama-4-scout` | ✅ Llama Community | $0.1/0.3 | **7.05** |  | 142 | [per-model](benchmarks/results/per-model/meta-llama_llama-4-scout.md) | [responses](benchmarks/results/responses/or-llama-4-scout/) |
| `liquid/lfm-3-1.7b` | ✅ LFM Open License v1.0 | $0.08/0.2 | **6.87** |  | 137 | [per-model](benchmarks/results/per-model/liquid_lfm-3-1_7b.md) | [responses](benchmarks/results/responses/lfm-3-1.7b/) |
| `nousresearch/hermes-4-405b` | ✅ Llama 3 community | $1.0/3.0 | **6.20** ⛔ |  | 460 | [per-model](benchmarks/results/per-model/nousresearch_hermes-4-405b.md) | [responses](benchmarks/results/responses/hermes-4-405b/) |
| `qwen/qwen3-next-80b-a3b-thinking` | ✅ Apache 2.0 | $0.15/1.2 | **5.66** ⛔ |  | 150 | [per-model](benchmarks/results/per-model/qwen_qwen3-next-80b-a3b-thinking.md) | [responses](benchmarks/results/responses/nim-qwen3-next-thinking/) |
| `mistralai/mistral-nemo` | ✅ Apache 2.0 | $0.02/0.02 | **—** |  | 498 | [per-model](benchmarks/results/per-model/mistralai_mistral-nemo.md) | [responses](benchmarks/results/responses/mistral-nemo/) |
| `meituan/longcat-2.0` | ❌  | $0.3/1.2 | **—** |  | 22 | [per-model](benchmarks/results/per-model/meituan_longcat-2_0.md) | [responses](benchmarks/results/responses/longcat-2.0/) |
| `sakana/sakana-namazu` | ❌  | $0.95/4.0 | **—** |  | 1584 | [per-model](benchmarks/results/per-model/sakana_sakana-namazu.md) | [responses](benchmarks/results/responses/sakana-namazu/) |
| `prism-ml/ternary-bonsai-2-27b` | ❌  | $0.075/0.5 | **—** |  | 93 | [per-model](benchmarks/results/per-model/prism-ml_ternary-bonsai-2-27b.md) | [responses](benchmarks/results/responses/bonsai-2-27b/) |
| `qwen/qwen3.8-omni-flash` | ❌  | $0.15/0.47 | **—** |  | 104 | [per-model](benchmarks/results/per-model/qwen_qwen3_8-omni-flash.md) | [responses](benchmarks/results/responses/qwen3.8-omni-flash/) |
| `inclusionai/ling-3.0-flash-vl` | ✅ MIT | $0.06/0.18 | **—** |  | 137 | [per-model](benchmarks/results/per-model/inclusionai_ling-3_0-flash-vl.md) | [responses](benchmarks/results/responses/ling-3.0-flash-vl/) |
| `openai/gpt-5.6-luna-pro` | ❌  | $0.2/1.2 | **—** |  | 252 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-luna-pro.md) | [responses](benchmarks/results/responses/gpt-5.6-luna-pro/) |
| `openai/gpt-5.6-terra-pro` | ❌  | $2/12 | **—** |  | 263 | [per-model](benchmarks/results/per-model/openai_gpt-5_6-terra-pro.md) | [responses](benchmarks/results/responses/gpt-5.6-terra-pro/) |
| `nvidia/nemotron-nano-9b-v2:free` | ✅ NVIDIA Open License | $0.05/0.2 | **—** |  | 128 | [per-model](benchmarks/results/per-model/nvidia_nemotron-nano-9b-v2_free.md) | [responses](benchmarks/results/responses/or-nemotron-nano-9b-v2/) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ NVIDIA Open License | $0.1/0.4 | **—** |  | 141 | [per-model](benchmarks/results/per-model/nvidia_nemotron-3-nano-omni-30b-a3b-reasoning_free.md) | [responses](benchmarks/results/responses/or-nemotron-3-nano-omni-reasoning/) |
| `qwen/qwen-2.5-72b-instruct` | ✅ Apache 2.0 | $0.36/0.4 | **—** |  | 161 | [per-model](benchmarks/results/per-model/qwen_qwen-2_5-72b-instruct.md) | [responses](benchmarks/results/responses/or-qwen-2.5-72b/) |
| `moonshotai/kimi-k2-thinking` | ✅ Modified MIT | $0.6/2.5 | **—** |  | 2 | [per-model](benchmarks/results/per-model/moonshotai_kimi-k2-thinking.md) | [responses](benchmarks/results/responses/nim-kimi-k2-thinking/) |

#### Retirados — fuera del ranking y de las recomendaciones

> **Un modelo que no puedes usar no es un candidato.** Sus números son reales y quedan acá por transparencia (alimentan el análisis histórico), pero no compiten. Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera, y Nemotron Super 49B v1.5 estaba **#8** el día que NVIDIA lo sacó de OpenRouter.

> **`Quién`** distingue lo que decidió el proveedor de lo que decidimos nosotros: Phi-4 no lo retiró nadie, es el modelo juez y no compite. **`Sigue vivo en`** avisa cuando lo que murió fue *una ruta* y no el modelo — el caso normal, no la excepción. Y el retiro **se re-verifica** (`check_endpoints.py --recheck-retired`): el 12-ago-2026 dos modelos retirados en julio habían vuelto a responder porque un proveedor los recogió, y volvieron al catálogo.

| Modelo | Retirado | Quién | Causa | Sigue vivo en | Score (histórico) | Runs |
|---|---|---|---|---|---:|---:|
| `inception/mercury-3` | 2026-11-08 | proveedor | OpenRouter: 0 endpoints y fuera del catálogo; salió la familia Inception entera | — | **5.69** | 137 |
| `inception/mercury-2.5` | 2026-11-08 | proveedor | OpenRouter: 0 endpoints y fuera del catálogo; salió la familia Inception entera | — | **6.03** | 137 |
| `deepseek/deepseek-r1:free` | 2026-11-04 | proveedor | openrouter 404: deepseek/deepseek-r1:free is no longer available on OpenRouter: no provider serves this model anymore. See available models  | — | — | 0 |
| `nousresearch/hermes-4-70b` | 2026-11-04 | proveedor | openrouter 404: nousresearch/hermes-4-70b is no longer available on OpenRouter: no provider serves this model anymore. See available models  | — | — | 0 |
| `kwaipilot/kat-coder-pro-v2.5` | 2026-11-04 | proveedor | openrouter 404: kwaipilot/kat-coder-pro-v2.5 is no longer available on OpenRouter: no provider serves this model anymore. See available mode | — | **3.73** | 250 |
| `nousresearch/hermes-4-70b` | 2026-11-04 | proveedor | openrouter 404: nousresearch/hermes-4-70b is no longer available on OpenRouter: no provider serves this model anymore. See available models  | — | **4.26** | 469 |
| `poolside/laguna-s-2.1` | 2026-11-04 | proveedor | openrouter 404: poolside/laguna-s-2.1 is no longer available on OpenRouter: no provider serves this model anymore. See available models at h | — | **4.29** | 137 |
| `nex-agi/nex-n2-mini` | 2026-11-04 | proveedor | openrouter 404: nex-agi/nex-n2-mini is no longer available on OpenRouter: no provider serves this model anymore. See available models at htt | — | **5.90** | 137 |
| `kwaipilot/kat-coder-air-v2.5` | 2026-11-04 | proveedor | openrouter 404: kwaipilot/kat-coder-air-v2.5 is no longer available on OpenRouter: no provider serves this model anymore. See available mode | — | **5.93** | 473 |
| `qwen/qwen3.6-max-preview` | 2026-11-04 | proveedor | openrouter 404: Qwen3.6 Max Preview was deprecated on Oct 9, 2026. We recommend migrating to Qwen3.8 Max (0902) (openrouter.ai/qwen/qwen3.8- | — | **6.58** | 167 |
| `deepseek/deepseek-r1` | 2026-11-04 | proveedor | openrouter 404: deepseek/deepseek-r1 is no longer available on OpenRouter: no provider serves this model anymore. See available models at ht | — | **6.69** | 152 |
| `poolside/laguna-xs-2.1` | 2026-11-04 | proveedor | openrouter 404: poolside/laguna-xs-2.1 is no longer available on OpenRouter: no provider serves this model anymore. See available models at  | — | **6.75** | 137 |
| `stepfun-ai/step3` | 2026-08-17 | proveedor | OpenRouter: 'No endpoints found for stepfun'. El id no existe en el catálogo; la familia sigue viva en step-3.5/3.7-flash. | — | — | 0 |
| `bytedance/seed-oss-36b-instruct` | 2026-08-17 | proveedor | OpenRouter: 'No endpoints found for bytedance'. El namespace pasó a `bytedance-seed/` y Seed-OSS 36B no está en el catálogo. | — | — | 0 |
| `llama-3.1-8b-instant` | 2026-08-16 | proveedor | Groq deprecó el endpoint (anunciado el 17-jun-2026, apagado el 16-ago). Recomiendan migrar a openai/gpt-oss-20b. Ojo: era el mejor de Groq en tool calling (8,01) y el reemplazo sugerido marca 6,45. | — | **3.48** | 78 |
| `llama-3.3-70b-versatile` | 2026-08-16 | proveedor | Groq deprecó el endpoint (anunciado por correo el 17-jun-2026, apagado el 16-ago). Recomiendan migrar a openai/gpt-oss-120b o qwen/qwen3.6-27b. El modelo Llama 3.3 70B sigue vivo en OpenRouter: lo que murió es esta ruta. | — | **5.58** | 78 |
| `mistralai/devstral-2512` | 2026-08-12 | proveedor | OpenRouter 404: la familia Devstral entera salió del catálogo | — | **5.36** | 130 |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | 2026-08-12 | proveedor | OpenRouter 404 'No endpoints found'; NVIDIA movió su oferta a la familia Nemotron 3 | ✅ Nemotron Super 49B v1.5 (NIM) (86 runs) | **7.34** | 122 |
| `phi4` | 2026-07-14 | decisión propia | decisión del benchmark, no del proveedor: no compite (Phi-4 es el modelo juez) | — | — | 0 |
| `qwen3.5:cloud` | 2026-07-14 | sin registrar | sin causa registrada; fecha recuperada del historial de git | — | **2.41** | 47 |
| `mimo-v2-omni` | 2026-07-14 | sin registrar | sin causa registrada; fecha recuperada del historial de git | — | **4.55** | 68 |
| `mimo-v2-pro` | 2026-07-14 | sin registrar | sin causa registrada; fecha recuperada del historial de git | — | **6.19** | 73 |
| `xiaomi/mimo-v2-omni` | 2026-07-13 | proveedor | Xiaomi lo deprecó; recomienda migrar a MiMo V2.5 | — | **3.92** | 74 |
| `mistralai/devstral-medium` | 2026-07-13 | proveedor | OpenRouter: 'No endpoints found' | — | **5.57** | 77 |
| `x-ai/grok-4.1-fast` | 2026-07-13 | proveedor | xAI lo deprecó; recomienda migrar a Grok 4.3 | — | **5.85** | 80 |
| `xiaomi/mimo-v2-pro` | 2026-07-13 | proveedor | Xiaomi deprecó el modelo | — | **6.33** | 73 |
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
