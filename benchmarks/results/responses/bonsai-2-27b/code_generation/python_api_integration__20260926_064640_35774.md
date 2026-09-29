# Bonsai 2 27B — code_generation/python_api_integration

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.02 | quality: 9.52
- latency_total: 356.235s | tokens_per_second: 37.1
- input_tokens: 155 | output_tokens: 13219
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



Aquí tienes una función con `httpx`, timeout de 10 segundos, retry con backoff exponencial y filtrado de productos con `price > 100`:

```python
import time
import httpx


def get_products(
    token: str,
    url: str = "https://api.example.com/products"
) -> list[dict]:
    """
    Realiza GET a /products con Bearer token.

    - Timeout: 10 segundos
    - Reintentos: máximo 3 intentos
    - Backoff exponencial: 1s, 2s
    - Filtra productos con price > 100
    - Devuelve una lista de dicts con solo: id, name, price
    """
    timeout = httpx.Timeout(10.0)
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3

    last_error = None
    payload = None

    for attempt in range(max_attempts):
        try:
            with httpx.Client(timeout=timeout, headers=headers) as client:
                response = client.get(url)
                response.raise_for_status()
                payload = response.json()

            break

        except (httpx.TimeoutException, httpx.TransportError) as exc:
            last_error = exc

            if attempt < max_attempts - 1:
                # Backoff exponencial: 1s, 2s
                time.sleep(2 ** attempt)

            continue

        except httpx.HTTPStatusError:
            # Errores HTTP no se reintentan por defecto
            raise

        except httpx.JSONDecodeError as exc:
            raise ValueError("La respuesta del API no es JSON válido") from exc

    if last_error is not None:
        raise last_error

    # Soporta respuestas como:
    # [ {...}, {...} ]
    # o
    # { "products": [ {...}, {...} ] }
    if isinstance(payload, dict):
        products = payload.get("products") or payload.get("data") or []
    else:
        products = payload

    if not isinstance(products, list):
        raise ValueError("Respuesta inválida: se esperaba una lista de productos")

    result = []

    for product in products:
        if not isinstance(product, dict):
            continue

        try:
            price_value = float(product.get("price"))
        except (TypeError, ValueError):
            continue

        if price_value > 100:
            result.append({
                "id": product.get("id"),
                "name": product.get("name"),
                "price": product.get("price"),
            })

    return result


# Alias en español, si lo prefieres
obtener_productos_caros = get_products
```

Ejemplo de uso:

```python
try:
    productos = get_products("mi-token")
    print(productos)
except httpx.HTTPError as error:
    print(f"Error al obtener productos: {error}")
```

Detalles importantes:

- Solo se reintenta si falla por timeout o red.
- Si el API devuelve `4xx` o `5xx`, la excepción HTTP se propaga.
- El backoff es exponencial:
  - Intento 1 falla → espera 1 segundo
  - Intento 2 falla → espera 2 segundos
  - Intento 3 falla → lanza el último error
- La función acepta que la respuesta JSON sea una lista directa o un diccionario con clave `products` o `data`.