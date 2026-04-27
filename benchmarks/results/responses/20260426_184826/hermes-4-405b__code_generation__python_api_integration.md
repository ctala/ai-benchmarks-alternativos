# Hermes 4 405B — code_generation/python_api_integration

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 7.5 | quality: 9.44
- latency_total: 24.411s | tokens_per_second: 36.5
- input_tokens: 125 | output_tokens: 890
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí está la función Python que cumple con todos los requisitos utilizando la biblioteca httpx:

```python
import httpx

def get_high_value_products(api_token: str) -> list[dict]:
    """
    Fetch products from API, filter by price > 100, and return simplified data.
    
    Handles network errors, timeouts (10 seconds), and implements exponential backoff retry.
    Returns list of {id, name, price} dictionaries.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {api_token}"}
    timeout = 10.0  # 10 seconds timeout
    max_retries = 3
    backoff_factor = 0.5  # Exponential backoff base

    for attempt in range(max_retries):
        try:
            # Create client with timeout
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Raise exception for 4xx/5xx responses

                # Parse and filter products
                products = response.json()
                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                return filtered_products

        except (httpx.NetworkError, httpx.TimeoutException) as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt == max_retries - 1:
                raise  # Re-raise on final attempt
            # Exponential backoff
            sleep_time = backoff_factor * (2 ** attempt)
            httpx.asyncio.sleep(sleep_time)
        except httpx.HTTPStatusError as e:
            print(f"HTTP error {e.response.status_code}: {str(e)}")
            return []  # Return empty list on client errors (4xx)

    return []  # Should never reach here
```

### Características clave:

1. **Autenticación Bearer Token**:
   - Utiliza encabezado de autorización con el token proporcionado
   - `headers = {"Authorization": f"Bearer {api_token}"}`

2. **Filtrado de productos**:
   - Filtra productos con precio > 100
   - Construye nueva lista con solo {id, name, price}
   - `{"id": p["id"], "name": p["name"], "price": p["price"]}`

3. **Manejo de errores**:
   - Captura errores de red (`httpx.NetworkError`)
   - Maneja timeouts (`httpx.TimeoutException`)
   - Captura errores HTTP (4xx/5xx) con `response.raise_for_status()`

4. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Retardo exponencial: `backoff_factor * (2 ** attempt)`
   - Utiliza `httpx.asyncio.sleep()` para retardos

5. **Timeout de 10 segundos**:
   - Establecido en `timeout=10.0`
   - Se aplica tanto al tiempo de conexión como al tiempo de respuesta

### Uso:

```python
try:
    products = get_high_value_products(api_token="tu_token_aquí")
    print(f"Productos encontrados: {len(products)}")
    for p in products:
        print(f"{p['name']} (${p['price']})")
except Exception as e:
    print(f"Error fatal: {str(e)}")
```

### Notas:

- La función devuelve una lista vacía en caso de errores HTTP 4xx (errores del cliente)
- Re-lanza la excepción en el último intento fallido para errores de red/timeouts
- Utiliza un cliente HTTPx con contexto (`with` block) para manejo adecuado de conexiones
- El backoff exponencial aumenta el tiempo de espera entre reintentos: 0.5s, 1s, 2s
- Compatible con Python 3.7+ (sintaxis de anotaciones de tipo)