# Ministral 14B — code_generation/python_api_integration

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.05 | quality: 9.72
- latency_total: 9.493s | tokens_per_second: 98.6
- input_tokens: 105 | output_tokens: 936
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función en Python que cumple con todos los requisitos utilizando `httpx` para hacer la petición HTTP con autenticación Bearer, manejo de errores, retry con backoff exponencial y filtrado de productos:

```python
import httpx
import time
from typing import List, Dict

async def fetch_filtered_products(
    bearer_token: str,
    max_retries: int = 3,
    initial_timeout: float = 10.0
) -> List[Dict[str, str | float]]:
    """
    Fetches products from API, filters those with price > 100, and returns a list of dicts with id, name, price.

    Args:
        bearer_token: Authentication token for Bearer token scheme
        max_retries: Maximum number of retry attempts (default: 3)
        initial_timeout: Initial timeout in seconds (default: 10.0)

    Returns:
        List of dictionaries with product information (id, name, price) for products with price > 100

    Raises:
        Exception: If all retries fail
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    backoff_factor = 2  # Exponential backoff factor

    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient(timeout=initial_timeout) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()  # Raises HTTPError for bad responses

                products = response.json()

                # Filter products with price > 100 and extract required fields
                filtered_products = [
                    {"id": str(product["id"]), "name": product["name"], "price": product["price"]}
                    for product in products
                    if product.get("price", 0) > 100
                ]

                return filtered_products

        except (httpx.HTTPError, httpx.TimeoutException, httpx.RequestError) as e:
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(f"All retries failed. Last error: {str(e)}")

            # Exponential backoff
            wait_time = initial_timeout * (backoff_factor ** attempt)
            print(f"Attempt {attempt + 1} failed. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)

# Ejemplo de uso (asincrónico)
import asyncio

async def main():
    try:
        bearer_token = "tu_token_aqui"  # Reemplaza con tu token real
        products = await fetch_filtered_products(bearer_token)
        print("Productos filtrados:")
        for product in products:
            print(product)
    except Exception as e:
        print(f"Error: {str(e)}")

# Para ejecutar el ejemplo
# asyncio.run(main())
```

### Características de la implementación:

1. **Autenticación Bearer**: Usa el token en el header de autorización.
2. **Filtro de precios**: Solo incluye productos con precio > 100.
3. **Estructura de respuesta**: Devuelve una lista de diccionarios con solo `id`, `name` y `price`.
4. **Manejo de errores**:
   - Errores de red (`httpx.RequestError`)
   - Timeouts (`httpx.TimeoutException`)
   - Respuestas HTTP no exitosas (`httpx.HTTPError`)
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos (configurable)
   - Tiempo de espera se duplica en cada intento (10s, 20s, 40s)
6. **Uso de httpx**: Solo depende de `httpx` (y `asyncio` para la ejecución asincrónica).

### Notas importantes:
- La función es asincrónica (usa `async/await`) para mejor manejo de operaciones I/O.
- El ejemplo incluye un `main()` para demostración, pero puedes adaptarlo a tu caso de uso.
- Asegúrate de instalar `httpx` con `pip install httpx` si no lo tienes.
- Para uso síncrono, podrías crear una versión con `httpx.Client` en lugar de `AsyncClient`.