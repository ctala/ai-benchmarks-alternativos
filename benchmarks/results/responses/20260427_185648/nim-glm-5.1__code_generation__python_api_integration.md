# GLM 5.1 (NIM) — code_generation/python_api_integration

- model_id: `z-ai/glm-5.1`
- success: True  | final: 7.4 | quality: 9.72
- latency_total: 102.235s | tokens_per_second: 10.3
- input_tokens: 108 | output_tokens: 1050
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la función implementada con `httpx`, incluyendo retry con backoff exponencial, manejo de timeouts, autenticación Bearer y el filtrado/mapeo solicitado:

```python
import httpx
import time

def get_expensive_products(bearer_token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra los de precio > 100 y retorna 
    una lista de diccionarios con {id, name, price}.
    
    Incluye retry con backoff exponencial (max 3 intentos) y manejo de errores.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_retries = 3
    timeout = 10.0

    for attempt in range(max_retries):
        try:
            # Se usa httpx.Client para manejar la conexión y el timeout
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                
            # Lanza una excepción si el status code es 4xx o 5xx
            response.raise_for_status()
            
            # Parsear la respuesta JSON
            products = response.json()
            
            # Filtrar precio > 100 y mapear a solo {id, name, price}
            filtered_products = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > 100
            ]
            
            return filtered_products

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            # Manejo específico de errores de red y timeout
            if attempt < max_retries - 1:
                # Backoff exponencial: 2^intento * 0.5 (1s, 2s, 4s...)
                wait_time = (2 ** attempt) * 0.5
                time.sleep(wait_time)
                continue
            else:
                # Si se agotan los reintentos, lanzamos la excepción
                raise RuntimeError(f"Error de red/timeout tras {max_retries} intentos: {e}")
                
        except httpx.HTTPStatusError as e:
            # Si es un error de estado (ej. 401 Unauthorized, 404, 500), 
            # normalmente no tiene sentido reintentar con backoff, así que fallamos rápido.
            raise RuntimeError(f"Error HTTP {e.response.status_code}: {e}")
            
        except (KeyError, ValueError) as e:
            # Manejo por si la respuesta JSON no tiene los campos esperados o no es JSON válido
            raise ValueError(f"Error procesando los datos de la API: {e}")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    TOKEN = "tu_token_secreto_aqui"
    try:
        result = get_expensive_products(TOKEN)
        print(f"Productos encontrados: {len(result)}")
        for prod in result:
            print(prod)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
```

### Detalles de la implementación:

1. **Autenticación Bearer**: Se inyecta en el header `Authorization` con el formato estándar `Bearer <token>`.
2. **Timeout (10s)**: Se configura el parámetro `timeout=10.0` en el cliente de `httpx`. Esto cubre tanto el tiempo de conexión como el de lectura.
3. **Filtrado y formato**: Uso de *list comprehension* para iterar la respuesta, filtrar usando `.get("price", 0)` (para evitar errores si un producto no tiene la clave precio) y construir el diccionario exacto con `id`, `name` y `price`.
4. **Manejo de errores**: 
   - `httpx.TimeoutException` y `httpx.NetworkError` capturan problemas de red y tiempo de espera agotado.
   - `httpx.HTTPStatusError` captura respuestas del servidor tipo 4xx o 5xx (activado por `response.raise_for_status()`). En este caso, no se hace retry porque los errores HTTP generalmente indican un problema lógico (como credenciales malas o un endpoint roto), no un problema transitorio de red.
   - `ValueError` y `KeyError` protegen contra respuestas JSON inesperadas o malformadas.
5. **Retry y Backoff Exponencial**: Si hay un error de red o timeout, el código espera `(2 ** attempt) * 0.5` segundos (es decir, 0.5s, 1s, 2s) antes de reintentar, hasta un máximo de 3 veces. Si falla la 3ra vez, lanza un `RuntimeError`.