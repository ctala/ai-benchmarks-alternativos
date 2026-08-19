# Claude Opus 5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 50.037s | tokens_per_second: 80.7
- input_tokens: 539 | output_tokens: 4040

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

## Por qué tu loop empeoraba el problema

Lo que tenías es un **retry storm**: el 429 te dice "frena", y tu código responde acelerando. Peor aún, es auto-sostenido — los reintentos consumen la cuota que necesitas para que la ventana se libere, así que nunca sales del estado de error. Con ~100 requests por cada fallo, un solo 429 te mantiene bloqueado indefinidamente.

Dos cosas antes del código:

- **Para el proceso y espera 1–2 minutos** antes de volver a probar, para que la ventana de rate limit se limpie.
- Revisa tu saldo en el dashboard. Los 429 normalmente no consumen créditos, pero si algunos requests sí llegaron a procesarse, conviene confirmar.

---

## Reglas de oro para retries

**1. Distingue errores reintentables de los que no lo son**

| Reintentar | No reintentar |
|---|---|
| 429 (rate limit) | 400 (request mal formado) |
| 500, 502, 503, 504 | 401 / 403 (auth) |
| Timeouts, connection reset | 404 (modelo inexistente) |
| | 422 (validación) |

Reintentar un 400 es inútil: el request va a fallar igual las 100 veces.

**2. Exponential backoff con jitter.** Espera 1s, 2s, 4s, 8s... con un componente aleatorio. El jitter evita que múltiples workers reintenten sincronizados (thundering herd).

**3. Límite duro de intentos.** 4–5 máximo. Si falla 5 veces con backoff, hay un problema real que un retry #6 no resuelve.

**4. Respeta `Retry-After`.** Si el servidor te dice explícitamente cuánto esperar, obedece — es más preciso que tu cálculo.

---

## Implementación en Python

```python
import httpx, random, time, logging

log = logging.getLogger(__name__)

RETRYABLE_STATUS = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 5
BASE_DELAY = 1.0
MAX_DELAY = 60.0
MAX_TOTAL_ELAPSED = 180.0  # circuit breaker temporal


def parse_retry_after(response: httpx.Response) -> float | None:
    """Extrae el delay sugerido por el servidor, si existe."""
    ra = response.headers.get("retry-after")
    if ra:
        try:
            return float(ra)
        except ValueError:
            pass  # puede venir como HTTP-date; ignoramos ese caso

    reset = response.headers.get("x-ratelimit-reset")
    if reset:
        try:
            val = float(reset)
            # OpenRouter suele devolver timestamp Unix en ms
            if val > 1e11:
                val = val / 1000
            delta = val - time.time()
            if 0 < delta < MAX_DELAY:
                return delta
        except ValueError:
            pass
    return None


def backoff_delay(attempt: int, suggested: float | None = None) -> float:
    """Full jitter. attempt empieza en 0."""
    if suggested is not None:
        # respeta el servidor + pequeño margen aleatorio
        return min(suggested + random.uniform(0, 1), MAX_DELAY)
    ceiling = min(MAX_DELAY, BASE_DELAY * (2 ** attempt))
    return random.uniform(0, ceiling)


def call_openrouter(client: httpx.Client, payload: dict) -> dict:
    started = time.monotonic()
    last_error = None

    for attempt in range(MAX_ATTEMPTS):
        if time.monotonic() - started > MAX_TOTAL_ELAPSED:
            raise RuntimeError(f"Presupuesto de tiempo agotado: {last_error}")

        try:
            r = client.post("/chat/completions", json=payload, timeout=60.0)

            if r.status_code == 200:
                return r.json()

            if r.status_code not in RETRYABLE_STATUS:
                # error permanente: falla rápido y ruidoso
                r.raise_for_status()

            last_error = f"HTTP {r.status_code}: {r.text[:200]}"
            delay = backoff_delay(attempt, parse_retry_after(r))
            log.warning(
                "Intento %d/%d falló (%s). Reintentando en %.2fs",
                attempt + 1, MAX_ATTEMPTS, last_error, delay
            )

        except (httpx.TimeoutException, httpx.TransportError) as e:
            last_error = repr(e)
            delay = backoff_delay(attempt)
            log.warning("Error de red: %s. Reintentando en %.2fs", e, delay)

        if attempt < MAX_ATTEMPTS - 1:
            time.sleep(delay)

    raise RuntimeError(f"Agotados {MAX_ATTEMPTS} intentos. Último error: {last_error}")


# Reutiliza el cliente: connection pooling, no lo crees por request
client = httpx.Client(
    base_url="https://openrouter.ai/api/v1",
    headers={"Authorization": f"Bearer {API_KEY}"},
    limits=httpx.Limits(max_connections=10),
)
```

**Nota sobre `MAX_TOTAL_ELAPSED`:** es tan importante como `MAX_ATTEMPTS`. Sin él, 5 intentos con backoff hasta 60s pueden bloquear un request de usuario casi 2 minutos.

---

## Rate limiter proactivo (mejor que reaccionar)

El retry es la red de seguridad. La solución real es no llegar al límite. Un token bucket simple:

```python
import threading, time

class RateLimiter:
    def __init__(self, rate_per_sec: float, burst: int):
        self.rate = rate_per_sec
        self.capacity = burst
        self.tokens = float(burst)
        self.last = time.monotonic()
        self.lock = threading.Lock()

    def acquire(self):
        with self.lock:
            now = time.monotonic()
            self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
            self.last = now
            if self.tokens < 1:
                wait = (1 - self.tokens) / self.rate
                time.sleep(wait)
                self.tokens = 0
                self.last = time.monotonic()
            else:
                self.tokens -= 1

# 4 req/s con burst de 8 — muy por debajo del límite
limiter = RateLimiter(rate_per_sec=4, burst=8)

limiter.acquire()
result = call_openrouter(client, payload)
```

---

## Alternativas si no quieres escribirlo a mano

**`tenacity`** (Python), declarativo:

```python
from tenacity import (retry, stop_after_attempt, wait_exponential_jitter,
                      retry_if_exception_type, before_sleep_log)

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=1, max=60),
    retry=retry_if_exception_type((httpx.TimeoutException, RateLimitError)),
    before_sleep=before_sleep_log(log, logging.WARNING),
    reraise=True,
)
def call(payload): ...
```

**SDK de OpenAI** (compatible con OpenRouter) ya trae retries con backoff:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
    max_retries=3,   # default es 2; nunca infinito
    timeout=60.0,
)
```

Si usas el SDK, **no envuelvas sus llamadas en tu propio retry loop** — se multiplican (3 × 3 = 9 requests reales).

---

## Detalle específico de OpenRouter

Algunos 429 no vienen de OpenRouter sino del proveedor upstream. El body suele incluir metadata útil:

```python
err = r.json().get("error", {})
provider = err.get("metadata", {}).get("provider_name")
log.warning("429 desde provider=%s", provider)
```

Si el 429 es del upstream, considera configurar fallbacks de proveedor en tu request (`provider.order` o `models` como array) en lugar de solo reintentar contra el mismo endpoint saturado.

---

## Checklist final

- [ ] Cliente HTTP creado **una vez**, reutilizado
- [ ] Retries con límite duro (4–5) y presupuesto de tiempo total
- [ ] Backoff exponencial **con jitter**
- [ ] `Retry-After` respetado cuando está presente
- [ ] Errores 4xx no reintentables fallan inmediatamente
- [ ] Rate limiter cliente por debajo del límite del proveedor
- [ ] Logs en cada reintento (para detectar el próximo storm)
- [ ] Sin retries anidados (SDK + tu wrapper)

¿Estás llamando desde un solo proceso o tienes varios workers en paralelo? Si son varios, el token bucket local no alcanza y hay que coordinar la cuota (típicamente con Redis) — te paso ese patrón si aplica.