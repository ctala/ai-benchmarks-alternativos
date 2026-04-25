# Devstral 2 (Dic 2025) — code_generation/python_api_integration

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.7 | quality: 9.72
- latency_total: 10.6s | tokens_per_second: 74.6
- input_tokens: 105 | output_tokens: 791
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos utilizando `httpx` y manejo de errores con retry y backoff exponencial:

```python
import httpx
import time
from typing import List, Dict

def get_expensive_products(bearer_token: str) -> List[Dict]:
    """
    Obtiene productos con precio > 100 de la API con autenticación Bearer.

    Args:
        bearer_token: Token de autenticación Bearer.

    Returns:
        Lista de diccionarios con {id, name, price} de productos caros.

    Raises:
        Exception: Si fallan todos los intentos de conexión.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    timeout = 10.0
    max_retries = 3
    base_delay = 1.0  # Delay inicial en segundos

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx

                products = response.json()
                expensive_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                return expensive_products

        except httpx.HTTPStatusError as e:
            if attempt == max_retries - 1:
                raise Exception(f"Error en la respuesta HTTP: {e}")
            print(f"Intento {attempt + 1} fallido: {e}")

        except (httpx.NetworkError, httpx.TimeoutException) as e:
            if attempt == max_retries - 1:
                raise Exception(f"Error de red/timeout después de {max_retries} intentos: {e}")
            delay = base_delay * (2 ** attempt)  # Backoff exponencial
            print(f"Intento {attempt + 1} fallido. Reintentando en {delay:.2f} segundos...")
            time.sleep(delay)

    raise Exception("Se agotaron todos los intentos de reconexión")
```

### Explicación:

1. **Autenticación Bearer**: Se incluye el token en el header `Authorization`.
2. **Filtro de productos**: Usa una lista por comprensión para filtrar productos con `price > 100`.
3. **Estructura de salida**: Retorna solo los campos `id`, `name` y `price`.
4. **Manejo de errores**:
   - `HTTPStatusError` para códigos de error HTTP (4xx/5xx).
   - `NetworkError` y `TimeoutException` para problemas de red/timeout.
5. **Retry con backoff exponencial**:
   - Hasta 3 intentos.
   - El delay se duplica en cada intento (1s, 2s, 4s).
6. **Timeout**: Configurado a 10 segundos para la conexión y respuesta.

### Uso:
```python
try:
    productos_caros = get_expensive_products("tu_token_aqui")
    print(productos_caros)
except Exception as e:
    print(f"Error: {e}")
```

### Notas:
- Asegúrate de tener instalado `httpx` (`pip install httpx`).
- La función asume que la API devuelve una lista de productos con los campos `id`, `name` y `price`. Si la estructura es diferente, ajusta el código según corresponda.