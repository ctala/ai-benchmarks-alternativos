# Solar Pro 4 — code_generation/python_api_integration

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.69 | quality: 9.52
- latency_total: 13.344s | tokens_per_second: 38.1
- input_tokens: 157 | output_tokens: 509
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



```python
import httpx
import time

def fetch_expensive_products(bearer_token: str) -> list[dict]:
    """
    Fetch products from API, filter by price > 100, and return selected fields.
    
    Args:
        bearer_token: Authentication token for Bearer auth
        
    Returns:
        List of dicts with {id, name, price} for products with price > 100
        
    Raises:
        httpx.HTTPError: If all retry attempts fail
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    timeout = httpx.Timeout(10.0)
    max_retries = 3
    
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                products = response.json()
                
                filtered = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                
                return filtered
                
        except (httpx.HTTPError, httpx.TimeoutException) as e:
            last_exception = e
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
            else:
                raise last_exception
```

**Notas de uso:**

```python
# Ejemplo de uso
try:
    products = fetch_expensive_products("tu_token_aqui")
    print(f"Productos encontrados: {len(products)}")
    for p in products:
        print(f"{p['name']}: ${p['price']}")
except httpx.HTTPError as e:
    print(f"Error al obtener productos: {e}")
```

**Características implementadas:**
- ✅ Autenticación Bearer token
- ✅ Timeout de 10 segundos
- ✅ Filtro precio > 100
- ✅ Retorno solo {id, name, price}
- ✅ Retry con backoff exponencial (2^0, 2^1, 2^2 segundos)
- ✅ Manejo de errores de red y timeout
- ✅ Solo usa httpx (sin dependencias adicionales)