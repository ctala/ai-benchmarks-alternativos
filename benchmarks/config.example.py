"""
Configuracion de proveedores para benchmarks.

Las API keys se leen desde el archivo .env (crear desde .env.example).
Este archivo define MODELS, OLLAMA_MODELS y constantes. NO editarlo con
valores de keys — ponelos en .env (que esta gitignored).

Setup:
    pip install python-dotenv
    cp .env.example .env   # editar con tus keys
    cp benchmarks/config.example.py benchmarks/config.py  # este archivo
"""
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

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
    "nemotron-nano": {
        "id": "nvidia/nemotron-3-nano-30b-a3b",
        "name": "Nemotron 3 Nano",
        "cost_input": 0.05,
        "cost_output": 0.20,
        "tier": "ultra_cheap",
        "open_source": True,
        "license": "NVIDIA Open",
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
    "nemotron-super": {
        "id": "nvidia/nemotron-3-super-120b-a12b",
        "name": "Nemotron 3 Super",
        "cost_input": 0.10,
        "cost_output": 0.50,
        "tier": "cheap",
        "open_source": True,
        "license": "NVIDIA Open",
    },
    "deepseek-v3": {
        "id": "deepseek/deepseek-chat",
        "name": "DeepSeek V3.2",
        "cost_input": 0.14,
        "cost_output": 0.28,
        "tier": "cheap",
    },
    "mistral-small-4": {
        "id": "mistralai/mistral-small-2603",
        "name": "Mistral Small 4",
        "cost_input": 0.15,
        "cost_output": 0.60,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "grok-4.1-fast": {
        "id": "x-ai/grok-4.1-fast",
        "name": "Grok 4.1 Fast",
        "cost_input": 0.20,
        "cost_output": 0.50,
        "tier": "cheap",
    },
    "gemini-3.1-flash-lite": {
        "id": "google/gemini-3.1-flash-lite-preview",
        "name": "Gemini 3.1 Flash Lite",
        "cost_input": 0.25,
        "cost_output": 1.50,
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
    "devstral": {
        "id": "mistralai/devstral-small",
        "name": "Devstral Small",
        "cost_input": 0.10,
        "cost_output": 0.30,
        "tier": "ultra_cheap",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "devstral-medium": {
        "id": "mistralai/devstral-medium",
        "name": "Devstral Medium",
        "cost_input": 0.40,
        "cost_output": 2.00,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "devstral-2": {
        "id": "mistralai/devstral-2512",
        "name": "Devstral 2 (Dic 2025)",
        "cost_input": 0.40,
        "cost_output": 2.00,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "mimo-v2-omni": {
        "id": "xiaomi/mimo-v2-omni",
        "name": "MiMo-V2-Omni",
        "cost_input": 0.40,
        "cost_output": 2.00,
        "tier": "cheap",
    },
    "glm-5.1": {
        "id": "z-ai/glm-5.1",
        "name": "GLM-5.1",
        "cost_input": 0.95,
        "cost_output": 3.15,
        "tier": "cheap",
        "open_source": True,
        "license": "MIT",
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
    "gemini-3.1-pro": {
        "id": "google/gemini-3.1-pro-preview",
        "name": "Gemini 3.1 Pro",
        "cost_input": 2.00,
        "cost_output": 12.00,
        "tier": "medium",
    },
    "grok-4.20": {
        "id": "x-ai/grok-4.20",
        "name": "Grok 4.20",
        "cost_input": 2.00,
        "cost_output": 6.00,
        "tier": "medium",
    },
    "gpt-4o": {
        "id": "openai/gpt-4o",
        "name": "GPT-4o",
        "cost_input": 2.50,
        "cost_output": 10.00,
        "tier": "medium",
    },

    # --- OpenAI directo (requiere OPENAI_API_KEY en .env) ---
    "gpt-4.1": {
        "id": "gpt-4.1", "name": "GPT-4.1",
        "cost_input": 2.00, "cost_output": 8.00,
        "tier": "medium", "provider": "openai_direct",
    },
    "gpt-4.1-mini": {
        "id": "gpt-4.1-mini", "name": "GPT-4.1 Mini",
        "cost_input": 0.40, "cost_output": 1.60,
        "tier": "cheap", "provider": "openai_direct",
    },
    "gpt-5.4": {
        "id": "gpt-5.4", "name": "GPT-5.4",
        "cost_input": 2.50, "cost_output": 10.00,
        "tier": "medium", "provider": "openai_direct",
    },
    "gpt-5.4-mini": {
        "id": "gpt-5.4-mini", "name": "GPT-5.4 Mini",
        "cost_input": 0.50, "cost_output": 1.50,
        "tier": "cheap", "provider": "openai_direct",
    },
    "gpt-5.5": {
        "id": "gpt-5.5", "name": "GPT-5.5",
        "cost_input": 5.00, "cost_output": 30.00,
        "tier": "premium", "provider": "openai_direct",
    },
    "gpt-5.5-pro": {
        "id": "gpt-5.5-pro", "name": "GPT-5.5 Pro",
        "cost_input": 30.00, "cost_output": 180.00,
        "tier": "premium", "provider": "openai_direct",
    },

    # --- Groq directo (LPU, super rápido — requiere GROQ_API_KEY en .env) ---
    "groq-llama-3.3-70b": {
        "id": "llama-3.3-70b-versatile", "name": "Llama 3.3 70B (Groq)",
        "cost_input": 0.59, "cost_output": 0.79,
        "tier": "cheap", "provider": "groq_direct",
        "open_source": True, "license": "Llama Community",
    },
    "groq-llama-3.1-8b": {
        "id": "llama-3.1-8b-instant", "name": "Llama 3.1 8B Instant (Groq)",
        "cost_input": 0.05, "cost_output": 0.08,
        "tier": "ultra_cheap", "provider": "groq_direct",
        "open_source": True, "license": "Llama Community",
    },
    "groq-llama-4-scout": {
        "id": "meta-llama/llama-4-scout-17b-16e-instruct", "name": "Llama 4 Scout 17B (Groq preview)",
        "cost_input": 0.11, "cost_output": 0.34,
        "tier": "cheap", "provider": "groq_direct",
        "open_source": True, "license": "Llama Community",
    },
    "groq-gpt-oss-120b": {
        "id": "openai/gpt-oss-120b", "name": "GPT-OSS 120B (Groq)",
        "cost_input": 0.15, "cost_output": 0.60,
        "tier": "cheap", "provider": "groq_direct",
        "open_source": True, "license": "Apache 2.0",
    },
    "groq-gpt-oss-20b": {
        "id": "openai/gpt-oss-20b", "name": "GPT-OSS 20B (Groq)",
        "cost_input": 0.075, "cost_output": 0.30,
        "tier": "ultra_cheap", "provider": "groq_direct",
        "open_source": True, "license": "Apache 2.0",
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
# Ver tags actuales en https://ollama.com/library/<modelo>/tags
OLLAMA_MODELS = {
    "qwen3.5-27b": {
        "id": "qwen3.5:27b",
        "name": "Qwen 3.5 27B (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
    },
    "qwen3.5-35b": {
        "id": "qwen3.5:35b",
        "name": "Qwen 3.5 35B (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
    },
    "qwen3.5-122b": {
        "id": "qwen3.5:122b",
        "name": "Qwen 3.5 122B (local, para DGX Spark)",
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
    # Cloud-only (requieren suscripción Ollama Cloud + OLLAMA_CLOUD_API_KEY)
    "qwen3.5-397b-cloud": {
        "id": "qwen3.5:397b-cloud",
        "name": "Qwen 3.5 397B (Ollama Cloud)",
        "cost_input": 0.0,   # flat fee via subscription
        "cost_output": 0.0,
        "tier": "cloud_ollama",
        "provider": "ollama_cloud",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "qwen3.5-cloud": {
        "id": "qwen3.5:cloud",
        "name": "Qwen 3.5 (Ollama Cloud, default)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "cloud_ollama",
        "provider": "ollama_cloud",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "gpt-oss-120b-cloud": {
        "id": "gpt-oss:120b-cloud",
        "name": "GPT-OSS 120B (Ollama Cloud)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "cloud_ollama",
        "provider": "ollama_cloud",
        "open_source": True,
        "license": "Apache 2.0",
    },
}

# Configuracion
RUNS_PER_TEST = 3
REQUEST_TIMEOUT = 300
RESULTS_DIR = "benchmarks/results"

# Las API keys se leen desde .env (copiar de .env.example)
# Cada var devuelve "" si no esta en .env; los providers opcionales se
# autodesactivan cuando la key esta vacia (ver runner.py).
INCLUDE_OLLAMA = os.getenv("INCLUDE_OLLAMA", "false").lower() == "true"

MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY", "")
MINIMAX_BASE_URL = os.getenv("MINIMAX_BASE_URL", "https://api.minimax.io/v1")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

OLLAMA_CLOUD_API_KEY = os.getenv("OLLAMA_CLOUD_API_KEY", "")
OLLAMA_CLOUD_BASE_URL = os.getenv("OLLAMA_CLOUD_BASE_URL", "https://ollama.com/v1")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
