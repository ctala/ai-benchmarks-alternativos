# GPT-6 Luna Pro — code_generation/python_api_integration

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.34 | quality: 9.08
- latency_total: 13.276s | tokens_per_second: 138.0
- input_tokens: 3148 | output_tokens: 1832
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


def obtener_productos(token: str) -> list[dict[str, Any]]:
    """Obtiene productos con precio mayor a 100; reintenta errores de red hasta 3 veces."""
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(timeout=10.0) as client:
        for intento in range(3):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                productos = response.json()

                return [
                    {campo: producto[campo] for campo in ("id", "name", "price")}
                    for producto in productos
                    if producto["price"] > 100
                ]

            except httpx.RequestError:
                if intento == 2:
                    raise
                time.sleep(2**intento)  # Espera 1 s y luego 2 s

    return []  # Inalcanzable; se incluye para satisfacer los analizadores de tipos.
```

Se asume que la API devuelve una lista de productos. Los errores HTTP, como `404` o `500`, se propagan mediante `raise_for_status()`; los errores de red y timeout se reintentan.