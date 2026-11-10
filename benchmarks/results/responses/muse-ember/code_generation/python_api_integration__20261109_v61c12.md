# Muse Ember — code_generation/python_api_integration

- model_id: `meta/muse-ember`
- success: True  | final: 8.87 | quality: 9.52
- latency_total: 4.431s | tokens_per_second: 578.7
- input_tokens: 100 | output_tokens: 2564
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
from typing import Any

import httpx


def get_products(token: str) -> list[dict[str, Any]]:
    """
    Hace GET a /products con Bearer token, filtra precio > 100
    y retorna solo {id, name, price}.

    - Timeout: 10 segundos
    - Retry: max 3 intentos con backoff exponencial (0.5s, 1s)
    - Reintenta solo en errores de red/timeout y HTTP 429/5xx
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_intentos = 3
    ultimo_error: Exception | None = None

    for intento in range(max_intentos):
        try:
            with httpx.Client(timeout=10.0) as client:
                respuesta = client.get(url, headers=headers)
                respuesta.raise_for_status()
                datos = respuesta.json()

            if not isinstance(datos, list):
                raise ValueError("Respuesta inesperada: se esperaba una lista")

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in datos
                if isinstance(p, dict)
                and "id" in p
                and "name" in p
                and isinstance(p.get("price"), (int, float))
                and p["price"] > 100
            ]

        except httpx.HTTPStatusError as e:
            ultimo_error = e
            # No reintentar errores 4xx (excepto 429)
            if e.response.status_code not in (429, 500, 502, 503, 504):
                raise

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            ultimo_error = e

        # Backoff exponencial antes del siguiente intento
        if intento < max_intentos - 1:
            time.sleep(0.5 * (2**intento))  # 0.5s, 1s

    raise RuntimeError(f"Falló tras {max_intentos} intentos") from ultimo_error
```

**Uso:**
```python
productos = get_products("tu_token")
print(productos)
# [{"id": 1, "name": "Laptop", "price": 999.99}, ...]
```

Solo requiere `httpx` (`pip install httpx`), el resto es stdlib.