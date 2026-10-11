# Claude Opus 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.85 | quality: 9.52
- latency_total: 31.263s | tokens_per_second: 119.5
- input_tokens: 156 | output_tokens: 3735
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

# Función para obtener productos con precio > 100

```python
import logging
import random
import time
from typing import Any, TypedDict

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10.0
MAX_ATTEMPTS = 3
BACKOFF_BASE_SECONDS = 1.0
MIN_PRICE = 100.0

# Códigos HTTP transitorios en los que tiene sentido reintentar
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


class Product(TypedDict):
    id: Any
    name: str
    price: float


class ProductFetchError(Exception):
    """Error al obtener o procesar los productos de la API."""


def _backoff_delay(attempt: int) -> float:
    """Backoff exponencial con jitter: ~1s, ~2s, ~4s..."""
    delay = BACKOFF_BASE_SECONDS * (2 ** (attempt - 1))
    return delay + random.uniform(0, delay * 0.1)


def _extract_items(payload: Any) -> list[dict]:
    """Admite una lista directa o un objeto tipo {"products": [...]}."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("products", "data", "items"):
            if isinstance(payload.get(key), list):
                return payload[key]
    raise ProductFetchError("Formato de respuesta inesperado")


def _to_float(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _filter_products(items: list[dict], min_price: float) -> list[Product]:
    result: list[Product] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        price = _to_float(item.get("price"))
        if price is None or price <= min_price:
            continue
        result.append({"id": item.get("id"), "name": item.get("name"), "price": price})
    return result


def fetch_expensive_products(
    token: str,
    *,
    url: str = API_URL,
    min_price: float = MIN_PRICE,
    timeout: float = TIMEOUT_SECONDS,
    max_attempts: int = MAX_ATTEMPTS,
) -> list[Product]:
    """
    Obtiene los productos de la API y devuelve los que tienen price > min_price.

    Reintenta (hasta `max_attempts` intentos en total) con backoff exponencial
    ante timeouts, errores de red y respuestas HTTP 429/5xx.

    Raises:
        ProductFetchError: si la petición falla definitivamente o la
        respuesta no es válida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    last_error: Exception | None = None

    with httpx.Client(timeout=httpx.Timeout(timeout)) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url, headers=headers)
            except httpx.TimeoutException as exc:
                last_error, reason = exc, "timeout"
            except httpx.TransportError as exc:  # conexión, DNS, etc.
                last_error, reason = exc, f"error de red ({exc.__class__.__name__})"
            else:
                status = response.status_code

                if status in RETRYABLE_STATUS_CODES:
                    last_error = httpx.HTTPStatusError(
                        f"HTTP {status}", request=response.request, response=response
                    )
                    reason = f"HTTP {status}"
                elif response.is_error:
                    # 4xx no transitorios (401, 403, 404...): no tiene sentido reintentar
                    raise ProductFetchError(
                        f"HTTP {status}: {response.text[:200]}"
                    )
                else:
                    try:
                        payload = response.json()
                    except ValueError as exc:
                        raise ProductFetchError("La respuesta no es JSON válido") from exc
                    return _filter_products(_extract_items(payload), min_price)

            if attempt < max_attempts:
                delay = _backoff_delay(attempt)
                logger.warning(
                    "Intento %d/%d fallido (%s). Reintentando en %.2fs...",
                    attempt, max_attempts, reason, delay,
                )
                time.sleep(delay)
            else:
                logger.error("Intento %d/%d fallido (%s).", attempt, max_attempts, reason)

    raise ProductFetchError(
        f"No se pudieron obtener los productos tras {max_attempts} intentos"
    ) from last_error
```

## Ejemplo de uso

```python
import os

logging.basicConfig(level=logging.INFO)

try:
    products = fetch_expensive_products(os.environ["API_TOKEN"])
    for p in products:
        print(f"{p['id']}: {p['name']} - ${p['price']:.2f}")
except ProductFetchError as e:
    print(f"Error: {e}")
```

## Decisiones de diseño

| Aspecto | Comportamiento |
|---|---|
| **Timeout** | 10 s aplicado a conexión, lectura, escritura y pool (`httpx.Timeout`). |
| **Reintentos** | 3 intentos en total, con esperas de ~1 s y ~2 s entre ellos. |
| **Jitter** | Añade hasta un 10 % aleatorio a cada espera para evitar que muchos clientes reintenten a la vez. |
| **Qué se reintenta** | Timeouts, errores de red (`TransportError`) y HTTP 429/500/502/503/504. |
| **Qué NO se reintenta** | 401, 403, 404 y otros 4xx, porque son errores permanentes y reintentar no los arregla. |
| **Datos robustos** | Ignora productos sin precio o con precio no numérico, y convierte precios en string como `"150.5"`. |
| **Formato flexible** | Acepta una lista directa o una respuesta envuelta en `products`, `data` o `items`. |
| **Errores** | Lanza una excepción propia (`ProductFetchError`) que conserva la causa original en `__cause__`. |

**Nota:** el filtro es estrictamente `> 100`, así que un producto con precio exactamente 100 se excluye.