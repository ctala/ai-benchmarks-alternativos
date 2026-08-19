# Gemini 3.7 Flash — code_generation/python_api_integration

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.43 | quality: 9.48
- latency_total: 11.373s | tokens_per_second: 151.1
- input_tokens: 104 | output_tokens: 1718
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

Aquí tienes la solución implementada con `httpx` y la librería estándar de Python (`time` y `typing`):

```python
import time
from typing import Any, Dict, List
import httpx


def get_expensive_products(token: str, max_retries: int = 3) -> List[Dict[str, Any]]:
    """Obtiene productos de la API, reintenta ante fallos con backoff exponencial

    y devuelve aquellos con precio mayor a 100 conteniendo solo id, name y
    price.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    timeout = 10.0  # 10 segundos de timeout

    for attempt in range(max_retries):
        try:
            # Usamos un cliente con el timeout configurado
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                # Maneja si la API devuelve directamente una lista o un objeto con clave 'products'
                items = data if isinstance(data, list) else data.get("products", [])

                # Filtrar precio > 100 y proyectar solo {id, name, price}
                result = [
                    {
                        "id": item["id"],
                        "name": item["name"],
                        "price": item["price"],
                    }
                    for item in items
                    if isinstance(item.get("price"), (int, float))
                    and item["price"] > 100
                ]
                return result

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # Si se agotaron los intentos, propagamos el error
            if attempt == max_retries - 1:
                raise RuntimeError(
                    f"Fallaron todos los {max_retries} intentos. Último error: {exc}"
                ) from exc

            # Backoff exponencial: 1s, 2s, 4s...
            sleep_time = 2**attempt
            time.sleep(sleep_time)

    return []
```

### Características implementadas:
1. **Autenticación:** Cabecera `Authorization: Bearer <token>`.
2. **Timeout:** Configurado explícitamente a `10.0` segundos en el cliente `httpx`.
3. **Manejo de Errores y Reintentos:** Captura `httpx.RequestError` (errores de red, DNS, timeouts) y `httpx.HTTPStatusError` (códigos 4xx/5xx).
4. **Backoff Exponencial:** Espera `2^intento` segundos (`1s`, `2s`, `4s`) antes de reintentar.
5. **Filtrado y Mapeo:** Extrae y devuelve únicamente los campos `id`, `name` y `price` de los elementos cuyo `price > 100`.