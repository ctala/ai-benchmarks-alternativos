# Nemotron 3 Ultra 550B (NIM) — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.66 | quality: 8.67
- latency_total: 22.021s | tokens_per_second: 49.5
- input_tokens: 118 | output_tokens: 1091

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any


def fetch_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API.
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
        Lista de diccionarios con {id, name, price}
        
    Raises:
        httpx.HTTPStatusError: Si la respuesta tiene status code 4xx/5xx
        httpx.RequestError: Si falla la conexión tras reintentos
        ValueError: Si la respuesta no es JSON válido o estructura inesperada
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    timeout = httpx.Timeout(10.0, connect=5.0)
    
    max_retries = 3
    base_delay = 1.0  # segundos
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                
                # Validar que sea una lista
                if not isinstance(data, list):
                    raise ValueError(f"Se esperaba lista, recibido: {type(data).__name__}")
                
                # Filtrar y transformar
                result = []
                for product in data:
                    if not isinstance(product, dict):
                        continue
                    
                    price = product.get("price")
                    if price is None:
                        continue
                    
                    try:
                        if float(price) > 100:
                            result.append({
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": float(price)
                            })
                    except (TypeError, ValueError):
                        continue
                
                return result
                
        except httpx.TimeoutException as e:
            if attempt == max_retries - 1:
                raise httpx.RequestError(f"Timeout tras {max_retries} intentos") from e
            
        except httpx.HTTPStatusError as e:
            # No reintentar en 4xx (errores de cliente)
            if 400 <= e.response.status_code < 500:
                raise
            # Reintentar en 5xx (errores de servidor)
            if attempt == max_retries - 1:
                raise
                
        except httpx.RequestError as e:
            if attempt == max_retries - 1:
                raise
                
        except ValueError as e:
            # Error de parsing JSON o estructura inválida - no reintentar
            raise
        
        # Backoff exponencial: 1s, 2s, 4s...
        delay = base_delay * (2 ** attempt)
        time.sleep(delay)
    
    # Nunca debería llegar aquí, pero por seguridad
    raise httpx.RequestError("Máximo de reintentos agotado")
```

**Uso:**

```python
if __name__ == "__main__":
    token = "tu-bearer-token-aqui"
    
    try:
        products = fetch_expensive_products(token)
        for p in products:
            print(f"{p['id']}: {p['name']} - ${p['price']:.2f}")
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP {e.response.status_code}: {e.response.text}")
    except httpx.RequestError as e:
        print(f"Error de red: {e}")
    except ValueError as e:
        print(f"Error de datos: {e}")
```

**Puntos clave:**

| Aspecto | Implementación |
|---------|----------------|
| **Auth** | Header `Authorization: Bearer <token>` |
| **Timeout** | 10s total, 5s conexión |
| **Retry** | 3 intentos, backoff 1s → 2s → 4s |
| **Reintentos** | Solo en timeout, 5xx, errores de red |
| **No reintenta** | 4xx, JSON inválido, estructura inesperada |
| **Filtrado** | `price > 100` con validación de tipos |
| **Salida** | Solo `{id, name, price}` (price como float) |