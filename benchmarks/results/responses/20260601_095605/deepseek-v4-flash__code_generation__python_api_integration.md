# DeepSeek V4 Flash (OpenRouter) — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.2 | quality: 9.48
- latency_total: 35.289s | tokens_per_second: 46.0
- input_tokens: 110 | output_tokens: 1625
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la función solicitada, que cumple con todos los requisitos:

```python
import time
from typing import List, Dict, Any

import httpx

def fetch_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde https://api.example.com/products con autenticación Bearer,
    filtra aquellos con precio > 100 y retorna una lista de diccionarios con id, name y price.

    Incluye manejo de errores de red y timeout, con reintentos exponenciales (máx. 3).

    Args:
        token: Token Bearer para autenticación.

    Returns:
        Lista de diccionarios con las claves 'id', 'name', 'price' para productos cuyo
        precio sea mayor a 100. Si ocurre un error no recuperable, retorna lista vacía.

    Raises:
        httpx.RequestError: Si tras los reintentos el error de red/timeout persiste.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)

    # Parámetros de backoff exponencial (base 1 segundo, máximo 3 intentos)
    max_retries = 3
    base_delay = 1.0

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción si status != 2xx
                data = response.json()

                # Suponemos que la respuesta es una lista de productos
                if not isinstance(data, list):
                    raise ValueError("Formato inesperado: se esperaba una lista.")

                # Filtrar productos con price > 100 y construir la salida
                filtered = [
                    {"id": item["id"], "name": item["name"], "price": item["price"]}
                    for item in data
                    if item.get("price", 0) > 100
                ]
                return filtered

        except (httpx.RequestError, httpx.TimeoutException) as e:
            # Error de red o timeout
            if attempt < max_retries:
                delay = base_delay * (2 ** (attempt - 1))  # 1, 2, 4 segundos
                time.sleep(delay)
            else:
                # Último intento falló, relanzamos la excepción
                raise
        except (ValueError, KeyError, TypeError) as e:
            # Error en el formato de la respuesta (no se reintenta)
            print(f"Error al procesar la respuesta: {e}")
            return []
        except httpx.HTTPStatusError as e:
            # Error HTTP (status no exitoso) – no se reintenta por defecto
            print(f"Error HTTP {e.response.status_code}: {e.response.text}")
            return []

    # Nunca debería llegar aquí, pero por si acaso
    return []
```

### Explicación

1. **GET con autenticación Bearer**: Se envía el token en el header `Authorization: Bearer <token>`.
2. **Filtrado**: Se asume que la API devuelve una lista de objetos JSON. Se filtran aquellos cuyo campo `price` sea mayor a 100 y se extraen solo `id`, `name`, `price`.
3. **Manejo de errores**:
   - **Red y timeout**: Se capturan `httpx.RequestError` y `httpx.TimeoutException`. Se realizan hasta 3 reintentos con backoff exponencial (1s, 2s, 4s). Si falla el último intento, se relanza la excepción.
   - **Formato inválido**: Si la respuesta no es una lista o faltan campos, se retorna lista vacía (sin reintento).
   - **HTTP errors**: Si el servidor responde con un código de error (4xx, 5xx), se captura `httpx.HTTPStatusError` y se retorna lista vacía (sin reintento, ya que no suele ser transitorio).
4. **Timeout**: Se configura un timeout de 10 segundos para toda la operación.
5. **Sin dependencias externas adicionales**: Solo se usa `httpx` y módulos estándar (`time`, `typing`).

### Uso

```python
productos = fetch_expensive_products("mi_token_secreto")
print(productos)
```

Si ocurre un error de red persistente, la función lanzará una excepción `httpx.RequestError`. En cualquier otro caso, retorna una lista (posiblemente vacía).