# Claude Opus 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.85 | quality: 9.52
- latency_total: 30.16s | tokens_per_second: 123.8
- input_tokens: 156 | output_tokens: 3734
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

# Función para obtener productos con httpx y reintentos

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
MIN_PRICE = 100

# Códigos HTTP transitorios que vale la pena reintentar
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}

# Errores de red/timeout que se reintentan
RETRYABLE_EXCEPTIONS = (
    httpx.TimeoutException,      # ConnectTimeout, ReadTimeout, WriteTimeout, PoolTimeout
    httpx.NetworkError,          # ConnectError, ReadError, WriteError, CloseError
    httpx.RemoteProtocolError,   # el servidor cerró la conexión inesperadamente
)


class ProductFetchError(Exception):
    """Error al obtener los productos de la API."""


def _compute_backoff(attempt: int, response: httpx.Response | None = None) -> float:
    """Backoff exponencial con jitter. Respeta Retry-After si viene en la respuesta."""
    if response is not None:
        retry_after = response.headers.get("Retry-After")
        if retry_after and retry_after.isdigit():
            return float(retry_after)
    # attempt=1 -> ~1s, attempt=2 -> ~2s, attempt=3 -> ~4s ...
    return BACKOFF_BASE_SECONDS * (2 ** (attempt - 1)) + random.uniform(0, 0.5)


def _get_json_with_retry(client: httpx.Client, url: str) -> Any:
    """Hace GET con reintentos y backoff exponencial. Devuelve el JSON parseado."""
    last_error: Exception | None = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        response: httpx.Response | None = None
        try:
            response = client.get(url)
        except RETRYABLE_EXCEPTIONS as exc:
            last_error = exc
            logger.warning(
                "Intento %d/%d falló por error de red/timeout: %r",
                attempt, MAX_ATTEMPTS, exc,
            )
        else:
            if response.status_code in RETRYABLE_STATUS_CODES:
                last_error = httpx.HTTPStatusError(
                    f"Respuesta transitoria {response.status_code}",
                    request=response.request,
                    response=response,
                )
                logger.warning(
                    "Intento %d/%d recibió HTTP %d",
                    attempt, MAX_ATTEMPTS, response.status_code,
                )
            else:
                # Errores 4xx (401, 403, 404...) no se reintentan
                try:
                    response.raise_for_status()
                except httpx.HTTPStatusError as exc:
                    raise ProductFetchError(
                        f"Error HTTP no recuperable: {response.status_code}"
                    ) from exc

                try:
                    return response.json()
                except ValueError as exc:
                    raise ProductFetchError("La respuesta no es JSON válido") from exc

        if attempt < MAX_ATTEMPTS:
            delay = _compute_backoff(attempt, response)
            logger.info("Reintentando en %.2f segundos...", delay)
            time.sleep(delay)

    raise ProductFetchError(
        f"No se pudo obtener los productos tras {MAX_ATTEMPTS} intentos"
    ) from last_error


def _parse_price(value: Any) -> float | None:
    """Convierte el precio a float; devuelve None si no es válido."""
    if isinstance(value, bool):  # evita que True/False pasen como 1/0
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_expensive_products(token: str, url: str = API_URL) -> list[dict[str, Any]]:
    """
    Obtiene los productos de la API y devuelve solo los que tienen precio > 100.

    Args:
        token: Bearer token de autenticación.
        url: Endpoint de productos.

    Returns:
        Lista de dicts con las claves {id, name, price}.

    Raises:
        ProductFetchError: si falla la petición tras los reintentos,
            si hay un error HTTP no recuperable o si la respuesta es inválida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    with httpx.Client(headers=headers, timeout=TIMEOUT_SECONDS) as client:
        data = _get_json_with_retry(client, url)

    # Acepta tanto una lista directa como {"products": [...]}
    if isinstance(data, dict):
        data = data.get("products", [])
    if not isinstance(data, list):
        raise ProductFetchError("Formato de respuesta inesperado")

    result: list[dict[str, Any]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        price = _parse_price(item.get("price"))
        if price is not None and price > MIN_PRICE:
            result.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "price": price,
            })

    return result


if __name__ == "__main__":
    import os

    logging.basicConfig(level=logging.INFO)

    try:
        products = fetch_expensive_products(os.environ["API_TOKEN"])
        for p in products:
            print(p)
    except ProductFetchError as e:
        logger.error("Error: %s", e)
```

## Decisiones de diseño

| Aspecto | Comportamiento |
|---|---|
| **Timeout** | 10 s aplicado a conexión, lectura, escritura y pool (`httpx.Client(timeout=10)`). |
| **Reintentos** | Máximo 3 intentos. Esperas de ~1 s y ~2 s entre ellos, más un *jitter* aleatorio para no saturar el servidor si muchos clientes fallan a la vez. |
| **Qué se reintenta** | Timeouts, errores de red, desconexiones y respuestas HTTP 429/5xx. |
| **Qué NO se reintenta** | Errores 4xx como 401 o 404, porque reintentarlos no cambia el resultado. Se lanzan de inmediato. |
| **Retry-After** | Si el servidor envía este header (típico en 429), se usa su valor en lugar del backoff calculado. |
| **Robustez del filtro** | Ignora items sin precio o con precio no numérico. Acepta precios como string (`"150.00"`). |
| **Errores** | Todo se expone como `ProductFetchError`. La causa original se conserva con `from exc` para depurar. |

> **Nota:** asumí que la API devuelve una lista de productos o un objeto `{"products": [...]}`. Si usa otra estructura (por ejemplo `{"data": [...]}` o paginación), ajusta la extracción en `fetch_expensive_products`.