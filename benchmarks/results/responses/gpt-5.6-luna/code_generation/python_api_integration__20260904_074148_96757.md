# GPT-5.6 Luna — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.83 | quality: 9.08
- latency_total: 4.882s | tokens_per_second: 104.7
- input_tokens: 102 | output_tokens: 511
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
    """
    Obtiene productos cuyo precio es mayor que 100.

    Reintenta hasta 3 veces ante errores de red, timeout o respuestas 5xx.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    max_intentos = 3

    with httpx.Client(timeout=10.0) as client:
        for intento in range(max_intentos):
            try:
                response = client.get(url, headers=headers)

                # Reintentar únicamente ante errores del servidor.
                if 500 <= response.status_code < 600:
                    response.raise_for_status()

                # Los errores 4xx no se reintentan.
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

            except (httpx.TimeoutException, httpx.NetworkError):
                if intento == max_intentos - 1:
                    raise

                # Backoff exponencial: 1, 2 segundos.
                time.sleep(2**intento)

            except httpx.HTTPStatusError:
                # Reintentar errores 5xx; propagar errores 4xx.
                if intento == max_intentos - 1:
                    raise

                if response.status_code < 500:
                    raise

                time.sleep(2**intento)

    return []
```

Ejemplo de uso:

```python
productos = obtener_productos_caros("mi-token-bearer")
print(productos)
```