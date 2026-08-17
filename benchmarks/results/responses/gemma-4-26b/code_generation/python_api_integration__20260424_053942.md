# Gemma 4 26B MoE (3.8B activos) — code_generation/python_api_integration

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.7 | quality: 9.72
- latency_total: 19.271s | tokens_per_second: 55.1
- input_tokens: 117 | output_tokens: 1061
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para resolver este problema, utilizaremos la librería `httpx`. Para implementar el **backoff exponencial** sin dependencias externas adicionales (como `tenacity`), implementaremos un bucle manual que gestione los reintentos y el tiempo de espera.

Aquí tienes el código completo y profesional:

```python
import httpx
import time
import asyncio

async def get_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna campos específicos.
    Implementa retry con backoff exponencial y manejo de errores.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    timeout = 10.0  # segundos
    
    # Configuración de la petición
    # Usamos un cliente para aprovechar el pool de conexiones
    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = await client.get(url, headers=headers)
                
                # Levanta excepción si el status es 4xx o 5xx
                response.raise_for_status()
                
                # Si llegamos aquí, la petición fue exitosa
                products = response.json()
                
                # 2. Filtrar productos con precio > 100
                # 3. Retornar lista de dicts con {id, name, price}
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

            except (httpx.ConnectError, httpx.TimeoutException, httpx.HTTPStatusError) as e:
                # 4 & 5. Manejo de errores y lógica de Retry
                wait_time = 2 ** attempt  # Backoff exponencial: 1s, 2s, 4s...
                
                print(f"Intento {attempt + 1} fallido: {e}")
                
                if attempt == max_retries - 1:
                    print("Se alcanzaron el máximo de reintentos.")
                    raise e
                
                print(f"Reintentando en {wait_time} segundos...")
                await asyncio.sleep(wait_time)
                
            except Exception as e:
                # Errores inesperados (ej. error de parseo JSON) no se reintentan
                print(f"Error inesperado: {e}")
                raise e

    return []

# --- Ejemplo de uso ---
if __name__ == "__main__":
    TOKEN = "tu_token_aqui"
    
    try:
        # Ejecutamos la función asíncrona
        result = asyncio.run(get_expensive_products(TOKEN))
        print("Productos filtrados:", result)
    except Exception as err:
        print(f"La operación falló definitivamente: {err}")
```

### Explicación técnica:

1.  **`httpx.AsyncClient`**: Se utiliza la versión asíncrona para no bloquear el hilo principal, lo cual es la mejor práctica en Python moderno para operaciones de I/O.
2.  **Backoff Exponencial**: Se calcula con `2 ** attempt`. 
    *   Intento 0 falla $\rightarrow$ espera $2^0 = 1$ seg.
    *   Intento 1 falla $\rightarrow$ espera $2^1 = 2$ seg.
    *   Intento 2 falla $\rightarrow$ espera $2^2 = 4$ seg.
3.  **Manejo de Errores**:
    *   `httpx.TimeoutException`: Captura si la API tarda más de 10s.
    *   `httpx.ConnectError`: Captura problemas de red/DNS.
    *   `httpx.HTTPStatusError`: Captura errores de servidor (500) o cliente (401, 404) mediante `raise_for_status()`.
4.  **List Comprehension**: Se utiliza una sola línea eficiente para filtrar los productos y transformar la estructura de los diccionarios al mismo tiempo, cumpliendo el requisito de retornar solo `{id, name, price}`.
5.  **Seguridad de datos**: Se usa `p.get("price", 0)` para evitar que la función falle si algún producto de la API viene con el campo `price` ausente o nulo.