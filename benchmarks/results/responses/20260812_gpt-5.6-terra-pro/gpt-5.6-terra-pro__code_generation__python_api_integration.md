# GPT-5.6 Terra Pro — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 7.72 | quality: 9.08
- latency_total: 27.484s | tokens_per_second: 143.9
- input_tokens: 5499 | output_tokens: 3955
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


URL_PRODUCTS = "https://api.example.com/products"


def obtener_productos_caros(token: str) -> list[dict[str, Any]]:
    """
    Obtiene productos cuyo precio sea mayor a 100.

    Realiza hasta 3 intentos en caso de errores de red, timeout,
    respuestas 429 o errores HTTP 5xx.
    """
    max_intentos = 3
    timeout = httpx.Timeout(10.0)

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    ultimo_error: Exception | None = None

    with httpx.Client(timeout=timeout, headers=headers) as client:
        for intento in range(1, max_intentos + 1):
            try:
                response = client.get(URL_PRODUCTS)

                # Reintentar ante rate limiting o errores temporales del servidor.
                if response.status_code == 429 or response.status_code >= 500:
                    response.raise_for_status()

                # Los errores 4xx distintos de 429 no se reintentan.
                response.raise_for_status()

                data = response.json()

                # Soporta tanto una lista directa como {"products": [...]}
                productos = data.get("products", []) if isinstance(data, dict) else data

                if not isinstance(productos, list):
                    raise ValueError("La respuesta de la API no contiene una lista de productos.")

                resultado = []

                for producto in productos:
                    if not isinstance(producto, dict):
                        continue

                    precio = producto.get("price")

                    # Se excluyen valores no numéricos y booleanos.
                    if (
                        isinstance(precio, (int, float))
                        and not isinstance(precio, bool)
                        and precio > 100
                    ):
                        resultado.append(
                            {
                                "id": producto.get("id"),
                                "name": producto.get("name"),
                                "price": precio,
                            }
                        )

                return resultado

            except httpx.RequestError as error:
                # Incluye errores de red y httpx.TimeoutException.
                ultimo_error = error

            except httpx.HTTPStatusError as error:
                # Solo se reintentan 429 y 5xx.
                status = error.response.status_code
                if status != 429 and status < 500:
                    raise
                ultimo_error = error

            # Backoff exponencial: 1 s, 2 s.
            # No se espera después del último intento.
            if intento < max_intentos:
                espera = 2 ** (intento - 1)
                time.sleep(espera)

    # Se alcanza únicamente si todos los intentos fallaron.
    assert ultimo_error is not None
    raise ultimo_error
```

Ejemplo de uso:

```python
try:
    productos = obtener_productos_caros("tu_bearer_token")
    print(productos)
except httpx.RequestError as exc:
    print(f"Error de red o timeout: {exc}")
except httpx.HTTPStatusError as exc:
    print(f"Error HTTP: {exc.response.status_code}")
```