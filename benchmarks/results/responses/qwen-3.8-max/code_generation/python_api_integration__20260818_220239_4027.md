# Qwen 3.8 Max — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.27 | quality: 9.08
- latency_total: 213.058s | tokens_per_second: 49.7
- input_tokens: 151 | output_tokens: 10596
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

Aquí tienes una función completa usando solo `httpx` y la librería estándar:

```python
import time
import httpx


def get_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos desde la API, filtra los que tienen precio > 100
    y devuelve una lista de dicts con id, name y price.

    - Usa autenticación Bearer.
    - Timeout de 10 segundos.
    - Reintenta hasta 3 veces con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    base_delay = 1.0

    with httpx.Client(timeout=10.0, headers=headers) as client:
        for attempt in range(max_attempts):
            try:
                response = client.get(url)
                response.raise_for_status()

                try:
                    payload = response.json()
                except ValueError as exc:
                    raise RuntimeError("La respuesta no contiene JSON válido.") from exc

                # Soporta respuesta directa como lista o como {"products": [...]}
                if isinstance(payload, list):
                    products = payload
                elif isinstance(payload, dict):
                    products = payload.get("products")
                else:
                    products = None

                if not isinstance(products, list):
                    raise RuntimeError("Formato de productos inesperado.")

                filtered = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    if "id" not in product or "name" not in product:
                        continue

                    try:
                        price_value = float(product.get("price"))
                    except (TypeError, ValueError):
                        continue

                    if price_value <= 100:
                        continue

                    filtered.append(
                        {
                            "id": product["id"],
                            "name": product["name"],
                            "price": product["price"],
                        }
                    )

                return filtered

            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                if attempt == max_attempts - 1:
                    raise RuntimeError(
                        "Timeout o error de red después de varios intentos."
                    ) from exc

                # Backoff exponencial: 1s, 2s...
                time.sleep(base_delay * (2 ** attempt))
                continue

            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code

                # Reintentar solo en errores transitorios comunes
                if status_code in {429, 500, 502, 503, 504} and attempt < max_attempts - 1:
                    time.sleep(base_delay * (2 ** attempt))
                    continue

                raise RuntimeError(
                    f"Error HTTP {status_code} al obtener productos."
                ) from exc

    raise RuntimeError("No se pudieron obtener los productos.")
```

Ejemplo de uso:

```python
try:
    products = get_expensive_products("my_token")
    print(products)
except RuntimeError as error:
    print(f"Error: {error}")
```