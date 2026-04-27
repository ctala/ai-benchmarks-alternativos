# Grok 4.20 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.20`
- success: True  | final: 7.33 | quality: 9.52
- latency_total: 14.967s | tokens_per_second: 56.1
- input_tokens: 217 | output_tokens: 839
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
                except (httpx.RequestError, httpx.TimeoutException) as e:
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
def get_filtered_products(token: str) -> List[Dict]:
    """
    Obtiene productos filtrados de la API.
    
    Args:
        token (str): Bearer token para autenticación
    
    Returns:
        List[Dict]: Lista de productos con {id, name, price}
    
    Raises:
        httpx.RequestError: En caso de error de red o timeout
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
            
            # Filtrar y transformar
            filtered_products = [
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"]
                }
                for product in products
                if isinstance(product.get("price"), (int, float)) and product["price"] > 100
            ]
            
            return filtered_products
            
    except httpx.HTTPStatusError as e:
        raise httpx.RequestError(f"Error HTTP {e.response.status_code}: {e.response.text}") from e
    except httpx.TimeoutException as e:
        raise httpx.RequestError("Timeout al conectar con la API") from e
    except httpx.RequestError as e:
        raise httpx.RequestError(f"Error de conexión: {str(e)}") from e
    except (KeyError, TypeError) as e:
        raise ValueError(f"Error en la estructura de datos de la API: {str(e)}") from e


# Ejemplo de uso:
if __name__ == "__main__":
    token = "tu_token_aqui"
    try:
        productos = get_filtered_products(token)
        print(f"Se obtuvieron {len(productos)} productos con precio > 100")
        for p in productos[:3]:  # Mostrar primeros 3
            print(p)
    except Exception as e:
        print(f"Error: {e}")
```

### Características implementadas:

- **Autenticación Bearer** con `Authorization` header
- **Timeout de 10 segundos** configurado explícitamente
- **Retry con backoff exponencial** (1s, 2s, 4s)
- **Manejo completo de errores** (network, timeout, HTTP, datos inválidos)
- **Filtrado por precio > 100**
- **Retorna solo los campos solicitados**: `id`, `name`, `price`
- **Usa solo `httpx`** (sin dependencias adicionales)
- **Type hints** completos
- **Context manager** para el cliente HTTP

Puedes ajustar el `base_delay` si quieres un backoff más agresivo o conservador.