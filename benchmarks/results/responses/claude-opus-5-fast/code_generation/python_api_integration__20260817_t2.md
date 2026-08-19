# Claude Opus 5 Fast — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.8 | quality: 9.8
- latency_total: 17.866s | tokens_per_second: 293.1
- input_tokens: 154 | output_tokens: 5237
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una implementación detallada que cumple con todos los requisitos.

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

# Cliente de productos con httpx

```python
"""
Cliente mínimo para el catálogo de productos.
Solo requiere: httpx (y stdlib).
"""

from __future__ import annotations

import logging
import random
import time
from typing import Any, TypedDict

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
DEFAULT_TIMEOUT = 10.0          # segundos (conexión + lectura + escritura + pool)
MAX_ATTEMPTS = 3                # intentos totales, no reintentos extra
BACKOFF_BASE = 1.0              # 1s, 2s, 4s...
BACKOFF_FACTOR = 2.0
MAX_BACKOFF = 30.0
RETRYABLE_STATUS = {408, 425, 429, 500, 502, 503, 504}


class Product(TypedDict):
    id: Any
    name: str
    price: float


class ProductFetchError(RuntimeError):
    """Fallo irrecuperable al obtener el catálogo (tras agotar reintentos)."""


# --------------------------------------------------------------------------- #
# Helpers privados
# --------------------------------------------------------------------------- #
def _backoff_delay(attempt: int, retry_after: float | None = None) -> float:
    """Backoff exponencial con jitter. `attempt` empieza en 1."""
    if retry_after is not None:
        return min(retry_after, MAX_BACKOFF)
    delay = min(BACKOFF_BASE * (BACKOFF_FACTOR ** (attempt - 1)), MAX_BACKOFF)
    return delay + random.uniform(0, delay * 0.25)  # jitter para evitar thundering herd


def _parse_retry_after(response: httpx.Response) -> float | None:
    """Respeta el header Retry-After si viene en formato de segundos."""
    raw = response.headers.get("Retry-After")
    try:
        return float(raw) if raw is not None else None
    except ValueError:
        return None  # formato HTTP-date: lo ignoramos y usamos backoff normal


def _normalize(payload: Any, min_price: float) -> list[Product]:
    """Filtra por precio y proyecta solo los campos requeridos."""
    if isinstance(payload, list):
        items = payload
    elif isinstance(payload, dict):
        items = payload.get("data") or payload.get("products") or payload.get("items") or []
    else:
        raise ProductFetchError(f"Formato de respuesta inesperado: {type(payload).__name__}")

    if not isinstance(items, list):
        raise ProductFetchError("El campo de productos no es una lista")

    result: list[Product] = []
    for raw in items:
        if not isinstance(raw, dict):
            continue
        try:
            price = float(raw["price"])
        except (KeyError, TypeError, ValueError):
            logger.warning("Producto descartado por precio inválido: %r", raw.get("id", raw))
            continue

        if price > min_price:
            result.append({"id": raw.get("id"), "name": raw.get("name"), "price": price})

    return result


# --------------------------------------------------------------------------- #
# API pública
# --------------------------------------------------------------------------- #
def fetch_expensive_products(
    token: str,
    *,
    min_price: float = 100.0,
    url: str = API_URL,
    timeout: float = DEFAULT_TIMEOUT,
    max_attempts: int = MAX_ATTEMPTS,
    client: httpx.Client | None = None,
) -> list[Product]:
    """
    Obtiene los productos con precio > `min_price`.

    Args:
        token: Bearer token de autenticación.
        min_price: Umbral exclusivo de precio.
        client: Cliente httpx reutilizable (recomendado en producción).

    Returns:
        Lista de dicts {id, name, price}.

    Raises:
        ProductFetchError: red caída, timeout, 5xx persistente o 4xx no recuperable.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    owns_client = client is None
    http = client or httpx.Client(timeout=httpx.Timeout(timeout))

    try:
        last_error: Exception | None = None

        for attempt in range(1, max_attempts + 1):
            retry_after: float | None = None
            try:
                response = http.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()
                return _normalize(response.json(), min_price)

            except httpx.TimeoutException as exc:
                last_error = exc
                logger.warning("Timeout (%ss) en intento %d/%d", timeout, attempt, max_attempts)

            except httpx.RequestError as exc:  # DNS, conexión, TLS, protocolo...
                last_error = exc
                logger.warning("Error de red en intento %d/%d: %s", attempt, max_attempts, exc)

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                last_error = exc
                if status not in RETRYABLE_STATUS:
                    # 401/403/404/422: reintentar no arregla nada, cortamos ya.
                    raise ProductFetchError(
                        f"HTTP {status} no recuperable: {exc.response.text[:200]}"
                    ) from exc
                retry_after = _parse_retry_after(exc.response)
                logger.warning("HTTP %d en intento %d/%d", status, attempt, max_attempts)

            except ValueError as exc:  # JSON inválido
                raise ProductFetchError("La respuesta no es JSON válido") from exc

            if attempt < max_attempts:
                delay = _backoff_delay(attempt, retry_after)
                logger.info("Reintentando en %.2fs...", delay)
                time.sleep(delay)

        raise ProductFetchError(
            f"No se pudo obtener el catálogo tras {max_attempts} intentos"
        ) from last_error

    finally:
        if owns_client:
            http.close()
```

## Versión async (mismo comportamiento)

```python
import asyncio


async def fetch_expensive_products_async(
    token: str,
    *,
    min_price: float = 100.0,
    url: str = API_URL,
    timeout: float = DEFAULT_TIMEOUT,
    max_attempts: int = MAX_ATTEMPTS,
    client: httpx.AsyncClient | None = None,
) -> list[Product]:
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    owns_client = client is None
    http = client or httpx.AsyncClient(timeout=httpx.Timeout(timeout))

    try:
        last_error: Exception | None = None

        for attempt in range(1, max_attempts + 1):
            retry_after: float | None = None
            try:
                response = await http.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()
                return _normalize(response.json(), min_price)

            except httpx.TimeoutException as exc:
                last_error = exc
                logger.warning("Timeout en intento %d/%d", attempt, max_attempts)

            except httpx.RequestError as exc:
                last_error = exc
                logger.warning("Error de red en intento %d/%d: %s", attempt, max_attempts, exc)

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                last_error = exc
                if status not in RETRYABLE_STATUS:
                    raise ProductFetchError(f"HTTP {status} no recuperable") from exc
                retry_after = _parse_retry_after(exc.response)

            except ValueError as exc:
                raise ProductFetchError("La respuesta no es JSON válido") from exc

            if attempt < max_attempts:
                await asyncio.sleep(_backoff_delay(attempt, retry_after))

        raise ProductFetchError(
            f"No se pudo obtener el catálogo tras {max_attempts} intentos"
        ) from last_error

    finally:
        if owns_client:
            await http.aclose()
```

## Uso

```python
import logging, os

logging.basicConfig(level=logging.INFO)

try:
    productos = fetch_expensive_products(os.environ["API_TOKEN"])
    for p in productos:
        print(f"{p['id']:>6} | {p['name']:<30} | {p['price']:.2f}")
except ProductFetchError as e:
    logging.error("Fallo al consultar productos: %s", e)
```

**Reutilizando cliente** (mejor rendimiento: pool de conexiones + keep-alive):

```python
with httpx.Client(timeout=httpx.Timeout(10.0)) as c:
    a = fetch_expensive_products(token, client=c)
    b = fetch_expensive_products(token, client=c, min_price=500)
```

## Decisiones de diseño

| Punto | Criterio |
|---|---|
| **Reintentos selectivos** | Solo 408/425/429/5xx y errores de transporte. Un 401 o 404 no mejora reintentando: falla rápido. |
| **Jitter** | 25% aleatorio sobre el delay para evitar que N clientes reintenten sincronizados. |
| **`Retry-After`** | Si el servidor indica cuánto esperar (típico en 429), se respeta por encima del backoff calculado. |
| **`max_attempts` = intentos totales** | 3 intentos → esperas de ~1s y ~2s. Peor caso ≈ 33s (3×10s timeout + 3s backoff). |
| **Inyección de cliente** | Permite reutilizar el pool y facilita testear con `httpx.MockTransport`. |
| **Parseo tolerante** | Un producto con `price` corrupto se descarta y se loguea, en vez de tumbar toda la llamada. |
| **`raise ... from exc`** | Se conserva la causa original en el traceback. |

## Test rápido sin red

```python
def test_filtra_y_proyecta():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["Authorization"] == "Bearer tok"
        return httpx.Response(200, json=[
            {"id": 1, "name": "Barato", "price": 50, "stock": 3},
            {"id": 2, "name": "Caro",   "price": 150.5, "stock": 1},
            {"id": 3, "name": "Justo",  "price": 100},      # excluido: no es > 100
        ])

    with httpx.Client(transport=httpx.MockTransport(handler)) as c:
        assert fetch_expensive_products("tok", client=c) == [
            {"id": 2, "name": "Caro", "price": 150.5}
        ]
```