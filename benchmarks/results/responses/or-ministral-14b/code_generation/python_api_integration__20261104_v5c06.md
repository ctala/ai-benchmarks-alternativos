# Ministral 14B — code_generation/python_api_integration

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 8.83 | quality: 9.72
- latency_total: 18.711s | tokens_per_second: 49.4
- input_tokens: 105 | output_tokens: 925
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

Aquí tienes una función en Python que cumple con todos los requisitos utilizando `httpx` y manejo de errores con retry y backoff exponencial:

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
    Fetches products from API with Bearer token, filters by price > 100,
    and returns a list of dictionaries with {id, name, price}.

    Args:
        bearer_token: Bearer token for authentication
        max_retries: Maximum number of retry attempts
        initial_timeout: Initial timeout in seconds

    Returns:
        List of dictionaries with product info

    Raises:
        Exception: If all retries fail
    """
    url = "https://api.example.com/products"
    retry_delay = initial_timeout  # Start with initial timeout as base for backoff

    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient(timeout=initial_timeout) as client:
                response = await client.get(
                    url,
                    headers={"Authorization": f"Bearer {bearer_token}"}
                )
                response.raise_for_status()  # Raises HTTPError for 4XX/5XX responses

                products = response.json()
                if not isinstance(products, list):
                    raise ValueError("Unexpected API response format")

                # Filter and transform products
                filtered_products = [
                    {"id": str(p.get("id")), "name": p.get("name"), "price": p.get("price")}
                    for p in products
                    if p.get("price", 0) > 100
                ]

                return filtered_products

        except (httpx.HTTPError, httpx.TimeoutException, httpx.RequestError) as e:
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(f"All {max_retries} attempts failed: {str(e)}")

            # Exponential backoff with jitter
            retry_delay *= 2
            retry_delay += 0.1 * (1 + attempt)  # Add small jitter
            time.sleep(retry_delay)

    # This line is theoretically unreachable due to the raise in the loop
    raise Exception("Unexpected error in retry logic")

# Example usage (async context)
import asyncio

async def main():
    token = "your_bearer_token_here"
    try:
        products = await fetch_filtered_products(token)
        print(products)
    except Exception as e:
        print(f"Error: {e}")

# To run the example:
# asyncio.run(main())
```

### Características implementadas:

1. **Autenticación Bearer**: Usa el token en el header `Authorization`
2. **Filtro de precios**: Solo incluye productos con `price > 100`
3. **Formato de salida**: Devuelve una lista de diccionarios con solo `id`, `name` y `price`
4. **Manejo de errores**:
   - Timeouts (10 segundos inicial)
   - Errores de red (HTTPError, RequestError)
   - Errores de formato de respuesta
5. **Retry con backoff exponencial**:
   - Hasta 3 intentos por defecto
   - Tiempo de espera multiplicado por 2 cada intento
   - Añade pequeño jitter para evitar thundering herd
6. **Tipo seguro**: Usa type hints para mejor claridad

### Notas importantes:

1. La función es asíncrona (usa `async/await`) para mejor manejo de I/O
2. Usa `httpx.AsyncClient` que es más eficiente para operaciones de red
3. El backoff exponencial comienza con el timeout inicial (10s) y duplica cada intento
4. El jitter (pequeña variación aleatoria) ayuda a evitar que múltiples clientes se retry al mismo tiempo

Para usar esta función, necesitarás ejecutarla en un contexto asíncrono como se muestra en el ejemplo de `main()`. Si prefieres una versión síncrona, puedo adaptarla usando `httpx.Client` en lugar de `AsyncClient`.