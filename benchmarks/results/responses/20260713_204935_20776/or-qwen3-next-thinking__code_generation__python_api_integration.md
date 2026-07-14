# Qwen 3-Next 80B Thinking — code_generation/python_api_integration

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.93 | quality: 8.8
- latency_total: 28.229s | tokens_per_second: 171.3
- input_tokens: 112 | output_tokens: 4836
- judge_score: 4.6 | justificación: 

## Respuesta completa

```python
import httpx
import time

def get_filtered_products(token):
    max_retries = 3
    base_delay = 1
    for attempt in range(max_retries):
        try:
            response = httpx.get(
                'https://api.example.com/products',
                headers={'Authorization': f'Bearer {token}'},
                timeout=10.0
            )
            response.raise_for_status()
            products = response.json()
            return [
                {'id': p['id'], 'name': p['name'], 'price': p['price']}
                for p in products
                if p['price'] > 100
            ]
        except (httpx.TimeoutException, httpx.NetworkError):
            if attempt == max_retries - 1:
                raise
            sleep_time = base_delay * (2 ** attempt)
            time.sleep(sleep_time)
        except httpx.HTTPStatusError:
            raise
        except Exception:
            raise
```