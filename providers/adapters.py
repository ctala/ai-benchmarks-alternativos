"""
Adaptador unificado para todos los proveedores usando la API compatible con OpenAI.
La mayoria de proveedores (OpenRouter, DeepSeek, Groq, Mistral, xAI, Ollama)
soportan el formato de API de OpenAI, lo que simplifica enormemente la integracion.

Manejo robusto de timeouts:
- Timeout de conexion: 10 segundos
- Timeout total por request: configurable (default 60s)
- Si un modelo no responde, se marca como error y se sigue al siguiente
"""

import signal
import time
from dataclasses import dataclass, field
from openai import OpenAI
import httpx


@dataclass
class BenchmarkResult:
    provider: str
    model: str
    test_name: str
    prompt: str
    response: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    latency_first_token: float = 0.0
    latency_total: float = 0.0
    tokens_per_second: float = 0.0
    tool_calls_made: int = 0
    tool_calls_correct: int = 0
    success: bool = False
    error: str = ""
    score: float = 0.0
    metadata: dict = field(default_factory=dict)


class TimeoutError(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TimeoutError("Request excedio el tiempo limite")


# =============================================================================
# Estándares del benchmark para thinking models
# Editables si tu hardware/budget difiere — todos los lotes usan estos valores.
# =============================================================================

# Modelos que consumen tokens internos en reasoning (su "thinking" se factura
# como completion_tokens aunque no aparezca en la respuesta visible).
THINKING_MODELS = (
    "gpt-5", "o3", "o1",         # OpenAI thinking
    "glm-5", "GLM-5",            # Zhipu agentic
    "kimi-k2.6", "Kimi",         # Moonshot K2.6+
    "nemotron", "Nemotron",      # NVIDIA Nemotron 3+
)

# Modelos que sólo aceptan temperature=1.0 (rechazan otros con error 400).
# El adapter omite el parámetro y deja que la API use su default.
FIXED_TEMP_MODELS = ("gpt-5.5", "gpt-5-pro", "gpt-5.5-pro", "o1", "o3")

# Multiplicador de max_tokens para thinking models. Sin esto, agotan el budget
# en reasoning interno y devuelven content="" (descubierto abril 2026 con 165
# runs vacíos en Kimi K2.6/GPT-5.5/GLM-5.1/Nemotron).
THINKING_TOKEN_MULTIPLIER = 4
# Mínimo absoluto para thinking models, aunque el max_tokens base sea bajo.
THINKING_MIN_TOKENS = 8192

# Tiempo de espera del cliente HTTP. Subido de 60s a 240s para que thinking
# models con razonamiento extenso (workshop_outline, business_validation, etc)
# puedan terminar. 60s causaba timeouts a 181s (3 retries × 60s) en GPT-5.5.
HTTP_READ_TIMEOUT_S = 240.0


class UnifiedProvider:
    """Adaptador unificado que funciona con cualquier API compatible OpenAI."""

    def __init__(self, provider_name: str, api_key: str, base_url: str):
        self.provider_name = provider_name
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            http_client=httpx.Client(
                timeout=httpx.Timeout(
                    connect=10.0, read=HTTP_READ_TIMEOUT_S, write=10.0, pool=10.0
                )
            ),
        )

    def chat(
        self,
        model: str,
        messages: list[dict],
        tools: list[dict] | None = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        timeout: int = 90,
    ) -> BenchmarkResult:
        """
        Llama al modelo SIN streaming (mas confiable para benchmarks).
        Timeout real via signal alarm como respaldo.
        """
        result = BenchmarkResult(
            provider=self.provider_name,
            model=model,
            test_name="",
            prompt=messages[-1].get("content", "")[:200],
        )

        # Configurar timeout via signal (Unix only)
        old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(timeout)

        start = time.perf_counter()
        try:
            # Detectar thinking models y aplicar el estándar definido al inicio del módulo
            is_thinking = any(model.startswith(p) or p in model for p in THINKING_MODELS)
            if is_thinking:
                token_param = "max_completion_tokens"
                effective_max = max(max_tokens * THINKING_TOKEN_MULTIPLIER, THINKING_MIN_TOKENS)
            else:
                token_param = "max_tokens"
                effective_max = max_tokens

            kwargs = {
                "model": model,
                "messages": messages,
                token_param: effective_max,
            }
            # GPT-5.5+ y gpt-5-pro sólo aceptan temperature=1 (default). Omitir.
            if not any(p in model.lower() for p in FIXED_TEMP_MODELS):
                kwargs["temperature"] = temperature
            if tools:
                kwargs["tools"] = tools
                kwargs["tool_choice"] = "auto"

            response = self.client.chat.completions.create(**kwargs)
            end = time.perf_counter()

            # Cancelar alarm
            signal.alarm(0)

            choice = response.choices[0]
            result.response = choice.message.content or ""
            result.latency_total = end - start
            result.latency_first_token = result.latency_total  # sin streaming = mismo
            result.success = True

            if response.usage:
                result.input_tokens = getattr(response.usage, "prompt_tokens", 0) or 0
                result.output_tokens = getattr(response.usage, "completion_tokens", 0) or 0

            if choice.message.tool_calls:
                result.tool_calls_made = len(choice.message.tool_calls)
                result.metadata["tool_calls"] = [
                    {"name": tc.function.name, "arguments": tc.function.arguments}
                    for tc in choice.message.tool_calls
                ]

            if result.output_tokens > 0 and result.latency_total > 0:
                result.tokens_per_second = result.output_tokens / result.latency_total

        except TimeoutError:
            end = time.perf_counter()
            result.latency_total = end - start
            result.error = f"TIMEOUT: No respondio en {timeout}s"
            result.success = False

        except Exception as e:
            end = time.perf_counter()
            result.latency_total = end - start
            error_msg = str(e)
            # Acortar mensajes de error muy largos
            if len(error_msg) > 200:
                error_msg = error_msg[:200] + "..."
            result.error = error_msg
            result.success = False

        finally:
            # Siempre restaurar el handler y cancelar alarm
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)

        return result
