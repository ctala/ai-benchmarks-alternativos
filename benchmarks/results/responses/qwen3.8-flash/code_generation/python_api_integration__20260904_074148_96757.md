# Qwen 3.8 Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.18 | quality: 9.32
- latency_total: 129.455s | tokens_per_second: 111.2
- input_tokens: 164 | output_tokens: 14390
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

Aquí tienes una implementación que cumple los 5 puntos usando solo `httpx` y la librería estándar `time`:

```python
import httpx
import time


def get_products_precio_mayor_100(bearer_token: str) -> list[dict]:
    """
    Hace GET a https://api.example.com/products con autenticación Bearer,
    filtra productos con price > 100 y devuelve solo {id, name, price}.

    Incluye:
    - Timeout de 10 segundos.
    - Manejo de errores de red y timeout.
    - Retry con backoff exponencial: 1s, 2s, 4s...
    - Máximo 3 intentos.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}

    timeout = 10.0
    max_attempts = 3
    backoff = 1.0

    if not bearer_token:
        raise ValueError("El bearer_token es obligatorio.")

    def _price_greater_than_100(price) -> bool:
        """
        Valida si el precio es numéricamente mayor a 100.
        Acepta int, float y strings numéricos como "150.50".
        """
        if isinstance(price, bool):
            return False

        if isinstance(price, (int, float)):
            return price > 100

        if isinstance(price, str):
            try:
                return float(price) > 100
            except ValueError:
                return False

        return False

    def _extract_product_list(payload):
        """
        Soporta APIs que devuelven una lista directa:
        [{"id": 1, ...}, ...]

        O un dict con clave común:
        {"products": [...]}
        {"data": [...]}
        {"items": [...]}
        {"results": [...]}
        """
        if isinstance(payload, list):
            return payload

        if isinstance(payload, dict):
            for key in ("products", "data", "items", "results"):
                value = payload.get(key)
                if isinstance(value, list):
                    return value

        return []

    last_error = None

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                products = _extract_product_list(response.json())
                filtered_products = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    price = product.get("price")

                    if _price_greater_than_100(price):
                        # Si viene como string numérica, la normalizamos a float
                        if isinstance(price, str):
                            price = float(price)

                        filtered_products.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": price,
                            }
                        )

                return filtered_products

            except httpx.HTTPStatusError as exc:
                # Reintentar solo en errores de servidor o rate limiting
                retryable_status = exc.response.status_code in (
                    408,  # Request Timeout
                    429,  # Too Many Requests
                    500,  # Internal Server Error
                    502,  # Bad Gateway
                    503,  # Service Unavailable
                    504,  # Gateway Timeout
                )

                if attempt < max_attempts and retryable_status:
                    last_error = exc
                    time.sleep(backoff)
                    backoff *= 2
                    continue

                raise RuntimeError(
                    f"Error HTTP {exc.response.status_code} al consultar productos"
                ) from exc

            except (httpx.TimeoutException, httpx.RequestError) as exc:
                # Errores de red, DNS, conexión, timeout, etc.
                last_error = exc

                if attempt < max_attempts:
                    time.sleep(backoff)
                    backoff *= 2
                    continue

                raise RuntimeError(
                    f"Fallo de red o timeout tras {max_attempts} intentos"
                ) from exc

            except ValueError as exc:
                # Si la respuesta no es JSON válida
                raise RuntimeError(
                    "La respuesta de la API no contiene JSON válido"
                ) from exc

    # Este raise es solo una protección extra; normalmente no se alcanza
    # porque se lanza dentro del último intento si todo falla.
    raise RuntimeError("No se pudo completar la petición") from last_error
```

Uso:

```python
token = "TU_TOKEN_AQUI"

productos = get_products_precio_mayor_100(token)

for producto in productos:
    print(producto)
```

Ejemplo de salida esperada:

```python
[
    {"id": 10, "name": "Producto A", "price": 150.0},
    {"id": 25, "name": "Producto B", "price": 300},
]
```

Notas:

- El timeout es de **10 segundos**.
- Máximo **3 intentos**.
- Backoff exponencial: **1s → 2s → 4s...**
- Si el último intento falla, lanza `RuntimeError`.
- Si prefieres que devuelva una lista vacía en lugar de lanzar excepción, puedes cambiar los `raise RuntimeError(...)` por:

```python
return []
```