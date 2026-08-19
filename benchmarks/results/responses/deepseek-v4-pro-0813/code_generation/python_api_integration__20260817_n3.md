# DeepSeek V4 Pro (0813) — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 7.55 | quality: 8.88
- latency_total: 106.522s | tokens_per_second: 75.8
- input_tokens: 189 | output_tokens: 8072
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
from typing import Any

def fetch_expensive_products(
    token: str,
    min_price: float = 100.0,
    max_attempts: int = 3,
) -> list[dict[str, Any]]:
    """
    Obtiene productos de la API y retorna una lista de dicts:
    {id, name, price}, solo con productos cuyo precio sea mayor a min_price.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    backoff = 1.0  # segundos iniciales para backoff exponencial

    with httpx.Client(timeout=10.0, headers=headers) as client:
        for attempt in range(max_attempts):
            try:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
            except httpx.RequestError:
                # Incluye httpx.TimeoutException y errores de red/transporte.
                if attempt == max_attempts - 1:
                    raise
                time.sleep(backoff)
                backoff *= 2
                continue
            except httpx.HTTPStatusError:
                # Error HTTP 4xx/5xx. Se propaga directamente.
                raise
            except ValueError:
                # JSON inválido
                raise

            # Normalizar respuesta: puede ser una lista directa o un dict
            # con clave "products".
            if isinstance(data, list):
                products = data
            elif isinstance(data, dict):
                products = data.get("products", [])
            else:
                products = []

            result: list[dict[str, Any]] = []
            for product in products:
                if not isinstance(product, dict):
                    continue

                raw_price = product.get("price")
                try:
                    price_value = float(raw_price)
                except (TypeError, ValueError):
                    continue

                if price_value > min_price:
                    result.append({
                        "id": product.get("id"),
                        "name": product.get("name"),
                        "price": raw_price,
                    })

            return result

    return []
```