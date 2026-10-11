# Claude Sonnet 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.9 | quality: 9.32
- latency_total: 18.99s | tokens_per_second: 148.2
- input_tokens: 156 | output_tokens: 2815
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
import logging
import random
import time
from typing import Any

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10.0
MAX_ATTEMPTS = 3
BACKOFF_BASE_SECONDS = 1.0
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


class ProductsAPIError(Exception):
    """Error al obtener productos desde la API."""


def get_expensive_products(
    token: str,
    min_price: float = 100,
    *,
    url: str = API_URL,
) -> list[dict[str, Any]]:
    """
    Obtiene productos de la API y devuelve los de precio > min_price,
    con solo los campos {id, name, price}.

    Reintenta con backoff exponencial (máx. 3 intentos) ante timeouts,
    errores de red y respuestas 429/5xx. Errores 4xx (401, 403, 404...)
    no se reintentan, ya que no se resolverían solos.

    Raises:
        ProductsAPIError: si se agotan los reintentos, hay un error
            no recuperable o la respuesta no tiene el formato esperado.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    data: Any = None

    with httpx.Client(timeout=TIMEOUT_SECONDS, headers=headers) as client:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
                break  # éxito

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                if status not in RETRYABLE_STATUS_CODES:
                    raise ProductsAPIError(
                        f"Error HTTP no recuperable: {status}"
                    ) from exc
                error: Exception = exc

            except httpx.TransportError as exc:
                # Incluye TimeoutException, ConnectError, ReadError, etc.
                error = exc

            except ValueError as exc:  # JSON inválido
                raise ProductsAPIError("La respuesta no es JSON válido") from exc

            # Si llegamos aquí, el error es reintentable
            if attempt == MAX_ATTEMPTS:
                raise ProductsAPIError(
                    f"Fallo tras {MAX_ATTEMPTS} intentos: {error!r}"
                ) from error

            delay = BACKOFF_BASE_SECONDS * 2 ** (attempt - 1)  # 1s, 2s, ...
            delay += random.uniform(0, 0.5)  # jitter
            logger.warning(
                "Intento %d/%d falló (%r). Reintentando en %.2fs",
                attempt, MAX_ATTEMPTS, error, delay,
            )
            time.sleep(delay)

    # Acepta tanto una lista directa como {"products": [...]}
    if isinstance(data, dict):
        data = data.get("products", [])
    if not isinstance(data, list):
        raise ProductsAPIError("Formato de respuesta inesperado")

    result: list[dict[str, Any]] = []
    for product in data:
        try:
            price = float(product["price"])
            if price > min_price:
                result.append(
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                    }
                )
        except (KeyError, TypeError, ValueError):
            logger.warning("Producto ignorado por datos inválidos: %r", product)

    return result
```

**Ejemplo de uso:**

```python
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        products = get_expensive_products("mi_token_secreto")
        for p in products:
            print(p)
    except ProductsAPIError as e:
        print(f"No se pudieron obtener los productos: {e}")
```

**Decisiones de diseño:**

- **Timeout:** `httpx.Client(timeout=10.0)` aplica 10 s a conexión, lectura, escritura y pool.
- **Retry sin dependencias extra:** es un bucle con `time.sleep`, usando solo la librería estándar (`random` para el jitter, que evita que muchos clientes reintenten a la vez).
- **Qué se reintenta:** `httpx.TransportError` (timeouts y errores de red) y los códigos 429/500/502/503/504. Un 401 o 404 falla de inmediato.
- **Backoff:** 1 s → 2 s (más jitter). Con 3 intentos solo hay 2 esperas; no se duerme tras el último fallo.
- **Robustez:** los productos con datos malformados se omiten con un warning en lugar de romper toda la función.
- **Formato de respuesta:** como no conozco el esquema real, acepto una lista directa o un objeto con la clave `"products"`. Ajusta esa parte si tu API usa otra estructura (por ejemplo, paginación).

Si necesitas una versión asíncrona, basta con usar `httpx.AsyncClient`, `await client.get(...)` y `asyncio.sleep` en lugar de `time.sleep`.