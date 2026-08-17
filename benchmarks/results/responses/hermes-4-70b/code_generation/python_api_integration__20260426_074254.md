# Hermes 4 70B — code_generation/python_api_integration

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 7.37 | quality: 8.64
- latency_total: 6.788s | tokens_per_second: 72.2
- input_tokens: 125 | output_tokens: 490
- judge_score: 4.2 | justificación: 

## Respuesta completa

```python
import httpx
import time

def get_expensive_products():
    url = "https://api.example.com/products"
    token = "YOUR_BEARER_TOKEN"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10

    for attempt in range(max_retries):
        try:
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()
                products = response.json()
                
                expensive_products = [
                    {item["id"], item["name"], item["price"]}
                    for item in products
                    if item["price"] > 100
                ]
                return expensive_products
                
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            if attempt < max_retries - 1:
                sleep_time = 2 ** attempt
                time.sleep(sleep_time)
            else:
                raise Exception(f"Error after {max_retries} retries: {str(e)}")

# Ejemplo de uso
products = get_expensive_products()
print(products)
```

Explicación:

1. Se configura la URL, el token de autenticación y los encabezados
2. Se define un bucle para los reintentos (máximo 3 veces)
3. Dentro del bucle, se usa `httpx.Client()` como contexto para manejar la conexión
4. Se realiza el request GET y se verifica el estado de la respuesta
5. Se parsea la respuesta JSON y se filtran los productos con precio > 100
6. Se construye la lista de diccionarios con los campos requeridos
7. Si ocurre un error de red o de estado HTTP, se espera un tiempo exponencial (2^n intento) antes de reintentar
8. Si fallan todos los intentos, se lanza una excepción con el error final

Notas:
- Reemplaza `"YOUR_BEARER_TOKEN"` con tu token real
- Asegúrate de tener instalado el paquete `httpx` (`pip install httpx`)
- El timeout es de 10 segundos como se pidió
- La función devuelve la lista de productos o lanza una excepción si falla después de los reintentos