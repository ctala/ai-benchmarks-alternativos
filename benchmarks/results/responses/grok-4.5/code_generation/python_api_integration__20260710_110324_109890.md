# Grok 4.5 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.5`
- success: True  | final: 8.02 | quality: 9.32
- latency_total: 18.778s | tokens_per_second: 124.8
- input_tokens: 301 | output_tokens: 2343
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
from typing import Any

import httpx


def fetch_expensive_products(token: str) -> list[dict[str, Any]]:
    """
    GET https://api.example.com/products con Bearer token.
    Filtra productos con price > 100 y devuelve [{id, name, price}, ...].
    Timeout 10s. Retry con backoff exponencial (máx. 3 intentos) ante
    errores de red, timeout y 5xx.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    max_attempts = 3
    timeout = 10.0
    last_exc: Exception | None = None

    for attempt in range(max_attempts):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

            products = data if isinstance(data, list) else data.get("products", [])
            if not isinstance(products, list):
                raise ValueError("Respuesta JSON inesperada: se esperaba lista de productos")

            result: list[dict[str, Any]] = []
            for p in products:
                if not isinstance(p, dict):
                    continue
                price = p.get("price")
                try:
                    price_val = float(price) if price is not None else None
                except (TypeError, ValueError):
                    continue
                if price_val is not None and price_val > 100:
                    result.append({
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "price": p.get("price"),  # se conserva el valor original
                    })
            return result

        except httpx.TimeoutException as e:
            last_exc = e
        except httpx.NetworkError as e:
            last_exc = e
        except httpx.HTTPStatusError as e:
            # Reintentar solo en errores de servidor (5xx)
            if e.response is not None and e.response.status_code >= 500:
                last_exc = e
            else:
                raise
        except (ValueError, TypeError, httpx.DecodingError) as e:
            # JSON inválido u otros errores de datos: no reintentar
            raise

        if attempt < max_attempts - 1:
            sleep_s = 2 ** attempt  # 1s, 2s, 4s
            time.sleep(sleep_s)

    assert last_exc is not None
    raise last_exc
```

**Uso:**
```python
productos = fetch_expensive_products("tu_token_aqui")
```

**Notas:**
- Solo `httpx` + stdlib (`time`, `typing`).
- Timeout de 10 s en el cliente.
- Backoff exponencial: espera 1 s → 2 s → 4 s entre intentos (máx. 3 intentos).
- Reintenta en `TimeoutException`, `NetworkError` y HTTP 5xx. Los 4xx y errores de parseo se propagan de inmediato.
- Si el body no es una lista, intenta `data["products"]` (común en APIs). Ajusta según el contrato real.
- `price` se compara como `float` pero se devuelve el valor original del JSON.