# Tencent Hy4 — multi_turn/debugging_conversation

- model_id: `tencent/hy4`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 48.994s | tokens_per_second: 100.8
- input_tokens: 371 | output_tokens: 4939

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico experto en APIs y automatizacion. Ayuda a diagnosticar problemas paso a paso.

**user:**

Mi API de OpenRouter me da error 429 todo el tiempo. No puedo hacer ni una llamada.

**assistant:**

Error 429 es 'Too Many Requests' - significa que estas excediendo el rate limit. Vamos a diagnosticarlo:

1. Cuantas requests/minuto estas haciendo aproximadamente?
2. Que modelo estas usando? (algunos tienen limites mas bajos)
3. Estas usando la API key correcta? (las keys gratuitas tienen limites muy bajos)

**user:**

Estoy haciendo como 5 requests por minuto, usando DeepSeek V3. Tengo una API key con creditos pagados, unos $20 de saldo.

**assistant:**

5 req/min con DeepSeek deberia funcionar sin problemas - el limite es 300 RPM. Algo mas esta pasando. Vamos a verificar:

1. Estas reutilizando la misma instancia del cliente o creando una nueva por cada request?
2. Tienes algun retry automatico que podria estar multiplicando los requests?
3. Me puedes mostrar el header completo de la respuesta 429? Especificamente los headers `x-ratelimit-*`

**user:**

Acabo de revisar y resulta que tengo un loop en mi codigo que hace retry infinito cuando recibe un error. Asi que cada 429 genera como 100 requests mas. Pero no se como arreglarlo bien, como deberia implementar los retries?


## Respuesta completa

Perfecto, ahí está la causa raíz. Y ojo con un detalle importante antes de tocar código:

> **El storm probablemente sigue activo ahora mismo.** Mientras el loop siga corriendo, sigue consumiendo cuota, por eso "ni una llamada" entra. Lo primero es **matar el proceso / desactivar el worker**, no arreglar el retry todavía.

Además, es muy probable que hayas quemado la cuota **diaria** (no solo la de por-minuto). Aunque arregles el código, puedes seguir viendo 429 hasta el reset. Compéalo con:

```bash
curl -s https://openrouter.ai/api/v1/key \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" | jq
# data.usage / data.limit / data.limit_remaining / data.rate_limit
```

Los headers `x-ratelimit-*` de la respuesta 429 son la fuente de verdad (los límites varían por saldo, modelo y proveedor upstream).

---

## Reglas de oro para retries

| Regla | Por qué |
|---|---|
| **Solo reintentar 429, 408, 5xx y timeouts de red** | Un 400/401/422 nunca se arregla solo; reintentarlo es puro ruido (y gasto) |
| **Tope duro de intentos** (3–5) | Un `while True` es exactamente lo que te rompió |
| **Respetar `Retry-After`** | En 429 manda sobre tu backoff. Ignorarlo = seguir golpeando la pared |
| **Exponential backoff + jitter** | Sin jitter, todos los workers reintentan sincronizados (thundering herd) |
| **Deadline total** | 4 intentos × 30s no deberían bloquear un request 2 min |
| **Circuit breaker** | Si llevas N 429 seguidos, deja de intentar hasta el reset |
| **Cap de concurrencia** | Limita cuántas llamadas pueden estar en vuelo a la vez |
| **Loguear, no silenciar** | Cada retry debe dejar rastro con status + wait + headers |

---

## Implementación de referencia (Python / httpx)

```python
import random, time, email.utils, httpx
from datetime import datetime, timezone

MAX_RETRIES   = 4
BASE, CAP     = 0.5, 30.0
DEADLINE_S    = 60.0
RETRYABLE     = {408, 429, 500, 502, 503, 504}

URL = "https://openrouter.ai/api/v1/chat/completions"

def parse_retry_after(resp: httpx.Response) -> float | None:
    """Acepta tanto segundos como HTTP-date."""
    v = resp.headers.get("retry-after")
    if not v:
        return None
    try:
        return max(0.0, float(v))
    except ValueError:
        try:
            dt = email.utils.parsedate_to_datetime(v)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return max(0.0, (dt - datetime.now(timezone.utc)).total_seconds())
        except Exception:
            return None

def backoff(attempt: int) -> float:
    """Exponential + equal jitter (evita reintentos sincronizados)."""
    cap = min(CAP, BASE * 2 ** attempt)
    return cap / 2 + random.uniform(0, cap / 2)

def chat(payload: dict, api_key: str) -> dict:
    started = time.monotonic()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://tu-app.com",  # opcional
        "X-Title": "mi-app",
    }

    with httpx.Client(timeout=30.0) as client:   # <- reutilizar el cliente
        for attempt in range(MAX_RETRIES + 1):
            try:
                r = client.post(URL, json=payload, headers=headers)
            except (httpx.TimeoutException, httpx.TransportError):
                if attempt == MAX_RETRIES:
                    raise
                time.sleep(backoff(attempt))
                continue

            if r.status_code < 400:
                return r.json()

            # Fail fast: 400/401/403/422 NO se reintentan
            if r.status_code not in RETRYABLE:
                raise RuntimeError(f"{r.status_code} no retryable: {r.text}")

            if attempt == MAX_RETRIES:
                raise RuntimeError(f"Agotados {MAX_RETRIES} reintentos: {r.status_code} {r.text}")

            wait = parse_retry_after(r)
            if wait is None:
                wait = backoff(attempt)

            # Un Retry-After enorme (reset diario) no se duerme dentro del handler
            if wait > 120:
                raise RuntimeError(
                    f"Rate limit de larga duración ({wait:.0f}s). "
                    f"reset={r.headers.get('x-ratelimit-reset')} — reagendar, no reintentar."
                )

            remaining = DEADLINE_S - (time.monotonic() - started)
            if remaining <= 0:
                raise TimeoutError("Deadline total excedido")
            wait = min(wait, remaining)

            print(
                f"[{attempt+1}/{MAX_RETRIES}] {r.status_code} → sleep {wait:.2f}s | "
                f"limit={r.headers.get('x-ratelimit-limit')} "
                f"remaining={r.headers.get('x-ratelimit-remaining')} "
                f"reset={r.headers.get('x-ratelimit-reset')}"
            )
            time.sleep(wait)
```

Puntos clave del snippet: el `for` con rango finito, el `raise` en 4xx, el `Retry-After` con tope, y el cliente reutilizado (crear uno por request también suma conexiones y latencia).

### Alternativa más limpia: `tenacity`

```python
from tenacity import retry, stop_after_attempt, retry_if_exception_type, reraise

class RetryableHTTP(Exception):
    def __init__(self, resp): self.resp = resp

def wait_smart(state) -> float:
    exc = state.outcome.exception()
    if isinstance(exc, RetryableHTTP):
        ra = parse_retry_after(exc.resp)
        if ra is not None:
            return min(ra, 120.0)
    return backoff(state.attempt_number - 1)

@retry(
    retry=retry_if_exception_type((RetryableHTTP, httpx.TransportError)),
    stop=stop_after_attempt(5),
    wait=wait_smart,
    reraise=True,
)
def chat(payload, api_key):
    r = httpx.post(URL, json=payload, headers={"Authorization": f"Bearer {api_key}"}, timeout=30)
    if r.status_code in RETRYABLE:
        raise RetryableHTTP(r)
    r.raise_for_status()          # 4xx sale disparado, sin retry
    return r.json()
```

---

## Guardarraíl anti-storm (circuit breaker)

Añade esto además del backoff, es lo que evita que un incidente se repita:

```python
_consecutive_429 = 0
_open_until = 0.0

def guard():
    global _consecutive_429, _open_until
    if time.monotonic() < _open_until:
        raise RuntimeError("Circuito abierto: demasiados 429, esperando reset")

def on_429(reset_epoch_s: float | None):
    global _consecutive_429, _open_until
    _consecutive_429 += 1
    if _consecutive_429 >= 3:
        _open_until = reset_epoch_s or (time.monotonic() + 60)
        # aquí: métrica / alerta
def on_success():
    global _consecutive_429
    _consecutive_429 = 0
```

Si trabajas async, acompáñalo con `asyncio.Semaphore(5)` para limitar concurrencia.

---

## Extra específico de OpenRouter

Si el 429 viene del **proveedor upstream** (DeepSeek) y no de tu key, el body suele indicarlo. En ese caso reintentar contra el mismo proveedor no ayuda. Usa el routing de OpenRouter en el payload:

```json
{
  "model": "deepseek/deepseek-chat",
  "messages": [{"role": "user", "content": "..."}],
  "models": ["deepseek/deepseek-chat", "deepseek/deepseek-r1"],
  "provider": { "allow_fallbacks": true, "sort": "throughput" }
}
```

Así OpenRouter conmuta de proveedor automáticamente en vez de devolverte el 429.

---

## Plan de acción ordenado

1. **Detén el proceso** que está en loop (ahora).
2. `GET /api/v1/key` → mira `limit_remaining` y `rate_limit` para saber si quemaste cuota diaria.
3. Si `remaining ≈ 0`, **espera al reset**; no sirve probar mientras tanto.
4. Sustituye el loop por una de las implementaciones de arriba.
5. **Prueba con UNA sola llamada y retries desactivados** → confirma 200.
6. Activa retries y verifica en logs que un 429 produce como máximo 4 líneas y luego corta.
7. Añade alerta sobre "≥3 429 consecutivos".

¿Quieres que te lo adapte a Node/TypeScript o a tu cliente actual? Si me pegas el fragmento del loop te lo parcheo directamente, y de paso reviso si estás propagando bien el `x-ratelimit-reset` (confirma la unidad en tu respuesta: algunos lo dan en epoch ms, no en segundos).