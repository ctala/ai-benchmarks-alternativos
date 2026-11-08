# Claude Haiku 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.47 | quality: 9.32
- latency_total: 11.685s | tokens_per_second: 260.0
- input_tokens: 156 | output_tokens: 3038
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
import time

import httpx

API_URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10.0
MAX_ATTEMPTS = 3
BASE_BACKOFF_SECONDS = 1.0  # Espera: 1s, 2s, 4s...
MIN_PRICE = 100

logger = logging.getLogger(__name__)


class ProductsAPIError(Exception):
    """Se lanza cuando no se pueden obtener los productos."""


def _is_retryable_status(status_code: int) -> bool:
    # Reintentar solo en errores temporales del servidor o límite de peticiones.
    return status_code == 429 or status_code >= 500


def _get_with_retry(client: httpx.Client, headers: dict) -> httpx.Response:
    last_error: Exception | None = None

    for attempt in range(MAX_ATTEMPTS):
        try:
            response = client.get(API_URL, headers=headers)
        except httpx.TransportError as exc:  # Incluye timeouts y errores de red
            last_error = exc
            logger.warning("Intento %d/%d falló por error de red: %s",
                           attempt + 1, MAX_ATTEMPTS, exc)
        else:
            if response.is_success:
                return response

            if response.status_code in (401, 403):
                # Error de autenticación: reintentar no tiene sentido.
                raise ProductsAPIError(
                    f"Autenticación rechazada (HTTP {response.status_code})"
                )

            if not _is_retryable_status(response.status_code):
                raise ProductsAPIError(
                    f"Error HTTP no recuperable: {response.status_code}"
                )

            last_error = httpx.HTTPStatusError(
                f"HTTP {response.status_code}",
                request=response.request,
                response=response,
            )
            logger.warning("Intento %d/%d recibió HTTP %d",
                           attempt + 1, MAX_ATTEMPTS, response.status_code)

        # Backoff exponencial entre intentos (no tras el último)
        if attempt < MAX_ATTEMPTS - 1:
            time.sleep(BASE_BACKOFF_SECONDS * (2 ** attempt))

    raise ProductsAPIError(
        f"No se pudo obtener productos tras {MAX_ATTEMPTS} intentos"
    ) from last_error


def get_products_over_100(token: str) -> list[dict]:
    """
    Obtiene los productos de la API, filtra los de precio > 100
    y devuelve una lista de dicts con solo id, name y price.

    Raises:
        ProductsAPIError: si falla la petición tras los reintentos
                          o la respuesta no es válida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
        response = _get_with_retry(client, headers)

    try:
        products = response.json()
    except ValueError as exc:
        raise ProductsAPIError("La respuesta no es JSON válido") from exc

    if not isinstance(products, list):
        raise ProductsAPIError("Se esperaba una lista de productos")

    result = []
    for product in products:
        price = product.get("price")
        if isinstance(price, (int, float)) and price > MIN_PRICE:
            result.append({
                "id": product.get("id"),
                "name": product.get("name"),
                "price": price,
            })

    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        expensive = get_products_over_100(token="TU_TOKEN_AQUI")
        for item in expensive:
            print(item)
    except ProductsAPIError as exc:
        print(f"Error: {exc}")
```

**Notas:**

- **Timeout:** `httpx.Client(timeout=10.0)` aplica 10 segundos a conexión, lectura y escritura.
- **Reintentos:** se reintenta ante errores de red/timeout (`httpx.TransportError`), HTTP 429 y 5xx. No se reintenta ante 401/403 ni otros 4xx, porque no se recuperarían.
- **Backoff:** con 3 intentos, las esperas son 1s y 2s (`1 * 2**intento`). Si quieres evitar que varios clientes reintenten a la vez, puedes añadir jitter con `random.uniform`.
- **Suposición sobre la respuesta:** asumo que la API devuelve una lista JSON de objetos con `id`, `name` y `price` numérico. Si la respuesta viene envuelta (por ejemplo, `{"data": [...]}`), hay que ajustar la línea donde se parsea `products`.