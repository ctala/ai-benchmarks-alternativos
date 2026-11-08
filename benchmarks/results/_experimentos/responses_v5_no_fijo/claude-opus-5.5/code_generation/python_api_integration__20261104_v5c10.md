# Claude Opus 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.89 | quality: 9.52
- latency_total: 24.221s | tokens_per_second: 125.9
- input_tokens: 156 | output_tokens: 3049
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

# Cliente de productos con httpx, retry y backoff exponencial

```python
"""
Cliente para obtener productos filtrados por precio desde la API.
Requiere solo: httpx (pip install httpx)
"""

import logging
import random
import time
from typing import Any

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10.0
MAX_ATTEMPTS = 3
BASE_BACKOFF_SECONDS = 1.0
PRICE_THRESHOLD = 100

# Códigos HTTP transitorios que vale la pena reintentar
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


class ProductFetchError(Exception):
    """Error al obtener productos de la API."""


def _calculate_backoff(attempt: int) -> float:
    """Backoff exponencial con jitter: ~1s, ~2s, ~4s..."""
    delay = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
    jitter = random.uniform(0, delay * 0.1)
    return delay + jitter


def _extract_products(payload: Any) -> list[dict]:
    """Acepta una lista directa o un objeto tipo {"products": [...]}."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("products", "data", "items", "results"):
            if isinstance(payload.get(key), list):
                return payload[key]
    raise ProductFetchError(f"Formato de respuesta inesperado: {type(payload).__name__}")


def _parse_price(value: Any) -> float | None:
    """Convierte el precio a float; devuelve None si no es válido."""
    if isinstance(value, bool):  # bool es subclase de int, lo excluimos
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def get_expensive_products(
    token: str,
    min_price: float = PRICE_THRESHOLD,
    url: str = API_URL,
) -> list[dict]:
    """
    Obtiene productos con precio > min_price.

    Args:
        token: Bearer token de autenticación.
        min_price: Umbral de precio (exclusivo). Por defecto 100.
        url: Endpoint de la API.

    Returns:
        Lista de dicts con las claves {id, name, price}.

    Raises:
        ProductFetchError: si fallan todos los intentos, hay un error
            no recuperable (p. ej. 401/404) o la respuesta es inválida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    timeout = httpx.Timeout(TIMEOUT_SECONDS)
    last_error: Exception | None = None

    with httpx.Client(timeout=timeout, headers=headers) as client:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = client.get(url)

                # Errores transitorios del servidor -> reintentar
                if response.status_code in RETRYABLE_STATUS_CODES:
                    raise httpx.HTTPStatusError(
                        f"Estado reintentable {response.status_code}",
                        request=response.request,
                        response=response,
                    )

                # Otros errores 4xx/5xx -> fallo inmediato sin reintento
                response.raise_for_status()
                payload = response.json()
                break  # éxito

            except httpx.TimeoutException as exc:
                last_error = exc
                logger.warning("Intento %d/%d: timeout (%ss)", attempt, MAX_ATTEMPTS, TIMEOUT_SECONDS)

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                if status not in RETRYABLE_STATUS_CODES:
                    raise ProductFetchError(
                        f"Error HTTP no recuperable {status}: {exc.response.text[:200]}"
                    ) from exc
                last_error = exc
                logger.warning("Intento %d/%d: HTTP %d", attempt, MAX_ATTEMPTS, status)

            except httpx.RequestError as exc:
                # Errores de red: DNS, conexión rechazada, SSL, etc.
                last_error = exc
                logger.warning("Intento %d/%d: error de red: %s", attempt, MAX_ATTEMPTS, exc)

            except ValueError as exc:
                # JSON inválido: no tiene sentido reintentar
                raise ProductFetchError("La respuesta no es JSON válido") from exc

            if attempt < MAX_ATTEMPTS:
                delay = _calculate_backoff(attempt)
                logger.info("Reintentando en %.2fs...", delay)
                time.sleep(delay)
        else:
            # El bucle terminó sin 'break': se agotaron los intentos
            raise ProductFetchError(
                f"Fallaron los {MAX_ATTEMPTS} intentos. Último error: {last_error}"
            ) from last_error

    products = _extract_products(payload)

    result: list[dict] = []
    for product in products:
        if not isinstance(product, dict):
            continue
        price = _parse_price(product.get("price"))
        if price is not None and price > min_price:
            result.append({
                "id": product.get("id"),
                "name": product.get("name"),
                "price": price,
            })

    return result


# ---------------------------------------------------------------------------
# Ejemplo de uso
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import os

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        items = get_expensive_products(token=os.environ["API_TOKEN"])
        print(f"{len(items)} productos con precio > {PRICE_THRESHOLD}:")
        for item in items:
            print(item)
    except KeyError:
        print("Define la variable de entorno API_TOKEN")
    except ProductFetchError as e:
        print(f"Error: {e}")
```

## Decisiones de diseño

| Aspecto | Comportamiento |
|---|---|
| **Timeout** | 10 s aplicado a conexión, lectura, escritura y pool. |
| **Reintentos** | Máximo 3 intentos en total, con esperas de ~1 s y ~2 s entre ellos. |
| **Jitter** | Añade un 10 % aleatorio para evitar que muchos clientes reintenten a la vez. |
| **Qué se reintenta** | Timeouts, errores de red, 429 y 5xx transitorios (500, 502, 503, 504). |
| **Qué NO se reintenta** | 401, 403, 404 y otros 4xx, porque reintentar no los soluciona. Tampoco el JSON inválido. |
| **Precios robustos** | Acepta `"150.5"` (string) o `150`. Ignora valores nulos o inválidos. |
| **Formato flexible** | Acepta `[...]` o `{"products": [...]}`, `{"data": [...]}`, etc. |

## Test rápido sin red

Puedes probarla usando `httpx.MockTransport`, que viene incluido en httpx:

```python
def test_filtrado():
    def handler(request):
        assert request.headers["Authorization"] == "Bearer abc"
        return httpx.Response(200, json=[
            {"id": 1, "name": "A", "price": 50, "stock": 3},
            {"id": 2, "name": "B", "price": 150, "stock": 1},
            {"id": 3, "name": "C", "price": "200.5"},
        ])

    original = httpx.Client
    httpx.Client = lambda **kw: original(transport=httpx.MockTransport(handler), **kw)
    try:
        assert get_expensive_products("abc") == [
            {"id": 2, "name": "B", "price": 150.0},
            {"id": 3, "name": "C", "price": 200.5},
        ]
    finally:
        httpx.Client = original
```

Si necesitas una versión asíncrona, el cambio es directo: usa `httpx.AsyncClient`, `await client.get(...)` y `await asyncio.sleep(delay)`.