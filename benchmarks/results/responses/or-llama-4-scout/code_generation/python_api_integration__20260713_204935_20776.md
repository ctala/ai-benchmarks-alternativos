# Llama 4 Scout 17B — code_generation/python_api_integration

- model_id: `meta-llama/llama-4-scout`
- success: True  | final: 9.08 | quality: 9.12
- latency_total: 1.603s | tokens_per_second: 351.9
- input_tokens: 102 | output_tokens: 564
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí te dejo una posible implementación de la función que estás solicitando:
```python
import httpx
import time
import logging

logging.basicConfig(level=logging.INFO)

def get_products(token: str) -> list:
    """
    Retrieves products from https://api.example.com/products with Bearer token auth.
    Filters products with price > 100 and returns a list of dicts with id, name, and price.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    params = {}

    max_retries = 3
    retry_delay = 1  # inicial
    retry_count = 0

    while retry_count <= max_retries:
        try:
            response = httpx.get(
                url,
                headers=headers,
                params=params,
                timeout=10.0,  # timeout de 10 segundos
            )
            response.raise_for_status()  # lanza excepción si el código de estado es 4xx o 5xx
            break
        except (httpx.NetworkError, httpx.Timeout) as e:
            logging.warning(f"Error de red o timeout: {e}")
            retry_count += 1
            if retry_count <= max_retries:
                retry_delay *= 2  # backoff exponencial
                logging.info(f"Reintentando en {retry_delay} segundos...")
                time.sleep(retry_delay)
            else:
                raise

    products = response.json()
    filtered_products = [
        {"id": product["id"], "name": product["name"], "price": product["price"]}
        for product in products
        if product["price"] > 100
    ]
    return filtered_products
```
Aquí hay algunas notas sobre la implementación:

* Utilizamos la biblioteca `httpx` para realizar la solicitud GET.
* Configuramos la autenticación Bearer token en el header `Authorization`.
* Establecemos un timeout de 10 segundos para la solicitud.
* Implementamos un mecanismo de retry con backoff exponencial (inicialmente 1 segundo, luego 2, 4, 8, ...). Si se excede el número máximo de retries (3), se lanza la excepción.
* Manejamos errores de red y timeout mediante excepción `httpx.NetworkError` y `httpx.Timeout`.
* Filtramos los productos con precio > 100 utilizando una lista de comprensión.
* Retornamos una lista de dicts con solo los campos `id`, `name` y `price`.

Puedes llamar a esta función pasando un token de autenticación válido, por ejemplo:
```python
token = "mi_token_de_autenticacion"
products = get_products(token)
print(products)
```