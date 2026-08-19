# GLM 5.2 — code_generation/python_api_integration

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.13 | quality: 9.72
- latency_total: 61.864s | tokens_per_second: 40.4
- input_tokens: 113 | output_tokens: 2499
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la función en Python que cumple con todos los requisitos solicitados, utilizando la librería `httpx` y módulos estándar de Python:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de una API, filtra los que tienen precio > 100 y maneja reintentos.
    
    :param token: Token de autenticación Bearer.
    :return: Lista de diccionarios con {id, name, price}.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    timeout = 10.0  # 10 segundos de timeout

    for attempt in range(max_attempts):
        try:
            # Usamos un contexto para asegurar el cierre de la conexión
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                
                # Lanza una excepción si el código de estado HTTP es 4xx o 5xx
                response.raise_for_status() 
                
                data = response.json()
                
                # Manejo flexible de la estructura del JSON (si es lista o dict con key 'products')
                products = data if isinstance(data, list) else data.get("products", [])

                # Filtrar productos con precio > 100 y mapear a la estructura solicitada
                result = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]
                
                return result

        except (httpx.TimeoutException, httpx.RequestError) as e:
            # Manejo de errores de red y timeout
            if attempt < max_attempts - 1:
                # Backoff exponencial: 2^0=1s, 2^1=2s, 2^2=4s
                wait_time = 2 ** attempt
                print(f"Intento {attempt + 1} fallido. Reintentando en {wait_time}s... Error: {e}")
                time.sleep(wait_time)
            else:
                raise RuntimeError(f"Error de red o timeout tras {max_attempts} intentos: {e}")
                
        except (httpx.HTTPStatusError, ValueError, KeyError) as e:
            # Manejo de errores de respuesta HTTP (ej. 401 Unauthorized, 404 Not Found)
            # o errores al parsear el JSON / acceder a las llaves.
            raise RuntimeError(f"Error al procesar la respuesta de la API: {e}")
```

### Características de la implementación:
1. **Autenticación y Petición:** Se inyecta el `Bearer token` en los headers y se hace la petición GET.
2. **Timeout:** Se configura un cliente `httpx` con un límite de 10 segundos (`timeout=10.0`).
3. **Filtro y Mapeo:** Se utiliza una *list comprehension* para iterar los productos, verificar que el precio sea numérico y mayor a 100, y construir el diccionario exacto `{id, name, price}`.
4. **Manejo de Errores:** 
   - `httpx.TimeoutException` y `httpx.RequestError` capturan problemas de red y de tiempo de espera agotado.
   - `httpx.HTTPStatusError` (lanzado por `raise_for_status()`) captura respuestas HTTP erroneas (4xx, 5xx).
5. **Retry con Backoff Exponencial:** Si ocurre un error de red o timeout, el código espera `1s`, luego `2s`, y luego `4s` antes de fallar definitivamente tras el tercer intento (`2 ** attempt`).