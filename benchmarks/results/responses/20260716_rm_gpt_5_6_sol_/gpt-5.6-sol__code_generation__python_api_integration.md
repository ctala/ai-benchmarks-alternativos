# GPT-5.6 Sol — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 6.88 | quality: 8.24
- latency_total: 30.855s | tokens_per_second: 52.5
- input_tokens: 102 | output_tokens: 1619
- judge_score: 4.2 | justificación: 

## Respuesta completa

```python
import time
from typing import Any

import httpx


def obtener_productos(token: str) -> list[dict[str, Any]]:
    url = "https://api.example.com/products"
    max_intentos = 3
    ultimo_error: Exception | None = None

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    with httpx.Client(headers=headers, timeout=10.0) as client:
        for intento in range(max_intentos):
            try:
                respuesta = client.get(url)

                # Reintentar solo errores HTTP potencialmente temporales.
                if respuesta.status_code == 429 or respuesta.status_code >= 500:
                    respuesta.raise_for_status()

                # Otros errores HTTP, como 401 o 404, no se reintentan.
                respuesta.raise_for_status()

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                if status != 429 and status < 500:
                    raise RuntimeError(
                        f"Error HTTP no reintentable: {status}"
                    ) from exc

                ultimo_error = exc

            except httpx.RequestError as exc:
                # Incluye errores de red, conexión y timeout.
                ultimo_error = exc

            else:
                try:
                    productos = respuesta.json()
                except ValueError as exc:
                    raise RuntimeError("La respuesta no contiene JSON válido") from exc

                if not isinstance(productos, list):
                    raise RuntimeError(
                        "Formato de respuesta inválido: se esperaba una lista"
                    )

                resultado = []
                for producto in productos:
                    if not isinstance(producto, dict):
                        continue

                    precio = producto.get("price")
                    es_numero = (
                        isinstance(precio, (int, float))
                        and not isinstance(precio, bool)
                    )

                    if es_numero and precio > 100:
                        try:
                            resultado.append(
                                {
                                    "id": producto["id"],
                                    "name": producto["name"],
                                    "price": precio,
                                }
                            )
                        except KeyError as exc:
                            raise RuntimeError(
                                f"Producto sin campo requerido: {exc.args[0]}"
                            ) from exc

                return resultado

            # Backoff exponencial: 1 segundo y 2 segundos.
            if intento < max_intentos - 1:
                time.sleep(2**intento)

    raise RuntimeError(
        f"No se pudo obtener los productos después de {max_intentos} intentos"
    ) from ultimo_error
```

Los errores de red y timeout se reintentan hasta un máximo de 3 intentos. También se reintentan respuestas `429` y `5xx`; errores como `401` o `404` fallan inmediatamente.