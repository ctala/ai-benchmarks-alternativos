"""
Sistema de puntuacion para benchmarks.
Evalua calidad, velocidad, costo y tool calling.

v2: Separa formato de sustancia para evitar sesgo hacia modelos
que solo formatean bien. Valida expected_answer y penaliza cliches.
"""

import json
import re
import unicodedata


def _normalize_text(text: str) -> str:
    """Normaliza texto removiendo acentos para comparaciones flexibles."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()


def score_content_quality(response: str, criteria: dict) -> float:
    """Evalua la calidad del contenido generado (0-10).

    Distribucion de puntos:
    - Longitud minima: 2 pts (cumple requisito basico)
    - Secciones requeridas: 4 pts (contenido relevante - peso principal)
    - Idioma correcto: 2 pts
    - Formato: 2 pts (reducido de 3 para no premiar formato sobre contenido)
    """
    score = 0.0

    # Longitud minima (2 pts)
    min_words = criteria.get("min_words", 50)
    word_count = len(response.split())
    if word_count >= min_words:
        score += 2.0
    elif word_count > 0:
        score += 2.0 * (word_count / min_words)

    # Contiene secciones/estructura esperada (4 pts - subido de 3)
    required_sections = criteria.get("required_sections", [])
    if required_sections:
        response_normalized = _normalize_text(response)
        found = sum(
            1 for s in required_sections
            if _normalize_text(s) in response_normalized
        )
        score += 4.0 * (found / len(required_sections))

    # Idioma correcto (2 pts)
    expected_lang = criteria.get("language", None)
    if expected_lang == "es":
        spanish_words = ["de", "en", "la", "el", "los", "las", "que", "por", "para", "con"]
        found = sum(1 for w in spanish_words if f" {w} " in response.lower())
        score += 2.0 if found >= 3 else 1.0 if found >= 1 else 0.0
        # Penalizar caracteres chinos en respuestas en espanol
        chinese_chars = sum(1 for c in response if '\u4e00' <= c <= '\u9fff')
        if chinese_chars > 5:
            score -= min(2.0, chinese_chars * 0.1)  # hasta -2 pts por chino
    else:
        score += 2.0  # No language check

    # Formato (2 pts - reducido de 3)
    has_headers = bool(re.search(r"^#{1,3}\s", response, re.MULTILINE))
    has_lists = bool(re.search(r"^[\-\*\d]+[\.\)]\s", response, re.MULTILINE))
    has_bold = "**" in response
    format_score = sum([has_headers, has_lists, has_bold])
    score += min(format_score * 0.67, 2.0)

    return min(score, 10.0)


def score_expected_answer(response: str, expected_answer: dict) -> float:
    """Evalua respuestas contra criterios especificos del test (0-10).

    Soporta tipos:
    - exact_string: coincidencia exacta de strings
    - multi_string_check: multiples strings que deben estar presentes
    - numeric: valores numericos con tolerancia
    - sequence: secuencia ordenada de elementos
    - reasoning: key insights que deben estar presentes
    - hallucination_check: detectar si el modelo inventa datos
    - honesty_check: detectar si el modelo admite incertidumbre
    - creativity_check: penalizar cliches y contenido generico
    - depth_check: penalizar respuestas superficiales
    - range: valor dentro de un rango razonable
    """
    answer_type = expected_answer.get("type", "")

    if answer_type == "exact_string":
        return _score_exact_string(response, expected_answer)
    elif answer_type == "multi_string_check":
        return _score_multi_string(response, expected_answer)
    elif answer_type == "numeric":
        return _score_numeric(response, expected_answer)
    elif answer_type == "sequence":
        return _score_sequence(response, expected_answer)
    elif answer_type == "reasoning":
        return _score_reasoning(response, expected_answer)
    elif answer_type == "hallucination_check":
        return _score_hallucination(response, expected_answer)
    elif answer_type == "honesty_check":
        return _score_honesty(response, expected_answer)
    elif answer_type == "creativity_check":
        return _score_creativity(response, expected_answer)
    elif answer_type == "depth_check":
        return _score_depth(response, expected_answer)
    elif answer_type == "range":
        return _score_range(response, expected_answer)
    else:
        return 5.0  # tipo desconocido, score neutral


def _score_exact_string(response: str, expected: dict) -> float:
    """Evalua precision de copia de strings (0-10)."""
    target = expected["expected"]
    cleaned = response.strip().strip('"').strip("'").strip("`")
    if cleaned == target:
        return 10.0
    matches = sum(1 for a, b in zip(cleaned, target) if a == b)
    max_len = max(len(cleaned), len(target))
    if max_len == 0:
        return 0.0
    ratio = matches / max_len
    if ratio >= 0.99:
        return 7.0
    elif ratio >= 0.95:
        return 4.0
    elif ratio >= 0.90:
        return 2.0
    return 1.0


def _score_multi_string(response: str, expected: dict) -> float:
    """Evalua que multiples strings exactos esten presentes (0-10)."""
    must_contain = expected.get("must_contain_exact", [])
    if not must_contain:
        return 5.0
    found = sum(1 for s in must_contain if s in response)
    return 10.0 * (found / len(must_contain))


def _score_numeric(response: str, expected: dict) -> float:
    """Evalua respuestas numericas con tolerancia (0-10)."""
    values = expected.get("values", {})
    tolerance = expected.get("tolerance", 2)
    if not values:
        return 5.0

    score = 0.0
    max_per_value = 10.0 / len(values)

    for key, expected_val in values.items():
        # Buscar el numero en la respuesta
        try:
            expected_num = float(str(expected_val).replace(":", ".").replace(",", "."))
        except ValueError:
            # Para valores como "8:42" buscar como string
            if str(expected_val) in response:
                score += max_per_value
            continue

        # Buscar numeros en la respuesta cercanos al esperado
        numbers = re.findall(r'[\d]+[.,]?\d*', response)
        for num_str in numbers:
            try:
                num = float(num_str.replace(",", "."))
                if abs(num - expected_num) <= tolerance:
                    score += max_per_value
                    break
            except ValueError:
                continue

    return min(score, 10.0)


def _score_sequence(response: str, expected: dict) -> float:
    """Evalua si una secuencia ordenada aparece en la respuesta (0-10)."""
    values = expected.get("values", [])
    if not values:
        return 5.0

    response_lower = response.lower()
    positions = []
    for v in values:
        pos = response_lower.find(v.lower())
        positions.append(pos)

    # Verificar que todos estan presentes
    all_found = all(p >= 0 for p in positions)
    if not all_found:
        found_count = sum(1 for p in positions if p >= 0)
        return 3.0 * (found_count / len(values))

    # Verificar que estan en orden
    valid_positions = [p for p in positions if p >= 0]
    in_order = all(valid_positions[i] < valid_positions[i + 1] for i in range(len(valid_positions) - 1))

    if in_order:
        return 10.0
    else:
        return 5.0  # Todos presentes pero en orden incorrecto


def _score_reasoning(response: str, expected: dict) -> float:
    """Evalua si los insights clave estan presentes (0-10)."""
    key_insights = expected.get("key_insights", [])
    if not key_insights:
        return 5.0

    response_normalized = _normalize_text(response)
    found = 0
    for insight in key_insights:
        # Buscar cada insight de forma flexible (palabras clave del insight)
        insight_words = _normalize_text(insight).split()
        # Considerar encontrado si al menos 60% de las palabras clave estan presentes
        key_words = [w for w in insight_words if len(w) > 3]  # ignorar palabras cortas
        if not key_words:
            key_words = insight_words
        matches = sum(1 for w in key_words if w in response_normalized)
        if matches >= max(1, len(key_words) * 0.6):
            found += 1

    return 10.0 * (found / len(key_insights))


def _score_hallucination(response: str, expected: dict) -> float:
    """Evalua si el modelo evita alucinar en preguntas trampa (0-10)."""
    score = 0.0

    # Verificar respuestas reales
    real_answers = expected.get("real_answers", {})
    if real_answers:
        per_answer = 5.0 / len(real_answers)
        for key, answer in real_answers.items():
            if str(answer).lower() in response.lower():
                score += per_answer

    # Verificar que dice "no se" en preguntas trampa
    should_unknown = expected.get("should_say_unknown", [])
    fake_entities = expected.get("fake_entities", [])
    if should_unknown:
        uncertainty_phrases = [
            "no tengo certeza", "no estoy seguro", "no se", "no tengo informacion",
            "no puedo confirmar", "no existe", "no conozco", "no he encontrado",
            "baja", "desconozco", "no dispongo", "ficticia", "inventad",
        ]
        per_unknown = 5.0 / len(should_unknown)
        response_lower = response.lower()
        for idx in should_unknown:
            # Buscar si en la zona de esa pregunta hay incertidumbre
            has_uncertainty = any(phrase in response_lower for phrase in uncertainty_phrases)
            # Verificar que no invento datos sobre entidades falsas
            if fake_entities:
                invented = any(
                    entity.lower() in response_lower and
                    not any(phrase in response_lower for phrase in ["no existe", "ficticia", "no conozco", "no tengo"])
                    for entity in fake_entities
                )
                if not invented and has_uncertainty:
                    score += per_unknown
                elif has_uncertainty:
                    score += per_unknown * 0.5
            elif has_uncertainty:
                score += per_unknown

    return min(score, 10.0)


def _score_honesty(response: str, expected: dict) -> float:
    """Evalua si el modelo es honesto sobre su incertidumbre (0-10)."""
    response_lower = response.lower()
    honesty_indicators = [
        "no estoy seguro", "certeza baja", "certeza media", "especulando",
        "de memoria", "no puedo verificar", "podria no ser exacto",
        "no tengo acceso", "aproximad", "puede variar", "no confirmar",
    ]
    found = sum(1 for phrase in honesty_indicators if phrase in response_lower)

    if found >= 4:
        return 10.0
    elif found >= 3:
        return 8.0
    elif found >= 2:
        return 6.0
    elif found >= 1:
        return 4.0
    return 2.0


def _score_creativity(response: str, expected: dict) -> float:
    """Evalua creatividad penalizando cliches (0-10)."""
    score = 8.0  # Base alta, se restan puntos por cliches

    # Penalizar cliches
    cliches = expected.get("penalize_cliches", [])
    response_lower = response.lower()
    cliche_count = sum(1 for c in cliches if c.lower() in response_lower)

    if cliche_count >= 5:
        score -= 5.0
    elif cliche_count >= 3:
        score -= 3.0
    elif cliche_count >= 1:
        score -= 1.5

    # Verificar cantidad minima de items
    min_hooks = expected.get("min_hooks", 0)
    min_analogies = expected.get("min_analogies", 0)
    target_count = min_hooks or min_analogies
    if target_count > 0:
        # Contar items numerados o con bullet points
        items = re.findall(r'(?:^|\n)\s*(?:\d+[\.\):]|[\-\*])\s+\S', response)
        if len(items) >= target_count:
            score += 1.0
        elif len(items) > 0:
            score += 0.5

    # Verificar conteo de palabras si es storytelling
    word_target = expected.get("word_count_target", 0)
    if word_target > 0:
        tolerance = expected.get("word_count_tolerance", 15)
        word_count = len(response.split())
        diff = abs(word_count - word_target)
        if diff <= tolerance:
            score += 1.0
        elif diff <= tolerance * 2:
            score += 0.5

    return max(min(score, 10.0), 1.0)


def _score_depth(response: str, expected: dict) -> float:
    """Evalua profundidad penalizando respuestas genericas (0-10)."""
    score = 8.0

    generic_phrases = expected.get("penalize_generic", [])
    response_lower = response.lower()
    generic_count = sum(1 for g in generic_phrases if g.lower() in response_lower)

    if generic_count >= 4:
        score -= 4.0
    elif generic_count >= 2:
        score -= 2.0
    elif generic_count >= 1:
        score -= 1.0

    # Bonus por numeros concretos (senial de profundidad)
    numbers = re.findall(r'\d+[%$]|\$[\d,.]+|[\d,.]+%', response)
    if len(numbers) >= 3:
        score += 1.5
    elif len(numbers) >= 1:
        score += 0.5

    # Bonus por mencion de riesgos o contrarian views
    if any(w in response_lower for w in ["riesgo", "peligro", "cuidado", "contrario", "sin embargo", "aunque"]):
        score += 0.5

    return max(min(score, 10.0), 1.0)


def _score_range(response: str, expected: dict) -> float:
    """Evalua si un numero esta dentro de un rango razonable (0-10)."""
    reasonable_range = expected.get("reasonable_range", [0, 0])
    must_mention = expected.get("must_mention", [])

    score = 0.0

    # Verificar que menciona los conceptos clave (5 pts)
    if must_mention:
        response_normalized = _normalize_text(response)
        found = sum(1 for m in must_mention if _normalize_text(m) in response_normalized)
        score += 5.0 * (found / len(must_mention))

    # Verificar que da un numero en el rango (5 pts)
    numbers = re.findall(r'[\d,.]+', response)
    in_range = False
    for num_str in numbers:
        try:
            num = float(num_str.replace(",", ""))
            if reasonable_range[0] <= num <= reasonable_range[1]:
                in_range = True
                break
        except ValueError:
            continue

    if in_range:
        score += 5.0

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
    # OpenAI directo
    "gpt-4.1": (2.00, 8.00),
    "gpt-4.1-mini": (0.40, 1.60),
    "gpt-5.4": (2.50, 10.00),
    "gpt-5.4-mini": (0.50, 1.50),
    "gpt-5.5": (5.00, 30.00),
    "gpt-5.5-pro": (30.00, 180.00),
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
    # NVIDIA Nemotron
    "nvidia/nemotron-3-nano-30b-a3b": (0.05, 0.20),
    "nvidia/nemotron-3-super-120b-a12b": (0.10, 0.50),
    # Mistral (nuevos Abril 2026)
    "mistralai/mistral-small-2603": (0.15, 0.60),
    "mistralai/devstral-small": (0.10, 0.30),
    "mistralai/devstral-medium": (0.40, 2.00),
    "mistralai/devstral-2512": (0.40, 2.00),
    # xAI Grok
    "x-ai/grok-4.1-fast": (0.20, 0.50),
    "x-ai/grok-4.20": (2.00, 6.00),
    # Google Gemini (nuevos Abril 2026)
    "google/gemini-3.1-flash-lite-preview": (0.25, 1.50),
    "google/gemini-3.1-pro-preview": (2.00, 12.00),
    # Zhipu GLM
    "z-ai/glm-5.1": (0.95, 3.15),
    # Xiaomi MiMo
    "xiaomi/mimo-v2-flash:free": (0.0, 0.0),
    "xiaomi/mimo-v2-flash": (0.09, 0.29),
    "xiaomi/mimo-v2-omni": (0.40, 2.00),
    "xiaomi/mimo-v2-pro": (1.00, 3.00),
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
