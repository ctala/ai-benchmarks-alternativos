# Grok 4.3 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.43 | quality: 7.87
- latency_total: 7.643s | tokens_per_second: 116.1
- input_tokens: 225 | output_tokens: 887

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any


def fetch_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0, connect=5.0)
    max_retries = 3

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

        except (httpx.TimeoutException, httpx.RequestError, httpx.HTTPStatusError) as exc:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)

    return []
```