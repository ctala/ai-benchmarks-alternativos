# Mistral-Nemotron (NIM) — code_generation/python_api_integration

- model_id: `mistralai/mistral-nemotron`
- success: True  | final: 7.7 | quality: 9.72
- latency_total: 16.215s | tokens_per_second: 52.5
- input_tokens: 105 | output_tokens: 852
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos usando `httpx` con manejo de errores, retries con backoff exponencial y filtros de productos:

```python
import httpx
import time
import random
from typing import List, Dict

async def get_expensive_products(bearer_token: str) -> List[Dict[str, any]]:
    """
    Obtiene productos con precio > 100 desde la API con autenticación Bearer.

    Args:
        bearer_token: Token de autenticación para la API

    Returns:
        Lista de diccionarios con productos filtrados (id, name, price)

    Raises:
        httpx.RequestError: Si fallan todos los intentos de conexión
    """
    max_retries = 3
    initial_delay = 1.0  # segundos
    timeout = httpx.Timeout(10.0)  # 10 segundos

    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                headers = {
                    "Authorization": f"Bearer {bearer_token}",
                    "Accept": "application/json"
                }

                response = await client.get(
                    "https://api.example.com/products",
                    headers=headers
                )

                # Check for HTTP errors
                response.raise_for_status()

                # Parse JSON response
                products = response.json()

                # Filter and transform products
                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p["price"] > 100
                ]

                return filtered_products

        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            if attempt == max_retries - 1:
                raise  # Re-raise the exception if it's the last attempt

            # Calculate exponential backoff with jitter
            delay = initial_delay * (2 ** attempt) * (1 + random.uniform(0, 0.1))
            await asyncio.sleep(delay)

    return []  # This line is theoretically unreachable but added for completeness

# Example usage (needs asyncio.run in Python 3.7+)
# async def main():
#     try:
#         products = await get_expensive_products("your_bearer_token_here")
#         print(f"Found {len(products)} expensive products")
#     except Exception as e:
#         print(f"Error: {str(e)}")

# asyncio.run(main())
```

### Explicación de los componentes:

1. **Autenticación Bearer**: Se incluye en los headers con `Authorization: Bearer {token}`
2. **Filtro de productos**: Usa una comprensión de lista para seleccionar solo productos con `price > 100`
3. **Transformación de datos**: Retorna solo los campos requeridos (`id`, `name`, `price`)
4. **Manejo de errores**:
   - `httpx.RequestError` para problemas de red
   - `httpx.HTTPStatusError` para errores HTTP (4xx/5xx)
5. **Retries con backoff**:
   - 3 intentos máximos
   - Retry delay: 1s, 2s, 4s (con un 10% de jitter aleatorio)
   - Timeout de 10 segundos para la petición
6. **Async/Await**: La función es asíncrona para no bloquear el hilo principal

Nota: Para usar esta función necesitas:
- Python 3.7+
- Tener instalado `httpx` (`pip install httpx`)
- Ejecutarla dentro de un contexto `asyncio` (como en el comentario de ejemplo)

Si necesitas una versión síncrona, podrías crear una envolvente con `asyncio.run()` pero ten en cuenta que esto no es recomendable para producción.