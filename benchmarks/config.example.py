"""
Configuracion de proveedores para benchmarks.
Copia este archivo como config.py y agrega tu API key de OpenRouter.
"""

# Tu API key de OpenRouter (unica key necesaria para todos los modelos)
OPENROUTER_API_KEY = "sk-or-v1-..."

# Modelos a evaluar via OpenRouter
# Organizados por tier de costo
MODELS = {
    # --- GRATIS (subsidiados por OpenRouter) ---
    "deepseek-r1-free": {
        "id": "deepseek/deepseek-r1:free",
        "name": "DeepSeek R1 (free)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "free",
    },
    "llama-3.3-70b-free": {
        "id": "meta-llama/llama-3.3-70b-instruct:free",
        "name": "Llama 3.3 70B (free)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "free",
    },
    "qwen-3.6-plus-free": {
        "id": "qwen/qwen3.6-plus:free",
        "name": "Qwen 3.6 Plus (free)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "free",
    },
    "mimo-v2-flash-free": {
        "id": "xiaomi/mimo-v2-flash:free",
        "name": "MiMo-V2-Flash (free)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "free",
        "open_source": True,
        "license": "MIT",
    },

    # --- ULTRA ECONOMICOS (<$0.10/M) ---
    "mistral-nemo": {
        "id": "mistralai/mistral-nemo",
        "name": "Mistral Nemo",
        "cost_input": 0.02,
        "cost_output": 0.02,
        "tier": "ultra_cheap",
    },
    "mimo-v2-flash": {
        "id": "xiaomi/mimo-v2-flash",
        "name": "MiMo-V2-Flash",
        "cost_input": 0.09,
        "cost_output": 0.29,
        "tier": "ultra_cheap",
        "open_source": True,
        "license": "MIT",
    },

    # --- ECONOMICOS ($0.10 - $1.00/M) ---
    "deepseek-v3": {
        "id": "deepseek/deepseek-chat",
        "name": "DeepSeek V3.2",
        "cost_input": 0.14,
        "cost_output": 0.28,
        "tier": "cheap",
    },
    "minimax-m2.7": {
        "id": "minimax/minimax-m2.7",
        "name": "MiniMax M2.7",
        "cost_input": 0.30,
        "cost_output": 1.20,
        "tier": "cheap",
    },
    "gemini-flash": {
        "id": "google/gemini-2.5-flash",
        "name": "Gemini 2.5 Flash",
        "cost_input": 0.30,
        "cost_output": 2.50,
        "tier": "cheap",
    },
    "qwen-3.6-plus": {
        "id": "qwen/qwen3.6-plus",
        "name": "Qwen 3.6 Plus",
        "cost_input": 0.33,
        "cost_output": 0.65,
        "tier": "cheap",
    },
    "mimo-v2-omni": {
        "id": "xiaomi/mimo-v2-omni",
        "name": "MiMo-V2-Omni",
        "cost_input": 0.40,
        "cost_output": 2.00,
        "tier": "cheap",
    },
    "qwen-3.5-plus": {
        "id": "qwen/qwen3.5-plus",
        "name": "Qwen 3.5 Plus",
        "cost_input": 1.20,
        "cost_output": 2.00,
        "tier": "cheap",
    },

    # --- MEDIO ($1.00 - $5.00/M) ---
    "mimo-v2-pro": {
        "id": "xiaomi/mimo-v2-pro",
        "name": "MiMo-V2-Pro",
        "cost_input": 1.00,
        "cost_output": 3.00,
        "tier": "medium",
    },
    "gemini-pro": {
        "id": "google/gemini-2.5-pro",
        "name": "Gemini 2.5 Pro",
        "cost_input": 1.25,
        "cost_output": 10.00,
        "tier": "medium",
    },
    "gpt-4o": {
        "id": "openai/gpt-4o",
        "name": "GPT-4o",
        "cost_input": 2.50,
        "cost_output": 10.00,
        "tier": "medium",
    },
    "claude-sonnet": {
        "id": "anthropic/claude-sonnet-4",
        "name": "Claude Sonnet 4",
        "cost_input": 3.00,
        "cost_output": 15.00,
        "tier": "medium",
    },

    # --- PREMIUM ($5.00+/M) ---
    "gpt-4o-high": {
        "id": "openai/gpt-4o:high",
        "name": "GPT-4o High",
        "cost_input": 5.00,
        "cost_output": 15.00,
        "tier": "premium",
    },
}

# Modelos locales via Ollama (agregar si tienes Ollama instalado)
OLLAMA_MODELS = {
    "qwen3.5-25b": {
        "id": "qwen3.5:25b",
        "name": "Qwen 3.5 25B (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
    },
    "llama3.3": {
        "id": "llama3.3",
        "name": "Llama 3.3 (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
    },
}

# Configuracion
RUNS_PER_TEST = 3          # Veces que se ejecuta cada test para promediar
REQUEST_TIMEOUT = 120      # Timeout en segundos
RESULTS_DIR = "benchmarks/results"
INCLUDE_OLLAMA = False     # Cambiar a True si tienes Ollama corriendo

# --- Opcional: APIs directas (descomentar si se usan) ---
# MiniMax directo (para M2.7 Highspeed y Image-01)
# MINIMAX_API_KEY = "eyJ..."
# MINIMAX_BASE_URL = "https://api.minimaxi.chat/v1"

# OpenAI directo (para GPT-5.4, GPT-4.1 - usa max_completion_tokens)
# OPENAI_API_KEY = "sk-..."
# OPENAI_BASE_URL = "https://api.openai.com/v1"
