# GLM 5 — code_generation/python_api_integration

- model_id: `z-ai/glm-5`
- success: True  | final: 8.35 | quality: 9.72
- latency_total: 43.142s | tokens_per_second: 63.9
- input_tokens: 106 | output_tokens: 2757
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la función implementada con `httpx`, cumpliendo todos los requisitos solicitados:

```python
import httpx
import time

def get_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra los que tienen precio > 100,
    y retorna una lista de diccionarios con id, name y price.
    Incluye manejo de errores, timeout y retry con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout_config = httpx.Timeout(10.0) # 10 segundos de timeout
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            # Realizamos la petición GET
            response = httpx.get(url, headers=headers, timeout=timeout_config)
            
            # Lanzamos excepción si la respuesta es un error HTTP (4xx o 5xx)
            response.raise_for_status()
            
            # Parseamos el JSON
            products = response.json()
            
            # Filtramos (precio > 100) y mapeamos el resultado
            # Usamos .get('price', 0) para evitar KeyError si algún producto no tiene precio
            filtered_products = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p.get("price", 0) > 100
            ]
            
            return filtered_products

        except (httpx.NetworkError, httpx.TimeoutException) as e:
            # Errores de red y timeout: son recuperables, aplicamos retry
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Backoff exponencial: 1s, 2s, 4s
                print(f"Error de red/timeout. Intento {attempt + 1} de {max_retries}. Reintentando en {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"Máximo de reintentos alcanzado. Error: {e}")
                # Retornamos lista vacía o podrías relanzar la excepción (raise) dependiendo de tu caso de uso
                return []
                
        except httpx.HTTPStatusError as e:
            # Errores de estado HTTP (ej. 401 Unauthorized, 404 Not Found, 500 Server Error)
            # Normalmente no tiene sentido hacer retry en 4xx, pero sí en algunos 5xx.
            # Por seguridad, interrumpimos el proceso si es un error de estado.
            print(f"Error HTTP irrecuperable: {e.response.status_code}")
            return []
            
        except (KeyError, TypeError) as e:
            # Error en la estructura de los datos devueltos por la API
            print(f"Error procesando los datos de la API: {e}")
            return []

# --- Ejemplo de uso ---
if __name__ == "__main__":
    mi_token = "tu_token_super_secreto_aqui"
    resultados = get_expensive_products(mi_token)
    print(f"Productos encontrados: {resultados}")
```

### Detalles de la implementación:

1. **Autenticación y Timeout**: Se inyecta el `Bearer token` en los headers y se configura `httpx.Timeout(10.0)` que cubre conexión, lectura y escritura.
2. **Filtrado y Mapeo**: Uso *list comprehension* para hacer el filtrado y la transformación en un solo paso limpio. Uso `.get("price", 0)` para evitar que la aplicación se rompa si la API envía un producto sin la llave `price`.
3. **Manejo de errores**: 
   * `httpx.NetworkError` y `httpx.TimeoutException` capturan los problemas de conectividad solicitados.
   * `httpx.HTTPStatusError` captura códigos de estado fallidos (gracias a `response.raise_for_status()`).
4. **Retry y Backoff Exponencial**: El bucle `for attempt in range(max_retries)` se ejecuta máximo 3 veces. Si falla por red/timeouts, espera `2 ** attempt` segundos (1s, 2s, 4s respectivamente) antes de reintentar. Si se acaba el número de intentos, maneja la excepción devolviendo una lista vacía.