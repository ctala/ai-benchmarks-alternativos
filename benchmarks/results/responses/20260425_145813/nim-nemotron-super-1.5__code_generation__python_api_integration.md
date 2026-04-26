# Nemotron Super 49B v1.5 (NIM) — code_generation/python_api_integration

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 6.37 | quality: 8.48
- latency_total: 510.699s | tokens_per_second: 12.0
- input_tokens: 118 | output_tokens: 6145
- judge_score: 4.2 | justificación: 

## Respuesta completa

```python
import httpx
import time

def get_products(token):
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    for attempt in range(3):
        try:
            response = httpx.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Parse JSON response
            products_data = response.json()
            
            # Filter products with price > 100 and extract required fields
            filtered_products = [
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"]
                }
                for product in products_data
                if product.get("price", 0) > 100
            ]
            
            return filtered_products
        
        except httpx.RequestError as e:
            # Retry on network errors and timeouts
            if attempt < 2:
                # Exponential backoff: 1s, 2s, 4s
                delay = 2 ** attempt
                time.sleep(delay)
            else:
                # All retries failed, re-raise the exception
                raise
```