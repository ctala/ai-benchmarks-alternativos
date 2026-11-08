# Qwen 3.8 Max 0902 — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.4 | quality: 9.32
- latency_total: 296.321s | tokens_per_second: 42.7
- input_tokens: 164 | output_tokens: 12647
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

Aquí tienes una función completa usando solo `httpx` y librería estándar:

```python
import time
from typing import Any, Dict, List

import httpx


def obtener_productos_mayores_a_100(
    token: str,
    url: str = "https://api.example.com/products",
) -> List[Dict[str, Any]]:
    """
    Hace GET a la API de productos, filtra precio > 100 y devuelve solo id/name/price.

    - Timeout: 10 segundos.
    - Retry: máximo 3 intentos con backoff exponencial.
    - Errores de red/timeout se reintentan.
    - Errores 4xx no se reintentan.
    - Errores 5xx se reintentan.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_intentos = 3
    delay_base = 1.0
    ultimo_error = None

    for intento in range(max_intentos):
        try:
            with httpx.Client(timeout=10.0, headers=headers) as client:
                response = client.get(url)
                response.raise_for_status()

                payload = response.json()

                # Soporta respuesta directa tipo lista o envuelta en {"products": [...]}
                products = (
                    payload.get("products", payload)
                    if isinstance(payload, dict)
                    else payload
                )

                if not isinstance(products, list):
                    raise ValueError("La respuesta no contiene una lista de productos.")

                result: List[Dict[str, Any]] = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    try:
                        price = float(product.get("price"))
                    except (TypeError, ValueError):
                        continue

                    if price > 100:
                        result.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": price,
                            }
                        )

                return result

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            ultimo_error = exc

        except httpx.HTTPStatusError as exc:
            # Reintentamos solo errores de servidor (5xx)
            if exc.response.status_code >= 500:
                ultimo_error = exc
            else:
                raise RuntimeError(
                    f"Error HTTP {exc.response.status_code} al consultar productos"
                ) from exc

        except ValueError as exc:
            raise RuntimeError("La respuesta JSON no tiene el formato esperado.") from exc

        # Backoff exponencial: 1s, 2s...
        if intento < max_intentos - 1:
            time.sleep(delay_base * (2 ** intento))

    raise RuntimeError(
        f"No se pudieron obtener los productos tras {max_intentos} intentos."
    ) from ultimo_error
```

Uso:

```python
try:
    productos = obtener_productos_mayores_a_100("tu_token_aqui")
    print(productos)
except RuntimeError as err:
    print(f"Error controlado: {err}")
```

Nota: si prefieres devolver una lista vacía en vez de lanzar error cuando fallen los 3 intentos, cambia el último `raise` por `return []`.