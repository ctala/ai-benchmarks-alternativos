# Qwen 3.5 (Ollama Cloud default) — code_generation/python_api_integration

- model_id: `qwen3.5:cloud`
- success: True  | final: 8.08 | quality: 9.52
- latency_total: 14.072s | tokens_per_second: 69.6
- input_tokens: 113 | output_tokens: 980
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Optional

def fetch_products(
    token: str,
    base_url: str = "https://api.example.com",
    timeout: int = 10,
    max_retries: int = 3
) -> List[Dict]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna 
    solo id, name y price. Implementa retry con backoff exponencial.
    
    Args:
        token: Bearer token para autenticación
        base_url: URL base de la API
        timeout: Timeout en segundos para cada petición
        max_retries: Número máximo de intentos
    
    Returns:
        Lista de diccionarios con {id, name, price}
    
    Raises:
        httpx.RequestError: Si fallan todos los intentos
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(
                    f"{base_url}/products",
                    headers=headers
                )
                response.raise_for_status()
                
                products = response.json()
                
                filtered = [
                    {
                        "id": p["id"],
                        "name": p["name"],
                        "price": p["price"]
                    }
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]
                
                return filtered
                
        except httpx.TimeoutException as e:
            last_exception = e
        except httpx.NetworkError as e:
            last_exception = e
        except httpx.HTTPStatusError as e:
            if e.response.status_code >= 500:
                last_exception = e
            else:
                raise
        except (KeyError, TypeError, ValueError) as e:
            raise ValueError(f"Error procesando respuesta: {str(e)}")
        
        if attempt < max_retries - 1:
            wait_time = (2 ** attempt)
            time.sleep(wait_time)
    
    raise httpx.RequestError(
        f"Fallaron {max_retries} intentos",
        request=None
    ) from last_exception


# Ejemplo de uso
if __name__ == "__main__":
    try:
        products = fetch_products(token="tu_token_aqui")
        print(f"Productos encontrados: {len(products)}")
        for p in products:
            print(f"{p['id']}: {p['name']} - ${p['price']}")
    except httpx.RequestError as e:
        print(f"Error de red: {e}")
    except Exception as e:
        print(f"Error: {e}")
```

**Características principales:**

| Característica | Implementación |
|---------------|----------------|
| **Auth Bearer** | Header `Authorization: Bearer <token>` |
| **Timeout** | 10 segundos por petición |
| **Retry** | Máximo 3 intentos |
| **Backoff** | Exponencial: 1s, 2s, 4s |
| **Filtro** | `price > 100` |
| **Campos** | Solo `id`, `name`, `price` |
| **Errores 5xx** | Se reintentan |
| **Errores 4xx** | Se propagan inmediatamente |

**Instalación:**
```bash
pip install httpx
```