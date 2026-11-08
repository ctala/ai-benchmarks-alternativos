# Nemotron 3 Super — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.36 | quality: 9.52
- latency_total: 84.553s | tokens_per_second: 34.9
- input_tokens: 118 | output_tokens: 2952
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

Aquí tienes una función síncrona usando **httpx** y solo la librería estándar de Python. Implementa reintentos con backoff exponencial, timeout de 10 segundos y filtra los productos con precio mayor a 100.

```python
import httpx
import time
from typing import List, Dict, Any, Optional


def get_products_over_100(
    bearer_token: str,
    max_retries: int = 3,
    timeout: float = 10.0,
) -> List[Dict[str, Any]]:
    """
    Consulta https://api.example.com/products con autenticación Bearer,
    filtra productos con precio > 100 y retorna solo {id, name, price}.

    Args:
        bearer_token: Token JWT/Bearer para la cabecera Authorization.
        max_retries: Número máximo de intentos (default 3).
        timeout: Tiempo de espera por petición en segundos (default 10).

    Returns:
        Lista de diccionarios con las claves id, name y price.

    Raises:
        httpx.HTTPError: Si se agotan los reintentos.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}

    last_exception: Optional[Exception] = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)

                # Lanza excepción para códigos 4xx / 5xx
                response.raise_for_status()

                data = response.json()

                if not isinstance(data, list):
                    raise ValueError("La respuesta de la API no es una lista")

                filtered: List[Dict[str, Any]] = []
                for product in data:
                    if not isinstance(product, dict):
                        continue

                    price = product.get("price")
                    if isinstance(price, (int, float)) and price > 100:
                        filtered.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": price,
                        })

                return filtered

        except httpx.TimeoutException as exc:
            last_exception = exc
        except httpx.RequestError as exc:
            last_exception = exc
        except httpx.HTTPStatusError as exc:
            last_exception = exc

        # Backoff exponencial: 1s, 2s, 4s ... (solo si no es el último intento)
        if attempt < max_retries - 1:
            backoff_seconds = 2 ** attempt
            time.sleep(backoff_seconds)

    # Si se agotaron los intentos, relanzar la última excepción capturada
    if last_exception:
        raise last_exception

    return []


# Ejemplo de uso (descomentar y ajustar para probar):
# if __name__ == "__main__":
#     try:
#         productos = get_products_over_100("mi_token_aqui")
#         print(productos)
#     except httpx.HTTPError as e:
#         print(f"Error tras reintentos: {e}")
```

### Puntos clave

| Requisito | Implementación |
|-----------|----------------|
| **GET + Bearer** | Cabecera `Authorization: Bearer <token>` con `httpx.Client.get`. |
| **Filtrar precio > 100** | Se valida que `price` sea numérico y se queda solo si es mayor a 100. |
| **Solo {id, name, price}** | Se construye un nuevo dict con únicamente esas tres claves. |
| **Timeout 10 s** | `httpx.Client(timeout=10.0)`. |
| **Errores de red** | Se capturan `httpx.TimeoutException`, `httpx.RequestError` y `httpx.HTTPStatusError`. |
| **Retry con backoff** | `time.sleep(2 ** attempt)` entre intentos (1s, 2s, 4s). Máximo 3 intentos. |

Si necesitas una versión **asíncrona** (`async/await`) con `httpx.AsyncClient`, dímelo y la adapto.