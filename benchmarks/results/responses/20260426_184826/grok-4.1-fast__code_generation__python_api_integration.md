# Grok 4.1 Fast — code_generation/python_api_integration

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 7.67 | quality: 8.48
- latency_total: 10.041s | tokens_per_second: 113.6
- input_tokens: 251 | output_tokens: 1141
- judge_score: 4.2 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any

def get_filtered_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100,
    y retorna una lista de dicts con {id, name, price}.
    
    Maneja errores de red y timeout (10s) con retry backoff exponencial (max 3 intentos).
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                products: List[Dict[str, Any]] = response.json()
                
                filtered = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                return filtered
        
        except (httpx.TimeoutException, httpx.ConnectError, httpx.NetworkError) as e:
            if attempt == max_retries - 1:
                raise
            # Backoff exponencial: 1s, 2s, 4s
            time.sleep(2 ** attempt)
    
    raise Exception("Max retries exceeded")
```