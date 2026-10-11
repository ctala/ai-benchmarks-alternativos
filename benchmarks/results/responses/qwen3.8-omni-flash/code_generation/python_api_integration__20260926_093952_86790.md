# Qwen 3.8 Omni Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 8.01 | quality: 9.32
- latency_total: 173.327s | tokens_per_second: 41.0
- input_tokens: 155 | output_tokens: 7101
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

Aquí tienes una implementación **síncrona** usando `httpx`, sin dependencias externas adicionales más allá de `httpx` y la biblioteca estándar de Python.

```python
from __future__ import annotations

import json
import time
from collections.abc import Mapping
from typing import Any, Dict, List, Optional

import httpx


PRODUCTS_URL = "https://api.example.com/products"


def fetch_products_over_100(
    token: str,
    *,
    url: str = PRODUCTS_URL,
    timeout: float = 10.0,
    max_attempts: int = 3,
    backoff_factor: float = 1.0,
) -> List[Dict[str, Any]]:
    """
    Hace GET a la API de productos con Bearer token, filtra los productos
    con price > 100 y devuelve una lista de diccionarios con solo:
        {"id": ..., "name": ..., "price": ...}

    Características:
    - Timeout de 10 segundos por defecto.
    - Reintentos con backoff exponencial.
    - max_attempts = 3 significa 3 intentos totales, no 3 reintentos.
    - Reintenta en errores de red/timeout, HTTP 429, HTTP 5xx y JSON inválido.
    """
    if max_attempts < 1:
        raise ValueError("max_attempts debe ser al menos 1")

    if not token:
        raise ValueError("El token Bearer no puede estar vacío")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    httpx_timeout = httpx.Timeout(timeout)

    payload: Any = None
    last_error: Optional[Exception] = None

    with httpx.Client(timeout=httpx_timeout, headers=headers) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url)
                response.raise_for_status()

                # Si la respuesta viene vacía, asumimos lista vacía.
                if response.content:
                    payload = response.json()
                else:
                    payload = []

                break

            except (httpx.TransportError, httpx.TimeoutException) as exc:
                last_error = exc

                if attempt == max_attempts:
                    raise

                delay = backoff_factor * (2 ** (attempt - 1))
                time.sleep(delay)

            except httpx.HTTPStatusError as exc:
                last_error = exc
                status_code = exc.response.status_code

                # Reintentamos solo en rate limiting o errores de servidor.
                if status_code == 429 or 500 <= status_code < 600:
                    if attempt == max_attempts:
                        raise

                    delay = backoff_factor * (2 ** (attempt - 1))

                    # Si el servidor manda Retry-After, lo respetamos si es mayor.
                    retry_after = exc.response.headers.get("Retry-After")
                    if retry_after:
                        try:
                            delay = max(delay, float(retry_after))
                        except ValueError:
                            pass

                    time.sleep(delay)
                else:
                    # Errores 4xx, salvo 429, normalmente no conviene reintentarlos.
                    raise

            except json.JSONDecodeError as exc:
                last_error = exc

                if attempt == max_attempts:
                    raise

                delay = backoff_factor * (2 ** (attempt - 1))
                time.sleep(delay)

    if payload is None:
        # En teoría no deberíamos llegar aquí porque el último intento relanza,
        # pero dejamos esto para claridad y tipado estático.
        if last_error is not None:
            raise last_error
        raise RuntimeError("No se obtuvo un payload válido desde la API")

    # Soportamos tanto una lista plana como envoltorios comunes:
    # [ {...}, {...} ]
    # {"products": [...]}
    # {"data": [...]}
    # {"items": [...]}
    # {"results": [...]}
    if isinstance(payload, Mapping):
        items = payload.get(
            "products",
            payload.get(
                "data",
                payload.get(
                    "items",
                    payload.get("results", []),
                ),
            ),
        )
    elif isinstance(payload, list):
        items = payload
    else:
        raise TypeError(f"Formato JSON inesperado: {type(payload).__name__}")

    if not isinstance(items, list):
        raise TypeError(
            f"La colección de productos no es una lista: {type(items).__name__}"
        )

    result: List[Dict[str, Any]] = []

    for product in items:
        if not isinstance(product, Mapping):
            continue

        # Solo tomamos productos que tengan los campos mínimos necesarios.
        if "id" not in product or "name" not in product or "price" not in product:
            continue

        try:
            price = float(product["price"])
        except (TypeError, ValueError):
            # Si el precio no es numérico, ignoramos ese producto.
            continue

        if price > 100:
            result.append(
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": price,
                }
            )

    return result
```

Uso básico:

```python
if __name__ == "__main__":
    productos_caros = fetch_products_over_100(token="MI_TOKEN_BEARER")

    for producto in productos_caros:
        print(producto)
```

Ejemplo de salida esperada:

```python
[
    {"id": 10, "name": "Teclado mecánico", "price": 150.0},
    {"id": 22, "name": "Monitor 4K", "price": 499.99},
]
```

Notas importantes:

- `max_attempts=3` significa **3 intentos totales**.
- El backoff exponencial por defecto espera aproximadamente:
  - 1 segundo tras el primer fallo
  - 2 segundos tras el segundo fallo
- El timeout es de 10 segundos por defecto.
- Se reintentan errores de red, timeouts, HTTP `429`, HTTP `5xx` y respuestas JSON inválidas.
- Los errores HTTP `4xx`, salvo `429`, se relanzan sin reintento porque normalmente indican un problema del cliente, como token inválido o petición mal formada.