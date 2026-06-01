# DeepSeek V4 Flash (OpenRouter) — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.24 | quality: 9.48
- latency_total: 31.452s | tokens_per_second: 43.8
- input_tokens: 110 | output_tokens: 1378
- judge_score: 4.8 | justificación: 

## Respuesta completa

A continuación se presenta una función Python que cumple con todos los requisitos especificados. Utiliza `httpx` como única dependencia externa y maneja reintentos con backoff exponencial, timeouts y filtrado de productos.

```python
import time
import httpx
from typing import List, Dict

def fetch_expensive_products(token: str) -> List[Dict]:
    """
    Obtiene productos desde la API, filtra aquellos con precio > 100
    y retorna una lista de diccionarios con id, name y price.

    Args:
        token (str): Token de autenticación Bearer.

    Returns:
        List[Dict]: Lista de productos filtrados.

    Raises:
        httpx.RequestError: Si fallan todas las tentativas de conexión.
        httpx.TimeoutException: Si se excede el timeout en todas las tentativas.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)  # 10 segundos de timeout total
    max_retries = 3
    backoff_base = 1  # segundos para el primer reintento

    last_exception = None

    for attempt in range(1, max_retries + 1):
        try:
            # Usamos el contexto de httpx.Client para mejor manejo de conexiones
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción si status no es 2xx
                data = response.json()

            # Filtrar productos con precio > 100
            filtered = [
                {"id": item["id"], "name": item["name"], "price": item["price"]}
                for item in data
                if item.get("price", 0) > 100
            ]
            return filtered

        except (httpx.TimeoutException, httpx.RequestError) as e:
            last_exception = e
            if attempt < max_retries:
                # Backoff exponencial: espera 1, 2, 4 segundos
                wait_time = backoff_base * (2 ** (attempt - 1))
                time.sleep(wait_time)
            else:
                # Último intento fallido, propagamos la excepción
                raise

    # Nunca debería llegar aquí, pero por si acaso
    raise last_exception
```

## Explicación del código:

1. **Autenticación Bearer**: Se pasa el token como argumento y se incluye en el header `Authorization`.
2. **Timeout**: Se configura un timeout de 10 segundos mediante `httpx.Timeout(10.0)`.
3. **Reintentos con backoff exponencial**: 
   - Máximo 3 intentos.
   - En cada fallo (timeout o error de red) se espera `1, 2, 4` segundos respectivamente (base 1, factor 2).
   - Si todos los intentos fallan, se relanza la última excepción.
4. **Filtrado**: Se recorre la respuesta JSON (asumiendo que es una lista de productos) y se conservan aquellos cuyo `price` es mayor a 100. Se devuelve una lista de diccionarios con solo las claves `id`, `name` y `price`.
5. **Manejo de errores**: 
   - `httpx.TimeoutException` y `httpx.RequestError` capturan problemas de red y timeout.
   - `response.raise_for_status()` lanza `httpx.HTTPStatusError` para códigos HTTP de error (4xx, 5xx). Si se desea reintentar también en esos casos, se puede añadir esa excepción al `except`. La especificación solo menciona errores de red y timeout, por lo que se deja así.
6. **Sin dependencias externas adicionales**: Solo se usa `httpx`, que es la única librería externa requerida.

## Uso de ejemplo:

```python
token = "mi_token_de_acceso"
try:
    productos_caros = fetch_expensive_products(token)
    print(productos_caros)
except Exception as e:
    print(f"Error al obtener productos: {e}")
```