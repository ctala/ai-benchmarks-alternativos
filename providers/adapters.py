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
    "kimi-k2.6", "kimi-k2.7", "Kimi",       # Moonshot K2.6+
    "nemotron", "Nemotron",                 # NVIDIA Nemotron 3+
    "gemini-2.5-pro", "gemini-3-pro",       # Google Pro tier (reasoning interno)
    "deepseek-v4", "deepseek-r",            # DeepSeek V4+ (R1, V4 Pro, V4 Flash) — descubierto abril 27 con 30/91 NoneType en V4 Pro
    "gemma4", "gemma-4",                    # Gemma 4 — descubierto abril 28 en Ollama DGX: expone "reasoning" field separado del "content"
    "minimax-m3", "MiniMax-M3",             # MiniMax M3 (1 jun 2026) — híbrido, emite <think> por default (verificado en API directa)
    "qwen3.7-max", "qwen3.7-plus",          # Qwen 3.7 (20 may 2026) — reasoning-agent, thinking tokens facturados
    "claude-fable", "fable-5",              # Claude Fable 5 (14 jul 2026) — thinking por default vía OpenRouter. Sin esto,
                                            # 22/143 runs con respuesta VACÍA y success=True (copy_jwt: 1 token) — el mismo
                                            # modo de falla de los 165 runs vacíos de abril. Su primer examen canónico salió
                                            # inválido (Q 7.64 = artefacto) y está en cuarentena (*.invalid).
)

# Modelos que sólo aceptan temperature=1.0 (rechazan otros con error 400).
# El adapter omite el parámetro y deja que la API use su default.
FIXED_TEMP_MODELS = ("gpt-5.5", "gpt-5-pro", "gpt-5.5-pro", "o1", "o3")

# Multiplicador de max_tokens para thinking models. Sin esto, agotan el budget
# en reasoning interno y devuelven content="" (descubierto abril 2026 con 165
# runs vacíos en Kimi K2.6/GPT-5.5/GLM-5.1/Nemotron).
THINKING_TOKEN_MULTIPLIER = 4
# Mínimo absoluto para thinking models, aunque el max_tokens base sea bajo.
# Vuelto a 8192 el 7 mayo 2026 tras experimento con 16384.
# Historial:
# - 8192 default: GPT-5.5 con 151/151 content vacío (consume todo en reasoning)
# - 16384: smoke OK pero en bench real cada test 16-50 min, ETA 181h para 223 tests
# Conclusión: GPT-5.5 es OVER-thinking y no es medible bien con nuestra
# metodología de single-shot. Documentado como limitación del benchmark.
# Para los demás thinking models (GPT-5/o1/o3/Kimi K2.6/Nemotron/Gemma 4),
# 8192 funciona bien en casi todos los casos.
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
            # llama-server (llama.cpp) sirve los builds Gemma 4 del Spark, que razonan
            # internamente por default (emiten reasoning_content). Dos variantes:
            #  - provider "llama_server"       → reasoning OFF (enable_thinking=false),
            #    max_tokens normal. Uso agente/baja latencia.
            #  - provider "llama_server_think" → reasoning ON, max_tokens ALTO (×4, min
            #    8192) para que quepan razonamiento + respuesta.
            # En ambos se usa el param `max_tokens` (llama.cpp NO acepta
            # max_completion_tokens). NO se toca el `gemma-4` global de THINKING_MODELS:
            # el Gemma de Ollama sí necesita su trato thinking aparte.
            is_llama_server = self.provider_name.startswith("llama_server")
            reasoning_off = self.provider_name == "llama_server"
            reasoning_on_llama = self.provider_name == "llama_server_think"
            if is_llama_server:
                token_param = "max_tokens"
                effective_max = (max(max_tokens * THINKING_TOKEN_MULTIPLIER, THINKING_MIN_TOKENS)
                                 if reasoning_on_llama else max_tokens)
            else:
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
            # llama-server: apagar el reasoning interno de Gemma 4 (verificado:
            # 232→6 tokens, content correcto, reasoning_content vacío). 3-4× más
            # rápido y representativo del uso en agentes/baja latencia.
            if reasoning_off:
                extra_body["chat_template_kwargs"] = {"enable_thinking": False}
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


class ClaudeCodeProvider:
    """Mide modelos Anthropic via la SUSCRIPCIÓN Claude Code (CLI `claude -p`),
    a tarifa plana en vez de pagar la API por token.

    Provider key: "claude_code". El `id` del modelo en config debe ser el alias
    del CLI (ej. "opus", "sonnet", "claude-opus-4-8").

    ⚠️ CAVEAT metodológico: `claude -p` corre el modelo en modo Claude Code, con
    ~8.8K tokens de scaffolding residual aun con tools deshabilitados y system
    prompt mínimo (vs ~30K sin flags). NO es un chat completion 100% limpio →
    los resultados se marcan `subscription_measured=True` y NO deben usarse para
    tool-calling (las tools del CLI difieren del schema OpenAI del benchmark).
    Costo real: $0 (suscripción); el ranking lo costea al precio OpenRouter.
    """

    def __init__(self, provider_name: str = "claude_code", cli: str = "claude"):
        self.provider_name = provider_name
        self.cli = cli

    def chat(self, model, messages, tools=None, temperature=0.7,
             max_tokens=2048, timeout=90, force_reasoning=False):
        import subprocess
        import json as _json
        import os as _os
        # CRÍTICO: limpiar credenciales de API del env. Si el runner cargó
        # ANTHROPIC_API_KEY/AUTH_TOKEN desde .env, `claude -p` intenta usarlas
        # (y da 401 si son inválidas) en vez del login OAuth de la suscripción.
        # Sin esas vars, claude usa la suscripción Claude Code (lo que queremos).
        _env = {k: v for k, v in _os.environ.items()
                if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL")}
        result = BenchmarkResult(
            provider=self.provider_name, model=model, test_name="",
            prompt=(messages[-1].get("content", "") or "")[:200],
        )
        system = "\n".join(m.get("content", "") for m in messages if m.get("role") == "system")
        convo = []
        for m in messages:
            if m.get("role") == "system":
                continue
            c = m.get("content", "") or ""
            convo.append(c if m.get("role") == "user" else f"[respuesta previa del asistente]:\n{c}")
        user_prompt = "\n\n".join(convo)
        cmd = [self.cli, "-p", "--output-format", "json", "--model", model,
               "--disallowedTools", "*", "--exclude-dynamic-system-prompt-sections",
               "--system-prompt", "Responde directamente la consulta del usuario."]
        if system:
            cmd += ["--append-system-prompt", system]
        # El prompt va por STDIN, no como argumento: prompts largos (niah long-context,
        # ~256K tokens = ~1M chars) excedían ARG_MAX → OSError Errno 7 "arg list too
        # long". Por stdin no hay límite de tamaño; `claude -p` lo lee igual. Verificado
        # (jun 2026): prompt corto y de 324K tokens funcionan; arriba del contexto real
        # del modelo devuelve "Prompt is too long" (error limpio, no crash).
        start = time.perf_counter()
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                                  input=user_prompt, env=_env)
            elapsed = time.perf_counter() - start
            # NOTA: `claude -p` anidado dentro de otra sesión Claude Code puede
            # salir con returncode=1 AUNQUE produzca JSON de resultado válido
            # (warning no-fatal). Por eso parseamos el stdout y nos guiamos por
            # `is_error`/`result`, no por el returncode.
            try:
                d = _json.loads((proc.stdout or "").strip())
            except Exception:
                result.error = f"claude cli rc={proc.returncode} sin JSON: err={(proc.stderr or '')[:150]} out={(proc.stdout or '')[:150]}"
                return result
            result.response = d.get("result", "") or ""
            u = d.get("usage") or {}
            result.input_tokens = u.get("input_tokens", 0) or 0
            result.output_tokens = u.get("output_tokens", 0) or 0
            result.latency_total = (d.get("duration_ms", 0) or 0) / 1000.0 or elapsed
            result.latency_first_token = (d.get("ttft_ms", 0) or 0) / 1000.0
            if result.output_tokens and result.latency_total:
                result.tokens_per_second = result.output_tokens / result.latency_total
            result.success = bool(result.response) and not d.get("is_error")
            if not result.success:
                result.error = f"is_error={d.get('is_error')} subtype={d.get('subtype')} api_err={d.get('api_error_status')} result={(result.response or '')[:120]}"
            result.metadata = {"subscription_measured": True}
        except subprocess.TimeoutExpired:
            result.error = "claude cli timeout"
        except Exception as e:
            result.error = f"claude cli error: {type(e).__name__}: {e}"
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


class DiffusionGemmaProvider:
    """
    Adaptador para DiffusionGemma via llama-diffusion-cli (llama.cpp PR #24423).

    DiffusionGemma NO es autoregresivo: genera bloques de 256 tokens mediante
    denoising. El binario llama-diffusion-cli es un CLI, no un servidor, así que
    este provider ejecuta un subprocess por request y parsea el output.

    Soporta "multi-turn" de forma stateless: el runner le pasa el historial
    completo en `messages` y se concatena en un único prompt. No es tan limpio
    como una conversación real con -cnv, pero permite correr agent_long_horizon.

    Provider key: "diffusion_cli". El config del modelo debe incluir:
        - bin_path: ruta al binario llama-diffusion-cli
        - gguf_path: ruta al .gguf
        - ngl: capas en GPU (default 99)
        - ctx_size: ventana de contexto (default 8192)
        - seed: semilla para reproducibilidad (default 42)
    """

    def __init__(
        self,
        provider_name: str = "diffusion_cli",
        bin_path: str = "",
        gguf_path: str = "",
        ngl: int = 99,
        ctx_size: int = 8192,
        seed: int = 42,
    ):
        self.provider_name = provider_name
        self.bin_path = bin_path
        self.gguf_path = gguf_path
        self.ngl = ngl
        self.ctx_size = ctx_size
        self.seed = seed

    @staticmethod
    def _messages_to_prompt(messages: list[dict]) -> str:
        """Convierte el historial de chat en un prompt de texto plano."""
        parts = []
        for m in messages:
            role = m.get("role", "user")
            content = (m.get("content", "") or "").strip()
            if not content:
                continue
            if role == "system":
                parts.append(f"System: {content}")
            elif role == "user":
                parts.append(f"User: {content}")
            elif role == "assistant":
                parts.append(f"Assistant: {content}")
        return "\n\n".join(parts)

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
        import subprocess
        import re as _re

        result = BenchmarkResult(
            provider=self.provider_name,
            model=model,
            test_name="",
            prompt=(messages[-1].get("content", "") or "")[:200],
        )

        prompt = self._messages_to_prompt(messages)
        if not prompt:
            result.error = "Prompt vacio"
            return result

        cmd = [
            self.bin_path,
            "-m", self.gguf_path,
            "-ngl", str(self.ngl),
            "--ctx-size", str(self.ctx_size),
            "-n", str(max_tokens),
            "--seed", str(self.seed),
            "-p", prompt,
        ]

        start = time.perf_counter()
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            elapsed = time.perf_counter() - start
            stdout = proc.stdout or ""
            stderr = proc.stderr or ""

            if proc.returncode != 0:
                result.latency_total = elapsed
                result.error = f"llama-diffusion-cli exit {proc.returncode}: {stderr[:250]}"
                return result

            # Parsear metricas. Ejemplo de linea final:
            # throughput: 23.2 tok/s (2048 tok in 88462.60ms), in-step parallel 472 tok/s
            throughput_match = _re.search(
                r"throughput:\s*([\d.]+)\s*tok/s\s*\((\d+)\s*tok\s+in\s+([\d.]+)\s*ms\)",
                stdout,
            )
            total_time_match = _re.search(
                r"total time:\s*([\d.]+)\s*ms",
                stdout,
            )

            if throughput_match:
                result.tokens_per_second = float(throughput_match.group(1))
                result.output_tokens = int(throughput_match.group(2))
                result.latency_total = float(throughput_match.group(3)) / 1000.0
                result.latency_first_token = result.latency_total
            elif total_time_match:
                result.latency_total = float(total_time_match.group(1)) / 1000.0
                result.latency_first_token = result.latency_total
            else:
                result.latency_total = elapsed
                result.latency_first_token = elapsed

            # La respuesta es todo lo anterior a la seccion de metricas.
            lines = stdout.splitlines()
            cutoff = len(lines)
            for i, line in enumerate(lines):
                if "total time:" in line or "throughput:" in line:
                    cutoff = i
                    break
            response = "\n".join(lines[:cutoff]).strip()

            # El CLI a veces repite el prompt al inicio; intentar limpiarlo.
            if response.startswith(prompt):
                response = response[len(prompt):].strip()

            # Si force_reasoning, agregar token <|think|> al system prompt. DiffusionGemma
            # soporta thinking mode incluyendo <|think|> al inicio del system prompt.
            # Como ya concatenamos, no hacemos nada especial aqui; el usuario puede
            # incluirlo en el system prompt del test si quiere.

            result.response = response
            result.success = bool(response)
            if not result.success:
                result.error = "Respuesta vacia del modelo"
                result.error += f" (stderr: {stderr[:200]})" if stderr else ""

        except subprocess.TimeoutExpired:
            result.latency_total = time.perf_counter() - start
            result.error = f"TIMEOUT: llama-diffusion-cli no respondio en {timeout}s"

        except Exception as e:
            result.latency_total = time.perf_counter() - start
            error_msg = str(e)
            if len(error_msg) > 200:
                error_msg = error_msg[:200] + "..."
            result.error = f"DiffusionGemmaProvider error: {error_msg}"

        return result
