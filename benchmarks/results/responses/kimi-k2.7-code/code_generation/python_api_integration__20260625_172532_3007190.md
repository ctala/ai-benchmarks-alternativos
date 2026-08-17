# Kimi K2.7 Code — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.29 | quality: 9.28
- latency_total: 57.728s | tokens_per_second: 20.9
- input_tokens: 115 | output_tokens: 1205
- judge_score: 4.8 | justificación: 

## Respuesta completa

 Aquí tienes una función que usa solo `httpx` y la librería estándar de Python:

```python
import time
import httpx


def fetch_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra los que tienen precio > 100
    y retorna solo id, name y price.
    """
    if not token:
        raise ValueError("Se requiere un token de autenticación")

    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_attempts = 3
    last_exception = None

    for attempt in range(max_attempts):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
                break  # Éxito, salimos del bucle de reintentos

        except (httpx.NetworkError, httpx.TimeoutException) as exc:
            last_exception = exc
            # Si no es el último intento, esperamos con backoff exponencial
            if attempt < max_attempts - 1:
                time.sleep(2 ** attempt)
        except httpx.HTTPStatusError as exc:
            # Errores HTTP (4xx/5xx) no se reintentan según lo solicitado
            raise exc

    else:
        # Se agotaron los reintentos
        raise last_exception or httpx.RequestError("No se pudo obtener los productos")

    # Algunas APIs envuelven la lista en un campo como {"products": [...]}
    products = data if isinstance(data, list) else data.get("products", [])

    return [
        {"id": p["id"], "name": p["name"], "price": p["price"]}
        for p in products
        if p.get("price", 0) > 100
    ]
```

### Uso

```python
try:
    products = fetch_expensive_products(token="tu_token_aqui")
    print(products)
except (httpx.NetworkError, httpx.TimeoutException) as e:
    print(f"Fallo después de 3 intentos: {e}")
```

### Características

- **Autenticación Bearer** mediante el header `Authorization`.
- **Timeout de 10 segundos** configurado con `httpx.Timeout(10.0)`.
- **Reintentos**: hasta 3 intentos.
- **Backoff exponencial**: espera `2^0 = 1s`, luego `2^1 = 2s` entre intentos.
- **Manejo de errores**: captura `httpx.NetworkError` y `httpx.TimeoutException`.
- **Filtrado y proyección**: retorna solo productos con `price > 100` y los campos `id`, `name`, `price`.

> Nota: para ejecutarla necesitas instalar `httpx` (`pip install httpx`). No requiere otras dependencias externas.