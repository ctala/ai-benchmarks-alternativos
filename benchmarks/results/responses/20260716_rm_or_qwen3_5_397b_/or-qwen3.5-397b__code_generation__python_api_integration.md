# Qwen 3.5 397B — code_generation/python_api_integration

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.55 | quality: 9.72
- latency_total: 16.386s | tokens_per_second: 102.0
- input_tokens: 113 | output_tokens: 1672
- judge_score: 4.8 | justificación: 

## Respuesta completa



```python
import httpx
import time
from typing import List, Dict

def get_expensive_products(token: str, base_url: str = "https://api.example.com") -> List[Dict]:
    """
    Obtiene productos con precio > 100 de la API.
    
    Args:
        token: Bearer token para autenticación
        base_url: URL base de la API
    
    Returns:
        Lista de diccionarios con id, name, price de productos con precio > 100
    
    Raises:
        httpx.TimeoutException: Si se agotan los reintentos por timeout
        httpx.RequestError: Si se agotan los reintentos por error de red
        httpx.HTTPStatusError: Si la API retorna error HTTP (no se reintenta)
    """
    max_retries = 3
    timeout_seconds = 10
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout_seconds) as client:
                headers = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                }
                
                response = client.get(
                    f"{base_url}/products",
                    headers=headers
                )
                
                # Lanzar excepción para errores HTTP (4xx, 5xx)
                response.raise_for_status()
                
                products = response.json()
                
                # Filtrar productos con precio > 100 y retornar solo campos requeridos
                filtered_products = [
                    {
                        "id": product.get("id"),
                        "name": product.get("name"),
                        "price": product.get("price")
                    }
                    for product in products
                    if isinstance(product.get("price"), (int, float)) and product.get("price", 0) > 100
                ]
                
                return filtered_products
                
        except httpx.TimeoutException as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Backoff exponencial: 1, 2, 4 segundos
                time.sleep(wait_time)
                continue
            else:
                raise
        except httpx.RequestError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
                continue
            else:
                raise
        except httpx.HTTPStatusError as e:
            # No reintentar errores HTTP (ej: 401, 404, 500)
            raise
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
                continue
            else:
                raise
    
    return []


# Ejemplo de uso
if __name__ == "__main__":
    try:
        products = get_expensive_products(token="tu_token_aqui")
        print(f"Encontrados {len(products)} productos con precio > 100")
        for product in products:
            print(f"  - {product['name']}: ${product['price']}")
    except httpx.TimeoutException:
        print("Error: Timeout después de múltiples intentos")
    except httpx.RequestError as e:
        print(f"Error de red: {e}")
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP {e.response.status_code}: {e}")
```

**Características principales:**

1. **Autenticación Bearer**: Usa header `Authorization: Bearer <token>`
2. **Filtrado**: Solo productos con `price > 100`
3. **Campos retornados**: Solo `id`, `name`, `price`
4. **Timeout**: 10 segundos por petición
5. **Retry con backoff exponencial**: 1s, 2s, 4s entre intentos (máx 3 intentos)
6. **Manejo de errores**: 
   - Reintenta en `TimeoutException` y `RequestError`
   - No reintenta en `HTTPStatusError` (errores del servidor/cliente)
7. **Dependencias**: Solo `httpx` (instalar con `pip install httpx`)