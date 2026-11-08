# Kimi K2 — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.22 | quality: 9.52
- latency_total: 23.173s | tokens_per_second: 43.7
- input_tokens: 116 | output_tokens: 1013
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Escribe una funcion Python que:
1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5. Incluya retry con backoff exponencial (max 3 intentos)

Usa httpx y no dependencias externas adicionales.


## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Optional


def get_expensive_products(token: str) -> List[Dict[str, object]]:
    """
    Obtiene productos con precio > 100 de la API.
    
    Args:
        token: Token Bearer para autenticación
    
    Returns:
        Lista de diccionarios con {id, name, price}
    
    Raises:
        httpx.HTTPStatusError: Si la API retorna error después de reintentos
        httpx.NetworkError: Si hay errores de red persistentes
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    base_delay = 1  # segundos
    
    last_exception: Optional[Exception] = None
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                
                # Asumimos que la respuesta es una lista de productos
                # o un dict con key 'products'
                products = data if isinstance(data, list) else data.get("products", [])
                
                # Filtrar y transformar
                result = [
                    {
                        "id": p["id"],
                        "name": p["name"],
                        "price": p["price"]
                    }
                    for p in products
                    if p.get("price", 0) > 100
                ]
                
                return result
                
        except httpx.TimeoutException as e:
            last_exception = e
            # Timeout: reintentar con backoff
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)  # 1, 2, 4 segundos
                time.sleep(delay)
                
        except httpx.NetworkError as e:
            last_exception = e
            # Error de red: reintentar con backoff
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                
        except httpx.HTTPStatusError as e:
            # Error HTTP (4xx, 5xx): reintentar solo si es 5xx
            if e.response.status_code >= 500 and attempt < max_retries - 1:
                last_exception = e
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
            else:
                # 4xx o último intento fallido
                raise
                
        except (KeyError, TypeError) as e:
            # Error de formato de datos: no reintentar
            raise ValueError(f"Formato de respuesta inválido: {e}")
    
    # Se agotaron los reintentos
    raise last_exception if last_exception else RuntimeError("Error desconocido")


# Ejemplo de uso
if __name__ == "__main__":
    try:
        products = get_expensive_products("tu-token-aqui")
        print(f"Encontrados {len(products)} productos caros")
        for p in products[:3]:  # Mostrar primeros 3
            print(f"  - {p['name']}: ${p['price']}")
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP: {e.response.status_code}")
    except httpx.NetworkError as e:
        print(f"Error de red: {e}")
    except Exception as e:
        print(f"Error: {e}")
```

## Características implementadas:

| Requerimiento | Implementación |
|-------------|---------------|
| GET con Bearer token | `headers = {"Authorization": f"Bearer {token}"}` |
| Timeout 10s | `httpx.Client(timeout=10.0)` |
| Filtro price > 100 | Condición en list comprehension |
| Retry 3 intentos | Loop `for attempt in range(3)` |
| Backoff exponencial | `delay = 1 * (2 ** attempt)` → 1s, 2s, 4s |
| Manejo de errores | Excepciones específicas de `httpx` |

## Notas:

- **Reintento inteligente**: Solo reintenta en errores de red, timeout y errores 5xx del servidor. Los 4xx (como 401 Unauthorized) no se reintentan.
- **Cierre de conexiones**: Usa `with httpx.Client()` para garantizar el cierre adecuado.
- **Flexibilidad**: Soporta respuesta como lista directa o envuelta en `{"products": [...]}`.