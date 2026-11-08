# Mercury 3 — code_generation/python_api_integration

- model_id: `inception/mercury-3`
- success: True  | final: 8.99 | quality: 9.52
- latency_total: 3.599s | tokens_per_second: 526.3
- input_tokens: 105 | output_tokens: 1894
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

Aquí tienes una función en Python que cumple todos los requisitos usando `httpx`:

```python
import time
import httpx
from typing import Any, Dict, List

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde la API, filtra los de precio > 100
    y devuelve solo id, name y price.

    Args:
        token: Token Bearer para autenticación.

    Returns:
        Lista de diccionarios con {id, name, price}.

    Raises:
        httpx.RequestError: Si falla la red o el timeout tras 3 intentos.
        httpx.HTTPStatusError: Si la API devuelve un error HTTP tras 3 intentos.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10.0

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza HTTPStatusError si status >= 400

                data = response.json()

                # Asumimos que la respuesta es una lista de productos.
                # Si viene dentro de una clave "products", la extraemos.
                products = data if isinstance(data, list) else data.get("products", [])

                # Filtramos precio > 100 y seleccionamos solo los campos pedidos.
                expensive = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                return expensive

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # Si es el último intento, propagamos la excepción.
            if attempt == max_retries - 1:
                raise exc

            # Backoff exponencial: 0.5s, 1s, 2s
            sleep_time = 0.5 * (2 ** attempt)
            time.sleep(sleep_time)

    # Nunca se llega aquí, pero por completitud.
    raise RuntimeError("No se pudo completar la solicitud")
```

### Explicación

- **Autenticación Bearer**: Se agrega el header `Authorization: Bearer <token>`.
- **Timeout de 10s**: `httpx.Client(timeout=10.0)`.
- **Filtrado**: Se recorre la lista de productos y se conservan los que tengan `price > 100`.
- **Solo `id`, `name`, `price`**: Se construye un nuevo diccionario con esas claves.
- **Manejo de errores**: Se capturan `httpx.RequestError` (incluye problemas de red y timeout) y `httpx.HTTPStatusError` (respuestas HTTP 4xx/5xx).
- **Retry con backoff exponencial**: Máximo 3 intentos. Entre intentos se espera `0.5 * 2^attempt` segundos (0.5, 1, 2).

### Ejemplo de uso

```python
try:
    productos_caros = get_expensive_products("mi_token_secreto")
    print(productos_caros)
except Exception as e:
    print(f"Error: {e}")
```