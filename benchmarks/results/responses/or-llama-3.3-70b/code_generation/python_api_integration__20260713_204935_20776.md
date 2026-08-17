# Llama 3.3 70B — code_generation/python_api_integration

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 8.69 | quality: 9.52
- latency_total: 12.773s | tokens_per_second: 40.0
- input_tokens: 112 | output_tokens: 511
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí te dejo una posible implementación:
```python
import httpx
import time
import logging

logging.basicConfig(level=logging.INFO)

def get_products(token: str) -> list:
    """
    Obtiene productos con precio > 100 desde la API de example.com
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10

    for attempt in range(max_retries):
        try:
            response = httpx.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            products = response.json()
            filtered_products = [{"id": p["id"], "name": p["name"], "price": p["price"]} for p in products if p["price"] > 100]
            return filtered_products
        except httpx.NetworkError as e:
            logging.error(f"Error de red: {e}")
            time.sleep(2 ** attempt)  # backoff exponencial
        except httpx.TimeoutException:
            logging.error("Timeout")
            time.sleep(2 ** attempt)  # backoff exponencial
        except httpx.HTTPStatusError as e:
            logging.error(f"Error HTTP: {e}")
            break  # no retry para errores HTTP

    logging.error("Max retries alcanzados")
    return []

# Ejemplo de uso:
token = "mi_token_secreto"
products = get_products(token)
print(products)
```
Aquí se utiliza la biblioteca `httpx` para realizar la solicitud GET a la API. Se incluye autenticación Bearer token en la cabecera `Authorization`.

La función `get_products` realiza la solicitud y maneja los siguientes errores:

* `httpx.NetworkError`: errores de red (por ejemplo, conexión rechazada)
* `httpx.TimeoutException`: timeouts (si la solicitud tarda más de 10 segundos en responder)
* `httpx.HTTPStatusError`: errores HTTP (por ejemplo, 404, 500)

En caso de error, se realiza un retry con backoff exponencial (2^intentos) durante un máximo de 3 intentos. Si se alcanza el máximo de intentos, se devuelve una lista vacía.

La función devuelve una lista de diccionarios con solo los campos `id`, `name` y `price` para los productos con precio mayor a 100.