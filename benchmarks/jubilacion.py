"""
Tracking de modelos jubilados del roster.

Este módulo contiene el conjunto JUBILADOS que lista todos los modelos
que no se vuelven a medir, según docs/jubilacion-2026-10.json.

Criterios de jubilación (en orden de precedencia):
1. retired: deprecado por el proveedor
2. provider_variant: mide infraestructura/serving, no calidad del modelo
3. sin_runs: nunca medido (0 runs)
4. dominado: otro modelo de la misma familia es estrictamente mejor

Los generadores (export_for_pages.py, generate_rankings.py, etc.) deben
    10|filtrar por `key not in JUBILADOS` para excluir estos modelos.

Actualización: Regenerar ejecutando benchmarks/add_jubilado_status.py
cuando se actualice docs/jubilacion-2026-10.json.
"""

# Conjunto de modelos jubilados (no se vuelven a medir)
# Generado automáticamente desde docs/jubilacion-2026-10.json el 2026-10-13
JUBILADOS = {
    "claude-fable-5-sub",  # provider_variant
    20|    "claude-fable-5.1",  # dominado
    "claude-haiku-4.5-sub",  # provider_variant
    "claude-haiku-4.5-thinking",  # sin_runs
    "claude-opus-4.7",  # dominado
    "claude-opus-4.7-sub",  # provider_variant
    "claude-opus-4.7-thinking",  # sin_runs
    "claude-opus-4.8-sub",  # provider_variant
    "claude-opus-5",  # dominado
    "claude-opus-5-fast",  # dominado
    "claude-opus-5-sub",  # provider_variant
    30|    "claude-sonnet",  # sin_runs
    "claude-sonnet-4.6",  # dominado
    "claude-sonnet-4.6-sub",  # provider_variant
    "claude-sonnet-4.6-thinking",  # sin_runs
    "claude-sonnet-5-sub",  # provider_variant
    "claude-sonnet-5.5",  # dominado
    "deepseek-r1-free",  # sin_runs
    "deepseek-v3",  # dominado
    "deepseek-v4-flash-cloud",  # provider_variant
    "deepseek-v4-pro",  # dominado
    40|    "deepseek-v4-pro-0813",  # dominado
    "deepseek-v4-pro-cloud",  # provider_variant
    "devstral",  # retired
    "devstral-2",  # retired
    "devstral-medium",  # retired
    "gemini-3.1-flash-lite-thinking",  # sin_runs
    "gemini-3.1-pro",  # dominado
    "gemini-3.1-pro-thinking",  # sin_runs
    "gemini-3.5-flash",  # dominado
    "gemini-3.8-flash",  # dominado
    50|    "gemini-flash",  # dominado
    "gemini-flash-thinking",  # sin_runs
    "gemini-pro",  # dominado
    "gemma-4-26b",  # dominado
    "gemma4-26b-moe",  # sin_runs
    "gemma4-31b",  # provider_variant
    "glm-5.1",  # dominado
    "glm-5.2",  # dominado
    "gpt-4.1",  # dominado
    "gpt-4.1-mini",  # dominado
    60|    "gpt-4o",  # sin_runs
    "gpt-4o-high",  # sin_runs
    "gpt-5.4",  # dominado
    "gpt-5.4-mini",  # dominado
    "gpt-5.5",  # dominado
    "gpt-5.5-pro",  # provider_variant
    "gpt-5.6-luna-pro",  # dominado
    "gpt-5.6-sol",  # dominado
    "gpt-5.6-terra",  # dominado
    "gpt-5.6-terra-pro",  # dominado
    70|    "gpt-6-luna",  # dominado
    "gpt-oss-120b-cloud",  # provider_variant
    "grok-4.1-fast",  # retired
    "grok-4.20",  # dominado
    "grok-4.20-multi-agent",  # sin_runs
    "grok-4.5",  # dominado
    "groq-gpt-oss-120b",  # provider_variant
    "groq-gpt-oss-20b",  # provider_variant
    "groq-llama-3.1-8b",  # retired
    "groq-llama-3.3-70b",  # retired
    80|    "groq-llama-4-scout",  # provider_variant
    "hermes-4-405b-thinking",  # sin_runs
    "hermes-4-70b-thinking",  # sin_runs
    "hy4-preview",  # dominado
    "kat-coder-pro-2.5",  # dominado
    "kimi-k2",  # dominado
    "kimi-k2.5-thinking",  # sin_runs
    "kimi-k2.6-thinking",  # sin_runs
    "kimi-k2.7-code",  # dominado
    "kimi-k3",  # dominado
    90|    "laguna-s-2.1",  # dominado
    "lfm2-24b-a2b",  # sin_runs
    "ling-3.0-flash",  # dominado
    "llama-3.3-70b-free",  # sin_runs
    "llama-4-maverick",  # dominado
    "llama3.3-70b",  # provider_variant
    "llama4-maverick",  # provider_variant
    "local-deepseek-v3",  # provider_variant
    "local-devstral-small-2",  # sin_runs
    "local-gemma4-31b",  # provider_variant
   100|    "local-nemotron-3-nano-omni-reasoning",  # sin_runs
    "local-nemotron-3-super-120b",  # provider_variant
    "local-nemotron3-base-33b",  # dominado
    "local-qwen2.5-72b",  # provider_variant
    "local-qwen3-coder-next",  # provider_variant
    "local-qwen3.5-35b",  # provider_variant
    "local-qwen3.6-27b",  # provider_variant
    "local-qwen3.6-35b",  # sin_runs
    "mimo-v2-flash",  # retired
    "mimo-v2-flash-free",  # sin_runs
   110|    "mimo-v2-omni",  # retired
    "mimo-v2-omni-xiaomi",  # retired
    "mimo-v2-pro",  # retired
    "mimo-v2-pro-xiaomi",  # retired
    "mimo-v2.5",  # provider_variant
    "mimo-v2.5-or",  # dominado
    "mimo-v2.5-pro",  # provider_variant
    "mimo-v2.5-pro-or",  # dominado
    "minimax-m2.5",  # provider_variant
    "minimax-m2.7",  # dominado
   120|    "minimax-m2.7-direct",  # provider_variant
    "minimax-m2.7-highspeed",  # provider_variant
    "minimax-m3-direct",  # provider_variant
    "mistral-large",  # dominado
    "mistral-nemo-12b",  # provider_variant
    "muse-spark-1.2",  # dominado
    "nemotron-3.5-lightning",  # dominado
    "nemotron-nano",  # dominado
    "nemotron-super",  # dominado
    "nim-deepseek-v4-flash",  # provider_variant
   130|    "nim-deepseek-v4-pro",  # provider_variant
    "nim-devstral-2-123b",  # provider_variant
    "nim-gemma-4-31b",  # provider_variant
    "nim-glm-5.1",  # provider_variant
    "nim-glm5",  # provider_variant
    "nim-kimi-k2-thinking",  # provider_variant
    "nim-kimi-k2.5",  # provider_variant
    "nim-magistral-small",  # provider_variant
    "nim-ministral-14b",  # provider_variant
    "nim-mistral-large-3",  # provider_variant
   140|    "nim-mistral-nemotron",  # provider_variant
    "nim-nemotron-3-nano-omni-reasoning",  # provider_variant
    "nim-nemotron-3.5-lightning",  # provider_variant
    "nim-nemotron-nano-9b-v2",  # provider_variant
    "nim-nemotron-super-1.5",  # provider_variant
    "nim-qwen3-next-instruct",  # provider_variant
    "nim-qwen3-next-thinking",  # provider_variant
    "nim-qwen3.5-397b",  # provider_variant
    "nim-step-3.5-flash",  # provider_variant
    "openrouter-nemotron-3-ultra-550b",  # dominado
   150|    "openrouter-north-mini-code",  # sin_runs
    "or-gemma-4-31b",  # dominado
    "or-glm5",  # dominado
    "or-kimi-k2-thinking",  # dominado
    "or-nemotron-3-nano-omni-reasoning",  # dominado
    "or-nemotron-super-1.5",  # retired
    "or-qwen-2.5-72b",  # dominado
    "or-qwen-3.5-35b",  # dominado
    "or-qwen3-next-instruct",  # dominado
    "or-qwen3-next-thinking",  # dominado
   160|    "or-qwen3.5-397b",  # dominado
    "phi-4-14b",  # retired
    "qwen-3.5-plus",  # sin_runs
    "qwen-3.6-max",  # dominado
    "qwen-3.6-plus",  # dominado
    "qwen-3.6-plus-free",  # sin_runs
    "qwen-3.7-max",  # dominado
    "qwen-3.8-2.4t",  # dominado
    "qwen-3.8-27b",  # dominado
    "qwen-3.8-max",  # dominado
   170|    "qwen-3.8-max-0902",  # dominado
    "qwen3-coder",  # dominado
    "qwen3-coder-free",  # sin_runs
    "qwen3-coder-next",  # dominado
    "qwen3.5-397b-cloud",  # provider_variant
    "qwen3.5-cloud",  # retired
    "qwen3.6-27b",  # dominado
    "qwen3.6-35b",  # dominado
    "qwen3.8-flash",  # dominado
    "seed-oss-36b",  # retired
   180|    "spark-gemma4-12b-think",  # dominado
    "spark-gemma4-31b-llamacpp",  # provider_variant
    "spark-gemma4-31b-think",  # provider_variant
    "step3",  # retired
}

# Totales (para verificación)
TOTAL_JUBILADOS = len(JUBILADOS)  # 165
JUBILADOS_POR_CATEGORIA = {
    "dominado": 69,
    "provider_variant": 54,
    "sin_runs": 26,
   190|    "retired": 16,
}
