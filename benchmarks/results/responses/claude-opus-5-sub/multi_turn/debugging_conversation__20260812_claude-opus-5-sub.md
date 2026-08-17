# Claude Opus 5 (suscripción) — multi_turn/debugging_conversation

- model_id: `claude-opus-5`
- success: True  | final: 7.99 | quality: 10.0
- latency_total: 60.075s | tokens_per_second: 62.1
- input_tokens: 2 | output_tokens: 3732

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

Buen hallazgo — ese loop es exactamente lo que convierte un problema chico (un 429 aislado) en un bloqueo total. Vamos por partes.

## Primero: apaga el fuego

Antes de tocar el código, mata el proceso y espera unos minutos. Un cliente que dispara ~100 requests por cada fallo puede dejarte con throttling más agresivo del normal (algunos proveedores endurecen la ventana cuando detectan abuso). No sigas probando "a ver si ya se arregló" — eso alimenta el mismo ciclo.

## Las 4 reglas de un retry correcto

1. **Acotado.** Máximo 4-5 intentos. Nunca `while True`.
2. **Con backoff exponencial + jitter.** Sin jitter, si tienes N workers todos reintentan en el mismo instante y recreas el pico.
3. **Selectivo.** Solo reintentas errores transitorios: `429`, `500`, `502`, `503`, `504`, timeouts y errores de conexión. Un `400`, `401`, `403` o `404` no se arregla insistiendo — falla rápido y ruidoso.
4. **Respeta `Retry-After`.** Si el servidor te dice cuánto esperar, esa cifra manda por sobre tu cálculo.

## Implementación

```python
import random
import time
import httpx

RETRYABLE_STATUS = {408, 409, 429, 500, 502, 503, 504}
MAX_ATTEMPTS = 5
BASE_DELAY = 1.0    # segundos
MAX_DELAY = 60.0    # techo por espera

def _delay_for(attempt: int, response: httpx.Response | None) -> float:
    # 1) El servidor manda
    if response is not None:
        retry_after = response.headers.get("retry-after")
        if retry_after:
            try:
                return min(float(retry_after), MAX_DELAY)
            except ValueError:
                pass
    # 2) Full jitter: uniform(0, 2^n) evita el thundering herd
    ceiling = min(MAX_DELAY, BASE_DELAY * (2 ** attempt))
    return random.uniform(0, ceiling)

def call_with_retry(client: httpx.Client, payload: dict) -> dict:
    last_error = None
    last_response = None

    for attempt in range(MAX_ATTEMPTS):
        try:
            resp = client.post("/chat/completions", json=payload)

            if resp.status_code not in RETRYABLE_STATUS:
                resp.raise_for_status()   # 4xx no transitorio: revienta acá
                return resp.json()

            last_response = resp
            last_error = f"HTTP {resp.status_code}"

        except (httpx.TimeoutException, httpx.ConnectError, httpx.ReadError) as e:
            last_response = None
            last_error = repr(e)

        if attempt == MAX_ATTEMPTS - 1:
            break

        wait = _delay_for(attempt, last_response)
        print(f"[retry {attempt + 1}/{MAX_ATTEMPTS}] {last_error} — espero {wait:.1f}s")
        time.sleep(wait)

    raise RuntimeError(f"Falló tras {MAX_ATTEMPTS} intentos. Último error: {last_error}")
```

Con estos parámetros el peor caso son ~5 requests y ~1 minuto de espera total. Antes eran cientos e infinito.

## Trampa clásica: retries anidados

Revisa que no tengas **dos capas de retry multiplicándose**. Es el error más común después de arreglar el loop:

```python
# httpx con transport retries + tu propio wrapper = 3 × 5 = 15 requests reales
transport = httpx.HTTPTransport(retries=3)
```

Lo mismo con el SDK de OpenAI, que trae `max_retries=2` por defecto. Si lo usas para hablarle a OpenRouter, ponlo en `0` y deja que tu capa maneje la política:

```python
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=..., max_retries=0)
```

Elige **una** capa que reintente. Nunca dos.

## Si prefieres librería

`tenacity` te da lo mismo declarativo:

```python
from tenacity import retry, stop_after_attempt, wait_random_exponential, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),
    wait=wait_random_exponential(multiplier=1, max=60),
    retry=retry_if_exception_type((httpx.TimeoutException, RateLimitError)),
    reraise=True,
)
def call(...):
    ...
```

Solo cuidado: por defecto no lee `Retry-After`, tienes que inyectarlo con un `wait` custom.

## El arreglo de fondo: no llegar al 429

El retry es red de seguridad, no estrategia. Si estás corriendo lotes, pon un límite de concurrencia del lado del cliente y así el 429 casi nunca aparece:

```python
import threading
sem = threading.Semaphore(4)   # máx 4 requests en vuelo

with sem:
    call_with_retry(client, payload)
```

## Verifica qué te está limitando de verdad

Con 5 req/min y saldo pagado, el límite de OpenRouter no debería ser el problema. Cuando vuelvas a ver un 429, mira estos headers antes de asumir:

```python
print({k: v for k, v in resp.headers.items() if "ratelimit" in k.lower()})
print(resp.text[:500])
```

Dos cosas que cambian el diagnóstico:

- **El 429 puede venir del proveedor upstream, no de OpenRouter.** DeepSeek en algunos endpoints tiene sus propias cuotas. El body del error suele decirlo. Si es eso, fuerza el ruteo a otro proveedor con `"provider": {"order": [...]}` o `"allow_fallbacks": true` en el payload.
- **Un `402` no es lo mismo que un `429`.** Si te quedaste sin créditos, ningún backoff lo arregla.

Un detalle que aplica a tu repo: esto va en `providers/adapters.py`, en el punto único donde ya manejas timeout. Si lo pones ahí, todos los proveedores heredan la misma política y no terminas con tres implementaciones distintas de retry conviviendo.

Un último apunte, y es el que más te va a servir a futuro: ese loop infinito existió durante días sin que nada gritara. Un contador de requests por corrida que falle ruidoso si supera lo esperado (digamos, 3× el número de tests) lo habría cazado en la primera ejecución. La regla sin instrumento que la haga cumplir es una regla ya rota.

¿Quieres que revisemos el código donde está el loop para adaptarlo directo?