# Qwen 3.8 Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.49 | quality: 9.52
- latency_total: 46.302s | tokens_per_second: 130.3
- input_tokens: 164 | output_tokens: 6033
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

```python
import time
from typing import Any, Dict, List

import httpx

# Códigos HTTP que pueden tener sentido reintentar
RETRYABLE_STATUS_CODES = {408, 425, 429, 500, 502, 503, 504}


def get_products_over_100(
    bearer_token: str,
    url: str = "https://api.example.com/products",
    timeout_seconds: float = 10.0,
    max_attempts: int = 3,
    base_backoff_seconds: float = 1.0,
) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde una API protegida con Bearer token,
    filtra los que tienen precio > 100 y devuelve una lista de dicts
    con solo las claves: id, name, price.

    Incluye:
    - Timeout de red: 10 segundos por defecto.
    - Retry con backoff exponencial: máximo 3 intentos por defecto.
    - Manejo de errores de red/timeout.
    """
    if max_attempts < 1:
        raise ValueError("max_attempts debe ser >= 1")

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
    }

    last_error: Exception | None = None

    with httpx.Client(timeout=timeout_seconds) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url, headers=headers)

                # Si el servidor responde con un error reintentable
                # y aún quedan intentos, esperamos antes de reintentar.
                if response.status_code in RETRYABLE_STATUS_CODES:
                    if attempt < max_attempts:
                        delay = base_backoff_seconds * (2 ** (attempt - 1))
                        time.sleep(delay)
                        continue

                # Esto lanzará HTTPStatusError para errores no reintentables
                # o para el último intento con error reintentable.
                response.raise_for_status()

                payload = response.json()

                # Soporta tanto una lista directa como {"products": [...]}
                if isinstance(payload, list):
                    products = payload
                else:
                    products = payload.get("products", [])

                filtered_products: List[Dict[str, Any]] = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    price = product.get("price")

                    # Evitar booleans, ya que bool es subclase de int en Python
                    if isinstance(price, bool):
                        continue

                    try:
                        price_value = float(price)
                    except (TypeError, ValueError):
                        continue

                    if price_value > 100:
                        filtered_products.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": price_value,
                            }
                        )

                return filtered_products

            except (httpx.TimeoutException, httpx.RequestError) as exc:
                # No reintentar errores HTTP generados por raise_for_status().
                # Estos ya fueron tratados arriba si eran reintentables.
                if isinstance(exc, httpx.HTTPStatusError):
                    raise

                last_error = exc

                # Si hay más intentos disponibles, aplicar backoff exponencial.
                if attempt < max_attempts:
                    delay = base_backoff_seconds * (2 ** (attempt - 1))
                    time.sleep(delay)
                    continue

                # Si ya era el último intento, salir y lanzar el último error.
                break

    if last_error is not None:
        raise last_error

    raise RuntimeError("No se pudo obtener una respuesta válida de la API")
```

Ejemplo de uso:

```python
products = get_products_over_100("TOKEN_AQUI")

for p in products:
    print(p)
```