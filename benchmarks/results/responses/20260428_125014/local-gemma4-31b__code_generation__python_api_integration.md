# Gemma 4 31B (DGX Spark Q4_K_M) — code_generation/python_api_integration

- model_id: `gemma4:31b`
- success: True  | final: 7.4 | quality: 9.72
- latency_total: 172.69s | tokens_per_second: 9.4
- input_tokens: 120 | output_tokens: 1617
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para implementar esta funcionalidad siguiendo estrictamente tus requisitos (especialmente el retry con backoff exponencial sin librerías externas como `tenacity`), debemos gestionar el bucle de reintentos y el tiempo de espera manualmente.

Aquí tienes la solución completa:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout_seconds = 10.0

    for attempt in range(max_retries):
        try:
            # Usamos un cliente para manejar la sesión y el timeout
            with httpx.Client(timeout=timeout_seconds) as client:
                response = client.get(url, headers=headers)
                
                # Lanza excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                # Si llegamos aquí, la petición fue exitosa
                products = response.json()
                
                # 2. Filtro precio > 100 y 3. Retorno de campos específicos
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]} 
                    for p in products 
                    if p.get("price", 0) > 100
                ]

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # 4. Manejo de errores de red y timeout
            print(f"Intento {attempt + 1} fallido: {exc}")
            
            # Si es el último intento, lanzamos la excepción
            if attempt == max_retries - 1:
                raise exc
            
            # 5. Retry con backoff exponencial (2^0, 2^1, ...)
            wait_time = 2 ** attempt 
            print(f"Reintentando en {wait_time} segundos...")
            time.sleep(wait_time)

    return []

# --- Ejemplo de uso ---
if __name__ == "__main__":
    try:
        token_usuario = "tu_token_aqui"
        resultado = get_expensive_products(token_usuario)
        print("Productos filtrados:", resultado)
    except Exception as e:
        print(f"Error final tras reintentos: {e}")
```

### Explicación de los puntos clave:

1.  **Autenticación**: Se pasa el token en el encabezado `Authorization` siguiendo el estándar `Bearer <token>`.
2.  **Filtrado y Mapeo**: He utilizado una *list comprehension* que hace dos cosas a la vez: filtra los elementos donde el precio es mayor a 100 y construye un nuevo diccionario solo con las llaves `id`, `name` y `price`.
3.  **Manejo de Errores**: 
    *   `httpx.RequestError`: Captura errores de red, DNS o timeouts.
    *   `httpx.HTTPStatusError`: Captura errores de respuesta del servidor (como 500 Internal Server Error o 404), disparado por `response.raise_for_status()`.
4.  **Timeout**: Se define `timeout=10.0` dentro del cliente para evitar que la petición quede colgada indefinidamente.
5.  **Backoff Exponencial**: 
    *   Se usa un bucle `for` hasta `max_retries`.
    *   La fórmula `2 ** attempt` genera esperas de 1, 2 y 4 segundos respectivamente entre fallos.
    *   Si el último intento falla, la excepción se propaga hacia arriba con `raise exc`.

**Complejidad Temporal:** $O(N)$ donde $N$ es el número de productos devueltos por la API.
**Complejidad Espacial:** $O(M)$ donde $M$ es el número de productos que cumplen la condición de precio.