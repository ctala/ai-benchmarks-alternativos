# GPT-5.5 — code_generation/python_api_integration

- model_id: `gpt-5.5`
- success: True  | final: 6.51 | quality: 8.04
- latency_total: 16.904s | tokens_per_second: 78.6
- input_tokens: 102 | output_tokens: 1328
- judge_score: 4.2 | justificación: 

## Respuesta completa

```python
import time
import httpx


def get_expensive_products(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_attempts = 3
    backoff_seconds = 1.0

    with httpx.Client(timeout=10.0) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                products = response.json()

                return [
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                    }
                    for product in products
                    if product.get("price", 0) > 100
                ]

            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                if attempt == max_attempts:
                    raise RuntimeError(
                        "No se pudo obtener la lista de productos después "
                        "de 3 intentos"
                    ) from exc

                time.sleep(backoff_seconds)
                backoff_seconds *= 2

            except httpx.HTTPStatusError as exc:
                raise RuntimeError(
                    f"Error HTTP al obtener productos: {exc.response.status_code}"
                ) from exc
```