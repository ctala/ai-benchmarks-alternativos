# Nemotron 3 Ultra 550B — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.33 | quality: 9.08
- latency_total: 6.607s | tokens_per_second: 129.0
- input_tokens: 118 | output_tokens: 852
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any


def fetch_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API con reintentos y backoff exponencial.
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
        Lista de diccionarios con {id, name, price}
        
    Raises:
        httpx.HTTPStatusError: Si la respuesta tiene status code 4xx/5xx tras reintentos
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
            
            if not isinstance(data, list):
                raise ValueError("Se esperaba una lista de productos en la respuesta")
            
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in data
                if isinstance(p, dict) and p.get("price", 0) > 100
            ]
            return filtered
            
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
        except (KeyError, TypeError, ValueError) as e:
            raise ValueError(f"Error procesando respuesta: {e}") from e
    
    return []  # Nunca se alcanza por el raise en el último intento
```

**Uso:**

```python
try:
    products = fetch_expensive_products("tu-bearer-token-aqui")
    for p in products:
        print(f"{p['id']}: {p['name']} - ${p['price']}")
except httpx.HTTPStatusError as e:
    print(f"Error HTTP {e.response.status_code}: {e}")
except httpx.RequestError as e:
    print(f"Error de red: {e}")
except ValueError as e:
    print(f"Error de datos: {e}")
```

**Detalles de implementación:**

| Aspecto | Detalle |
|---------|---------|
| Timeout | 10s total, 5s conexión |
| Reintentos | 3 (intentos 0, 1, 2) |
| Backoff | 1s, 2s, 4s (exponencial base 2) |
| Errores de red | `httpx.RequestError` (DNS, conexión, timeout) |
| Errores HTTP | `httpx.HTTPStatusError` (4xx, 5xx) |
| Validación | Verifica que sea lista y que cada item tenga `price` numérico |