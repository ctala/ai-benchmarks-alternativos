# Tests Faltantes por Modelo

> Tracking de cobertura del benchmark. Generado automáticamente desde los resultados JSON.
>
> **Regla**: un modelo se considera con cobertura suficiente cuando tiene ≥50 runs en tareas prácticas (sin contar niah ni prompt_injection). Este archivo lista los modelos que aún no alcanzan ese umbral o les faltan suites generales.

## Resumen

- Modelos catalogados: **125**
- Modelos con al menos un run: **114**
- Modelos con cobertura ≥50 runs: **90**
- Modelos catalogados sin runs: **16**
- Modelos con ≥50 runs pero suites faltantes: **45**
- Modelos con runs pero <50 (insuficiente): **24**

## Modelos sin runs

Hay **16** modelos catalogados que no tienen ningún run exitoso en `benchmarks/results/`.

| Modelo | Config key | ID |
|---|---|---|
| Claude Sonnet 4 | `claude-sonnet` | `anthropic/claude-sonnet-4` |
| DeepSeek R1 (free) | `deepseek-r1-free` | `deepseek/deepseek-r1:free` |
| GPT-4o | `gpt-4o` | `openai/gpt-4o` |
| GPT-4o High | `gpt-4o-high` | `openai/gpt-4o:high` |
| GPT-5.5 Pro | `gpt-5.5-pro` | `gpt-5.5-pro` |
| GPT-OSS 120B (Groq) | `groq-gpt-oss-120b` | `openai/gpt-oss-120b` |
| Grok 4.20 Multi-Agent | `grok-4.20-multi-agent` | `x-ai/grok-4.20-multi-agent` |
| Grok 4.3 | `grok-4.3` | `x-ai/grok-4.3` |
| Llama 3.3 70B (free) | `llama-3.3-70b-free` | `meta-llama/llama-3.3-70b-instruct:free` |
| MiMo-V2-Flash (free) | `mimo-v2-flash-free` | `xiaomi/mimo-v2-flash:free` |
| Nemotron Ultra 253B (NIM) | `nim-nemotron-ultra-253b` | `nvidia/llama-3.1-nemotron-ultra-253b-v1` |
| Qwen 3.5 Plus | `qwen-3.5-plus` | `qwen/qwen3.5-plus` |
| Qwen 3.6 Plus (free) | `qwen-3.6-plus-free` | `qwen/qwen3.6-plus:free` |
| Qwen3 Coder 480B (free) | `qwen3-coder-free` | `qwen/qwen3-coder-480b:free` |
| Seed-OSS 36B Instruct | `seed-oss-36b` | `bytedance/seed-oss-36b-instruct` |
| Step3 (StepFun) | `step3` | `stepfun-ai/step3` |

## Modelos con cobertura ≥50 runs y suites faltantes

### Faltan 7 suites (1 modelo)

| Modelo | ID | Runs | Suites faltantes |
|---|---|---:|---|
| Devstral 2 123B (NIM) | `mistralai/devstral-2-123b-instruct-2512` | 68 | `agent_capabilities`, `agent_long_horizon`, `policy_adherence`, `sales_outreach`, `strategy`, `summarization`, `translation` |

### Faltan 4 suites (2 modelos)

| Modelo | ID | Runs | Suites faltantes |
|---|---|---:|---|
| Claude Opus 4.7 (suscripción) | `claude-opus-4-7` | 82 | `agent_capabilities`, `policy_adherence`, `strategy`, `tool_calling` |
| Hermes 4 405B | `nousresearch/hermes-4-405b` | 74 | `agent_long_horizon`, `customer_support`, `orchestration`, `tool_calling` |

### Faltan 3 suites (1 modelo)

| Modelo | ID | Runs | Suites faltantes |
|---|---|---:|---|
| Hermes 4 70B | `nousresearch/hermes-4-70b` | 86 | `customer_support`, `orchestration`, `tool_calling` |

### Faltan 2 suites (2 modelos)

| Modelo | ID | Runs | Suites faltantes |
|---|---|---:|---|
| Devstral Medium | `mistralai/devstral-medium` | 88 | `agent_long_horizon`, `translation` |
| Llama 4 Maverick | `meta-llama/llama-4-maverick` | 134 | `agent_long_horizon`, `orchestration` |

### Faltan 1 suite (39 modelos)

| Modelo | ID | Runs | Suites faltantes |
|---|---|---:|---|
| Claude Haiku 4.5 (suscripción) | `claude-haiku-4-5` | 98 | `tool_calling` |
| Claude Opus 4.6 | `anthropic/claude-opus-4-6` | 246 | `agent_long_horizon` |
| Claude Opus 4.7 | `anthropic/claude-opus-4-7` | 182 | `agent_long_horizon` |
| Claude Opus 4.8 (suscripción) | `claude-opus-4-8` | 101 | `tool_calling` |
| Claude Sonnet 4.6 (suscripción) | `claude-sonnet-4-6` | 98 | `tool_calling` |
| Claude Sonnet 4.6 (ultimo Anthropic) | `anthropic/claude-sonnet-4-6` | 155 | `agent_long_horizon` |
| DeepSeek V3.2 | `deepseek/deepseek-chat` | 155 | `agent_long_horizon` |
| DeepSeek V4 Pro | `deepseek/deepseek-v4-pro` | 81 | `customer_support` |
| Gemini 2.5 Flash Lite | `google/gemini-2.5-flash-lite` | 155 | `agent_long_horizon` |
| Gemini 2.5 Pro | `google/gemini-2.5-pro` | 91 | `agent_long_horizon` |
| Gemma 4 26B MoE (3.8B activos) | `google/gemma-4-26b-a4b-it` | 104 | `agent_long_horizon` |
| Gemma 4 31B (DGX Spark Q4_K_M) | `gemma4:31b` | 89 | `agent_long_horizon` |
| GLM 5 (NIM) | `z-ai/glm5` | 90 | `agent_long_horizon` |
| GLM 5.1 (NIM) | `z-ai/glm-5.1` | 91 | `agent_long_horizon` |
| GLM-5.1 | `z-ai/glm-5.1` | 91 | `agent_long_horizon` |
| GPT-4.1 Mini | `gpt-4.1-mini` | 155 | `agent_long_horizon` |
| GPT-5.4 | `gpt-5.4` | 150 | `agent_long_horizon` |
| GPT-5.4 Mini | `gpt-5.4-mini` | 155 | `agent_long_horizon` |
| Grok 4.20 | `x-ai/grok-4.20` | 91 | `agent_long_horizon` |
| Kimi K2 | `moonshotai/kimi-k2` | 138 | `agent_long_horizon` |
| Kimi K2.5 (NIM) | `moonshotai/kimi-k2.5` | 91 | `agent_long_horizon` |
| Kimi K2.6 | `moonshotai/kimi-k2.6` | 182 | `agent_long_horizon` |
| MiMo-V2-Pro | `xiaomi/mimo-v2-pro` | 91 | `agent_long_horizon` |
| MiMo-V2.5 (omnimodal) | `xiaomi/mimo-v2.5` | 91 | `agent_long_horizon` |
| MiMo-V2.5 Pro | `xiaomi/mimo-v2.5-pro` | 91 | `agent_long_horizon` |
| Ministral 14B (NIM) | `mistralai/ministral-14b-instruct-2512` | 90 | `agent_long_horizon` |
| Mistral Large | `mistralai/mistral-large` | 152 | `agent_long_horizon` |
| Mistral Large 3 675B (NIM) | `mistralai/mistral-large-3-675b-instruct-2512` | 87 | `agent_long_horizon` |
| Mistral Nemo | `mistralai/mistral-nemo` | 122 | `agent_long_horizon` |
| Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM) | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | 91 | `agent_long_horizon` |
| Nemotron 3 Super | `nvidia/nemotron-3-super-120b-a12b` | 91 | `agent_long_horizon` |
| Nemotron 3 Super 120B (DGX Spark Q4_K_M) | `nemotron-3-super:120b` | 90 | `agent_long_horizon` |
| Nemotron Nano 9B v2 (NIM) | `nvidia/nvidia-nemotron-nano-9b-v2` | 91 | `agent_long_horizon` |
| Nemotron Super 49B v1.5 (NIM) | `nvidia/llama-3.3-nemotron-super-49b-v1.5` | 86 | `agent_long_horizon` |
| Qwen 3-Next 80B Thinking (NIM) | `qwen/qwen3-next-80b-a3b-thinking` | 182 | `agent_long_horizon` |
| Qwen 3.5 (Ollama Cloud default) | `qwen3.5:cloud` | 91 | `agent_long_horizon` |
| Qwen 3.5 397B (Ollama Cloud) | `qwen3.5:397b-cloud` | 94 | `agent_long_horizon` |
| Qwen 3.6 Plus | `qwen/qwen3.6-plus` | 150 | `agent_long_horizon` |
| Qwen3 Coder | `qwen/qwen3-coder` | 155 | `agent_long_horizon` |

## Modelos con runs pero <50 (cobertura insuficiente)

Hay **24** modelos/variantes con runs pero por debajo del umbral de 50. No se listan individualmente aquí; correr `python benchmarks/audit_results.py` da el detalle completo.

## Notas

- La suite **`agent_long_horizon`** es la que más falta: fue agregada en v2.4 y muchos modelos anteriores no la corrieron.
- Algunos modelos tienen **drift de IDs** en el provider (p.ej. Groq, NIM, OpenRouter) y sus runs históricos quedaron huérfanos; esos aparecen como sin runs hasta que se actualice `models.py` o se re-corran.
- Este archivo NO imputa datos: solo documenta los gaps para planificar corridas futuras.

---

> Última generación: script ad-hoc contra `benchmarks/results/*.json` y `benchmarks/config.py`.