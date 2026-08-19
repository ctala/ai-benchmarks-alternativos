# KAT Coder Air v2.5 — code_generation/python_api_integration

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.06 | quality: 9.52
- latency_total: 4.32s | tokens_per_second: 177.8
- input_tokens: 113 | output_tokens: 768
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
import httpx
import time


def fetch_expensive_products(token: str) -> list[dict]:
    """
    Fetches products from the API, filters those with price > 100,
    and returns a list of {id, name, price} dicts.

    - Uses Bearer token authentication.
    - 10-second timeout.
    - Exponential backoff retry, max 3 attempts.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    base_delay = 1.0  # seconds

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                products = response.json()

            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p["price"] > 100
            ]
            return filtered

        except httpx.TimeoutException:
            if attempt == max_attempts:
                raise
            delay = base_delay * (2 ** (attempt - 1))
            time.sleep(delay)

        except httpx.HTTPStatusError as e:
            if 500 <= e.response.status_code < 600 and attempt < max_attempts:
                delay = base_delay * (2 ** (attempt - 1))
                time.sleep(delay)
            else:
                raise

        except (httpx.RequestError, ValueError, KeyError) as e:
            if attempt == max_attempts:
                raise RuntimeError(f"Failed after {max_attempts} attempts: {e}") from e
            delay = base_delay * (2 ** (attempt - 1))
            time.sleep(delay)
```

### Cómo funciona

| Aspecto | Detalle |
|---|---|
| **Autenticación** | Header `Authorization: Bearer <token>` |
| **Timeout** | 10 s por intento (configurado en el `Client`) |
| **Retry** | 3 intentos con backoff exponencial: 1s → 2s → 4s |
| **Solo retries en errores transitorios** | `TimeoutException` y errores `5xx` se retryean; `4xx` y otros errores se propagan de inmediato |
| **Filtro** | Solo productos con `price > 100`, devolviendo `{id, name, price}` |
| **Manejo de errores de red** | `RequestError` (DNS, conexión, etc.) y `ValueError`/`KeyError` (JSON mal formado o campos faltantes) se capturan y retryean |

### Ejemplo de uso

```python
try:
    result = fetch_expensive_products("mi_token_secreto")
    print(result)
except httpx.HTTPStatusError as e:
    print(f"Error HTTP: {e.response.status_code}")
except RuntimeError as e:
    print(e)
except httpx.RequestError as e:
    print(f"Error de red: {e}")
```