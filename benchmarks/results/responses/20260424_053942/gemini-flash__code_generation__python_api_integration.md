# Gemini 2.5 Flash — code_generation/python_api_integration

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 7.03 | quality: 8.36
- latency_total: 11.083s | tokens_per_second: 183.6
- input_tokens: 105 | output_tokens: 2035
- judge_score: 4.0 | justificación: 

## Respuesta completa

Claro, aquí tienes una función Python que cumple con tus requisitos, utilizando `httpx` para las solicitudes HTTP y manejo de reintentos con backoff exponencial:

```python
import httpx
import asyncio
import time

async def get_high_priced_products(bearer_token: str) -> list[dict]:
    """
    Realiza una solicitud GET a 'https://api.example.com/products' con autenticación Bearer token,
    filtra los productos con precio > 100 y retorna una lista de diccionarios
    con solo {id, name, price}. Incluye manejo de errores de red, timeout y reintentos
    con backoff exponencial.

    Args:
        bearer_token: El token Bearer para la autenticación.

    Returns:
        Una lista de diccionarios con los productos filtrados, cada uno con 'id', 'name' y 'price'.
        Retorna una lista vacía si hay errores persistentes o no se encuentran productos.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json"
    }
    timeout_seconds = 10
    max_retries = 3
    base_delay = 1  # segundos para el primer reintento

    async with httpx.AsyncClient() as client:
        for attempt in range(max_retries):
            try:
                print(f"Intento {attempt + 1} de {max_retries} para {url}...")
                response = await client.get(url, headers=headers, timeout=timeout_seconds)
                response.raise_for_status()  # Lanza una excepción para códigos de estado 4xx/5xx

                products_data = response.json()
                
                # Asegurarse de que products_data sea una lista
                if not isinstance(products_data, list):
                    print("Advertencia: La respuesta de la API no es una lista. Intentando buscar 'products' key.")
                    if isinstance(products_data, dict) and "products" in products_data:
                        products_data = products_data["products"]
                    else:
                        print("Error: La respuesta de la API no es una lista de productos válida.")
                        return []

                filtered_products = []
                for product in products_data:
                    if isinstance(product, dict) and product.get("price", 0) > 100:
                        filtered_products.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": product.get("price")
                        })
                return filtered_products

            except httpx.TimeoutException:
                print(f"Error: Timeout después de {timeout_seconds} segundos. Intento {attempt + 1} fallido.")
            except httpx.NetworkError as e:
                print(f"Error de red: {e}. Intento {attempt + 1} fallido.")
            except httpx.HTTPStatusError as e:
                print(f"Error de estado HTTP {e.response.status_code}: {e.response.text}. Intento {attempt + 1} fallido.")
                if e.response.status_code == 401: # No autorizado, probablemente no tiene sentido reintentar
                    print("Error de autenticación 401. No se reintentará.")
                    return []
                if e.response.status_code == 404: # No encontrado, probablemente no tiene sentido reintentar
                    print("Recurso no encontrado 404. No se reintentará.")
                    return []
            except httpx.RequestError as e:
                print(f"Error general de solicitud: {e}. Intento {attempt + 1} fallido.")
            except Exception as e:
                print(f"Error inesperado: {e}. Intento {attempt + 1} fallido.")

            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                print(f"Reintentando en {delay} segundos...")
                await asyncio.sleep(delay)
            else:
                print(f"Todos los {max_retries} intentos fallaron. No se pudo obtener los productos.")

    return []

# --- Ejemplo de uso ---
async def main():
    # NOTA: Reemplaza "YOUR_BEARER_TOKEN" con tu token real
    # Y considera que https://api.example.com/products es un placeholder.
    # Para probar la función, podrías necesitar un mock server o una API real que controles.
    
    # Ejemplo de un token ficticio
    my_bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

    # Para simular una API que devuelve datos
    # Si quieres probar la función con datos reales, necesitarías una URL de API real.
    # Si quieres probar el manejo de errores, puedes modificar la URL a algo que falle,
    # o usar un mock server.

    try:
        products = await get_high_priced_products(my_bearer_token)
        if products:
            print("\nProductos con precio > 100:")
            for product in products:
                print(product)
        else:
            print("\nNo se encontraron productos o hubo un error.")
    except Exception as e:
        print(f"Un error ocurrió durante la ejecución de main: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Explicación y características:**

1.  **`httpx.AsyncClient()`**: Se utiliza un `AsyncClient` para realizar solicitudes asíncronas, lo cual es eficiente para operaciones de E/S como las solicitudes de red. El `async with` asegura que el cliente se cierre correctamente.

2.  **Autenticación Bearer Token**:
    *   Se construye un diccionario `headers` con la clave `"Authorization"` y el valor `f"Bearer {bearer_token}"`.
    *   Estos encabezados se pasan al método `client.get()`.

3.  **Filtrado de Productos**:
    *   Después de obtener una respuesta exitosa y parsear el JSON, la función itera sobre la lista de `products_data`.
    *   Para cada `product`, verifica si `product.get("price", 0)` es mayor que 100. `product.get("price", 0)` es una forma segura de acceder al valor, devolviendo `0` si la clave `price` no existe, para evitar `KeyError`.
    *   Si el producto cumple la condición, se crea un nuevo diccionario con solo `id`, `name` y `price` y se añade a `filtered_products`.

4.  **Manejo de Errores y Timeout**:
    *   **`httpx.TimeoutException`**: Captura errores cuando la solicitud excede el tiempo de espera configurado (`timeout_seconds`).
    *   **`httpx.NetworkError`**: Captura problemas de conectividad de red (DNS, conexión, etc.).
    *   **`httpx.HTTPStatusError`**: Captura errores de estado HTTP (4xx o 5xx) que son lanzados por `response.raise_for_status()`. Esto es crucial para manejar respuestas no exitosas de la API.
    *   **`httpx.RequestError`**: Es una clase base para muchos errores de `httpx`, útil como un catch-all más específico.
    *   **`Exception`**: Un catch-all final para cualquier otro error inesperado.
    *   **Timeout**: Se configura directamente en el `client.get()` con el parámetro `timeout=timeout_seconds`.

5.  **Reintentos con Backoff Exponencial**:
    *   Un bucle `for attempt in range(max_retries)` controla el número máximo de intentos.
    *   Si ocurre un error (capturado en los bloques `except`), se imprime un mensaje.
    *   `if attempt < max_retries - 1:`: Verifica si no es el último intento. Si no lo es, calcula el tiempo de espera.
    *   `delay = base_delay * (2 ** attempt)`: Implementa el backoff exponencial. El primer reintento espera `base_delay * 2^0 = base_delay` segundos, el segundo `base_delay * 2^1` segundos, y así sucesivamente.
    *   `await asyncio.sleep(delay)`: Pausa la ejecución de la corrutina por el tiempo calculado.

6.  **Retorno de Datos**:
