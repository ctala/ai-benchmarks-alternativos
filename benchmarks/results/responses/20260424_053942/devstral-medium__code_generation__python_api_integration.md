# Devstral Medium — code_generation/python_api_integration

- model_id: `mistralai/devstral-medium`
- success: True  | final: 7.65 | quality: 9.44
- latency_total: 6.25s | tokens_per_second: 95.4
- input_tokens: 105 | output_tokens: 596
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para lograr esto, puedes usar la biblioteca `httpx` en Python. Aquí tienes un ejemplo de cómo podrías implementar la función:

```python
import httpx
import time

def fetch_products_with_retry(url, token, max_retries=3, timeout=10):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Raise an exception for HTTP errors
                products = response.json()

                # Filter products with price > 100
                filtered_products = [
                    {"id": product["id"], "name": product["name"], "price": product["price"]}
                    for product in products if product["price"] > 100
                ]

                return filtered_products

        except httpx.HTTPStatusError as exc:
            print(f"HTTP error occurred: {exc}")
            break
        except httpx.RequestError as exc:
            print(f"Request error occurred: {exc}")
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries reached, giving up.")
                break

    return []

# Example usage
url = "https://api.example.com/products"
token = "your_bearer_token_here"
filtered_products = fetch_products_with_retry(url, token)
print(filtered_products)
```

### Explicación:

1. **Autenticación Bearer Token**: Se incluye el token en los headers de la solicitud.
2. **Filtrado de Productos**: Se filtra la lista de productos para incluir solo aquellos con un precio mayor a 100.
3. **Manejo de Errores**: Se manejan errores de red y timeout utilizando `httpx.RequestError` y `httpx.HTTPStatusError`.
4. **Retry con Backoff Exponencial**: Se implementa un mecanismo de reintento con backoff exponencial, donde el tiempo de espera entre intentos aumenta exponencialmente.

### Notas:

- **httpx.Client**: Se utiliza un cliente `httpx` para manejar la conexión y el timeout.
- **Exponential Backoff**: El tiempo de espera entre intentos se calcula como `2 ** attempt`, lo que proporciona un backoff exponencial.
- **Max Retries**: Se limita el número de reintentos a `max_retries`.

Asegúrate de tener `httpx` instalado en tu entorno. Puedes instalarlo usando pip:

```sh
pip install httpx
```