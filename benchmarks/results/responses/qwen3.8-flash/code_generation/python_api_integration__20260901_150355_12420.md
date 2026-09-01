# Qwen 3.8 Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.17 | quality: 9.28
- latency_total: 111.068s | tokens_per_second: 117.9
- input_tokens: 164 | output_tokens: 13091
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

Aquí tienes una función Python que cumple todo lo que pediste usando **solo `httpx`** y la librería estándar `time` para el backoff:

```python
import time
import httpx


def obtener_productos_caros(
    token: str,
    url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout: float = 10.0,
) -> list:
    """
    Hace GET a /products con autenticación Bearer token,
    reintenta ante errores de red o timeout,
    y retorna productos con price > 100 como lista de dicts {id, name, price}.
    """
    if max_retries < 1:
        raise ValueError("max_retries debe ser al menos 1")

    headers = {"Authorization": f"Bearer {token}"}
    last_error = None
    base_delay = 1.0

    # Timeout total configurado en el cliente.
    # httpx.Timeout aplica el timeout a conexión, lectura, escritura y pool.
    with httpx.Client(timeout=httpx.Timeout(timeout)) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                data = response.json()

                # Soporta una respuesta tipo lista:
                # [ {...}, {...} ]
                # o un objeto tipo:
                # { "products": [...] }
                # o { "data": [...] }
                if isinstance(data, dict):
                    products = data.get("products", data.get("data", []))
                else:
                    products = data

                if not isinstance(products, list):
                    raise ValueError("Formato de respuesta inesperado")

                filtered = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    raw_price = product.get("price")

                    # Convertimos a float para filtrar correctamente.
                    # Si no es numérico, se ignora el producto.
                    try:
                        numeric_price = float(raw_price)
                    except (TypeError, ValueError):
                        continue

                    if numeric_price > 100:
                        # Preservamos el price original si ya era int o float.
                        # Si venía como string numérico, retornamos float.
                        price = (
                            raw_price
                            if isinstance(raw_price, (int, float))
                            else numeric_price
                        )

                        filtered.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": price,
                            }
                        )

                return filtered

            except httpx.RequestError as exc:
                # httpx.RequestError incluye errores de red y también
                # httpx.TimeoutException.
                last_error = exc

                # Backoff exponencial: 1s, 2s, 4s...
                # Con max_retries = 3, se espera:
                # intento 0 -> sleep 1s
                # intento 1 -> sleep 2s
                # intento 2 -> no se duerme, se lanza el error
                if attempt < max_retries - 1:
                    time.sleep(base_delay * (2 ** attempt))

    if last_error is not None:
        raise last_error

    raise RuntimeError("No se pudo completar la solicitud")
```

Ejemplo de uso:

```python
productos = obtener_productos_caros("TU_BEARER_TOKEN")
print(productos)
```

Comportamiento:

1. Hace `GET` a `https://api.example.com/products`.
2. Envía el header:
   ```http
   Authorization: Bearer TU_BEARER_TOKEN
   ```
3. Usa timeout de `10` segundos.
4. Reintenta hasta `3` intentos en errores de red o timeout.
5. Aplica backoff exponencial con esperas `1s` y `2s`.
6. Filtra productos con `price > 100`.
7. Retorna solo:
   ```python
   {"id": ..., "name": ..., "price": ...}
   ```

Nota: los errores HTTP como `401`, `403` o `404` no se reintentan; se propagan inmediatamente porque no son errores de red/timeout.