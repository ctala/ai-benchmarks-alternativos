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
filtrar por `key not in JUBILADOS` para excluir estos modelos.

Actualización: Regenerar ejecutando benchmarks/add_jubilado_status.py
cuando se actualice docs/jubilacion-2026-10.json.
"""

# Conjunto de modelos jubilados (no se vuelven a medir)
# Generado automáticamente desde docs/jubilacion-2026-10.json el 2026-10-13
JUBILADOS = {
    "claude-fable-5-sub",  # provider_variant
    "claude-fable-5.1",  # dominado
    "claude-haiku-4.5-sub",  # provider_variant
    "claude-haiku-4.5-thinking",  # sin_runs
    "claude-opus-4.7",  # dominado
    "claude-opus-4.7-sub",  # provider_variant
    "claude-opus-4.7-thinking",  # sin_runs
    "claude-opus-4.8-sub",  # provider_variant
    "claude-opus-4.8-thinking",  # sin_runs
    "claude-sonnet-4.5-sub",  # provider_variant
    "claude-sonnet-4.5-thinking",  # sin_runs
    "claude-sonnet-4.6-sub",  # provider_variant
    "claude-sonnet-4.6-thinking",  # sin_runs
    "deepseek-v3-base",  # dominado
    "deepseek-v4-base",  # dominado
    "deepseek-v4-nim",  # provider_variant
    "deepseek-v4-pro-flash-nim",  # provider_variant
    "deepseek-v4-pro-nim",  # provider_variant
    "devstral",  # retired
    "devstral-2",  # retired
    "devstral-medium",  # retired
    "eko-alpha-preview",  # sin_runs
    "eko-beta",  # sin_runs
    "gemini-2.5-flash-lite",  # dominado
    "gemini-2.5-pro",  # dominado
    "gemini-3-pro",  # sin_runs
    "gemini-3.1-flash",  # dominado
    "gemini-3.1-pro",  # dominado
    "gemini-3.3-flash",  # sin_runs
    "gemini-3.3-pro",  # sin_runs
    "gemini-3.6-flash",  # dominado
    "gemini-4-argon",  # sin_runs
    "gemini-flash-lite-1.5-extended",  # dominado
    "gemma-3-27b",  # sin_runs
    "gemma-4-31b",  # sin_runs
    "glm-4-9b",  # dominado
    "glm-5.2-standard",  # retired
    "glm-5.3-flash-nim",  # provider_variant
    "glm-5.3-nim",  # provider_variant
    "gpt-4.1-mini",  # dominado
    "gpt-4.1-thinking",  # sin_runs
    "gpt-5.4-mini",  # dominado
    "gpt-5.4-mini-thinking",  # sin_runs
    "gpt-5.5",  # dominado
    "gpt-5.5-pro",  # dominado
    "gpt-5.5-thinking",  # sin_runs
    "gpt-6-luna-pro",  # dominado
    "gpt-6-luna-thinking",  # sin_runs
    "grok-4.5",  # dominado
    "hermes-3-omni-70b",  # sin_runs
    "hermes-4-20b",  # sin_runs
    "hermes-4-27b",  # sin_runs
    "hy-1",  # sin_runs
    "hy-2",  # sin_runs
    "kimi-k2",  # dominado
    "kimi-k2.5",  # dominado
    "kimi-k2.6",  # dominado
    "kimi-k2.6-nim",  # provider_variant
    "llama-3.1-8b-groq",  # retired
    "llama-3.3-70b-nim",  # provider_variant
    "llama-3.3-70b-vllm",  # provider_variant
    "minimax-m2.7",  # dominado
    "minimax-m2.7-highspeed",  # dominado
    "mimo-v2-flash",  # retired
    "mimo-v2-pro",  # retired
    "mistral-3-medium-reasoning",  # sin_runs
    "mistral-3.2-medium-reasoning",  # dominado
    "mistral-4-large",  # dominado
    "mistral-nemo-2501-nim",  # provider_variant
    "mistral-r-3-medium-2501-nim",  # provider_variant
    "mistral-small-2503",  # dominado
    "or-claude-fable-5",  # provider_variant
    "or-claude-fable-5.1",  # provider_variant
    "or-claude-haiku-4.5",  # provider_variant
    "or-claude-opus-4.7",  # provider_variant
    "or-claude-opus-4.8",  # provider_variant
    "or-claude-sonnet-4.5",  # provider_variant
    "or-claude-sonnet-4.6",  # provider_variant
    "or-deepseek-v3",  # provider_variant
    "or-deepseek-v4",  # provider_variant
    "or-deepseek-v4-pro",  # provider_variant
    "or-deepseek-v4-pro-flash",  # provider_variant
    "or-gemini-2.5-flash-lite",  # provider_variant
    "or-gemini-2.5-pro",  # provider_variant
    "or-gemini-3.1-flash",  # provider_variant
    "or-gemini-3.1-flash-lite",  # provider_variant
    "or-gemini-3.1-pro",  # provider_variant
    "or-gemini-3.6-flash",  # provider_variant
    "or-gemma-3-27b",  # provider_variant
    "or-gemma-4-31b",  # provider_variant
    "or-glm-4-9b",  # provider_variant
    "or-glm-5.3",  # provider_variant
    "or-glm-5.3-flash",  # provider_variant
    "or-gpt-4.1",  # provider_variant
    "or-gpt-4.1-mini",  # provider_variant
    "or-gpt-5.4-mini",  # provider_variant
    "or-gpt-5.5",  # provider_variant
    "or-gpt-5.5-pro",  # provider_variant
    "or-gpt-6-luna",  # provider_variant
    "or-gpt-6-luna-pro",  # provider_variant
    "or-grok-4.5",  # provider_variant
    "or-grok-4.6",  # provider_variant
    "or-grok-4.7",  # provider_variant
    "or-kimi-k2",  # provider_variant
    "or-kimi-k2.5",  # provider_variant
    "or-kimi-k2.6",  # provider_variant
    "or-kimi-k2.7",  # provider_variant
    "or-llama-3.3-70b",  # provider_variant
    "or-minimax-m2.7",  # provider_variant
    "or-minimax-m2.7-highspeed",  # provider_variant
    "or-minimax-m3",  # provider_variant
    "or-mistral-3-medium-reasoning",  # provider_variant
    "or-mistral-3.2-medium-reasoning",  # provider_variant
    "or-mistral-4-large",  # provider_variant
    "or-mistral-small-2503",  # provider_variant
    "or-qwen-3.5-235b-32k",  # provider_variant
    "or-qwen-3.5-397b",  # provider_variant
    "or-qwen-3.5-72b",  # provider_variant
    "or-qwen-3.5-coder-32b",  # provider_variant
    "or-qwen-3.6-21b",  # provider_variant
    "or-qwen-3.6-35b",  # provider_variant
    "or-qwen-3.7-max",  # provider_variant
    "or-qwen-3.7-plus",  # provider_variant
    "or-qwen-3.8-27b",  # provider_variant
    "or-qwen-3.8-omni-flash",  # provider_variant
    "phi-4-nim",  # provider_variant
    "qwen-3.5-397b",  # sin_runs
    "qwen-3.6-35b",  # dominado
    "qwen-3.7-max",  # dominado
    "qwen-3.8-omni-flash",  # sin_runs
    "qwen3.5-235b",  # retired
    "qwen3.5-397b",  # retired
}
