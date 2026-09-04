# Gemma 4 31B — code_generation/python_api_integration

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.01 | quality: 9.72
- latency_total: 6.026s | tokens_per_second: 277.3
- input_tokens: 120 | output_tokens: 1671
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

Para implementar esta funcionalidad utilizando únicamente `httpx` y la librería estándar de Python, podemos estructurar la función con un bucle de reintentos y un bloque `try-except`.

Aquí tienes el código completo:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    # Configuración de timeout (10 segundos)
    timeout = httpx.Timeout(10.0)
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            # Usamos Client como context manager para eficiencia de conexiones
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                
                # Lanza excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                products = response.json()
                
                # Filtrado y mapeo de datos
                # Retorna solo id, name y price si price > 100
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products 
                    if p.get("price", 0) > 100
                ]

        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            # Si es el último intento, lanzamos la excepción
            if attempt == max_retries - 1:
                print(f"Error final después de {max_retries} intentos: {e}")
                raise e
            
            # Backoff exponencial: 2^0=1s, 2^1=2s, 2^2=4s...
            wait_time = 2 ** attempt
            print(f"Intento {attempt + 1} fallido. Reintentando en {wait_time}s...")
            time.sleep(wait_time)

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        token_usuario = "tu_token_aqui"
        resultado = get_expensive_products(token_usuario)
        print(resultado)
    except Exception as err:
        print(f"La solicitud falló: {err}")
```

### Explicación de los puntos clave:

1.  **Autenticación**: Se pasa el token en el encabezado `Authorization` siguiendo el estándar `Bearer <token>`.
2.  **Filtrado y Transformación**: He utilizado una *list comprehension* que realiza dos tareas en un solo paso: filtra los productos cuyo precio es mayor a 100 y crea un nuevo diccionario extrayendo únicamente las llaves solicitadas (`id`, `name`, `price`).
3.  **Manejo de Errores**: 
    *   `httpx.RequestError`: Captura problemas de red, DNS o timeouts.
    *   `response.raise_for_status()`: Convierte códigos de error HTTP (como 500 Internal Server Error) en una excepción `HTTPStatusError` para que el bucle de reintentos pueda capturarla.
4.  **Timeout**: Se define un objeto `httpx.Timeout(10.0)` que se aplica a todas las etapas de la petición (conexión, lectura, escritura).
5.  **Retry con Backoff Exponencial**:
    *   Se utiliza un bucle `for` hasta `max_retries`.
    *   `time.sleep(2 ** attempt)` implementa la espera exponencial: el primer fallo espera 1 segundo, el segundo 2 segundos, etc.
    *   Si se llega al último intento y sigue fallando, se relanza la excepción original mediante `raise e`.