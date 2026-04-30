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
    "gpt-5", "o3", "o1",                    # OpenAI thinking
    "glm-5", "GLM-5",                       # Zhipu agentic
    "kimi-k2.6", "Kimi",                    # Moonshot K2.6+
    "nemotron", "Nemotron",                 # NVIDIA Nemotron 3+
    "gemini-2.5-pro", "gemini-3-pro",       # Google Pro tier (reasoning interno)
    "deepseek-v4", "deepseek-r",            # DeepSeek V4+ (R1, V4 Pro, V4 Flash) — descubierto abril 27 con 30/91 NoneType en V4 Pro
    "gemma4", "gemma-4",                    # Gemma 4 — descubierto abril 28 en Ollama DGX: expone "reasoning" field separado del "content"
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

# Tiempo de espera del cliente HTTP. Subido a 360s tras detectar timeouts
# residuales en DeepSeek V4 Pro (abril 27, 2026). Original 60s → 240s →
# 360s. Algunos thinking models con prompts largos (workshop_outline,
# perplexity_research) razonan >240s y timean.
HTTP_READ_TIMEOUT_S = 360.0


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
        force_reasoning: bool = False,
    ) -> BenchmarkResult:
        """
        Llama al modelo SIN streaming (mas confiable para benchmarks).
        Timeout real via signal alarm como respaldo.

        force_reasoning: para modelos hybrid (Hermes 4, Kimi K2.5, Kimi K2.6,
        Qwen3-Next instruct con thinking opt-in) que NO activan reasoning por
        default. Inyecta `reasoning: {effort: "high"}` + `include_reasoning: true`
        via extra_body. Aplica el mismo tratamiento de THINKING_MODELS
        (max_tokens × 4, min 8192) para que el modelo tenga budget suficiente.
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
            # Detectar thinking models y aplicar el estándar definido al inicio del módulo.
            # `force_reasoning=True` (config flag) trata al modelo como thinking aunque
            # no esté en la tupla — para modelos hybrid (Hermes 4, Kimi K2.5) que solo
            # activan reasoning cuando se les pasa el parámetro explícito.
            is_thinking = force_reasoning or any(
                model.startswith(p) or p in model for p in THINKING_MODELS
            )
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

            # Ollama (local o cloud) acepta `keep_alive` como extension del body.
            # Mantiene el modelo cargado en VRAM 30 min entre requests durante el
            # benchmark (91 tests por modelo) — evita cold start repetido. Default
            # Ollama es 5min, queda corto si el run es lento.
            extra_body = {}
            if "ollama" in self.provider_name.lower():
                extra_body["keep_alive"] = "30m"
            # Hybrid reasoning models (Hermes 4 70B/405B, Kimi K2.5/K2.6,
            # Qwen3-Next 80B Instruct con thinking opt-in): activar reasoning
            # explícitamente vía OpenRouter. effort="high" usa ~80% del max_tokens
            # para razonar, dejando ~20% para la respuesta visible — coherente con
            # nuestro multiplier 4× y min 8192.
            if force_reasoning:
                extra_body["reasoning"] = {"effort": "high"}
                extra_body["include_reasoning"] = True

            if extra_body:
                response = self.client.chat.completions.create(**kwargs, extra_body=extra_body)
            else:
                response = self.client.chat.completions.create(**kwargs)
            end = time.perf_counter()

            # Cancelar alarm
            signal.alarm(0)

            # Guard contra responses malformadas — algunos providers devuelven
            # choices=None o choices=[] bajo errores internos en lugar de raise.
            # Descubierto abril 27 con DeepSeek V4 Pro: 30/91 runs con
            # "'NoneType' object is not subscriptable" antes del fix.
            if not response.choices:
                result.success = False
                result.error = "Response sin choices (provider devolvio respuesta vacia)"
                return result

            choice = response.choices[0]
            if choice.message is None:
                result.success = False
                result.error = "Choice sin message (provider devolvio choice malformada)"
                return result

            content = choice.message.content or ""

            # Algunos providers (Ollama con Gemma 4, DeepSeek V4 Pro via NIM, otros
            # thinking models) exponen el razonamiento interno en un campo separado
            # `reasoning` o `thinking`. Si content esta vacio pero hay reasoning,
            # usar reasoning como fallback para no perder la respuesta. Capturar
            # ambos en metadata para auditoria.
            reasoning = getattr(choice.message, "reasoning", None) or getattr(choice.message, "thinking", None)
            if reasoning:
                result.metadata["reasoning"] = reasoning[:5000]  # cap 5K chars
                if not content.strip():
                    # Fallback: usar reasoning como respuesta (caso Gemma 4 thinking
                    # con max_tokens insuficiente). Mejor algo que nada.
                    content = reasoning
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
                # Si content es None pero hay tool_calls, serializarlas en el response
                # para que el MD/preview no quede vacío. Mantiene auditabilidad.
                if not content:
                    tc_lines = [
                        f"[tool_call] {tc.function.name}({tc.function.arguments})"
                        for tc in choice.message.tool_calls
                    ]
                    content = "\n".join(tc_lines)

            result.response = content

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


class OpenAIResponsesProvider:
    """
    Adaptador para el endpoint /v1/responses de OpenAI (Responses API).
    Usado por modelos pro/o1-pro que NO funcionan en /v1/chat/completions:
    - gpt-5.5-pro
    - gpt-5-pro
    - o1-pro

    Diferencias vs UnifiedProvider:
    - Usa client.responses.create() en lugar de chat.completions
    - Mapea messages → instructions (system) + input (user concatenado)
    - max_tokens → max_output_tokens
    - Lectura: response.output_text directo (sin choices)
    - Usage: input_tokens/output_tokens (no prompt_tokens/completion_tokens)
    """

    def __init__(self, provider_name: str, api_key: str, base_url: str = "https://api.openai.com/v1"):
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

    @staticmethod
    def _messages_to_input(messages: list[dict]) -> tuple[str | None, str]:
        """Separa messages en instructions (system) + input (resto concatenado)."""
        instructions = None
        input_parts = []
        for m in messages:
            role = m.get("role", "user")
            content = m.get("content", "")
            if role == "system":
                instructions = (instructions + "\n\n" + content) if instructions else content
            elif role == "user":
                input_parts.append(content)
            elif role == "assistant":
                # Para multi-turn, prefijar el assistant con tag para que el modelo lo entienda
                input_parts.append(f"[Previous assistant response]: {content}")
        return instructions, "\n\n".join(input_parts)

    def chat(
        self,
        model: str,
        messages: list[dict],
        tools: list[dict] | None = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        timeout: int = 90,
    ) -> BenchmarkResult:
        result = BenchmarkResult(
            provider=self.provider_name,
            model=model,
            test_name="",
            prompt=messages[-1].get("content", "")[:200],
        )

        old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(timeout)

        start = time.perf_counter()
        try:
            instructions, user_input = self._messages_to_input(messages)

            # Pro models son thinking heavy: aplicar multiplicador del estándar
            is_thinking = any(model.startswith(p) or p in model for p in THINKING_MODELS)
            effective_max = (
                max(max_tokens * THINKING_TOKEN_MULTIPLIER, THINKING_MIN_TOKENS)
                if is_thinking
                else max_tokens
            )

            kwargs: dict = {
                "model": model,
                "input": user_input,
                "max_output_tokens": effective_max,
            }
            if instructions:
                kwargs["instructions"] = instructions
            # Pro models NO aceptan temperature ≠ 1.0
            if not any(p in model.lower() for p in FIXED_TEMP_MODELS):
                kwargs["temperature"] = temperature
            if tools:
                kwargs["tools"] = tools
                kwargs["tool_choice"] = "auto"

            response = self.client.responses.create(**kwargs)
            end = time.perf_counter()

            signal.alarm(0)

            # Extraer texto: SDK expone output_text como atajo
            result.response = getattr(response, "output_text", "") or ""
            result.latency_total = end - start
            result.latency_first_token = result.latency_total
            result.success = True

            usage = getattr(response, "usage", None)
            if usage:
                # Responses API usa input_tokens/output_tokens (no prompt/completion)
                result.input_tokens = getattr(usage, "input_tokens", 0) or 0
                result.output_tokens = getattr(usage, "output_tokens", 0) or 0
                # Capturar reasoning tokens si están expuestos (output_tokens_details.reasoning_tokens)
                details = getattr(usage, "output_tokens_details", None)
                if details:
                    rt = getattr(details, "reasoning_tokens", None)
                    if rt:
                        result.metadata["reasoning_tokens"] = rt

            # Tool calls: vienen en output como items tipo function_call
            output_items = getattr(response, "output", []) or []
            tool_calls = [it for it in output_items if getattr(it, "type", "") == "function_call"]
            if tool_calls:
                result.tool_calls_made = len(tool_calls)
                result.metadata["tool_calls"] = [
                    {
                        "name": getattr(tc, "name", ""),
                        "arguments": getattr(tc, "arguments", ""),
                    }
                    for tc in tool_calls
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
            if len(error_msg) > 200:
                error_msg = error_msg[:200] + "..."
            result.error = error_msg
            result.success = False

        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)

        return result
