# GPT-5.6 Terra — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 7.74 | quality: 9.08
- latency_total: 11.087s | tokens_per_second: 93.2
- input_tokens: 102 | output_tokens: 1033
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
    url = "https://api.example.com/products"
    max_intentos = 3
    timeout = 10.0

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    with httpx.Client(timeout=timeout, headers=headers) as client:
        for intento in range(max_intentos):
            try:
                response = client.get(url)

                # Los errores 5xx son temporales y pueden reintentarse.
                if response.status_code >= 500:
                    response.raise_for_status()

                # Errores 4xx, por ejemplo token inválido, no se reintentan.
                response.raise_for_status()

                productos = response.json()

                if not isinstance(productos, list):
                    raise ValueError("La respuesta de la API debe ser una lista de productos")

                resultado = []

                for producto in productos:
                    if not isinstance(producto, dict):
                        continue

                    precio = producto.get("price")

                    if (
                        isinstance(precio, (int, float))
                        and not isinstance(precio, bool)
                        and precio > 100
                    ):
                        resultado.append({
                            "id": producto.get("id"),
                            "name": producto.get("name"),
                            "price": precio,
                        })

                return resultado

            except httpx.HTTPStatusError as exc:
                # Solo reintentar errores del servidor (5xx).
                es_error_reintentable = (
                    exc.response is not None and exc.response.status_code >= 500
                )

                if not es_error_reintentable or intento == max_intentos - 1:
                    raise

            except httpx.RequestError:
                # Incluye errores de red, conexión y timeout.
                if intento == max_intentos - 1:
                    raise

            # Backoff exponencial: 1 s, luego 2 s.
            espera = 2 ** intento
            time.sleep(espera)

    # No debería alcanzarse porque los errores se relanzan.
    return []
```

Ejemplo de uso:

```python
productos = obtener_productos_caros("mi_bearer_token")
print(productos)
```

Los 3 intentos incluyen el primero: si falla, espera 1 segundo antes del segundo intento y 2 segundos antes del tercero.