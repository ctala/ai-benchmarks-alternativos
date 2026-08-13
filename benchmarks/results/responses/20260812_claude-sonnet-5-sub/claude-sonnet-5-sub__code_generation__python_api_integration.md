# Claude Sonnet 5 (suscripción) — code_generation/python_api_integration

- model_id: `claude-sonnet-5`
- success: True  | final: 8.07 | quality: 9.6
- latency_total: 25.894s | tokens_per_second: 56.7
- input_tokens: 2 | output_tokens: 1468
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, con una implementación detallada que incluye manejo de errores y reintentos.

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
import time
import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)

TIMEOUT_SECONDS = 10.0
MAX_RETRIES = 3
BASE_BACKOFF_SECONDS = 1.0  # 1s, 2s, 4s...


def get_expensive_products(
    api_url: str = "https://api.example.com/products",
    bearer_token: str = "",
    price_threshold: float = 100.0,
) -> list[dict[str, Any]]:
    """
    Obtiene productos desde la API y filtra los que tienen precio > price_threshold.

    Retorna una lista de dicts con {id, name, price}.
    Reintenta hasta MAX_RETRIES veces con backoff exponencial ante
    errores de red o timeout.

    Raises:
        httpx.HTTPStatusError: si la respuesta final sigue siendo un error HTTP.
        httpx.RequestError: si todos los reintentos fallan por red/timeout.
    """
    headers = {"Authorization": f"Bearer {bearer_token}"}
    last_exception: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
                response = client.get(api_url, headers=headers)
                response.raise_for_status()
                data = response.json()

            products = data.get("products", data) if isinstance(data, dict) else data

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > price_threshold
            ]

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            last_exception = e
            logger.warning(
                "Intento %d/%d falló (%s): %s",
                attempt, MAX_RETRIES, type(e).__name__, e,
            )
            if attempt < MAX_RETRIES:
                backoff = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
                time.sleep(backoff)
            continue

        except httpx.HTTPStatusError as e:
            # Error de status (4xx/5xx) — no vale la pena reintentar
            # salvo que sea 5xx (server-side transitorio)
            if e.response.status_code >= 500 and attempt < MAX_RETRIES:
                last_exception = e
                backoff = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
                logger.warning(
                    "HTTP %d en intento %d/%d, reintentando en %.1fs",
                    e.response.status_code, attempt, MAX_RETRIES, backoff,
                )
                time.sleep(backoff)
                continue
            raise

    # Se agotaron los reintentos
    raise last_exception
```

**Notas de diseño:**

- **Timeout único (10s)** aplicado por `httpx.Client(timeout=...)` — cubre connect + read + write + pool.
- **Retry solo en fallos transitorios**: `TimeoutException`, `NetworkError` y `5xx`. Un `4xx` (ej. 401 por token inválido) falla rápido sin reintentar — reintentar un error del cliente no lo arregla.
- **Backoff exponencial**: 1s → 2s → 4s entre los 3 intentos.
- **Context manager `with httpx.Client(...)`** por request para no dejar conexiones colgadas entre reintentos (alternativa: crear el client una vez fuera del loop si vas a llamar la función muchas veces seguidas — trade-off de performance vs simplicidad).
- Asume que la API responde `{"products": [...]}` o directamente `[...]` — ajustá el `data.get(...)` según el shape real.

Uso:

```python
productos = get_expensive_products(bearer_token="tu_token_aqui")
```