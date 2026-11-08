# Nemotron 3.5 Lightning — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.34 | quality: 9.72
- latency_total: 3.726s | tokens_per_second: 293.6
- input_tokens: 118 | output_tokens: 1094
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

Aquí tienes la función implementada en Python utilizando `httpx`. Cumple con todos los requisitos especificados: autenticación Bearer, filtrado de precios, estructura de retorno específica, manejo de errores y retry con backoff exponencial.

```python
import httpx
import asyncio
from typing import List, Dict

async def get_expensive_products() -> List[Dict]:
    """
    Realiza una petición GET a la API con autenticación Bearer,
    filtra productos con precio > 100 y retorna una lista de diccionarios
    con id, name y price.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": "Bearer token_ejemplo"} # Se asume el token aquí, 
    # en un caso real se pasaría como parámetro o se obtendría de un gestor de secretos.
    
    max_retries = 3
    timeout = httpx.Timeout(10.0) # Timeout de 10 segundos

    for attempt in range(1, max_retries + 1):
        try:
            # Usamos async with para la sesión y el cliente httpx
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers, timeout=timeout)
                
                # Lanza una excepción si el código de estado es 4xx o 5xx
                response.raise_for_status()
                
                # Procesamos los datos
                products = response.json()
                
                # Filtramos productos con precio > 100
                # Asumimos que el precio viene en el campo 'price'
                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                
                return filtered_products

        except httpx.TimeoutException:
            # Manejo específico de timeouts
            if attempt < max_retries:
                wait_time = 2 ** (attempt - 1) # Backoff exponencial: 1s, 2s
                print(f"Timeout en intento {attempt}. Reintentando en {wait_time}s...")
                await asyncio.sleep(wait_time)
            else:
                print("Error: Se agotaron los intentos por timeout.")
                return []

        except httpx.HTTPStatusError as e:
            # Manejo de errores HTTP (401, 404, 500, etc.)
            print(f"Error HTTP {e.response.status_code}: {e}")
            # Generalmente no se reintenta errores de cliente (4xx) a menos que sea 429
            if e.response.status_code in [429, 500, 502, 503, 504] and attempt < max_retries:
                 wait_time = 2 ** (attempt - 1)
                 print(f"Reintentando en {wait_time}s...")
                 await asyncio.sleep(wait_time)
            else:
                return []

        except httpx.RequestError as e:
            # Manejo de errores de red (DNS failure, connection refused, etc.)
            print(f"Error de red: {e}")
            if attempt < max_retries:
                wait_time = 2 ** (attempt - 1)
                print(f"Reintentando en {wait_time}s...")
                await asyncio.sleep(wait_time)
            else:
                return []

    return [] # Retorna lista vacía si fallan todos los intentos
```

### Explicación de los puntos clave:

1.  **Autenticación Bearer**: Se incluye el encabezado `{"Authorization": "Bearer token_ejemplo"}` en la llamada `client.get`.
2.  **Filtrado**: Se utiliza una lista comprehension para iterar sobre los productos y crear nuevos diccionarios `{id, name, price}` solo aquellos donde `price > 100`.
3.  **Manejo de Errores y Timeout**:
    *   `httpx.Timeout(10.0)`: Establece un límite de 10 segundos para la conexión y lectura.
    *   `try/except`: Captura `TimeoutException`, `HTTPStatusError` (códigos 4xx/5xx) y `RequestError` (problemas de conexión).
4.  **Retry con Backoff Exponencial**:
    *   El bucle `for attempt in range(1, max_retries + 1)` controla los 3 intentos.
    *   El cálculo `wait_time = 2 ** (attempt - 1)` genera los tiempos de espera: Intento 1 -> 1s, Intento 2 -> 2s, Intento 3 -> 4s (aunque el último no espera si falla, la lógica común es esperar antes del siguiente intento).
    *   Se utiliza `await asyncio.sleep(wait_time)` para pausar la ejecución entre reintentos.