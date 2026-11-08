# Muse Glimmer 30B — code_generation/python_api_integration

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.44 | quality: 9.32
- latency_total: 9.954s | tokens_per_second: 164.6
- input_tokens: 148 | output_tokens: 1638
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

Aquí tienes una implementación con `httpx` que cumple todos los requisitos: autenticación Bearer, timeout de 10s, retry con backoff exponencial y filtrado.

```python
import time
import httpx
from typing import List, Dict

def get_expensive_products(bearer_token: str, url: str = "https://api.example.com/products", timeout: float = 10.0, max_retries: int = 3) -> List[Dict]:
    """
    Obtiene productos desde la API y devuelve solo los con precio > 100.

    Args:
        bearer_token: Token para Authorization: Bearer
        url: Endpoint de la API
        timeout: Timeout en segundos para cada petición
        max_retries: Número máximo de intentos

    Returns:
        Lista de dicts con {id, name, price}
    """
    headers = {"Authorization": f"Bearer {bearer_token}"}
    
    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                resp = client.get(url, headers=headers)
                resp.raise_for_status()
                data = resp.json()

            # Se asume que la API devuelve una lista
            if not isinstance(data, list):
                raise ValueError("Respuesta inesperada de la API")

            result = []
            for p in data:
                try:
                    price = float(p.get("price", 0))
                    if price > 100:
                        result.append({
                            "id": p.get("id"),
                            "name": p.get("name"),
                            "price": price
                        })
                except (TypeError, ValueError):
                    continue
            return result

        except httpx.TimeoutException as e:
            # Timeout específico
            if attempt == max_retries:
                raise RuntimeError(f"Timeout después de {max_retries} intentos") from e
        except httpx.HTTPStatusError as e:
            # Reintenta solo en errores 5xx o 429
            status = e.response.status_code
            if status >= 500 or status == 429:
                if attempt == max_retries:
                    raise RuntimeError(f"Error HTTP {status} tras {max_retries} intentos") from e
            else:
                raise
        except httpx.RequestError as e:
            # Errores de red: ConnectError, ReadError, etc.
            if attempt == max_retries:
                raise RuntimeError(f"Error de red tras {max_retries} intentos") from e
        except Exception as e:
            # Error inesperado, no reintentar
            raise

        # Backoff exponencial: 1s, 2s, 4s...
        sleep_time = 2 ** (attempt - 1)
        time.sleep(sleep_time)

    return []  # Nunca debería llegar aquí
```

**Uso**

```python
token = "tu_token_aqui"
try:
    productos = get_expensive_products(token)
    print(productos)
except RuntimeError as err:
    print(f"No se pudo obtener datos: {err}")
```

Detalles:
* `httpx.Client(timeout=10.0)` aplica timeout de 10 segundos a conexión y lectura.
* Retry máximo 3 intentos con backoff exponencial 1s → 2s → 4s.
* Solo se reintenta en errores de red, timeout y HTTP 5xx/429.
* El resultado se filtra por `price > 100` y se normaliza a `{id, name, price}`.