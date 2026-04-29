# GLM 5 (NIM) — code_generation/python_api_integration

- model_id: `z-ai/glm5`
- success: True  | final: 7.3 | quality: 9.44
- latency_total: 96.857s | tokens_per_second: 12.3
- input_tokens: 108 | output_tokens: 1190
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes la función implementada con `httpx`, incluyendo todas las solicitudes: manejo de Bearer token, filtrado, manejo de errores, timeout y retry con backoff exponencial implementado manualmente (sin librerías externas adicionales como `tenacity`).

```python
import httpx
import time

def get_expensive_products(bearer_token: str) -> list[dict]:
    """
    Obtiene productos con precio > 100 de la API, con retry y backoff exponencial.
    
    :param bearer_token: Token de autenticación Bearer.
    :return: Lista de diccionarios con {id, name, price}
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_retries = 3
    timeout = 10.0

    for attempt in range(max_retries):
        try:
            # Usamos httpx con timeout
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                
            # Lanza una excepción si el código de estado es 4xx o 5xx
            response.raise_for_status()
            
            # Parsear el JSON
            data = response.json()
            
            # Filtrar precio > 100 y retornar solo {id, name, price}
            filtered_products = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in data
                if p.get("price", 0) > 100
            ]
            
            return filtered_products

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            # Manejo de errores de red y timeout
            print(f"Intento {attempt + 1} fallido por error de red/timeout: {e}")
            
            # Si ya alcanzamos el máximo de reintentos, lanzamos la excepción
            if attempt == max_retries - 1:
                print("Máximo de reintentos alcanzado. Abortando.")
                raise
            
            # Backoff exponencial: 2^0=1s, 2^1=2s, 2^2=4s
            wait_time = 2 ** attempt
            print(f"Esperando {wait_time} segundos antes de reintentar...")
            time.sleep(wait_time)
            
        except httpx.HTTPStatusError as e:
            # Si es un error de estado (ej. 401 Unauthorized, 404, 500), 
            # normalmente no tiene sentido reintentar con backoff a menos que sea 5xx.
            # Aquí lo manejamos separando los errores de servidor (reintento) de los de cliente (no reintento).
            if e.response.status_code >= 500 and attempt < max_retries - 1:
                print(f"Intento {attempt + 1} fallido por error de servidor ({e.response.status_code}). Reintentando...")
                wait_time = 2 ** attempt
                time.sleep(wait_time)
                continue
            
            # Si es un 4xx o ya agotamos los reintentos por 5xx, lanzamos la excepción
            print(f"Error HTTP irrecuperable: {e}")
            raise
            
        except (KeyError, TypeError, ValueError) as e:
            # Manejo de errores si el JSON no tiene la estructura esperada o es inválido
            print(f"Error procesando los datos de la API: {e}")
            raise

# --- Ejemplo de uso ---
# products = get_expensive_products("tu_token_super_secreto_aqui")
# print(products)
```

### Detalles de la implementación:

1. **Autenticación Bearer**: Se inyecta directamente en el diccionario `headers` con el formato estándar `Authorization: Bearer <token>`.
2. **Filtrado y formato**: Se usa una *list comprehension* que primero verifica `p.get("price", 0) > 100` (usando `.get` por si algún producto no tiene la clave `price`) y luego crea el diccionario estrictamente con las claves `id`, `name` y `price`.
3. **Timeout (10s)**: Se pasa el argumento `timeout=10.0` al instanciar `httpx.Client()`. Esto cubre tanto el tiempo de conexión como el de lectura.
4. **Errores de red y timeout**: Se capturan explícitamente `httpx.TimeoutException` y `httpx.NetworkError`, que son las excepciones padre que `httpx` utiliza para este tipo de fallos.
5. **Retry con Backoff Exponencial**: 
   - Se usa un bucle `for attempt in range(max_retries)`.
   - El tiempo de espera se calcula como `2 ** attempt` (1s en el primer reintento, 2s en el segundo, 4s en el tercero).
   - Si se alcanza el máximo de intentos, se relanza la excepción (`raise`) para que el llamador sepa que falló definitivamente.
6. **Errores HTTP (4xx/5xx)**: Se añade una lógica inteligente para `HTTPStatusError`. Si la API responde con un error de cliente (ej. 401, 403, 404), reintentar no tiene sentido, así que falla inmediatamente. Si responde con un error de servidor (5xx), entra en la lógica de reintento.