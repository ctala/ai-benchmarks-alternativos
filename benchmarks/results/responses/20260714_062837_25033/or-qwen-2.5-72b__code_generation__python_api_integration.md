# Qwen 2.5 72B — code_generation/python_api_integration

- model_id: `qwen/qwen-2.5-72b-instruct`
- success: True  | final: 8.74 | quality: 9.72
- latency_total: 17.609s | tokens_per_second: 43.7
- input_tokens: 112 | output_tokens: 769
- judge_score: 4.8 | justificación: 

## Respuesta completa

Claro, a continuación te presento una función en Python que cumple con los requisitos solicitados. Utilizamos la biblioteca `httpx` para manejar las solicitudes HTTP y el manejo de errores, timeouts y reintentos con backoff exponencial.

```python
import httpx
import time
from typing import List, Dict

def fetch_products(token: str) -> List[Dict[str, any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10

    def exponential_backoff(attempt: int) -> float:
        return (2 ** attempt) + 0.5

    for attempt in range(max_retries):
        try:
            response = httpx.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()  # Lanza una excepción si la respuesta es un error HTTP
            products = response.json()
            filtered_products = [
                {"id": product["id"], "name": product["name"], "price": product["price"]}
                for product in products
                if product.get("price", 0) > 100
            ]
            return filtered_products
        except (httpx.HTTPError, httpx.TimeoutException) as e:
            if attempt == max_retries - 1:
                raise Exception(f"Failed to fetch products after {max_retries} attempts: {e}")
            else:
                backoff_time = exponential_backoff(attempt)
                print(f"Request failed, retrying in {backoff_time} seconds...")
                time.sleep(backoff_time)

# Ejemplo de uso
if __name__ == "__main__":
    token = "your_bearer_token"
    try:
        products = fetch_products(token)
        print(products)
    except Exception as e:
        print(f"Error: {e}")
```

### Explicación del código:

1. **Importaciones y Configuración**:
   - Importamos `httpx` para manejar las solicitudes HTTP.
   - Importamos `time` para manejar el backoff exponencial.
   - Definimos el tipo de retorno de la función como `List[Dict[str, any]]`.

2. **Función `fetch_products`**:
   - Recibe un token de autenticación.
   - Define la URL de la API y los headers con el token de autenticación.
   - Configura el número máximo de reintentos (`max_retries`) y el timeout (`timeout`).

3. **Función `exponential_backoff`**:
   - Calcula el tiempo de espera exponencial basado en el número de intentos.

4. **Bucle de Reintentos**:
   - Intenta hacer una solicitud GET a la API.
   - Si la solicitud es exitosa, filtra los productos con precio mayor a 100 y devuelve una lista de diccionarios con `id`, `name` y `price`.
   - Si ocurre un error HTTP o de timeout, se maneja con una excepción.
   - Si se alcanza el número máximo de reintentos, se lanza una excepción.
   - Si no, se espera el tiempo de backoff exponencial y se vuelve a intentar.

5. **Ejemplo de Uso**:
   - Se proporciona un ejemplo de cómo llamar a la función `fetch_products` y manejar cualquier error que pueda ocurrir.

Este código es robusto y maneja varios escenarios de error, incluyendo reintentos con backoff exponencial.