# GPT-5.6 Luna — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.05 | quality: 9.08
- latency_total: 9.284s | tokens_per_second: 139.3
- input_tokens: 102 | output_tokens: 1293
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
from typing import Any

import httpx


def get_expensive_products(token: str) -> list[dict[str, Any]]:
    """
    Obtiene productos y devuelve únicamente aquellos cuyo precio es mayor que 100.

    Se realizan como máximo 3 intentos, con backoff exponencial entre reintentos.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_attempts = 3
    last_error: Exception | None = None

    with httpx.Client(timeout=10.0) as client:
        for attempt in range(max_attempts):
            try:
                response = client.get(url, headers=headers)

                # Los errores 4xx no se reintentan.
                # Los errores 5xx sí se reintentan.
                response.raise_for_status()

                data = response.json()

                # Se admite tanto una lista directa como {"products": [...]}
                products = data["products"] if isinstance(data, dict) else data

                return [
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                    }
                    for product in products
                    if product["price"] > 100
                ]

            except httpx.RequestError as exc:
                # Incluye errores de red y timeouts.
                last_error = exc

            except httpx.HTTPStatusError as exc:
                # Solo reintentar errores del servidor.
                if exc.response.status_code < 500:
                    raise

                last_error = exc

            if attempt < max_attempts - 1:
                # Esperas: 1, 2 segundos
                time.sleep(2**attempt)

    raise RuntimeError(
        f"No se pudo obtener la lista de productos tras "
        f"{max_attempts} intentos"
    ) from last_error
```

El timeout total de cada petición es de 10 segundos y el backoff exponencial espera 1 y 2 segundos antes de los siguientes intentos.