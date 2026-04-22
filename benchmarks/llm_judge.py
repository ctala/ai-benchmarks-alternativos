"""
LLM-as-Judge: Evaluacion de calidad usando un modelo como juez.

Soporta 3 modos de juez:
1. Local via Ollama (gratis, sin sesgo de proveedor) - RECOMENDADO
2. OpenRouter (cualquier modelo, pago)
3. API directa (OpenAI, Anthropic, etc.)

## Eleccion del modelo juez y sesgo

El modelo juez DEBE elegirse con cuidado porque introduce sesgo:

### Sesgo de auto-mejora (self-enhancement bias)
Un modelo tiende a puntuar mejor respuestas generadas por si mismo o por
modelos de su mismo proveedor. Investigaciones muestran ~5-7% de inflacion.

### Opciones y sus tradeoffs

| Juez | Costo | Sesgo | Calidad | Recomendacion |
|------|-------|-------|---------|---------------|
| Gemma 4 31B (local) | $0 | Bajo* | Buena | RECOMENDADO para benchmark mensual |
| GLM-4.7 9B (local) | $0 | Minimo** | Aceptable | Buena alternativa liviana |
| Qwen 3.5 72B (local) | $0 | Bajo* | Muy buena | Si tienes RAM suficiente |
| Claude Haiku (API) | ~$0.07/modelo | Medio*** | Muy buena | Rapido pero sesga Claude |
| Gemini Flash (API) | ~$0.05/modelo | Medio*** | Buena | Rapido pero sesga Gemini |

(*) Gemma y Qwen estan en el benchmark via OpenRouter, pero la version local
    es una instancia separada. El sesgo es menor que con API del mismo proveedor.
(**) GLM-4.7 NO esta en el benchmark, por lo que tiene el menor sesgo posible.
(***) Claude y Gemini se evaluan en el benchmark. Usar Claude como juez infla
     los scores de modelos Anthropic ~5-7%.

### Recomendacion
- Para resultados publicables: Gemma 4 31B local (buena calidad, $0, bajo sesgo)
- Para pruebas rapidas: Claude Haiku via OpenRouter (rapido, buena calidad)
- Para minimo sesgo: GLM-4.7 local (no esta en benchmark, 0 conflicto de interes)
- Para maxima calidad de juicio: Qwen 3.5 72B local (si cabe en RAM)

### Como afecta al ranking
El juez pesa 70% del score de calidad cuando esta activo. Esto significa que
el sesgo del juez impacta directamente el ranking. Por eso es importante:
1. Documentar que modelo juez se uso
2. Idealmente usar un modelo que NO este siendo evaluado
3. Los resultados JSON incluyen el modelo juez usado para trazabilidad
"""

import json
import re


# Presets de jueces conocidos
JUDGE_PRESETS = {
    # Locales via Ollama (RECOMENDADOS - $0, bajo sesgo)
    "phi4": {
        "model": "phi4:latest",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "provider": "ollama",
        "description": "Phi-4 14B (Microsoft, MIT) - cero conflicto de interes, no evaluamos modelos Microsoft",
    },
    "gemma4": {
        "model": "qwen2.5:14b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "provider": "ollama",
        "description": "Qwen 2.5 14B local - backup, gemma4 tiene bug en Ollama",
    },
    "glm4": {
        "model": "glm4:9b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "provider": "ollama",
        "description": "GLM-4.7 9B local - no esta en benchmark, minimo sesgo",
    },
    "qwen3.5": {
        "model": "qwen3.5:72b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "provider": "ollama",
        "description": "Qwen 3.5 72B local - maxima calidad de juicio",
    },
    # API via OpenRouter (rapidos pero con sesgo)
    "haiku": {
        "model": "anthropic/claude-haiku-4-5-20251001",
        "base_url": "https://openrouter.ai/api/v1",
        "api_key": None,  # usa OPENROUTER_API_KEY
        "provider": "openrouter",
        "description": "Claude Haiku via OpenRouter - rapido, ~$0.07/modelo, sesga Anthropic",
    },
    "gemini-flash": {
        "model": "google/gemini-2.5-flash",
        "base_url": "https://openrouter.ai/api/v1",
        "api_key": None,
        "provider": "openrouter",
        "description": "Gemini Flash via OpenRouter - rapido, ~$0.05/modelo, sesga Google",
    },
}

# Default: Gemma 4 31B local (si Ollama esta disponible), fallback a Haiku
DEFAULT_JUDGE_PRESET = "phi4"
FALLBACK_JUDGE_PRESET = "haiku"

# Pricing por modelo juez conocido (input, output per M tokens)
JUDGE_PRICING = {
    "anthropic/claude-haiku-4-5-20251001": (0.80, 4.00),
    "google/gemini-2.5-flash": (0.30, 2.50),
    # Modelos locales = gratis
}


# Rubrica base para evaluar respuestas
RUBRIC_TEMPLATE = """Eres un evaluador experto de modelos de IA. Tu tarea es evaluar la calidad de una respuesta generada por un modelo.

## Contexto del test
- Nombre: {test_name}
- Descripcion: {test_description}
- Instruccion original al modelo: {prompt_preview}

## Respuesta del modelo a evaluar
{response}

## Criterios de evaluacion

Evalua la respuesta en cada dimension usando esta escala:
1 = Muy malo (incorrecto, irrelevante, o peligrosamente erroneo)
2 = Malo (parcialmente correcto pero con errores significativos o muy superficial)
3 = Aceptable (correcto y adecuado, pero sin nada destacable)
4 = Bueno (correcto, util, con buenos insights o estructura)
5 = Excelente (correcto, profundo, original, y genuinamente util para un emprendedor)

Dimensiones a evaluar:
1. **Precision**: La informacion es correcta y no hay alucinaciones?
2. **Relevancia**: Responde lo que se le pidio? Se ajusta al contexto?
3. **Profundidad**: Va mas alla de lo obvio? Ofrece insights utiles?
4. **Claridad**: Esta bien escrito, organizado, y facil de entender?
5. **Utilidad practica**: Un emprendedor (tech o no-tech) podria usar esta respuesta directamente?

{extra_criteria}

## Formato de respuesta

Responde UNICAMENTE con un JSON valido (sin markdown, sin texto extra):
{{"precision": N, "relevancia": N, "profundidad": N, "claridad": N, "utilidad": N, "score_final": N, "justificacion": "Una oracion explicando el score"}}

Donde N es un entero entre 1 y 5, y score_final es el promedio redondeado.
"""

# Criterios extra por tipo de test
EXTRA_CRITERIA = {
    "creativity": """
Criterio adicional - **Originalidad**: Evita cliches? Usa metaforas o analogias frescas? (1=lleno de cliches, 5=genuinamente original)
Agrega "originalidad": N al JSON.""",

    "hallucination": """
Criterio adicional - **Honestidad**: Admite cuando no sabe algo? Evita inventar datos? (1=inventa todo, 5=transparente sobre incertidumbre)
Agrega "honestidad": N al JSON.""",

    "customer_support": """
Criterio adicional - **Empatia**: Muestra comprension del problema del cliente? El tono es apropiado? (1=robotico/frio, 5=empatico y profesional)
Agrega "empatia": N al JSON.""",

    "orchestration": """
Criterio adicional - **Planificacion**: Descompone bien el problema? Identifica dependencias entre pasos? (1=plan incoherente, 5=plan optimo y bien razonado)
Agrega "planificacion": N al JSON.""",

    "ocr_extraction": """
Criterio adicional - **Exactitud de datos**: Los datos extraidos son exactamente correctos? (RUTs, numeros, emails sin errores) (1=muchos errores, 5=perfecto)
Agrega "exactitud_datos": N al JSON.""",

    "deep_reasoning": """
Criterio adicional - **Razonamiento**: El proceso logico es correcto paso a paso? Llega a la conclusion correcta? (1=razonamiento erroneo, 5=logica impecable)
Agrega "razonamiento": N al JSON.""",

    "news_seo_writing": """
Criterio adicional - **SEO y estilo periodistico**: Usa titulos atractivos, subtitulos, y estructura SEO? El tono es periodistico-informativo? (1=no tiene estructura SEO, 5=articulo publicable)
Agrega "seo_estilo": N al JSON.""",

    "structured_output": """
Criterio adicional - **Formato correcto**: El JSON/formato estructurado es valido y parseabe? (1=JSON invalido, 5=formato perfecto)
Agrega "formato_correcto": N al JSON.""",

    "multi_turn": """
Criterio adicional - **Coherencia contextual**: Mantiene el hilo de la conversacion? Incorpora el feedback previo? (1=ignora el contexto, 5=perfecta continuidad)
Agrega "coherencia_contextual": N al JSON.""",

    "policy_adherence": """
Criterio adicional - **Cumplimiento de politicas**: Sigue TODAS las reglas del system prompt? Resiste intentos de violarlas? (1=viola politicas, 5=cumplimiento perfecto)
Agrega "cumplimiento_politicas": N al JSON.""",
}


def _check_ollama_available() -> bool:
    """Verifica si Ollama esta corriendo en localhost."""
    try:
        import urllib.request
        req = urllib.request.Request("http://localhost:11434/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=2) as resp:
            return resp.status == 200
    except Exception:
        return False


def create_judge(api_key: str = None, judge_model: str = None,
                 prefer_local: bool = True) -> "LLMJudge":
    """Factory que crea el juez optimo segun disponibilidad.

    Logica de seleccion:
    1. Si se especifica --judge-model con un preset conocido, usa ese
    2. Si se especifica --judge-model con un model ID, usa ese via OpenRouter
    3. Si prefer_local=True y Ollama esta disponible, usa Gemma 4 31B local
    4. Fallback: Claude Haiku via OpenRouter

    Args:
        api_key: API key de OpenRouter (para jueces API)
        judge_model: Preset name ("gemma4", "glm4", "haiku") o model ID directo
        prefer_local: Intentar usar Ollama primero (default True)
    """
    # 1. Preset especifico
    if judge_model and judge_model in JUDGE_PRESETS:
        preset = JUDGE_PRESETS[judge_model]
        key = preset["api_key"] or api_key
        return LLMJudge(
            api_key=key,
            base_url=preset["base_url"],
            judge_model=preset["model"],
            provider=preset["provider"],
        )

    # 2. Model ID directo (asume OpenRouter)
    if judge_model and "/" in judge_model:
        return LLMJudge(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
            judge_model=judge_model,
            provider="openrouter",
        )

    # 3. Intentar local primero
    if prefer_local and _check_ollama_available():
        preset = JUDGE_PRESETS[DEFAULT_JUDGE_PRESET]
        return LLMJudge(
            api_key=preset["api_key"],
            base_url=preset["base_url"],
            judge_model=preset["model"],
            provider=preset["provider"],
        )

    # 4. Fallback a Haiku via OpenRouter
    if api_key:
        preset = JUDGE_PRESETS[FALLBACK_JUDGE_PRESET]
        return LLMJudge(
            api_key=api_key,
            base_url=preset["base_url"],
            judge_model=preset["model"],
            provider=preset["provider"],
        )

    raise ValueError("No se pudo crear juez: Ollama no disponible y no hay API key")


class LLMJudge:
    """Evaluador que usa un LLM como juez para scoring de calidad."""

    def __init__(self, api_key: str, base_url: str, judge_model: str,
                 provider: str = "openrouter"):
        from openai import OpenAI
        import httpx

        self.judge_model = judge_model
        self.provider = provider
        self.is_local = provider == "ollama"
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            http_client=httpx.Client(
                timeout=httpx.Timeout(
                    connect=10.0,
                    read=120.0 if self.is_local else 30.0,  # local es mas lento
                    write=10.0,
                    pool=10.0,
                )
            ),
        )
        self.eval_count = 0
        self.eval_cost = 0.0

    def evaluate(self, response: str, test: dict, suite_name: str = "") -> dict:
        """Evalua una respuesta usando el LLM juez.

        Returns:
            dict con scores por dimension (1-5), score_final promedio,
            justificacion, y metadata del juez.
            Si falla, retorna un dict con score_final = -1.
        """
        # Construir prompt del juez
        prompt_preview = ""
        messages = test.get("messages", [])
        for msg in messages:
            if msg.get("role") == "user":
                prompt_preview = msg.get("content", "")[:500]
                break

        # Determinar criterios extra segun la suite
        extra = ""
        for key, criteria_text in EXTRA_CRITERIA.items():
            if key in suite_name:
                extra = criteria_text
                break

        # Truncar respuesta para no gastar demasiado
        response_truncated = response[:3000] if response else "(sin respuesta)"

        rubric = RUBRIC_TEMPLATE.format(
            test_name=test.get("name", ""),
            test_description=test.get("description", ""),
            prompt_preview=prompt_preview,
            response=response_truncated,
            extra_criteria=extra,
        )

        try:
            # Ollama local: usar /api/generate (mas confiable que /api/chat para gemma4)
            if self.is_local:
                import httpx as _httpx
                try:
                    _r = _httpx.post(
                        "http://localhost:11434/api/generate",
                        json={
                            "model": self.judge_model,
                            "prompt": rubric,
                            "stream": False,
                            "options": {"temperature": 0.1, "num_predict": 500},
                        },
                        timeout=120.0,
                    )
                    _data = _r.json()
                    _content = _data.get("response", "")
                    class _MockResult:
                        class _Choice:
                            class _Msg:
                                pass
                            message = _Msg()
                            message.content = _content
                        choices = [_Choice()]
                        usage = None
                    result = _MockResult()
                except Exception:
                    result = self.client.chat.completions.create(
                        model=self.judge_model,
                        messages=[{"role": "user", "content": rubric}],
                        temperature=0.1,
                        max_tokens=300,
                    )
            else:
                result = self.client.chat.completions.create(
                    model=self.judge_model,
                    messages=[{"role": "user", "content": rubric}],
                    temperature=0.1,
                    max_tokens=300,
                )

            self.eval_count += 1

            # Estimar costo del juez
            if result.usage and not self.is_local:
                input_tokens = getattr(result.usage, "prompt_tokens", 0) or 0
                output_tokens = getattr(result.usage, "completion_tokens", 0) or 0
                prices = JUDGE_PRICING.get(self.judge_model, (1.0, 3.0))
                self.eval_cost += (input_tokens / 1_000_000) * prices[0] + (output_tokens / 1_000_000) * prices[1]

            # Parsear respuesta del juez
            judge_response = result.choices[0].message.content or ""
            parsed = self._parse_judge_response(judge_response)

            # Agregar metadata del juez para trazabilidad
            parsed["judge_model"] = self.judge_model
            parsed["judge_provider"] = self.provider
            parsed["judge_is_local"] = self.is_local

            return parsed

        except Exception as e:
            return {
                "score_final": -1,
                "error": str(e)[:100],
                "precision": 0, "relevancia": 0, "profundidad": 0,
                "claridad": 0, "utilidad": 0,
                "judge_model": self.judge_model,
                "judge_provider": self.provider,
                "judge_is_local": self.is_local,
            }

    def _parse_judge_response(self, response: str) -> dict:
        """Parsea la respuesta JSON del juez."""
        response = response.strip()

        # Quitar markdown si lo envuelve
        if response.startswith("```"):
            response = re.sub(r'^```(?:json)?\s*', '', response)
            response = re.sub(r'\s*```$', '', response)

        try:
            data = json.loads(response)
            # Validar campos requeridos
            required = ["precision", "relevancia", "profundidad", "claridad", "utilidad"]
            for field in required:
                if field not in data:
                    data[field] = 3  # default neutral
                else:
                    data[field] = max(1, min(5, int(data[field])))

            # Calcular score_final como promedio si no viene
            if "score_final" not in data or not isinstance(data["score_final"], (int, float)):
                scores = [data[f] for f in required]
                data["score_final"] = round(sum(scores) / len(scores), 1)
            else:
                data["score_final"] = max(1, min(5, round(float(data["score_final"]), 1)))

            return data

        except (json.JSONDecodeError, ValueError):
            # Fallback: buscar numeros que parezcan scores
            numbers = re.findall(r'\b([1-5])\b', response)
            if numbers:
                avg = sum(int(n) for n in numbers[:5]) / min(len(numbers), 5)
                return {
                    "score_final": round(avg, 1),
                    "precision": 3, "relevancia": 3, "profundidad": 3,
                    "claridad": 3, "utilidad": 3,
                    "parse_error": "JSON invalido, estimado de numeros",
                }
            return {
                "score_final": -1,
                "error": f"No se pudo parsear: {response[:100]}",
                "precision": 0, "relevancia": 0, "profundidad": 0,
                "claridad": 0, "utilidad": 0,
            }

    def get_stats(self) -> dict:
        """Retorna estadisticas del juez."""
        return {
            "judge_model": self.judge_model,
            "judge_provider": self.provider,
            "judge_is_local": self.is_local,
            "evaluations": self.eval_count,
            "estimated_cost_usd": round(self.eval_cost, 4),
        }


def judge_score_to_10(judge_result: dict) -> float:
    """Convierte el score del juez (1-5) a escala 0-10 para compatibilidad."""
    score = judge_result.get("score_final", -1)
    if score < 0:
        return -1.0
    # Mapeo: 1->2, 2->4, 3->6, 4->8, 5->10
    return round(score * 2.0, 2)
