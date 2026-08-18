# Claude Opus 5 — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.61 | quality: 9.52
- latency_total: 47.818s | tokens_per_second: 97.4
- input_tokens: 154 | output_tokens: 4656
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

## Implementación

```python
"""
Cliente para obtener productos filtrados desde api.example.com.
Solo requiere httpx (el resto es stdlib).
"""

from __future__ import annotations

import logging
import random
import time
from typing import Any, Iterable

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"

TIMEOUT_SECONDS = 10.0
MAX_ATTEMPTS = 3
BACKOFF_BASE = 0.5          # segundos
BACKOFF_MAX = 8.0           # techo del sleep
RETRY_STATUS_CODES = frozenset({408, 429, 500, 502, 503, 504})


class ProductFetchError(RuntimeError):
    """Error no recuperable al consultar el catálogo de productos."""


def fetch_expensive_products(
    token: str,
    *,
    min_price: float = 100.0,
    url: str = API_URL,
    timeout: float = TIMEOUT_SECONDS,
    max_attempts: int = MAX_ATTEMPTS,
    client: httpx.Client | None = None,
) -> list[dict[str, Any]]:
    """
    Devuelve los productos con precio > `min_price` en formato
    [{"id": ..., "name": ..., "price": ...}, ...].

    Args:
        token: Bearer token de autenticación.
        min_price: umbral de precio (exclusivo).
        url: endpoint a consultar.
        timeout: timeout total por intento, en segundos.
        max_attempts: número máximo de intentos (incluye el primero).
        client: httpx.Client externo opcional (útil para tests o reuso de conexiones).

    Raises:
        ProductFetchError: si se agotan los reintentos o la respuesta es inválida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    owns_client = client is None
    client = client or httpx.Client(timeout=httpx.Timeout(timeout))

    try:
        payload = _request_with_retries(
            client=client,
            url=url,
            headers=headers,
            max_attempts=max_attempts,
        )
    finally:
        if owns_client:
            client.close()

    return _normalize(payload, min_price)


# ---------------------------------------------------------------------------
# Capa de red + retry
# ---------------------------------------------------------------------------

def _request_with_retries(
    *,
    client: httpx.Client,
    url: str,
    headers: dict[str, str],
    max_attempts: int,
) -> Any:
    last_error: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            response = client.get(url, headers=headers)

            if response.status_code in RETRY_STATUS_CODES:
                # Error transitorio del servidor -> reintentar
                raise httpx.HTTPStatusError(
                    f"Status transitorio {response.status_code}",
                    request=response.request,
                    response=response,
                )

            response.raise_for_status()  # 4xx definitivos -> no se reintentan

            try:
                return response.json()
            except ValueError as exc:
                raise ProductFetchError("La respuesta no es JSON válido") from exc

        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            if status not in RETRY_STATUS_CODES:
                # 401, 403, 404, 422... reintentar no sirve de nada.
                raise ProductFetchError(
                    f"Error HTTP {status}: {exc.response.text[:200]}"
                ) from exc
            last_error = exc
            logger.warning("Intento %d/%d falló con HTTP %s", attempt, max_attempts, status)

        except httpx.TimeoutException as exc:
            last_error = exc
            logger.warning("Intento %d/%d: timeout (%s)", attempt, max_attempts, exc)

        except httpx.TransportError as exc:
            # Cubre ConnectError, ReadError, RemoteProtocolError, ProxyError, etc.
            last_error = exc
            logger.warning("Intento %d/%d: error de red (%s)", attempt, max_attempts, exc)

        if attempt < max_attempts:
            time.sleep(_backoff_delay(attempt, exc=last_error))

    raise ProductFetchError(
        f"No se pudo obtener el catálogo tras {max_attempts} intentos: {last_error!r}"
    ) from last_error


def _backoff_delay(attempt: int, *, exc: Exception | None = None) -> float:
    """Backoff exponencial con jitter completo; respeta Retry-After si existe."""
    retry_after = _retry_after_seconds(exc)
    if retry_after is not None:
        return min(retry_after, BACKOFF_MAX)

    # attempt=1 -> ~0.5s, attempt=2 -> ~1s, attempt=3 -> ~2s (con jitter)
    ceiling = min(BACKOFF_BASE * (2 ** (attempt - 1)), BACKOFF_MAX)
    return random.uniform(0, ceiling)


def _retry_after_seconds(exc: Exception | None) -> float | None:
    if not isinstance(exc, httpx.HTTPStatusError):
        return None
    raw = exc.response.headers.get("Retry-After")
    try:
        return max(0.0, float(raw))  # solo formato numérico (segundos)
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------------------
# Parseo / filtrado
# ---------------------------------------------------------------------------

def _normalize(payload: Any, min_price: float) -> list[dict[str, Any]]:
    """Filtra por precio y proyecta solo id, name, price."""
    items = _extract_items(payload)
    result: list[dict[str, Any]] = []

    for item in items:
        if not isinstance(item, dict):
            continue

        price = _to_float(item.get("price"))
        if price is None or price <= min_price:
            continue

        result.append({
            "id": item.get("id"),
            "name": item.get("name"),
            "price": price,
        })

    return result


def _extract_items(payload: Any) -> Iterable[Any]:
    """Soporta respuestas tipo lista o envueltas en {"data": [...]} / {"products": [...]}."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("data", "products", "items", "results"):
            value = payload.get(key)
            if isinstance(value, list):
                return value
    raise ProductFetchError(f"Formato de respuesta inesperado: {type(payload).__name__}")


def _to_float(value: Any) -> float | None:
    """Convierte precios numéricos o strings ('129.99') a float."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value.strip())
        except ValueError:
            return None
    return None
```

### Uso

```python
logging.basicConfig(level=logging.INFO)

try:
    products = fetch_expensive_products("mi-token-secreto")
    for p in products:
        print(f"{p['id']:>6} | {p['name']:<30} | {p['price']:>8.2f}")
except ProductFetchError as exc:
    print(f"Fallo al consultar productos: {exc}")
```

Reutilizando conexiones para varias llamadas:

```python
with httpx.Client(timeout=httpx.Timeout(10.0)) as client:
    caros = fetch_expensive_products(token, client=client)
    muy_caros = fetch_expensive_products(token, min_price=500, client=client)
```

---

## Variante asíncrona

```python
import asyncio


async def afetch_expensive_products(
    token: str,
    *,
    min_price: float = 100.0,
    url: str = API_URL,
    timeout: float = TIMEOUT_SECONDS,
    max_attempts: int = MAX_ATTEMPTS,
    client: httpx.AsyncClient | None = None,
) -> list[dict[str, Any]]:
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    owns_client = client is None
    client = client or httpx.AsyncClient(timeout=httpx.Timeout(timeout))

    last_error: Exception | None = None
    try:
        for attempt in range(1, max_attempts + 1):
            try:
                response = await client.get(url, headers=headers)

                if response.status_code in RETRY_STATUS_CODES:
                    raise httpx.HTTPStatusError(
                        f"Status transitorio {response.status_code}",
                        request=response.request,
                        response=response,
                    )
                response.raise_for_status()

                try:
                    payload = response.json()
                except ValueError as exc:
                    raise ProductFetchError("La respuesta no es JSON válido") from exc

                return _normalize(payload, min_price)

            except httpx.HTTPStatusError as exc:
                if exc.response.status_code not in RETRY_STATUS_CODES:
                    raise ProductFetchError(
                        f"Error HTTP {exc.response.status_code}: {exc.response.text[:200]}"
                    ) from exc
                last_error = exc
            except (httpx.TimeoutException, httpx.TransportError) as exc:
                last_error = exc

            logger.warning("Intento %d/%d falló: %r", attempt, max_attempts, last_error)
            if attempt < max_attempts:
                await asyncio.sleep(_backoff_delay(attempt, exc=last_error))

        raise ProductFetchError(
            f"No se pudo obtener el catálogo tras {max_attempts} intentos: {last_error!r}"
        ) from last_error
    finally:
        if owns_client:
            await client.aclose()
```

---

## Decisiones de diseño

| Punto | Decisión |
|---|---|
| **Timeout** | `httpx.Timeout(10.0)` aplica 10 s a connect, read, write y pool. Es **por intento**, no global: el peor caso son ~30 s + backoff. Si necesitas un presupuesto total, envuelve con `asyncio.wait_for` (async) o compara `time.monotonic()` antes de cada intento. |
| **Qué se reintenta** | Timeouts, errores de transporte (`ConnectError`, `ReadError`, `RemoteProtocolError`…) y status transitorios (408, 429, 5xx). |
| **Qué NO se reintenta** | 401/403 (token inválido), 404, 422 → fallan rápido con `ProductFetchError`. Reintentar un token expirado solo añade latencia. |
| **Backoff** | Exponencial con *full jitter* (`random.uniform(0, base*2^n)`) para evitar tormentas de reintentos sincronizados. Techo de 8 s. Si el servidor manda `Retry-After` numérico, se respeta. |
| **3 intentos** | `max_attempts=3` = 1 llamada original + 2 reintentos. Si tu interpretación es "3 reintentos", pasa `max_attempts=4`. |
| **Robustez del parseo** | Acepta respuesta como lista o envuelta en `data`/`products`/`items`/`results`, ignora elementos no-dict, y convierte precios en string (`"129.99"`) a float. Ítems con precio inválido se descartan en lugar de romper la función. |
| **Inyección de cliente** | El parámetro `client` permite reutilizar conexiones (keep-alive) y testear con `httpx.MockTransport` sin monkeypatching. |

### Test rápido sin red (usando `MockTransport` de httpx)

```python
def test_filtra_por_precio():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["Authorization"] == "Bearer t"
        return httpx.Response(200, json=[
            {"id": 1, "name": "Barato", "price": 50, "stock": 3},
            {"id": 2, "name": "Caro", "price": "150.5", "stock": 1},
        ])

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        assert fetch_expensive_products("t", client=client) == [
            {"id": 2, "name": "Caro", "price": 150.5}
        ]
```