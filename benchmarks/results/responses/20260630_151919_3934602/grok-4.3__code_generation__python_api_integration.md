# Grok 4.3 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.19 | quality: 7.87
- latency_total: 10.777s | tokens_per_second: 90.4
- input_tokens: 225 | output_tokens: 974

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any


def get_expensive_products(
    token: str,
    url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout: float = 10.0
) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API.
    Maneja reintentos con backoff exponencial y timeout.
    """
    headers = {"Authorization": f"Bearer {token}"}
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                products = response.json()

                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

        except (httpx.TimeoutException, httpx.NetworkError, httpx.RequestError) as e:
            if attempt == max_retries - 1:
                raise
            # Backoff exponencial: 1s, 2s, 4s
            time.sleep(2 ** attempt)

        except (httpx.HTTPStatusError, ValueError, KeyError, TypeError) as e:
            # Errores no recuperables (400, 401, JSON inválido, etc.)
            raise

    return []
```