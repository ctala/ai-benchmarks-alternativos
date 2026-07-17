# Nemotron Nano 9B v2 — code_generation/python_api_integration

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 8.08 | quality: 9.08
- latency_total: 115.36s | tokens_per_second: 20.0
- input_tokens: 114 | output_tokens: 2305
- judge_score: 4.8 | justificación: 

## Respuesta completa



```python
import httpx
import time

def get_expensive_products(token):
    headers = {'Authorization': f'Bearer {token}'}
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10) as client:
                response = client.get('https://api.example.com/products', headers=headers)
                response.raise_for_status()
                products = response.json()
                
                # Filter products and format output
                filtered_products = [
                    {'id': p['id'], 'name': p['name'], 'price': p['price']}
                    for p in products
                    if p.get('price', 0) > 100
                ]
                return filtered_products
                
        except (httpx.RequestError, httpx.Timeout) as e:
            if attempt < max_retries - 1:
                delay = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                time.sleep(delay)
            else:
                return []  # Return empty list after all retries fail
                
    return []  # Fallback return (shouldn't be reached)
```
