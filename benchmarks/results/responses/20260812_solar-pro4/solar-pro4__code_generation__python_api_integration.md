# Solar Pro 4 — code_generation/python_api_integration

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.84 | quality: 9.52
- latency_total: 11.889s | tokens_per_second: 57.0
- input_tokens: 157 | output_tokens: 678
- judge_score: 4.8 | justificación: 

## Respuesta completa



```python
import httpx
import time
from typing import List, Dict, Any, Optional

def fetch_expensive_products(
    bearer_token: str,
    base_url: str = "https://api.example.com/products",
    price_threshold: float = 100.0,
    timeout: float = 10.0,
    max_retries: int = 3
) -> List[Dict[str, Any]]:
    """
    Fetches products from API, filters by price > threshold, and returns 
    a list of dicts with id, name, and price.
    
    Implements retry with exponential backoff for network/timeout errors.
    
    Args:
        bearer_token: Authentication token for Bearer auth.
        base_url: API endpoint URL.
        price_threshold: Minimum price to filter products.
        timeout: Request timeout in seconds.
        max_retries: Maximum number of retry attempts.
    
    Returns:
        List of dictionaries containing 'id', 'name', and 'price' for 
        products exceeding the price threshold.
    """
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json"
    }

    last_exception = None

    for attempt in range(max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()
                products = response.json()

                filtered = [
                    {
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "price": p.get("price")
                    }
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p.get("price") > price_threshold
                ]

                return filtered

        except (httpx.RequestError, httpx.TimeoutException, httpx.HTTPError) as e:
            last_exception = e
            if attempt < max_retries:
                backoff = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s...
                time.sleep(backoff)
            continue

    # All retries exhausted
    raise RuntimeError(
        f"Failed to fetch products after {max_retries + 1} attempts. "
        f"Last error: {last_exception}"
    )
```

### Key Features

- **Authentication**: Uses Bearer token via `Authorization` header.
- **Filtering**: Returns only products with `price > 100`.
- **Output Format**: Each item includes only `id`, `name`, and `price`.
- **Error Handling**: Catches network, timeout, and HTTP errors.
- **Retry Logic**: Retries up to 3 times with exponential backoff (1s, 2s, 4s).
- **Timeout**: Enforced at 10 seconds per request.
- **Dependencies**: Uses only `httpx` and standard library modules.

### Example Usage

```python
try:
    products = fetch_expensive_products(bearer_token="your_token_here")
    print(f"Found {len(products)} products above $100")
    for product in products:
        print(f"{product['name']}: ${product['price']}")
except RuntimeError as e:
    print(f"Error: {e}")
```