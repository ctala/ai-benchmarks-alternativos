# Claude Opus 5 Fast — multi_turn/debugging_conversation

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.01 | quality: 10.0
- latency_total: 14.372s | tokens_per_second: 244.2
- input_tokens: 539 | output_tokens: 3510

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

Encontraste el problema real: un **retry storm**. Cada 429 genera 100 requests, que generan 100 más 429s... es una bomba exponencial que te auto-banea. Vamos con la solución correcta.

## Antes de tocar código

Detén el proceso y espera ~5-10 minutos. Muchos providers aplican penalizaciones extendidas cuando detectan patrones de abuso, así que aunque arregles el código, puede que sigas bloqueado un rato por el comportamiento previo.

## Los 5 principios de un retry correcto

| Principio | Por qué |
|---|---|
| **Límite duro de intentos** | Nunca `while True`. Máximo 3-5 intentos. |
| **Backoff exponencial** | 1s, 2s, 4s, 8s... da tiempo a que la ventana se resetee. |
| **Jitter (aleatoriedad)** | Sin él, todos tus workers reintentan en el mismo instante → thundering herd. |
| **Respetar `Retry-After`** | El servidor te dice exactamente cuánto esperar. Ignorarlo es pelear contra él. |
| **Solo reintentar lo reintentable** | Un 401 o 400 nunca se va a arreglar reintentando. |

## Implementación en Python

```python
import time
import random
import httpx

RETRYABLE_STATUS = {408, 409, 429, 500, 502, 503, 504}
MAX_ATTEMPTS = 5
BASE_DELAY = 1.0
MAX_DELAY = 60.0


class RateLimitError(Exception):
    pass


def calcular_espera(intento: int, response=None) -> float:
    """Prioriza el header del servidor; si no, backoff exponencial con jitter."""
    if response is not None:
        # 1) Retry-After (segundos o fecha HTTP)
        retry_after = response.headers.get("retry-after")
        if retry_after:
            try:
                return min(float(retry_after), MAX_DELAY)
            except ValueError:
                pass

        # 2) OpenRouter: X-RateLimit-Reset (timestamp Unix en ms)
        reset = response.headers.get("x-ratelimit-reset")
        if reset:
            try:
                espera = (int(reset) / 1000) - time.time()
                if espera > 0:
                    return min(espera + 0.5, MAX_DELAY)
            except ValueError:
                pass

    # 3) Backoff exponencial con "full jitter"
    tope = min(BASE_DELAY * (2 ** intento), MAX_DELAY)
    return random.uniform(0, tope)


def llamar_openrouter(client: httpx.Client, payload: dict) -> dict:
    ultimo_error = None

    for intento in range(MAX_ATTEMPTS):
        try:
            r = client.post("/chat/completions", json=payload, timeout=60.0)

            if r.status_code == 200:
                return r.json()

            # Errores permanentes: fallar rápido, no reintentar
            if r.status_code not in RETRYABLE_STATUS:
                raise RuntimeError(f"Error no reintentable {r.status_code}: {r.text}")

            ultimo_error = f"HTTP {r.status_code}"
            espera = calcular_espera(intento, r)

        except (httpx.TimeoutException, httpx.ConnectError) as e:
            ultimo_error = repr(e)
            espera = calcular_espera(intento)

        # No dormir después del último intento
        if intento < MAX_ATTEMPTS - 1:
            print(f"[retry {intento + 1}/{MAX_ATTEMPTS}] {ultimo_error} → espero {espera:.1f}s")
            time.sleep(espera)

    raise RateLimitError(f"Agotados {MAX_ATTEMPTS} intentos. Último error: {ultimo_error}")
```

Uso con cliente reutilizado (importante — no crees uno nuevo por request):

```python
client = httpx.Client(
    base_url="https://openrouter.ai/api/v1",
    headers={"Authorization": f"Bearer {API_KEY}"},
    limits=httpx.Limits(max_connections=10, max_keepalive_connections=5),
)

resultado = llamar_openrouter(client, {
    "model": "deepseek/deepseek-chat",
    "messages": [{"role": "user", "content": "hola"}],
})
```

## La pieza que falta: rate limiting preventivo

Los retries son la red de seguridad. Lo ideal es **no llegar al 429**. Un token bucket del lado cliente:

```python
import threading

class TokenBucket:
    def __init__(self, rate_per_sec: float, burst: int):
        self.rate = rate_per_sec
        self.capacity = burst
        self.tokens = float(burst)
        self.last = time.monotonic()
        self.lock = threading.Lock()

    def acquire(self):
        with self.lock:
            ahora = time.monotonic()
            self.tokens = min(self.capacity, self.tokens + (ahora - self.last) * self.rate)
            self.last = ahora

            if self.tokens < 1:
                espera = (1 - self.tokens) / self.rate
                time.sleep(espera)
                self.tokens = 0
                self.last = time.monotonic()
            else:
                self.tokens -= 1


# 4 req/s con ráfagas de hasta 8 → muy por debajo de los 300 RPM
bucket = TokenBucket(rate_per_sec=4, burst=8)

def llamar_con_limite(client, payload):
    bucket.acquire()
    return llamar_openrouter(client, payload)
```

## Alternativa: usar librerías probadas

Si prefieres no mantener esto tú mismo:

**Con `tenacity`:**
```python
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=1, max=60),
    retry=retry_if_exception_type(RateLimitError),
    reraise=True,
)
def mi_llamada():
    ...
```

**Con el SDK de OpenAI** (compatible con OpenRouter) — ya trae retries con backoff:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
    max_retries=3,   # por defecto son 2; NUNCA lo pongas alto
    timeout=60.0,
)
```

## Circuit breaker (si tienes volumen alto)

Si 429s consecutivos superan un umbral, deja de intentar del todo por N segundos en lugar de que cada request pelee por su cuenta:

```python
class CircuitBreaker:
    def __init__(self, umbral=5, cooldown=60):
        self.umbral = umbral
        self.cooldown = cooldown
        self.fallos = 0
        self.abierto_hasta = 0

    def permitir(self) -> bool:
        return time.monotonic() >= self.abierto_hasta

    def registrar_fallo(self):
        self.fallos += 1
        if self.fallos >= self.umbral:
            self.abierto_hasta = time.monotonic() + self.cooldown
            self.fallos = 0

    def registrar_exito(self):
        self.fallos = 0
```

## Checklist de verificación

- [ ] Eliminado el `while True` / recursión infinita
- [ ] `MAX_ATTEMPTS` ≤ 5
- [ ] Jitter aplicado (no backoff determinista)
- [ ] `Retry-After` / `X-RateLimit-Reset` respetados
- [ ] 4xx no reintentables fallan rápido
- [ ] Cliente HTTP reutilizado, no instanciado por request
- [ ] Logging de cada retry para detectar regresiones
- [ ] Rate limiter cliente por debajo del límite del provider

---

Una nota sobre **idempotencia**: si un request llega al servidor y se procesa, pero pierdes la respuesta por timeout, el retry te cobra los tokens dos veces. Para llamadas caras vale la pena loggear un ID de request y verificar antes de reintentar timeouts.

Si después de esto sigues viendo 429s, pásame los headers `x-ratelimit-*` de una respuesta y vemos si hay algo específico de tu cuenta o del modelo.