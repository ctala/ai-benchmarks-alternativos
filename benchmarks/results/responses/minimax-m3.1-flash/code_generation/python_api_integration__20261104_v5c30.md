# MiniMax M3.1 Flash — code_generation/python_api_integration

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 8.25 | quality: 9.32
- latency_total: 84.929s | tokens_per_second: 82.5
- input_tokens: 294 | output_tokens: 7004
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
MAX_ATTEMPTS = 3
TIMEOUT_SECONDS = 10.0
RETRYABLE_STATUS_CODES = {408, 425, 429, 500, 502, 503, 504}


def get_products(token: str) -> list[dict[str, Any]]:
    """
    Obtiene los productos con precio mayor que 100.

    Se esperan como respuesta una lista JSON o un objeto con la forma:
        {"products": [...]}

    Tras agotar los intentos, el último error se vuelve a lanzar.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(
        headers=headers,
        timeout=TIMEOUT_SECONDS,
    ) as client:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = client.get(API_URL)
                response.raise_for_status()

                payload = response.json()
                products = (
                    payload.get("products", [])
                    if isinstance(payload, dict)
                    else payload
                )

                result: list[dict[str, Any]] = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    price = product.get("price")

                    # Se asume que el precio es un número JSON.
                    if isinstance(price, (int, float)) and price > 100:
                        result.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": price,
                            }
                        )

                return result

            except httpx.RequestError:
                # Incluye errores de red y httpx.TimeoutException.
                if attempt == MAX_ATTEMPTS:
                    raise

                # Backoff exponencial: 1 s, 2 s, ...
                time.sleep(2 ** (attempt - 1))

            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code

                # Reintentar solo errores HTTP transitorios.
                if (
                    status_code not in RETRYABLE_STATUS_CODES
                    or attempt == MAX_ATTEMPTS
                ):
                    raise

                time.sleep(2 ** (attempt - 1))
```

La función realiza como máximo **3 intentos en total**, con esperas de `1` y `2` segundos entre ellos. Los errores de red y los timeouts se reintentan; los errores HTTP no transitorios, como `400` o `404`, se propagan inmediatamente.