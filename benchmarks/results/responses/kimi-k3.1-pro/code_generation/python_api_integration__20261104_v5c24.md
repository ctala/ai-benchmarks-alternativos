# Kimi K3.1 Pro — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 6.28 | quality: 7.68
- latency_total: 106.031s | tokens_per_second: 28.7
- input_tokens: 192 | output_tokens: 3038
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


PRODUCTS_URL = "https://api.example.com/products"
MAX_INTENTOS = 3
TIMEOUT_SEGUNDOS = 10


def obtener_productos(token: str) -> list[dict]:
    """Obtiene productos y devuelve únicamente aquellos con precio > 100."""
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(
        headers=headers,
        timeout=httpx.Timeout(TIMEOUT_SEGUNDOS),
    ) as client:
        for intento in range(MAX_INTENTOS):
            try:
                response = client.get(PRODUCTS_URL)
                response.raise_for_status()
                productos = response.json()

                return [
                    {
                        "id": producto["id"],
                        "name": producto["name"],
                        "price": producto["price"],
                    }
                    for producto in productos
                    if producto["price"] > 100
                ]

            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                if intento == MAX_INTENTOS - 1:
                    raise RuntimeError(
                        f"No se pudieron obtener los productos tras "
                        f"{MAX_INTENTOS} intentos"
                    ) from exc

                # Backoff exponencial: 1 segundo, luego 2 segundos.
                time.sleep(2**intento)
```

- Se realizan **3 intentos como máximo en total**, no 3 reintentos adicionales.
- El timeout de **10 segundos se aplica a cada intento**.
- Los errores HTTP (`4xx`/`5xx`) se propagan como `httpx.HTTPStatusError`; solo los errores de red y timeout se reintentan.
- Se asume que la API devuelve una lista JSON de productos con los campos `id`, `name` y `price`.