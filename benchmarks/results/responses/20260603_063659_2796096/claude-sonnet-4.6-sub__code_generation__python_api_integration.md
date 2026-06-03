# Claude Sonnet 4.6 (suscripción) — code_generation/python_api_integration

- model_id: `claude-sonnet-4-6`
- success: True  | final: 7.5 | quality: 9.52
- latency_total: 20.859s | tokens_per_second: 73.1
- input_tokens: 3 | output_tokens: 1524
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
import logging
from typing import Any

logger = logging.getLogger(__name__)


def get_expensive_products(
    token: str,
    base_url: str = "https://api.example.com/products",
    price_threshold: float = 100.0,
    max_retries: int = 3,
    timeout: float = 10.0,
) -> list[dict[str, Any]]:
    """
    Obtiene productos de la API y retorna los que superen el precio indicado.

    Args:
        token:            Bearer token de autenticación.
        base_url:         URL del endpoint.
        price_threshold:  Precio mínimo para incluir un producto (default 100).
        max_retries:      Intentos máximos ante errores transitorios (default 3).
        timeout:          Timeout en segundos por request (default 10).

    Returns:
        Lista de dicts con keys {id, name, price}.

    Raises:
        httpx.HTTPStatusError:  Error HTTP no recuperable (4xx).
        RuntimeError:           Si se agotan todos los reintentos.
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_exception: Exception | None = None

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()          # lanza HTTPStatusError en 4xx/5xx

            products: list[dict] = response.json()

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > price_threshold
            ]

        except httpx.HTTPStatusError as exc:
            # Errores 4xx son del cliente → no reintentar
            if 400 <= exc.response.status_code < 500:
                logger.error("Error del cliente %s: %s", exc.response.status_code, exc)
                raise
            # 5xx → puede ser transitorio, reintentar
            last_exception = exc
            logger.warning("Error servidor %s (intento %d/%d)",
                           exc.response.status_code, attempt, max_retries)

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_exception = exc
            logger.warning("Error de red/timeout: %s (intento %d/%d)",
                           exc, attempt, max_retries)

        # Backoff exponencial: 1s → 2s → 4s (no duerme después del último intento)
        if attempt < max_retries:
            wait = 2 ** (attempt - 1)          # 1, 2, 4 segundos
            logger.info("Reintentando en %ss...", wait)
            time.sleep(wait)

    raise RuntimeError(
        f"Fallaron todos los {max_retries} intentos. Último error: {last_exception}"
    ) from last_exception
```

---

## Cómo funciona

| Aspecto | Decisión |
|---|---|
| **Auth** | Header `Authorization: Bearer <token>` en cada request |
| **Timeout** | `httpx.Client(timeout=10.0)` — aplica a connect + read |
| **Retry** | Loop `for attempt in range(1, max_retries+1)` con `time.sleep(2 ** (attempt-1))` |
| **Backoff** | Intento 1 → falla → espera 1s · Intento 2 → falla → espera 2s · Intento 3 → lanza |
| **Errores 4xx** | Se propagan de inmediato (son culpa del cliente, reintentar no ayuda) |
| **Errores 5xx / red / timeout** | Se reintentan hasta agotar intentos |
| **Filtrado** | List comprehension con `p.get("price", 0) > price_threshold` (tolerante a campo ausente) |

## Ejemplo de uso

```python
# Uso básico
productos = get_expensive_products(token="mi_token_aqui")

# Customizado
productos = get_expensive_products(
    token="mi_token_aqui",
    price_threshold=500.0,
    max_retries=5,
    timeout=15.0,
)

print(productos)
# [{"id": 42, "name": "Laptop Pro", "price": 1299.99}, ...]
```

## Testing con mock (sin red real)

```python
import pytest
import httpx
from unittest.mock import patch, MagicMock

def test_filtra_por_precio():
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"id": 1, "name": "Barato",  "price": 50},
        {"id": 2, "name": "Caro",    "price": 200},
        {"id": 3, "name": "Sin precio"},           # tolerancia a campo ausente
    ]
    mock_response.raise_for_status = MagicMock()

    with patch("httpx.Client") as mock_client:
        mock_client.return_value.__enter__.return_value.get.return_value = mock_response
        resultado = get_expensive_products(token="test")

    assert resultado == [{"id": 2, "name": "Caro", "price": 200}]
```