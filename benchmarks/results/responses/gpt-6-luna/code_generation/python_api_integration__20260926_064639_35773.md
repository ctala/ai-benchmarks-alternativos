# GPT-6 Luna — code_generation/python_api_integration

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.65 | quality: 7.68
- latency_total: 6.248s | tokens_per_second: 128.5
- input_tokens: 102 | output_tokens: 803
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

import httpx


def obtener_productos(token: str) -> list[dict]:
    """Devuelve los productos cuyo precio supera 100."""
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(timeout=10.0) as client:
        for intento in range(3):
            try:
                respuesta = client.get(url, headers=headers)
                respuesta.raise_for_status()
                productos = respuesta.json()

                return [
                    {"id": producto["id"],
                     "name": producto["name"],
                     "price": producto["price"]}
                    for producto in productos
                    if producto["price"] > 100
                ]

            except httpx.RequestError:
                # Incluye errores de red y de timeout.
                if intento == 2:
                    raise
                time.sleep(2 ** intento)  # Espera 1 s y luego 2 s.
```

Se realizan hasta **3 intentos**. Los errores HTTP (por ejemplo, un `404`) se propagan sin reintento.