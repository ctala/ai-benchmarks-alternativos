# Grok 4.7 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.7`
- success: True  | final: 7.95 | quality: 9.08
- latency_total: 6.558s | tokens_per_second: 91.6
- input_tokens: 1337 | output_tokens: 601
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


def fetch_expensive_products(token: str) -> list[dict[str, Any]]:
    """GET /products, filtra price > 100 y retorna [{id, name, price}].

    Reintenta hasta 3 veces con backoff exponencial ante errores de red o timeout.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_attempts = 3

    last_error: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
            break
        except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as exc:
            last_error = exc
            if attempt == max_attempts:
                raise
            time.sleep(2 ** (attempt - 1))  # 1s, 2s
    else:
        raise last_error  # type: ignore[misc]

    products = data if isinstance(data, list) else data.get("products", [])

    return [
        {"id": p["id"], "name": p["name"], "price": p["price"]}
        for p in products
        if p.get("price") is not None and p["price"] > 100
    ]
```

- Timeout de 10 s en conexión, lectura y escritura.
- Reintentos solo ante timeout, errores de red y respuestas HTTP 4xx/5xx (`raise_for_status`).
- Backoff: 1 s y luego 2 s entre intentos (máximo 3).
- Acepta un JSON que sea una lista o un objeto con clave `products`.