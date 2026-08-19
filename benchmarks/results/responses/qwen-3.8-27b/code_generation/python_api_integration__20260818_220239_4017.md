# Qwen 3.8 27B — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.63 | quality: 9.32
- latency_total: 182.113s | tokens_per_second: 41.7
- input_tokens: 155 | output_tokens: 7592
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



Claro. Aquí tienes una función síncrona usando `httpx`, timeout de 10 segundos, retry con backoff exponencial y máximo 3 intentos.

```python
import time
import httpx
from typing import Any, Dict, List, Optional


def get_products_over_100(
    token: str,
    url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout: float = 10.0,
    base_delay: float = 1.0,
) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde una API.

    - GET a la URL con Bearer token
    - Timeout de 10 segundos
    - Retry con backoff exponencial, máximo 3 intentos
    - Maneja errores de red y timeout
    - Retorna solo: {"id": ..., "name": ..., "price": ...}
    """
    if not token:
        raise ValueError("token es obligatorio")

    if max_retries < 1:
        raise ValueError("max_retries debe ser >= 1")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    last_error: Optional[Exception] = None

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)

                # Lanza excepción si la API devuelve 4xx/5xx
                response.raise_for_status()

                data = response.json()

                # Compatible con:
                # 1) [ {...}, {...} ]
                # 2) { "products": [ {...}, {...} ] }
                if isinstance(data, dict) and "products" in data:
                    products = data["products"]
                elif isinstance(data, list):
                    products = data
                else:
                    raise ValueError("Respuesta JSON inesperada")

                if not isinstance(products, list):
                    raise ValueError("El campo 'products' no es una lista")

                filtered = []

                for product in products:
                    if not isinstance(product, dict):
                        continue

                    price = product.get("price")

                    # Evita bool, que en Python es subclase de int
                    if isinstance(price, bool):
                        continue

                    if isinstance(price, (int, float)):
                        parsed_price = price
                    elif isinstance(price, str):
                        try:
                            parsed_price = float(price)
                        except ValueError:
                            continue
                    else:
                        continue

                    if parsed_price > 100:
                        filtered.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": parsed_price,
                            }
                        )

                return filtered

            except httpx.TransportError as exc:
                # httpx.TransportError cubre errores de red y timeout
                last_error = exc

                if attempt < max_retries - 1:
                    # Backoff exponencial:
                    # intento 0 -> 1s
                    # intento 1 -> 2s
                    # intento 2 -> no duerme, porque es el último
                    delay = base_delay * (2 ** attempt)
                    time.sleep(delay)

    if last_error is not None:
        raise last_error

    raise RuntimeError("No se realizó ningún intento de petición")
```

Ejemplo de uso:

```python
try:
    productos = get_products_over_100(token="mi-token")
    print(productos)
except Exception as e:
    print("Error obteniendo productos:", e)
```

Notas:

- `httpx.Client(timeout=10.0)` aplica un timeout de 10 segundos.
- El retry se aplica solo ante errores de red/timeout, es decir, `httpx.TransportError`.
- Si la API devuelve un error HTTP como `401`, `403`, `500`, etc., la función lo propaga mediante `response.raise_for_status()`.
- Si quieres reintentar también errores HTTP temporales como `429` o `5xx`, puedes ampliar la lógica de retry.