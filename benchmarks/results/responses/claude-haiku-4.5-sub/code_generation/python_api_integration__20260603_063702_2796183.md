# Claude Haiku 4.5 (suscripción) — code_generation/python_api_integration

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.67 | quality: 9.52
- latency_total: 15.159s | tokens_per_second: 156.7
- input_tokens: 10 | output_tokens: 2375
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí está la función Python completa con todos los requisitos:

```python
import httpx
import time
from typing import List, Dict

def fetch_filtered_products(
    api_token: str,
    api_url: str = "https://api.example.com/products",
    min_price: float = 100,
    timeout_seconds: int = 10,
    max_retries: int = 3,
    backoff_base: float = 2.0
) -> List[Dict]:
    """
    Fetch products from API, filter by minimum price, with exponential backoff retry.
    
    Args:
        api_token: Bearer token for authentication
        api_url: API endpoint URL
        min_price: Minimum price threshold for filtering (default: 100)
        timeout_seconds: HTTP timeout in seconds (default: 10)
        max_retries: Maximum retry attempts (default: 3)
        backoff_base: Exponential backoff multiplier (default: 2.0)
    
    Returns:
        List of dicts with {id, name, price} for products > min_price
    
    Raises:
        httpx.RequestError: If all retries fail or on non-retryable errors
        ValueError: If API response format is invalid
    """
    headers = {"Authorization": f"Bearer {api_token}"}
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout_seconds) as client:
                response = client.get(api_url, headers=headers)
                response.raise_for_status()
            
            # Parse JSON response
            data = response.json()
            products = data.get("products", [])
            
            # Filter and extract only required fields
            filtered = [
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"]
                }
                for product in products
                if product.get("price", 0) > min_price
            ]
            
            return filtered
        
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            # Retryable errors (timeout, connection issues)
            if attempt < max_retries - 1:
                wait_time = backoff_base ** attempt  # 1s, 2s, 4s
                print(f"[Attempt {attempt + 1}] {type(e).__name__}. "
                      f"Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"[FAILED] All {max_retries} attempts exhausted.")
                raise
        
        except httpx.HTTPStatusError as e:
            # Non-retryable HTTP errors (4xx/5xx)
            print(f"[ERROR] HTTP {e.response.status_code}: {e}")
            raise
        
        except (KeyError, ValueError) as e:
            # JSON parsing or missing required fields
            print(f"[ERROR] Invalid response format: {e}")
            raise


# Ejemplo de uso
if __name__ == "__main__":
    # Configurar tu token
    bearer_token = "tu_token_aqui"
    
    try:
        products = fetch_filtered_products(
            api_token=bearer_token,
            min_price=100
        )
        
        print(f"✓ Found {len(products)} products with price > $100:\n")
        for product in products:
            print(f"  ID: {product['id']}")
            print(f"  Name: {product['name']}")
            print(f"  Price: ${product['price']}\n")
    
    except httpx.RequestError as e:
        print(f"✗ Request failed: {e}")
    except ValueError as e:
        print(f"✗ Invalid data: {e}")
```

**Características principales:**

| Requisito | Implementación |
|-----------|---|
| **GET + Bearer** | `headers` con `Authorization: Bearer {token}` |
| **Filtro precio > 100** | List comprehension con `if product.get("price", 0) > min_price` |
| **Campos {id, name, price}** | Solo estos 3 campos en el dict retornado |
| **Timeout 10s** | `httpx.Client(timeout=10)` |
| **Errores de red** | Captura `TimeoutException` + `NetworkError` → retry |
| **Backoff exponencial** | `backoff_base ** attempt` (1s → 2s → 4s) |
| **Max 3 intentos** | `for attempt in range(max_retries)` con `max_retries=3` |
| **Solo httpx** | Sin requests, tenacity, ni librerías externas |

**Manejo de errores:**
- ✅ `TimeoutException` / `NetworkError` → Reintenta con backoff
- ✅ `HTTPStatusError` (4xx/5xx) → Falla inmediatamente (no retryable)
- ✅ JSON parsing/missing fields → Excepción clara

**Uso:**
```bash
pip install httpx  # Si no lo tienes ya
python script.py
```