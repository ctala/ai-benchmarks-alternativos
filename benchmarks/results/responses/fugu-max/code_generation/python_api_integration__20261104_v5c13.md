# Fugu Max — code_generation/python_api_integration

- model_id: `sakana/fugu-max`
- success: True  | final: 7.96 | quality: 9.32
- latency_total: 14.035s | tokens_per_second: 241.3
- input_tokens: 228 | output_tokens: 3386
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
from __future__ import annotations

import time
from typing import Any

import httpx

PRODUCTS_URL = "https://api.example.com/products"
MAX_ATTEMPTS = 3
TIMEOUT_SECONDS = 10.0


def get_expensive_products(token: str) -> list[dict[str, Any]]:
    """
    Obtiene productos desde la API, filtra los que tienen price > 100
    y devuelve solo {id, name, price}.

    Reintenta hasta 3 intentos con backoff exponencial para errores
    de red/timeout y respuestas 429/5xx.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    with httpx.Client(timeout=TIMEOUT_SECONDS, headers=headers) as client:
        for attempt in range(MAX_ATTEMPTS):
            try:
                response = client.get(PRODUCTS_URL)
                response.raise_for_status()
                products = response.json()

                if not isinstance(products, list):
                    raise ValueError("La API no devolvió una lista de productos")

                result: list[dict[str, Any]] = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    if not {"id", "name", "price"}.issubset(product):
                        continue

                    price = product["price"]

                    # Evita bool y valores no numéricos
                    if isinstance(price, bool) or not isinstance(price, (int, float)):
                        continue

                    if price > 100:
                        result.append({
                            "id": product["id"],
                            "name": product["name"],
                            "price": price,
                        })

                return result

            except (httpx.TimeoutException, httpx.NetworkError):
                # Backoff exponencial: 1s, 2s
                if attempt == MAX_ATTEMPTS - 1:
                    raise
                time.sleep(2 ** attempt)

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                retryable = status == 429 or 500 <= status < 600

                if not retryable or attempt == MAX_ATTEMPTS - 1:
                    raise

                time.sleep(2 ** attempt)

    raise RuntimeError("No se pudo completar la solicitud")
```

Notas:
- `MAX_ATTEMPTS = 3` significa 3 intentos totales.
- El backoff es `1s`, `2s` entre intentos.
- Los errores de red/timeout se vuelven a lanzar cuando se agotan los intentos.
- Solo se usa `httpx` y la librería estándar (`time`, `typing`).