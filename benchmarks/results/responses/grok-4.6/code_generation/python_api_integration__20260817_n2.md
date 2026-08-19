# Grok 4.6 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.6`
- success: True  | final: 7.83 | quality: 9.08
- latency_total: 13.016s | tokens_per_second: 94.0
- input_tokens: 301 | output_tokens: 1223
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
    """GET /products, filtra price > 100 y devuelve [{id, name, price}].

    Autenticación Bearer, timeout 10s y hasta 3 intentos con backoff
    exponencial ante errores de red o timeout.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_attempts = 3

    last_exc: Exception | None = None

    for attempt in range(max_attempts):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                payload = response.json()

            if not isinstance(payload, list):
                raise ValueError("La respuesta de /products no es una lista")

            return [
                {"id": item["id"], "name": item["name"], "price": item["price"]}
                for item in payload
                if isinstance(item, dict) and item.get("price", 0) > 100
            ]

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_exc = exc
            if attempt == max_attempts - 1:
                break
            time.sleep(2**attempt)  # 1s, 2s

    raise last_exc  # type: ignore[misc]
```

- Reintenta solo timeout y errores de red (`TimeoutException`, `NetworkError`). Un 4xx/5xx de `raise_for_status()` no se reintenta.
- Backoff: 1 s tras el 1.er fallo, 2 s tras el 2.º; el 3.er fallo se propaga.
- `httpx` cubre timeout y transporte; `time` es stdlib.