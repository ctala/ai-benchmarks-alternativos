# GPT-6 Luna Pro — code_generation/python_api_integration

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 7.23 | quality: 7.48
- latency_total: 11.967s | tokens_per_second: 144.6
- input_tokens: 3074 | output_tokens: 1731
- judge_score: 3.8 | justificación: 

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
    """Obtiene productos con precio > 100 y devuelve solo id, name y price.

    Reintenta hasta 3 veces ante errores de red o timeout, con backoff
    exponencial. Si los intentos fallan, propaga el último error.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    espera = 0.5

    with httpx.Client(timeout=10.0) as cliente:
        for intento in range(3):
            try:
                respuesta = cliente.get(url, headers=headers)
                respuesta.raise_for_status()
                productos = respuesta.json()
                break
            except httpx.RequestError:
                if intento == 2:
                    raise
                time.sleep(espera)
                espera *= 2

    return [
        {"id": producto["id"], "name": producto["name"], "price": producto["price"]}
        for producto in productos
        if producto["price"] > 100
    ]
```

Los tres intentos son en total; las esperas entre ellos son de 0,5 y 1 segundo. Los errores HTTP (`4xx` o `5xx`) se propagan sin reintento.