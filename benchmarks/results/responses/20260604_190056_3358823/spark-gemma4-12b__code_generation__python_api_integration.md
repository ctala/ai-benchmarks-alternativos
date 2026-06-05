# Gemma 4 12B (Spark llama-server Q4_K_M) — code_generation/python_api_integration

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 8.02 | quality: 9.48
- latency_total: 78.918s | tokens_per_second: 25.3
- input_tokens: 120 | output_tokens: 1993
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para resolver este problema, utilizaremos `httpx` para las peticiones y un bucle `for` con `time.sleep` para implementar la lógica de reintentos con backoff exponencial manualmente, ya que no podemos usar librerías externas como `tenacity`.

Aquí tienes el código:

```python
import httpx
import time
from typing import List, Dict, Any

def get_filtered_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    max_retries = 3
    timeout = 10.0
    
    for attempt in range(max_retries):
        try:
            # Usamos un cliente con el timeout especificado
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                
                # Lanza una excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                products = response.json()
                
                # Filtrar productos con precio > 100 y mapear a los campos requeridos
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

        except (httpx.RequestError, httpx.TimeoutException, httpx.HTTPStatusError) as e:
            print(f"Intento {attempt + 1} falló: {e}")
            
            # Si es el último intento, lanzamos la excepción o retornamos vacío
            if attempt == max_retries - 1:
                print("Se agotaron los reintentos.")
                return []
            
            # Backoff exponencial: 2^1, 2^2, 2^3... segundos
            wait_time = 2 ** (attempt + 1)
            time.sleep(wait_time)

    return []

# Ejemplo de uso:
if __name__ == "__main__":
    token_ejemplo = "tu_token_aqui"
    resultado = get_filtered_products(token_ejemplo)
    print(resultado)
```

### Explicación de la solución:

1.  **`httpx.Client(timeout=10.0)`**: Creamos una instancia del cliente especificando el tiempo máximo de espera para evitar que la función se quede bloqueada infinitamente.
2.  **`response.raise_for_status()`**: Esta es una buena práctica; asegura que si el servidor responde con un error (como 404 o 500), la ejecución salte directamente al bloque `except`.
3.  **Manejo de Errores**: Capturamos `httpx.RequestError` (errores de red), `httpx.TimeoutException` (tiempo agotado) y `httpx.HTTPStatusError` (errores de respuesta del servidor).
4.  **Backoff Exponencial**: 
    *   En el primer fallo, espera $2^1 = 2$ segundos.
    *   En el segundo fallo, espera $2^2 = 4$ segundos.
    *   En el tercer fallo, termina la ejecución.
5.  **List Comprehension**: Se utiliza para filtrar los productos y reconstruir el diccionario con solo las llaves `{id, name, price}` en una sola línea eficiente.
6.  **Sin dependencias adicionales**: Solo se importan `httpx` y módulos estándar de Python (`time`, `typing`).