# Qwen 3.8 2.4T (A95B) — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 7.35 | quality: 9.08
- latency_total: 149.888s | tokens_per_second: 98.6
- input_tokens: 155 | output_tokens: 14775
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



Aquí tienes una implementación usando solo `httpx` y la librería estándar (`time`), sin dependencias externas adicionales:

```python
import time
import httpx


def get_products_gt_100(token: str) -> list[dict]:
    """
    Obtiene productos con precio mayor a 100 desde https://api.example.com/products.

    - Hace GET con autenticación Bearer token.
    - Usa timeout de 10 segundos.
    - Reintenta hasta 3 intentos con backoff exponencial para errores de red/timeout.
    - Retorna una lista de dicts con solo: id, name y price.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    timeout = httpx.Timeout(10.0)

    max_attempts = 3
    base_delay = 1.0
    last_error = None

    for attempt in range(max_attempts):
        try:
            response = httpx.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            payload = response.json()

            # Soporta respuesta directa como lista o formato {"products": [...]}
            if isinstance(payload, list):
                products = payload
            elif isinstance(payload, dict) and isinstance(payload.get("products"), list):
                products = payload["products"]
            else:
                raise ValueError("La respuesta JSON no contiene una lista de productos válida.")

            filtered_products = []

            for product in products:
                if not isinstance(product, dict):
                    continue

                try:
                    price = float(product.get("price"))
                except (TypeError, ValueError):
                    # Si el precio no es convertible a número, se omite el producto
                    continue

                if price > 100.0:
                    filtered_products.append(
                        {
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": price,
                        }
                    )

            return filtered_products

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_error = exc

            if attempt < max_attempts - 1:
                # Backoff exponencial: 1s, 2s...
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
            else:
                raise RuntimeError(
                    "La petición falló después de 3 intentos por timeout o error de red."
                ) from exc

    # En principio no debería alcanzarse, pero se deja como salvaguarda.
    raise RuntimeError("La petición falló después de 3 intentos.") from last_error
```

Notas:

- `max_attempts = 3` significa **3 intentos totales**.
- El backoff exponencial usado es:
  - intento 1 falla → espera 1 segundo
  - intento 2 falla → espera 2 segundos
  - intento 3 falla → lanza excepción
- Si quieres también reintentar errores HTTP como `429` o `5xx`, podrías añadir un `except httpx.HTTPStatusError` adicional.