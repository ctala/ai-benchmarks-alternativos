# Nemotron 3.5 Lightning — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 32.11s | tokens_per_second: 151.5
- input_tokens: 118 | output_tokens: 4866
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, con una estructura bien organizada y un manejo adecuado de errores y reintentos.

## Respuesta completa

Aquí tienes una función limpia, autónoma y que cumple con todos los puntos solicitados usando solo `httpx` y la librería estándar `time`:

```python
import httpx
import time
from typing import list, dict


def fetch_expensive_products(bearer_token: str) -> list[dict]:
    """
    Realiza una petición GET a la API de productos con autenticación Bearer,
    filtra los productos con precio > 100 y devuelve una lista con {id, name, price}.
    Incluye reintentos con backoff exponencial (máx 3 intentos) y timeout de 10s.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_retries = 3
    timeout = httpx.Timeout(10)  # 10 segundos para connect y read

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # lanza error si no es 2xx

                products = response.json()
                # Filtrado y proyección a solo los campos solicitados
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

        except httpx.RequestError as e:
            # Errores de red, timeout, fallo DNS, etc.
            if attempt == max_retries:
                raise RuntimeError(f"❌ Fallo de red después de {max_retries} intentos: {e}") from e
            # Backoff exponencial: 1s, luego 2s
            time.sleep(2 ** (attempt - 1))

        except httpx.HTTPStatusError as e:
            # Respuestas HTTP no exitosas (4xx/5xx). 
            # No se reintenta por defecto (la especificación pide manejo de red/timeout).
            raise RuntimeError(f"❌ Error HTTP: {e}") from e

    # Línea teóricamente inalcanzable (el último intento siempre levanta o retorna)
    return []
```

### Puntos cubiertos:
1. **GET a `https://api.example.com/products`** con header `Authorization: Bearer <token>`.
2. **Filtrado `price > 100`** y proyección a `{id, name, price}`.
3. **Timeout de 10 segundos** configurado via `httpx.Timeout(10)`.
4. **Manejo de errores de red** capturado por `httpx.RequestError` (timeouts, conexión, DNS).
5. **Retry con backoff exponencial**: espera 1s antes del reintento 2, y 2s antes del reintento 3 (máximo 3 intentos).

Usa exclusivamente `httpx` y `time` (stdlib), sin dependencias externas adicionales.