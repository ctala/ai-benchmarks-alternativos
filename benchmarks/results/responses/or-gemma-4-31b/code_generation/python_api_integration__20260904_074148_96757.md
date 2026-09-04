# Gemma 4 31B — code_generation/python_api_integration

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.62 | quality: 9.72
- latency_total: 42.001s | tokens_per_second: 42.8
- input_tokens: 119 | output_tokens: 1797
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

Para implementar esta funcionalidad con `httpx`, la mejor práctica es utilizar un cliente (`httpx.Client`) y manejar las excepciones específicas de la librería.

Aquí tienes el código completo y detallado:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10.0

    with httpx.Client() as client:
        for attempt in range(max_retries):
            try:
                # 1. GET con autenticación y timeout
                response = client.get(url, headers=headers, timeout=timeout)
                
                # Lanza excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                # Si llegamos aquí, la petición fue exitosa
                products = response.json()
                
                # 2 y 3. Filtrar precio > 100 y retornar solo {id, name, price}
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]} 
                    for p in products 
                    if p.get("price", 0) > 100
                ]

            except (httpx.ConnectError, httpx.TimeoutException, httpx.HTTPStatusError) as e:
                # Solo reintentamos si es un error de red, timeout o error de servidor (5xx)
                # Si es un error de cliente (4xx), no tiene sentido reintentar
                is_server_error = isinstance(e, httpx.HTTPStatusError) and e.response.is_server_error
                is_network_error = isinstance(e, (httpx.ConnectError, httpx.TimeoutException))

                if (is_server_error or is_network_error) and attempt < max_retries - 1:
                    # 5. Backoff exponencial: 1s, 2s, 4s...
                    wait_time = 2 ** attempt 
                    print(f"Error detectando: {e}. Reintentando en {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                
                # Si agotamos los intentos o es un error 4xx, lanzamos la excepción
                print(f"Error fatal o máximo de reintentos alcanzado: {e}")
                raise e

# Ejemplo de uso
if __name__ == "__main__":
    try:
        token_usuario = "tu_token_aqui"
        resultado = get_expensive_products(token_usuario)
        print(resultado)
    except Exception as ex:
        print(f"La función falló: {ex}")
```

### Explicación de los puntos clave:

1.  **`httpx.Client()`**: Se utiliza un gestor de contexto (`with`) para asegurar que las conexiones se cierren correctamente y sea más eficiente que llamar a `httpx.get` repetidamente.
2.  **Manejo de Errores**: 
    *   `response.raise_for_status()`: Convierte códigos de respuesta como 404 o 500 en excepciones (`HTTPStatusError`).
    *   Se capturan específicamente `ConnectError` y `TimeoutException` para cubrir fallos de red.
3.  **Lógica de Reintentos (Retry & Backoff)**:
    *   Se usa un bucle `for` hasta `max_retries`.
    *   **Backoff Exponencial**: `2 ** attempt` hace que el tiempo de espera crezca exponencialmente (0s $\to$ 1s $\to$ 2s), evitando saturar el servidor si este está caído.
    *   **Filtro de Errores**: El código distingue entre errores 4xx (como "No autorizado" o "No encontrado"), donde reintentar sería inútil, y errores 5xx o de red, donde el reintento es válido.
4.  **Filtrado y Transformación**:
    *   Se utiliza una **list comprehension** para filtrar (`if p.get("price", 0) > 100`) y mapear los campos requeridos en un solo paso, lo cual es muy eficiente en Python.
5.  **Timeout**: Se define explícitamente en `10.0` segundos según el requerimiento.