# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/python_api_integration

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.79 | quality: 9.28
- latency_total: 8.366s | tokens_per_second: 99.4
- input_tokens: 112 | output_tokens: 832
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos, utilizando `httpx` y sin dependencias externas adicionales:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 de la API, usando autenticación Bearer.
    
    Args:
        bearer_token: Token de autenticación Bearer.
        
    Returns:
        Lista de dicts con {id, name, price} para productos con precio > 100.
        
    Raises:
        httpx.HTTPError: Si ocurre un error tras los reintentos.
        ValueError: Si la respuesta no contiene datos válidos.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    
    max_retries = 3
    base_delay = 1.0  # segundos
    
    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=httpx.Timeout(10.0)) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                
                # Asegurar que data es una lista
                if not isinstance(data, list):
                    raise ValueError("La respuesta no es una lista de productos")
                
                # Filtrar productos con precio > 100
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
                
        except (httpx.RequestError, httpx.TimeoutException) as e:
            if attempt == max_retries:
                raise httpx.HTTPError(f"Error tras {max_retries} intentos: {e}") from e
            # Esperar con backoff exponencial
            delay = base_delay * (2 ** (attempt - 1))
            time.sleep(delay)
        except (ValueError, KeyError) as e:
            # Errores lógicos o de datos (no se reintentan por defecto)
            raise ValueError(f"Error procesando datos: {e}") from e

# Nota: Esta función asume que la respuesta JSON es una lista de productos.
# Ajusta según el formato real de la API si es necesario.
```

### Características clave:
- ✅ Usa `httpx.Client` con timeout de 10 segundos (`httpx.Timeout(10.0)`).
- ✅ Autenticación Bearer: cabecera `Authorization: Bearer {token}`.
- ✅ Filtro: solo productos con `price > 100`.
- ✅ Retorno: lista de dicts `{id, name, price}`.
- ✅ Retries con **backoff exponencial**: `1s → 2s → 4s` (máx 3 intentos).
- ✅ Manejo robusto de errores de red (`RequestError`, `TimeoutException`) y errores lógicos.
- ✅ Validación básica de estructura de datos (`isinstance(product, dict)`, etc.).

> 💡 **Nota**: Si la API devuelve los precios como strings (p. ej., `"120.5"`), puedes convertirlos:
> ```python
> try:
>     price = float(product.get("price"))
> except (TypeError, ValueError):
>     price = None
> ```
> Pero como no se especifica, se asume que son numéricos.

¿Quieres que la función también maneje paginación si la API la usa?