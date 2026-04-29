# Ministral 14B (NIM) — code_generation/python_api_integration

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 7.21 | quality: 8.88
- latency_total: 42.419s | tokens_per_second: 25.4
- input_tokens: 105 | output_tokens: 1076
- judge_score: 4.2 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos utilizando `httpx` para hacer la petición HTTP, con manejo de errores, retry con backoff exponencial y filtrado de resultados:

```python
import httpx
from typing import List, Dict
import time

async def get_products_above_price() -> List[Dict[str, str | int | float]]:
    """
    Realiza una solicitud GET a la API de productos con autenticación Bearer,
    filtra productos con precio > 100 y retorna solo {id, name, price}.

    Parámetros:
        - No requiere parámetros, usa un token hardcodeado (en producción,
          esto debería configurarse de forma segura).

    Retorna:
        Lista de diccionarios con los productos filtrados.

    Maneja:
        - Errores de red y timeout (10 segundos).
        - Retry con backoff exponencial (máx. 3 intentos).
    """
    url = "https://api.example.com/products"
    token = "tu_bearer_token_aqui"  # Cambiar por el token real

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    max_retries = 3
    base_delay = 1  # segundos

    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(url, headers=headers)

                # Verificar si la respuesta es exitosa (2xx)
                response.raise_for_status()

                products = response.json()

                # Filtrar productos con precio > 100 y retornar solo {id, name, price}
                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

                return filtered_products

        except (httpx.TimeoutException, httpx.RequestError) as e:
            if attempt == max_retries - 1:
                raise  # Re-lanzar el error si es el último intento
            delay = base_delay * (2 ** attempt)  # Backoff exponencial
            print(f"Intento {attempt + 1} fallido. Retry en {delay} segundos...")
            time.sleep(delay)

        except httpx.HTTPStatusError as e:
            # Manejar errores de HTTP (4xx, 5xx)
            if attempt == max_retries - 1:
                raise  # Re-lanzar el error si es el último intento
            delay = base_delay * (2 ** attempt)
            print(f"Error HTTP {e.response.status_code}. Retry en {delay} segundos...")
            time.sleep(delay)

        except (ValueError, KeyError) as e:
            # Manejar errores en el parseo de JSON o datos faltantes
            raise ValueError("Error al procesar la respuesta de la API") from e

# Ejemplo de uso (asíncrono)
import asyncio

async def main():
    try:
        products = await get_products_above_price()
        print(products)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Explicación:
1. **Autenticación Bearer**: Se incluye el token en el header `Authorization`.
2. **Filtrado**: Se usan comprensión de listas para filtrar productos con `price > 100` y retornar solo `{id, name, price}`.
3. **Timeout y errores de red**: Se configura un timeout de 10 segundos con `httpx.AsyncClient(timeout=10.0)` y se manejan `httpx.TimeoutException` y `httpx.RequestError`.
4. **Retry con backoff exponencial**:
   - Máximo 3 intentos (`max_retries`).
   - Tiempo de espera entre intentos se calcula como `base_delay * (2 ** attempt)`.
5. **Manejo de errores adicionales**:
   - `HTTPStatusError` para errores HTTP (4xx/5xx).
   - `ValueError`/`KeyError` para problemas en el parseo de JSON o datos faltantes.

### Notas:
- El token debe sustituirse por el token real de autenticación.
- La función es asíncrona (`async def`) para aprovechar `httpx.AsyncClient`, pero puedes adaptarla a versión síncrona con `httpx.Client` si prefieres.
- En producción, evita hardcodear el token. Usa variables de entorno o un gestor de configuración seguro. Ejemplo con `python-dotenv`:
  ```python
  from dotenv import load_dotenv
  import os
  load_dotenv()
  token = os.getenv("BEARER_TOKEN")
  ```