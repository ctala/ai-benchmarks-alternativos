# DeepSeek V4.1 Flash — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.19 | quality: 9.08
- latency_total: 28.263s | tokens_per_second: 157.4
- input_tokens: 136 | output_tokens: 4448
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
    timeout = httpx.Timeout(10.0)
    max_intentos = 3
    base_delay = 1.0  # segundos

    with httpx.Client(timeout=timeout, headers=headers) as client:
        for intento in range(1, max_intentos + 1):
            try:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()

                # Permitir respuesta como lista directa o como {"products": [...]}
                if isinstance(data, dict):
                    data = data.get("products", [])

                if not isinstance(data, list):
                    raise ValueError("La respuesta de la API no es una lista de productos")

                resultado = []
                for producto in data:
                    if not isinstance(producto, dict):
                        continue

                    try:
                        precio = float(producto.get("price", 0))
                    except (TypeError, ValueError):
                        continue

                    if precio > 100:
                        resultado.append({
                            "id": producto.get("id"),
                            "name": producto.get("name"),
                            "price": producto.get("price"),
                        })

                return resultado

            except httpx.HTTPStatusError as exc:
                # Reintentar solo errores 5xx; los 4xx se consideran definitivos
                if exc.response.status_code >= 500 and intento < max_intentos:
                    delay = base_delay * (2 ** (intento - 1))
                    time.sleep(delay)
                    continue
                raise RuntimeError(
                    f"Error HTTP {exc.response.status_code} al consultar productos"
                ) from exc

            except httpx.RequestError as exc:
                # Incluye timeout, errores de conexión, DNS, etc.
                if intento == max_intentos:
                    raise RuntimeError(
                        f"Error de red/timeout tras {max_intentos} intentos"
                    ) from exc
                delay = base_delay * (2 ** (intento - 1))
                time.sleep(delay)

            except (ValueError, TypeError, KeyError) as exc:
                raise RuntimeError("Respuesta inesperada de la API") from exc

    return []
```

Esta función:
- Usa autenticación `Bearer` con `httpx`.
- Define timeout de 10 segundos.
- Reintenta hasta 3 intentos en errores de red/timeout y en errores HTTP `5xx`.
- Aplica backoff exponencial: `1s`, `2s`, etc.
- Filtra productos con `price > 100`.
- Devuelve una lista de diccionarios con solo `id`, `name` y `price`.