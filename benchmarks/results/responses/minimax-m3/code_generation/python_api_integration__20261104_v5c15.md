# MiniMax M3 — code_generation/python_api_integration

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.51 | quality: 8.8
- latency_total: 136.416s | tokens_per_second: 89.6
- input_tokens: 290 | output_tokens: 12219
- judge_score: 4.6 | justificación: 

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

Suponiendo que la API devuelve una lista JSON o un objeto con la forma `{"products": [...]}`:

```python
import logging
import time
from typing import Any

import httpx

logger = logging.getLogger(__name__)


def get_products(token: str) -> list[dict[str, Any]]:
    """
    Obtiene los productos con precio mayor que 100.

    Si la petición falla después de 3 intentos, registra el error
    y devuelve una lista vacía.
    """
    if not token:
        raise ValueError("El token Bearer es obligatorio")

    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    timeout = httpx.Timeout(10.0)

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                payload = response.json()

                # Compatible con una lista o con {"products": [...]}
                products = (
                    payload.get("products", [])
                    if isinstance(payload, dict)
                    else payload
                )

                if not isinstance(products, list):
                    raise ValueError("La respuesta no contiene una lista de productos")

                result: list[dict[str, Any]] = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    try:
                        price = product["price"]

                        if isinstance(price, (int, float)) and price > 100:
                            result.append(
                                {
                                    "id": product["id"],
                                    "name": product["name"],
                                    "price": price,
                                }
                            )
                    except (KeyError, TypeError):
                        logger.warning(
                            "Se omite un producto con campos id, name o price inválidos"
                        )

                return result

            except httpx.TimeoutException as exc:
                logger.warning(
                    "Timeout en el intento %d/%d: %s",
                    attempt,
                    max_attempts,
                    exc,
                )

            except httpx.RequestError as exc:
                logger.warning(
                    "Error de red en el intento %d/%d: %s",
                    attempt,
                    max_attempts,
                    exc,
                )

            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code

                # Reintenta errores temporales del servidor.
                if 500 <= status_code < 600 and attempt < max_attempts:
                    logger.warning(
                        "Error HTTP %s en el intento %d/%d",
                        status_code,
                        attempt,
                        max_attempts,
                    )
                else:
                    logger.error("Error HTTP %s; no se reintentará", status_code)
                    return []

            except (ValueError, TypeError) as exc:
                logger.error("No se pudo interpretar la respuesta de la API: %s", exc)
                return []

            # Backoff exponencial: 1 segundo y luego 2 segundos.
            if attempt < max_attempts:
                delay = 2 ** (attempt - 1)
                logger.info("Reintentando en %d segundo(s)", delay)
                time.sleep(delay)

    return []
```

Los tres intentos son en total: el primero más dos reintentos, con esperas de `1` y `2` segundos. Si se prefiere propagar la excepción final al llamador en lugar de devolver `[]`, se pueden reemplazar los retornos de error por `raise`.