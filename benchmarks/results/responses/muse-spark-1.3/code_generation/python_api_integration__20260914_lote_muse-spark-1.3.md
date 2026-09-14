# Muse Spark 1.3 — code_generation/python_api_integration

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.39 | quality: 9.72
- latency_total: 10.242s | tokens_per_second: 210.8
- input_tokens: 99 | output_tokens: 2159
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

Aquí tienes una función completa que cumple los 5 requisitos usando solo `httpx` + librería estándar:

```python
import time
import httpx
from typing import Any

def get_expensive_products(token: str) -> list[dict[str, Any]]:
    """
    Obtiene productos de la API y filtra los de precio > 100.

    Args:
        token: Bearer token para autenticación.

    Returns:
        Lista de dicts con formato: [{"id": ..., "name": ..., "price": ...}]

    Raises:
        RuntimeError: Si falla después de 3 intentos.
        ValueError: Si la respuesta no es JSON válido.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    max_retries = 3
    timeout = 10.0

    last_error: Exception | None = None

    for attempt in range(max_retries):
        try:
            response = httpx.get(url, headers=headers, timeout=timeout)
            # Lanza HTTPStatusError para 4xx / 5xx
            response.raise_for_status()

            data = response.json()

            # Soporta tanto [...] como {"products": [...]} o {"data": [...]}
            if isinstance(data, dict):
                products = data.get("products", data.get("data", []))
            else:
                products = data

            # 2. Filtrar precio > 100 y 3. quedarnos solo con id, name, price
            result = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict) and isinstance(p.get("price"), (int, float)) and p["price"] > 100
            ]
            return result

        except httpx.HTTPStatusError as e:
            last_error = e
            # No reintentar errores de cliente (400, 401, 403, 404), solo 429 y 5xx
            status = e.response.status_code
            if status < 500 and status != 429:
                raise RuntimeError(f"Error HTTP {status}: {e.response.text}") from e

        except (httpx.RequestError, httpx.TimeoutException) as e:
            # 4. Maneja errores de red, DNS, conexión y timeout
            last_error = e

        except ValueError as e:
            # Error decodificando JSON, no tiene sentido reintentar
            raise ValueError(f"Respuesta JSON inválida: {e}") from e

        # 5. Retry con backoff exponencial: 1s, 2s, 4s
        # No dormir en el último intento
        if attempt < max_retries - 1:
            backoff = 2 ** attempt
            time.sleep(backoff)

    raise RuntimeError(f"Fallo al obtener productos después de {max_retries} intentos: {last_error}") from last_error


# Ejemplo de uso:
# products = get_expensive_products("tu_token_aqui")
# print(products)
```

**Cómo funciona:**

1.  **Auth:** Envía `Authorization: Bearer <token>` en el header.
2.  **Timeout:** `httpx.get(..., timeout=10.0)` corta la conexión a los 10 segundos y lanza `httpx.TimeoutException`.
3.  **Retry:** Bucle de 3 intentos. Si falla por red/timeout o por 5xx/429, espera `1s -> 2s -> 4s` con `time.sleep(2 ** attempt)`.
4.  **Filtro:** Solo retorna `id, name, price` donde `price > 100`.