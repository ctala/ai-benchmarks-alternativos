# DeepSeek V4 Pro — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.35 | quality: 9.32
- latency_total: 24.983s | tokens_per_second: 57.9
- input_tokens: 110 | output_tokens: 1446
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
import httpx
from typing import Any, Dict, List

def fetch_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Fetches products from the API, filters those with price > 100,
    and returns a list of dictionaries containing only 'id', 'name', and 'price'.

    Implements exponential backoff (max 3 attempts) and a 10-second timeout.
    Raises an exception if all retries fail.

    Args:
        token: Bearer token for authentication.

    Returns:
        List of dicts with keys 'id', 'name', 'price' for products with price > 100.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_retries = 3
    base_backoff = 1.0  # seconds

    last_exception = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Raise for 4xx/5xx status codes
                products = response.json()

                # Filter and extract required fields
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]

        except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as exc:
            last_exception = exc
            # Only retry on server errors (5xx) or network/timeout issues
            if isinstance(exc, httpx.HTTPStatusError) and exc.response.status_code < 500:
                raise  # Do not retry client errors

            if attempt < max_retries - 1:
                sleep_time = base_backoff * (2 ** attempt)
                time.sleep(sleep_time)
            else:
                raise last_exception

    # This line is unreachable but satisfies type checkers
    raise RuntimeError("Unexpected end of retry loop")
```