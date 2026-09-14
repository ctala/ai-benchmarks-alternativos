# Qwen 3.8 Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.29 | quality: 9.52
- latency_total: 100.977s | tokens_per_second: 75.9
- input_tokens: 164 | output_tokens: 7666
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

Aquí tienes una función en Python usando solo `httpx` y librería estándar (`time`, `typing`):

```python
# pip install httpx

import time
from typing import Any, Dict, List, Optional

import httpx


class ProductsAPIError(Exception):
    """Error al consultar o procesar los productos."""


def get_expensive_products(
    bearer_token: str,
    *,
    url: str = "https://api.example.com/products",
    timeout: float = 10.0,
    max_attempts: int = 3,
) -> List[Dict[str, Any]]:
    """
    Hace GET a la API de productos, filtra los que tienen price > 100
    y retorna una lista con dicts que contienen solo id, name y price.

    Incluye:
    - Autenticación Bearer token
    - Timeout de 10 segundos por defecto
    - Manejo de errores de red y timeout
    - Retry con backoff exponencial: 1s, 2s, ...
    - Máximo de 3 intentos por defecto
    """

    if not bearer_token:
        raise ValueError("El Bearer token es obligatorio")

    if max_attempts < 1:
        raise ValueError("max_attempts debe ser mayor o igual a 1")

    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    # Códigos HTTP que suelen considerarse transitorios y reintentables.
    transient_status_codes = {429, 500, 502, 503, 504}

    data: Optional[Any] = None

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url, headers=headers)

                # Si el HTTP status es error, lanza HTTPStatusError.
                response.raise_for_status()

                data = response.json()
                break

            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code

                # Reintentar solo errores HTTP transitorios.
                if status_code in transient_status_codes and attempt < max_attempts:
                    time.sleep(2 ** (attempt - 1))
                    continue

                raise ProductsAPIError(
                    f"Error HTTP {status_code} al consultar productos"
                ) from exc

            except (httpx.TimeoutException, httpx.RequestError) as exc:
                # Errores de red, timeout, conexión, etc.
                if attempt == max_attempts:
                    raise ProductsAPIError(
                        f"Error de red o timeout tras {max_attempts} intentos"
                    ) from exc

                # Backoff exponencial: 1, 2, 4, ...
                time.sleep(2 ** (attempt - 1))

            except ValueError as exc:
                raise ProductsAPIError(
                    "La respuesta no contiene un JSON válido"
                ) from exc

    if data is None:
        raise ProductsAPIError("No se obtuvo una respuesta válida")

    if not isinstance(data, list):
        raise ProductsAPIError("La respuesta JSON no es una lista de productos")

    result: List[Dict[str, Any]] = []

    for product in data:
        if not isinstance(product, dict):
            continue

        raw_price = product.get("price")

        # Evitar que True/False se interpreten como 1/0.
        if isinstance(raw_price, bool):
            continue

        try:
            price = float(raw_price)
        except (TypeError, ValueError):
            continue

        if price > 100:
            result.append(
                {
                    "id": product.get("id"),
                    "name": product.get("name"),
                    "price": price,
                }
            )

    return result
```

Ejemplo de uso:

```python
products = get_expensive_products("TU_TOKEN_AQUI")

print(products)
```

Notas:

- La función hace exactamente `GET` a `https://api.example.com/products`.
- Usa autenticación:

```http
Authorization: Bearer TU_TOKEN_AQUI
```

- Timeout por defecto: `10` segundos.
- Máximo de intentos: `3`.
- Backoff exponencial:

```text
Intento 1 falla -> espera 1 segundo
Intento 2 falla -> espera 2 segundos
Intento 3 falla -> lanza ProductsAPIError
```

- Solo retorna productos con `price > 100`.
- Cada producto retornado contiene únicamente:

```python
{"id": ..., "name": ..., "price": ...}
```