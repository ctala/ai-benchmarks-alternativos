# GPT-OSS 20B — code_generation/python_api_integration

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.81 | quality: 9.48
- latency_total: 11.964s | tokens_per_second: 88.8
- input_tokens: 163 | output_tokens: 1062
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
from typing import Any, Dict, List, Optional

import httpx


def fetch_expensive_products(token: str, *, max_price: float = 100.0) -> List[Dict[str, Any]]:
    """
    Obtiene los productos cuyo precio es mayor que ``max_price`` desde
    https://api.example.com/products usando autenticación Bearer.

    Parámetros
    ----------
    token: str
        Token Bearer que se enviará en el encabezado ``Authorization``.
    max_price: float, optional
        Umbral de precio a partir del cual un producto se considera “caro”.
        Por defecto 100.0.

    Retorna
    -------
    List[Dict[str, Any]]
        Lista de diccionarios con las claves ``id``, ``name`` y ``price``.

    Excepciones
    -----------
    httpx.HTTPError
        Si ocurre un error de red o el servidor devuelve un código distinto a 200
        después de los reintentos permitidos.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0, read=10.0, write=10.0, connect=10.0)

    max_attempts = 3
    backoff_factor = 2  # segundos

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # lanza si 4xx/5xx

            # Suponemos que la respuesta es JSON y contiene una lista bajo la clave "products"
            data = response.json()
            if not isinstance(data, dict) or "products" not in data:
                raise httpx.HTTPError("Respuesta inesperada: no contiene 'products'")

            products = data["products"]
            if not isinstance(products, list):
                raise httpx.HTTPError("'products' no es una lista")

            # Filtrar y mapear
            result: List[Dict[str, Any]] = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p["price"] > max_price
            ]
            return result

        except (httpx.RequestError, httpx.HTTPError, httpx.TimeoutException) as exc:
            # Si es el último intento, propagamos la excepción
            if attempt == max_attempts:
                raise exc from None

            # Backoff exponencial antes del siguiente intento
            sleep_time = backoff_factor ** (attempt - 1)
            time.sleep(sleep_time)
```

### Cómo funciona

1. **Cliente con timeout** – Se crea un `httpx.Client` con un *timeout* de 10 s para todas las operaciones.
2. **Autenticación Bearer** – Se envía el token en el encabezado `Authorization: Bearer …`.
3. **Reintentos con back‑off exponencial** – Se intentan hasta 3 veces. Entre intentos se espera `1 s`, `2 s` y `4 s` respectivamente.
4. **Manejo de errores** – Se capturan `RequestError`, `HTTPError` (por status codes) y `TimeoutException`. Si después de los 3 intentos sigue fallando se vuelve a lanzar la excepción.
5. **Filtrado y mapeo** – Se filtran los productos con precio mayor a 100 (o el valor de `max_price`) y se devuelve una lista de diccionarios con solo `id`, `name` y `price`.

> **Nota:** Este código utiliza únicamente la biblioteca estándar y `httpx`, sin dependencias externas.