# Nemotron 3 Ultra 550B (NIM) — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.83 | quality: 8.67
- latency_total: 11.073s | tokens_per_second: 88.5
- input_tokens: 118 | output_tokens: 980

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
    base_backoff = 1.0  # segundos

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                
                # Validar estructura esperada
                if not isinstance(data, list):
                    raise ValueError("Se esperaba una lista de productos en la respuesta")
                
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
            if attempt == max_retries - 1:
                raise httpx.RequestError(f"Timeout tras {max_retries} intentos") from e
        except httpx.NetworkError as e:
            if attempt == max_retries - 1:
                raise httpx.RequestError(f"Error de red tras {max_retries} intentos") from e
        except httpx.HTTPStatusError:
            # No reintentar en 4xx (error cliente), solo 5xx
            if 400 <= response.status_code < 500:
                raise
            if attempt == max_retries - 1:
                raise
        except ValueError:
            # Error de parsing/validación - no reintentar
            raise

        # Backoff exponencial: 1s, 2s, 4s...
        time.sleep(base_backoff * (2 ** attempt))

    # Nunca debería llegar aquí, pero por seguridad
    raise httpx.RequestError("Se agotaron los reintentos")
```

**Uso:**

```python
token = "tu-bearer-token-aqui"
try:
    productos = fetch_expensive_products(token)
    for p in productos:
        print(f"{p['id']}: {p['name']} - ${p['price']}")
except httpx.RequestError as e:
    print(f"Error de conexión: {e}")
except httpx.HTTPStatusError as e:
    print(f"Error HTTP {e.response.status_code}: {e.response.text}")
except ValueError as e:
    print(f"Datos inválidos: {e}")
```

**Notas:**
- `httpx` ya viene con `retry` logic built-in desde v0.23+, pero esta implementación manual da control total sobre backoff y qué errores reintentar
- `Timeout(10.0, connect=5.0)`: 10s total, 5s para conectar
- No reintenta en 4xx (errores de cliente como 401, 404)
- Valida que `price` sea numérico antes de comparar