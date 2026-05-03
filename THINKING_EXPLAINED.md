---
title: "Extended Thinking — qué es, qué modelos lo tienen, cómo lo medimos"
fecha: "2026-04-30"
audiencia: "Lectores del benchmark que ven scores de modelos thinking vs no-thinking y quieren entender la diferencia"
---

# Extended Thinking — guía rápida

> 📍 **Contexto del benchmark**: este documento explica cómo medimos thinking models en `ai-benchmarks-alternativos` — un benchmark **complementario** (no sustituto) de los oficiales (HumanEval, MMLU, GSM8K, SWE-bench), pensado para emprendedores hispanohablantes que deciden producción real. Los hallazgos sobre "thinking puede empeorar multi-turn" aplican a nuestras suites en español neutro — para validar contra literatura inglesa, ver [BENCHMARKS_EXTERNOS.md](BENCHMARKS_EXTERNOS.md).

## Qué es

**Extended thinking** (también llamado *reasoning*, *chain-of-thought interno*, *deep think*) es la capacidad de un LLM de **razonar antes de responder**, generando tokens internos de planificación que NO van directo al usuario pero que mejoran la calidad de la respuesta final en tareas complejas (matemática, lógica, planning multi-paso).

Trade-offs:

| Pro | Con |
|---|---|
| Mejor performance en razonamiento complejo (matemática, lógica formal, problemas multi-paso) | Latencia 3-10× mayor (modelo "piensa" antes de hablar) |
| Reduce alucinaciones en tareas con respuesta verificable | Costo 4-8× mayor (los reasoning tokens se facturan como output) |
| Mejor adherencia a instrucciones complejas en algunos modelos | NO siempre ayuda — empeora en tareas conversacionales y agéntica multi-turn (ver Hallazgo 2) |

## Tres tipos de modelos según thinking

### 1. Thinking-only (siempre razonan)

El modelo siempre genera tokens de reasoning, no se puede desactivar. La latencia y costo son inherentes al modelo.

Ejemplos en este benchmark:
- OpenAI: **GPT-5, GPT-5 mini, o1, o3** (toda la family GPT-5)
- DeepSeek: **DeepSeek R1, R1 distill, DeepSeek V4 Pro**
- Mistral: **Magistral Small** (post-trained para reasoning)
- NVIDIA: **Nemotron 3 Super 120B, Nemotron 3 Nano Omni Reasoning** (post-trained)
- Moonshot: **Kimi K2 Thinking** (variante explícita)
- Alibaba: **Qwen 3-Next 80B Thinking** (variante explícita)
- Google: **Gemini 2.5/3.x Pro tier** (thinking default)

### 2. Hybrid (opt-in)

El modelo PUEDE razonar, pero por default no lo hace. Hay que pasarle un parámetro explícito (`reasoning: {effort: high}` en OpenRouter, o `thinking: {type: enabled}` en API directa Anthropic).

**Anthropic Claude 4.x family** (extended thinking, abril 2025+):
- Claude Opus 4.x (4.0, 4.1, 4.5, 4.6, 4.7) — **interleaved adaptive thinking**: el modelo decide dinámicamente cuánto razonar según la dificultad. NO es exclusivo de Opus 4.7 — toda la family Claude 4.x lo tiene.
- Claude Sonnet 4.x — mismo mecanismo
- Claude Haiku 4.5 — mismo mecanismo (más limitado en budget)

**Otros hybrid medidos**:
- **Hermes 4 70B/405B** (NousResearch) — post-trained con reasoning opt-in
- **Kimi K2.5, K2.6** (Moonshot) — hybrid base, K2 Thinking es la variante always-on
- **Gemini 2.5/3.x Flash, Flash Lite** — thinking dinámico, budget controlable

### 3. Sin reasoning API (no-thinking)

El modelo NO expone parámetro `reasoning` en el API. Aunque puede generar CoT inline en el `content` cuando se le pide, no hay budget separado de reasoning_tokens.

Ejemplos: Llama 3/4 family, Mistral Small/Large/Devstral, Gemma 3/4, GPT-OSS 20B/120B, GPT-4.1, Qwen base, MiMo (la mayoría), Step 3.5 Flash, Grok 4.1 Fast.

## Cómo lo activamos en este benchmark

El adapter (`providers/adapters.py`) tiene 2 mecanismos:

### Mecanismo A — `THINKING_MODELS` tuple (automático)

Modelos cuyo `id` matchea patrones conocidos de thinking-only se tratan automáticamente como thinking:

```python
THINKING_MODELS = (
    "gpt-5", "o3", "o1",
    "glm-5", "GLM-5",
    "kimi-k2.6", "Kimi",
    "nemotron", "Nemotron",
    "gemini-2.5-pro", "gemini-3-pro",
    "deepseek-v4", "deepseek-r",
    "gemma4", "gemma-4",
)
```

Para estos modelos:
- `max_tokens` se multiplica × 4 (default 2048 → 8192) — sin esto, el modelo agota el budget razonando y devuelve content vacío
- `max_tokens` mínimo 8192 absoluto
- Capturamos el campo `reasoning` separado del `content` cuando el provider lo expone

### Mecanismo B — `force_reasoning: True` en config (manual, hybrid)

Para modelos hybrid (Claude 4.x, Hermes 4, Kimi K2.5/K2.6, Gemini 2.5/3.x) agregamos al config flag `force_reasoning: True`. El adapter:

```python
if force_reasoning:
    extra_body["reasoning"] = {"effort": "high"}
    extra_body["include_reasoning"] = True
```

`effort: "high"` se mapea (vía OpenRouter) a:
- Anthropic: ~80% del budget como thinking tokens
- OpenAI: ~80% del max output
- Gemini: thinking_budget alto
- DeepSeek: reasoning effort high

Reportamos modelo y modelo (thinking) como **entradas separadas** en el ranking — para que veas el costo del reasoning explícito y el delta de score por separado.

## Hallazgos del benchmark sobre thinking

### Hallazgo 1 — Thinking ayuda en algunos modelos

Kimi K2.5 single-turn 6.27 → con thinking forzado en agent_long_horizon **7.00** (+0.73 puntos). Confirmado para modelos diseñados como hybrid desde origen (Moonshot).

### Hallazgo 2 — Thinking EMPEORA otros modelos (sorpresa)

Hermes 4 70B single-turn 7.24 → con thinking forzado en agent_long_horizon **6.70** (-0.54 puntos). Hermes 4 405B también baja con thinking. **Hipótesis**: el reasoning explícito en modelos post-trained sobre Llama 3 puede degradar la capacidad agéntica multi-turn — el modelo "razona demasiado" y pierde foco/contexto del usuario.

### Hallazgo 3 — Thinking ON multiplica el costo

Claude Opus 4.7 con extended thinking factura ~5-7x más por test que sin. En benchmarks de 12 tests:
- Opus 4.7 sin thinking: ~$1.5 por lote
- Opus 4.7 con thinking: ~$8.10 por lote

### Hallazgo 4 — Thinking-only NO siempre top

Modelos thinking-only no son automáticamente los mejores. Ejemplos del benchmark:
- DeepSeek V4 Pro (thinking-only): 502/504 timeouts en NIM, descartado
- Magistral Small (thinking-only): error 400 en 91/91 NIM
- Nemotron 3 Nano Omni Reasoning (thinking-only): 6.97 — debajo de Gemma 4 31B (NIM) 7.20 que es no-thinking

## Implicancias para tu producción

1. **Si tu pipeline es agente multi-turn (N8N, OpenClaw)**: empezá con la variante NO-thinking. Solo activá thinking si tu task específica lo necesita (lógica formal, planning multi-paso). Para conversación, customer support, content marketing → thinking puede empeorar.

2. **Si tu task es razonamiento puro (matemática, lógica, debugging complejo)**: thinking puede ayudar. Mide ambas variantes (con y sin) en tus prompts típicos antes de comprometerte al costo extra.

3. **Para producción a volumen**: el costo extra del thinking se acumula. 1k calls/día × $8 extras por call = $8k/día. Vale la pena cuando la calidad mejora demostrablemente.

## Métodos NO usados en este benchmark (porque no aplican)

- **Anthropic API directa**: usamos OpenRouter. La API directa Anthropic permite el campo `thinking` separado pero el formato cambia. OpenRouter lo abstrae.
- **OpenAI Responses API**: la usamos para gpt-5.5-pro y o1-pro porque NO funcionan en chat/completions. Devuelve `reasoning_tokens` en metadata aparte.
- **Streaming**: nunca usamos streaming porque introduce variabilidad en los benchmarks. Mode síncrono solo.

## Referencias

- Anthropic extended thinking docs: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
- OpenRouter reasoning parameter: https://openrouter.ai/docs/use-cases/reasoning-tokens
- OpenAI reasoning models: https://platform.openai.com/docs/guides/reasoning
- Google Gemini thinking: https://ai.google.dev/gemini-api/docs/thinking
