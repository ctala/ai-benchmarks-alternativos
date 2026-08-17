# Llama 4 Scout 17B (Groq preview) — code_generation/python_api_integration

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 8.11 | quality: 9.32
- latency_total: 2.004s | tokens_per_second: 280.4
- input_tokens: 102 | output_tokens: 562
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí te dejo una función que cumple con los requisitos solicitados:
```python
import httpx
import time
import logging

logging.basicConfig(level=logging.INFO)

def get_products(token: str) -> list:
    """
    Obtiene productos de https://api.example.com/products con autenticación Bearer token
    y retorna una lista de dicts con id, name y price de productos con precio > 100.

    :param token: Token de autenticación Bearer
    :return: Lista de dicts con id, name y price de productos
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    params = {}

    max_retries = 3
    backoff_factor = 1  # segundos
    timeout = 10  # segundos

    for attempt in range(max_retries):
        try:
            response = httpx.get(url, headers=headers, params=params, timeout=timeout)
            response.raise_for_status()  # Lanza excepción si el código de estado no es 200
            break
        except httpx.HTTPError as e:
            logging.error(f"Error en intento {attempt+1}: {e}")
            if attempt < max_retries - 1:
                backoff = backoff_factor * (2 ** attempt)
                logging.info(f"Reintentando en {backoff} segundos...")
                time.sleep(backoff)
            else:
                raise

    products = response.json()
    filtered_products = [
        {"id": p["id"], "name": p["name"], "price": p["price"]}
        for p in products
        if p["price"] > 100
    ]

    return filtered_products
```
Aquí hay un ejemplo de uso:
```python
token = "mi_token_de_autenticacion"
try:
    products = get_products(token)
    print(products)
except Exception as e:
    logging.error(f"Error: {e}")
```
Notas:

* Utilizo `httpx` para realizar la solicitud GET con autenticación Bearer token.
* Configuro un timeout de 10 segundos para la solicitud.
* Implementé retry con backoff exponencial, con un máximo de 3 intentos. En cada intento fallido, espero un tiempo que se duplica exponencialmente (1, 2, 4 segundos, etc.) antes de reintentar.
* Filtré los productos con precio > 100 utilizando una lista de comprensión.
* Retorné una lista de dicts con solo los campos `id`, `name` y `price`.
* Manejo errores de red y timeout mediante excepción `httpx.HTTPError`.
* Utilicé `logging` para registrar información y errores.