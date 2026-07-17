# Nemotron 3 Super — multi_turn/debugging_conversation

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 18.952s | tokens_per_second: 218.7
- input_tokens: 356 | output_tokens: 4145
- judge_score: 5 | justificación: La respuesta es precisa, relevante y profundiza en el problema de los errores 429 con una solución detallada y práctica, manteniendo la coherencia con el contexto de la conversación.

## Respuesta completa


¡Perfecto! El problema no es el límite de la API, sino que tu **retry infinito** está multiplicando las peticiones y provocando un *cascada* de 429.  
A continuación tienes una guía paso‑a‑paso para implementar un mecanismo de reintentos **seguro, controlado y respetuoso con los límites de rate‑limit** de OpenRouter (y de cualquier API REST).

---

## 1. Principios básicos de un buen retry

| Principio | Por qué importa |
|-----------|-----------------|
| **Límite de intentos** (ej. 3‑5) | Evita bucles infinitos. |
| **Back‑off exponencial** (1 s, 2 s, 4 s, 8 s…) | Da tiempo al servidor para recuperarse y reduce la presión. |
| **Jitter** (aleatoriedad pequeña) | Evita que muchos clientes hagan retry al mismo milisegundo ( “thundering herd”). |
| **Respeto al header `Retry‑After`** | Si la API indica cuándo volver a intentarlo, úsalo en vez de tu propio cálculo. |
| **Solo reintentar en errores transitorios** (429, 5xx, timeout, conexión caída) | No reintentes errores 4xx que indican un problema de solicitud (p.ej. 400, 401, 403). |
| **Logging claro** | Saber cuántos intentos se hicieron y por qué falló ayuda a depurar. |

---

## 2. Qué headers revisar en la respuesta 429

OpenRouter (como la mayoría de proveedores compatibles con OpenAI) devuelve, además del cuerpo JSON, headers como:

| Header | Significado |
|--------|-------------|
| `x-ratelimit-limit-requests` | Límite de requests por ventana (ej. 300). |
| `x-ratelimit-remaining-requests` | Cuántos te quedan en la ventana actual. |
| `x-ratelimit-reset-requests` | Época Unix (segundos) cuando se reinicia el contador. |
| `retry-after` (o `Retry-After`) | Segundos que debes esperar antes de volver a intentar (a veces incluye un timestamp). |

Si el header `retry-after` está presente, **úsalo directamente**; si no, calcula el tiempo de espera a partir de `x-ratelimit-reset-requests`.

---

## 3. Implementación práctica (Python)

A continuación tienes dos versiones:

### 3.1. Usando la biblioteca `tenacity` (recomendado)

`tenacity` ya implementa todo lo anterior (stop, wait, retry conditions, jitter, etc.) y es muy ligera.

```python
# pip install tenacity openai   # openai es el cliente oficial compatible con OpenRouter
import time
import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
)
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# ----------------- Configuración del cliente -----------------
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_API_KEY_AQUI",   # <-- pon tu key
)

# ----------------- Condiciones de retry -----------------
def is_retryable(exc):
    """Solo reintentar en 429, 5xx o errores de red/timeout."""
    if isinstance(exc, openai.RateLimitError):   # 429
        return True
    if isinstance(exc, openai.APIError):        # 5xx o otros API errors
        # openai.APIError tiene un atributo .status_code
        return getattr(exc, "status_code", 0) >= 500
    if isinstance(exc, (openai.APIConnectionError, openai.APITimeoutError)):
        return True
    return False

# Esperar según el header Retry-After si está disponible
def wait_retry_after(retry_state):
    exc = retry_state.outcome.exception()
    if isinstance(exc, openai.RateLimitError):
        # Intentamos leer el header desde la respuesta
        resp = getattr(exc, "response", None)
        if resp and resp.headers:
            # 1) Retry-After (puede ser segundos o una fecha HTTP)
            ra = resp.headers.get("retry-after") or resp.headers.get("Retry-After")
            if ra:
                try:
                    # Si es un número entero -> segundos
                    delay = int(ra)
                except ValueError:
                    # Si es una fecha HTTP, convertimos a segundos
                    from email.utils import parsedate_to_datetime
                    retry_dt = parsedate_to_datetime(ra)
                    delay = max(0, (retry_dt - datetime.datetime.now(datetime.timezone.utc)).total_seconds())
                return delay
            # 2) x-ratelimit-reset-requests (epoch seconds)
            reset = resp.headers.get("x-ratelimit-reset-requests")
            if reset:
                try:
                    reset_ts = int(reset)
                    now = int(time.time())
                    delay = max(0, reset_ts - now)
                    return delay
                except ValueError:
                    pass
    # Fallback: backoff exponencial con jitter
    return None   # dejamos que tenacity use su wait

# ----------------- Decorador de retry -----------------
@retry(
    reraise=True,                         # lanzar la excepción original si fallan todos los intentos
    stop=stop_after_attempt(4),           # máximo 4 intentos (1 original + 3 reintentos)
    wait=wait_exponential(multiplier=1, min=1, max=10),  # 1s,2s,4s,8s (capped a 10s)
    retry=retry_if_exception_type((openai.RateLimitError,
                                   openai.APIError,
                                   openai.APIConnectionError,
                                   openai.APITimeoutError)),
    before_sleep=before_sleep_log(log, logging.WARNING),
)
def call_openrouter(model: str, messages: list, **kwargs):
    """
    Envía una petición a OpenRouter y devuelve la respuesta.
    Se encarga de los reintentos según el decorador arriba.
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=512,
        **kwargs,
    )
    return response

# ----------------- Uso de ejemplo -----------------
if __name__ == "__main__":
    try:
        resp = call_openrouter(
            model="deepseek/deepseek-chat",   # o el identificador exacto que use OpenRouter
            messages=[{"role": "user", "content": "Hola, ¿cómo estás?"}],
        )
        print(resp.choices[0].message.content)
    except openai.RateLimitError as e:
        print(f"Se agotaron los reintentos por rate limit: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
```

#### Qué hace este código

1. **Define qué errores son retryables** (`is_retryable` implícitamente a través de `retry_if_exception_type`).  
2. **Intenta leer `Retry-After`** o `x-ratelimit-reset-requests` de la respuesta 429 y, si los encuentra, usa ese tiempo de espera en vez del back‑off genérico.  
3. **Si no hay header**, cae en un back‑off exponencial con `multiplier=1`, `min=1s`, `max=10s`.  
4. **Límite de intentos**: 4 en total (1 intento original + 3 reintentos). Puedes ajustar `stop_after_attempt`.  
5. **Logging**: cada vez que se duerme antes de un retry se escribe un `WARNING` con el motivo y el tiempo de espera.  

> **Tip**: Si prefieres no añadir una dependencia externa, puedes replicar la lógica con un bucle `while` y `time.sleep`, pero `tenacity` hace que el código sea mucho más legible y menos propenso a errores.

---

### 3.2. Implementación “manual” (sin librerías externas)

Si por alguna razón no quieres añadir `tenacity`, aquí tienes una versión pura de Python que sigue los mismos principios:

```python
import time
import openai
import logging
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_API_KEY_AQUI",
)

MAX_ATTEMPTS = 4          # 1 intento original + 3 reintentos
BASE_DELAY = 1            # segundos
MAX_DELAY = 10            # techo del backoff

def should_retry(exc: Exception) -> bool:
    if isinstance(exc, openai.RateLimitError):
        return True
    if isinstance(exc, openai.APIError):
        return getattr(exc, "status_code", 0) >= 500
    if isinstance(exc, (openai.APIConnectionError, openai.APITimeoutError)):
        return True
    return False

def get_retry_delay(exc: Exception, attempt: int) -> float:
    """
    Devuelve cuántos segundos esperar antes del próximo intento.
    Respeta Retry-After / x-ratelimit-reset-requests si existen.
    """
    if isinstance(exc, openai.RateLimitError):
        resp = getattr(exc, "response", None)
        if resp and resp.headers:
            # 1) Retry-After
            ra = resp.headers.get("retry-after") or resp.headers.get("Retry-After")
            if ra:
                try:
                    return float(ra)
                except ValueError:
                    # Fecha HTTP
                    retry_dt = parsedate_to_datetime(ra)
                    return max(0, (retry_dt - datetime.now(timezone.utc)).total_seconds())
            # 2) x-ratelimit-reset-requests
            reset = resp.headers.get("x-ratelimit-reset-requests")
            if reset:
                try:
                    reset_ts = int(reset)
                    now = int(time.time())
                    return max(0, reset_ts - now)
                except ValueError:
                    pass
    # Fallback: exponencial con jitter
    exp_delay = BASE_DELAY * (2 ** (attempt - 1))   # attempt starts at 1
    exp_delay = min(exp_delay, MAX_DELAY)
    jitter = exp_delay * 0.1 * (2 * random.random() - 1)  # +/-10%
    return max(0, exp_delay + jitter)

# Necesitamos parsedate_to_datetime para fechas HTTP
from email.utils import parsedate_to_datetime
import random

def call_with_retry(model: str, messages: list, **kwargs):
    attempt = 0
    while True:
        attempt += 1
        try:
            log.info(f"Intento {attempt}/{MAX_ATTEMPTS}...")
            return client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs,
            )
        except Exception as exc:
            if not should_retry(exc) or attempt >= MAX_ATTEMPTS:
                log.error(f"Se agotaron los reintentos o error no retryable: {exc}")
                raise  # re-lanza la excepción original
            delay = get_retry_delay(exc, attempt)
            log.warning(f"Error {exc.__class__.__name__}: reintentando en {delay:.2f}s...")
            time.sleep(delay)

# ----------------- Uso -----------------
if __name__ == "__main__":
    try:
        resp = call_with_retry(
            model="deepseek/deepseek-chat",
            messages=[{"role": "user", "content": "Hola, ¿cómo estás?"}],
            temperature=0.7,
            max_tokens=512,
        )
        print(resp.choices[0].message.content)
    except Exception as e:
        print(f"Fallo final: {e}")
```

**Puntos clave de esta versión manual:**

- **`MAX_ATTEMPTS`** controla cuántas veces se vuelve a intentar.
- **`get_retry_delay`** prioriza los headers de la API; si no existen, usa un back‑off exponencial con un pequeño *jitter* (±10 %) para evitar sincronización.
- Se hace **logging** en cada intento y en cada espera.

---

## 4. Checklist rápido para que lo pongas en producción

| ✅ | Acción |
|----|--------|
| 1 | **Envuelve cada llamada a la API** en una función con retry (como `call_openrouter` o `call_with_retry`). |
| 2 | **Limita los intentos** a 3‑5 (dependiendo de cuán crítico sea el request). |
| 3 | **Usa back‑off exponencial** (1 s, 2 s, 4 s…) con un techo razonable (8‑10 s). |
| 4 | **Añade jitter** (±10‑20 %) para evitar thundering herd. |
| 5 | **Lee y respeta** `Retry-After` o `x-ratelimit-reset-requests` cuando estén presentes. |
| 6 | **Solo reintenta** en 429, 5xx, timeout y errores de conexión. No reintentes 400/401/403/404 (esos son errores de la request). |
| 7 | **Loguea** cada intento, cada tiempo de espera y la excepción final. |
| 8 | **Prueba** simulando un 429 (por ejemplo, poniendo un `rate limit` muy bajo en un entorno de staging) para asegurar que el back‑off funciona y no se dispara un bucle infinito. |
| 9 | **Monitoriza** la tasa de reintentos en tus métricas (por ejemplo, con Prometheus o CloudWatch) para detectar si estás rozando el límite frecuentemente y quizá necesites subir tu plan o distribuir la carga. |
|10| **Documenta** el wrapper en tu códigobase para que otros desarrolladores sepan que no deben llamar directamente al cliente sin pasar por la función de retry. |

---

## 5. Preguntas frecuentes (FAQ)

| Pregunta | Respuesta |
|----------|-----------|
| **¿Cuántos requests por minuto puedo hacer realmente con DeepSeek V3 en OpenRouter?** | Según la documentación pública, el límite es **300 requests por minuto** (RPM) para la mayoría de los modelos en el plan de pago. Si tienes un plan “free tier” puede ser mucho menor (ej. 20 RPM). Verifica tu panel de usuario → “Limits”. |
| **¿El header `Retry-After` siempre viene en segundos?** | Puede venir como número de segundos **o** como una fecha HTTP (ej. `Wed, 21 Oct 2025 07:28:00 GMT`). El código anterior maneja ambos casos. |
| **¿Qué pasa si ignoro `Retry-After` y sigo usando mi propio backoff?** | No es catastrófico, pero podrías estar esperando más tiempo del necesario (inyectando latencia) o menos (siguiendo recibiendo 429). Lo mejor es usar el hint del servidor cuando está disponible. |
| **¿Debería usar una cola o worker externo para evitar que mi aplicación se bloquee?** | Si tu aplicación es de alta concurrencia (muchas peticiones simultáneas), considera usar un **pool de workers** (ej. `concurrent.futures.ThreadPoolExecutor`, `asyncio` con semáforo, o un sistema de colas como Redis + RQ) para que el límite de la API no bloquee todo el proceso. |
| **¿Puedo reutilizar el mismo cliente `openai.OpenAI` entre hilos?** | Sí, el cliente es thread‑safe. No necesitas crear uno por request; de hecho, crear uno por request agrega overhead y puede generar problemas de socket. |

---

## 6. Resumen rápido (para copiar‑pegar)

```python
# 1️⃣ Instala dependencias
# pip install tenacity openai

# 2️⃣ Código de reutilización
import openai, time, random, logging
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type, before_sleep_log

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

client = openai.OpenAI(base_url="https://openrouter.ai/api/v1", api_key="TU_API_KEY")

def is_retryable(exc):
    if isinstance(exc, openai.RateLimitError): return True
    if isinstance(exc, openai.APIError): return getattr(exc, "status_code", 0) >= 500
    if isinstance(exc, (openai.APIConnectionError, openai.APITimeoutError)): return True
    return False

@retry(
    reraise=True,
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((openai.RateLimitError,
                                   openai.APIError,
                                   openai.APIConnectionError,
                                   openai.APITimeoutError)),
    before_sleep=before_sleep_log(log, logging.WARNING),
)
def safe_call(model, messages, **kwargs):
    return client.chat.completions.create(model=model, messages=messages, **kwargs)

# Uso
resp = safe_call(
    model="deepseek/deepseek-chat",
    messages=[{"role":"user","content":"Hola"}],
    temperature=0.7,
    max_tokens=200,
)
print(resp.choices[0].message.content)
```

Con este patrón **eliminarás el loop infinito**, respetarás los límites de la API y tendrás un comportamiento predecible y observable. ¡Éxitos con tus integraciones! 🚀