# Muse Spark 1.2 — code_generation/python_api_integration

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.39 | quality: 9.72
- latency_total: 13.157s | tokens_per_second: 167.3
- input_tokens: 99 | output_tokens: 2201
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

Aquí tienes una función completa que cumple los 5 requisitos usando solo `httpx`:

```python
import time
import httpx
from typing import List, Dict, Any

def get_filtered_products(token: str, max_retries: int = 3) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna solo id, name, price.
    
    Args:
        token: Bearer token para autenticación
        max_retries: Número máximo de intentos (default 3)
    
    Returns:
        Lista de dicts con formato {id, name, price}
    
    Raises:
        RuntimeError: Si falla después de todos los reintentos
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    last_exception = None

    for attempt in range(max_retries):
        try:
            # 1. GET con autenticación Bearer y 4. Timeout de 10 segundos
            response = httpx.get(url, headers=headers, timeout=10.0)
            
            # Lanza excepción si el status no es 2xx
            response.raise_for_status()
            
            data = response.json()
            
            # Soporta si la API retorna {"products": [...]} o directamente [...]
            if isinstance(data, dict) and "products" in data:
                products = data["products"]
            else:
                products = data

            # 2. Filtrar precio > 100 y 3. Retornar solo id, name, price
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p["price"] > 100
            ]
            
            return filtered

        except (httpx.RequestError, httpx.TimeoutException) as e:
            # 4. Errores de red y timeout
            last_exception = e
            print(f"Intento {attempt + 1}/{max_retries} falló por error de red/timeout: {e}")

        except httpx.HTTPStatusError as e:
            last_exception = e
            # Reintentar solo en errores temporales 5xx o 429
            if e.response.status_code in [429, 500, 502, 503, 504]:
                print(f"Intento {attempt + 1}/{max_retries} falló con status {e.response.status_code}: {e}")
            else:
                # Error 4xx no recuperable, no reintentar
                print(f"Error HTTP no recuperable {e.response.status_code}: {e.response.text}")
                raise RuntimeError(f"Error HTTP {e.response.status_code}") from e
        
        except (ValueError, KeyError) as e:
            # Error al parsear JSON o estructura inesperada
            raise RuntimeError(f"Error procesando la respuesta de la API: {e}") from e

        # 5. Retry con backoff exponencial si no es el último intento
        if attempt < max_retries - 1:
            backoff = 2 ** attempt  # 1s, 2s, 4s
            print(f"Reintentando en {backoff} segundos...")
            time.sleep(backoff)

    # Si llegamos aquí, todos los intentos fallaron
    raise RuntimeError(f"Fallo después de {max_retries} intentos") from last_exception


# Ejemplo de uso
if __name__ == "__main__":
    TOKEN = "tu_bearer_token_aqui"
    try:
        productos = get_filtered_products(TOKEN)
        print(productos)
        # Ejemplo salida: [{'id': 1, 'name': 'Laptop', 'price': 1200}, ...]
    except RuntimeError as e:
        print(f"No se pudieron obtener los productos: {e}")
```

### Cómo cumple cada punto:

1.  **GET + Bearer:** `httpx.get(url, headers={"Authorization": f"Bearer {token}"})`
2.  **Filtro:** `if p["price"] > 100`
3.  **Retorno:** List comprehension que crea nuevos dicts solo con `id, name, price`
4.  **Manejo de errores y timeout:** `timeout=10.0` y `except (httpx.RequestError, httpx.TimeoutException, httpx.HTTPStatusError)`
5.  **Retry con backoff exponencial:** Bucle `for attempt in range(3)` + `time.sleep(2 ** attempt)` -> espera 1s, 2s y 4s entre reintentos. Solo reintenta en errores de red/timeout y errores 5xx/429.

> **Nota para versión asíncrona:** Si usas `async/await`, cambia `httpx.get` por `httpx.AsyncClient`, `time.sleep` por `asyncio.sleep` y define la función como `async def`.