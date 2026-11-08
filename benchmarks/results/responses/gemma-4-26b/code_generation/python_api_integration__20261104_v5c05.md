# Gemma 4 26B MoE (3.8B activos) — code_generation/python_api_integration

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.9 | quality: 9.72
- latency_total: 19.716s | tokens_per_second: 52.6
- input_tokens: 117 | output_tokens: 1037
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

Para resolver este problema, utilizaremos la librería `httpx` para las peticiones y el módulo estándar `time` para implementar la lógica de backoff exponencial manualmente, cumpliendo con la restricción de no usar dependencias externas adicionales (como `tenacity`).

Aquí tienes la implementación:

```python
import httpx
import time

def get_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100
    y retorna una lista con id, name y price.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    timeout = 10.0  # segundos
    
    # Configuración de la petición
    # Usamos un bloque try/except para manejar errores de red y reintentos
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                
                # Lanza una excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                products = response.json()
                
                # 2. Filtrar productos con precio > 100
                # 3. Retornar lista de dicts con {id, name, price}
                filtered_products = [
                    {
                        "id": p["id"],
                        "name": p["name"],
                        "price": p["price"]
                    }
                    for p in products 
                    if p.get("price", 0) > 100
                ]
                
                return filtered_products

        except (httpx.ConnectError, httpx.TimeoutException, httpx.HTTPStatusError) as e:
            # 4 y 5. Manejo de errores y lógica de Retry con Backoff Exponencial
            print(f"Intento {attempt + 1} fallido: {e}")
            
            if attempt == max_retries - 1:
                print("Se alcanzó el máximo de reintentos.")
                raise e
            
            # Backoff exponencial: 2^0, 2^1, 2^2... (1s, 2s, 4s)
            wait_time = 2 ** attempt
            print(f"Reintentando en {wait_time} segundos...")
            time.sleep(wait_time)
            
        except Exception as e:
            # Errores inesperados (ej. error de parseo de JSON) que no deben reintentarse
            print(f"Error inesperado: {e}")
            raise e

    return []

# --- Ejemplo de uso ---
if __name__ == "__main__":
    TOKEN = "tu_token_aqui"
    try:
        resultado = get_expensive_products(TOKEN)
        print("Productos filtrados:", resultado)
    except Exception as err:
        print("Error final en la ejecución:", err)
```

### Explicación técnica:

1.  **Autenticación**: Se pasan los headers mediante un diccionario con el formato `{"Authorization": "Bearer <token>"}`.
2.  **Timeout**: Se configura `timeout=10.0` directamente en el cliente de `httpx`.
3.  **Backoff Exponencial**: Implementado con `time.sleep(2 ** attempt)`. 
    *   Intento 1 falla $\rightarrow$ espera $2^0 = 1$ segundo.
    *   Intento 2 falla $\rightarrow$ espera $2^1 = 2$ segundos.
    *   Intento 3 falla $\rightarrow$ lanza la excepción.
4.  **Manejo de Errores**: 
    *   `httpx.ConnectError` y `httpx.TimeoutException` capturan problemas de red.
    *   `response.raise_for_status()` permite capturar errores del servidor (como 500 Internal Server Error) para que entren en la lógica de reintento.
5.  **Filtrado y Transformación**: Se utiliza una *list comprehension* para realizar el filtrado (`if p.get("price", 0) > 100`) y la selección de campos (`id`, `name`, `price`) en un solo paso eficiente.
6.  **Seguridad**: Se usa `.get("price", 0)` al filtrar para evitar que la función falle si un producto de la API no tiene el campo `price`.