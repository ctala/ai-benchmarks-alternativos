# Nemotron 3 Ultra 550B — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.34 | quality: 9.52
- latency_total: 14.09s | tokens_per_second: 79.8
- input_tokens: 118 | output_tokens: 1124
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
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API con retry y backoff exponencial.
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
        Lista de dicts con {id, name, price} de productos filtrados
        
    Raises:
        httpx.HTTPStatusError: Si la respuesta tiene status code 4xx/5xx tras reintentos
        httpx.RequestError: Si hay error de red tras reintentos
        ValueError: Si la respuesta no es JSON válido o estructura inesperada
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    timeout = httpx.Timeout(10.0, connect=5.0)
    max_retries = 3
    base_delay = 1.0  # segundos
    
    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
            data = response.json()
            
            # Validar que sea una lista
            if not isinstance(data, list):
                raise ValueError(f"Se esperaba lista, recibido: {type(data).__name__}")
            
            # Filtrar y transformar
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in data
                if isinstance(p, dict) 
                and all(k in p for k in ("id", "name", "price"))
                and isinstance(p["price"], (int, float))
                and p["price"] > 100
            ]
            
            logger.info(f"Éxito: {len(filtered)} productos con precio > 100")
            return filtered
            
        except httpx.TimeoutException as e:
            logger.warning(f"Intento {attempt}/{max_retries} - Timeout: {e}")
        except httpx.HTTPStatusError as e:
            # No reintentar en 4xx (errores de cliente), solo 5xx
            if 400 <= e.response.status_code < 500:
                logger.error(f"Error cliente (no reintentable): {e.response.status_code}")
                raise
            logger.warning(f"Intento {attempt}/{max_retries} - HTTP {e.response.status_code}: {e}")
        except httpx.RequestError as e:
            logger.warning(f"Intento {attempt}/{max_retries} - Error de red: {e}")
        except (ValueError, KeyError) as e:
            logger.error(f"Error procesando respuesta: {e}")
            raise
        
        # Backoff exponencial antes del siguiente intento
        if attempt < max_retries:
            delay = base_delay * (2 ** (attempt - 1))
            logger.info(f"Reintentando en {delay}s...")
            time.sleep(delay)
    
    # Si llegamos aquí, se agotaron los reintentos
    raise httpx.RequestError(f"Falló tras {max_retries} intentos", request=None)


# Ejemplo de uso
if __name__ == "__main__":
    try:
        products = fetch_expensive_products("tu_token_aqui")
        for p in products:
            print(f"{p['id']}: {p['name']} - ${p['price']}")
    except Exception as e:
        print(f"Error: {e}")
```

**Puntos clave:**

| Característica | Implementación |
|----------------|----------------|
| **Auth Bearer** | Header `Authorization: Bearer <token>` |
| **Timeout** | 10s total, 5s conexión (`httpx.Timeout`) |
| **Retry** | 3 intentos con backoff 1s → 2s → 4s |
| **Filtrado** | `price > 100` + validación de tipos/keys |
| **Errores 4xx** | No reintenta (error de cliente) |
| **Errores 5xx/red** | Reintenta con backoff |
| **Sin deps extra** | Solo `httpx` (stdlib: `time`, `logging`, `typing`) |