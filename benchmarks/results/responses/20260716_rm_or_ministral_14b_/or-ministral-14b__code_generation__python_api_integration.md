# Ministral 14B — code_generation/python_api_integration

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 8.96 | quality: 9.72
- latency_total: 19.181s | tokens_per_second: 57.2
- input_tokens: 105 | output_tokens: 1098
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función en Python que cumple con todos los requisitos utilizando `httpx` para gestionar las peticiones HTTP:

```python
import httpx
import time
from typing import List, Dict

def fetch_expensive_products(bearer_token: str, max_retries: int = 3) -> List[Dict[str, str | float]]:
    """
    Realiza una petición GET a la API para obtener productos con precio > 100,
    con autenticación Bearer token, manejo de errores y retry con backoff exponencial.

    Args:
        bearer_token: Token de autenticación Bearer.
        max_retries: Número máximo de reintentos (por defecto 3).

    Returns:
        Lista de diccionarios con {id, name, price} de productos filtrados.

    Raises:
        RuntimeError: Si fallan todos los intentos después de retry.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    backoff_factor = 1  # Factor para el backoff exponencial (en segundos)

    for attempt in range(1, max_retries + 1):
        try:
            # Realizar la petición con timeout
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)

                # Verificar código de estado OK
                response.raise_for_status()

                # Filtrar productos por precio > 100
                expensive_products = [
                    {"id": product["id"], "name": product["name"], "price": product["price"]}
                    for product in response.json()
                    if product.get("price", 0) > 100
                ]

                return expensive_products

        except httpx.TimeoutException:
            if attempt == max_retries:
                raise RuntimeError("Se agotaron los intentos. Timeout al conectar con la API.")
            wait_time = backoff_factor * (2 ** (attempt - 1))
            print(f"Timeout en intento {attempt}. Reintentando en {wait_time:.2f} segundos...")
            time.sleep(wait_time)

        except httpx.HTTPStatusError as e:
            if attempt == max_retries:
                raise RuntimeError(f"Error HTTP persistente: {e}")
            wait_time = backoff_factor * (2 ** (attempt - 1))
            print(f"Error HTTP {e.response.status_code} en intento {attempt}. Reintentando en {wait_time:.2f} segundos...")
            time.sleep(wait_time)

        except (httpx.RequestError, ValueError) as e:
            if attempt == max_retries:
                raise RuntimeError(f"Error inesperado: {e}")
            wait_time = backoff_factor * (2 ** (attempt - 1))
            print(f"Error inesperado en intento {attempt}. Reintentando en {wait_time:.2f} segundos...")
            time.sleep(wait_time)

    raise RuntimeError("Fallaron todos los intentos después del retry.")

# Ejemplo de uso:
# products = fetch_expensive_products("tu_token_bearer_aqui")
# print(products)
```

### Explicación:

1. **Autenticación Bearer**:
   El token se incluye en el header `Authorization` como "Bearer {token}".

2. **Filtro de productos**:
   Se filtran los productos con `price > 100` usando una lista por comprensión.

3. **Manejo de errores y timeout**:
   - `httpx.TimeoutException`: Si la petición tarda más de 10 segundos.
   - `httpx.HTTPStatusError`: Si la API devuelve un código de error (4xx, 5xx).
   - `ValueError`: Si la respuesta no es JSON válido.
   - `httpx.RequestError`: Para otros errores de red.

4. **Retry con backoff exponencial**:
   El tiempo de espera entre reintentos se calcula como:
   `wait_time = backoff_factor * 2^(n-1)`, donde `n` es el intento actual.
   Por ejemplo:
   - Intento 1: `1 * 2^0 = 1` segundo.
   - Intento 2: `1 * 2^1 = 2` segundos.
   - Intento 3: `1 * 2^2 = 4` segundos.

5. **Retorno**:
   Devuelve una lista de diccionarios con solo `{id, name, price}` de los productos filtrados.

### Dependencia:
Asegúrate de tener instalado `httpx` (si no lo tienes, ejecuta):
```bash
pip install httpx
```

### Notas adicionales:
- Usa `with httpx.Client(timeout=10.0)` para manejar el contexto de la conexión y el timeout de manera automática.
- Si prefieres un backoff más agresivo o personalizado, puedes ajustar `backoff_factor`. Por defecto es `1`, lo que da tiempos de espera de 1s, 2s, 4s, etc.