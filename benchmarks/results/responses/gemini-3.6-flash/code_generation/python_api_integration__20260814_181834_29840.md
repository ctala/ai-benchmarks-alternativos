# Gemini 3.6 Flash — code_generation/python_api_integration

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.34 | quality: 9.48
- latency_total: 8.222s | tokens_per_second: 248.6
- input_tokens: 105 | output_tokens: 2044
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

Aquí tienes la función en Python utilizando **`httpx`** y librerías nativas del lenguaje.

```python
import time
from typing import Any, Dict, List
import httpx


def fetch_expensive_products(token: str) -> List[Dict[str, Any]]:
    """Obtiene productos de la API, aplica un filtro por precio (>100) y

    devuelve solo las claves id, name y price.

    Incluye reintentos con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10.0  # Timeout de 10 segundos
    max_retries = 3
    base_backoff_seconds = 1  # Tiempo base para el backoff exponencial

    for attempt in range(max_retries):
        try:
            # Usamos un cliente HTTP con el timeout configurado
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                # Lanza HTTPStatusError si la respuesta es 4xx o 5xx
                response.raise_for_status()

            # Asumimos que la API retorna una lista de dicts o un objeto con clave 'products'
            data = response.json()
            products = (
                data.get("products", []) if isinstance(data, dict) else data
            )

            # Filtrar productos con precio > 100 y extraer solo id, name, price
            filtered_products = [
                {
                    "id": item["id"],
                    "name": item["name"],
                    "price": item["price"],
                }
                for item in products
                if item.get("price", 0) > 100
            ]

            return filtered_products

        except httpx.HTTPStatusError as exc:
            # No reintentar si es un error del cliente (4xx) a menos que sea 429 (Too Many Requests)
            if (
                400 <= exc.response.status_code < 500
                and exc.response.status_code != 429
            ):
                raise exc

            # Si es el último intento, volvemos a lanzar la excepción
            if attempt == max_retries - 1:
                raise exc

        except httpx.RequestError as exc:
            # Maneja errores de red, DNS, Timeouts, etc.
            if attempt == max_retries - 1:
                raise exc

        # Cálculo de backoff exponencial: 1s, 2s, 4s...
        sleep_time = base_backoff_seconds * (2**attempt)
        time.sleep(sleep_time)

    return []
```

### Características implementadas:
1. **Autenticación Bearer**: Se envía en el encabezado `Authorization: Bearer <token>`.
2. **Filtrado y Transformación**: Mediante una comprensión de listas, se filtran elementos con `price