# GPT-6 Luna — code_generation/python_api_integration

- model_id: `openai/gpt-6-luna`
- success: True  | final: 8.6 | quality: 9.08
- latency_total: 7.903s | tokens_per_second: 121.0
- input_tokens: 102 | output_tokens: 956
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


def obtener_productos_caros(token: str) -> list[dict[str, Any]]:
    """Obtiene productos con precio > 100; reintenta hasta 3 veces."""
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(timeout=10.0) as client:
        for intento in range(3):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                productos = response.json()
                return [
                    {clave: producto[clave] for clave in ("id", "name", "price")}
                    for producto in productos
                    if producto["price"] > 100
                ]

            except httpx.RequestError:
                # Errores de red, incluidos los de timeout.
                if intento == 2:
                    raise
            except httpx.HTTPStatusError as exc:
                # Reintentar errores del servidor; no reintentar errores 4xx.
                if exc.response.status_code < 500 or intento == 2:
                    raise

            # Espera 1 s y luego 2 s antes del siguiente intento.
            time.sleep(2**intento)

    return []  # Inalcanzable: el último error se vuelve a lanzar.
```

Se asume que la respuesta del endpoint es una lista de productos. Los errores de red, timeout y respuestas HTTP 5xx se reintentan hasta completar **3 intentos**.