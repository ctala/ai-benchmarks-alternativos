# GPT-6.1 Terra — code_generation/python_api_integration

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 7.68 | quality: 8.52
- latency_total: 8.034s | tokens_per_second: 80.3
- input_tokens: 102 | output_tokens: 645
- judge_score: 4.4 | justificación: 

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
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(timeout=10.0) as client:
        for intento in range(3):
            try:
                respuesta = client.get(url, headers=headers)
                respuesta.raise_for_status()

                productos = respuesta.json()
                return [
                    {"id": producto["id"], "name": producto["name"], "price": producto["price"]}
                    for producto in productos
                    if producto["price"] > 100
                ]

            except (httpx.RequestError, httpx.HTTPStatusError) as error:
                if isinstance(error, httpx.HTTPStatusError):
                    estado = error.response.status_code
                    reintentable = estado in (408, 429) or 500 <= estado < 600
                    if not reintentable:
                        raise

                if intento == 2:
                    raise

                time.sleep(2 ** intento)  # Espera 1 y 2 segundos.
```

Se asume que la respuesta JSON es una lista de productos con `id`, `name` y `price` numérico. Tras tres intentos fallidos, la función propaga la excepción. En httpx, el timeout de 10 segundos se aplica a las operaciones de red, no al tiempo total de todos los intentos.