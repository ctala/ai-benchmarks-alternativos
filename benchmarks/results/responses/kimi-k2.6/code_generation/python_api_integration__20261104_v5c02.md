# Kimi K2.6 — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.18 | quality: 9.8
- latency_total: 73.541s | tokens_per_second: 59.6
- input_tokens: 115 | output_tokens: 4385
- judge_score: 5.0 | justificación: 

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

 Aquí tienes una implementación completa usando solo **`httpx`** y la librería estándar:

```python
import random
import time
import httpx

def get_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos desde la API y retorna únicamente los que tienen precio > 100.
    
    Incluye reintentos automáticos (máx. 3) con backoff exponencial + jitter para
    errores de red y timeouts. Si se agotan los intentos, lanza RuntimeError.
    
    Args:
        token: Bearer token para la cabecera Authorization.
        
    Returns:
        Lista de diccionarios con las claves 'id', 'name' y 'price'.
        
    Raises:
        RuntimeError: Si persiste un error de red/timeout tras 3 intentos.
        httpx.HTTPStatusError: Si la API responde con un HTTP 4xx/5xx.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_retries = 3

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                break  # Petición exitosa, salimos del bucle de reintentos
            except (httpx.NetworkError, httpx.TimeoutException) as exc:
                # Último intento fallido: propagamos el error envuelto
                if attempt == max_retries - 1:
                    raise RuntimeError(
                        f"Error de red/timeout persistente tras {max_retries} intentos: {exc}"
                    ) from exc

                # Backoff exponencial con jitter (0-1s) para evitar thundering herd
                backoff = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(backoff)

    # La respuesta puede ser una lista directa o un objeto con clave 'products'
    payload = response.json()
    products = payload if isinstance(payload, list) else payload.get("products", [])

    # Filtrado y proyección de campos
    result = []
    for product in products:
        if not isinstance(product, dict):
            continue
        price = product.get("price", 0)
        if isinstance(price, (int, float)) and price > 100:
            result.append({
                "id": product.get("id"),
                "name": product.get("name"),
                "price": price,
            })

    return result
```

### Características clave

| Requerimiento | Implementación |
|---|---|
| **Autenticación Bearer** | Cabecera `Authorization: Bearer <token>`. |
| **Timeout 10 s** | `httpx.Timeout(10.0)` aplicado al cliente. |
| **Retry ×3** | Bucle `for attempt in range(3)`. |
| **Backoff exponencial** | `sleep_time = 2^attempt + random.uniform(0, 1)` (ej. ~1s, ~2s, ~4s). |
| **Errores de red / timeout** | Captura explícita de `httpx.NetworkError` y `httpx.TimeoutException`. |
| **Errores HTTP** | Se delegan a `raise_for_status()`; **no** se reintentan 4xx/5xx. |
| **Sin dependencias extra** | Solo `httpx` + `random`/`time` de la stdlib. |

### Ejemplo de uso

```python
try:
    products = get_expensive_products(token="mi_api_key_secreta")
    print(products)
    # Salida: [{'id': 42, 'name': 'Auriculares Pro', 'price': 250.0}, ...]
except RuntimeError as e:
    print(f"Fallo de conectividad: {e}")
except httpx.HTTPStatusError as e:
    print(f"Error HTTP de la API: {e}")
```