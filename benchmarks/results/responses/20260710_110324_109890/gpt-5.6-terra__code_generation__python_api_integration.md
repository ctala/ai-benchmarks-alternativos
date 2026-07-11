# GPT-5.6 Terra — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 7.7 | quality: 9.08
- latency_total: 11.257s | tokens_per_second: 89.9
- input_tokens: 102 | output_tokens: 1012
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
from typing import Any

import httpx


def obtener_productos_caros(token: str) -> list[dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_intentos = 3
    timeout = httpx.Timeout(10.0)

    with httpx.Client(timeout=timeout, headers=headers) as client:
        for intento in range(1, max_intentos + 1):
            try:
                response = client.get(url)

                # Reintenta únicamente errores del servidor (5xx).
                if response.status_code >= 500:
                    response.raise_for_status()

                # Errores 4xx no se reintentan.
                response.raise_for_status()

                productos = response.json()

                if not isinstance(productos, list):
                    raise ValueError("La respuesta de la API debe ser una lista de productos.")

                return [
                    {
                        "id": producto["id"],
                        "name": producto["name"],
                        "price": producto["price"],
                    }
                    for producto in productos
                    if isinstance(producto, dict)
                    and isinstance(producto.get("price"), (int, float))
                    and not isinstance(producto["price"], bool)
                    and producto["price"] > 100
                ]

            except httpx.HTTPStatusError as exc:
                # No reintentar errores de cliente, como 401, 403, 404, etc.
                if exc.response.status_code < 500 or intento == max_intentos:
                    raise

            except httpx.RequestError:
                # Incluye errores de red, conexión y timeout.
                if intento == max_intentos:
                    raise

            # Backoff exponencial: 1 s tras el primer fallo, 2 s tras el segundo.
            espera = 2 ** (intento - 1)
            time.sleep(espera)

    # No debería alcanzarse debido a los raise anteriores.
    raise RuntimeError("No se pudo obtener la lista de productos.")
```

Ejemplo de uso:

```python
productos = obtener_productos_caros("mi_bearer_token")
print(productos)
```

La función realiza como máximo 3 intentos totales y usa un timeout de 10 segundos por solicitud.