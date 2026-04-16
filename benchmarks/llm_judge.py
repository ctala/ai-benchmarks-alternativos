"""
LLM-as-Judge: Evaluacion de calidad usando un modelo como juez.

Usa Claude Haiku 4.5 via OpenRouter como juez por defecto.
El juez evalua la respuesta con una rubrica estructurada en espanol,
puntuando de 1 a 5 en multiples dimensiones.

Costo estimado: ~$0.001 por evaluacion (~$0.07 por modelo con 69 tests).
"""

import json
import re
from openai import OpenAI
import httpx


# Modelo juez por defecto - Claude Haiku via OpenRouter (barato y bueno en rubrics)
DEFAULT_JUDGE_MODEL = "anthropic/claude-haiku-4-5-20251001"
DEFAULT_JUDGE_BASE_URL = "https://openrouter.ai/api/v1"


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
}


class LLMJudge:
    """Evaluador que usa un LLM como juez para scoring de calidad."""

    def __init__(self, api_key: str, base_url: str = DEFAULT_JUDGE_BASE_URL,
                 judge_model: str = DEFAULT_JUDGE_MODEL):
        self.judge_model = judge_model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            http_client=httpx.Client(
                timeout=httpx.Timeout(connect=10.0, read=30.0, write=10.0, pool=10.0)
            ),
        )
        self.eval_count = 0
        self.eval_cost = 0.0

    def evaluate(self, response: str, test: dict, suite_name: str = "") -> dict:
        """Evalua una respuesta usando el LLM juez.

        Returns:
            dict con scores por dimension (1-5) y score_final promedio.
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
            result = self.client.chat.completions.create(
                model=self.judge_model,
                messages=[{"role": "user", "content": rubric}],
                temperature=0.1,  # Bajo para consistencia
                max_tokens=300,
            )

            self.eval_count += 1

            # Estimar costo del juez
            if result.usage:
                input_tokens = getattr(result.usage, "prompt_tokens", 0) or 0
                output_tokens = getattr(result.usage, "completion_tokens", 0) or 0
                # Haiku pricing: $0.80/$4.00 per M via OpenRouter
                self.eval_cost += (input_tokens / 1_000_000) * 0.80 + (output_tokens / 1_000_000) * 4.00

            # Parsear respuesta del juez
            judge_response = result.choices[0].message.content or ""
            return self._parse_judge_response(judge_response)

        except Exception as e:
            return {
                "score_final": -1,
                "error": str(e)[:100],
                "precision": 0, "relevancia": 0, "profundidad": 0,
                "claridad": 0, "utilidad": 0,
            }

    def _parse_judge_response(self, response: str) -> dict:
        """Parsea la respuesta JSON del juez."""
        # Intentar extraer JSON del response
        response = response.strip()

        # Quitar markdown si lo envuelve
        if response.startswith("```"):
            response = re.sub(r'^```(?:json)?\s*', '', response)
            response = re.sub(r'\s*```$', '', response)

        try:
            data = json.loads(response)
            # Validar que tiene los campos requeridos
            required = ["precision", "relevancia", "profundidad", "claridad", "utilidad"]
            for field in required:
                if field not in data:
                    data[field] = 3  # default neutral
                else:
                    # Asegurar que es int entre 1-5
                    data[field] = max(1, min(5, int(data[field])))

            # Calcular score_final como promedio si no viene
            if "score_final" not in data or not isinstance(data["score_final"], (int, float)):
                scores = [data[f] for f in required]
                data["score_final"] = round(sum(scores) / len(scores), 1)
            else:
                data["score_final"] = max(1, min(5, round(float(data["score_final"]), 1)))

            return data

        except (json.JSONDecodeError, ValueError):
            # Fallback: buscar un numero que parezca el score
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
            "evaluations": self.eval_count,
            "estimated_cost_usd": round(self.eval_cost, 4),
        }


def judge_score_to_10(judge_result: dict) -> float:
    """Convierte el score del juez (1-5) a escala 0-10 para compatibilidad."""
    score = judge_result.get("score_final", -1)
    if score < 0:
        return -1.0  # Error, no evaluar
    # Mapeo: 1->2, 2->4, 3->6, 4->8, 5->10
    return round(score * 2.0, 2)
