# Qwen 3.8 Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 7.15 | quality: 8.16
- latency_total: 248.135s | tokens_per_second: 80.3
- input_tokens: 164 | output_tokens: 19917
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los aspectos de la tarea, incluyendo manejo de errores y backoff exponencial, aunque la profundidad podría mejorarse con más detalles sobre la lógica de filtrado o manejo de diferentes estructuras de datos.

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

Aquí tienes una función **síncrona** con `httpx`, usando solo `httpx` y módulos estándar de Python (`time`, `typing`):

```python
import time
from typing import Any, Dict, List

import httpx


def fetch_expensive_products(
    bearer_token: str,
    *,
    timeout_seconds: float = 10.0,
    max_attempts: int = 3,
) -> List[Dict[str, Any]]:
    """
    Hace GET a https://api.example.com/products usando autenticación Bearer token.

    - Filtra productos con price > 100.
    - Devuelve una lista de dicts con solo: {"id", "name", "price"}.
    - Usa timeout de 10 segundos por defecto.
    - Reintenta errores de red/timeout y errores HTTP transitorios
      con backoff exponencial: 1s, 2s, ...
    """
    if max_attempts < 1:
        raise ValueError("max_attempts debe ser al menos 1")

    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    timeout = httpx.Timeout(timeout_seconds)
    backoff = 1.0
    data: Any = None

    # Cliente HTTP con timeout y headers configurados
    with httpx.Client(timeout=timeout, headers=headers) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
                break

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code

                # Solo reintentar errores HTTP transitorios:
                # 408 Request Timeout, 429 Too Many Requests, 5xx Server Errors
                if status not in (408, 429) and not (500 <= status < 600):
                    raise

                if attempt == max_attempts:
                    raise

            except httpx.TransportError:
                # Incluye errores de red, conexión, timeout, etc.
                if attempt == max_attempts:
                    raise

            # Espera exponencial antes del siguiente intento
            time.sleep(backoff)
            backoff *= 2

    # Soporta APIs que devuelven:
    # 1) una lista directa de productos
    # 2) un dict con clave "products" o "data"
    if isinstance(data, dict):
        products = data.get("products")
        if products is None:
            products = data.get("data")
    elif isinstance(data, list):
        products = data
    else:
        products = []

    if not isinstance(products, list):
        products = []

    result: List[Dict[str, Any]] = []

    for product in products:
        if not isinstance(product, dict):
            continue

        raw_price = product.get("price")

        # Convertimos el precio a número para poder filtrarlo.
        # Si no es numérico, se ignora ese producto.
        try:
            price = float(raw_price)
        except (TypeError, ValueError):
            continue

        # Filtramos solo precio > 100
        if price > 100:
            result.append(
                {
                    "id": product.get("id"),
                    "name": product.get("name"),
                    "price": price,
                }
            )

    return result
```

## Ejemplo de uso

```python
productos = fetch_expensive_products("TU_TOKEN_BEARER")
print(productos)
```

## Notas importantes

- `httpx.Timeout(10.0)` aplica timeout de **10 segundos** a las operaciones HTTP.
- `httpx.TransportError` cubre errores de red y timeout.
- Si fallan los **3 intentos**, la función lanza la excepción original.
- Si quieres que no falle y devuelva una lista vacía en errores finales, puedes capturar la excepción desde el llamador:

```python
try:
    productos = fetch_expensive_products("TU_TOKEN")
except httpx.HTTPError:
    productos = []
```