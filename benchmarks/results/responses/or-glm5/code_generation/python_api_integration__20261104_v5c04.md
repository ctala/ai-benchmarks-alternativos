# GLM 5 — code_generation/python_api_integration

- model_id: `z-ai/glm-5`
- success: True  | final: 7.9 | quality: 9.0
- latency_total: 31.414s | tokens_per_second: 66.5
- input_tokens: 113 | output_tokens: 2088
- judge_score: 4.6 | justificación: 

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


def fetch_filtered_products(
    token: str,
    url: str = "https://api.example.com/products",
    *,
    timeout: float = 10.0,
    max_attempts: int = 3,
    base_backoff: float = 1.0,
) -> list[dict[str, Any]]:
    """
    Obtiene productos desde la API y devuelve aquellos con precio > 100.

    - Autenticación con Bearer token.
    - Timeout de 10s por intento.
    - Reintentos con backoff exponencial (máximo 3 intentos).
    - Reintenta solo en errores transitorios (red, timeout, 5xx, 429).

    Args:
        token: Bearer token.
        url: Endpoint a consultar.
        timeout: Timeout por intento en segundos.
        max_attempts: Número máximo de intentos (incluye el primero).
        base_backoff: Segundos base para el backoff exponencial.

    Returns:
        Lista de dicts con las claves {id, name, price}.

    Raises:
        httpx.HTTPError: Si todos los intentos fallan o se recibe un error no transitorio.
    """
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    last_exc: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

            # Soporta respuestas tipo lista o {"products": [...]}
            if isinstance(data, list):
                products = data
            elif isinstance(data, dict):
                products = data.get("products", [])
            else:
                products = []

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict)
                and isinstance(p.get("price"), (int, float))
                and p["price"] > 100
            ]

        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            # No reintentar errores 4xx salvo 429 (Too Many Requests)
            if 400 <= status < 500 and status != 429:
                logger.error("HTTP %d no transitorio, abortando: %s", status, exc)
                raise
            last_exc = exc
            logger.warning(
                "HTTP %d en intento %d/%d: %s", status, attempt, max_attempts, exc
            )

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_exc = exc
            logger.warning(
                "Error de red/timeout en intento %d/%d: %s",
                attempt, max_attempts, exc,
            )

        except httpx.HTTPError as exc:
            # Otros errores HTTP genéricos (request mal formado, etc.)
            last_exc = exc
            logger.warning(
                "Error HTTP en intento %d/%d: %s", attempt, max_attempts, exc
            )

        if attempt < max_attempts:
            sleep_time = base_backoff * (2 ** (attempt - 1))  # 1s, 2s, 4s, ...
            logger.info("Reintentando en %.2fs...", sleep_time)
            time.sleep(sleep_time)

    # Agotados los intentos
    assert last_exc is not None
    raise last_exc
```

**Notas de diseño:**

1. **Cliente por intento**: se crea un `httpx.Client` nuevo en cada intento para garantizar estado limpio tras un fallo de red.
2. **Backoff exponencial**: `base_backoff * 2^(attempt-1)` → 1s, 2s, 4s. Solo se espera entre intentos (no tras el último).
3. **Errores transitorios vs. permanentes**: 
   - Se reintenta en `TimeoutException`, `NetworkError`, HTTP 5xx y 429.
   - No se reintenta en 4xx (salvo 429) porque son errores del cliente que persistirán.
4. **Defensa en el parseo**: se admite respuesta como lista o como `{"products": [...]}`, y se valida que `price` sea numérico antes de comparar.
5. **Re-raise final**: si todos los intentos fallan, se propaga la última excepción para que el llamador decida.
6. **Sin dependencias extra**: solo `httpx` y stdlib (`time`, `logging`, `typing`).