# Qwen 3.8 27B — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.39 | quality: 9.08
- latency_total: 289.768s | tokens_per_second: 46.9
- input_tokens: 155 | output_tokens: 13585
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



Aquí tienes una función usando `httpx`, sin dependencias externas adicionales:

```python
import time
from typing import Any, Dict, List

import httpx


def get_products(token: str, url: str = "https://api.example.com/products") -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API con Bearer token, timeout de 10 segundos
    y hasta 3 intentos con backoff exponencial.
    """
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    base_delay = 1.0  # esperas: 1s, 2s
    timeout = httpx.Timeout(10.0)

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_attempts):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                if not isinstance(data, list):
                    raise ValueError("La respuesta esperada es una lista de productos.")

                result: List[Dict[str, Any]] = []

                for product in data:
                    if not isinstance(product, dict):
                        continue

                    price = product.get("price")
                    try:
                        price_value = float(price)
                    except (TypeError, ValueError):
                        continue

                    if price_value > 100:
                        result.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": price,
                            }
                        )

                return result

            except httpx.RequestError:
                # Cubre timeouts y errores de red.
                if attempt == max_attempts - 1:
                    raise
                time.sleep(base_delay * (2 ** attempt))

            except ValueError:
                # Respuesta JSON inválida o formato inesperado:
                # no tiene sentido reintentar automáticamente.
                raise

    # Nunca debería llegarse aquí.
    raise RuntimeError("No se pudo obtener la lista de productos.")
```

Ejemplo de uso:

```python
productos = get_products("mi-token-aqui")
print(productos)
```

Notas:

- El timeout de 10 segundos aplica a toda la petición.
- Solo se reintenta ante errores de red/timeout.
- Los errores HTTP, como 401 o 404, se lanzan directamente con `raise_for_status()`.