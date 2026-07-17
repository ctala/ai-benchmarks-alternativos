# Grok 4.20 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.20`
- success: True  | final: 8.59 | quality: 9.52
- latency_total: 6.016s | tokens_per_second: 143.8
- input_tokens: 278 | output_tokens: 865
- judge_score: 4.8 | justificación: 

## Respuesta completa

**✅ Solución:**

```python
import httpx
from typing import List, Dict
import time
from functools import wraps


def retry_with_backoff(max_retries: int = 3, base_delay: float = 1.0):
    """Decorador para retry con backoff exponencial."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (httpx.TimeoutException, httpx.NetworkError, httpx.ConnectError) as e:
                    last_exception = e
                    if attempt == max_retries - 1:
                        break
                    
                    delay = base_delay * (2 ** attempt)
                    print(f"Intento {attempt + 1} fallido. Reintentando en {delay:.1f}s...")
                    time.sleep(delay)
            
            raise last_exception
        return wrapper
    return decorator


@retry_with_backoff(max_retries=3, base_delay=1.0)
def get_expensive_products(token: str) -> List[Dict]:
    """
    Obtiene productos con precio > 100 usando autenticación Bearer.
    
    Args:
        token (str): Token de autenticación Bearer
    
    Returns:
        List[Dict]: Lista de productos con solo id, name y price
    
    Raises:
        httpx.RequestError: En caso de errores de red o timeout
        ValueError: Si la respuesta no es JSON válido
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    timeout = httpx.Timeout(10.0, connect=5.0)
    
    try:
        with httpx.Client(timeout=timeout) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            
            products = response.json()
            
            # Filtrar y mapear solo los campos requeridos
            filtered_products = [
                {
                    "id": product.get("id"),
                    "name": product.get("name"),
                    "price": product.get("price")
                }
                for product in products
                if isinstance(product.get("price"), (int, float)) and product.get("price") > 100
            ]
            
            return filtered_products
            
    except httpx.HTTPStatusError as e:
        raise httpx.RequestError(f"Error HTTP {e.response.status_code}: {e.response.text}") from e
    except httpx.TimeoutException as e:
        raise httpx.RequestError("Timeout al conectar con la API") from e
    except httpx.RequestError as e:
        raise httpx.RequestError(f"Error de red: {str(e)}") from e
    except (ValueError, TypeError, KeyError) as e:
        raise ValueError(f"Error procesando la respuesta JSON: {str(e)}") from e


# Ejemplo de uso:
if __name__ == "__main__":
    try:
        token = "tu_token_aqui"
        productos_caros = get_expensive_products(token)
        print(f"Se encontraron {len(productos_caros)} productos con precio > 100")
        for p in productos_caros[:3]:  # Mostrar primeros 3
            print(p)
    except Exception as e:
        print(f"Error: {e}")
```

### Características incluidas:

- **Autenticación Bearer** correcta
- **Timeout de 10 segundos** configurado
- **Retry con backoff exponencial** (1s, 2s, 4s)
- **Manejo detallado de errores** (network, timeout, HTTP, JSON)
- **Filtrado por precio > 100**
- **Retorna solo** `id`, `name`, `price`
- **Uso de `httpx`** (recomendado sobre `requests`)
- **Type hints** completos
- **Context manager** para el cliente

¿Quieres también una versión **asíncrona** con `httpx.AsyncClient`?