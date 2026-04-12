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


class UnifiedProvider:
    """Adaptador unificado que funciona con cualquier API compatible OpenAI."""

    def __init__(self, provider_name: str, api_key: str, base_url: str):
        self.provider_name = provider_name
        # httpx timeout: 10s connect, 60s total read
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            http_client=httpx.Client(
                timeout=httpx.Timeout(connect=10.0, read=60.0, write=10.0, pool=10.0)
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
            kwargs = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
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
