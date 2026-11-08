# DeepSeek V4 Flash 0731 — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.9 | quality: 9.32
- latency_total: 8.245s | tokens_per_second: 233.8
- input_tokens: 190 | output_tokens: 1928
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
    Fetch products from the API, filter those with price > 100,
    and return a list of dicts with keys: id, name, price.

    Uses Bearer token authentication, a 10-second timeout,
    and retries with exponential backoff (max 3 attempts).

    Args:
        token: Bearer token for API authentication.

    Returns:
        List of dicts containing id, name, and price for products
        with price > 100.

    Raises:
        httpx.RequestError: If the request fails after all retries.
        httpx.HTTPStatusError: If the API returns a non-2xx status
            that is not retryable (e.g., 4xx).
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10.0

    for attempt in range(3):
        try:
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()

                data = response.json()
                # Assume the API returns a list directly, or a dict with 'products'.
                products = data if isinstance(data, list) else data.get("products", [])

                # Filter and shape the output.
                return [
                    {
                        "id": p["id"],
                        "name": p["name"],
                        "price": p["price"],
                    }
                    for p in products
                    if p.get("price", 0) > 100
                ]

        except httpx.RequestError as exc:
            # Network errors, timeouts, etc. Retry with backoff.
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)  # 1s, 2s, 4s

        except httpx.HTTPStatusError as exc:
            # Only retry on 5xx (server) errors; re-raise 4xx immediately.
            if exc.response.status_code >= 500:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
            else:
                raise

    # This point is unreachable because the last retry either returns or raises.
    return []
```