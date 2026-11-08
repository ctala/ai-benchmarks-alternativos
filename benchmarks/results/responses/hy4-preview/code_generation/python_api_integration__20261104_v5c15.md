# Tencent Hy4 preview — code_generation/python_api_integration

- model_id: `tencent/hy4-preview`
- success: True  | final: 7.78 | quality: 9.08
- latency_total: 63.33s | tokens_per_second: 62.5
- input_tokens: 129 | output_tokens: 3960
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


def get_products_over_100(token: str) -> list[dict[str, Any]]:
    """
    Obtiene productos desde https://api.example.com/products,
    filtra los que tienen price > 100 y retorna solo {id, name, price}.

    Reintentos:
    - Máximo 3 intentos.
    - Backoff exponencial: 1s, 2s.
    """

    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_attempts = 3
    timeout = httpx.Timeout(10.0)

    def price_gt_100(price: Any) -> bool:
        if isinstance(price, bool):
            return False
        return isinstance(price, (int, float)) and price > 100

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_attempts):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                data = response.json()

                # Si la API responde {"products": [...]}
                if isinstance(data, dict):
                    products = data.get("products", [])
                else:
                    products = data

                if not isinstance(products, list):
                    raise ValueError("La respuesta no contiene una lista de productos")

                return [
                    {
                        "id": product.get("id"),
                        "name": product.get("name"),
                        "price": product.get("price"),
                    }
                    for product in products
                    if isinstance(product, dict)
                    and price_gt_100(product.get("price"))
                ]

            except httpx.RequestError as exc:
                # Incluye timeouts, errores de conexión, DNS, etc.
                if attempt == max_attempts - 1:
                    raise RuntimeError(
                        f"Error de red/timeout tras {max_attempts} intentos"
                    ) from exc

                time.sleep(2 ** attempt)

            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code

                # Reintenta solo errores 5xx
                if 500 <= status_code < 600 and attempt < max_attempts - 1:
                    time.sleep(2 ** attempt)
                    continue

                raise RuntimeError(
                    f"Error HTTP {status_code} al consultar productos"
                ) from exc

    return []
```

Ejemplo de uso:

```python
products = get_products_over_100("tu_token_aqui")
print(products)
```

`httpx.RequestError` cubre errores de red y timeout, y el timeout se configura en `10.0` segundos con `httpx.Timeout(10.0)`.