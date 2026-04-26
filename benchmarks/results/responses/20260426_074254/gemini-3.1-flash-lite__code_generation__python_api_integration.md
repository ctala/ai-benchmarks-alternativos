# Gemini 3.1 Flash Lite — code_generation/python_api_integration

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.87 | quality: 9.48
- latency_total: 3.742s | tokens_per_second: 225.0
- input_tokens: 105 | output_tokens: 842
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para implementar esta solución, utilizaremos `httpx` junto con su capacidad de manejo de excepciones y reintentos.

Aunque `httpx` tiene una funcionalidad de reintento integrada a través de `Transport`, para un control más explícito del **backoff exponencial** (esperar más tiempo entre cada intento), a menudo es más claro usar un bucle simple o la lógica de `urllib3` si estuvieras usando `requests`. Sin embargo, aquí te presento una implementación robusta usando **`httpx`** puro:

```python
import httpx
import time
import asyncio

async def fetch_expensive_products(token: str):
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    
    async with httpx.AsyncClient(timeout=10.0) as client:
        for attempt in range(max_retries):
            try:
                response = await client.get(url, headers=headers)
                response.raise_for_status()  # Lanza error para códigos 4xx/5xx
                
                products = response.json()
                
                # Filtrar y transformar
                result = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                return result

            except (httpx.HTTPStatusError, httpx.RequestError) as e:
                wait_time = 2 ** attempt  # Backoff exponencial: 1, 2, 4 segundos
                print(f"Intento {attempt + 1} fallido: {e}. Reintentando en {wait_time}s...")
                
                if attempt == max_retries - 1:
                    print("Se alcanzó el límite de reintentos.")
                    raise
                
                await asyncio.sleep(wait_time)

# Ejemplo de uso:
# result = asyncio.run(fetch_expensive_products("tu_token_aqui"))
```

### Puntos clave de la implementación:

1.  **`httpx.AsyncClient`**: Es la forma estándar y eficiente de manejar peticiones asíncronas con `httpx`.
2.  **Manejo de errores**:
    *   `httpx.RequestError`: Captura problemas de red (DNS, conexión rechazada, timeout).
    *   `httpx.HTTPStatusError`: Captura errores de respuesta (como 401, 500, etc.) activado por `raise_for_status()`.
3.  **Backoff Exponencial**: Usamos `2 ** attempt` (1, 2, 4 segundos de espera). Esto evita saturar el servidor si este está experimentando problemas.
4.  **Filtrado y Transformación**: Se utiliza una *list comprehension* para realizar el filtrado por precio y la limpieza de los campos de forma eficiente en una sola línea.
5.  **Timeout**: Se define en el constructor del cliente (`timeout=10.0`), cubriendo tanto el tiempo de conexión como el de lectura.

### Consideraciones adicionales:
*   **Dependencias**: Asegúrate de tener instalado `httpx` (`pip install httpx`).
*   **Asincronía**: Esta función es `async`. Si necesitas llamarla desde un entorno sincrónico, usa `asyncio.run(fetch_expensive_products(token))`.
*   **Estructura de datos**: El código asume que la API retorna una lista de objetos JSON. Si la respuesta tiene una estructura diferente (ej. `{"data": [...]}`), deberás ajustar la línea `products = response.json()` para acceder a la clave correcta.