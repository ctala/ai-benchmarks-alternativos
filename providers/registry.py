"""
Registro de providers — UN solo lugar donde se decide qué cliente atiende a cada modelo.

POR QUÉ EXISTE
--------------
El 13-jul-2026 escribí un health-check de endpoints que llamaba a una función
(`call_model`) que NO EXISTÍA: había **adivinado** la API del adapter en vez de leerla.
El script parecía correcto y estaba roto de raíz.

La lección no es "leé el adapter". Es que **un chequeo que no usa el mismo camino que el
runner puede mentirte**: puede decir VIVO lo que el runner no logra llamar, o al revés.
Por eso el dispatch vive acá una sola vez, y tanto el runner como el health-check lo
importan. Si el camino cambia, cambia para los dos.
"""
import os

from providers.adapters import (
    ClaudeCodeProvider,
    DiffusionGemmaProvider,
    OpenAIResponsesProvider,
    UnifiedProvider,
)


def _try(fn):
    """Un provider que no está configurado es None, no una excepción."""
    try:
        return fn()
    except (ImportError, AttributeError):
        return None


def build_providers(include_ollama: bool = False) -> dict:
    """Construye los clientes disponibles. Los no configurados quedan en None."""
    from benchmarks.config import OPENROUTER_API_KEY

    P = {"openrouter": UnifiedProvider("openrouter", OPENROUTER_API_KEY, "https://openrouter.ai/api/v1")}

    def _u(name, key_attr, url_attr, default_url=None):
        def go():
            import benchmarks.config as c
            key = getattr(c, key_attr, None)
            url = getattr(c, url_attr, None) or default_url
            return UnifiedProvider(name, key, url) if key and url else None
        return _try(go)

    P["minimax_direct"] = _u("minimax", "MINIMAX_API_KEY", "MINIMAX_BASE_URL")
    P["groq_direct"] = _u("groq", "GROQ_API_KEY", "GROQ_BASE_URL")
    P["nvidia_nim"] = _u("nvidia_nim", "NVIDIA_NIM_API_KEY", "NVIDIA_NIM_BASE_URL")
    P["ollama_cloud"] = _u("ollama_cloud", "OLLAMA_CLOUD_API_KEY", "OLLAMA_CLOUD_BASE_URL", "https://ollama.com/v1")
    P["xiaomi_direct"] = _u("xiaomi", "XIAOMI_API_KEY", "XIAOMI_BASE_URL", "https://token-plan-sgp.xiaomimimo.com/v1")

    def _openai():
        import benchmarks.config as c
        k, u = getattr(c, "OPENAI_API_KEY", None), getattr(c, "OPENAI_BASE_URL", None)
        return (UnifiedProvider("openai", k, u), OpenAIResponsesProvider("openai_responses", k, u)) if k else (None, None)
    P["openai_direct"], P["openai_responses"] = _try(_openai) or (None, None)

    def _nim_local():
        import benchmarks.config as c
        u = getattr(c, "NIM_LOCAL_BASE_URL", None)
        return UnifiedProvider("nim_local", "nim-local-no-auth", u) if u else None
    P["nim_local"] = _try(_nim_local)

    # Anthropic va por SUSCRIPCIÓN (claude -p), nunca por API facturada. Ver CLAUDE.md.
    P["claude_code"] = ClaudeCodeProvider("claude_code")

    P["ollama"] = (
        UnifiedProvider("ollama", "ollama", os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"))
        if include_ollama else None
    )
    return P


class MissingCredential(RuntimeError):
    """El modelo vive en un provider propio y no tenemos la key. NO está muerto."""


def provider_for(cfg: dict, P: dict):
    """Qué cliente atiende a este modelo. Mismo orden de precedencia que el runner.

    Si el modelo declara un provider PROPIO (Groq, Xiaomi, MiniMax…) y no tenemos su
    credencial, esto LEVANTA MissingCredential en vez de caer a OpenRouter.

    Por qué: el `id` de un modelo es específico de su provider. `llama-3.3-70b-versatile`
    es el nombre de Groq; OpenRouter lo llama `meta-llama/llama-3.3-70b-instruct`. Al caer
    a OpenRouter con el ID de Groq, OpenRouter responde "not a valid model ID" — y ese
    error se lee EXACTAMENTE igual que el de un modelo retirado. El 13-jul-2026 eso me
    hizo marcar como muerto a Llama 3.1 8B (Groq), que está perfectamente vivo.
    Una credencial que falta no es un modelo que murió.
    """
    prov = cfg.get("provider")

    # llama_server va PRIMERO: gana al routing is_local→ollama aunque tier sea "local".
    if prov in ("llama_server", "llama_server_think") and cfg.get("base_url"):
        return UnifiedProvider(prov, "no-auth", cfg["base_url"])
    if prov == "diffusion_cli":
        return DiffusionGemmaProvider(
            "diffusion_cli",
            bin_path=cfg["bin_path"], gguf_path=cfg["gguf_path"],
            ngl=cfg.get("ngl", 99), ctx_size=cfg.get("ctx_size", 8192), seed=cfg.get("seed", 42),
        )
    if cfg.get("tier") == "local" and P.get("ollama"):
        return P["ollama"]
    if prov and prov != "openrouter":
        if not P.get(prov):
            raise MissingCredential(f"falta la credencial de «{prov}» — el modelo no está muerto, no lo podemos llamar")
        return P[prov]
    return P["openrouter"]
