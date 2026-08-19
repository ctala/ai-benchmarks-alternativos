# GPT-5.4 — code_generation/python_api_integration

- model_id: `gpt-5.4`
- success: True  | final: 7.53 | quality: 9.08
- latency_total: 5.867s | tokens_per_second: 72.8
- input_tokens: 102 | output_tokens: 427
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
from typing import List, Dict, Any

import httpx


def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_attempts = 3
    timeout = 10.0

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                products = response.json()

                if not isinstance(products, list):
                    raise ValueError("La respuesta JSON no es una lista de productos")

                filtered = [
                    {
                        "id": product.get("id"),
                        "name": product.get("name"),
                        "price": product.get("price"),
                    }
                    for product in products
                    if isinstance(product, dict)
                    and isinstance(product.get("price"), (int, float))
                    and product["price"] > 100
                ]

                return filtered

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            if attempt == max_attempts:
                raise RuntimeError(
                    f"Error de red/timeout tras {max_attempts} intentos"
                ) from e

            backoff_seconds = 2 ** (attempt - 1)
            time.sleep(backoff_seconds)

        except httpx.HTTPStatusError as e:
            raise RuntimeError(
                f"Error HTTP {e.response.status_code} al consultar {url}"
            ) from e

        except ValueError as e:
            raise RuntimeError(f"Respuesta inválida: {e}") from e

    return []
```

Ejemplo de uso:

```python
token = "tu_token_aqui"
products = get_expensive_products(token)
print(products)
```

Si quieres, también te la puedo dar en versión `async` con `httpx.AsyncClient`.