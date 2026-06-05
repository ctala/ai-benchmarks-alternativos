# Gemma 4 12B (Spark llama-server, reasoning) — code_generation/python_api_integration

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 8.21 | quality: 9.72
- latency_total: 65.595s | tokens_per_second: 25.6
- input_tokens: 120 | output_tokens: 1680
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para resolver este problema, utilizaremos `httpx` para las peticiones y la librería estándar `time` para gestionar el backoff exponencial.

Aquí tienes la solución:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    max_retries = 3
    timeout = 10.0
    
    for attempt in range(max_retries):
        try:
            # Realizamos la petición con el timeout especificado
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                
                # Lanza una excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                data = response.json()
                
                # Filtrar y transformar la data
                # Filtro: precio > 100
                # Transformación: solo {id, name, price}
                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in data
                    if p.get("price", 0) > 100
                ]
                
                return filtered_products

        except (httpx.RequestError, httpx.TimeoutException) as e:
            # Si es el último intento, lanzamos la excepción
            if attempt == max_retries - 1:
                print(f"Error final tras {max_retries} intentos: {e}")
                raise e
            
            # Calcular backoff exponencial: 2^0, 2^1, 2^2... (1s, 2s, 4s)
            wait_time = 2 ** attempt
            print(f"Error detectado ({e}). Reintentando en {wait_time}s...")
            time.sleep(wait_time)

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        token_ejemplo = "tu_token_aqui"
        productos = get_expensive_products(token_ejemplo)
        print(productos)
    except Exception as err:
        print(f"No se pudo obtener la información: {err}")
```

### Explicación de la solución:

1.  **Uso de `httpx.Client`**: Se utiliza dentro de un contexto (`with`) para asegurar que la conexión se cierre correctamente. Se define el `timeout=10.0` como pide el requerimiento.
2.  **Autenticación**: Se inyecta el token en el header `Authorization` usando el formato estándar `Bearer`.
3.  **Manejo de Errores**: Capturamos `httpx.RequestError` (errores de conexión, DNS, etc.) y `httpx.TimeoutException`.
4.  **Retry con Backoff Exponencial**: 
    *   Usamos un bucle `for` para los 3 intentos.
    *   `time.sleep(2 ** attempt)` genera esperas de 1, 2 y 4 segundos respectivamente antes de reintentar.
5.  **List Comprehension**: Se utiliza para filtrar los productos con precio mayor a 100 y, en una sola línea, reconstruir los diccionarios con las llaves solicitadas (`id`, `name`, `price`).
6.  **Sin dependencias extra**: Solo se utilizan `httpx` (solicitado) y módulos nativos de Python (`time`, `typing`).