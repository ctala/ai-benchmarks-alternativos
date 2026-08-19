# Qwen 3.7 Max — code_generation/python_api_integration

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 7.47 | quality: 9.28
- latency_total: 22.808s | tokens_per_second: 56.4
- input_tokens: 113 | output_tokens: 1286
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)

URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10
MAX_RETRIES = 3


def fetch_expensive_products(token: str, min_price: float = 100) -> list[dict[str, Any]]:
    """
    Obtiene productos de la API, filtra los que tienen precio mayor a `min_price`
    y retorna una lista de dicts con las claves {id, name, price}.

    Incluye reintentos con backoff exponencial (hasta MAX_RETRIES intentos)
    ante errores de red, timeout o respuestas HTTP de error.
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_exception: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
                response = client.get(URL, headers=headers)
                response.raise_for_status()
                data = response.json()

            products = data if isinstance(data, list) else data.get("products", [])

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > min_price
            ]

        except (
            httpx.NetworkError,
            httpx.TimeoutException,
            httpx.HTTPStatusError,
        ) as exc:
            last_exception = exc
            if attempt == MAX_RETRIES:
                logger.error("Fallo definitivo tras %d intentos: %s", attempt, exc)
                break

            backoff = 2 ** (attempt - 1)  # 1s, 2s, 4s...
            logger.warning(
                "Intento %d/%d falló (%s). Reintentando en %ds...",
                attempt, MAX_RETRIES, exc, backoff,
            )
            time.sleep(backoff)

        except (KeyError, TypeError, ValueError) as exc:
            # Errores de estructura de datos: no tiene sentido reintentar.
            raise ValueError(f"Respuesta inesperada de la API: {exc}") from exc

    raise RuntimeError(
        f"No se pudieron obtener los productos tras {MAX_RETRIES} intentos"
    ) from last_exception
```

### Puntos clave de la implementación

- **Autenticación**: cabecera `Authorization: Bearer <token>`.
- **Timeout**: se pasa `timeout=10` al `httpx.Client`; lanza `httpx.TimeoutException` si se excede.
- **Filtrado y proyección**: *list comprehension* que descarta `price <= 100` y construye el dict con solo las tres claves pedidas.
- **Reintentos con backoff exponencial**: `2 ** (attempt - 1)` → esperas de 1 s, 2 s y 4 s. Solo se reintenta ante errores recuperables (`NetworkError`, `TimeoutException`, `HTTPStatusError`).
- **Errores no recuperables** (JSON inválido, claves faltantes) se propagan como `ValueError` sin reintentar, ya que repetir la petición no lo solucionaría.
- **Flexibilidad de payload**: acepta tanto una lista directa como un objeto con clave `"products"`, que son las dos formas más comunes en APIs REST.
- **Sin dependencias extra**: solo `httpx` + stdlib (`time`, `logging`, `typing`).

### Uso

```python
products = fetch_expensive_products(token="mi_token_secreto")
for p in products:
    print(p)  # {'id': ..., 'name': ..., 'price': ...}
```

Si prefieres la versión **asíncrona**, basta con cambiar `httpx.Client` por `httpx.AsyncClient`, `client.get` por `await client.get` y `time.sleep` por `asyncio.sleep`.