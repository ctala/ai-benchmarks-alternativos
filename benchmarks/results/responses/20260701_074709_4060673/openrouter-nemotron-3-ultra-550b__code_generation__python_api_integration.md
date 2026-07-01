# Nemotron 3 Ultra 550B — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.46 | quality: 9.34
- latency_total: 9.648s | tokens_per_second: 115.7
- input_tokens: 118 | output_tokens: 1116

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any


def fetch_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API con retry y backoff exponencial.
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
        Lista de dicts con {id, name, price} de productos filtrados
        
    Raises:
        httpx.HTTPStatusError: Si la respuesta tiene status code de error (4xx, 5xx)
        httpx.RequestError: Si falla la conexión tras todos los reintentos
        ValueError: Si la respuesta no es JSON válido o estructura inesperada
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    timeout = httpx.Timeout(10.0, connect=5.0)
    max_retries = 3
    base_delay = 1.0  # segundos
    
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                
                # Validar que la respuesta sea una lista
                if not isinstance(data, list):
                    raise ValueError(f"Se esperaba lista, recibido: {type(data).__name__}")
                
                # Filtrar y transformar
                result = []
                for product in data:
                    if not isinstance(product, dict):
                        continue
                    
                    price = product.get("price")
                    if isinstance(price, (int, float)) and price > 100:
                        result.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": price
                        })
                
                return result
                
        except httpx.TimeoutException as e:
            last_exception = e
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                continue
            raise httpx.RequestError(f"Timeout tras {max_retries} intentos") from e
            
        except httpx.NetworkError as e:
            last_exception = e
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                continue
            raise httpx.RequestError(f"Error de red tras {max_retries} intentos") from e
            
        except httpx.HTTPStatusError:
            # No reintentar en errores 4xx/5xx (salvo 5xx transitorios si se desea)
            raise
            
        except ValueError:
            # Error de parsing JSON o estructura inválida - no reintentar
            raise
    
    # Si se agotan reintentos
    raise httpx.RequestError("Máximo de reintentos alcanzado") from last_exception


# Ejemplo de uso
if __name__ == "__main__":
    try:
        products = fetch_expensive_products("tu_bearer_token_aqui")
        for p in products:
            print(f"{p['id']}: {p['name']} - ${p['price']}")
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP {e.response.status_code}: {e.response.text}")
    except httpx.RequestError as e:
        print(f"Error de conexión: {e}")
    except ValueError as e:
        print(f"Error de datos: {e}")
```

**Puntos clave:**

| Aspecto | Implementación |
|---------|----------------|
| **Auth** | Header `Authorization: Bearer <token>` |
| **Timeout** | 10s total, 5s conexión (`httpx.Timeout`) |
| **Retry** | 3 intentos con backoff: 1s → 2s → 4s |
| **Errores red/timeout** | Se reintentan con backoff exponencial |
| **Errores HTTP 4xx/5xx** | No se reintentan (fallan rápido) |
| **Filtrado** | `price > 100` (int/float) |
| **Salida** | Solo `{id, name, price}` |

**Dependencias:** Solo `httpx` (incluido en `httpx[cli]` o `pip install httpx`).