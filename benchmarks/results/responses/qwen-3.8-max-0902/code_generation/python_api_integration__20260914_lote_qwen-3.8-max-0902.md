# Qwen 3.8 Max 0902 — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.4 | quality: 9.32
- latency_total: 290.549s | tokens_per_second: 44.2
- input_tokens: 164 | output_tokens: 12842
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

Aquí tienes una función síncrona usando solo `httpx` y la librería estándar `time`:

```python
import time
import httpx


def get_expensive_products(bearer_token: str) -> list[dict]:
    """
    Hace GET a /products, filtra productos con precio > 100 y retorna
    una lista de dicts con {id, name, price}.

    - Timeout: 10 segundos.
    - Retry: máximo 3 intentos con backoff exponencial.
    - Si fallan todos los intentos, lanza la última excepción.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}

    timeout_seconds = 10.0
    max_attempts = 3
    base_delay_seconds = 1.0

    last_exc = None

    with httpx.Client(timeout=timeout_seconds, headers=headers) as client:
        for attempt in range(max_attempts):
            try:
                response = client.get(url)
                response.raise_for_status()

                payload = response.json()

                # Soporta respuesta directa como lista o envuelta en un objeto.
                if isinstance(payload, dict):
                    products = payload.get("products", payload.get("results", []))
                else:
                    products = payload

                if not isinstance(products, list):
                    raise ValueError("La respuesta no contiene una lista de productos.")

                filtered_products = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    raw_price = product.get("price")

                    try:
                        price = float(raw_price)
                    except (TypeError, ValueError):
                        continue

                    if price > 100:
                        filtered_products.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": raw_price,
                            }
                        )

                return filtered_products

            except httpx.TransportError as exc:
                # httpx.TransportError cubre errores de red y timeouts.
                last_exc = exc

                if attempt < max_attempts - 1:
                    # Backoff exponencial: 1s, 2s...
                    time.sleep(base_delay_seconds * (2 ** attempt))

    if last_exc is not None:
        raise last_exc

    raise RuntimeError("No se pudo completar la solicitud.")
```

Notas:

- `httpx.TransportError` cubre errores de red y timeout en `httpx`.
- El timeout está fijado en `10.0` segundos.
- La función intenta como máximo `3` veces.
- El backoff es exponencial: espera `1` segundo tras el primer fallo y `2` segundos tras el segundo.
- Si después de los reintentos sigue fallando, lanza la última excepción capturada.