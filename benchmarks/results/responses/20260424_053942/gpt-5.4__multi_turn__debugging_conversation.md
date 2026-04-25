# GPT-5.4 — multi_turn/debugging_conversation

- model_id: `gpt-5.4`
- success: True  | final: 7.26 | quality: 8.46
- latency_total: 15.224s | tokens_per_second: 77.9
- input_tokens: 312 | output_tokens: 1186
- judge_score: 4.6 | justificación: 

## Respuesta completa

Sí: el problema no es tu cuota sino el bucle de reintentos. La forma correcta es:

## Qué hacer
- **No** reintentar infinitamente.
- Reintentar **solo** errores transitorios:
  - `429 Too Many Requests`
  - `500`, `502`, `503`, `504`
  - timeouts / errores de red
- Usar:
  - **máximo de intentos**
  - **backoff exponencial**
  - **jitter** aleatorio
  - respetar `Retry-After` si viene en la respuesta

## Regla práctica
Un buen patrón es:
- máximo `3` a `5` reintentos
- delay base `1s`
- backoff: `1s`, `2s`, `4s`, `8s`
- con jitter: sumar un valor aleatorio pequeño

## Pseudocódigo
```python
max_retries = 5
base_delay = 1.0

for attempt in range(max_retries + 1):
    try:
        response = call_api()

        if response.status_code < 400:
            return response

        if response.status_code not in [429, 500, 502, 503, 504]:
            raise Exception(f"Non-retryable error: {response.status_code}")

        if attempt == max_retries:
            raise Exception(f"Max retries exceeded: {response.status_code}")

        retry_after = response.headers.get("Retry-After")
        if retry_after:
            delay = float(retry_after)
        else:
            delay = base_delay * (2 ** attempt)
            jitter = random.uniform(0, 0.5 * delay)
            delay += jitter

        sleep(delay)

    except TimeoutError:
        if attempt == max_retries:
            raise
        delay = base_delay * (2 ** attempt)
        jitter = random.uniform(0, 0.5 * delay)
        sleep(delay + jitter)
```

## Ejemplo real en Python con `requests`
```python
import time
import random
import requests

RETRYABLE_STATUS = {429, 500, 502, 503, 504}

def call_openrouter_with_retry(url, headers, payload, max_retries=5, base_delay=1.0, timeout=60):
    last_error = None

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=timeout)

            if resp.status_code < 400:
                return resp

            if resp.status_code not in RETRYABLE_STATUS:
                # error definitivo, no reintentar
                resp.raise_for_status()

            if attempt == max_retries:
                resp.raise_for_status()

            retry_after = resp.headers.get("Retry-After")
            if retry_after is not None:
                try:
                    delay = float(retry_after)
                except ValueError:
                    delay = base_delay * (2 ** attempt)
            else:
                delay = base_delay * (2 ** attempt)

            jitter = random.uniform(0, delay * 0.25)
            delay = delay + jitter

            print(f"Retryable error {resp.status_code}. Retry in {delay:.2f}s (attempt {attempt+1}/{max_retries})")
            time.sleep(delay)

        except (requests.Timeout, requests.ConnectionError) as e:
            last_error = e

            if attempt == max_retries:
                raise

            delay = base_delay * (2 ** attempt)
            jitter = random.uniform(0, delay * 0.25)
            delay = delay + jitter

            print(f"Network error: {e}. Retry in {delay:.2f}s (attempt {attempt+1}/{max_retries})")
            time.sleep(delay)

    if last_error:
        raise last_error

    raise RuntimeError("Request failed after retries")
```

## Recomendaciones importantes
### 1. Pon un límite global de concurrencia
Aunque hagas pocas requests/min, si lanzas muchas a la vez puedes disparar 429.

Ejemplo:
- máximo 2–5 requests concurrentes al mismo tiempo

### 2. No reintentes errores 4xx normales
Por ejemplo:
- `400` bad request
- `401` unauthorized
- `403` forbidden
- `404`
Esos casi nunca se arreglan reintentando.

### 3. Loguea cada retry
Guarda:
- status code
- attempt number
- delay aplicado
- `Retry-After`
- request id si existe

Eso hace muy fácil depurar.

### 4. Usa timeout
Si no pones timeout, puedes dejar workers colgados.

## Patrón todavía mejor
Si quieres hacerlo más robusto:
- **circuit breaker**: si recibes muchos 429 seguidos, pausas 30–60s antes de seguir
- **cola**: en vez de disparar requests directamente, las encolas y un worker las procesa con rate limit

## Versión simple recomendada
Si quieres algo práctico y suficiente:
- `max_retries=4`
- `base_delay=1`
- retry solo en `429, 500, 502, 503, 504`
- respetar `Retry-After`
- jitter 10–25%
- cortar totalmente al llegar al máximo

Si quieres, te puedo escribir una implementación lista para pegar en:
- **Python**
- **Node.js / TypeScript**
- **fetch**
- **axios**
- **OpenAI/OpenRouter SDK**

Pásame el lenguaje que usas y te la adapto exacta a tu código.