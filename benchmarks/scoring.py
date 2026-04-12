"""
Sistema de puntuacion para benchmarks.
Evalua calidad, velocidad, costo y tool calling.
"""

import json
import re


def score_content_quality(response: str, criteria: dict) -> float:
    """Evalua la calidad del contenido generado (0-10)."""
    score = 0.0

    # Longitud minima
    min_words = criteria.get("min_words", 50)
    word_count = len(response.split())
    if word_count >= min_words:
        score += 2.0
    elif word_count > 0:
        score += 2.0 * (word_count / min_words)

    # Contiene secciones/estructura esperada
    required_sections = criteria.get("required_sections", [])
    if required_sections:
        found = sum(1 for s in required_sections if s.lower() in response.lower())
        score += 3.0 * (found / len(required_sections))

    # Idioma correcto
    expected_lang = criteria.get("language", None)
    if expected_lang == "es":
        spanish_words = ["de", "en", "la", "el", "los", "las", "que", "por", "para", "con"]
        found = sum(1 for w in spanish_words if f" {w} " in response.lower())
        score += 2.0 if found >= 3 else 1.0 if found >= 1 else 0.0
    else:
        score += 2.0  # No language check

    # Formato (usa markdown, listas, etc.)
    has_headers = bool(re.search(r"^#{1,3}\s", response, re.MULTILINE))
    has_lists = bool(re.search(r"^[\-\*\d]+[\.\)]\s", response, re.MULTILINE))
    has_bold = "**" in response
    format_score = sum([has_headers, has_lists, has_bold])
    score += min(format_score, 3.0)

    return min(score, 10.0)


def score_tool_calling(result, expected_tools: list[dict]) -> float:
    """Evalua la precision del tool calling (0-10)."""
    tool_calls = result.metadata.get("tool_calls", [])

    if not expected_tools:
        return 10.0 if not tool_calls else 5.0

    if not tool_calls:
        return 0.0

    score = 0.0
    max_per_tool = 10.0 / len(expected_tools)

    for expected in expected_tools:
        expected_name = expected["name"]
        matching = [tc for tc in tool_calls if tc.get("name") == expected_name]

        if not matching:
            continue

        # Nombre correcto
        score += max_per_tool * 0.4

        # Argumentos correctos
        try:
            actual_args = json.loads(matching[0].get("arguments", "{}"))
            expected_args = expected.get("arguments", {})

            if expected_args:
                correct_keys = sum(
                    1 for k, v in expected_args.items()
                    if k in actual_args and _values_match(actual_args[k], v)
                )
                score += max_per_tool * 0.6 * (correct_keys / len(expected_args))
            else:
                score += max_per_tool * 0.6
        except (json.JSONDecodeError, AttributeError):
            pass

    return min(score, 10.0)


def _values_match(actual, expected) -> bool:
    """Compara valores de forma flexible."""
    if isinstance(expected, str) and isinstance(actual, str):
        return expected.lower() in actual.lower()
    return actual == expected


def score_speed(tokens_per_second: float) -> float:
    """Puntaje de velocidad (0-10). >100 tok/s = 10, <5 tok/s = 1."""
    if tokens_per_second >= 100:
        return 10.0
    elif tokens_per_second >= 50:
        return 8.0
    elif tokens_per_second >= 30:
        return 6.0
    elif tokens_per_second >= 15:
        return 4.0
    elif tokens_per_second >= 5:
        return 2.0
    else:
        return 1.0


def score_latency(first_token_seconds: float) -> float:
    """Puntaje de latencia hasta primer token (0-10). <0.5s = 10, >10s = 1."""
    if first_token_seconds <= 0.5:
        return 10.0
    elif first_token_seconds <= 1.0:
        return 8.0
    elif first_token_seconds <= 2.0:
        return 6.0
    elif first_token_seconds <= 5.0:
        return 4.0
    elif first_token_seconds <= 10.0:
        return 2.0
    else:
        return 1.0


# Precios por millon de tokens (input, output)
PRICING = {
    # OpenAI
    "gpt-4o": (2.50, 10.00),
    "gpt-4o-mini": (0.15, 0.60),
    "o3-mini": (1.10, 4.40),
    # DeepSeek
    "deepseek-chat": (0.14, 0.28),
    "deepseek/deepseek-chat": (0.14, 0.28),
    "deepseek-reasoner": (0.0, 0.0),  # gratis en OpenRouter
    "deepseek/deepseek-reasoner": (0.0, 0.0),
    # Google
    "gemini-2.5-flash": (0.30, 2.50),
    "google/gemini-2.5-flash": (0.30, 2.50),
    "gemini-2.5-pro": (1.25, 10.00),
    # Mistral
    "mistral-medium-latest": (0.40, 2.00),
    "mistral-nemo": (0.02, 0.02),
    "mistralai/mistral-nemo": (0.02, 0.02),
    # Llama (gratis en OpenRouter)
    "meta-llama/llama-3.3-70b": (0.0, 0.0),
    "llama-3.3-70b-versatile": (0.05, 0.08),  # Groq
    # Qwen
    "qwen/qwen-3.5-72b": (1.20, 2.00),
    # Grok
    "grok-2": (2.00, 10.00),
    # Ollama (local = gratis)
    "llama3.3": (0.0, 0.0),
    "qwen3.5": (0.0, 0.0),
    "deepseek-coder-v2": (0.0, 0.0),
}


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Estima el costo en USD de una llamada."""
    prices = PRICING.get(model, (1.0, 3.0))  # default conservador
    input_cost = (input_tokens / 1_000_000) * prices[0]
    output_cost = (output_tokens / 1_000_000) * prices[1]
    return input_cost + output_cost


def compute_final_score(
    quality: float,
    speed: float,
    latency: float,
    tool_calling: float,
    cost_per_call: float,
) -> dict:
    """Calcula el puntaje final ponderado."""
    # Normalizar costo (inverso - menos costo = mejor score)
    if cost_per_call <= 0:
        cost_score = 10.0  # gratis
    elif cost_per_call <= 0.001:
        cost_score = 9.0
    elif cost_per_call <= 0.005:
        cost_score = 7.0
    elif cost_per_call <= 0.01:
        cost_score = 5.0
    elif cost_per_call <= 0.05:
        cost_score = 3.0
    else:
        cost_score = 1.0

    weights = {
        "quality": 0.35,
        "cost": 0.15,
        "speed": 0.05,
        "latency": 0.05,
        "tool_calling": 0.25,
        "availability": 0.15,  # hardcoded por ahora basado en proveedor
    }

    final = (
        quality * weights["quality"]
        + cost_score * weights["cost"]
        + speed * weights["speed"]
        + latency * weights["latency"]
        + tool_calling * weights["tool_calling"]
        + 7.0 * weights["availability"]  # default availability
    )

    return {
        "quality": round(quality, 2),
        "cost_score": round(cost_score, 2),
        "cost_usd": round(cost_per_call, 6),
        "speed": round(speed, 2),
        "latency": round(latency, 2),
        "tool_calling": round(tool_calling, 2),
        "final": round(final, 2),
    }
