# Nemotron Nano 9B v2 (NIM) — code_generation/python_api_integration

- model_id: `nvidia/nvidia-nemotron-nano-9b-v2`
- success: True  | final: 6.58 | quality: 8.24
- latency_total: 66.7s | tokens_per_second: 60.9
- input_tokens: 114 | output_tokens: 4059
- judge_score: 4.2 | justificación: 

## Respuesta completa



```python
import httpx
import time

def get_filtered_products(token):
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    for attempt in range(3):
        try:
            response = httpx.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            filtered_products = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in data if p.get("price", 0) > 100
            ]
            return filtered_products
        except (httpx.TimeoutException, httpx.HTTPError) as e:
            if attempt < 2:
                delay = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                time.sleep(delay)
            else:
                return []  # Return empty list after all retries fail
    return []
```
