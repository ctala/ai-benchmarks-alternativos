# GPT-5.6 Sol — code_generation/python_api_integration

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.42 | quality: 9.08
- latency_total: 19.977s | tokens_per_second: 48.3
- input_tokens: 102 | output_tokens: 964
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
import httpx


def obtener_productos(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_intentos = 3

    with httpx.Client(timeout=10.0, headers=headers) as client:
        for intento in range(1, max_intentos + 1):
            try:
                response = client.get(url)
                response.raise_for_status()

                data = response.json()
                productos = data.get("products", []) if isinstance(data, dict) else data

                if not isinstance(productos, list):
                    raise ValueError("La respuesta no contiene una lista de productos")

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
                        and all(campo in producto for campo in ("id", "name", "price"))
                    )
                ]

            except httpx.RequestError as error:
                if intento == max_intentos:
                    raise RuntimeError(
                        f"Error de red después de {max_intentos} intentos"
                    ) from error

                # Backoff exponencial: 1 s, 2 s
                time.sleep(2 ** (intento - 1))

            except httpx.HTTPStatusError as error:
                raise RuntimeError(
                    f"Error HTTP {error.response.status_code}: "
                    f"{error.response.text}"
                ) from error

            except ValueError as error:
                raise RuntimeError("Respuesta inválida de la API") from error
```

Los errores de red y timeout —ambos derivados de `httpx.RequestError`— se reintentan hasta 3 veces, con esperas de 1 y 2 segundos. Los errores HTTP y las respuestas JSON inválidas no se reintentan.