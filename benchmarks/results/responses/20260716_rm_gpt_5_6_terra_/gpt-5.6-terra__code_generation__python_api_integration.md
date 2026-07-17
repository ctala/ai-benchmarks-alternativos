# GPT-5.6 Terra — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 6.84 | quality: 7.68
- latency_total: 11.53s | tokens_per_second: 101.4
- input_tokens: 102 | output_tokens: 1169
- judge_score: 3.8 | justificación: 

## Respuesta completa

```python
import time
from typing import Any

import httpx


API_URL = "https://api.example.com/products"


class ProductAPIError(Exception):
    """Error al obtener productos desde la API."""


def obtener_productos_caros(token: str) -> list[dict[str, Any]]:
    """
    Obtiene productos con precio mayor a 100.

    Realiza hasta 3 intentos en total, con backoff exponencial:
    1s antes del segundo intento y 2s antes del tercero.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_intentos = 3
    codigos_reintentables = {429, 500, 502, 503, 504}

    with httpx.Client(timeout=10.0) as client:
        for intento in range(max_intentos):
            try:
                response = client.get(API_URL, headers=headers)

                # Reintentar errores temporales del servidor o rate limiting.
                if response.status_code in codigos_reintentables:
                    response.raise_for_status()

                # Lanza excepción para otros códigos 4xx/5xx.
                response.raise_for_status()

                productos = response.json()

                if not isinstance(productos, list):
                    raise ProductAPIError(
                        "La respuesta de la API debe ser una lista de productos."
                    )

                resultado = []

                for producto in productos:
                    if not isinstance(producto, dict):
                        continue

                    precio = producto.get("price")

                    if (
                        isinstance(precio, (int, float))
                        and not isinstance(precio, bool)
                        and precio > 100
                        and "id" in producto
                        and "name" in producto
                    ):
                        resultado.append(
                            {
                                "id": producto["id"],
                                "name": producto["name"],
                                "price": precio,
                            }
                        )

                return resultado

            except httpx.HTTPStatusError as exc:
                # Solo se reintentan ciertos errores HTTP temporales.
                if (
                    exc.response.status_code not in codigos_reintentables
                    or intento == max_intentos - 1
                ):
                    raise ProductAPIError(
                        f"Error HTTP al obtener productos: {exc.response.status_code}"
                    ) from exc

            except httpx.TransportError as exc:
                # Incluye errores de red y timeouts.
                if intento == max_intentos - 1:
                    raise ProductAPIError(
                        "No fue posible conectar con la API después de varios intentos."
                    ) from exc

            # Backoff exponencial: 1s, 2s...
            espera = 2 ** intento
            time.sleep(espera)

    raise ProductAPIError("No fue posible obtener los productos.")
```

Uso:

```python
productos = obtener_productos_caros("tu_bearer_token")
print(productos)
```

El parámetro `timeout=10.0` aplica un timeout de 10 segundos por solicitud, y `max_intentos = 3` representa un máximo de tres intentos totales.