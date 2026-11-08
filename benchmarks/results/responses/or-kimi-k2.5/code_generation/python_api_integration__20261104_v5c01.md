# Kimi K2.5 — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.98 | quality: 9.52
- latency_total: 114.739s | tokens_per_second: 31.3
- input_tokens: 115 | output_tokens: 3595
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

Aquí tienes una implementación completa usando solo `httpx` y la librería estándar (`time`). Incluye reintentos con backoff exponencial, manejo de timeouts/errores de red, y filtrado/transformación de la respuesta.

```python
import time
import httpx

def fetch_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos con precio > 100 desde https://api.example.com/products.
    
    Args:
        token: Bearer token para autenticación.
        
    Returns:
        Lista de diccionarios con las claves {id, name, price}.
        
    Raises:
        httpx.HTTPStatusError: Para errores 4xx que no deben reintentarse.
        Exception: Última excepción de red/timeout/5xx si se agotan los 3 intentos.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    timeout = 10.0
    max_retries = 3
    base_delay = 1.0  # segundo(s)
    
    last_exception = None

    for attempt in range(1, max_retries + 1):
        try:
            response = httpx.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            data = response.json()

            # Soporta respuesta como lista directa o {"products": [...]}
            products = data if isinstance(data, list) else data.get("products", [])

            result = []
            for product in products:
                try:
                    price = product["price"]
                    if isinstance(price, (int, float)) and price > 100:
                        result.append({
                            "id": product["id"],
                            "name": product["name"],
                            "price": price,
                        })
                except (KeyError, TypeError):
                    # Ignora productos malformados
                    continue

            return result

        except (
            httpx.TimeoutException,
            httpx.ConnectError,
            httpx.ReadError,
            httpx.WriteError,
            httpx.NetworkError,
        ) as exc:
            # Errores de red/timeout: reintentar con backoff exponencial
            last_exception = exc
            if attempt < max_retries:
                sleep_time = base_delay * (2 ** (attempt - 1))
                time.sleep(sleep_time)
            else:
                break

        except httpx.HTTPStatusError as exc:
            # Reintentar solo en errores del servidor (5xx) o rate limit (429)
            if exc.response.status_code >= 500 or exc.response.status_code == 429:
                last_exception = exc
                if attempt < max_retries:
                    sleep_time = base_delay * (2 ** (attempt - 1))
                    time.sleep(sleep_time)
                else:
                    break
            else:
                # Errores 4xx del cliente no mejoran reintentando
                raise

    # Si salimos del bucle, agotamos los reintentos
    if last_exception:
        raise last_exception

    return []
```

### Características clave

| Requisito | Implementación |
|-----------|----------------|
| **GET con Bearer** | Header `Authorization: Bearer <token>` |
| **Timeout 10s** | `timeout=10.0` en `httpx.get` |
| **Filtro `price > 100`** | Comprensión de lista con validación de tipos |
| **Proyección `{id, name, price}`** | Solo esas 3 claves se incluyen en el resultado |
| **Retry ×3** | Bucle `for attempt in range(1, 4)` |
| **Backoff exponencial** | `sleep_time = 1.0 * (2 ** (attempt - 1))` → esperas de **1s**, **2s** y **4s** |
| **Errores de red** | Captura `TimeoutException`, `ConnectError`, `ReadError`, `WriteError`, `NetworkError` |
| **Sin dependencias extra** | Solo `httpx` (externa) y `time` (stdlib) |

> **Nota:** Si la API devuelve los productos bajo una clave distinta a `products` (por ejemplo, `results` o `data`), ajusta la línea `data.get("products", [])` a la estructura real de la API.