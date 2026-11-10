# Gemini 3.1 Flash Lite (GA) — code_generation/python_api_integration

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 8.87 | quality: 9.48
- latency_total: 2.866s | tokens_per_second: 252.2
- input_tokens: 104 | output_tokens: 723
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

Para implementar esto usando `httpx` con reintentos y backoff exponencial, la forma más eficiente y limpia es utilizar la clase `httpx.Client` junto con un bloque `try-except`.

Aquí tienes la solución:

```python
import httpx
import time
import asyncio

def get_expensive_products(token: str):
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    backoff_factor = 1  # segundos iniciales
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                
                # Lanza excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                data = response.json()
                
                # Filtrar y transformar
                filtered_data = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in data 
                    if p.get("price", 0) > 100
                ]
                
                return filtered_data

        except (httpx.HTTPStatusError, httpx.RequestError) as e:
            print(f"Intento {attempt + 1} fallido: {e}")
            if attempt < max_retries - 1:
                # Backoff exponencial: 1s, 2s, 4s...
                time.sleep(backoff_factor * (2 ** attempt))
            else:
                print("Se agotaron los intentos.")
                raise e

# Ejemplo de uso:
# products = get_expensive_products("tu_token_aqui")
```

### Puntos clave de la implementación:

1.  **`httpx.Client`**: Se utiliza como gestor de contexto (`with`) para asegurar que las conexiones se cierren correctamente después de la petición.
2.  **`timeout=10.0`**: Definido directamente en el cliente para cubrir tanto la conexión como la lectura de datos.
3.  **Manejo de errores**:
    *   `httpx.RequestError`: Captura problemas de red (DNS, conexión rechazada, timeout).
    *   `httpx.HTTPStatusError`: Captura errores de la API (404, 500, etc.) gracias a `raise_for_status()`.
4.  **Reintentos con Backoff**:
    *   Utiliza un bucle `for` simple.
    *   `time.sleep(backoff_factor * (2 ** attempt))` genera la espera exponencial:
        *   Intento 1 fallido: espera $1 * 2^0 = 1$ segundo.
        *   Intento 2 fallido: espera $1 * 2^1 = 2$ segundos.
5.  **Filtrado**: Se utiliza una *list comprehension* que extrae únicamente las claves solicitadas (`id`, `name`, `price`) solo para aquellos productos que cumplen la condición `price > 100`.