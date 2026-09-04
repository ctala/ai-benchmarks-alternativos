# Qwen 3.8 Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.17 | quality: 9.32
- latency_total: 92.566s | tokens_per_second: 72.6
- input_tokens: 164 | output_tokens: 6719
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

Aquí tienes una función Python que cumple lo solicitado usando **solo `httpx`** como dependencia externa:

```python
import time
from typing import Any, Dict, List, Optional

import httpx


PRODUCTS_URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10.0
MAX_ATTEMPTS = 3
BACKOFF_BASE_SECONDS = 1.0
RETRYABLE_STATUS_CODES = {408, 429, 500, 502, 503, 504}


class ProductFetchError(Exception):
    """Error al obtener o procesar los productos."""


def get_expensive_products(
    token: str,
    url: str = PRODUCTS_URL,
) -> List[Dict[str, Any]]:
    """
    Hace GET a la API de productos con Bearer token, reintenta con backoff
    exponencial, maneja errores de red/timeout y retorna productos con
    price > 100.

    Retorna:
        List[Dict[str, Any]] con elementos de la forma:
        {"id": ..., "name": ..., "price": ...}
    """

    if not token:
        raise ValueError("El token Bearer es obligatorio.")

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    last_error: Optional[Exception] = None
    payload: Any = None

    # Cliente con timeout global de 10 segundos.
    with httpx.Client(
        timeout=httpx.Timeout(TIMEOUT_SECONDS),
        headers=headers,
    ) as client:

        for attempt in range(MAX_ATTEMPTS):
            try:
                response = client.get(url)

                # Si el status es recuperable, forzamos retry.
                if response.status_code in RETRYABLE_STATUS_CODES:
                    raise httpx.HTTPStatusError(
                        "Retryable HTTP status",
                        request=response.request,
                        response=response,
                    )

                # Para errores HTTP no recuperables: 4xx, etc.
                response.raise_for_status()

                # Si la respuesta es válida, parseamos JSON.
                payload = response.json()
                break

            except httpx.TimeoutException as exc:
                last_error = exc

            except httpx.RequestError as exc:
                # Incluye errores de conexión, red, etc.
                last_error = exc

            except httpx.HTTPStatusError as exc:
                if exc.response.status_code not in RETRYABLE_STATUS_CODES:
                    raise ProductFetchError(
                        f"Error HTTP no recuperable: {exc.response.status_code}"
                    ) from exc

                last_error = exc

            except ValueError as exc:
                # JSON inválido.
                raise ProductFetchError(
                    "La respuesta no contiene JSON válido."
                ) from exc

            # Backoff exponencial: 1s, 2s...
            if attempt < MAX_ATTEMPTS - 1:
                time.sleep(BACKOFF_BASE_SECONDS * (2 ** attempt))

        else:
            raise ProductFetchError(
                f"La petición falló después de {MAX_ATTEMPTS} intentos."
            ) from last_error

    # Aceptamos tanto una lista directa como un dict con clave "products",
    # "data" o "items".
    if isinstance(payload, dict):
        items = payload.get("products")
        if items is None:
            items = payload.get("data")
        if items is None:
            items = payload.get("items")
        if items is None:
            items = []
    else:
        items = payload

    if not isinstance(items, list):
        raise ProductFetchError(
            "Formato de respuesta inesperado: se esperaba una lista de productos."
        )

    result: List[Dict[str, Any]] = []

    for product in items:
        if not isinstance(product, dict):
            continue

        price = product.get("price")

        # Evitamos bool porque bool es subclase de int.
        if isinstance(price, bool):
            continue

        try:
            price_value = float(price)
        except (TypeError, ValueError):
            continue

        if price_value > 100:
            result.append(
                {
                    "id": product.get("id"),
                    "name": product.get("name"),
                    "price": price_value,
                }
            )

    return result
```

Uso:

```python
products = get_expensive_products("YOUR_TOKEN")

for product in products:
    print(product)
```