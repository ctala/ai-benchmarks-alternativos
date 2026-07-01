# Nemotron 3 Ultra 550B — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.46 | quality: 7.87
- latency_total: 5.906s | tokens_per_second: 164.6
- input_tokens: 118 | output_tokens: 972

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
        httpx.HTTPStatusError: Si la respuesta tiene status >= 400
        httpx.RequestError: Si falla la conexión tras reintentos
        ValueError: Si el token es inválido o la respuesta no es JSON válido
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
                
                products = response.json()
                
                if not isinstance(products, list):
                    raise ValueError("La respuesta no es una lista de productos")
                
                filtered = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p, dict)
                    and all(k in p for k in ("id", "name", "price"))
                    and isinstance(p["price"], (int, float))
                    and p["price"] > 100
                ]
                
                return filtered
                
        except httpx.TimeoutException as e:
            if attempt == max_retries - 1:
                raise httpx.RequestError(f"Timeout tras {max_retries} intentos") from e
            
        except httpx.HTTPStatusError as e:
            # No reintentar en errores 4xx (salvo 429)
            if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                raise
            if attempt == max_retries - 1:
                raise
                
        except (httpx.RequestError, ValueError) as e:
            if attempt == max_retries - 1:
                raise
        
        # Backoff exponencial: 1s, 2s, 4s...
        delay = base_delay * (2 ** attempt)
        time.sleep(delay)
    
    raise httpx.RequestError("Se agotaron los reintentos")
```

**Uso:**

```python
token = "tu-bearer-token-aqui"
try:
    productos = fetch_expensive_products(token)
    for p in productos:
        print(f"{p['id']}: {p['name']} - ${p['price']}")
except httpx.HTTPStatusError as e:
    print(f"Error HTTP {e.response.status_code}: {e.response.text}")
except httpx.RequestError as e:
    print(f"Error de red: {e}")
except ValueError as e:
    print(f"Error de datos: {e}")
```

**Detalles de implementación:**

| Aspecto | Detalle |
|---------|---------|
| Timeout | 10s total, 5s conexión |
| Reintentos | 3 (exponencial: 1s, 2s, 4s) |
| Errores reintentables | Timeout, 5xx, 429, errores de red |
| Errores no reintentables | 4xx (salvo 429), JSON inválido, estructura inesperada |
| Validación | Verifica que `price` sea numérico y existan claves requeridas |