# Grok 4.6 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.6`
- success: True  | final: 7.75 | quality: 9.08
- latency_total: 21.542s | tokens_per_second: 86.9
- input_tokens: 301 | output_tokens: 1872
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


def fetch_expensive_products(token: str) -> list[dict[str, Any]]:
    """GET /products, filtra price > 100 y devuelve [{id, name, price}]."""
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10.0
    max_attempts = 3

    last_error: Exception | None = None
    for attempt in range(max_attempts):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

            if not isinstance(data, list):
                data = []

            return [
                {"id": item["id"], "name": item["name"], "price": item["price"]}
                for item in data
                if isinstance(item, dict)
                and item.get("id") is not None
                and item.get("name") is not None
                and isinstance(item.get("price"), (int, float))
                and item["price"] > 100
            ]
        except httpx.RequestError as exc:
            # Errores de red, DNS, conexión y timeout
            last_error = exc
            if attempt == max_attempts - 1:
                raise
            time.sleep(2**attempt)  # 1s, 2s, 4s
        except httpx.HTTPStatusError:
            raise

    if last_error:
        raise last_error
    return []
```