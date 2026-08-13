# Nex-N2-Mini — code_generation/python_api_integration

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 8.76 | quality: 9.36
- latency_total: 21.629s | tokens_per_second: 181.4
- input_tokens: 112 | output_tokens: 3923
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, con una buena profundidad en el manejo de errores y reintentos.

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
import httpx
from typing import Any

def obtener_productos(token: str) -> list[dict[str, Any]]:
    """
    Obtiene productos desde https://api.example.com/products,
    filtra price > 100 y retorna solo {id, name, price}.
    """
    if not token:
        raise ValueError("Token Bearer requerido")

    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    max_attempts = 3
    backoff = 1.0

    with httpx.Client(timeout=10.0) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                payload = response.json()
                products = payload.get("products", payload)

                if not isinstance(products, list):
                    raise ValueError("La respuesta de la API no contiene una lista de productos")

                return [
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"]
                    }
                    for product in products
                    if isinstance(product, dict)
                    and isinstance(product.get("price"), (int, float))
                    and product["price"] > 100
                ]

            except httpx.HTTPStatusError as exc:
                # Reintentar solo errores transitorios.
                if exc.response.status_code in {429, 500, 502, 503, 504} and attempt < max_attempts:
                    time.sleep(backoff * (2 ** (attempt - 1)))
                    backoff *= 2
                    continue

                raise

            except httpx.RequestError as exc:
                # Incluye errores de red, conexión y timeout.
                if attempt < max_attempts:
                    time.sleep(backoff * (2 ** (attempt - 1)))
                    backoff *= 2
                    continue

                raise RuntimeError(
                    f"No se pudo obtener la lista de productos tras {max_attempts} intentos: {exc}"
                ) from exc
```

Uso:

```python
productos = obtener_productos("TU_TOKEN_BEARER")
print(productos)
```