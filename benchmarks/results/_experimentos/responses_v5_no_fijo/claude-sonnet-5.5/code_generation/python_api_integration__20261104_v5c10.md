# Claude Sonnet 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.89 | quality: 9.32
- latency_total: 17.867s | tokens_per_second: 162.3
- input_tokens: 156 | output_tokens: 2900
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


def get_expensive_products(token: str, min_price: float = 100) -> list[dict[str, Any]]:
    """
    Obtiene productos de la API y devuelve los de precio > min_price.

    Returns:
        Lista de dicts con las claves {id, name, price}.

    Raises:
        ProductsAPIError: si fallan todos los reintentos, si hay un error
        HTTP no reintentable (p. ej. 401, 404) o si la respuesta es inválida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    last_exc: Exception | None = None

    with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = client.get(API_URL, headers=headers)
                response.raise_for_status()
                data = response.json()
                break  # éxito

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                if status not in RETRYABLE_STATUS_CODES:
                    # Errores del cliente (401, 403, 404...) no se reintentan
                    raise ProductsAPIError(
                        f"Error HTTP no reintentable: {status}"
                    ) from exc
                last_exc = exc
                logger.warning("Intento %d/%d: HTTP %d", attempt, MAX_ATTEMPTS, status)

            except httpx.TransportError as exc:
                # Incluye timeouts (TimeoutException), errores de conexión, DNS, etc.
                last_exc = exc
                logger.warning(
                    "Intento %d/%d: error de red (%s: %s)",
                    attempt, MAX_ATTEMPTS, type(exc).__name__, exc,
                )

            except ValueError as exc:
                # JSON inválido en la respuesta
                raise ProductsAPIError("La respuesta no es un JSON válido") from exc

            # Backoff exponencial con jitter: ~1s, ~2s, ...
            if attempt < MAX_ATTEMPTS:
                delay = BACKOFF_BASE_SECONDS * (2 ** (attempt - 1))
                time.sleep(delay + random.uniform(0, 0.5))
        else:
            raise ProductsAPIError(
                f"Falló la petición tras {MAX_ATTEMPTS} intentos"
            ) from last_exc

    if not isinstance(data, list):
        raise ProductsAPIError(
            f"Formato inesperado: se esperaba una lista, se recibió {type(data).__name__}"
        )

    result: list[dict[str, Any]] = []
    for item in data:
        try:
            if float(item["price"]) > min_price:
                result.append(
                    {"id": item["id"], "name": item["name"], "price": item["price"]}
                )
        except (KeyError, TypeError, ValueError):
            logger.warning("Producto malformado ignorado: %r", item)

    return result
```

**Ejemplo de uso:**

```python
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        products = get_expensive_products(token="mi_token_secreto")
        for p in products:
            print(p)
    except ProductsAPIError as e:
        print(f"No se pudieron obtener los productos: {e}")
```

**Decisiones de diseño:**

- **Timeout:** `httpx.Client(timeout=10.0)` aplica 10 s a conexión, lectura, escritura y pool.
- **Qué se reintenta:** errores de red/timeout (`httpx.TransportError`, de la que hereda `TimeoutException`) y códigos 429/5xx. Los 4xx como 401 o 404 fallan de inmediato, porque reintentarlos no tiene sentido.
- **Backoff:** 1 s y 2 s entre intentos (`base * 2^(n-1)`), más un pequeño jitter aleatorio para evitar que varios clientes reintenten a la vez. No hay espera tras el último intento.
- **Robustez:** los productos sin `id`, `name` o `price`, o con precio no numérico, se ignoran con un warning en vez de romper toda la función.
- **Error único:** todo se expone como `ProductsAPIError`, así quien llama solo captura una excepción. La causa original queda encadenada con `from`.

**Supuestos:** la API devuelve directamente una lista JSON de productos. Si devuelve algo como `{"products": [...]}` o paginación, cambia la línea `data = ...` por `data = response.json()["products"]` o añade un bucle de paginación. Si quieres una versión asíncrona con `httpx.AsyncClient` y `asyncio.sleep`, dímelo y te la adapto.