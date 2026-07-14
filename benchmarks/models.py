"""
Catalogo de modelos del benchmark — metadata publica (sin API keys).

Este archivo es la fuente unica de verdad para los modelos. Lo importan
config.py, runner.py y los scripts de auto-generacion. Versionado en git.

Para agregar un modelo nuevo:
- OpenRouter: agregar entry al dict MODELS con id provider/model
- Provider directo: agregar entry con campo "provider": "<provider_key>"
- Local Ollama: agregar a OLLAMA_MODELS

Para agregar un provider nuevo: editar runner.py + adapters.py.
"""

# Suscripciones mensuales disponibles que dan acceso a modelos.
# Un modelo puede estar incluido en MÚLTIPLES suscripciones — usar
# `subscriptions: ["key1", "key2"]` en cada entry de MODELS.
# Precios al 30 abril 2026, verificar antes de actualizar docs.
SUBSCRIPTIONS = {
    "ollama_cloud_pro": {
        "name": "Ollama Cloud",
        "plan": "Pro",
        "price_month_usd": 30,
        "url": "https://ollama.com/cloud",
        "notes": "Rate limit varía por modelo. Recomendado para uso a volumen mid (1-10k calls/día).",
    },
    "xiaomi_standard": {
        "name": "Xiaomi MiMo Standard",
        "plan": "Standard",
        "price_month_usd": 14,
        "url": "https://mimo.xiaomi.com",
        "notes": "200M credits/mes. Off-peak 16-24 UTC = 0.8x consumption. Acceso a 8 modelos MiMo.",
    },
    "minimax_agent_pro": {
        "name": "MiniMax Agent Pro",
        "plan": "Agent Pro",
        "price_month_usd": 19,
        "url": "https://api.minimax.io",
        "notes": "Acceso a M2.7 highspeed + límites generosos para agentes (1k+ calls/día).",
    },
    "anthropic_pro": {
        "name": "Anthropic Pro",
        "plan": "Pro",
        "price_month_usd": 20,
        "url": "https://www.anthropic.com/pricing",
        "notes": "Sub Anthropic Pro $20/mes. NO incluye API access (solo claude.ai web).",
    },
    "xai_supergrok": {
        "name": "xAI SuperGrok",
        "plan": "Standard",
        "price_month_usd": 30,
        "url": "https://grok.com/plans",
        "notes": "$30/mes o $300/año. Acceso consumer a Grok 4/4.1 (128K, DeepSearch, Big Brain, voz). NO incluye API access (igual que Anthropic Pro). Grok 4.3 + multi-agente requieren SuperGrok Heavy $300/mes.",
    },
    # Nota: Groq, OpenRouter, OpenAI tienen pricing por token (pay-as-you-go)
    # sin suscripción mensual fija. NIM gratis tiene 40 RPM sin sub.
}

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
    # Qwen 3.6 Plus free fue deprecado, usar version pagada
    "qwen3-coder-free": {
        "id": "qwen/qwen3-coder-480b:free",
        "name": "Qwen3 Coder 480B (free)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "free",
        "open_source": True,
    },

    # --- ULTRA ECONOMICOS (<$0.10/M) ---
    "mistral-nemo": {
        "id": "mistralai/mistral-nemo",
        "name": "Mistral Nemo",
        "cost_input": 0.02,
        "cost_output": 0.02,
        "tier": "ultra_cheap",
        "open_source": True,
        "license": "Apache 2.0",
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
    "minimax-m3": {
        "id": "minimax/minimax-m3",
        "name": "MiniMax M3",
        "cost_input": 0.30,
        "cost_output": 1.20,
        "tier": "cheap",
        "thinking": True,
        "notes": "Lanzado 1 jun 2026 (https://www.minimax.io/models/text/m3). Sucesor de M2.7 — caso activo de Cristian (sub MiniMax). Contexto 1M (vs 200k de M2.7), mismo precio $0.30/$1.20. Híbrido (emite <think>). Verificado vía OpenRouter API 1 jun 2026.",
    },
    "minimax-m3-direct": {
        # Variante: el modelo ya está medido en OpenRouter (plano común) y esa es su
        # fila canónica. Ésta conserva la medición vía API directa MiniMax para comparar.
        "provider_variant": True,
        "id": "MiniMax-M3",
        "name": "MiniMax M3 (directo / sub)",
        "cost_input": 0.30,
        "cost_output": 1.20,
        "tier": "subscription",
        "provider": "minimax_direct",
        "thinking": True,
        "subscriptions": ["minimax_agent_pro"],
        "notes": "M3 vía API directa de MiniMax (token plan del usuario, key en .env). Mismo modelo que minimax-m3 (OpenRouter) — comparar provider stability + base para el eje cost-to-complete del caso real de Cristian. Costo del ranking = precio OpenRouter ($0.30/$1.20).",
    },
    # MiniMax M2.7 Highspeed requiere API directa de MiniMax (no OpenRouter)
    # Configurar MINIMAX_API_KEY abajo para habilitarlo
    "minimax-m2.7-direct": {
        # Variante de proveedor: el modelo ya se mide en OpenRouter (plano común) y esa es
        # su fila canónica. Ésta conserva la medición en la infra del proveedor.
        "provider_variant": True,
        "id": "MiniMax-M2.7",
        "name": "MiniMax M2.7 (directo)",
        "cost_input": 0.30,
        "cost_output": 1.20,
        "tier": "cheap",
        "provider": "minimax_direct",
        "subscriptions": ["minimax_agent_pro"],
        "notes": "API directa MiniMax. Disponible también en sub Agent Pro $19/mes.",
    },
    "minimax-m2.7-highspeed": {
        # Variante de proveedor: el modelo ya se mide en OpenRouter (plano común) y esa es
        # su fila canónica. Ésta conserva la medición en la infra del proveedor.
        "provider_variant": True,
        "id": "MiniMax-M2.7-highspeed",
        "name": "MiniMax M2.7 Highspeed",
        "cost_input": 0.30,
        "cost_output": 1.20,
        "tier": "cheap",
        "provider": "minimax_direct",
        "subscriptions": ["minimax_agent_pro"],
        "notes": "Acceso vía sub Agent Pro $19/mes. Misma calidad que M2.7 directo, latencia ultra baja.",
    },
    "gemini-3.5-flash": {
        "id": "google/gemini-3.5-flash",
        "name": "Gemini 3.5 Flash",
        "cost_input": 1.50,
        "cost_output": 9.00,
        "tier": "medium",
        # niah sin cap: medir su curva completa hasta 800K para confirmar si el
        # hallazgo (peor que 2.5 Flash Lite en español) se sostiene en contexto grande.
        "notes": "Sucesor del Flash (19 may 2026), contexto 1M. $1.50/$9 vía OpenRouter API. Releva al 2.5 Flash.",
    },
    "gemini-flash": {
        "id": "google/gemini-2.5-flash",
        "name": "Gemini 2.5 Flash",
        "cost_input": 0.30,
        "cost_output": 2.50,
        "tier": "cheap",
    },
    "gemini-flash-thinking": {
        "id": "google/gemini-2.5-flash",
        "name": "Gemini 2.5 Flash (thinking)",
        "cost_input": 0.30,
        "cost_output": 2.50,
        "tier": "cheap",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Misma versión que gemini-flash con thinking forzado (effort=high).",
    },
    "qwen-3.6-max": {
        "id": "qwen/qwen3.6-max-preview",
        "name": "Qwen 3.6 Max",
        "cost_input": 1.04,
        "cost_output": 6.24,
        "tier": "medium",
        "open_source": False,
        "license": "Proprietary",
        "notes": "Tier Max de Alibaba (API-only propietario, el más capaz de la familia). Completa base+Plus+Max. $1.04/$6.24 vía OpenRouter API jun 2026.",
    },
    "qwen-3.7-max": {
        "id": "qwen/qwen3.7-max",
        "name": "Qwen 3.7 Max",
        "cost_input": 2.50,
        "cost_output": 7.50,
        "tier": "premium",
        "open_source": False,
        "license": "Proprietary",
        "context_window": 1000000,
        "niah_max_context": 262144,   # cap de costo en niah (modelo caro), como Opus
        "notes": "Flagship Qwen 3.7 (20 may 2026, API-only). Reasoning-agent, 1M contexto. Vence a Claude Opus 4.6 Max en Terminal-Bench 2.0, SWE-Bench Pro y MCP-Atlas. $2.50/$7.50 rate card vía OpenRouter (promo 50% a $1.25/$3.75 al lanzar). Plus (multimodal) no está en OR — pendiente para suite multimodal.",
    },
    "qwen-3.6-plus": {
        "id": "qwen/qwen3.6-plus",
        "name": "Qwen 3.6 Plus",
        "cost_input": 0.18,
        "cost_output": 1.07,
        "tier": "cheap",
        "open_source": False,
        "license": "Proprietary",
        "notes": "Plus = API-only propietario de Alibaba (NO confundir con Qwen 3.6 base que es Apache 2.0)",
    },
    "qwen-3.5-plus": {
        "id": "qwen/qwen3.5-plus",
        "name": "Qwen 3.5 Plus",
        "cost_input": 1.20,
        "cost_output": 2.00,
        "tier": "cheap",
        "open_source": False,
        "license": "Proprietary",
        "notes": "Plus = API-only propietario de Alibaba",
    },

    # --- Kimi (Moonshot AI) — pesos públicos en HuggingFace, Modified MIT ---
    "kimi-k2": {
        "id": "moonshotai/kimi-k2",
        "name": "Kimi K2",
        "cost_input": 0.20,
        "cost_output": 0.80,
        "tier": "cheap",
        "open_source": True,
        "license": "Modified MIT",
    },
    "kimi-k2.5": {
        "id": "moonshotai/kimi-k2.5",
        "name": "Kimi K2.5",
        "cost_input": 0.20,
        "cost_output": 0.80,
        "tier": "cheap",
        "open_source": True,
        "license": "Modified MIT",
    },
    "kimi-k2.5-thinking": {
        "id": "moonshotai/kimi-k2.5",
        "name": "Kimi K2.5 (thinking)",
        "cost_input": 0.20,
        "cost_output": 0.80,
        "tier": "cheap",
        "open_source": True,
        "license": "Modified MIT",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Misma versión que kimi-k2.5 pero con reasoning forzado vía OpenRouter (effort=high).",
    },

    "kimi-k2.6": {
        "id": "moonshotai/kimi-k2.6",
        "name": "Kimi K2.6",
        "cost_input": 0.73,
        "cost_output": 3.49,
        "tier": "cheap",
        "open_source": True,
        "license": "Modified MIT",
        "notes": "Thinking model. Pesos públicos en HF (1.1T params). Precio corregido may 2026 vía OpenRouter API ($0.73/$3.49).",
    },
    "kimi-k2.6-thinking": {
        "id": "moonshotai/kimi-k2.6",
        "name": "Kimi K2.6 (thinking)",
        "cost_input": 0.73,
        "cost_output": 3.49,
        "tier": "cheap",
        "open_source": True,
        "license": "Modified MIT",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Misma versión que kimi-k2.6 con thinking forzado vía OpenRouter (effort=high).",
    },
    "kimi-k2.7-code": {
        "id": "moonshotai/kimi-k2.7-code",
        "name": "Kimi K2.7 Code",
        "cost_input": 0.74,
        "cost_output": 3.50,
        "tier": "medium",
        "open_source": True,
        "license": "Modified MIT",
        "thinking": True,
        "niah_max_context": 131072,
        "notes": "Coding-focused K2.7 family, reasoning mandatory. Precio vía OpenRouter API jun 2026 ($0.74/$3.50). Contexto 262K; niah capado a 128K porque 256K+output supera el límite real.",
    },

    # --- GLM (Zhipu AI / Z.ai) ---
    "glm-5.1": {
        "id": "z-ai/glm-5.1",
        "name": "GLM-5.1",
        "cost_input": 0.95,
        "cost_output": 3.15,
        "tier": "cheap",
        "open_source": True,
        "license": "MIT",
    },
    "glm-5.2": {
        "id": "z-ai/glm-5.2",
        "name": "GLM 5.2",
        "cost_input": 0.95,
        "cost_output": 3.00,
        "tier": "cheap",
        "open_source": True,
        "license": "MIT",
        "notes": (
            "Large-scale reasoning model de Z.ai con 1M de contexto y reasoning opcional. "
            "Benchmarks de terceros lo ubican fuerte en coding agents y tareas visuales/dataviz. "
            "Precio competitivo: $0.95/$3.00 por M tokens."
        ),
    },

    # --- Xiaomi MiMo ---
    "mimo-v2-flash": {
        "retired": True,  # Xiaomi: modelo deprecado (13-jul-2026)
        "id": "xiaomi/mimo-v2-flash",
        "name": "MiMo-V2-Flash",
        "cost_input": 0.09,
        "cost_output": 0.29,
        "tier": "ultra_cheap",
        "open_source": True,
        "license": "MIT",
    },
    "mimo-v2-pro": {
        "retired": True,  # Xiaomi: modelo deprecado (13-jul-2026)
        "id": "xiaomi/mimo-v2-pro",
        "name": "MiMo-V2-Pro",
        "cost_input": 1.00,
        "cost_output": 3.00,
        "tier": "medium",
        "open_source": False,
        "license": "Proprietary",
        "notes": "API-only Xiaomi (NO confundir con MiMo V2 Flash que sí es MIT en HF). El Pro no se publica en HuggingFace.",
    },

    # --- NVIDIA Nemotron ---
    "nemotron-super": {
        "id": "nvidia/nemotron-3-super-120b-a12b",
        "name": "Nemotron 3 Super",
        "cost_input": 0.10,
        "cost_output": 0.50,
        "tier": "ultra_cheap",
        "open_source": True,
        "license": "NVIDIA Open",
    },

    # --- Anthropic nuevos ---
    "claude-opus-4.7": {
        "id": "anthropic/claude-opus-4-7",
        "name": "Claude Opus 4.7",
        "cost_input": 5.00,
        "cost_output": 25.00,
        "tier": "premium",
        "notes": "Precio corregido may 2026 vía OpenRouter API: $5/$25 (antes teníamos $15/$75, era pricing viejo de Claude-3 Opus).",
    },
    "claude-opus-4.8": {
        "id": "anthropic/claude-opus-4.8",
        "name": "Claude Opus 4.8",
        "cost_input": 5.00,
        "cost_output": 25.00,
        "tier": "premium",
        "context_window": 1000000,
        "niah_max_context": 262144,  # cap de costo: skip tramos 1M (evita ~$40 en niah)
        "notes": "Flagship Anthropic más nuevo (jun 2026), contexto 1M. $5/$25 vía OpenRouter API. Techo de calidad de referencia. Sucesor de 4.7.",
    },
    # --- Anthropic vía SUSCRIPCIÓN Claude Code (CLI `claude -p`, tarifa plana) ---
    # Costo del ranking = precio OpenRouter (free_runtime via sub). CAVEAT: ~8.8K
    # scaffolding residual de Claude Code, NO usar para tool-calling. id = alias CLI.
    "claude-fable-5-sub": {
        # Solo medido por suscripción (`claude -p`), que arrastra ~8.8K tokens de
        # scaffolding del CLI: NO es un chat completion limpio y no es comparable
        # con el resto. Va a la tabla de suscripción, fuera del ranking principal.
        "provider_variant": True,
        "id": "claude-fable-5",
        "name": "Claude Fable 5 (suscripción)",
        "cost_input": 10.00, "cost_output": 50.00,
        "tier": "subscription", "provider": "claude_code",
        "subscriptions": ["anthropic_pro"], "free_runtime": True,
        "context_window": 1000000,
        "notes": "Fable 5 medido por la suscripción Claude Code (no API) — a costo $0. Costeado a precio OpenRouter ($10/$50 = 2x Opus 4.8). Incluido en plan Max hasta 21-jun-2026; después solo API. CAVEAT: subscription_measured.",
    },
    "claude-opus-4.8-sub": {
        # Variante: el modelo ya está medido en OpenRouter (plano común) y esa es su
        # fila canónica. Ésta conserva la medición vía Claude Code CLI para comparar.
        "provider_variant": True,
        "id": "claude-opus-4-8",
        "name": "Claude Opus 4.8 (suscripción)",
        "cost_input": 5.00, "cost_output": 25.00,
        "tier": "subscription", "provider": "claude_code",
        "subscriptions": ["anthropic_pro"], "free_runtime": True,
        "context_window": 1000000,
        "notes": "Opus 4.8 medido por la suscripción Claude Code (no API) — a costo $0. Costeado a precio OpenRouter ($5/$25). CAVEAT: subscription_measured.",
    },
    "claude-opus-4.7-sub": {
        # Variante: el modelo ya está medido en OpenRouter (plano común) y esa es su
        # fila canónica. Ésta conserva la medición vía Claude Code CLI para comparar.
        "provider_variant": True,
        "id": "claude-opus-4-7",
        "name": "Claude Opus 4.7 (suscripción)",
        "cost_input": 5.00, "cost_output": 25.00,
        "tier": "subscription", "provider": "claude_code",
        "subscriptions": ["anthropic_pro"], "free_runtime": True,
        "context_window": 1000000,
        "notes": "Opus 4.7 vía suscripción Claude Code.",
    },
    "claude-sonnet-4.6-sub": {
        # Variante: el modelo ya está medido en OpenRouter (plano común) y esa es su
        # fila canónica. Ésta conserva la medición vía Claude Code CLI para comparar.
        "provider_variant": True,
        "id": "claude-sonnet-4-6",
        "name": "Claude Sonnet 4.6 (suscripción)",
        "cost_input": 3.00, "cost_output": 15.00,
        "tier": "subscription", "provider": "claude_code",
        "subscriptions": ["anthropic_pro"], "free_runtime": True,
        "context_window": 1000000,
        "notes": "Sonnet 4.6 vía suscripción Claude Code.",
    },
    "claude-haiku-4.5-sub": {
        # Solo medido por suscripción (`claude -p`), que arrastra ~8.8K tokens de
        # scaffolding del CLI: NO es un chat completion limpio y no es comparable
        # con el resto. Va a la tabla de suscripción, fuera del ranking principal.
        "provider_variant": True,
        "id": "claude-haiku-4-5",
        "name": "Claude Haiku 4.5 (suscripción)",
        "cost_input": 1.00, "cost_output": 5.00,
        "tier": "subscription", "provider": "claude_code",
        "subscriptions": ["anthropic_pro"], "free_runtime": True,
        "context_window": 200000,
        "notes": "Haiku 4.5 vía suscripción Claude Code.",
    },
    "claude-opus-4.7-thinking": {
        "id": "anthropic/claude-opus-4-7",
        "name": "Claude Opus 4.7 (thinking)",
        "cost_input": 5.00,
        "cost_output": 25.00,
        "tier": "premium",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Mismo modelo que claude-opus-4.7 con extended thinking forzado (effort=high). Reasoning tokens facturados como output a $25/M — ~5-7x más caro por test que sin thinking.",
    },
    # --- Mistral ---
    "mistral-large": {
        "id": "mistralai/mistral-large",
        "name": "Mistral Large",
        "cost_input": 2.00,
        "cost_output": 6.00,
        "tier": "medium",
        "open_source": False,
        "license": "MRL (no comercial)",
    },
    "devstral": {
        "retired": True,  # OpenRouter: "No endpoints found" (13-jul-2026). Estaba #5 del ranking.
        "id": "mistralai/devstral-small",
        "name": "Devstral Small",
        "cost_input": 0.10,
        "cost_output": 0.30,
        "tier": "ultra_cheap",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "devstral-medium": {
        "retired": True,  # OpenRouter: No endpoints found (13-jul-2026)
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

    # --- GPT-4.1 via OpenAI directo ---
    "gpt-4.1": {
        # Variante: medido en la API directa de OpenAI. La fila canónica se mide en
        # OpenRouter para que la velocidad y la latencia sean comparables con el resto.
        "provider_variant": True,
        "id": "gpt-4.1",
        "name": "GPT-4.1",
        "cost_input": 2.00,
        "cost_output": 8.00,
        "tier": "medium",
        "provider": "openai_direct",
    },
    "gpt-4.1-mini": {
        # Variante: medido en la API directa de OpenAI. La fila canónica se mide en
        # OpenRouter para que la velocidad y la latencia sean comparables con el resto.
        "provider_variant": True,
        "id": "gpt-4.1-mini",
        "name": "GPT-4.1 Mini",
        "cost_input": 0.40,
        "cost_output": 1.60,
        "tier": "cheap",
        "provider": "openai_direct",
    },

    # --- MEDIO ($1.00 - $5.00/M) ---
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

    # --- MEDIO - Nuevos modelos Abril 2026 ---
    "gemma-4-31b": {
        "id": "google/gemma-4-31b-it",
        "name": "Gemma 4 31B",
        "cost_input": 0.30,
        "cost_output": 0.60,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "gemma-4-26b": {
        "id": "google/gemma-4-26b-a4b-it",
        "name": "Gemma 4 26B MoE (3.8B activos)",
        "cost_input": 0.15,
        "cost_output": 0.30,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
    },
    "llama-4-maverick": {
        "id": "meta-llama/llama-4-maverick",
        "name": "Llama 4 Maverick",
        "cost_input": 0.50,
        "cost_output": 1.00,
        "tier": "cheap",
        "open_source": True,
        "license": "Llama Community",
    },
    "qwen3-coder": {
        "id": "qwen/qwen3-coder",
        "name": "Qwen3 Coder",
        "cost_input": 0.20,
        "cost_output": 0.60,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
    },

    # --- Qwen 3.6 base + Coder-Next vía OpenRouter (FP8) — pares de los locales
    #     del DGX Spark para medir el delta Q4(local) vs FP8(API). Precios
    #     verificados vía OpenRouter /api/v1/models el 1 jun 2026. ---
    "qwen3.6-27b": {
        "id": "qwen/qwen3.6-27b",
        "name": "Qwen 3.6 27B base (OpenRouter FP8)",
        "cost_input": 0.29,
        "cost_output": 3.20,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
        "notes": "Qwen 3.6 BASE abierto vía OpenRouter (FP8). Par del local-qwen3.6-27b (Q4 en DGX Spark) para medir delta cuantización.",
    },
    "qwen3.6-35b": {
        "id": "qwen/qwen3.6-35b-a3b",
        "name": "Qwen 3.6 35B base (OpenRouter FP8)",
        "cost_input": 0.14,
        "cost_output": 1.00,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
        "notes": "Qwen 3.6 BASE 35B (MoE a3b) vía OpenRouter (FP8). Par del local-qwen3.6-35b (Q4).",
    },
    "qwen3-coder-next": {
        "id": "qwen/qwen3-coder-next",
        "name": "Qwen3-Coder-Next (OpenRouter FP8)",
        "cost_input": 0.11,
        "cost_output": 0.80,
        "tier": "cheap",
        "open_source": True,
        "license": "Apache 2.0",
        "notes": "Coding next-gen vía OpenRouter (FP8). Par del local-qwen3-coder-next (Q4 en DGX Spark).",
    },

    # --- MEDIO - Ultimos modelos de cada proveedor ---
    "claude-opus-4.6": {
        "id": "anthropic/claude-opus-4-6",
        "name": "Claude Opus 4.6",
        "cost_input": 5.00,
        "cost_output": 25.00,
        "tier": "premium",
        "notes": "Precio corregido may 2026 vía web/OpenRouter: $5/$25 (antes $15/$75 stale).",
    },
    "claude-sonnet-4.6": {
        "id": "anthropic/claude-sonnet-4-6",
        "name": "Claude Sonnet 4.6 (ultimo Anthropic)",
        "cost_input": 3.00,
        "cost_output": 15.00,
        "tier": "medium",
    },
    "claude-sonnet-4.6-thinking": {
        "id": "anthropic/claude-sonnet-4-6",
        "name": "Claude Sonnet 4.6 (thinking)",
        "cost_input": 3.00,
        "cost_output": 15.00,
        "tier": "medium",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Mismo modelo que claude-sonnet-4.6 con extended thinking forzado (effort=high). Reasoning tokens facturados como output a $15/M — ~5-7x más caro por test que sin thinking.",
    },
    "claude-haiku-4.5": {
        "id": "anthropic/claude-haiku-4.5",
        "name": "Claude Haiku 4.5",
        "cost_input": 1.00,
        "cost_output": 5.00,
        "tier": "cheap",
        "notes": "Anthropic Haiku family. Hybrid (extended thinking opt-in).",
    },
    "claude-haiku-4.5-thinking": {
        "id": "anthropic/claude-haiku-4.5",
        "name": "Claude Haiku 4.5 (thinking)",
        "cost_input": 1.00,
        "cost_output": 5.00,
        "tier": "cheap",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Misma versión con extended thinking forzado.",
    },
    "gemini-flash-lite": {
        "id": "google/gemini-2.5-flash-lite",
        "name": "Gemini 2.5 Flash Lite",
        "cost_input": 0.10,
        "cost_output": 0.40,
        "tier": "ultra_cheap",
    },

    # --- Cohere North (coding, via OpenRouter) ---
    "openrouter-north-mini-code": {
        "id": "cohere/north-mini-code",
        "name": "North Mini Code",
        "cost_input": 0.2,
        "cost_output": 0.6,
        "tier": "cheap",
        "provider": "openrouter",
        "open_source": False,
        "license": "Cohere Commercial",
        "notes": "Modelo de Cohere enfocado en coding via OpenRouter (version de paga, sin rate limit restrictivo).",
    },

    # --- PREMIUM ($5.00+/M) ---
    # GPT-5.4 y GPT-5.4-mini via API directa de OpenAI
    "gpt-5.4": {
        # Variante: medido en la API directa de OpenAI. La fila canónica se mide en
        # OpenRouter para que la velocidad y la latencia sean comparables con el resto.
        "provider_variant": True,
        "id": "gpt-5.4",
        "name": "GPT-5.4",
        "cost_input": 5.00,
        "cost_output": 15.00,
        "tier": "premium",
        "provider": "openai_direct",
    },
    "gpt-5.4-mini": {
        # Variante: medido en la API directa de OpenAI. La fila canónica se mide en
        # OpenRouter para que la velocidad y la latencia sean comparables con el resto.
        "provider_variant": True,
        "id": "gpt-5.4-mini",
        "name": "GPT-5.4 Mini",
        "cost_input": 0.50,
        "cost_output": 1.50,
        "tier": "cheap",
        "provider": "openai_direct",
    },
    "gpt-5.6-luna": {
        "id": "openai/gpt-5.6-luna",
        "name": "GPT-5.6 Luna",
        "cost_input": 1.00,
        "cost_output": 6.00,
        "tier": "cheap",
        "niah_max_context": 262144,
        "notes": "Variante rápida y económica de GPT-5.6 (GA 9 jul 2026). $1/$6 vía OpenRouter.",
    },
    "gpt-5.5": {
        # Variante: medido en la API directa de OpenAI. La fila canónica se mide en
        # OpenRouter para que la velocidad y la latencia sean comparables con el resto.
        "provider_variant": True,
        "id": "gpt-5.5",
        "name": "GPT-5.5",
        "cost_input": 5.00,
        "cost_output": 30.00,
        "tier": "premium",
        "provider": "openai_direct",
    },
    "gpt-5.6-terra": {
        "id": "openai/gpt-5.6-terra",
        "name": "GPT-5.6 Terra",
        "cost_input": 2.50,
        "cost_output": 15.00,
        "tier": "medium",
        "niah_max_context": 262144,
        "notes": "Variante balanceada de GPT-5.6. OpenAI la ubica al nivel de GPT-5.5 a mitad de costo. $2.5/$15 vía OpenRouter.",
    },
    "gpt-5.6-sol": {
        "id": "openai/gpt-5.6-sol",
        "name": "GPT-5.6 Sol",
        "cost_input": 5.00,
        "cost_output": 30.00,
        "tier": "premium",
        "niah_max_context": 262144,
        "notes": "Flagship GPT-5.6 (GA 9 jul 2026). $5/$30 vía OpenRouter.",
    },
    "gpt-5.5-pro": {
        # Variante: medido en la Responses API de OpenAI. La fila canónica se mide en
        # OpenRouter para que velocidad y latencia sean comparables.
        "provider_variant": True,
        "id": "gpt-5.5-pro",
        "name": "GPT-5.5 Pro",
        "cost_input": 30.00,
        "cost_output": 180.00,
        "tier": "premium",
        "provider": "openai_responses",
        "notes": "Sólo /v1/responses (no chat/completions)",
    },

    # --- Groq directo (LPU - super rapido, requiere GROQ_API_KEY) ---
    "groq-llama-3.3-70b": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía Groq para comparar infraestructuras.
        "provider_variant": True,
        # Vivo en Groq, pero GROQ_API_KEY está vacía → no lo podemos medir.
        # NO es retired: el modelo existe. Solo nos falta la llave.
        "unavailable": "falta GROQ_API_KEY",
        "id": "llama-3.3-70b-versatile",
        "name": "Llama 3.3 70B (Groq)",
        "cost_input": 0.59, "cost_output": 0.79,
        "tier": "cheap", "provider": "groq_direct",
        "open_source": True, "license": "Llama Community",
    },
    "groq-llama-3.1-8b": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía Groq para comparar infraestructuras.
        "provider_variant": True,
        # Vivo en Groq, pero GROQ_API_KEY está vacía → no lo podemos medir.
        # NO es retired: el modelo existe. Solo nos falta la llave.
        "unavailable": "falta GROQ_API_KEY",
        "id": "llama-3.1-8b-instant",
        "name": "Llama 3.1 8B Instant (Groq)",
        "cost_input": 0.05, "cost_output": 0.08,
        "tier": "ultra_cheap", "provider": "groq_direct",
        "open_source": True, "license": "Llama Community",
    },
    "groq-llama-4-scout": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía Groq para comparar infraestructuras.
        "provider_variant": True,
        "id": "meta-llama/llama-4-scout-17b-16e-instruct",
        "name": "Llama 4 Scout 17B (Groq preview)",
        "cost_input": 0.11, "cost_output": 0.34,
        "tier": "cheap", "provider": "groq_direct",
        "open_source": True, "license": "Llama Community",
    },
    "groq-gpt-oss-120b": {
        # Variante de proveedor: el modelo ya se mide en OpenRouter (plano común) y esa es
        # su fila canónica. Ésta conserva la medición en la infra del proveedor.
        "provider_variant": True,
        "id": "openai/gpt-oss-120b",
        "name": "GPT-OSS 120B (Groq)",
        "cost_input": 0.15, "cost_output": 0.60,
        "tier": "cheap", "provider": "groq_direct",
        "open_source": True, "license": "Apache 2.0",
    },
    "groq-gpt-oss-20b": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía Groq para comparar infraestructuras.
        "provider_variant": True,
        "id": "openai/gpt-oss-20b",
        "name": "GPT-OSS 20B (Groq)",
        "cost_input": 0.075, "cost_output": 0.30,
        "tier": "ultra_cheap", "provider": "groq_direct",
        "open_source": True, "license": "Apache 2.0",
    },
    "gpt-4o-high": {
        "id": "openai/gpt-4o:high",
        "name": "GPT-4o High",
        "cost_input": 5.00,
        "cost_output": 15.00,
        "tier": "premium",
    },

    # --- Ollama Cloud (suscripcion, requiere OLLAMA_CLOUD_API_KEY abajo) ---
    "deepseek-v4-pro-cloud": {
        # Variante de proveedor: el modelo ya se mide en OpenRouter (plano común) y esa es
        # su fila canónica. Ésta conserva la medición en la infra del proveedor.
        "provider_variant": True,
        "id": "deepseek-v4-pro",
        "name": "DeepSeek V4 Pro (Ollama Cloud)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_ollama",
        "provider": "ollama_cloud",
        "subscriptions": ["ollama_cloud_pro"],
        "open_source": True,
        "license": "MIT",
        "notes": "Recien agregado a Ollama Cloud (abril 28). Smoke test 22s OK, sin timeouts vs OpenRouter (76% cobertura) y NIM (504s timeouts).",
    },
    "deepseek-v4-flash-cloud": {
        # Variante de proveedor: el modelo ya se mide en OpenRouter (plano común) y esa es
        # su fila canónica. Ésta conserva la medición en la infra del proveedor.
        "provider_variant": True,
        "id": "deepseek-v4-flash",
        "name": "DeepSeek V4 Flash (Ollama Cloud)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_ollama",
        "provider": "ollama_cloud",
        "subscriptions": ["ollama_cloud_pro"],
        "open_source": True,
        "license": "MIT",
        "notes": "Variante mas chica de V4. Comparar con V4 Flash NIM (7.07 score).",
    },
    "qwen3.5-397b-cloud": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía Ollama Cloud para comparar infraestructuras.
        "provider_variant": True,
        "id": "qwen3.5:397b-cloud",
        "name": "Qwen 3.5 397B (Ollama Cloud)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "cloud_ollama",
        "provider": "ollama_cloud",
        "subscriptions": ["ollama_cloud_pro"],
        "open_source": True,
        "license": "Apache 2.0",
    },
    "qwen3.5-cloud": {
        # Id ambiguo (`qwen3.5:cloud`): Ollama no documenta qué tamaño sirve. Sin saber
        # QUÉ es, no se puede rankear ni recomendar.
        "retired": True,
        "unavailable": "id ambiguo (`qwen3.5:cloud`): Ollama no documenta qué tamaño sirve",
        "id": "qwen3.5:cloud",
        "name": "Qwen 3.5 (Ollama Cloud default)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "cloud_ollama",
        "provider": "ollama_cloud",
        "subscriptions": ["ollama_cloud_pro"],
        "open_source": True,
        "license": "Apache 2.0",
    },
    "gpt-oss-120b-cloud": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía Ollama Cloud para comparar infraestructuras.
        "provider_variant": True,
        "id": "gpt-oss:120b-cloud",
        "name": "GPT-OSS 120B (Ollama Cloud)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "cloud_ollama",
        "provider": "ollama_cloud",
        "subscriptions": ["ollama_cloud_pro"],
        "open_source": True,
        "license": "Apache 2.0",
    },

    # --- NVIDIA NIM (gratis con 40 RPM, OpenAI-compatible, 100+ modelos) ---
    # Ideal para benchmarks: secuencial, mismo formato API. Free tier suficiente.
    # Catálogo completo: https://build.nvidia.com/explore/discover
    "nim-nemotron-super-1.5": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "nvidia/llama-3.3-nemotron-super-49b-v1.5",
        "name": "Nemotron Super 49B v1.5 (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "NVIDIA Open Model",
        "notes": "Versión iterada del Nemotron Super 120B que ya medimos en Lote 2",
    },
    "openrouter-nemotron-3-ultra-550b": {
        "id": "nvidia/nemotron-3-ultra-550b-a55b",
        "name": "Nemotron 3 Ultra 550B",
        "cost_input": 0.5, "cost_output": 2.2,
        "tier": "cloud",
        "provider": "openrouter",
        "open_source": True, "license": "NVIDIA Open Model",
        "notes": "Modelo más grande de la familia Nemotron 3 (550B total / 55B activos) vía OpenRouter. Mucho más rápido que NIM gratuito. Disponible también como :free con rate limit.",
    },
    "nim-qwen3-next-instruct": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "qwen/qwen3-next-80b-a3b-instruct",
        "name": "Qwen 3-Next 80B Instruct (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Próxima generación Qwen — pendiente desde Lote 4",
    },
    "nim-qwen3-next-thinking": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "qwen/qwen3-next-80b-a3b-thinking",
        "name": "Qwen 3-Next 80B Thinking (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Variante thinking — comparar con Qwen 3-Next Instruct",
    },
    "nim-mistral-nemotron": {
        # Solo existe en NVIDIA NIM (no hay endpoint público en OpenRouter) y no tenemos
        # credencial. Medido en la infra de NIM: su velocidad no es comparable con el
        # resto. Fuera del ranking; los datos quedan.
        "provider_variant": True,
        "id": "mistralai/mistral-nemotron",
        "name": "Mistral-Nemotron (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Colaboración Mistral × NVIDIA, optimizado en Nemo",
    },
    "nim-kimi-k2-thinking": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "moonshotai/kimi-k2-thinking",
        "name": "Kimi K2 Thinking (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Modified MIT",
        "notes": "Variante thinking de K2 — comparar con K2.6 thinking",
    },
    "nim-deepseek-v4-flash": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "deepseek-ai/deepseek-v4-flash",
        "name": "DeepSeek V4 Flash (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "MIT",
        "notes": "Mismo modelo que probamos via OpenRouter — comparar latencia/calidad NIM vs OR",
    },
    "nim-deepseek-v4-pro": {
        # Variante de proveedor: el modelo ya se mide en OpenRouter (plano común) y esa es
        # su fila canónica. Ésta conserva la medición en la infra del proveedor.
        "provider_variant": True,
        "id": "deepseek-ai/deepseek-v4-pro",
        "name": "DeepSeek V4 Pro (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "MIT",
        "notes": "Re-test del flagship via NIM (vs OpenRouter que dio 76% cobertura en Lote 7-8)",
    },

    # --- Lote 9 candidatos NIM (todos gratis, 40 RPM) ---
    "nim-kimi-k2.5": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "moonshotai/kimi-k2.5",
        "name": "Kimi K2.5 (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Modified MIT",
        "notes": "Version nueva 2026, no tenemos K2.5 antes. Comparar con K2.6 thinking",
    },
    "nim-mistral-large-3": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "mistralai/mistral-large-3-675b-instruct-2512",
        "name": "Mistral Large 3 675B (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Flagship Mistral diciembre 2025. Comparar contra Mistral Small 4 (#4 ranking).",
    },
    "nim-step-3.5-flash": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "stepfun-ai/step-3.5-flash",
        "name": "Step 3.5 Flash (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Step 3.5 Flash - reemplazo de Step3 que fallo 91/91 con 404 en OpenRouter",
    },
    "nim-glm-5.1": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "z-ai/glm-5.1",
        "name": "GLM 5.1 (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "MIT",
        "notes": "Z.AI agentic, no tenemos. Variante GLM 5 con mejoras",
    },
    "nim-glm5": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "z-ai/glm5",
        "name": "GLM 5 (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "MIT",
        "notes": "Z.AI flagship base, comparar con 5.1",
    },
    "nim-magistral-small": {
        # Solo existe en NVIDIA NIM (no hay endpoint público en OpenRouter) y no tenemos
        # credencial. Medido en la infra de NIM: su velocidad no es comparable con el
        # resto. Fuera del ranking; los datos quedan.
        "provider_variant": True,
        "id": "mistralai/magistral-small-2506",
        "name": "Mistral Magistral Small (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Mistral con razonamiento, tamano medio",
    },
    "nim-ministral-14b": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "mistralai/ministral-14b-instruct-2512",
        "name": "Ministral 14B (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Mistral chico nuevo dic 2025 - comparar con Mistral Small 4",
    },
    "nim-devstral-2-123b": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "mistralai/devstral-2-123b-instruct-2512",
        "name": "Devstral 2 123B (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Mismo modelo que probamos via OpenRouter - comparar provider stability",
    },
    "nim-nemotron-nano-9b-v2": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "nvidia/nvidia-nemotron-nano-9b-v2",
        "name": "Nemotron Nano 9B v2 (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": False, "license": "NVIDIA Open License",
        "notes": "Variante chica de Nemotron 3, comparar con Nano 30B",
    },
    "nim-nemotron-3-nano-omni-reasoning": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
        "name": "Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "NVIDIA Open License",
        "thinking": True,
        "multimodal": True,
        "notes": "Lanzado 20 abril 2026. MoE 30B totales / 3B activos (A3B). Multimodal (texto+imagen+audio+video) + reasoning. Comparar contra Nano 30B normal y Nano 9B v2 — sirve para medir el costo de razonar y la ganancia de multimodal en single-turn texto.",
    },
    "nim-gemma-4-31b": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "google/gemma-4-31b-it",
        "name": "Gemma 4 31B (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Gemma Terms",
        "notes": "Mismo modelo que via OpenRouter (10 runs parciales) - completar via NIM gratis",
    },
    "nim-qwen3.5-397b": {
        # Variante de proveedor: el modelo se mide en OpenRouter (plano común).
        # Esta fila conserva la medición vía NVIDIA NIM para comparar infraestructuras.
        "provider_variant": True,
        "id": "qwen/qwen3.5-397b-a17b",
        "name": "Qwen 3.5 397B (NIM)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim",
        "provider": "nvidia_nim",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Mismo modelo que Cristian usa via Ollama Cloud para producción — comparar",
    },

    # --- DeepSeek V4 (lanzado abril 2026, MIT, 1M context) ---
    "deepseek-v4-flash": {
        "id": "deepseek/deepseek-v4-flash",
        "name": "DeepSeek V4 Flash (OpenRouter)",
        "cost_input": 0.098, "cost_output": 0.197,
        "tier": "cheap",
        "open_source": True, "license": "MIT",
        "notes": "284B params, 13B activos, 1M context. Sucesor V3.2. Precio re-verificado vía OpenRouter API 1 jun 2026 ($0.098/$0.197, antes $0.112/$0.224).",
    },
    "deepseek-r1": {
        "id": "deepseek/deepseek-r1",
        "name": "DeepSeek R1 (reasoning)",
        "cost_input": 0.70, "cost_output": 2.50,
        "tier": "cheap",
        "open_source": True, "license": "MIT",
        "thinking": True,
        "notes": "Reasoning puro DeepSeek (versión paga estable). Llena el gap de razonamiento — el :free tenía 0 runs por flakiness. Verificado vía OpenRouter API 1 jun 2026 ($0.70/$2.50).",
    },
    "deepseek-v4-pro": {
        "id": "deepseek/deepseek-v4-pro",
        "name": "DeepSeek V4 Pro",
        "cost_input": 0.435, "cost_output": 0.87,
        "tier": "cheap",
        "open_source": True, "license": "MIT",
        "notes": "1.6T params, 49B activos, 1M context. Flagship V4. Precio corregido may 2026 vía OpenRouter API ($0.435/$0.87, antes teníamos $1.74/$3.48 — 4x sobreprecio). Re-clasificado a tier cheap.",
    },

    # --- Google Gemini 3.1 (preview, abril 2026) ---
    "gemini-3.1-flash-lite": {
        "id": "google/gemini-3.1-flash-lite-preview",
        "name": "Gemini 3.1 Flash Lite",
        "cost_input": 0.25, "cost_output": 1.50,
        "tier": "cheap",
    },
    "gemini-3.1-flash-lite-thinking": {
        "id": "google/gemini-3.1-flash-lite-preview",
        "name": "Gemini 3.1 Flash Lite (thinking)",
        "cost_input": 0.25, "cost_output": 1.50,
        "tier": "cheap",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Misma versión con thinking forzado.",
    },
    "gemini-3.1-pro": {
        "id": "google/gemini-3.1-pro-preview",
        "name": "Gemini 3.1 Pro",
        "cost_input": 2.00, "cost_output": 12.00,
        "tier": "medium",
    },
    "gemini-3.1-pro-thinking": {
        "id": "google/gemini-3.1-pro-preview",
        "name": "Gemini 3.1 Pro (thinking)",
        "cost_input": 2.00, "cost_output": 12.00,
        "tier": "medium",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Misma versión con thinking forzado (effort=high). Costo ~5x mayor por test que sin thinking.",
    },

    # --- xAI Grok ---
    "grok-4.1-fast": {
        # Endpoint MUERTO: el proveedor lo apagó. Los datos quedan como estadística
        # histórica (son mediciones reales), pero no compite ni se recomienda.
        "retired": True,  # xAI: deprecated, recomienda migrar a Grok 4.3 (13-jul-2026)
        "id": "x-ai/grok-4.1-fast",
        "name": "Grok 4.1 Fast",
        "cost_input": 0.20, "cost_output": 0.50,
        "tier": "cheap",
    },
    "grok-4.20": {
        "id": "x-ai/grok-4.20",
        "name": "Grok 4.20",
        "cost_input": 1.25, "cost_output": 2.50,
        "tier": "medium",
        "notes": "Precio corregido may 2026 vía OpenRouter API ($1.25/$2.50, antes $2/$6).",
    },
    "grok-4.3": {
        "id": "x-ai/grok-4.3",
        "name": "Grok 4.3",
        "cost_input": 1.25, "cost_output": 2.50,
        "tier": "medium",
        "notes": "Flagship xAI (30 abr 2026), contexto 1M. Precio vía OpenRouter API may 2026.",
    },
    "grok-4.5": {
        "id": "x-ai/grok-4.5",
        "name": "Grok 4.5",
        "cost_input": 2.00, "cost_output": 6.00,
        "tier": "medium",
        "niah_max_context": 262144,
        "notes": "Nuevo flagship xAI (jul 2026), contexto 500K. $2/$6 vía OpenRouter API jul 2026.",
    },
    "grok-4.20-multi-agent": {
        "id": "x-ai/grok-4.20-multi-agent",
        "name": "Grok 4.20 Multi-Agent",
        "cost_input": 2.00, "cost_output": 6.00,
        "tier": "premium",
        "notes": "Variante multi-agente (Heavy) de Grok 4.20, contexto 2M. Precio vía OpenRouter API may 2026.",
    },

    # --- Mistral Small 4 (Apache 2.0) ---
    "mistral-small-4": {
        "id": "mistralai/mistral-small-2603",
        "name": "Mistral Small 4",
        "cost_input": 0.15, "cost_output": 0.60,
        "tier": "cheap",
        "open_source": True, "license": "Apache 2.0",
    },

    # --- NVIDIA Nemotron Nano (más chico de la familia) ---
    "nemotron-nano": {
        "id": "nvidia/nemotron-3-nano-30b-a3b",
        "name": "Nemotron 3 Nano 30B",
        "cost_input": 0.05, "cost_output": 0.20,
        "tier": "ultra_cheap",
        "open_source": True, "license": "NVIDIA Open",
    },

    # --- Xiaomi MiMo extras ---
    "mimo-v2-flash-free": {
        "id": "xiaomi/mimo-v2-flash:free",
        "name": "MiMo-V2-Flash (free)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "free",
        "open_source": True, "license": "MIT",
    },
    "mimo-v2-omni": {
        # Endpoint MUERTO: el proveedor lo apagó. Los datos quedan como estadística
        # histórica (son mediciones reales), pero no compite ni se recomienda.
        "retired": True,  # Xiaomi: deprecated, recomienda migrar a mimo-v2.5 (13-jul-2026)
        "id": "xiaomi/mimo-v2-omni",
        "name": "MiMo-V2-Omni (multimodal)",
        "cost_input": 0.40, "cost_output": 2.00,
        "tier": "cheap",
    },

    # --- Qwen 3.6 Plus free (a veces deprecado, probar a su disponibilidad) ---
    "qwen-3.6-plus-free": {
        "id": "qwen/qwen3.6-plus:free",
        "name": "Qwen 3.6 Plus (free)",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "free",
    },

    # --- Nous Research Hermes 4 (open, abril 2026) ---
    "hermes-4-70b": {
        "id": "nousresearch/hermes-4-70b",
        "name": "Hermes 4 70B",
        "cost_input": 0.13, "cost_output": 0.40,
        "tier": "cheap",
        "open_source": True, "license": "Llama 3 community",
        "notes": "Hybrid reasoning mode. Open-source de Nous Research. Sin reasoning explícito en este config.",
    },
    "hermes-4-70b-thinking": {
        "id": "nousresearch/hermes-4-70b",
        "name": "Hermes 4 70B (thinking)",
        "cost_input": 0.13, "cost_output": 0.40,
        "tier": "cheap",
        "open_source": True, "license": "Llama 3 community",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Misma versión que hermes-4-70b pero con reasoning forzado vía OpenRouter (effort=high). Technical report reporta +12 puntos MMLU al activar reasoning (76.7 → 88.4).",
    },
    "hermes-4-405b": {
        "id": "nousresearch/hermes-4-405b",
        "name": "Hermes 4 405B",
        "cost_input": 1.00, "cost_output": 3.00,
        "tier": "cheap",
        "open_source": True, "license": "Llama 3 community",
        "notes": "Flagship Hermes 4 con reasoning híbrido. Sin reasoning explícito en este config.",
    },
    "hermes-4-405b-thinking": {
        "id": "nousresearch/hermes-4-405b",
        "name": "Hermes 4 405B (thinking)",
        "cost_input": 1.00, "cost_output": 3.00,
        "tier": "cheap",
        "open_source": True, "license": "Llama 3 community",
        "thinking": True,
        "force_reasoning": True,
        "notes": "Misma versión que hermes-4-405b pero con reasoning forzado.",
    },

    # --- StepFun Step3 (multimodal MoE) ---
    "step3": {
        "id": "stepfun-ai/step3",
        "name": "Step3 (StepFun)",
        "cost_input": 1.00, "cost_output": 3.00,  # estimado, verificar
        "tier": "cheap",
        "open_source": True, "license": "Apache 2.0",
        "notes": "MoE 321B/38B activos, multimodal reasoning. 65K context. Lanzado ago 2025.",
    },

    # --- Xiaomi MiMo V2.5 (omnimodal nuevos abril 2026, 1M context) ---
    "mimo-v2.5-or": {
        "id": "xiaomi/mimo-v2.5",
        "name": "MiMo-V2.5 (omnimodal)",
        "cost_input": 0.40, "cost_output": 2.00,
        "tier": "cheap",
        "notes": "Omnimodal Pro-level a mitad de costo del Pro. 1.05M context.",
    },
    "mimo-v2.5-pro-or": {
        "id": "xiaomi/mimo-v2.5-pro",
        "name": "MiMo-V2.5 Pro",
        "cost_input": 1.00, "cost_output": 3.00,
        "tier": "medium",
        "notes": "Flagship Xiaomi 2026, agentic capabilities. 1.05M context.",
    },

    # --- ByteDance Seed-OSS (Apache 2.0, reasoning + agentic) ---
    "seed-oss-36b": {
        "id": "bytedance/seed-oss-36b-instruct",
        "name": "Seed-OSS 36B Instruct",
        "cost_input": 0.20, "cost_output": 0.60,  # estimado, verificar
        "tier": "cheap",
        "open_source": True, "license": "Apache 2.0",
        "notes": "Reasoning + math + coding + agentic. 131K context. ByteDance.",
    },

    # --- Xiaomi MiMo Token Plan (lanzado 22 abril 2026, requiere XIAOMI_API_KEY) ---
    # API OpenAI-compatible. Pricing en USD calculado del Standard plan ($14.08
    # first / $16 normal por 200M credits = $0.0704/M credits). Off-peak 16-24
    # UTC = 0.8x = 20% off. 1 token = 1 credit en V2.5; 2 credits en V2.5-Pro.
    "mimo-v2.5": {
        # Variante: el modelo ya está medido en OpenRouter (plano común) y esa es su
        # fila canónica. Ésta conserva la medición vía API directa Xiaomi para comparar.
        "provider_variant": True,
        "id": "mimo-v2.5",
        "name": "MiMo V2.5 (Xiaomi)",
        "cost_input": 0.07, "cost_output": 0.07,
        "tier": "subscription",
        "provider": "xiaomi_direct",
        "subscriptions": ["xiaomi_standard"],
        "open_source": False, "license": "Xiaomi Commercial",
        "notes": "All-in-one multimodal nativo, 1M context, lanzado 22 abril 2026",
    },
    "mimo-v2.5-pro": {
        # Variante: el modelo ya está medido en OpenRouter (plano común) y esa es su
        # fila canónica. Ésta conserva la medición vía API directa Xiaomi para comparar.
        "provider_variant": True,
        "id": "mimo-v2.5-pro",
        "name": "MiMo V2.5-Pro (Xiaomi)",
        "cost_input": 0.14, "cost_output": 0.14,
        "tier": "subscription",
        "provider": "xiaomi_direct",
        "subscriptions": ["xiaomi_standard"],
        "open_source": False, "license": "Xiaomi Commercial",
        "notes": "Flagship reasoning, agentic, 1M context, lanzado 22 abril 2026",
    },
    "mimo-v2-pro-xiaomi": {
        # Sin acceso: la suscripción a Xiaomi se dio de baja (jul-2026) Y su versión
        # pública en OpenRouter está deprecada. No lo puede llamar nadie sin ese plan.
        # Los datos quedan como estadística histórica.
        "retired": True,
        "id": "mimo-v2-pro",
        "name": "MiMo V2-Pro (Xiaomi direct)",
        "cost_input": 0.07, "cost_output": 0.07,
        "tier": "subscription",
        "provider": "xiaomi_direct",
        "subscriptions": ["xiaomi_standard"],
        "open_source": True, "license": "MIT",
        "notes": "Mismo modelo que via OpenRouter — comparar provider stability",
    },
    "mimo-v2-omni-xiaomi": {
        # Sin acceso: la suscripción a Xiaomi se dio de baja (jul-2026) Y su versión
        # pública en OpenRouter está deprecada. No lo puede llamar nadie sin ese plan.
        # Los datos quedan como estadística histórica.
        "retired": True,
        "id": "mimo-v2-omni",
        "name": "MiMo V2-Omni (Xiaomi direct)",
        "cost_input": 0.07, "cost_output": 0.07,
        "tier": "subscription",
        "provider": "xiaomi_direct",
        "subscriptions": ["xiaomi_standard"],
        "open_source": True, "license": "MIT",
        "notes": "Mismo modelo que via OpenRouter — comparar provider stability",
    },
    # --- Gemma 4 en DGX Spark via llama.cpp/llama-server (multimodal, puertos propios) ---
    "spark-gemma4-12b": {
        # Solo existe self-hosted: no hay endpoint público. Su velocidad es la de TU
        # hardware. Se reporta en la tabla de self-hosted, no compite en el ranking
        # principal contra modelos servidos por datacenters.
        "self_hosted": True,
        "id": "gemma-4-12b-it-Q4_K_M.gguf",
        "context_window": 131072,
        "name": "Gemma 4 12B (Spark llama-server Q4_K_M)",
        "cost_input": 0.05,        # OR-equivalente (~12B dense); free_runtime real
        "cost_output": 0.20,
        "tier": "local",
        "open_source": True,
        "license": "Gemma Terms",
        "provider": "llama_server",
        "base_url": "http://localhost:8091/v1",
        "free_runtime": True,
        "vram_gb": 9,
        "notes": "Q4_K_M en DGX Spark via llama.cpp/llama-server (multimodal). Medido SIN reasoning (enable_thinking=false) — uso agente/baja latencia. Comparar con el 31B llama-server.",
    },
    "spark-gemma4-31b-llamacpp": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "gemma-4-31B-it-Q4_K_M.gguf",
        "context_window": 131072,
        "name": "Gemma 4 31B (Spark llama-server Q4_K_M)",
        "cost_input": 0.12,        # OR-equivalente; free_runtime real
        "cost_output": 0.37,
        "tier": "local",
        "open_source": True,
        "license": "Gemma Terms",
        "provider": "llama_server",
        "base_url": "http://localhost:8092/v1",
        "free_runtime": True,
        "vram_gb": 20,
        "notes": "Q4_K_M en DGX Spark via llama.cpp/llama-server (multimodal). Medido SIN reasoning (enable_thinking=false) — uso agente/baja latencia. Comparar con 12B llama-server y 31B Ollama/NIM (esos SÍ razonan).",
    },
    # --- Variantes CON reasoning interno (mismos builds, provider llama_server_think) ---
    "spark-gemma4-12b-think": {
        # Solo existe self-hosted: no hay endpoint público. Su velocidad es la de TU
        # hardware. Se reporta en la tabla de self-hosted, no compite en el ranking
        # principal contra modelos servidos por datacenters.
        "self_hosted": True,
        "id": "gemma-4-12b-it-Q4_K_M.gguf",
        "name": "Gemma 4 12B (Spark llama-server, reasoning)",
        "cost_input": 0.05,
        "cost_output": 0.20,
        "tier": "local",
        "open_source": True,
        "license": "Gemma Terms",
        "provider": "llama_server_think",
        "base_url": "http://localhost:8091/v1",
        "context_window": 131072,
        "free_runtime": True,
        "vram_gb": 9,
        "notes": "Mismo build que spark-gemma4-12b pero CON reasoning interno (default). Comparar delta calidad vs latencia contra la variante sin reasoning.",
    },
    "spark-gemma4-31b-think": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "gemma-4-31B-it-Q4_K_M.gguf",
        "name": "Gemma 4 31B (Spark llama-server, reasoning)",
        "cost_input": 0.12,
        "cost_output": 0.37,
        "tier": "local",
        "open_source": True,
        "license": "Gemma Terms",
        "provider": "llama_server_think",
        "base_url": "http://localhost:8092/v1",
        "context_window": 131072,
        "free_runtime": True,
        "vram_gb": 20,
        "notes": "Mismo build que spark-gemma4-31b-llamacpp pero CON reasoning interno (default). Comparar delta calidad vs latencia contra la variante sin reasoning.",
    },

    # ─────────────────────────────────────────────────────────────────────
    # Plano común: OpenRouter.
    # Estos modelos vivían en NIM / Groq / Ollama Cloud, donde la velocidad y la
    # latencia son de la INFRA y no del modelo (el mismo Qwen 3.5 397B da 5.43 en
    # Ollama Cloud y 8.17 en NIM) — y donde hoy ni siquiera tenemos credencial.
    # Medirlos a todos por el mismo camino es lo único que hace comparable la
    # comparación. Sus filas antiguas quedan como `provider_variant`: fuera del
    # ranking, pero conservadas, porque la diferencia entre proveedores es un
    # hallazgo, no basura.
    # ─────────────────────────────────────────────────────────────────────
    "or-llama-3.3-70b": {
        "id": "meta-llama/llama-3.3-70b-instruct",
        "name": "Llama 3.3 70B",
        "cost_input": 0.1, "cost_output": 0.32,
        "tier": "cheap", "provider": "openrouter",
        "open_source": True, "license": "Llama Community",
    },
    "or-llama-3.1-8b": {
        "id": "meta-llama/llama-3.1-8b-instruct",
        "name": "Llama 3.1 8B Instant",
        "cost_input": 0.02, "cost_output": 0.03,
        "tier": "ultra_cheap", "provider": "openrouter",
        "open_source": True, "license": "Llama Community",
    },
    "or-llama-4-scout": {
        "id": "meta-llama/llama-4-scout",
        "name": "Llama 4 Scout 17B",
        "cost_input": 0.1, "cost_output": 0.3,
        "tier": "cheap", "provider": "openrouter",
        "open_source": True, "license": "Llama Community",
    },
    "or-gpt-oss-20b": {
        "id": "openai/gpt-oss-20b",
        "name": "GPT-OSS 20B",
        "cost_input": 0.029, "cost_output": 0.14,
        "tier": "ultra_cheap", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-gpt-oss-120b": {
        "id": "openai/gpt-oss-120b",
        "name": "GPT-OSS 120B",
        "cost_input": 0.036, "cost_output": 0.18,
        "tier": "cloud_ollama", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-nemotron-super-1.5": {
        "id": "nvidia/llama-3.3-nemotron-super-49b-v1.5",
        "name": "Nemotron Super 49B v1.5",
        "cost_input": 0.4, "cost_output": 0.4,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "NVIDIA Open Model",
    },
    "or-qwen3-next-instruct": {
        "id": "qwen/qwen3-next-80b-a3b-instruct",
        "name": "Qwen 3-Next 80B Instruct",
        "cost_input": 0.09, "cost_output": 1.1,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-qwen3-next-thinking": {
        "id": "qwen/qwen3-next-80b-a3b-thinking",
        "name": "Qwen 3-Next 80B Thinking",
        "cost_input": 0.098, "cost_output": 0.78,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-kimi-k2-thinking": {
        "id": "moonshotai/kimi-k2-thinking",
        "name": "Kimi K2 Thinking",
        "cost_input": 0.6, "cost_output": 2.5,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Modified MIT",
    },
    "or-kimi-k2.5": {
        "id": "moonshotai/kimi-k2.5",
        "name": "Kimi K2.5",
        "cost_input": 0.375, "cost_output": 2.025,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Modified MIT",
    },
    "or-mistral-large-3": {
        "id": "mistralai/mistral-large-2512",
        "name": "Mistral Large 3 675B",
        "cost_input": 0.5, "cost_output": 1.5,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-step-3.5-flash": {
        # OpenRouter lista el id pero NINGÚN proveedor lo sirve: "No endpoints found".
        # El modelo existe en el catálogo y no se puede llamar — que para quien
        # decide es lo mismo que no existir. (14-jul-2026)
        "retired": True,
        "id": "stepfun/step-3.5-flash",
        "name": "Step 3.5 Flash",
        "cost_input": 0.1, "cost_output": 0.3,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-glm5": {
        "id": "z-ai/glm-5",
        "name": "GLM 5",
        "cost_input": 0.6, "cost_output": 1.92,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "MIT",
    },
    "or-ministral-14b": {
        "id": "mistralai/ministral-14b-2512",
        "name": "Ministral 14B",
        "cost_input": 0.2, "cost_output": 0.2,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-nemotron-nano-9b-v2": {
        "id": "nvidia/nemotron-nano-9b-v2:free",
        "name": "Nemotron Nano 9B v2",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": False, "license": "NVIDIA Open License",
    },
    "or-nemotron-3-nano-omni-reasoning": {
        "id": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        "name": "Nemotron 3 Nano Omni 30B-A3B Reasoning",
        "cost_input": 0.0, "cost_output": 0.0,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "NVIDIA Open License",
    },
    "or-gemma-4-31b": {
        "id": "google/gemma-4-31b-it",
        "name": "Gemma 4 31B",
        "cost_input": 0.12, "cost_output": 0.35,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Gemma Terms",
    },
    "or-qwen3.5-397b": {
        "id": "qwen/qwen3.5-397b-a17b",
        "name": "Qwen 3.5 397B",
        "cost_input": 0.385, "cost_output": 2.45,
        "tier": "cloud_nim", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },


    # GPT en el plano común (antes solo por la API directa de OpenAI).
    "or-gpt-4.1": {
        "id": "openai/gpt-4.1",
        "name": "GPT-4.1",
        "cost_input": 2.0, "cost_output": 8.0,
        "tier": "medium", "provider": "openrouter",
        "open_source": False, "license": "Proprietary",
    },
    "or-gpt-4.1-mini": {
        "id": "openai/gpt-4.1-mini",
        "name": "GPT-4.1 Mini",
        "cost_input": 0.4, "cost_output": 1.6,
        "tier": "cheap", "provider": "openrouter",
        "open_source": False, "license": "Proprietary",
    },
    "or-gpt-5.4": {
        "id": "openai/gpt-5.4",
        "name": "GPT-5.4",
        "cost_input": 2.5, "cost_output": 15.0,
        "tier": "premium", "provider": "openrouter",
        "open_source": False, "license": "Proprietary",
    },
    "or-gpt-5.4-mini": {
        "id": "openai/gpt-5.4-mini",
        "name": "GPT-5.4 Mini",
        "cost_input": 0.75, "cost_output": 4.5,
        "tier": "cheap", "provider": "openrouter",
        "open_source": False, "license": "Proprietary",
    },
    "or-gpt-5.5": {
        "id": "openai/gpt-5.5",
        "name": "GPT-5.5",
        "cost_input": 5.0, "cost_output": 30.0,
        "tier": "premium", "provider": "openrouter",
        "open_source": False, "license": "Proprietary",
    },


    # Modelos que corríamos en el Spark y AHORA se miden en OpenRouter.
    # La máquina propia no puede ser el camino por defecto: su velocidad es la de TU
    # GPU, no la del modelo, y mezclarla con datacenters rompe la comparación igual que
    # mezclar Groq con NIM. El Spark responde otra pregunta ("¿puedo correrlo yo?"), y
    # esa pregunta tiene su propia tabla.
    "or-qwen-3.5-35b": {
        "id": "qwen/qwen3.5-35b-a3b",
        "name": "Qwen 3.5 35B",
        "cost_input": 0.14, "cost_output": 1.0,
        "tier": "cheap", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-qwen-2.5-72b": {
        # OpenRouter lo lista pero ningún proveedor lo sirve: el upstream responde
        # "does not exist". Está en el catálogo y no se puede llamar — que para quien
        # decide es lo mismo que no existir. (14-jul-2026)
        "retired": True,
        "id": "qwen/qwen-2.5-72b-instruct",
        "name": "Qwen 2.5 72B",
        "cost_input": 0.36, "cost_output": 0.4,
        "tier": "cheap", "provider": "openrouter",
        "open_source": True, "license": "Apache 2.0",
    },
    "or-deepseek-v3": {
        "id": "deepseek/deepseek-v3.2",
        "name": "DeepSeek V3",
        "cost_input": 0.214, "cost_output": 0.322,
        "tier": "cheap", "provider": "openrouter",
        "open_source": True, "license": "MIT",
    },
    "or-minimax-m2.5": {
        "id": "minimax/minimax-m2.5",
        "name": "MiniMax M2.5",
        "cost_input": 0.15, "cost_output": 0.9,
        "tier": "cheap", "provider": "openrouter",
        "open_source": True, "license": "MIT",
    },


    # GPT-5.5 Pro en el plano común (antes solo por la Responses API de OpenAI).
    "or-gpt-5.5-pro": {
        "id": "openai/gpt-5.5-pro",
        "name": "GPT-5.5 Pro",
        "cost_input": 30.0, "cost_output": 180.0,
        "tier": "premium", "provider": "openrouter",
        "open_source": False, "license": "Proprietary",
    },

}

# Modelos locales via Ollama - Optimizados para NVIDIA DGX Spark (128GB RAM unificada)
# Con 128GB puedes correr modelos de hasta ~200B parametros
OLLAMA_MODELS = {
    # --- Modelos que corren en DGX Spark (128GB) ---
    "local-gemma4-31b": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "gemma4:31b",
        "name": "Gemma 4 31B (DGX Spark Q4_K_M)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Gemma Terms",
        "vram_gb": 20,
        "notes": "Q4_K_M en DGX Spark via Ollama. Comparar con Gemma 4 31B NIM y OpenRouter.",
    },
    "local-nemotron-3-super-120b": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "nemotron-3-super:120b",
        "name": "Nemotron 3 Super 120B (DGX Spark Q4_K_M)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": False,
        "license": "NVIDIA Open License",
        "vram_gb": 87,
        "notes": "Q4_K_M en DGX Spark. Modelo gigante, primer test post cold start tarda ~3-5min.",
    },
    "local-nemotron-3-nano-omni-reasoning": {
        # Solo existe self-hosted: no hay endpoint público. Su velocidad es la de TU
        # hardware. Se reporta en la tabla de self-hosted, no compite en el ranking
        # principal contra modelos servidos por datacenters.
        "self_hosted": True,
        "id": "hf.co/unsloth/NVIDIA-Nemotron-3-Nano-Omni-30B-A3B-Reasoning-GGUF:Q4_K_M",
        "name": "Nemotron 3 Nano Omni 30B-A3B Reasoning (DGX Spark Q4_K_M)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "NVIDIA Open License",
        "vram_gb": 18,
        "thinking": True,
        "multimodal": True,
        "notes": "MoE 30B totales / 3B activos (A3B), thinking + multimodal. GGUF community por unsloth — los tags oficiales de Ollama (nemotron3:33b) son la versión base, no la Omni Reasoning. Ollama: `ollama pull hf.co/unsloth/NVIDIA-Nemotron-3-Nano-Omni-30B-A3B-Reasoning-GGUF:Q4_K_M`. Comparar contra el mismo modelo via NIM (FP16) para medir costo de cuantización.",
    },
    "local-nemotron3-base-33b": {
        # Solo existe self-hosted: no hay endpoint público. Su velocidad es la de TU
        # hardware. Se reporta en la tabla de self-hosted, no compite en el ranking
        # principal contra modelos servidos por datacenters.
        "self_hosted": True,
        "id": "nemotron3:33b-q4_K_M",
        "name": "Nemotron 3 Base 33B (DGX Spark Q4_K_M)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "NVIDIA Open License",
        "vram_gb": 26,
        "notes": "Nemotron 3 base 33B (NO la versión Omni Reasoning) en Q4_K_M via Ollama oficial. Comparar con Nemotron 3 Super 120B (DGX, también Q4) y Nemotron 3 Nano Omni Reasoning cuando esté disponible.",
    },
    # --- Tags actualizados al sweep DGX Spark (1 jun 2026) ---
    # Reemplazan los tags obsoletos qwen3.5:25b / qwen3.5:72b que ya no existen
    # en Ollama (deuda del roadmap). Verificados con `ollama list` en spark-8c1f.
    "local-qwen3.5-35b": {
        # Variante self-hosted: ahora este modelo se mide en OpenRouter (plano común).
        # Acá su velocidad es la de TU Spark, no la del modelo. La fila queda para
        # responder "¿y si lo corro en mi propia máquina?", que es otra pregunta.
        "provider_variant": True,
        "self_hosted": True,
        "id": "qwen3.5:35b",
        "name": "Qwen 3.5 35B (DGX Spark)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 23,
        "notes": "Tag real instalado en DGX Spark. Comparar vs Qwen 3.5 397B Cloud/NIM (misma familia, distinto tamaño).",
    },
    "local-qwen3.6-27b": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "qwen3.6:27b",
        "name": "Qwen 3.6 27B base (DGX Spark)",
        "cost_input": 0.29,
        "cost_output": 3.20,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 17,
        "or_id": "qwen/qwen3.6-27b",
        "notes": "Qwen 3.6 BASE (Apache 2.0, pesos en HF) — cierra el gap del roadmap: solo teníamos Qwen 3.6 Plus (propietario API-only). Corre gratis local en DGX Spark; el costo del ranking usa el precio OpenRouter ($0.29/$3.20) para comparación justa.",
    },
    "local-qwen3.6-35b": {
        # Solo existe self-hosted: no hay endpoint público. Su velocidad es la de TU
        # hardware. Se reporta en la tabla de self-hosted, no compite en el ranking
        # principal contra modelos servidos por datacenters.
        "self_hosted": True,
        "id": "qwen3.6:35b",
        "name": "Qwen 3.6 35B base (DGX Spark)",
        "cost_input": 0.14,
        "cost_output": 1.00,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 23,
        "or_id": "qwen/qwen3.6-35b-a3b",
        "notes": "Qwen 3.6 BASE 35B (MoE a3b) abierto. Corre gratis local en DGX Spark; costo del ranking = precio OpenRouter ($0.14/$1.00). Comparar vs 3.6 Plus propietario y vs 3.6 27B.",
    },
    "local-qwen3-coder-next": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "qwen3-coder-next:q4_K_M",
        "name": "Qwen3-Coder-Next (DGX Spark Q4_K_M)",
        "cost_input": 0.11,
        "cost_output": 0.80,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 51,
        "or_id": "qwen/qwen3-coder-next",
        "notes": "Coding-especializado next-gen. Corre gratis local en DGX Spark (Q4_K_M); costo del ranking = precio OpenRouter ($0.11/$0.80, FP8). Comparar vs Devstral Small (#1) y Qwen3 Coder en el pilar Coding. Caveat: la versión local Q4 puede rendir algo bajo la FP8 de OpenRouter.",
    },
    "local-qwen2.5-72b": {
        # Variante self-hosted: ahora este modelo se mide en OpenRouter (plano común).
        # Acá su velocidad es la de TU Spark, no la del modelo. La fila queda para
        # responder "¿y si lo corro en mi propia máquina?", que es otra pregunta.
        "provider_variant": True,
        "self_hosted": True,
        "id": "qwen2.5:72b",
        "name": "Qwen 2.5 72B (DGX Spark)",
        "cost_input": 0.36,
        "cost_output": 0.40,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 47,
        "or_id": "qwen/qwen-2.5-72b-instruct",
        "notes": "Generación previa instalada en el Spark — baseline para medir salto 2.5→3.5→3.6 a igual tamaño grande. Corre gratis local; costo del ranking = precio OpenRouter ($0.36/$0.40).",
    },
    "llama3.3-70b": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "llama3.3:70b",
        "name": "Llama 3.3 70B (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Llama Community",
        "vram_gb": 40,
    },
    "llama4-maverick": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "llama4-maverick",
        "name": "Llama 4 Maverick (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Llama Community",
        "vram_gb": 60,
    },
    "gemma4-31b": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "gemma4:31b",
        "name": "Gemma 4 31B (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 20,
    },
    "gemma4-26b-moe": {
        # Solo existe self-hosted: no hay endpoint público. Su velocidad es la de TU
        # hardware. Se reporta en la tabla de self-hosted, no compite en el ranking
        # principal contra modelos servidos por datacenters.
        "self_hosted": True,
        "id": "gemma4:26b",
        "name": "Gemma 4 26B MoE (local, solo 3.8B activos)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 16,
    },
    "local-devstral-small-2": {
        # Solo existe self-hosted: no hay endpoint público. Su velocidad es la de TU
        # hardware. Se reporta en la tabla de self-hosted, no compite en el ranking
        # principal contra modelos servidos por datacenters.
        "self_hosted": True,
        "id": "devstral-small2:24b",
        "name": "Devstral Small 2 24B (DGX Spark Q4_K_M)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 15,
        "notes": "Nueva generación pequeña de Mistral (24B). Verificar tag real en Ollama con `ollama pull devstral-small2:24b` antes de correr. Comparar contra Devstral Small original y Qwen3-Coder-Next en coding.",
    },
    "local-diffusiongemma-26b": {
        # Solo existe self-hosted: no hay endpoint público. Su velocidad es la de TU
        # hardware. Se reporta en la tabla de self-hosted, no compite en el ranking
        # principal contra modelos servidos por datacenters.
        "self_hosted": True,
        "id": "hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0",
        "name": "DiffusionGemma 26B-A4B (DGX Spark Q8_0)",
        "provider": "diffusion_cli",
        "bin_path": "/home/ctala/llama.cpp-diffusion/build/bin/llama-diffusion-cli",
        "gguf_path": "/home/ctala/models/diffusiongemma/diffusiongemma-26B-A4B-it-Q8_0.gguf",
        "ngl": 99,
        "ctx_size": 262144,
        "seed": 42,
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 26,
        "thinking": True,
        "multimodal": True,
        "notes": (
            "Modelo de difusión textual (NO autoregresivo) basado en Gemma 4 26B-A4B (3.8B activos). "
            "Genera bloques de 256 tokens en paralelo vía denoising, optimizado para velocidad y multimodalidad. "
            "Requiere llama.cpp PR #24423 (binario llama-diffusion-cli) o Unsloth Studio; Ollama todavía no lo soporta. "
            "Instrucciones: https://unsloth.ai/docs/models/diffusiongemma#llama.cpp-guide. "
            "Contexto 256K, vision nativa (OCR, documentos, UI, video frames), tool calling y thinking con <|think|>. "
            "Q8_0 (~25 GB) para medir calidad real sin pérdida de cuantización. "
            "Para probar en Spark: descargar Q8_0 y servir con llama-diffusion-cli -m gguf -ngl 99 -n 2048."
        ),
    },
    "local-deepseek-v3": {
        # Variante self-hosted: ahora este modelo se mide en OpenRouter (plano común).
        # Acá su velocidad es la de TU Spark, no la del modelo. La fila queda para
        # responder "¿y si lo corro en mi propia máquina?", que es otra pregunta.
        "provider_variant": True,
        "self_hosted": True,
        "id": "deepseek-v3",
        "name": "DeepSeek V3 (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "MIT",
        "vram_gb": 120,
        "note": "Cabe justo en DGX Spark 128GB con cuantizacion",
    },
    "mistral-nemo-12b": {
        # Variante self-hosted: este modelo ya se mide en OpenRouter (plano común).
        # Su velocidad acá es la de TU Spark, no la del modelo — compararla contra un
        # datacenter no significa nada. La fila queda para responder "¿y si lo corro yo?".
        "provider_variant": True,
        "self_hosted": True,
        "id": "mistral-nemo",
        "name": "Mistral Nemo 12B (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "Apache 2.0",
        "vram_gb": 8,
    },
    "phi-4-14b": {
        # ⚠️ ES EL JUEZ del benchmark. NO se mide, nunca.
        # Toda la neutralidad del juez se apoya en que Microsoft no tiene modelos acá
        # ("no puede auto-preferirse"). Medirlo rompería esa premisa: se estaría
        # puntuando a sí mismo. Hoy tiene 0 runs; que siga así.
        "is_judge": True,
        "retired": True,  # no es que muriera: es que no compite
        "id": "phi4",
        "name": "Phi-4 14B (local)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "MIT",
        "vram_gb": 10,
    },
    "minimax-m2.5": {
        # Variante self-hosted: ahora este modelo se mide en OpenRouter (plano común).
        # Acá su velocidad es la de TU Spark, no la del modelo. La fila queda para
        # responder "¿y si lo corro en mi propia máquina?", que es otra pregunta.
        "provider_variant": True,
        "self_hosted": True,
        "id": "MiniMax-M2.5",
        "name": "MiniMax M2.5 (local, open-source)",
        "cost_input": 0.0,
        "cost_output": 0.0,
        "tier": "local",
        "open_source": True,
        "license": "MIT",
        "vram_gb": 90,
        "note": "80.2% SWE-Bench, cabe en DGX Spark",
    },
}

# ============================================================================
# Context windows (max tokens) — fuente: OpenRouter /api/v1/models + manuales.
# El runner saltea tests niah cuyo context_tokens supera este valor (cada
# modelo se mide hasta su techo). Regenerar con scripts/update_context_windows
# o consultando OpenRouter. Verificado 2 jun 2026.
# ============================================================================
CONTEXT_WINDOWS = {
    'MiniMax-M2.7': 204800,
    'MiniMax-M2.7-highspeed': 204800,
    'MiniMax-M3': 1048576,
    'anthropic/claude-haiku-4.5': 200000,
    # Opus 4.8: OpenRouter/API usa punto; suscripción Claude Code usa guion sin provider prefix.
    # Ambos IDs deben tener 1M para que el runner y la UI reporten context_window correcto.
    'anthropic/claude-opus-4.8': 1000000,
    'anthropic/claude-opus-4-8': 1000000,
    'claude-opus-4-8': 1000000,
    # Fable 5: solo se mantiene la versión suscripción (API fue deprecada/abajo).
    'claude-fable-5': 1000000,
    'anthropic/claude-sonnet-4': 1000000,
    'cohere/north-mini-code': 128000,
    'devstral-small2:24b': 131072,
    'deepseek-ai/deepseek-v4-flash': 1048576,
    'deepseek-ai/deepseek-v4-pro': 1048576,
    'deepseek-v4-flash': 1048576,
    'deepseek-v4-pro': 1048576,
    'deepseek/deepseek-chat': 131072,
    'deepseek/deepseek-r1': 163840,
    'deepseek/deepseek-v4-flash': 1048576,
    'deepseek/deepseek-v4-pro': 1048576,
    'google/gemini-2.5-flash': 1048576,
    'google/gemini-2.5-flash-lite': 1048576,
    'google/gemini-2.5-pro': 1048576,
    'google/gemini-3.1-flash-lite-preview': 1048576,
    'google/gemini-3.1-pro-preview': 1048576,
    'google/gemini-3.5-flash': 1048576,
    'google/gemma-4-26b-a4b-it': 262144,
    'google/gemma-4-31b-it': 262144,
    'hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0': 262144,
    'meta-llama/llama-3.3-70b-instruct:free': 131072,
    'meta-llama/llama-4-maverick': 1048576,
    'mimo-v2.5': 1048576,
    'mimo-v2.5-pro': 1048576,
    'minimax/minimax-m2.7': 204800,
    'minimax/minimax-m3': 1048576,
    'mistralai/devstral-2512': 262144,
    'mistralai/mistral-large': 128000,
    'mistralai/mistral-nemo': 131072,
    'mistralai/mistral-small-2603': 262144,
    'moonshotai/kimi-k2': 131072,
    'moonshotai/kimi-k2-thinking': 262144,
    'moonshotai/kimi-k2.5': 262144,
    'moonshotai/kimi-k2.6': 262144,
    'moonshotai/kimi-k2.7-code': 262144,
    'nousresearch/hermes-4-405b': 131072,
    'nousresearch/hermes-4-70b': 131072,
    'nvidia/nemotron-3-ultra-550b-a55b': 131072,  # OpenRouter / NIM
    'nvidia/llama-3.3-nemotron-super-49b-v1.5': 131072,
    'nvidia/nemotron-3-nano-30b-a3b': 262144,
    'nvidia/nemotron-3-super-120b-a12b': 1000000,
    'openai/gpt-4o': 128000,
    'openai/gpt-oss-120b': 131072,
    'openai/gpt-oss-20b': 131072,
    'qwen/qwen3-coder': 1048576,
    'qwen/qwen3-coder-next': 262144,
    'qwen/qwen3-next-80b-a3b-instruct': 262144,
    'qwen/qwen3-next-80b-a3b-thinking': 262144,
    'qwen/qwen3.5-397b-a17b': 262144,
    'qwen/qwen3.6-27b': 262144,
    'qwen/qwen3.6-35b-a3b': 262144,
    'qwen/qwen3.6-max-preview': 262144,
    'qwen/qwen3.6-plus': 1000000,
    'qwen3.5:397b-cloud': 262144,
    'x-ai/grok-4.20': 2000000,
    'x-ai/grok-4.20-multi-agent': 2000000,
    'x-ai/grok-4.3': 1000000,
    'x-ai/grok-4.5': 500000,
    'openai/gpt-5.6-luna': 1050000,
    'openai/gpt-5.6-terra': 1050000,
    'openai/gpt-5.6-sol': 1050000,
    'xiaomi/mimo-v2-flash': 262144,
    'z-ai/glm-5.1': 202752,
    'z-ai/glm-5.2': 1048576,
}

# Inyectar context_window a cada modelo (por id). Los que no estén en el mapa
# quedan sin context_window → el runner corre todos los tamaños (error→N/A).
for _m in list(MODELS.values()) + list(OLLAMA_MODELS.values()):
    if "context_window" not in _m:
        _cw = CONTEXT_WINDOWS.get(_m.get("id"))
        if _cw:
            _m["context_window"] = _cw


# ============================================================================
# Repricing a precio OpenRouter (2 jun 2026) — decisión del usuario: NINGÚN
# modelo debe tener costo $0 porque infla el cost_score (~10) y arruina la
# comparación. Los que corren gratis (NIM 40rpm, DGX local, Ollama Cloud sub)
# se costean al precio OpenRouter del MISMO modelo (o el equivalente más cercano
# para los NIM-exclusivos). Verificado vía OpenRouter /api/v1/models.
# El campo `free_runtime: True` marca que el runtime real es $0 (la calculadora
# puede mostrarlo), pero el cost del ranking usa el precio OR de abajo.
# ============================================================================
OR_COMPARISON_PRICING = {
    'gemma4-31b': (0.12, 0.37),
    'gpt-oss-120b-cloud': (0.039, 0.18),
    'llama-3.3-70b-free': (0.0, 0.0),
    'local-gemma4-31b': (0.12, 0.37),
    'local-nemotron-3-nano-omni-reasoning': (0.1, 0.4),
    'local-nemotron-3-super-120b': (0.09, 0.45),
    'local-nemotron3-base-33b': (0.09, 0.45),
    'nim-deepseek-v4-flash': (0.098, 0.197),
    'nim-devstral-2-123b': (0.4, 2.0),
    'nim-gemma-4-31b': (0.12, 0.37),
    'nim-glm-5.1': (0.98, 3.08),
    'nim-glm5': (0.98, 3.08),
    'nim-kimi-k2-thinking': (0.6, 2.5),
    'nim-kimi-k2.5': (0.4, 1.9),
    'nim-magistral-small': (0.5, 1.5),
    'nim-ministral-14b': (0.1, 0.4),
    'nim-mistral-large-3': (2.0, 6.0),
    'nim-mistral-nemotron': (0.3, 1.2),
    'nim-nemotron-3-nano-omni-reasoning': (0.1, 0.4),
    'nim-nemotron-nano-9b-v2': (0.05, 0.2),
    'nim-nemotron-super-1.5': (0.1, 0.4),
    'openrouter-nemotron-3-ultra-550b': (0.5, 2.2),
    'nim-qwen3-next-instruct': (0.09, 1.1),
    'nim-qwen3-next-thinking': (0.098, 0.78),
    'nim-qwen3.5-397b': (0.39, 2.34),
    'nim-step-3.5-flash': (1.0, 3.0),
    'qwen3.5-397b-cloud': (0.39, 2.34),
    'qwen3.5-cloud': (0.39, 2.34),
}

# Aplicar el repricing: a cada modelo con costo $0 que esté en el mapa, asignarle
# el precio OpenRouter equivalente y marcar free_runtime=True (corre gratis pero
# se costea a OR para la comparación). Ver memoria benchmark-pricing-openrouter-source.
for _k, _price in OR_COMPARISON_PRICING.items():
    _m = MODELS.get(_k) or OLLAMA_MODELS.get(_k)
    if _m and float(_m.get("cost_input", 0)) == 0:
        _m["free_runtime"] = True
        _m["cost_input"], _m["cost_output"] = _price

# Extensión del repricing (3 jun 2026): cubre los $0 restantes que el mapa
# inicial no tenía — :free mirrors, cloud/nim DeepSeek (incl V4 Pro), locales.
# Así NINGÚN modelo queda en $0 en la calculadora.
OR_COMPARISON_PRICING_EXT = {
    'deepseek-r1-free': (0.7, 2.5),
    'deepseek-v3': (0.2, 0.8),
    'deepseek-v4-flash-cloud': (0.098, 0.197),
    'deepseek-v4-pro-cloud': (0.435, 0.87),
    'gemma4-26b-moe': (0.06, 0.33),
    'llama-3.3-70b-free': (0.1, 0.32),
    'llama3.3-70b': (0.1, 0.32),
    'llama4-maverick': (0.15, 0.6),
    'local-diffusiongemma-26b': (0.06, 0.33),
    'local-qwen3.5-35b': (0.39, 2.34),
    'mimo-v2-flash-free': (0.1, 0.3),
    'nim-deepseek-v4-pro': (0.435, 0.87),
    'qwen-3.6-plus-free': (0.325, 1.95),
    'qwen3-coder-free': (0.22, 1.8),
}

for _k, _price in OR_COMPARISON_PRICING_EXT.items():
    _m = MODELS.get(_k) or OLLAMA_MODELS.get(_k)
    if _m and float(_m.get("cost_input", 0)) == 0:
        _m["free_runtime"] = True
        _m["cost_input"], _m["cost_output"] = _price


# ── Backfill long-context top-20 (jun 2026) ────────────────────────────────
# Cap de niah a 256K = techo justo de comparación + control de costo/tiempo (la
# grilla niah escala a 800K; sin cap, los modelos de 1M razonarían contextos
# enormes y caros). context_window real para los que estaban en None evita que
# los tests sobre su ventana real den error en vez de saltarse limpio.
_NIAH_CTX_DEFAULTS = {
    "devstral": 131072, "groq-llama-4-scout": 131072, "groq-llama-3.3-70b": 131072,
    "groq-llama-3.1-8b": 131072, "grok-4.1-fast": 2097152,
}
for _k in ("devstral", "groq-llama-4-scout", "groq-llama-3.3-70b", "mistral-small-4",
           "gemini-3.1-flash-lite", "groq-llama-3.1-8b", "hermes-4-70b", "claude-haiku-4.5-sub",
           "grok-4.1-fast", "claude-fable-5-sub", "claude-opus-4.8-sub", "claude-sonnet-4.6-sub",
           "nim-qwen3-next-instruct", "spark-gemma4-12b", "nim-deepseek-v4-flash"):
    _m = MODELS.get(_k)
    if _m:
        if _m.get("context_window") is None:
            _m["context_window"] = _NIAH_CTX_DEFAULTS.get(_k, 131072)
        # cap 256K, pero nunca por encima del contexto real (Haiku=200K → cap a 128K
        # para que el test de 256K se salte limpio en vez de dar "Prompt too long")
        _m["niah_max_context"] = min(262144, _m.get("context_window") or 262144)
