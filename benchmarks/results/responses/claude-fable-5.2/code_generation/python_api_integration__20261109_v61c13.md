# Claude Fable 5.2 — code_generation/python_api_integration

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.63 | quality: 9.32
- latency_total: 22.642s | tokens_per_second: 119.9
- input_tokens: 156 | output_tokens: 2715
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
import time
from typing import Any

import httpx

API_URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10.0
MAX_ATTEMPTS = 3
BACKOFF_BASE_SECONDS = 1.0
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


class ProductsAPIError(Exception):
    """Error al obtener productos de la API."""


def _filter_products(data: Any, min_price: float) -> list[dict[str, Any]]:
    if not isinstance(data, list):
        raise ProductsAPIError("Formato de respuesta inesperado: se esperaba una lista")

    result = []
    for product in data:
        if not isinstance(product, dict):
            continue
        price = product.get("price")
        if isinstance(price, (int, float)) and not isinstance(price, bool) and price > min_price:
            result.append(
                {"id": product.get("id"), "name": product.get("name"), "price": price}
            )
    return result


def get_expensive_products(token: str, min_price: float = 100) -> list[dict[str, Any]]:
    """
    Obtiene los productos con precio > min_price.

    Reintenta hasta 3 veces con backoff exponencial (1s, 2s) ante errores
    de red, timeouts y respuestas 429/5xx.

    Raises:
        ProductsAPIError: si la petición falla definitivamente.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    last_error: Exception | None = None

    with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = client.get(API_URL, headers=headers)
                response.raise_for_status()
                return _filter_products(response.json(), min_price)

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                if status not in RETRYABLE_STATUS:
                    # Errores como 401/403/404 no se arreglan reintentando
                    raise ProductsAPIError(f"Error HTTP {status}") from exc
                last_error = exc

            except httpx.RequestError as exc:
                # Incluye timeouts, errores de conexión, DNS, etc.
                last_error = exc

            except ValueError as exc:
                raise ProductsAPIError("La respuesta no es JSON válido") from exc

            if attempt < MAX_ATTEMPTS:
                time.sleep(BACKOFF_BASE_SECONDS * 2 ** (attempt - 1))

    raise ProductsAPIError(
        f"No se pudo obtener productos tras {MAX_ATTEMPTS} intentos: {last_error}"
    ) from last_error
```

Ejemplo de uso:

```python
try:
    products = get_expensive_products("mi_token")
    print(products)  # [{"id": 1, "name": "Laptop", "price": 999.99}, ...]
except ProductsAPIError as e:
    print(f"Fallo: {e}")
```

Decisiones de diseño:

- **Qué se reintenta:** errores de red, timeouts y los códigos 429/500/502/503/504. Los demás errores 4xx (por ejemplo, 401 por token inválido) fallan de inmediato.
- **Formato de respuesta:** asumí que la API devuelve una lista JSON directamente. Si viene envuelta (por ejemplo, `{"products": [...]}`), cambia la llamada a `_filter_products(response.json()["products"], min_price)`.
- **Datos sucios:** los productos sin `price` o con un precio no numérico se ignoran en lugar de lanzar una excepción.
- **Errores:** todo fallo definitivo se lanza como `ProductsAPIError`, con la excepción original encadenada.