# Nemotron Super 49B v1.5 — code_generation/python_api_integration

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 8.45 | quality: 9.52
- latency_total: 70.898s | tokens_per_second: 53.5
- input_tokens: 120 | output_tokens: 3792
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time

def get_products(token):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = httpx.get(
                "https://api.example.com/products",
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            products = response.json()
            
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > 100
            ]
            return filtered
        
        except (httpx.NetworkError, httpx.Timeout) as e:
            if attempt < max_retries - 1:
                sleep_time = 2 ** attempt
                time.sleep(sleep_time)
            else:
                raise RuntimeError("Request failed after maximum retries") from e
        
        except httpx.HTTPError as e:
            raise RuntimeError("HTTP error occurred") from e
```

**Explicación:**

1. **Autenticación Bearer Token:**  
   Se incluye el header `Authorization` con el formato `Bearer {token}`.

2. **Filtrado de productos:**  
   Se usa una lista por comprensión para filtrar productos con `price > 100` y crear dicts con los campos requeridos.

3. **Manejo de errores y timeout:**  
   - Se capturan `httpx.NetworkError` y `httpx.Timeout`.
   - Se implementa retry con backoff exponencial (`2^attempt` segundos).
   - Máximo 3 intentos (incluyendo el primero).

4. **Excepciones HTTP:**  
   Se capturan errores HTTP (ej: 4xx, 5xx) y se lanzan nuevamente como `RuntimeError` para diferenciarlos de errores de red.

**Uso:**  
```python
try:
    products = get_products("your_bearer_token_here")
    print(products)
except RuntimeError as e:
    print(f"Error: {e}")
```