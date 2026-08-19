# GPT-5.6 Luna — multi_turn/debugging_conversation

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.4 | quality: 9.55
- latency_total: 6.76s | tokens_per_second: 172.8
- input_tokens: 312 | output_tokens: 1168
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en estrategias de manejo de errores HTTP, proporcionando un ejemplo de código detallado y útil para un emprendedor.

## Respuesta completa

El problema principal es que el retry infinito convierte un error puntual en una avalancha de solicitudes. Implementa estas reglas:

- Máximo de intentos, por ejemplo 3–5.
- Backoff exponencial.
- Jitter aleatorio para evitar que varias tareas reintenten a la vez.
- Respetar `Retry-After` si OpenRouter lo envía.
- Timeout total por solicitud.
- No reintentar errores permanentes, como saldo insuficiente o una API key inválida.

Una espera típica sería:

```text
1.º retry: 1–2 s
2.º retry: 2–4 s
3.º retry: 4–8 s
4.º retry: 8–16 s
```

### Ejemplo en Python con `requests`

```python
import random
import time
import requests

MAX_RETRIES = 4
BASE_DELAY = 1.0
MAX_DELAY = 30.0

def call_openrouter(payload, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=(10, 90),  # conexión, lectura
            )

            if response.status_code < 400:
                return response.json()

            # No tiene sentido reintentar estos errores automáticamente
            if response.status_code in (400, 401, 403, 404):
                raise RuntimeError(
                    f"Error permanente {response.status_code}: {response.text}"
                )

            # Reintentar 429 y errores temporales del servidor
            retryable = response.status_code == 429 or response.status_code >= 500

            if not retryable:
                raise RuntimeError(
                    f"Error HTTP {response.status_code}: {response.text}"
                )

            if attempt == MAX_RETRIES:
                raise RuntimeError(
                    f"Se agotaron los reintentos. "
                    f"HTTP {response.status_code}: {response.text}"
                )

            retry_after = response.headers.get("Retry-After")

            if retry_after:
                try:
                    delay = float(retry_after)
                except ValueError:
                    delay = BASE_DELAY * (2 ** attempt)
            else:
                # Exponential backoff + jitter
                exponential = BASE_DELAY * (2 ** attempt)
                delay = min(MAX_DELAY, exponential)
                delay = random.uniform(delay * 0.5, delay * 1.5)

            print(
                f"Solicitud temporalmente rechazada "
                f"(HTTP {response.status_code}). "
                f"Reintento {attempt + 1}/{MAX_RETRIES} "
                f"en {delay:.1f}s"
            )

            time.sleep(delay)

        except requests.Timeout:
            if attempt == MAX_RETRIES:
                raise

            delay = random.uniform(
                0.5 * BASE_DELAY * (2 ** attempt),
                1.5 * BASE_DELAY * (2 ** attempt),
            )
            delay = min(delay, MAX_DELAY)
            time.sleep(delay)

        except requests.RequestException:
            if attempt == MAX_RETRIES:
                raise

            delay = min(MAX_DELAY, BASE_DELAY * (2 ** attempt))
            time.sleep(random.uniform(delay * 0.5, delay * 1.5))
```

### Importante en tu caso

Como ya generaste muchos 429, primero elimina o corrige el loop infinito y espera unos segundos antes de volver a probar. Además, revisa el cuerpo de la respuesta:

```python
print(response.status_code)
print(response.headers)
print(response.text)
```

Un `429` puede significar dos cosas distintas:

1. **Límite temporal de solicitudes**: se soluciona esperando y aplicando backoff.
2. **Cuota, crédito o límite del proveedor/modelo**: reintentar no lo solucionará; debes revisar el mensaje de error, el saldo, el modelo y los límites de OpenRouter.

### Si tienes varias solicitudes concurrentes

Los retries no sustituyen un limitador de concurrencia. Usa un semáforo para evitar que muchas tareas disparen llamadas al mismo tiempo:

```python
import asyncio

semaphore = asyncio.Semaphore(2)

async def limited_call(client, payload):
    async with semaphore:
        return await call_with_retries(client, payload)
```

Y evita este patrón:

```python
while True:
    try:
        return make_request()
    except Exception:
        continue
```

Sustitúyelo por un número limitado de intentos y, al agotarlos, registra el error y devuélvelo al sistema para que pueda decidir si lo pone en una cola, lo marca como fallido o usa otro modelo.