# Nemotron Super 49B v1.5 — code_generation/python_api_integration

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 8.05 | quality: 9.08
- latency_total: 114.589s | tokens_per_second: 53.3
- input_tokens: 120 | output_tokens: 6104
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time

def get_expensive_products(token):
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client() as client:
                response = client.get(
                    "https://api.example.com/products",
                    headers={"Authorization": f"Bearer {token}"},
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()
                filtered = [
                    {"id": product["id"], "name": product["name"], "price": product["price"]}
                    for product in data
                    if product.get("price", 0) > 100
                ]
                return filtered
        except httpx.HTTPError as e:
            if isinstance(e, (httpx.Timeout, httpx.ConnectError)):
                if attempt < max_retries:
                    sleep_time = 2 ** (attempt - 1)
                    time.sleep(sleep_time)
                else:
                    raise e
            else:
                # Re-raise non-retriable HTTP errors (4xx, 5xx)
                raise e
        except Exception as e:
            # Handle other unexpected errors
            raise e
```