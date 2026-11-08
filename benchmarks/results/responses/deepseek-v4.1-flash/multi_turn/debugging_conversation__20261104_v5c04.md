# DeepSeek V4.1 Flash — multi_turn/debugging_conversation

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 22.236s | tokens_per_second: 109.1
- input_tokens: 359 | output_tokens: 2426

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

Perfecto, eso explica todo. Un loop de retry sin backoff es un amplificador: 5 req/min se convierten en 500. Y hay un detalle que probablemente agravó el problema: **el SDK de OpenAI (que OpenRouter usa como base) ya reintenta 429 por su cuenta** (`max_retries=2` por defecto). Si tenías tu loop *encima* del SDK, cada intento tuyo generaba 3 requests reales.

## Reglas para un retry correcto

1. **Nunca reintentar sin esperar.** Sin delay, el retry es un DoS autoinfligido.
2. **Backoff exponencial con jitter** (full jitter, para que no se sincronicen tus workers).
3. **Respetar `Retry-After`** y `x-ratelimit-reset` si vienen en la respuesta. OpenRouter los manda.
4. **Máximo de intentos** (3-5) y **presupuesto total de tiempo** (deadline).
5. **Solo reintentar errores transitorios**: 429, 500, 502, 503, 504, timeouts y errores de conexión. Nunca 400/401/403/404/422 — esos no se arreglan solos, y reintentarlos es puro desperdicio.
6. **No apilar retries**: o lo hace el SDK o lo haces tú, no ambos.

## Implementación

```python
import random, time
from openai import OpenAI, APIStatusError, APIConnectionError, APITimeoutError

# Desactiva los retries del SDK para no multiplicar
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="...",
    max_retries=0,
)

MAX_ATTEMPTS = 5
BASE_DELAY   = 1.0    # segundos
MAX_DELAY    = 30.0
DEADLINE     = 60.0   # presupuesto total por llamada
RETRYABLE    = {429, 500, 502, 503, 504}


def _retry_after(resp):
    """Segundos a esperar, segun los headers del servidor."""
    if resp is None:
        return None
    if (v := resp.headers.get("retry-after")):
        try:
            return float(v)
        except ValueError:
            return None  # puede venir como fecha HTTP; simplificamos
    if (v := resp.headers.get("x-ratelimit-reset")):
        try:
            return max(0.0, float(v) - time.time())
        except ValueError:
            return None
    return None


def _delay(attempt, retry_after):
    if retry_after is not None:
        return min(retry_after, MAX_DELAY)
    ceiling = min(MAX_DELAY, BASE_DELAY * (2 ** attempt))
    return random.uniform(0, ceiling)   # full jitter


def call_with_retry(fn, *args, **kwargs):
    start = time.monotonic()
    last_exc = None

    for attempt in range(MAX_ATTEMPTS):
        try:
            return fn(*args, **kwargs)
        except APIStatusError as e:
            if e.status_code not in RETRYABLE:
                raise                      # 4xx no transitorio: falla ya
            last_exc = e
            wait = _delay(attempt, _retry_after(e.response))
        except (APIConnectionError, APITimeoutError) as e:
            last_exc = e
            wait = _delay(attempt, None)

        elapsed = time.monotonic() - start
        if elapsed + wait > DEADLINE:
            break
        print(f"[retry] attempt={attempt+1} status={getattr(last_exc,'status_code','?')} "
              f"waiting={wait:.2f}s")
        time.sleep(wait)

    raise last_exc
```

Uso:

```python
resp = call_with_retry(
    client.chat.completions.create,
    model="deepseek/deepseek-chat-v3",
    messages=[{"role": "user", "content": "hola"}],
)
```

Nota: pasas la función y los argumentos, **no** la request ya ejecutada — así el retry vuelve a construir y enviar la petición.

## Dos capas más que te convienen

**Limita la concurrencia en el cliente.** Aunque el retry esté bien, si lanzas 200 corrutinas a la vez vas a comer 429 igual. Un token bucket o semáforo es tu segunda línea de defensa:

```python
import asyncio
sem = asyncio.Semaphore(5)   # máx 5 requests en vuelo

async def guarded(...):
    async with sem:
        return await call_with_retry(...)
```

**Circuit breaker.** Si en 10 llamadas seguidas te comes 429, corta todo 30 segundos en vez de seguir golpeando. Es lo que te habría ahorrado el incidente completo.

## Un apunte sobre OpenRouter específicamente

A veces el 429 **no es tuyo**: es el provider upstream (DeepSeek) rate-limitándote a través de OpenRouter. El body del error lo indica en `error.metadata`. Si es ese caso, el retry ayuda poco y lo que sirve es habilitar fallbacks a otros providers:

```python
extra_body={"provider": {"allow_fallbacks": True, "sort": "throughput"}}
```

## Checklist para verificar el fix

- [ ] `max_retries=0` en el cliente, retries solo en tu wrapper
- [ ] Logueás cada reintento con intento + delay (te habría delatado el bug en 10 segundos)
- [ ] Tope de intentos y deadline total
- [ ] Solo reintentás status transitorios
- [ ] Concurrencia limitada en el cliente
- [ ] Probado con un mock que devuelve 429 siempre → debe terminar en ~30s, no en 100 requests