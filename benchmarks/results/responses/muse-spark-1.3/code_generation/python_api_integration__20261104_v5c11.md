# Muse Spark 1.3 — code_generation/python_api_integration

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.28 | quality: 9.52
- latency_total: 13.182s | tokens_per_second: 146.4
- input_tokens: 100 | output_tokens: 1930
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
import time
import httpx

def get_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra los de precio > 100
    y retorna solo {id, name, price}.

    - Auth: Bearer token
    - Timeout: 10 segundos
    - Retry: max 3 intentos con backoff exponencial
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = httpx.get(url, headers=headers, timeout=10.0)
            response.raise_for_status()  # lanza HTTPStatusError si 4xx/5xx

            products = response.json()
            # Si la API devuelve {"products": [...]}, soportarlo
            if isinstance(products, dict) and "products" in products:
                products = products["products"]

            # 2 y 3. Filtrar y proyectar
            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p["price"] > 100
            ]

        except httpx.HTTPStatusError as e:
            status = e.response.status_code
            # No reintentar errores 4xx (excepto 429)
            if 400 <= status < 500 and status != 429:
                raise RuntimeError(f"Error HTTP {status}: {e.response.text}") from e
            
            # Reintentar 5xx y 429
            if attempt == max_retries - 1:
                raise RuntimeError(f"Fallo tras {max_retries} intentos: {e}") from e

        except (httpx.RequestError, httpx.TimeoutException) as e:
            # 4. Errores de red, conexión, DNS, timeout
            if attempt == max_retries - 1:
                raise RuntimeError(f"Error de red tras {max_retries} intentos: {e}") from e

        except (ValueError, KeyError) as e:
            # Error de JSON inválido o formato inesperado, no reintentar
            raise RuntimeError(f"Respuesta inválida de la API: {e}") from e

        # 5. Backoff exponencial: 1s, 2s, 4s
        time.sleep(2 ** attempt)

    return []  # inalcanzable, por seguridad
```

**Uso:**

```python
# pip install httpx
try:
    caros = get_expensive_products(token="tu_token_aqui")
    print(caros)
    # [{'id': 1, 'name': 'Laptop', 'price': 1200}, ...]
except RuntimeError as e:
    print(f"No se pudo obtener productos: {e}")
```