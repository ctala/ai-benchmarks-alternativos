# GPT-OSS 20B (Groq) — code_generation/python_api_integration

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.35 | quality: 9.72
- latency_total: 1.923s | tokens_per_second: 809.3
- input_tokens: 167 | output_tokens: 1556
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
"""
Utility for fetching products from an API and filtering them.

The function `fetch_expensive_products`:
1. Performs a GET request to https://api.example.com/products
   using Bearer‑token authentication.
2. Retries up to 3 times on network errors or timeouts,
   waiting with an exponential back‑off (1 s, 2 s, 4 s).
3. Filters the returned product list for items with `price > 100`.
4. Returns a list of dictionaries containing only the keys
   `id`, `name` and `price`.
"""

import time
from typing import Any, Dict, List

import httpx


def fetch_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Retrieve products from the API and return only those with price > 100.

    Parameters
    ----------
    token : str
        Bearer token used for authentication.

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries with keys `id`, `name` and `price`.

    Raises
    ------
    RuntimeError
        If all retry attempts fail or the response cannot be parsed.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)          # 10‑second timeout per request
    max_attempts = 3
    backoff = 1.0                          # initial back‑off in seconds

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()          # raise for 4xx/5xx

                # Expecting a JSON array of product objects
                data = response.json()
                if not isinstance(data, list):
                    raise ValueError("API did not return a list of products")

                # Filter and keep only the required fields
                filtered = [
                    {
                        "id": prod["id"],
                        "name": prod["name"],
                        "price": prod["price"],
                    }
                    for prod in data
                    if isinstance(prod.get("price"), (int, float))
                    and prod["price"] > 100
                ]

                return filtered

        except (httpx.RequestError, httpx.HTTPError, ValueError) as exc:
            # If this was the last attempt, re‑raise as a RuntimeError
            if attempt == max_attempts:
                raise RuntimeError(
                    f"Failed to fetch products after {max_attempts} attempts"
                ) from exc

            # Otherwise wait and retry
            time.sleep(backoff)
            backoff *= 2.0   # exponential back‑off

    # In theory we should never reach this point because we either
    # return inside the try block or raise in the except block.
    raise RuntimeError("Unexpected error in fetch_expensive_products")
```

### How it works

1. **Request & auth** – A `httpx.Client` is created with a 10‑second timeout and the
   `Authorization: Bearer <token>` header.
2. **Retry logic** – The outer `for` loop attempts the request up to `max_attempts`
   times. On any network error, HTTP error, or JSON parsing issue, the function
   sleeps for an exponentially increasing delay (`1 s, 2 s, 4 s`) before retrying.
3. **Filtering** – After a successful response, the JSON payload (expected to be a
   list) is filtered for products whose `price` field is a numeric value greater
   than `100`. Only the `id`, `name` and `price` fields are kept in the returned
   dictionaries.
4. **Error handling** – If all attempts fail, a `RuntimeError` is raised with the
   original exception chained for debugging purposes.