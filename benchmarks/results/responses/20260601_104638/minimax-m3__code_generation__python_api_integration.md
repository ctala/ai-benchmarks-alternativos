# MiniMax M3 — code_generation/python_api_integration

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.78 | quality: 9.52
- latency_total: 39.875s | tokens_per_second: 35.9
- input_tokens: 268 | output_tokens: 1431
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Solución en Python con `httpx`

```python
import httpx
import logging
from typing import Any

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10
MAX_RETRIES = 3
PRICE_THRESHOLD = 100


def fetch_filtered_products(
    bearer_token: str,
    *,
    price_threshold: float = PRICE_THRESHOLD,
) -> list[dict[str, Any]]:
    """
    Obtiene productos desde la API, filtra por precio y devuelve {id, name, price}.

    - Autenticación: Bearer token.
    - Timeout: 10s por intento.
    - Reintentos: hasta 3, con backoff exponencial (1s, 2s, 4s).

    Raises:
        httpx.HTTPStatusError: Si la API responde con error tras agotar reintentos.
        httpx.RequestError:    Si hay error de red/transporte tras agotar reintentos.
    """
    if not bearer_token:
        raise ValueError("bearer_token es obligatorio")

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
    }

    last_exc: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
                response = client.get(API_URL, headers=headers)
                response.raise_for_status()
                products = response.json()

            if not isinstance(products, list):
                raise ValueError(
                    f"Se esperaba una lista, se recibió: {type(products).__name__}"
                )

            filtered: list[dict[str, Any]] = [
                {
                    "id": int(item["id"]),
                    "name": str(item["name"]),
                    "price": float(item["price"]),
                }
                for item in products
                if _is_valid_product(item, price_threshold)
            ]
            return filtered

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            last_exc = exc
            if attempt == MAX_RETRIES:
                break

            backoff = 2 ** (attempt - 1)  # 1s, 2s, 4s
            logger.warning(
                "Intento %d/%d falló (%s). Reintentando en %ds...",
                attempt, MAX_RETRIES, exc, backoff,
            )
            _sleep(backoff)

    # Si llegamos aquí, se agotaron los reintentos
    assert last_exc is not None
    raise last_exc


def _is_valid_product(item: Any, threshold: float) -> bool:
    """Valida la estructura y el precio de un producto."""
    try:
        return (
            isinstance(item, dict)
            and "id" in item
            and "name" in item
            and "price" in item
            and float(item["price"]) > threshold
        )
    except (TypeError, ValueError):
        return False


def _sleep(seconds: float) -> None:
    """Wrapper de sleep para facilitar testing."""
    import time
    time.sleep(seconds)
```

## Uso

```python
products = fetch_filtered_products("mi_token_secreto")
print(products)
# [{'id': 1, 'name': 'Laptop', 'price': 999.99}, ...]
```

## Versión asíncrona (opcional)

Si lo necesitas no bloqueante, esta variante es equivalente con `httpx.AsyncClient`:

```python
async def fetch_filtered_products_async(
    bearer_token: str,
    *,
    price_threshold: float = PRICE_THRESHOLD,
) -> list[dict[str, Any]]:
    if not bearer_token:
        raise ValueError("bearer_token es obligatorio")

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
    }

    last_exc: Exception | None = None

    async with httpx.AsyncClient(timeout=TIMEOUT_SECONDS) as client:
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = await client.get(API_URL, headers=headers)
                response.raise_for_status()
                products = response.json()
                break  # éxito
            except (httpx.RequestError, httpx.HTTPStatusError) as exc:
                last_exc = exc
                if attempt == MAX_RETRIES:
                    raise
                import asyncio
                await asyncio.sleep(2 ** (attempt - 1))

        filtered = [
            {"id": int(p["id"]), "name": str(p["name"]), "price": float(p["price"])}
            for p in products
            if isinstance(p, dict)
            and all(k in p for k in ("id", "name", "price"))
            and float(p["price"]) > price_threshold
        ]
        return filtered
```

## Aspectos clave de la implementación

| Requisito | Cómo se cumple |
|---|---|
| **GET con Bearer** | Header `Authorization: Bearer <token>` |
| **Filtro `price > 100`** | List comprehension con `_is_valid_product()` |
| **Salida `{id, name, price}`** | Se construye el dict explícitamente con tipos seguros |
| **Timeout 10s** | `httpx.Client(timeout=10)` (cubre connect + read) |
| **Retry con backoff** | Hasta 3 intentos, esperas `2^(n-1)` segundos: 1s → 2s → 4s |
| **Errores de red** | `httpx.RequestError` (timeouts, DNS, conexión) |
| **Errores HTTP** | `response.raise_for_status()` → `httpx.HTTPStatusError` (4xx/5xx) |
| **Sin dependencias extra** | Solo `httpx`; `logging` y `time` son stdlib |

> 💡 **Tip:** Si quieres añadir jitter al backoff para evitar el *thundering herd*, cambia `2 ** (attempt - 1)` por algo como `(2 ** (attempt - 1)) + random.uniform(0, 0.5)`.