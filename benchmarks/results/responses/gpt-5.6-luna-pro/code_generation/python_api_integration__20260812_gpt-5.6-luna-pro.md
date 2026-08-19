# GPT-5.6 Luna Pro — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.41 | quality: 9.36
- latency_total: 20.428s | tokens_per_second: 159.5
- input_tokens: 4585 | output_tokens: 3258
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, cubriendo todos los aspectos de la tarea con un manejo adecuado de errores y reintentos.

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
    """
    Obtiene productos y retorna únicamente aquellos cuyo precio es mayor a 100.

    Reintenta hasta 3 veces ante errores de red, timeout o respuestas HTTP 5xx.
    Cada intento tiene un timeout de 10 segundos.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_intentos = 3

    with httpx.Client(timeout=10.0) as client:
        for intento in range(max_intentos):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                data = response.json()

                # Soporta tanto una respuesta tipo lista como:
                # {"products": [...]}
                productos = data.get("products", []) if isinstance(data, dict) else data

                return [
                    {
                        "id": producto["id"],
                        "name": producto["name"],
                        "price": producto["price"],
                    }
                    for producto in productos
                    if float(producto["price"]) > 100
                ]

            except (httpx.TimeoutException, httpx.RequestError):
                # Errores de timeout o red: se reintenta.
                if intento == max_intentos - 1:
                    raise

            except httpx.HTTPStatusError as exc:
                # Reintentar únicamente ante errores temporales del servidor.
                if exc.response.status_code < 500 or intento == max_intentos - 1:
                    raise

            # Backoff exponencial: 1s, 2s
            time.sleep(2**intento)

    # Este punto no debería alcanzarse.
    return []
```

Los errores `4xx` no se reintentan, mientras que los errores de red, timeout y respuestas `5xx` sí se reintentan hasta un máximo de tres intentos.