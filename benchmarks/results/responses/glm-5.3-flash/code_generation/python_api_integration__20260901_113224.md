# GLM 5.3 Flash — code_generation/python_api_integration

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.0 | quality: 9.32
- latency_total: 288.783s | tokens_per_second: 48.4
- input_tokens: 113 | output_tokens: 13985
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Escribe una funcion Python que:
1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5. Incluya retry con backoff exponencial (max 3 intentos)

Usa httpx y no dependencias externas adicionales.


## Respuesta completa

```python
import random
import time

import httpx

API_URL = "https://api.example.com/products"
TIMEOUT = 10.0        # segundos por intento
MAX_ATTEMPTS = 3      # intentos totales (1 inicial + 2 reintentos)
BASE_DELAY = 1.0      # delay inicial del backoff (segundos)


def fetch_expensive_products(token: str, min_price: float = 100.0) -> list[dict]:
    """
    GET a la API de productos con Bearer token y retorna {id, name, price}
    de los productos con precio > min_price.

    - Timeout de 10 s por intento.
    - Hasta 3 intentos con backoff exponencial (~1s, ~2s) ante errores
      de red, timeouts y respuestas 5xx/429.
    - Los 4xx (401, 403, 404...) fallan de inmediato: reintentar no cambia nada.

    Raises:
        httpx.HTTPError: si se agotan los reintentos o hay un 4xx no reintentable.
    """
    headers = {"Authorization": f"Bearer {token}"}
    products: list[dict] = []

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with httpx.Client(timeout=TIMEOUT) as client:
                resp = client.get(API_URL, headers=headers)
                resp.raise_for_status()
                products = resp.json()
            break  # éxito
        except httpx.TransportError as exc:  # timeout, DNS, conexión rechazada...
            _retry_or_raise(attempt, exc)
        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            if status < 500 and status != 429:
                raise  # 4xx (salvo 429): no tiene sentido reintentar
            _retry_or_raise(attempt, exc)

    return [
        {"id": p["id"], "name": p["name"], "price": p["price"]}
        for p in products
        if p.get("price", 0) > min_price
    ]


def _retry_or_raise(attempt: int, exc: httpx.HTTPError) -> None:
    """Espera con backoff exponencial (+jitter) o relanza si no quedan intentos."""
    if attempt >= MAX_ATTEMPTS:
        raise exc
    delay = BASE_DELAY * 2 ** (attempt - 1)       # intento 1 → 1s, intento 2 → 2s
    time.sleep(delay * random.uniform(1.0, 1.5))  # jitter: evita reintentos sincronizados


if __name__ == "__main__":
    import os

    productos = fetch_expensive_products(os.environ["API_TOKEN"])
    print(productos)
```

**Notas:**

- **3 intentos totales** (1 inicial + 2 reintentos), con esperas de ~1s y ~2s. Si "max 3 intentos" para ti significa 3 reintentos *adicionales*, cambia `MAX_ATTEMPTS = 4`.
- **Timeout**: `timeout=10.0` aplica a conexión, lectura, escritura y pool, no solo a la respuesta.
- **Supuesto**: la API devuelve una lista JSON directa y cada item tiene `id`, `name` y `price` numérico. Si los datos vienen envueltos (`{"products": [...]}`), usa `resp.json()["products"]`.
- **5xx y 429 sí se reintentan** (suelen ser transitorios); el resto de 4xx no, porque reintentar no los corrige. Si solo quieres reintentar errores de red/timeout, elimina el bloque `except httpx.HTTPStatusError`.
- **¿Versión async?** Declara la función `async def`, usa `httpx.AsyncClient` (con `async with`), `await client.get(...)` y `await asyncio.sleep(...)` en lugar de `time.sleep`.