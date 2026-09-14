# Gemini 3.8 Flash — code_generation/python_api_integration

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.46 | quality: 9.72
- latency_total: 17.236s | tokens_per_second: 102.5
- input_tokens: 105 | output_tokens: 1767
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

Aquí tienes la solución utilizando únicamente `httpx` y la biblioteca estándar de Python:

```python
import time
from typing import Any, Dict, List
import httpx


def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """Obtiene productos desde la API externa, reintentando con backoff exponencial

    si ocurren fallos de red o timeout, y retorna solo aquellos con precio > 100.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    timeout = 10.0  # Segundos
    max_retries = 3
    base_delay = 1.0  # Tiempo base para backoff: 1s, 2s, 4s...

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                products = response.json()

                # Filtrar y proyectar los campos requeridos
                return [
                    {
                        "id": item["id"],
                        "name": item["name"],
                        "price": item["price"],
                    }
                    for item in products
                    if item.get("price", 0) > 100
                ]

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # Si es el último intento, propagamos el error
            if attempt == max_retries - 1:
                raise RuntimeError(
                    f"Fallaron los {max_retries} intentos. Último error: {exc}"
                ) from exc

            # Backoff exponencial: 2^attempt * base_delay (1s, 2s)
            sleep_time = base_delay * (2**attempt)
            time.sleep(sleep_time)

    return []
```

### Características implementadas:
1. **Autenticación**: Cabecera `Authorization: Bearer <token>`.
2. **Filtrado y transformación**: Comprensión de listas que valida `price > 100` y extrae únicamente `{id, name, price}`.
3. **Manejo de errores y timeout**: Se especifica `timeout=10.0` (cubre conexión, lectura y escritura) y se capturan `httpx.RequestError` (timeouts, DNS, caída de red) y `httpx.HTTPStatusError` (códigos 4xx/5xx).
4. **Retry con Backoff Exponencial**:
   - Intento 1: Si falla, duerme `1s` ($1 \cdot 2^0$).
   - Intento 2: Si falla, duerme `2s` ($1 \cdot 2^1$).
   - Intento 3: Si falla, agota los intentos y lanza una excepción explicativa.