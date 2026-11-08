# GPT-5.6 Sol — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.0 | quality: 9.08
- latency_total: 9.575s | tokens_per_second: 107.5
- input_tokens: 102 | output_tokens: 1029
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
import httpx


def obtener_productos_caros(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_intentos = 3

    with httpx.Client(timeout=10.0, headers=headers) as client:
        for intento in range(max_intentos):
            try:
                response = client.get(url)

                # Reintentar errores temporales.
                if response.status_code == 429 or response.status_code >= 500:
                    response.raise_for_status()

                # Otros errores HTTP, como 401 o 404, no se reintentan.
                response.raise_for_status()

                productos = response.json()
                if not isinstance(productos, list):
                    raise ValueError("La respuesta de la API no es una lista")

                return [
                    {
                        "id": producto["id"],
                        "name": producto["name"],
                        "price": producto["price"],
                    }
                    for producto in productos
                    if (
                        isinstance(producto, dict)
                        and isinstance(producto.get("price"), (int, float))
                        and not isinstance(producto["price"], bool)
                        and producto["price"] > 100
                        and all(campo in producto for campo in ("id", "name"))
                    )
                ]

            except httpx.HTTPStatusError as error:
                codigo = error.response.status_code
                es_temporal = codigo == 429 or codigo >= 500

                if not es_temporal:
                    raise RuntimeError(
                        f"Error HTTP no recuperable: {codigo}"
                    ) from error

                ultimo_error = error

            except httpx.RequestError as error:
                # Incluye timeouts, errores DNS y fallos de conexión.
                ultimo_error = error

            except ValueError as error:
                raise RuntimeError("Respuesta JSON inválida de la API") from error

            if intento < max_intentos - 1:
                # Backoff exponencial: 1 y 2 segundos.
                time.sleep(2**intento)

    raise RuntimeError(
        f"No se pudo obtener los productos tras {max_intentos} intentos"
    ) from ultimo_error
```

La función reintenta errores de red, timeouts, respuestas `429` y errores `5xx`. Los errores HTTP no temporales, como `401` o `404`, fallan inmediatamente.